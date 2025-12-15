import pandas as pd
import duckdb

ECOCROP_CSV_URL = (
    "https://raw.githubusercontent.com/OpenCLIM/ecocrop/main/EcoCrop_DB.csv"
)

# 1. Load CSV into pandas
df = pd.read_csv(ECOCROP_CSV_URL, encoding="latin1")

print("Loaded rows:", len(df))
print(df.head())

# 2. Connect to DuckDB
con = duckdb.connect("ecocrop.duckdb")

# 3. Create table from DataFrame
#con.execute("DROP TABLE IF EXISTS ecocrop_raw")
con.register("ecocrop_df", df)

con.execute("""
    CREATE TABLE IF NOT EXISTS ecocrop_raw AS 
    SELECT * FROM ecocrop_df
""")
