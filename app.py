import streamlit as st
import pandas as pd
import duckdb

st.write("Hello World")
data = {"a": [1, 2, 3], "B": [4, 5, 6]}
df = pd.DataFrame(data)

tab1, tab2, tab3 = st.tabs(["Cat", "Dog", "Owl"])

with tab1:
    #input_text = st.text_area(label="entrez votre input")
    #st.write(input_text)
    #st.write(df)

    sql_query = st.text_area(label="entrez votre input")
    result = duckdb.query(sql_query).df()
    st.write(f"Vous avez entré la query suivante {sql_query}")
    st.write(result)

with tab2:
    st.header("A dog")
    st.image("https://static.streamlit.io/examples/dog.jpg", width=200)

with tab3:
    st.header("An owl")
    st.image("https://static.streamlit.io/examples/owl.jpg", width=200)
