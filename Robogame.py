import random

# Game setup
battery_power = 10
robot_inventory = []
zones = {
    "park": ["power cell", "short circuit", "battery pack", "battery pack", "power cell"],
    "factory": ["short circuit", "power cell", "power cell"],
    "city_center": ["battery pack", "short circuit", "short circuit", "power cell"],
    "warehouse": ["power cell", "short circuit"],
}

# Function to display the current status
def display_status():
    print("\nCurrent battery power:", battery_power)
    print("Current zone:", current_zone)
    print("Power cells collected:", robot_inventory.count("power cell"))
    print("Remaining power cells to collect:", sum(1 for zone in zones.values() for item in zone if item == "power cell"))

# Function to move to a different zone and encounter items
def move_to_zone(zone):
    global battery_power, current_zone

    if zone not in zones:
        print("Invalid zone! Please choose a valid zone.")
        return

    # Battery cost for moving between zones
    battery_cost = 1

    # Check battery power
    if battery_power <= 0:
        print("You have no battery power left! Game Over.")
        return

    battery_power -= battery_cost
    current_zone = zone
    print(f"\nMoved to {current_zone}. Battery power is now {battery_power}.")
    encounter_items()

# Function to encounter items in the current zone
def encounter_items():
    global battery_power

    item = random.choice(zones[current_zone])
    print(f"You encountered: {item}")

    if item == "power cell":
        robot_inventory.append(item)
        zones[current_zone].remove(item)  # Remove the collected power cell from the zone
        print("Collected a power cell!")
    elif item == "short circuit":
        battery_loss = random.randint(1, 3)  # Lose 1 to 3 battery power
        battery_power -= battery_loss
        print(f"Encountered a hazard! Lost {battery_loss} battery power.")
    elif item == "battery pack":
        recharge_amount = random.randint(1, 5)  # Recharge 1 to 5 battery power
        battery_power += recharge_amount
        print(f"Found a battery pack! Recharged {recharge_amount} battery power.")

# Function to display the robot's inventory
def display_inventory():
    print("Inventory:", robot_inventory)

# Main game loop
current_zone = "park"

while True:
    display_status()
    
    # Check for game over conditions
    if battery_power <= 0:
        print("Game Over! You ran out of battery power.")
        break
    
    if sum(1 for zone in zones.values() for item in zone if item == "power cell") == 0:
        print("Congratulations! You've collected all power cells!")
        break

    command = input("Enter command to move to a zone (park, factory, city_center, warehouse), 'inventory' to check inventory, or 'quit' to exit: ").lower()

    if command == "quit":
        print("Thanks for playing!")
        break
    elif command == "inventory":
        display_inventory()
    else:
        move_to_zone(command)
