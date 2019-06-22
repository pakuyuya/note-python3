import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq

df = pd.read_csv('input/test.csv')
table = pa.Table.from_pandas(df)
pq.write_table(table, 'output/test.parquet')
