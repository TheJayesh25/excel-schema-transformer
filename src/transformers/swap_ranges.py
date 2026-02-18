from utils import excel_col_to_index


def swap_ranges(df, rule, config):
    start1, end1 = rule["range1"]
    start2, end2 = rule["range2"]

    s1 = excel_col_to_index(start1)
    e1 = excel_col_to_index(end1)
    s2 = excel_col_to_index(start2)
    e2 = excel_col_to_index(end2)

    # Copy slices
    range1 = df.iloc[:, s1:e1 + 1].copy()
    range2 = df.iloc[:, s2:e2 + 1].copy()

    # Ensure equal width
    if (e1 - s1) != (e2 - s2):
        raise ValueError("Ranges must be of equal width to swap.")

    # Swap in place
    df.iloc[:, s1:e1 + 1] = range2.values
    df.iloc[:, s2:e2 + 1] = range1.values

    return df
