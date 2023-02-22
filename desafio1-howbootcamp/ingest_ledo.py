import os
import pandas as pd
from sqlalchemy import create_engine

engine = create_engine('postgresql://root:root@localhost:5432/test_db')

for dirname, _, filenames in os.walk('C:\\Users\\leandro.mestrinare\\OneDrive\\How Bootcamp\\desafio1'):
    for filename in filenames:
        file = os.path.join(dirname, filename)

        table_name = filename.split('.csv')[0]

        df = pd.read_csv(file)

        print(f'Creating table {table_name}')
        df.to_sql(table_name, engine, if_exists= 'replace', index = False) 

print('Process completed')