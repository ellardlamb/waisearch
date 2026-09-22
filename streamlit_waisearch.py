# streamlit run <app_name>.py
import streamlit as st
import urllib.parse
import webbrowser
from random import randrange

rotating_greeting = ["What's on your mind?", "I'm feeling lucky!", "Let's do this!"]

if "on_mobile" not in st.session_state:
    st.session_state.on_mobile = False

# print(f"Initial session state: {st.session_state.on_mobile}")

def check_mobile():
    if on_mobile == True:
        st.session_state.on_mobile = True
    elif on_mobile == False:
        st.session_state.on_mobile = False
    # print(f"Mobile session state: {st.session_state.on_mobile} | Mobile Visible: {on_mobile}")

def on_input():
    query = st.session_state["input"]
    encoded_query = urllib.parse.quote_plus(query)
    url = f"https://www.google.com/search?q={encoded_query}&udm=14"

    if st.session_state.on_mobile:
        print("Using mobile component to render results!")
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
    # st.title("waiSearch", text_alignment="center")
    top_container = st.container(horizontal_alignment="center")
    middle_container = st.container(horizontal_alignment="center")
    bottom_container = st.container(horizontal_alignment="center")

    with st.empty():
        on_mobile = st.toggle("On Mobile?", value=False, on_change=check_mobile)

    with bottom_container:
        if on_mobile:
            st.button("Search 🔎", on_click=on_input)
                
        # st.badge("Google Search, without AI summarization.")
        with st.bottom:
            st.caption("Inspired by [udm14.com](https://udm14.com)", text_alignment="center")

    with middle_container:
        query = st.text_input(
            "Search",
            placeholder=rotating_greeting[randrange(len(rotating_greeting))],
            label_visibility="collapsed",
            key="input",
            on_change=on_input,
            args=[on_mobile]
        )
        st.badge("Google Search, without AI summarization.")

    with top_container:
        st.title("waiSearch", text_alignment="center")

    # st.badge("Google Search, without AI summarization.")

    # st.badge("Google Search, without AI summarization.")

# with st.bottom:
    # st.caption("Inspired by [udm14.com](https://udm14.com)", text_alignment="center")
