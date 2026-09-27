

time = int(input("Enter in seconds the time"))

seconds_remaining = 600-time

if time > 600:
    print("The time is greater than 10 minutes")

elif time == 600:
    print("The time is equal to 10 minutes")
else:
    print(f"Seconds remaining until 10 minutes: {seconds_remaining} seconds")   