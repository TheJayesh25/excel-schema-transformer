import pandas as pd
import yaml
from transformers import TRANSFORMER_REGISTRY


def run_pipeline(config_path):
    with open(config_path, "r") as f:
        config = yaml.safe_load(f)

    df = pd.read_excel(config["input_file"], header=None)
    
    print(f"\nColumns before applying any rules: {list(df.iloc[0])}")
    print(f"Column labels before applying any rules: {list(df.iloc[1])}\n")

    for i, rule in enumerate(config["transformations"], start=1):
        rule_type = rule["type"]
        print(f"Applying rule {i}: {rule_type}")
        transformer = TRANSFORMER_REGISTRY[rule_type]
        df = transformer(df, rule, config)
        print(f"Columns after rule {i}: {list(df.iloc[0])}")
        print(f"Column labels after rule {i}: {list(df.iloc[1])}\n")


    df.to_excel(config["output_file"], header=False, index=False)


if __name__ == "__main__":
    run_pipeline("configs/example_config.yaml")




