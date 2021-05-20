command=""
car_status=""
start_error="Car is already started"
stop_error="Car is already stopped"
##other option instead of using car_status
## started = False
# if started:
#    print("Car is already started")
# if started:
#    print("Car is already started")

while True:
    command = (input(">")).lower()
    if command == "start":
        if command == car_status:
            print(f"{start_error}")
        else:
            print("Car Started")
            car_status = command
    elif command == "stop":
        if command == car_status:
            print(f"{stop_error}")
        else:
            print("Car Stopped")
            car_status = command
    elif command == "help":
        print("""
        start - to start the car
        stop - to stop the car
        quit - to exit""")
    elif command == "quit":
        break
    else:
        print("Sorry, I don't understand that")