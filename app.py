# streamlit_app.py
import streamlit as st
from gsheetsdb import connect
import pandas as pd

# Create a connection object.
conn = connect()

# Perform SQL query on the Google Sheet.
# Uses st.cache to only rerun when the query changes or after 10 min.
@st.cache(ttl=60)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url = st.secrets["Sheet1"]
rows_1 = run_query(f'SELECT * FROM "{sheet_url}"')

st.subheader('Sheet 1:')
# ---- Data frame ----
data_1 = []
for row in rows_1:
    #st.write(f"{row.Contratista} has a :{row.Volumen}:")
    datas = (str(row.Fecha),
             str(row.Operario),
             row.Horas,
             row.Producción)
    data_1.append(datas)

df = pd.DataFrame(data_1,columns = ['Fecha', 'Operario', 'Horas', 'Produccion'])

st.write(df)


@st.cache(ttl=60)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    return rows

sheet_url2 = st.secrets["Sheet2"]
rows = run_query(f'SELECT * FROM "{sheet_url2}"')

st.subheader('Sheet 2:')
# Print results.
for row in rows:
    st.write(f"{row.Operario} has a :{row.Horas}:")