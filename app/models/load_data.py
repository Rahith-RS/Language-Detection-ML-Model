import pandas as pd
from sqlalchemy.orm import Session
from app.models.database import SessionLocal, LanguageDataset

# 📌 Load dataset from CSV
df = pd.read_csv(r"app\assets\Language Detection.csv")


# 📌 Insert Data into DB
def load_data():
    session = SessionLocal()
    for _, row in df.iterrows():
        data_entry = LanguageDataset(text=row["Text"], language=row["Language"])
        session.add(data_entry)
    session.commit()
    session.close()
    print("✅ Data loaded into database")

# Run this script to load data
if __name__ == "__main__":
    load_data()
