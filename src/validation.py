import re
import pandas as pd


def validate_emails(df):
    """
    Validate email addresses and return a boolean Series.
    """

    pattern = r"^[^@\s]+@[^@\s]+\.[^@\s]+$"

    return df["email"].apply(
        lambda email: (
            False
            if pd.isna(email) or email == "unknown"
            else bool(re.match(pattern, str(email)))
        )
    )
def validate_purchase_amount(df):
    """
    Check that purchase amounts are not negative.
    """

    return df["purchase_amount"].ge(0)
def validate_age(df):
    """
    Check that ages fall within a reasonable range.
    """

    return df["age"].between(0, 120)