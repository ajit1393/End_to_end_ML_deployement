from matplotlib.font_manager import json_load
import pymongo # pip install pymongo
import pandas as pd
import json

client = pymongo.MongoClient("mongodb+srv://khandaleajit:Admin123@cluster0.ejsnh68.mongodb.net/?retryWrites=true&w=majority")

DATA_FILE_PATH = (r"C:\Users\Dell\Desktop\Data files\End_to_end_ML_deployement\insurance.csv")
DATABASE_NAME = "INSURANCE"
COLLECTION_NAME = "INSURANCE_PROJECT"


if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    df.reset_index(drop=True,inplace=True)

    json_record=list(json.loads(df.T.to_json()).values())
    print(json_record[0])

    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_record)