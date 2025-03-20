import time
import streamlit as st
from services.auth_service import authenticate_user, register_new_user  # Import authentication functions  
from components.footer import add_footer  # Import footer

# Authentication page logic  
def authentication_page():
    # Initialize session state variables if not set  
    if "user" not in st.session_state:
        st.session_state.user = None
    if "username" not in st.session_state:
        st.session_state.username = None

    if "auth_action" not in st.session_state:
        st.session_state.auth_action = "Login"

    # Page title and introduction
    st.title("AI-Powered Health Assistant")
    st.markdown("Welcome! Please log in or register to continue.")
    st.divider()
    
    # Toggle buttons for login/register 
    col1, col2 = st.columns(2)
    with col1:
        if st.button("Login", use_container_width=True):
            st.session_state.auth_action = "Login"
    with col2:
        if st.button("Register", use_container_width=True):
            st.session_state.auth_action = "Register"

    # Login form 
    if st.session_state.auth_action == "Login":
        st.info("Log in with your credentials to continue.")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")

        if st.button("Submit", use_container_width=True):
            user_data, error_message = authenticate_user(email, password)
            
            if user_data:
                # Store user session data on successful login 
                st.session_state.user = user_data
                st.session_state.username = user_data["username"]
                st.success(f"Login successful! Welcome, {st.session_state.username}!")
                time.sleep(2)
                st.rerun()
            else:
                st.error(error_message)

        st.caption("New here? Register to create an account first!")

    # Registration form 
    elif st.session_state.auth_action == "Register":
        st.info("Register to create a new account.")
        username = st.text_input("Username")
        email = st.text_input("Email")
        password = st.text_input("Password", type="password")
        confirm_password = st.text_input("Confirm Password", type="password")

        if password != confirm_password:
            st.error("Passwords do not match!")

        if st.button("Submit", use_container_width=True) and password == confirm_password:
            message = register_new_user(email, password, username)
            if "successful" in message:
                st.success(message)
                time.sleep(2)
                st.session_state.auth_action = "Login"  # Redirect to login after registration
                st.rerun()
            else:
                st.error(message)

        st.caption("Already have an account? Sign in instead!")
    
    add_footer()  # Display footer