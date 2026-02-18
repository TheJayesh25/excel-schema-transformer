from .move_column import move_column
from .swap_ranges import swap_ranges
from .relocate_range import relocate_range
from .replace_values import replace_values
from .clear_ranges import clear_ranges
from .clear_columns import clear_columns
from .mapping_copy_by_labels import mapping_copy_by_labels
from .split_column_digits import split_column_digits

TRANSFORMER_REGISTRY = {
    "move_column": move_column,
    "swap_ranges": swap_ranges,
    "relocate_range": relocate_range,
    "replace_values": replace_values,
    "clear_ranges": clear_ranges,
    "clear_columns": clear_columns,
    "mapping_copy_by_labels": mapping_copy_by_labels,
    "split_column_digits": split_column_digits,
}
