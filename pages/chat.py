import streamlit as st
from services.chat_service import get_chat_history, store_chat_history, generate_ai_response  # Import chat functions  
from components.sidebar import sidebar  # Import sidebar  
from components.footer import add_footer  # Import footer  

# Page title and introduction  
st.title("AI-Powered Health Assistant")
st.text("Get personalized medical guidance from our AI assistant. The assistant takes into account your medical history, past health issues, and medication intake from previous conversations to provide informed responses.")
st.divider()
st.warning("This AI assistant is experimental and may provide incorrect information. Always verify medical advice with a qualified healthcare professional.")

user_id = st.session_state.user["uid"]  # Get current user ID

chat_history = get_chat_history(user_id)  # Retrieve past chat history

# Display chat history  
for message in chat_history:
    with st.chat_message("user" if message["role"] == "user" else "assistant"):
        st.write(message["content"])

# Handle user input  
user_input = st.chat_input("Type your message:")
if user_input:
    with st.chat_message("user"):
        st.write(user_input)

    ai_response = generate_ai_response(user_input, chat_history)  # Generate AI response  

    if ai_response:
        store_chat_history(user_id, user_input, ai_response)  # Save conversation
        with st.chat_message("assistant"):
            st.write(ai_response)

sidebar()  # Display sidebar  
add_footer()  # Display footer