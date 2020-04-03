class Ingredient:
    """Object type that contains food name, quantity, and measuring unit"""
    def __init__(self, food, quantity, unit):
        self.food = food
        self.quantity = quantity
        self.unit = unit


class Contribution:
    """Contains data for a single contribution"""
    def __init__(self, quantity, unit):
        self.quantity = quantity
        self.unit = unit


class MenuItem:
    """Object type that will hold data for each menu item"""
    def __init__(self, name, contributions, displayname=None, servings=None, servingsize=None, recipeyield=None, ingredients=None):
        self.name = name
        self.contributions = contributions
        self.display_name = displayname
        self.servings = servings
        self.servingsize = servingsize
        self.recipeyield = recipeyield
        self.ingredients = ingredients



class Meal:
    """Contains a list of MenuItems"""
    def __init__(self, description, mealtype, menuitems):
        self.description = description
        self.mealtype = mealtype
        self.menuitems = menuitems  # list of menuitem objects
        self.reimburse = None
        self.servings = None


class Reimburse:
    """Holds the categories and amounts for a meal"""
    def __init__(self, free, reduced, paid):
        self.free = free
        self.reduced = reduced
        self.paid = paid


class Day:
    """Contains all relevant menu data for a single day"""
    def __init__(self, date, meals):
        self.date = date
        self.meal = meals  # this will be a list of 3 meal objects since python treats lists so casually
