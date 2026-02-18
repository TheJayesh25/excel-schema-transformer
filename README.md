# ⚙️ Excel Schema Transformer

A config-driven automation engine for restructuring Excel datasets at scale.

Designed to eliminate repetitive manual Excel work by turning structural transformations into reproducible, rule-based pipelines.

> 💡 _Inspired by real-world analytics workflow automation challenges._

---

## 📌 Navigation

- [The Problem](#-the-problem)
- [The Idea](#-the-idea)
- [What This Enables](#-what-this-enables)
- [Core Capabilities](#-core-capabilities)
- [Architecture](#-architecture)
- [Project Structure](#-project-structure)
- [Why This Matters](#-why-this-matters)
- [Roadmap](#-roadmap)
- [License](#-license)

---

## 🚨 The Problem

In analytics and survey workflows, exported Excel datasets often require repeated structural adjustments:

- Moving and regrouping variables  
- Swapping or relocating column blocks  
- Cleaning or clearing specific ranges  
- Copying values between mapped variable groups  
- Generating derived structural columns  

When done manually, this leads to:

- ⏳ Hours of repetitive work  
- ⚠️ Inconsistent formatting  
- 🔁 Update fatigue after stakeholder changes  
- ❌ High risk of human error  
- 📉 No reproducibility  

**Small updates shouldn’t require rebuilding Excel structure from scratch.**

---

## 💡 The Idea

Instead of editing spreadsheets manually:

1. Define transformation rules once in YAML  
2. Run the pipeline  
3. Produce a delivery-ready dataset automatically  

The same configuration can be reused across iterations, updates, and batch exports.

👉 This shifts the workflow from manual editing to **engineering automation**.

---

## 🚀 What This Enables

- Rapid restructuring of large Excel datasets  
- Config-driven, repeatable formatting  
- Built-in validation for structural consistency  
- Clear separation between transformation logic and business rules  
- Faster turnaround in analytics delivery cycles  

**Time previously spent on manual formatting becomes time spent on analysis.**

---

## 🧠 Core Capabilities

### 🔧 Structural Automation

- Move individual columns  
- Swap equal-width column ranges  
- Relocate column blocks dynamically  

### 🎯 Scoped Data Transformations

- Replace values within defined ranges  
- Clear metadata, data, or both via rule scope  
- Preserve structural integrity  

### 🏷️ Label-Aware Mapping with Validation

- Positionally map source and target ranges  
- Validate target emptiness before copy  
- Prevent accidental data overwrites  

### 🔢 Derived Column Generation

- Split numeric identifiers into padded digit columns  
- Insert columns without overwriting schema  

---

## Architecture

The engine operates on three simple principles:

- Configuration over hardcoding  
- Deterministic rule sequencing  
- Metadata-aware transformations  

All transformations are defined declaratively:

```yaml
transformations:
  - type: move_column
    source: E
    target: fourth_last

  - type: replace_values
    range: [E, AF]
    from: 0
    to: ""
    scope: data_only
```

The engine interprets and applies each rule sequentially.

✅ **No manual Excel edits required.**

---

## 📂 Project Structure


```
excel-schema-transformer/
│
├── src/
│   ├── main.py
│   ├── utils.py
│   └── transformers/
│       ├── __init__.py
│       ├── move_column.py
│       ├── swap_ranges.py
│       ├── relocate_range.py
│       ├── replace_values.py
│       ├── clear_ranges.py
│       ├── clear_columns.py
│       ├── mapping_copy_by_labels.py
│       └── split_column_digits.py
│
├── configs/
│   └── example_config.yaml
│
├── data/
│   ├── sample_input.xlsx
│   └── sample_output.xlsx
│
├── requirements.txt
└── README.md
```

---

## 🎯 Why This Matters

High-quality analytics isn’t just about modeling or reporting.

It’s about engineering reliable data workflows.

Automating structural transformations:

- ⚡ Reduces turnaround time  
- 📈 Improves delivery consistency  
- 🔄 Minimizes rework after updates  
- 📦 Scales across projects  

**This project reflects an automation-first approach to analytics engineering.**

---

## Roadmap
- CSV support  
- CLI interface  
- Structured logging  
- YAML schema validation  
- Unit tests  

---

## 📜 License

This project is licensed under the **MIT License**.

You are free to use, modify, and distribute this software with proper attribution and credit.

See the `LICENSE` file for full details.
