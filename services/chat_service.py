import requests
import streamlit as st
from firebase_admin import firestore

db = firestore.client()  # Initialize Firestore client
TEXT_API_KEY = st.secrets["TEXT_API_KEY"]  # OpenAI API key

# Retrieve chat history for a user from Firestore  
def get_chat_history(user_id):
    chat_history_ref = db.collection("chatHistory").document(user_id)
    chat_history_doc = chat_history_ref.get()
    
    if chat_history_doc.exists:
        return chat_history_doc.to_dict().get("messages", [])  # Return stored messages 
    else:
        return []  # Return empty list if no chat history

# Store user and AI messages in Firestore  
def store_chat_history(user_id, user_input, ai_response):
    chat_history_ref = db.collection("chatHistory").document(user_id)
    chat_history_doc = chat_history_ref.get()
    
    if chat_history_doc.exists:
        chat_history = chat_history_doc.to_dict().get("messages", [])
    else:
        chat_history = []
    
    # Append new user and AI responses  
    chat_history.append({"role": "user", "content": user_input})
    chat_history.append({"role": "assistant", "content": ai_response})
    
    chat_history_ref.set({"messages": chat_history})  # Save updated chat history

# Generate AI response via OpenAI API
def generate_ai_response(user_input, chat_history):
    headers = {"Authorization": f"Bearer {TEXT_API_KEY}", "Content-Type": "application/json"}
    payload = {
        "model": "gpt-4-1106-preview",
        "messages": chat_history + [{"role": "user", "content": user_input}],  # Include chat context  
        "temperature": 0.4  # Controls randomness of responses  
    }

    try:
        response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)
        response_data = response.json()
        return response_data["choices"][0]["message"]["content"] if "choices" in response_data else "Error: No response from AI."
    except Exception as e:
        return f"Error processing AI response: {str(e)}"  # Handle API request failures