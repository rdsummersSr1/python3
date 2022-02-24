print('1',update)
           i+=1
        elif update.count(item) == 0:
           update += f",'{item}':{quantity} " 
        else:
           pass
    print (update)
    dict_.append(update)
    print(dict_)
   
    c1=Counter(items)
    return dict(c1)  
        
      
 






def add_items(inventory, items):
    """


    :param inventory: dict - dictionary of existing inventory.
    :param items: list - list of items to update the inventory with.
    :return:  dict - the inventory dictionary update with the new items.
    """
    dict_ = []
    update_ = []
    item_add = ''
    print(dict_)
    c1=Counter(items)
    update_ = print(dict(c1))
    quant = 0
    if inventory == {}:
       for item in items:
           quant = items.count(item)
           inventory[item] = quant 
           if inventory != {} :
              inventory[item] = quant 
    else:
        for item_add in c1:
            if inventory.get(item_add, -1) != -1:
               inventory[item_add] = c1[item_add] + inventory[item_add]
            else:
               inventory[item_add] = c1[item_add] 
    return inventory
    




   


    
def decrement_items(inventory, items):
    """


    :param inventory: dict - inventory dictionary.
    :param items: list - list of items to decrement from the inventory.
    :return:  dict - updated inventory dictionary with items decremented.
    """
    dict_ = []
    for item in items:
        if inventory[item] > 0:
           inventory[item] -= 1
        else :
           pass
   
    return inventory
         


        


def remove_item(inventory, item):
    """
    :param inventory: dict - inventory dictionary.
    :param item: str - item to remove from the inventory.
    :return:  dict - updated inventory dictionary with item removed.
    """
    for key, value in inventory.items():
        if key == item:
           inventory.pop(item)
           break
    return inventory






def list_inventory(inventory):
    """


    :param inventory: dict - an inventory dictionary.
    :return: list of tuples - list of key, value pairs from the inventory dictionary.
    """


    output_inventory = [(k, v) for k, v in inventory.items() if inventory[k] > 0]
    return output_inventory