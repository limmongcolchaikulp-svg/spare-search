import streamlit as st
import pandas as pd

df = pd.read_excel("SparePart.xlsx")

st.title("🔧 Spare Part Search")

search = st.text_input("Search Part")

if search:
    result = df[
        df.astype(str).apply(
            lambda row: row.str.contains(search, case=False).any(),
            axis=1
        )
    ]

    st.dataframe(result)

else:
    st.dataframe(df)