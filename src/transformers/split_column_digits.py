def split_column_digits(df, rule, config):
    metadata_rows = config.get("metadata_rows", 0)

    source_column_name = rule["source_column"]
    pad_length = rule.get("pad_length")

    # Locate source column
    try:
        source_index = list(df.iloc[0]).index(source_column_name)
    except ValueError:
        raise ValueError(f"Source column '{source_column_name}' not found.")

    # Extract data rows
    data = df.iloc[metadata_rows:].copy()

    # Generate split digit columns
    split_columns = []

    for row_idx in range(len(data)):
        value = data.iat[row_idx, source_index]

        try:
            value = int(value)
        except:
            value = 0

        value_str = str(value).zfill(pad_length)

        split_columns.append([int(d) for d in value_str])

    # Convert to DataFrame
    import pandas as pd
    split_df = pd.DataFrame(split_columns)

    # Insert new columns after source column
    for i in range(pad_length):
        insert_position = source_index + i
        df.insert(insert_position, f"{source_column_name}_digit_{i+1}", "")

    # Fill data rows
    for i in range(pad_length):
        df.iloc[metadata_rows:, source_index + i] = split_df.iloc[:, i].values

    # Set metadata
    for i in range(pad_length):
        df.iat[0, source_index + i] = source_column_name
        df.iat[1, source_index + i] = source_column_name

    # Remove original source column (now shifted right)
    df.drop(df.columns[source_index + pad_length], axis=1, inplace=True)

    return df
