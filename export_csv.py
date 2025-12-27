import sqlite3
import pandas as pd

db_path = "data/dw/netflix.db"
conn = sqlite3.connect(db_path)

df = pd.read_sql_query("SELECT * FROM netflix_titles;", conn)
conn.close()

out_path = "data/prepared/netflix_titles.csv"
df.to_csv(out_path, index=False, encoding="utf-8-sig")

print(f"Done: {out_path} | rows={len(df)} cols={df.shape[1]}")
