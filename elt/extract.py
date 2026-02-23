import pandas as pd
from sqlalchemy import create_engine
from dotenv import load_dotenv
import os

load_dotenv()

DB_PASSWORD = os.environ.get("DB_PASSWORD")
DB_NAME = os.environ.get("DB_NAME")

engine = create_engine(f"postgresql://postgres:{DB_PASSWORD}@localhost:5432/{DB_NAME}")

# extract raw patients csv data into PostgreSQL tables
df = pd.read_csv("data/raw/patients.csv")
df.to_sql("patients", engine, if_exists="append", index=False)

# extract raw diagnoses csv data into PostgreSQL tables
df = pd.read_csv("data/raw/diagnoses.csv")
df.to_sql("diagnoses", engine, if_exists="append", index=False)

# extract raw encounters csv data into PostgreSQL tables
df = pd.read_csv("data/raw/encounters.csv")
df.to_sql("encounters", engine, if_exists="append", index=False)
