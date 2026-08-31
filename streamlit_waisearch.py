import streamlit as st
import webbrowser
import urllib.parse

st.set_page_config(
    page_title="waiSearch",
    page_icon="🔎",
    layout="centered",
)

with st.container(horizontal_alignment="center"):
    st.space(size="large")
    st.title("waiSearch", text_alignment="center")

    query = st.text_input(
        "Search",
        placeholder="Search...",
        label_visibility="collapsed"
    )

    st.badge("Google Search, the way it should be - without AI summarization.")

if query:
    try:        
        encoded_query = urllib.parse.quote_plus(query)
        url = f"https://www.google.com/search?q={encoded_query}&udm=14"

        webbrowser.open(url)
    except Exception as e:
        raise e

with st.bottom:
    st.caption("Inspired by [udm14.com](https://udm14.com)", text_alignment="center")
