import getcsv, sys, parsecsv, pickle, os, itemio, menuobjects


folder = sys.argv[1]
raw = getcsv.load_data(folder)
recipies = getcsv.parse_rows(raw)
list = parsecsv.parse(recipies)

for item in list:
    itemio.save_item(item)

sample_item = pickle.load(open("saved_items/" + "Barley-Soup-B12 (LR1049) - (Barley Soup).menuitem", "rb"))

for file in os.listdir("saved_items"):
    path = "saved_items/" + file
    current_item = pickle.load(open(path, "rb"))
    print(current_item.display_name)
    for contrib in current_item.contributions:
        print("QTY: " + contrib.quantity + "\t" + "TYPE: " + contrib.unit)
    for ingredient in current_item.ingredients:
        print("FOOD: " + ingredient.food, "\n",
              "QTY: " + ingredient.quantity, "\t",
              "UNIT: " + ingredient.unit)
    print("***")

frac = ["1", "1/4"]
contribute1 = menuobjects.Contribution(quantity=str(["1/4"]), unit="Veg-S")
contribute2 = menuobjects.Contribution(quantity=str(frac), unit="Veg-RO")

contriblist = [contribute1, contribute2]

salad = menuobjects.MenuItem(name="The Salad", contributions=contriblist)
print(salad.name)
for contrib in salad.contributions:
    print("QTY: " + contrib.quantity + "\t" + "TYPE: " + contrib.unit)

