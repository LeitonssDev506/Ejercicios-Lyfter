

age = int(input("Type your age: "))
name = str(input("Type your Name: "))
lastname = str(input("Type your lastname: "))


if age < 0:
        print(f"Hello {name} {lastname}, your {age} is invalid")
elif age <= 2:
        print(f"{name} {lastname} is a baby")
elif age <= 9:
        print(f"{name} {lastname} is a child")
elif age <= 12:
        print(f"{name} {lastname} is a preteen")
elif age <= 17:
        print(f"{name} {lastname} is a teenager")
elif age <= 25:
        print(f"{name} {lastname} is a young adult")
elif age <= 64:
        print(f"{name} {lastname} is an adult")
else:
        print(f"{name} {lastname} is a senior")
