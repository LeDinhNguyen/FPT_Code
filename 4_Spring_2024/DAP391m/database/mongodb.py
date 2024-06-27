import pymongo
import os
import pandas as pd
from concurrent.futures import ThreadPoolExecutor
import time

myclient = pymongo.MongoClient("mongodb://localhost:27017")

mydb = myclient["DAP301m_movies"]

"""
data/
    cleaned_keywords.csv
    collection_df.csv
    company_df.csv
    country.csv
    craw.csv
    crew.csv
    genre.csv
    language_df.csv
"""

data_file = os.listdir("./data")
collections_name = {d: d[:-4] for d in data_file}
for i in data_file:
    print(i)
data = pd.read_csv("./data/cleaned_keywords.csv", index_col=0)

def mongoimport(csv_path, collection):
    df = pd.read_csv(csv_path, index_col=0)
    data = df.to_dict(orient='records')
    collection.insert_many(data)


for d in data_file:
    if collections_name[d] not in mydb.list_collection_names():
        mydb.create_collection(collections_name[d])
    curr_coll = mydb[collections_name[d]]
    print(f"******Start {collections_name[d]}******")
    mongoimport(f"./data/{d}", curr_coll)
    print(f"******Done {collections_name[d]}******\n")

    chunk_size = 1000
    data_chunks = [data[i:i + chunk_size] for i in range(0, len(data), chunk_size)]

    # Number of threads (adjust as needed)
    num_threads = 4

    start_time = time.time()

    # Use ThreadPoolExecutor for multithreading
    with ThreadPoolExecutor(max_workers=num_threads) as executor:
        executor.map(mongoimport, data_chunks)

    end_time = time.time()

    # Calculate and print the total running time
    total_time = end_time - start_time
    print(f"Total running time: {total_time} seconds")