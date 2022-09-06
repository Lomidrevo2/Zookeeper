# Save the input in this variable
ticket = list(input())
ticket = [int(item) for item in ticket]

# Add up the digits for each half

half1 = ticket[0] + ticket[1] + ticket[2]

half2 = ticket[3] + ticket[4] + ticket[5]

# Thanks to you, this code will work
if half1 == half2:
    print("Lucky")
else:
    print("Ordinary")
