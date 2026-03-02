import pandas as pd
import re

def add_virtual_column(df: pd.DataFrame, role: str, new_column: str) -> pd.DataFrame:
    # "Column labels must consist only of letters and underscores (_)"
    if not new_column or not all(c.isalpha() or c == '_' for c in new_column):
        return pd.DataFrame()

    # Validating all existing df columns
    for col in df.columns:
        if not col or not all(c.isalpha() or c == '_' for c in str(col)):
            return pd.DataFrame()
    
    # Parse expression (role) - so must be column [spaces] op [spaces] column, where op is +, -, or *
    role = role.strip()
    match = re.match(r'^([a-zA-Z_]+)\s*([+*-])\s*([a-zA-Z_]+)$', role)
    if not match:
        return pd.DataFrame()

    left_col, operator, right_col = match.groups()

    # "If the role or any column label is incorrect, the function should return an empty DataFrame"
    if left_col not in df.columns or right_col not in df.columns:
        return pd.DataFrame()

    # "The function must support basic operations: addition (+), subtraction (-), and multiplication (*)"
    result_df = df.copy()
    if operator == '+':
        result_df[new_column] = result_df[left_col] + result_df[right_col]
    elif operator == '-':
        result_df[new_column] = result_df[left_col] - result_df[right_col]
    elif operator == '*':
        result_df[new_column] = result_df[left_col] * result_df[right_col]
    else:
        return pd.DataFrame()

    return result_df