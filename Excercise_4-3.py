# เกมค้นหาสมบัติ

row1 = ["⬜️","⬜️","⬜️"]
row2 = ["⬜️","⬜️","⬜️"]
row3 = ["⬜️","⬜️","⬜️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")

position_1 = int(position[0])
position_2 = int(position[1])

choose = map[position_1 - 1]
choose[position_2 - 1] = "X"

print(f"{row1}\n{row2}\n{row3}")