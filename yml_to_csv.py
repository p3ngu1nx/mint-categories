import yaml 
import pandas as pd 
import sys

transaction_file_name = 'transaction-specification.csv'
new_output_file_name = 'trans2.csv'
yaml_data_file = 'data.yml'

# Open yaml data file and store data in a variable
with open(yaml_data_file) as f:
        data = yaml.load(f, Loader=yaml.FullLoader)


def get_my_parent_category(category):
    """
    get parent category from chield
    :param: category:child category name
                type: <str> for category file, <float> for blank category
    : retrun: parent category name or blank
        type: str
    """
    if type(category) == str:
        for key, value in data.items():
            if key.lower() == category.lower():
                # if category have no parent
                if value == 'Root':
                    return key
                return value
    else:
        # if parent category is blank, return empty string
        return ""

# read transaction file
df = pd.read_csv(transaction_file_name)

# Get parent category for eatch row or category column
# and store to new column 'parent_category'
df['parent_category'] = df['category'].apply(get_my_parent_category)

# save dataframe to new csv file
df.to_csv(new_output_file_name, index=False)
f.close()  # close yaml file
