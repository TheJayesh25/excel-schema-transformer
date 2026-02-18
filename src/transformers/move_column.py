from utils import excel_col_to_index, resolve_target_position


def move_column(df, rule, config):
    source = rule["source"]
    target = rule["target"]

    source_index = excel_col_to_index(source)
    target_index = resolve_target_position(df, target)

    # Extract column
    col_series = df.iloc[:, source_index]

    # Drop original
    df = df.drop(df.columns[source_index], axis=1)

    # If source column was before target, adjust target index
    if source_index < target_index:
        target_index -= 1

    # Insert at new location
    df.insert(target_index, col_series.name, col_series)

    return df
