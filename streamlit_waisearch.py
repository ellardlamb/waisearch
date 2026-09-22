import streamlit as st
import webbrowser
import urllib.parse
from streamlit.components.v1 import html

def on_input():
    query = st.session_state["input"]
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={encoded_query}&udm=14"

    # webbrowser.open_new_tab(url) # Only works when running locally, not in Streamlit Cloud
    open_page(url)

def open_page(url):
    open_script= """
        <script type="text/javascript">
            window.open('%s', '_blank').focus();
        </script>
    """ % (url)
    html(open_script)

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
        label_visibility="collapsed",
        key="input",
        on_change=on_input,
    )

    st.badge("Google Search, the way it should be - without AI summarization.", )

with st.bottom:
    st.caption("Inspired by [udm14.com](https://udm14.com)", text_alignment="center")
