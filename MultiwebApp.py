import streamlit as st

# --- PAGE SETUP ---
def show_about_page():
    st.title("About Me")
    st.write("This is the About Me page.")

def show_project_1_page():
    st.title("Sales Dashboard")
    st.write("This is the Sales Dashboard page.")

def show_project_2_page():
    st.title("Chat Bot")
    st.write("This is the Chat Bot page.")


# --- NAVIGATION SETUP ---
page = st.sidebar.selectbox(
    "Navigate",
    ("About Me", "Sales Dashboard", "Chat Bot")
)

# --- PAGE DISPLAY ---
if page == "About Me":
    show_about_page()
elif page == "Sales Dashboard":
    show_project_1_page()
elif page == "Chat Bot":
    show_project_2_page()

# --- SHARED ON ALL PAGES ---
st.sidebar.markdown("Made with ❤️ by [Sven](https://youtube.com/@codingisfun)")
