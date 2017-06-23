# This is the file where you must work. Write code in the functions, create new functions, 
# so they work according to the specification

import csv # for csv usage
import operator # for sorting

# Custom functions
def purge_inventory(loot): # purge the loot list from non items and commas
    purgedloot = []
    for i in loot: 
        if i.isspace(): # delete space only items
            continue
        else:
            purgedloot.append(i)
    purgedloot = list(filter(None, purgedloot)) # purge more...
    purgedloot = list(filter(len, purgedloot))
    purgedloot = list(filter(bool, purgedloot))
    return purgedloot

def longest_key(inventory): # returns longest key length
    maxkeylength = 0
    for k in inventory:
        if len(str(k)) > maxkeylength:
            maxkeylength = len(str(k))
    return maxkeylength

def longest_value(inventory): # returns longest value length
    maxvaluelength = 0
    for v in inventory.values():
        if len(str(v)) > maxvaluelength:
            maxvaluelength = len(str(v))
    return maxvaluelength

# Displays the inventory.
def display_inventory(inventory):
    sumvalues = sum(inventory.values())
    print("Inventory:") # basic inv printing
    for k, v in inventory.items():
        print("{} {}".format(k, v))
    print("Total number of items: {}\n".format(sumvalues))

# Adds to the inventory dictionary a list of items from added_items.
def add_to_inventory(inventory, added_items):
    for k in added_items:
        if k not in inventory: # if its a new item, add a new key to inv
            inventory[k] = 1 # with a staring value 1
        else:
            for i in inventory: # add a value for an existing key 
                if i == k:
                    inventory[i] += 1
    return inventory

# Takes your inventory and displays it in a well-organized table with 
# each column right-justified. The input argument is an order parameter (string)
# which works as the following:
# - None (by default) means the table is unordered
# - "count,desc" means the table is ordered by count (of items in the inventory) 
#   in descending order
# - "count,asc" means the table is ordered by count in ascending order
def print_table(inventory, order=None): # formatted printing
    sumvalues = sum(inventory.values())

    longestk = longest_key(inventory) # for formatting in columns to fit well
    if longestk < len("item name"):
        longest = len("item name")

    longestv = longest_value(inventory) # for formatting in columns
    if longestv < len("count"):
        longestv = len("count")

    maxlinelenght = longestk + longestv + 5 # + 5 spaces for max line length

    invasc = sorted(inventory.items(), key=operator.itemgetter(1)) # asc tuple from inventory
    invdesc = list(reversed(sorted(inventory.items(), key=operator.itemgetter(1)))) # desc tuple from inventory

    print("Inventory:")
    print(" {}    {}".format("count".rjust(longestv), "item name".rjust(longestk)))
    print("{}".format("-" * maxlinelenght))

    if order == None: # if no arg, prints in random order
        for k, v in inventory.items():
            print(" {}    {}".format(str(v).rjust(longestv), str(k).rjust(longestk)))

    elif order == "count,desc": # prints in desc order
        for i in invdesc:
            print(" {}    {}".format(str(i[1]).rjust(longestv), str(i[0]).rjust(longestk)))
            
    elif order == "count,asc": # prints in asc order
        for i in invasc:
            print(" {}    {}".format(str(i[1]).rjust(longestv), str(i[0]).rjust(longestk)))

    print("{}".format("-" * maxlinelenght))
    print("Total number of items: {}\n".format(sumvalues))

# Imports new inventory items from a file
# The filename comes as an argument, but by default it's 
# "import_inventory.csv". The import automatically merges items by name.
# The file format is plain text with comma separated values (CSV).
def import_inventory(inventory, filename=None):
    if filename == None:
        f = open("import_inventory.csv", "r") # if no arg, open import_inventory.csv file
        file = f.read()
        newloot = file.split(",") # split by commas
        newloot = purge_inventory(newloot) # purge loots
        add_to_inventory(inventory, newloot) # add new loots
        f.close()
    else:
        f = open(filename, "r") # open user given file
        file = f.read()
        newloot = file.split(",") # split by commas
        newloot = purge_inventory(newloot) # purge loots
        add_to_inventory(inventory, newloot) # add new loots
        f.close()
    return inventory

# Exports the inventory into a .csv file.
# if the filename argument is None it creates and overwrites a file
# called "export_inventory.csv". The file format is the same plain text 
# with comma separated values (CSV).
def export_inventory(inventory, filename=None):
    listforcsv = []
    defaultfile = "export_inventory.csv" # default file name for export

    for k, v in inventory.items(): # create a list from inv for csv
        for i in range(v):
            listforcsv.append(str(k))    
    listforcsv = ",".join(listforcsv) # join items with commas

    if filename == None:
        f = open(defaultfile, "w") # write to default csv file
    else:
        f = open(filename, "w") # write to user given filename

    f.write(listforcsv)
    f.close()