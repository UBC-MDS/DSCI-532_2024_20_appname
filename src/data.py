import json
import pandas as pd

# Get data from parquet file
df = pd.read_parquet("data/processed/co2-data.parquet")

with open("data/processed/country_codes.json", encoding="utf-8") as f:
    country_codes = json.load(f)
