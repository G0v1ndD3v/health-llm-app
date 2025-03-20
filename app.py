import streamlit as st
from pages import authentication

def main():
    # Redirect if not logged in
    if "user" not in st.session_state or not st.session_state.user:
        authentication.authentication_page()
    else:
        st.switch_page("pages/chat.py")  # Load chat if authenticated

if __name__ == "__main__":
    main()
