
# Ores

tin = 10
iron = 20
lead = 30

mithril = 2000

Ore_Count = input("Enter the amount of Ore: ")
Ore_Value = input("Enter the type of Ore (tin, iron, lead): ")

if Ore_Value == "tin":
    Ore_Value = tin
elif Ore_Value == "iron":
    Ore_Value = iron
elif Ore_Value == "lead":
    Ore_Value = lead
elif Ore_Value == "mithril":
    Ore_Value = mithril
else:
    Ore_Value = 0

Ore_Load = int(Ore_Count) * Ore_Value


# Machines


Ore_Cleaner = 10

Polisher = 10

Ore_Smelter = 10

print(Ore_Load)
