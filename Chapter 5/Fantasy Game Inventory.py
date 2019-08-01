

def displayInventory(inventory):
    for k,v in inventory.items():
        print(str(v)+ " " + k)
    print("Total number of items: {}" .format(sum(inventory.values())))

inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
displayInventory(inventory)
print("######################################")



def add_to_inventory(items,inventory):
    for x in items:
        inventory[x] = inventory.get(x,0)+1

    return inventory
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}


add_to_inventory(dragonLoot,inv)
displayInventory(inv)

