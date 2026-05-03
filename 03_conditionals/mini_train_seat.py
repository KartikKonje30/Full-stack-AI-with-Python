
seat_input = input("Enter the seat type (sleeper/AC/general/luxury)").lower()

match seat_input:
    case "sleeper":
        print("Sleeper - Non AC, beds available")
    case "ac":
        print("AC - Fully Air Conditioned, beds available")
    case "general":
        print("General - General seats, No reservation")
    case "luxury":
        print("Luxury - Fully Air Conditioned, Comfy beds, Free Wifi, Lunch/Dinner Included")
    case _:
        print("Invalid seat type")