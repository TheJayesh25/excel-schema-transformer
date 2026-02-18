import pandas as pd
from utils import excel_col_to_index


def is_blank(val):
    if pd.isna(val):
        return True
    if isinstance(val, str) and val.strip() == "":
        return True
    return False


def mapping_copy_by_labels(df, rule, config):
    metadata_rows = config.get("metadata_rows", 0)

    source_start, source_end = rule["source_range"]
    target_start, target_end = rule["target_range"]
    copy_value = rule.get("copy_value", 1)
    require_target_blank = rule.get("require_target_blank", True)

    s1 = excel_col_to_index(source_start)
    e1 = excel_col_to_index(source_end)
    s2 = excel_col_to_index(target_start)
    e2 = excel_col_to_index(target_end)

    # Validate equal width
    if (e1 - s1) != (e2 - s2):
        raise ValueError("Source and target ranges must have equal width.")

    # Extract labels (row index = metadata_rows - 1)
    label_row_index = metadata_rows - 1

    source_labels = (
        df.iloc[label_row_index, s1:e1 + 1]
        .fillna("")
        .astype(str)
        .tolist()
    )

    target_labels = (
        df.iloc[label_row_index, s2:e2 + 1]
        .fillna("")
        .astype(str)
        .tolist()
    )

    # Positional mapping
    mapping = []
    for i in range(len(source_labels)):
        mapping.append((s1 + i, s2 + i, source_labels[i], target_labels[i]))

    data = df.iloc[metadata_rows:].copy()

    # Validation pass
    for source_pos, target_pos, source_label, target_label in mapping:
        for row_idx in range(len(data)):
            source_val = data.iat[row_idx, source_pos]
            target_val = data.iat[row_idx, target_pos]

            source_matches = (
                source_val == copy_value
                or str(source_val).strip() == str(copy_value)
            )

            if source_matches and require_target_blank and not is_blank(target_val):
                excel_row = row_idx + metadata_rows + 1
                raise ValueError(
                    f"Violation at Excel row {excel_row}: "
                    f"Source '{source_label}' has value {copy_value} "
                    f"but target '{target_label}' not blank."
                )

    # Copy pass
    for source_pos, target_pos, _, _ in mapping:
        for row_idx in range(len(data)):
            source_val = data.iat[row_idx, source_pos]
            target_val = data.iat[row_idx, target_pos]

            source_matches = (
                source_val == copy_value
                or str(source_val).strip() == str(copy_value)
            )

            if source_matches:
                if not require_target_blank or is_blank(target_val):
                    data.iat[row_idx, target_pos] = copy_value

    df.iloc[metadata_rows:] = data.values

    return df
