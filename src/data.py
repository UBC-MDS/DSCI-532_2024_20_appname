import json
import pandas as pd

df = pd.read_csv("data/processed/co2-data.csv")

with open("data/processed/country_codes.json", encoding="utf-8") as f:
    country_codes = json.load(f)
