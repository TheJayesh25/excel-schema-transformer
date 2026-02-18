from openpyxl.utils import column_index_from_string


def excel_col_to_index(col_letter):
    """Convert Excel column letter (e.g., 'E') to 0-based index."""
    return column_index_from_string(col_letter) - 1


def resolve_target_position(df, target):
    """
    Resolve special target positions like 'fourth_last'
    or explicit Excel column letters.
    """
    if isinstance(target, str):
        if target == "last":
            return len(df.columns)
        if target == "fourth_last":
            return len(df.columns) - 4
        # assume Excel letter
        return excel_col_to_index(target)

    return int(target)
