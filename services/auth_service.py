import requests
import streamlit as st
from firebase_admin import auth
from services.firebase_config import db  # Firestore database instance

FIREBASE_WEB_API_KEY = st.secrets["FIREBASE_WEB_API_KEY"]  # Firebase API key for authentication

# Store username in Firestore
def save_user_to_firestore(user_id, username):
    db.collection("users").document(user_id).set({"username": username})

# Retrieve username from Firestore
def fetch_username(user_id):
    user_doc = db.collection("users").document(user_id).get()
    return user_doc.to_dict().get("username") if user_doc.exists else None

# User login function
def authenticate_user(email, password):
    url = f"https://identitytoolkit.googleapis.com/v1/accounts:signInWithPassword?key={FIREBASE_WEB_API_KEY}"
    response = requests.post(url, json={"email": email, "password": password, "returnSecureToken": True}).json()

    if "error" in response:
        return None, response["error"]["message"]  # Return error message if login fails

    user_id = response["localId"]
    return {"uid": user_id, "email": email, "username": fetch_username(user_id) or email}, None

# User registration function
def register_new_user(email, password, username):
    try:
        user = auth.create_user(email=email, password=password)  # Create new user in Firebase  
        save_user_to_firestore(user.uid, username)  # Save user details in Firestore  
        return "Registration successful! Please login."
    except Exception as e:
        return f"Registration error: {str(e)}"  # Return error message if registration fails  