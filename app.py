import streamlit as st
import pandas as pd

st.title("Decision Journal")

if "rows" not in st.session_state:
    st.session_state.rows = []

with st.form("add"):
    title = st.text_input("Decision")
    cost = st.slider("Cost (low=better)", 1, 10, 5)
    risk = st.slider("Risk (low=better)", 1, 10, 5)
    growth = st.slider("Growth", 1, 10, 5)
    if st.form_submit_button("Save") and title:
        score = round(growth * 0.5 + (10 - cost) * 0.25 + (10 - risk) * 0.25, 1)
        st.session_state.rows.append(
            {"Decision": title, "Score": score}
        )

if st.session_state.rows:
    df = pd.DataFrame(st.session_state.rows)
    st.dataframe(df)
    st.bar_chart(df.set_index("Decision")["Score"])
