command = ""
while command == "QUIT":
    command = input("> ").lower()
    if command == "START":
        print("CAR STARTED...")
    elif command == "STOP":
        print("CAR STOPPED.")
    elif command == "HELP":
        print("""
        START - TO START THE CAR
        STOP - TO STOP THE CAR
        QUIT - TO QUIT
        """)
    else:
        print("SORRY, I DON'T UNDERSTAND THAT.")
    