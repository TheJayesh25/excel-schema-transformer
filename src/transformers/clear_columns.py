from utils import excel_col_to_index


def clear_columns(df, rule, config):
    metadata_rows = config.get("metadata_rows", 0)
    scope = rule.get("scope", "all")

    for col_letter in rule["columns"]:
        c = excel_col_to_index(col_letter)

        if scope in ("all", "metadata_only"):
            df.iloc[:metadata_rows, c] = ""

        if scope in ("all", "data_only"):
            df.iloc[metadata_rows:, c] = ""

    return df
