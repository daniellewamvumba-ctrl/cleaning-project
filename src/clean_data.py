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
def clean_text_columns(df):
    """
    Clean and standardize text columns.
    """

    text_columns = ["name", "email", "country"]

    for column in text_columns:
        df[column] = df[column].astype("string").str.strip()

    # Standardize names
    df["name"] = df["name"].str.title()

    # Standardize emails
    df["email"] = df["email"].str.lower()

    # Standardize country names
    df["country"] = df["country"].str.title()

    return df
def handle_missing_values(df):
    """
    Handle missing values according to column-specific rules.
    """

    # Missing emails remain missing because we should not invent an email.
    df["email"] = df["email"].fillna("unknown")

    # Missing age is left as missing until we convert it to numeric.
    df["age"] = df["age"].replace("", pd.NA)

    # Missing purchase dates remain missing.
    df["purchase_date"] = df["purchase_date"].replace("", pd.NA)

    return df
def convert_data_types(df):
    """
    Convert columns into appropriate data types.
    """

    df["customer_id"] = pd.to_numeric(
        df["customer_id"],
        errors="coerce"
    )

    df["age"] = pd.to_numeric(
        df["age"],
        errors="coerce"
    )

    df["purchase_amount"] = pd.to_numeric(
        df["purchase_amount"],
        errors="coerce"
    )

    df["purchase_date"] = pd.to_datetime(
        df["purchase_date"],
        errors="coerce"
    )

    return df
def remove_duplicates(df):
    """
    Remove duplicate customer records using customer_id.
    """

    df = df.drop_duplicates(
        subset="customer_id",
        keep="first"
    )

    return df
def clean_dataset(df):
    """
    Run the complete reusable cleaning pipeline.
    """

    df = standardize_column_names(df)

    df = clean_text_columns(df)

    df = handle_missing_values(df)

    df = convert_data_types(df)

    df = remove_duplicates(df)

    return df
                  
def main():

    input_file = "data/raw/customer_sales_raw.csv"
    output_file = "data/cleaned/customers_sales_cleaned.csv"

    # Load
    df = load_data(input_file)

    # Profile raw data
    print("\nRAW DATA PROFILE")
    raw_report = profile_data(df)
    print_profile(raw_report)

    # Clean
    df = clean_dataset(df)

    # Validate
    from validation import validate_emails, validate_purchase_amount, validate_age

    df["valid_email"] = validate_emails(df)
    df["valid_purchase_amount"] = validate_purchase_amount(df)
    df["valid_age"] = validate_age(df)

    # Display validation results
    print("\nVALIDATION RESULTS")
    print("Invalid emails:", (~df["valid_email"]).sum())
    print("Invalid purchase amounts:", (~df["valid_purchase_amount"]).sum())
    print("Invalid ages:", (~df["valid_age"]).sum())

    # Remove validation columns before exporting
    df = df.drop(
        columns=[
            "valid_email",
            "valid_purchase_amount",
            "valid_age"
        ]
    )

    # Save cleaned dataset
    df.to_csv(output_file, index=False)

    print("\nCLEANING COMPLETE!")
    print(f"Cleaned dataset saved to: {output_file}")

    # Final profile
    print("\nFINAL DATA PROFILE")
    final_report = profile_data(df)
    print_profile(final_report)


if __name__ == "__main__":
    main()


if __name__ =="__main__":
    main()
