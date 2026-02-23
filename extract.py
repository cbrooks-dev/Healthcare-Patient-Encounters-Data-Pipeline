import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

engine = create_engine(f"postgresql://postgres:{DB_PASSWORD}@localhost:5432/{DB_NAME}")

df = pd.read_csv("data/patients.csv")
df.to_sql("patients", engine, if_exists="append", index=False)

df = pd.read_csv("data/diagnoses.csv")
df.to_sql("diagnoses", engine, if_exists="append", index=False)

df = pd.read_csv("data/encounters.csv")
df.to_sql("encounters", engine, if_exists="append", index=False)
