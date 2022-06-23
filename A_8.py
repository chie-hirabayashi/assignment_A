from xml.dom.expatbuilder import FilterVisibilityController


users_info = [["Bob", 79], ["Tom", 59], ["Ken", 61]]
# print(users_info[0][0])

for number in range(0, len(users_info)):
    print(f"Name: {users_info[number][0]}, Age: {users_info[number][1]}")
