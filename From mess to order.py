import xlwings as xw
from os import getcwd
import json

#  The first part of this file will call the Excel file to "sort-it-out"
full_name = getcwd()+'/Scotch_data/Excel_data.xlsx'
app_target = '/Applications/Microsoft Office 2011/Microsoft Excel'

wb = xw.Workbook(fullname=full_name, app_visible=False, app_target=app_target)

grand_scotch_dict = {}
for i in range(3, 112):
    whiskey_dict = {'1. name': xw.Range(1, (i, 1)).value, '2. name': xw.Range(1, (i, 2)).value}  # Insert the names

    whiskey_tuple_float = tuple(xw.Range(1, (i, 3), (i, 70)).value)  # Read the line of attributes i.e. 0 or 1
    whiskey_tuple_integer = tuple([int(x) for x in whiskey_tuple_float])  # Convert to integer tuple
    whiskey_dict['tuple'] = whiskey_tuple_integer  # Insert the tuple in the whiskey_dict

    descriptive_dict = {'color': [], 'nose': [], 'body': [], 'pal': [], 'fin': []}  # Placeholder for the 5 attrib.
    for x in range(3, 71):
        category_name = xw.Range(1, (1, x)).value.lower()
        category_value = xw.Range(1, (2, x)).value.lower()
        attribute_value_int = int(xw.Range(1, (i, x)).value)
        if attribute_value_int == 1:
            categories_list = descriptive_dict[category_name]  # Get the categorys list
            categories_list.append(category_value)  # Append the value
            descriptive_dict[category_name] = categories_list  # Put the new list back in
    whiskey_dict['descriptive'] = descriptive_dict

    grand_scotch_dict[i-2] = whiskey_dict  # Insert the whiskey only with number

### Write dict to txt file
with open("whiskey_dict.txt", "w") as myfile:
    json.dump(grand_scotch_dict, myfile)


'''
categories_dict = {'color': {}, 'nose': {}, 'body': {}, 'pal': {}, 'fin': {}}
categories_dict_original = {'color': {}, 'nose': {}, 'body': {}, 'pal': {}, 'fin': {}}

for i in range(3, 70):
    category_name = xw.Range(1, (1, i)).value.lower()  # get category
    category_value = xw.Range(1, (2, i)).value.lower()  # get value
    categories_value_dict = categories_dict[category_name]  # get the existing dict for the category
    categories_value_dict[category_value] = (2, i)  # Save the new value with coordinates
    categories_value_dict[2, i] = category_value  # Now save the tuple as key!
    categories_dict[category_name] = categories_value_dict  # insert back into dict
'''