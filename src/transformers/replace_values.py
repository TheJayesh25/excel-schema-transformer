from utils import excel_col_to_index


def replace_values(df, rule, config):
    start, end = rule["range"]
    from_value = rule["from"]
    to_value = rule["to"]

    metadata_rows = config.get("metadata_rows", 0)

    s = excel_col_to_index(start)
    e = excel_col_to_index(end)

    # Work only on data rows
    data = df.iloc[metadata_rows:, s:e + 1]

    df.iloc[metadata_rows:, s:e + 1] = data.replace(from_value, to_value)

    return df
