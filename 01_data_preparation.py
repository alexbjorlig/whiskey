import xlwings as xw ### Xlwings is a library that makes it easy to call Python from Excel and vice versa
import json
from os import getcwd


# Path to Excel source file
full_path = getcwd()+'/source_data_from_legendre_lapointe/Excel_data.xlsx'

# Setting Excel version
app_target = '/Applications/Microsoft Office 2011/Microsoft Excel.app'

# Creating Xlwings workbook object to extract data from excel file
wb = xw.Workbook(fullname=full_path, app_visible=False, app_target=app_target)


def create_dict_of_whiskeys():
    """
    This method loops over the rows and colums of the given excel spreadsheet with whiskey data
    The objective is to create a master dictionary where each key is a whiskey
    and the value is the corresponding attributes of the whiskey in its own dictionary
    :return: dict_of_whiskeys
    """

    dict_of_whiskeys = {}

    # This loop iterates through excel rows [3:112] as the whiskeys starts on row 3 and ends at row 111
    for i in range(3, 112):

        # Here we insert the names..
        # Example... {"1. name": "Aberfeldy", "2. name": "Aberfeldy"}
        whiskey_dict = {'1. name': xw.Range(1, (i, 1)).value, '2. name': xw.Range(1, (i, 2)).value}

        # Read the line of attributes i.e. 0 or 1
        # Example... [0.0, 1.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.0, 1.0, 0.0______1.0, 0.0]
        whiskey_list_float = xw.Range(1, (i, 3), (i, 70)).value

        # Insert the list in the whiskey_dict and convert XlWings float to Integer
        # Example... "list": [0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0_________1, 0, 0]
        whiskey_dict['attribute_value_list'] = [int(x) for x in whiskey_list_float]

        '''
        The following code below creates a dictionary of the attributes but in a human readable format instead of binary
        '''

        # Each whiskey has 5 categories - each categories has a list consisting of attributes
        whiskey_attributes_dict = {'color': [], 'nose': [], 'body': [], 'pal': [], 'fin': []}

        # This loop iterates through excel columns [3:71] as the whiskeys attributes start on column 3 and ends on 70
        for x in range(3, 71):

            # Reads category key from first row
            whiskey_category_key = xw.Range(1, (1, x)).value.lower()

            # Reads attribute name from second row
            whiskey_attribute_name = xw.Range(1, (2, x)).value.lower()

            # Reads the attribute value from the current [i] row (outer loop)
            whiskey_attribute_value = int(xw.Range(1, (i, x)).value)

            # Checks if the whiskey has the attribute name
            if whiskey_attribute_value == 1:

                # Retrieve the attribute list for the current category
                categories_list = whiskey_attributes_dict[whiskey_category_key]

                # Append the attribute name to the attribute list
                categories_list.append(whiskey_attribute_name)

                # Append the attribute list to the whiskey_attributes_dict
                whiskey_attributes_dict[whiskey_category_key] = categories_list

        whiskey_dict['whiskey_attributes'] = whiskey_attributes_dict

        # [i-2] because we start the first loop at range(3, 112)
        dict_of_whiskeys[i-2] = whiskey_dict

    return dict_of_whiskeys

# Write dict to txt file
with open("whiskey_dict.txt", "w") as f:
    json.dump(create_dict_of_whiskeys(), f)

