from sqlalchemy import create_engine, text
import pandas as pd

engine = create_engine(
    'postgresql+psycopg2://root:root@localhost/test_db').connect()

sql = '''
select * from vw_song;
'''

df = pd.read_sql_query(text(sql),engine)

sql2 = '''
insert into tb_artist (
SELECT t1."date"
	,t1."rank"
	,t1.artist
	,t1.song 
FROM PUBLIC."Billboard" AS t1 
where t1.artist like 'Nirvana'
order by t1.artist, t1.song , t1."date" 
);
'''
df2 = engine.execute(text(sql2))
