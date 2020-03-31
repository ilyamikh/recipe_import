import getcsv, sys, parsecsv, pickle


folder = sys.argv[1]
raw = getcsv.load_data(folder)
recipies = getcsv.parse_rows(raw)
list = parsecsv.parse(recipies)

for item in list:
    pickle.dump(item, open(item.name + ".menuitem", "wb"))

sample_item = pickle.load(open("Barley-Soup-B12 (LR1049) - (Barley Soup).menuitem", "rb"))

print(sample_item.display_name)
