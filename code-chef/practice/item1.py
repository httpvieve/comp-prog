ship_no = int(input())
id_arr = [input() for x in range(ship_no)]
class_arr = []
for id_char in id_arr:
    if id_char == 'b' or id_char == 'B':
        class_arr.append("BattleShip")
    elif id_char == 'c' or id_char == 'C':
        class_arr.append("Cruiser")
    elif id_char == 'd' or id_char == 'D':
        class_arr.append("Destroyer")
    elif id_char == 'f' or id_char == 'F':
        class_arr.append("Frigate")
for ship in class_arr:
    print(ship)

