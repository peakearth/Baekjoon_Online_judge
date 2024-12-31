tiger_score = 0
lion_score = 0

for i in range(int(9)):
    usr_input = input()
    if usr_input == "Tiger":
        tiger_score += 1
    elif usr_input == "Lion":
        lion_score += 1

if tiger_score < lion_score:
    print("Lion")
elif tiger_score > lion_score:
    print("Tiger")