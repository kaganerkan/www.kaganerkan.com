import streamlit as st
st.set_page_config("Blog")

def read_markdown_file(markdown_file):
    with open(markdown_file, "r", encoding="utf-8") as file:
        content = file.read()
    return content
def build_page(pagename):
    pagename = str(pagename).replace(" ","_")
    markdown_content = read_markdown_file(f'Resorces/{pagename}.md')
    st.markdown(markdown_content, unsafe_allow_html=True)

pages = ["","Simple Voice Chat Not Working"]

st.session_state.page = st.selectbox(label="Search",options=pages)

try:
    build_page(st.session_state.page)
except:
    build_page("page_not_found")