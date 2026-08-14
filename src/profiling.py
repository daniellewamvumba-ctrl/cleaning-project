import pandas

def profile_data(df):
    """Generate a basic data quality"""
    report = {"rows": len(df),
              "columns":len(df.columns),
              "missing_values":df.isnull().sum().to_dict(),
              "duplicate_rows":int(df.duplicated().sum()),
              "data_types":df.dtypes.astype(str).to_dict()}
    return report

def print_profile(report):
    """Print the data quality in a readable format"""
    print("\n" + "="* 40)
    print("DATA QUALITY PROFILE")
    print("=" * 40)

    print(f"\nRows:{report['rows']}")
    print(f"Columns:{report['columns']}")
    print("\nMissing_values:")
    for column,count in report["missing_values"].items():
        print(f" {column}:{count}")
    print(f"\nDuplicate Rows:{report['duplicate_rows']}")
    print("\nData Types:")
    for column,dtype in report["data_types"].items():
        print(f" {column}:{dtype}")
