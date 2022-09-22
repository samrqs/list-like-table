linha1 = ["😁","😁","😁"]
linha2 = ["😁","😁","😁"]
linha3 = ["😁","😁","😁"]
map = [linha1, linha2, linha3]
print(f"{linha1}\n{linha2}\n{linha3}")

position = input("Escolha a linha e coluna respectivamente para alterar o emoji: (ex: 23)  ")

horizontal = int(position[0])
vertical = int(position[1])

map[vertical - 1][horizontal - 1] = "🤯"

print(f"{linha1}\n{linha2}\n{linha3}")