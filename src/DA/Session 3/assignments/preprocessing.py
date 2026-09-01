import pandas as pd

def read_data_file(file_path):
    try:
        if ".csv" not in  file_path :
            raise TypeError("This is not a csv file")
        df = pd.read_csv(file_path)
    except FileNotFoundError:
        print("This file doesn't exist") 
        return None
    except TypeError as e:
        print(e)
        return None
            
    return df

def drop_unnecessary_features(df , cols_to_drop):
    return df.drop(columns=cols_to_drop)

def check_data_type(df):
    result = pd.DataFrame(
    {
    'Unique': df.nunique(),
    'Dtype': df.dtypes
    })
    return result