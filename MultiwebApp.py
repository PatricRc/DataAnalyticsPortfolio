import streamlit as st

# --- PAGE SETUP ---
def show_about_page():
    st.title("Patricio Rios - Data Analyst Portfolio")
    st.subheader("Senior Data Analyst, assisting enterprises by supporting data-driven decision-making.")
    st.write("Experience & Qualifications")
    st.markdown("""
    - 7 Years experience extracting actionable insights from data
    - Strong hands-on experience and knowledge in Python and Excel
    - Good understanding of statistical principles and their respective applications
    - Excellent team-player and displaying a strong sense of initiative on tasks
    """)

def show_project_1_page():
    st.title("Sales Dashboard")
    st.write("This is the Sales Dashboard page.")

def show_project_2_page():
    st.title("Chat Bot")
    st.write("This is the Chat Bot page.")

# --- SIDEBAR SETUP ---
#st.sidebar.image("https://path_to_your_logo_image.com", width=150)  # Add your logo
st.sidebar.markdown("### Info")
page = st.sidebar.radio(
    "Select a page:",
    ["About Me", "Sales Dashboard", "Chat Bot"]
)

st.sidebar.markdown("### Projects")
st.sidebar.markdown("- Sales Dashboard\n- Chat Bot")

# --- PAGE DISPLAY ---
if page == "About Me":
    show_about_page()
elif page == "Sales Dashboard":
    show_project_1_page()
elif page == "Chat Bot":
    show_project_2_page()

# --- SHARED ON ALL PAGES ---
st.sidebar.markdown("Made with ❤️ by [Patricio](https://www.linkedin.com/in/patriciorioscanepa/)")

