#!/usr/bin/env python3

#The purpose of this script is to use functions 
#to modify items inside a list.

# Author ID: 160682231
#_________________________________________________________________________

# Place my_list below this comment (before the function definitions)
my_list = [ 1,2,3,4,5]



def add_item_to_list(ordered_list):
    # Appends new item to end of list with the value (last item + 1)
    last_number = ordered_list[-1] #create new variable to read the last in the original list
    new_last_number = last_number + 1 #add the new variable by 1
    return ordered_list.append(new_last_number) #append to the end and save to the list

def remove_items_from_list(ordered_list, items_to_remove):
    # Removes all values, found in items_to_remove list, from ordered_list
    for remove_item in items_to_remove:
        # check whether remove_item is in ordered_list, then remove the item ONLY if in the ordered_list
        for original_item in ordered_list: 
            if original_item == remove_item:
                ordered_list.remove (remove_item)


# Main code
if __name__ == '__main__':
    print(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    add_item_to_list(my_list)
    print(my_list)
    remove_items_from_list(my_list, [1,5,6])
    print(my_list)
