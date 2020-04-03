from menuobjects import Ingredient
from menuobjects import Contribution
from menuobjects import MenuItem


def parse(raw_dict):
    """Takes the raw dictionary and returns a lits of initialized MenuItem objects"""
    menuitemlist = []
    for key in raw_dict:
        menuitemlist.append(
           MenuItem(name=key,
                    displayname=displayname(key),
                    servings=servings(raw_dict[key]),
                    servingsize=servingsize(raw_dict[key]),
                    recipeyield=recipeyield(raw_dict[key]),
                    ingredients=ingredients(raw_dict[key]),
                    contributions=contribs(raw_dict[key])
                    )
            )

    return menuitemlist


def displayname(recipename):
    """Returns the display name portion of the recipe name string"""
    wordlist = recipename.split('-')
    displayname = wordlist[-1]  # the last item in the list is the display name in parenthesis
    displayname = displayname.strip()[1:-1]  # remove whitespaces, first and last symbols are parenthesis
    return displayname


def qty(rawstring):
    """Takes the string and returns the quantity portion"""
    res = []
    for item in rawstring.split(' '):
        if len(item):
            res.append(item)  # get rid of empty strings

    return str(res[:-1])


def unit(rawstring):
    """Takes the string and returns the unit portion"""
    strlist = rawstring.split(' ')
    vals = []
    for item in strlist:
        if len(item):
            vals.append(item)  # get rid of blank strings
    res = ''
    for val in vals[-1:]:
        res += val  # in case there are more than 1 str for unit

    return res


def servings(rows):
    """Returns the servings amount from the rows part of csv"""
    return float(rows[1][6])


def servingsize(rows):
    """Returns the serving size from rows as string"""
    return rows[1][7]


def recipeyield(rows):
    """Returns the yield from rows as string"""
    return rows[1][9]


def contribs(rows):
    """Using rows from the csv, parses the contribs field and returns a list"""
    raw = rows[1][5]  # row 2 column 6 is the contributions information
    res = []
    for item in raw.split(','):  # here's hoping they're separated by commas and nothing else
        res.append(Contribution(qty(item), unit(item)))

    return res


def ingredients(rows):
    """Takes the rows portion of the imported csv file, parses the ingredient info, and returns a list of Ingredient
    objects. """
    r = 4  # Row five is where the ingredient count starts
    val = len(rows[r])  # check for blank string
    cnt = int(rows[r][0])  # Hold the number of ingredients here, the count starts at 1
    res = []
    while val:
        res.append(
            Ingredient(
                rows[r][6],  # column 7 is the food name
                qty(rows[r][7]),  # column 8 is the quantity, number comes first
                unit(rows[r][7])
            )
        )
        cnt += 1
        r += 1
        val = len(rows[r])

    return res
