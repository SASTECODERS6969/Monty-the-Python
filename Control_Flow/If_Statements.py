a = 45
b = 78
if a > b:
    print("a is greater than b")
else:
    print("b is greater than a")

Marks = 95
if Marks >= 90:
    print("Great")
elif Marks >= 80:
    print("Good")
else:
    print("You need to work hard")

traffic_light = "Blue"
if traffic_light == "Red":
    print("Stop")
elif traffic_light == "Yellow":
    print("Wait")
elif traffic_light == "Blue" or "Green":
    print("Go")
else:
    print("Please enter a valid traffic signal colour!")

friends = ["Bheem", "Chutki", "Raju", "Jaggu"]
i = str(input("Please enter a name of a friend"))
for a in friends:
    if a == i:
        print("True")
    else:
        print("This is false")