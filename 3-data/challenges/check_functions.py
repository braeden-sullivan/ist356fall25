'''create a module `check_functions.py`
    - add the `clean_currency()` function definition to it.
    - under `if __name__=='__main__':` add the tests
    - run the code to make sure it works.'''

import pandas as pd

def clean_currency(currency_series):
    """
    Cleans a pandas Series containing currency values by removing
    currency symbols and commas, and converting to float.

    Parameters:
    currency_series (pd.Series): Series containing currency strings.

    Returns:
    pd.Series: Series with cleaned float values.
    """
    return currency_series.replace('[\$,]', '', regex=True).astype(float)

if __name__ == '__main__':
    # Test cases
    test_data = pd.Series(['$1,234.56', '$78.90', '$0.99', '$10,000.00'])
    cleaned_data = clean_currency(test_data)
    print("Original Data:")
    print(test_data)
    print("\nCleaned Data:")
    print(cleaned_data)
    assert cleaned_data.equals(pd.Series([1234.56, 78.90, 0.99, 10000.00])), "Test failed!"
    print("\nAll tests passed!")