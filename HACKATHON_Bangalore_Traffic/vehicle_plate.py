import matplotlib.pyplot as plt
from collections import Counter
from datetime import timedelta, datetime
import random
import time
from typing import List, Dict, Tuple, Set

# --- Configuration for Plate Generation ---
PLATE_CONFIG = {
    "private": {
        "prefix_chars": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "prefix_len": 2,
        "num_len": 4,
        "suffix_chars": "ABCDEFGHIJKLMNOPQRSTUVWXYZ",
        "suffix_len": 2,
        "format": lambda p, n, s: f"{p}{n}{s}"
    },
    "public_transport": {  # Specific prefixes for public transport
        "prefix_chars": "BUS",
        "prefix_len": 3,
        "num_len": 3,
        "suffix_chars": "",
        "suffix_len": 0,
        "format": lambda p, n, s: f"{p}{n}"
    },
    "emergency_ambulance": {  # Example for ambulance
        "prefix_chars": "AMB",
        "prefix_len": 3,
        "num_len": 3,
        "suffix_chars": "",
        "suffix_len": 0,
        "format": lambda p, n, s: f"{p}{n}"
    },
    "emergency_police": {  # Example for police
        "prefix_chars": "POL",
        "prefix_len": 3,
        "num_len": 3,
        "suffix_chars": "",
        "suffix_len": 0,
        "format": lambda p, n, s: f"{p}{n}"
    },
    "government": {
        "prefix_chars": "GOVT",
        "prefix_len": 4,
        "num_len": 3,
        "suffix_chars": "",
        "suffix_len": 0,
        "format": lambda p, n, s: f"{p}{n}"
    }
}

# --- Plate Generation Function ---
def generate_plate_number(vehicle_type: str = "private", specific_prefix: str = None) -> str:
    """
    Generates a random license plate number based on the specified vehicle type configuration.
    Can also force a specific prefix for certain types (e.g., 'KA' for private).

    Args:
        vehicle_type (str): The type of vehicle (e.g., "private", "public_transport").
        specific_prefix (str, optional): If provided, overrides random prefix generation for this plate.

    Returns:
        str: A generated license plate number.
    """
    config = PLATE_CONFIG.get(vehicle_type)
    if not config:
        raise ValueError(f"Unknown vehicle type: {vehicle_type}")

    if specific_prefix:
        prefix = specific_prefix
    else:
        prefix = "".join(random.choice(config["prefix_chars"]) for _ in range(config["prefix_len"]))

    number = "".join(random.choice("0123456789") for _ in range(config["num_len"]))
    suffix = "".join(random.choice(config["suffix_chars"]) for _ in range(config["suffix_len"]))

    return config["format"](prefix, number, suffix)


# --- Database of ALL Authorized Vehicles (single set) ---
AUTHORIZED_VEHICLES: Set[str] = set()

# Populate AUTHORIZED_VEHICLES with generated plates
def populate_authorized_vehicles(num_each_type: int = 5):
    # Public Transport
    for _ in range(num_each_type):
        AUTHORIZED_VEHICLES.add(generate_plate_number("public_transport", specific_prefix="BUS"))
    # Emergency (Ambulance)
    for _ in range(num_each_type):
        AUTHORIZED_VEHICLES.add(generate_plate_number("emergency_ambulance", specific_prefix="AMB"))
    # Emergency (Police)
    for _ in range(num_each_type):
        AUTHORIZED_VEHICLES.add(generate_plate_number("emergency_police", specific_prefix="POL"))
    # Government
    for _ in range(num_each_type):
        AUTHORIZED_VEHICLES.add(generate_plate_number("government", specific_prefix="GOVT"))

# Call to populate the authorized vehicle set
populate_authorized_vehicles(10)  # Generate 10 plates for each authorized category

# Violation log for fines
VIOLATION_LOG: List[Dict] = []

# Unauthorized vehicle tracking for repeat offenders
UNAUTHORIZED_VEHICLES_DAILY_COUNT: Dict[str, Dict[str, int]] = {}
# Format: { "plate": { "YYYY-MM-DD": count, ... }, ... }

# Fine amounts
FLAT_FINE_AMOUNT = 100
REPEAT_OFFENDER_FINE_AMOUNT = 250
REPEAT_VIOLATION_THRESHOLD = 3  # Number of violations in a day to trigger repeat offender fine

def is_authorized(vehicle_plate: str) -> bool:
    """Check if vehicle is authorized for special lane."""
    return vehicle_plate in AUTHORIZED_VEHICLES

def issue_fine(vehicle_plate: str, timestamp: str, fine_amount: int = FLAT_FINE_AMOUNT) -> None:
    """Issue fine to violator."""
    fine_record = {
        'vehicle_plate': vehicle_plate,
        'timestamp': timestamp,
        'fine_amount': fine_amount,
        'type': 'Flat Fine' if fine_amount == FLAT_FINE_AMOUNT else 'Repeat Offender Fine'
    }
    VIOLATION_LOG.append(fine_record)
    # Production: send notification/email/SMS here

def detect_vehicle_on_lane(vehicle_plate: str, timestamp_str: str) -> None:
    """Process vehicle detected on special lane, log violations, and track unauthorized."""
    timestamp = datetime.strptime(timestamp_str, '%Y-%m-%d %H:%M:%S')
    current_date = timestamp.strftime('%Y-%m-%d')

    if is_authorized(vehicle_plate):
        print(f"Vehicle {vehicle_plate} is authorized at {timestamp_str}.")
    else:
        print(f"Violation: Vehicle {vehicle_plate} is NOT authorized at {timestamp_str}.")
        issue_fine(vehicle_plate, timestamp_str)

        # Track unauthorized vehicle for repeat offenses
        if vehicle_plate not in UNAUTHORIZED_VEHICLES_DAILY_COUNT:
            UNAUTHORIZED_VEHICLES_DAILY_COUNT[vehicle_plate] = {}

        # Increment count for the current day
        UNAUTHORIZED_VEHICLES_DAILY_COUNT[vehicle_plate][current_date] = \
            UNAUTHORIZED_VEHICLES_DAILY_COUNT[vehicle_plate].get(current_date, 0) + 1

        # Check for repeat offender
        if UNAUTHORIZED_VEHICLES_DAILY_COUNT[vehicle_plate][current_date] >= REPEAT_VIOLATION_THRESHOLD:
            print(f"!!! Repeat Offender: Vehicle {vehicle_plate} has violated {UNAUTHORIZED_VEHICLES_DAILY_COUNT[vehicle_plate][current_date]} times today. Implementing a fine of ₹{REPEAT_OFFENDER_FINE_AMOUNT} !!!")
            issue_fine(vehicle_plate, timestamp_str, REPEAT_OFFENDER_FINE_AMOUNT)

def show_violations() -> None:
    """Display all violation logs."""
    print("\n--- Violation Log ---")
    if not VIOLATION_LOG:
        print("No violations recorded.")
        return
    for violation in VIOLATION_LOG:
        print(f"Plate: {violation['vehicle_plate']}, Time: {violation['timestamp']}, Fine: ₹{violation['fine_amount']} ({violation['type']})")

def show_unauthorized_vehicles_summary() -> None:
    """Display a summary of unauthorized vehicles and their daily violation counts."""
    print("\n--- Unauthorized Vehicles Daily Violation Summary ---")
    if not UNAUTHORIZED_VEHICLES_DAILY_COUNT:
        print("No unauthorized vehicles detected.")
        return
    for plate, daily_counts in UNAUTHORIZED_VEHICLES_DAILY_COUNT.items():
        print(f"Vehicle: {plate}")
        for date, count in daily_counts.items():
            print(f"  Date: {date}, Violations: {count}")

def plot_last_week_violations():
    if not VIOLATION_LOG:
        print("No violations to plot.")
        return

    # Extract dates from violation log
    violation_dates = [datetime.strptime(record['timestamp'], '%Y-%m-%d %H:%M:%S').date() for record in VIOLATION_LOG]

    max_date = max(violation_dates)
    start_date = max_date - timedelta(days=6)  # last 7 days including max_date

    # Create date range for the week
    week_dates = [start_date + timedelta(days=i) for i in range(7)]

    # Count violations per day in that week
    counts = Counter(date for date in violation_dates if start_date <= date <= max_date)

    # Prepare data for plotting
    x_labels = [date.strftime('%a %d-%b') for date in week_dates]
    y_values = [counts.get(date, 0) for date in week_dates]

    # Plot bar chart
    plt.figure(figsize=(10, 5))
    plt.bar(x_labels, y_values, color='royalblue')
    plt.title("Vehicle Violations in the Last 7 Days")
    plt.xlabel("Date")
    plt.ylabel("Number of Violations")
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

# --- Simulation ---
if __name__ == '__main__':
    print("--- Initializing Authorized Vehicles ---")
    print("Total Authorized Vehicles:", len(AUTHORIZED_VEHICLES))
    print("Sample Authorized Plates:", list(AUTHORIZED_VEHICLES)[:5])
    print("-" * 40)

    # Generate unauthorized plates for simulation (all private starting with KA)
    random_unauthorized_plates = [generate_plate_number("private", specific_prefix="KA") for _ in range(20)]

    detected_vehicles_for_sim: List[Tuple[str, str]] = []

    # Add some authorized vehicles to the detection list
    authorized_list = list(AUTHORIZED_VEHICLES)
    detected_vehicles_for_sim.append((authorized_list[0], '2025-07-16 09:00:01'))
    detected_vehicles_for_sim.append((authorized_list[1], '2025-07-16 09:01:05'))
    detected_vehicles_for_sim.append((authorized_list[2], '2025-07-16 09:02:10'))

    # Add unauthorized vehicles, including repeats for repeat offender test
    detected_vehicles_for_sim.append((random_unauthorized_plates[0], '2025-07-16 09:03:00'))  # Violation 1
    detected_vehicles_for_sim.append((random_unauthorized_plates[1], '2025-07-16 09:04:15'))
    detected_vehicles_for_sim.append((random_unauthorized_plates[0], '2025-07-16 09:05:00'))  # Violation 2
    detected_vehicles_for_sim.append((random_unauthorized_plates[2], '2025-07-16 09:06:30'))
    detected_vehicles_for_sim.append((random_unauthorized_plates[0], '2025-07-16 09:07:00'))  # Violation 3 - repeat offender fine
    detected_vehicles_for_sim.append((random_unauthorized_plates[3], '2025-07-16 09:08:00'))
    detected_vehicles_for_sim.append((random_unauthorized_plates[0], '2025-07-16 09:09:00'))  # Violation 4 - another repeat fine

    # Add more unauthorized detections on different dates to fill a week
    base_date = datetime.strptime('2025-07-12', '%Y-%m-%d')
    for day_offset in range(7):
        current_date = (base_date + timedelta(days=day_offset)).strftime('%Y-%m-%d')
        for _ in range(random.randint(2, 5)):
            plate = random.choice(random_unauthorized_plates)
            ts = f"{current_date} {random.randint(9, 23):02d}:{random.randint(0,59):02d}:{random.randint(0,59):02d}"  # Correct hour formatting
            detected_vehicles_for_sim.append((plate, ts))

    # Shuffle detections to simulate real random traffic
    random.shuffle(detected_vehicles_for_sim)

    print("\n--- Simulating Vehicle Detections ---")
    for plate, ts in detected_vehicles_for_sim:
        detect_vehicle_on_lane(plate, ts)
        time.sleep(0.01)  # Short delay for simulation

    print()
    show_violations()
    show_unauthorized_vehicles_summary()

    # Plot violations over the last 7 days
    plot_last_week_violations()
