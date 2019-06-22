#!/usr/bin/env python
import os
import sys
import pandas as pd
import pymongo
import json
import glob

def import_content(filepath):
    mng_client = pymongo.MongoClient('localhost', 27017)
    mng_db = mng_client['csv_entries']
    collection_name = 'test'
    db_cm = mng_db[collection_name]
    cdir = os.path.dirname(__file__)
    file_res = os.path.join(cdir, filepath)

    data = pd.read_csv(file_res,encoding='utf-16')
    data_json = json.loads(data.to_json(orient='records'))
    db_cm.insert(data_json)

if __name__ == "__main__":
  filepath = './csv/test.csv'
  import_content(filepath)