from utils import excel_col_to_index


def clear_ranges(df, rule, config):
    metadata_rows = config.get("metadata_rows", 0)
    scope = rule.get("scope", "all")

    for start, end in rule["ranges"]:
        s = excel_col_to_index(start)
        e = excel_col_to_index(end)

        if scope in ("all", "metadata_only"):
            df.iloc[:metadata_rows, s:e + 1] = ""

        if scope in ("all", "data_only"):
            df.iloc[metadata_rows:, s:e + 1] = ""

    return df
