# streamlit run <app_name>.py
import streamlit as st
import urllib.parse
import webbrowser
from random import randrange

rotating_greeting = ["What's on your mind?", "I'm feeling lucky!", "Let's do this!"]

def on_input():
    query = st.session_state["input"]
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={encoded_query}&udm=14"

    if on_mobile:
        webbrowser.open_new_tab(url)
    else:
        open_page(url)

def open_page(url):
    open_script = f"""
        <script style="width: 0; height: 0; display: block;" type="text/javascript">
            window.open('{url}', '_blank').focus();
        </script>
    """

    with st.empty().container():
        # Height cannot be zero; limitation with CSS iframe attr
        # Causes slight visual blip when processing first request, but not subsequent requests
        st.iframe(open_script, height=1)

st.set_page_config(
    page_title="waiSearch",
    page_icon="🔎",
    layout="centered",
)

with st.container(horizontal_alignment="center", vertical_alignment="distribute"):
    st.title("waiSearch", text_alignment="center")

    query = st.text_input(
        "Search",
        placeholder=rotating_greeting[randrange(len(rotating_greeting))],
        label_visibility="collapsed",
        key="input",
        on_change=on_input,
    )

    on_mobile = st.toggle("On Mobile?", value=False)

    if on_mobile:
        st.button("Search 🔎", on_click=on_input)

    st.badge("Google Search, without AI summarization.")

with st.bottom:
    st.caption("Inspired by [udm14.com](https://udm14.com)", text_alignment="center")
