from utils import excel_col_to_index


def relocate_range(df, rule, config):
    start, end = rule["source_range"]
    insert_at = rule["insert_at"]

    s = excel_col_to_index(start)
    e = excel_col_to_index(end)
    insert_index = excel_col_to_index(insert_at)

    # Extract range to move
    cols_to_move = df.columns[s:e + 1]
    moved_block = df.iloc[:, s:e + 1].copy()

    # Drop original range
    df = df.drop(columns=cols_to_move)

    # Adjust insert position if range was before insert location
    if s < insert_index:
        insert_index -= (e - s + 1)

    # Split dataframe
    left = df.iloc[:, :insert_index]
    right = df.iloc[:, insert_index:]

    # Reassemble
    df = left.join(moved_block).join(right)

    return df
