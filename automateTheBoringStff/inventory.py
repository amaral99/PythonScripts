stuff = {'rope': 1,'torch': 6,'gold coin': 42,'dagger': 1,'arrow': 12}

def displayInventory(inventory):
	print('inventory:')
	item_total=0
	for k, v in inventory.items():
		print(str(v) + ' ' + k)
		item_total += v
	print('total number of items: ' + str(item_total))
	
#displayInventory(stuff)

def addToInventory(inventory, addedItems):
	for i in range(len(addedItems)):
	#iterate through loot
		inventory.setdefault(addedItems[i],0)
		#matched whats in inv?0 if nothing?
	
		inventory[addedItems[i]]=inventory[addedItems[i]]+1
		#value is added 
	return inventory
	
inv = {'gold coin': 42,'rope': 1}


dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = addToInventory(inv, dragonLoot)


addToInventory(stuff, dragonLoot)	
displayInventory(stuff)
