#BITSO API CLIENT
import pandas as pd
from pandas import DataFrame
import matplotlib as plt
import mysql.connector
from datetime import datetime

hostname = 'localhost'
username = 'root'
password = 'root'
database = 'bitso_client_db'

def db_getBTC_HIST() :

    conn = mysql.connector.connect( host=hostname, user=username, passwd=password, db=database )
    cur = conn.cursor()
    cur.execute( "SELECT ask FROM bitcoin_hist" )
    names = [ x[0] for x in cur.description]
    rows = cur.fetchall()
    list = []
    for row in rows:
        list.append(row)
    conn.close()

    return pd.DataFrame(list, columns=names)

df =  db_getBTC_HIST()
print(df.head())


# plotting a histogram
df['ask'].plot(kind='hist', bins=10, color = 'green')
  
# x-axis label
plt.xlabel('age')
# frequency label
plt.ylabel('No. of people')
# plot title
plt.title('My histogram')
  
# function to show the plot
plt.show()