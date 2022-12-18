import pymongo
import pandas as pd
import json


client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")
DATA_FILE_PATH="/config/workspace/aps_failure_training_set1.csv"
DATABASE_NAME="aps"
COLLECTION_NAME="sensor"

if __name__=="__main__":
    df = pd.read_csv(DATA_FILE_PATH)
    print(f"Rows and columns: {df.shape}")

    #convert dataframe to json so that we can dump the data into MongoDB
    df.reset_index(drop=True,inplace=True)

    #transpose the dataframe and convert it as json
    json_records=list(json.loads(df.T.to_json()).values())
    print(json_records[0])

    #then dump the data into mongodb
    client[DATABASE_NAME][COLLECTION_NAME].insert_many(json_records)


