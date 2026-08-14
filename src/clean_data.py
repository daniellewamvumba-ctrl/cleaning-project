import pandas as pd
from profiling import profile_data,print_profile

def load_data(file_path):
    """Load CSV file into a Pandas DataFrame."""
    return pd.read_csv(file_path) 
def standardize_column_names(df):
    """Conver column names to lower case with underscores"""
    df.columns = (df.columns.str.strip().str.lower().str.replace(" ", "_"))
    return df
def clean_text_columns(df):
    """Clean text columns by removing extra spaces and using title case"""
    text_columns = df.select_dtypes(include="object").columns
    for col in text_columns:
        df[col] = df[col].astype(str).str.strip()
    if "name" in df.columns:
        df["name"] = df["name"].str.title()
    if "country" in df.columns:
        df["country"] = df["country"].str.title()
    return df

                  
def main():
    #Path to raw dataset
    input_file = "data/raw/customer_sales_raw.csv"

    #Load dataset
    df =load_data(input_file)

    #Profile dataset
    report = profile_data(df)

    #Display profile
    print_profile(report)

    df =standardize_column_names(df)
    df = clean_text_columns(df)

    print("\nCleaning Stage 1 Complete!")
    print(df.head())
    

if __name__ =="__main__":
    main()
