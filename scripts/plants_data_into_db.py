import pandas as pd
import duckdb

ECOCROP_CSV_URL = (
    "https://raw.githubusercontent.com/OpenCLIM/ecocrop/main/EcoCrop_DB.csv"
)
duckdb.connect("../data/ecocrop.duckdb")

ecocrop_df = pd.read_csv(ECOCROP_CSV_URL, encoding="latin1")

print("Loaded rows:", len(ecocrop_df))

duckdb.sql("""
    CREATE TABLE IF NOT EXISTS ecocrop_raw AS 
    SELECT * FROM ecocrop_df
""")
