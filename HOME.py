import streamlit as st
st.set_page_config(
    page_title="Streamlit Test",
    page_icon="❤️",
    layout="centered",
    initial_sidebar_state="auto"
    )

st.write("# Hovedside for eksperimenter")
st.divider()
reader=open("readme.md").read()

st.markdown(reader)
test = input("Habs")

"""with open('readme.md', 'r') as file:
    readme_md = file.read()

st.markdown(readme_md)
"""