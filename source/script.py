import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine

data = pd.read_csv("/root/hubble_data.csv")
print(data)
print('Total cost: ',data['cost'].sum())
data2 = data[['distance','recession_velocity']]
data2.set_index("distance", inplace= True)
data2.plot()
plt.savefig('/root/source_container/figure.pdf')

#engine = create_engine('postgresql://postgres:Mypass.1234@db_postgres_pandas1/postgres')
#data.to_sql('hubble_data',engine,if_exists='replace')
#df = pd.read_sql_query('select * from "hubble_data"',con=engine)
#print('Data from db: ',df )


#SOME MODIFICATION IN FEATURE DEV PANDAS
