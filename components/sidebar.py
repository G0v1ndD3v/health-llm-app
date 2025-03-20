import streamlit as st

# Sidebar with navigation 
def sidebar():
    # Check if a user is logged in
    if "user" in st.session_state and st.session_state.user:
        username = st.session_state.get("username", "Guest")
        st.sidebar.write(f"Logged in as: {username}")
        
        # Navigation links
        st.sidebar.subheader("Navigation")
        st.sidebar.page_link("pages/chat.py", label="AI-Powered Health Assistant")
        st.sidebar.page_link("pages/acknowledgments.py", label="Acknowledgments")

        # Logout button
        if st.sidebar.button("Logout", use_container_width=True):
            st.session_state.user = None  # Clear user session
            st.session_state.username = None
            st.success("Logged out successfully!")
            st.switch_page("app.py")  # Redirect to authentication page
