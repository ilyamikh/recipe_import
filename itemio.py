import pickle


def save_item(item):
    pickle.dump(item, open("saved_items/" + item.name + ".menuitem", "wb"))
