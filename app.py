import streamlit as st
import random

st.title("אפליקציית כן / לא 🎲")

st.write("לחץ על הכפתור כדי לקבל תשובה!")

if st.button("לחץ כאן"):
    answer = random.choice(["כן", "לא"])
    st.subheader(f"התשובה היא: {answer}")
