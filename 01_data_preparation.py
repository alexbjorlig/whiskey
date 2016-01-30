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

        # Insert the names
        whiskey_dict = {'1. name': xw.Range(1, (i, 1)).value, '2. name': xw.Range(1, (i, 2)).value}

        # Read the line of attributes i.e. 0 or 1
        whiskey_list_float = xw.Range(1, (i, 3), (i, 70)).value

        # Convert Xlwings standard float type to integer
        whiskey_list_integer = [int(x) for x in whiskey_list_float]

        # Insert the list in the whiskey_dict
        whiskey_dict['list'] = whiskey_list_integer

        # Each whiskey has 5 attributes
        descriptive_dict = {'color': [], 'nose': [], 'body': [], 'pal': [], 'fin': []}

        # This loop iterates through excel columns [3:71] as the whiskeys attributes start on column 3 and ends on 70
        for x in range(3, 71):

            category_name = xw.Range(1, (1, x)).value.lower()
            category_value = xw.Range(1, (2, x)).value.lower()
            attribute_value_int = int(xw.Range(1, (i, x)).value)
            if attribute_value_int == 1:
                categories_list = descriptive_dict[category_name]  # Get the categorys list
                categories_list.append(category_value)  # Append the value
                descriptive_dict[category_name] = categories_list  # Put the new list back in
        whiskey_dict['descriptive'] = descriptive_dict

        dict_of_whiskeys[i-2] = whiskey_dict  # Insert the whiskey only with number

    return dict_of_whiskeys

dict_of_whiskeys = create_dict_of_whiskeys()

### Write dict to txt file
with open("whiskey_dict.txt", "w") as myfile:
    json.dump(dict_of_whiskeys, myfile)

