#python 3.7.1

signals = ["red", "yellow", "green"]
vehicle_types = ["car", "bike", "bus", "truck", "pedestrian"]

current_signal = input("Enter the current traffic signal (red/yellow/green): ").lower()

if current_signal in signals and current_signal == signals[0]:  # Red Signal
    vehicle = input(f"Select your vehicle type for {current_signal} signal: ").lower()
    if vehicle == vehicle_types[0]:  # Car
        print("STOP! Wait for the signal to change.")
    elif vehicle == vehicle_types[1]:  # Bike
        print("STOP! It's dangerous to move.")
    elif vehicle == vehicle_types[2]:  # Bus
        print("STOP! Follow the traffic rules.")
    elif vehicle == vehicle_types[3]:  # Truck
        print("STOP! Heavy vehicles must wait.")
    elif vehicle == vehicle_types[4]:  # Pedestrian
        print("CROSS the road carefully.")
    else:
        print("Invalid input.")

elif current_signal == signals[1]:  # Yellow Signal
    vehicle = input(f"Select your vehicle type for {current_signal} signal: ").lower()
    if vehicle == vehicle_types[0]:  # Car
        print("SLOW DOWN! Prepare to stop.")
    elif vehicle == vehicle_types[1]:  # Bike
        print("SLOW DOWN! Be cautious.")
    elif vehicle == vehicle_types[2]:  # Bus
        print("SLOW DOWN! Be ready to stop.")
    elif vehicle == vehicle_types[3]:  # Truck
        print("SLOW DOWN! Trucks take longer to stop.")
    elif vehicle == vehicle_types[4]:  # Pedestrian
        print("WAIT! Do not cross yet.")
    else:
        print("Invalid input.")

elif current_signal == signals[2]:  # Green Signal
    vehicle = input(f"Select your vehicle type for {current_signal} signal: ").lower()
    if vehicle == vehicle_types[0]:  # Car
        print("GO! You can proceed.")
    elif vehicle == vehicle_types[1]:  # Bike
        print("GO! Ride carefully.")
    elif vehicle == vehicle_types[2]:  # Bus
        print("GO! Follow traffic lanes.")
    elif vehicle == vehicle_types[3]:  # Truck
        print("GO! Maintain speed limits.")
    elif vehicle == vehicle_types[4]:  # Pedestrian
        print("STOP! Wait until the signal turns red.")
    else:
        print("Invalid input.")

else:
    print("Invalid signal color. Please enter red, yellow, or green.")