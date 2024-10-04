import streamlit as st
from hugchat import hugchat

# App title
st.set_page_config(page_title="🤗💬 ThincSync")

# Remove Hugging Face Credentials
with st.sidebar:
    st.title("🤗💬 ThincSync")
    st.info("You can start chatting without logging in!")

# Store LLM generated responses
if "messages" not in st.session_state.keys():
    st.session_state.messages = [
        {"role": "assistant", "content": "How may I help you?"}
    ]

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])


# Function for generating LLM response
def generate_response(prompt_input):
    # Create ChatBot without login (modify this according to your API usage)
    chatbot = hugchat.ChatBot()
    return chatbot.chat(prompt_input)


# User-provided prompt
if prompt := st.chat_input():
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.write(prompt)

    # Generate a new response if the last message is not from the assistant
    if st.session_state.messages[-1]["role"] != "assistant":
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response = generate_response(prompt)
                st.write(response)
        message = {"role": "assistant", "content": response}
        st.session_state.messages.append(message)
