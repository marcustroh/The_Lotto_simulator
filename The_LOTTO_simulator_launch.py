import random

i = 1
user_num_list =[]
while i < 7:
    try:
        choice = int(input(f"Choose the number {i}: "))
        if choice > 49:
            print("Number too high - please enter a number in range 1-49")
        elif choice < 1:
            print("Number too low - please enter a number in range 1-49")
        else:
            if choice in user_num_list:
                print(f"Number {choice} has been already chosen - select different one")
            else:
                user_num_list.append(choice)
                i = i + 1
    except Exception:
        print("ValueError - please enter a number in range 1-49")

user_num_list.sort()

user_num_list_easytoread = []
for l in user_num_list:
    user_num_list_easytoread.append(str(l))
easytoread_user = ", ".join(user_num_list_easytoread)

j = 1
pc_num_list =[]

while j < 7:
    pc_choice = random.randint(1,49)
    if pc_choice in pc_num_list:
        continue
    else:
        pc_num_list.append(pc_choice)
        j = j + 1

pc_num_list_easytoread = []
for m in pc_num_list:
    pc_num_list_easytoread.append(str(m))
easytoread_pc = ", ".join(pc_num_list_easytoread)

k = 1
shoot = 0
num_exist = True

while k < 7:
    for k in user_num_list:
        if k in pc_num_list:
            shoot = shoot + 1
    k = k + 1

print(f"Drawn numbers: {easytoread_pc}")
print(f"Selected numbers: {easytoread_user}")
if shoot > 2:
    print(f"You hit {shoot} numbers!")
elif shoot == 0:
    print(f"Unfortunately no hits, try again...")
else:
    print(f"You hit {shoot} number!")
