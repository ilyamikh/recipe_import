import getcsv, sys, parsecsv, pickle, os, itemio


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
