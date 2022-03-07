import pandas as pd
from sqlalchemy import create_engine

def df_to_table(hostname,dbname,uname,pwd,table_name,df):

    engine = create_engine("mysql+pymysql://{user}:{pw}@{host}/{db}"
                    .format(host=hostname, db=dbname, user=uname, pw=pwd))

    df.to_sql(con=engine,name=table_name,if_exists='append',index=False)
    print('db updated successfully')



if __name__ =='__main__':

    hostname="localhost"
    dbname="test"
    uname="root"
    pwd="root"
    table_name='student'

    student_df=pd.read_csv("C:/Users/i.e.bhattacharya/Downloads/Educo/sample_df.csv")
    df_to_table(hostname,dbname,uname,pwd,table_name,student_df)


