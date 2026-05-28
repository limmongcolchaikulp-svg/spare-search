import streamlit as st
import pandas as pd

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Spare Part Search",
    page_icon="🔧",
    layout="centered"
)

# ---------------- HIDE STREAMLIT MENU ----------------
hide_style = """
<style>
#MainMenu {visibility:hidden;}
footer {visibility:hidden;}
header {visibility:hidden;}

.block-container{
    padding-top:20px;
    padding-bottom:20px;
}

.stTextInput > div > div > input {
    border-radius:15px;
    padding:12px;
    font-size:18px;
}

</style>
"""

st.markdown(hide_style, unsafe_allow_html=True)

# ---------------- LOAD EXCEL ----------------
df = pd.read_excel("SparePart.xlsx")

# ---------------- TITLE ----------------
st.markdown("""
<h1 style='text-align:center;
color:#2E86C1;
font-size:42px;'>
🔧 Spare Search
</h1>
""", unsafe_allow_html=True)

st.markdown("""
<p style='text-align:center;
color:gray;
font-size:18px;'>
Search spare parts quickly on mobile
</p>
""", unsafe_allow_html=True)

# ---------------- SEARCH BOX ----------------
search = st.text_input(
    "",
    placeholder="🔍 Search Part No / Name / Machine"
)

# ---------------- FILTER DATA ----------------
if search:
    result = df[
        df.astype(str).apply(
            lambda row: row.str.contains(search, case=False).any(),
            axis=1
        )
    ]
else:
    result = df

# ---------------- SHOW RESULT ----------------
for i, row in result.iterrows():

    stock_color = "#27AE60"

    try:
        if int(row['Stock']) <= 2:
            stock_color = "#E74C3C"
    except:
        pass

    st.markdown(
        f"""
        <div style="
            background-color:white;
            padding:18px;
            border-radius:18px;
            margin-bottom:15px;
            box-shadow:0 3px 10px rgba(0,0,0,0.08);
            border-left:8px solid #2E86C1;
        ">

        <h3 style="margin-bottom:10px;">
        {row['PartName']}
        </h3>

        <p style="font-size:16px;">
        📦 <b>Part No:</b> {row['PartNo']}<br>
        🏭 <b>Machine:</b> {row['Machine']}<br>
        📍 <b>Location:</b> {row['Location']}<br>
        🔢 <b>Stock:</b>
        <span style="
            color:{stock_color};
            font-weight:bold;
        ">
        {row['Stock']}
        </span>
        </p>

        </div>
        """,
        unsafe_allow_html=True
    )