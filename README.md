# 🤖 ThincSync Chatbot

Welcome to **ThincSync**! This is an interactive chatbot powered by a Language Learning Model (LLM) and integrated with Hugging Face's API. Built using **Streamlit**, this chatbot allows you to have dynamic and intelligent conversations.

## Features

- **User Authentication**: Secure login using Hugging Face credentials.
- **Interactive Chat**: The chatbot responds to user inputs in real-time.
- **Session Management**: Keeps track of the conversation history.
- **Seamless Integration**: Built with the Hugging Face API for LLM responses.

## Requirements

Make sure you have the following installed to run the project:

- Python 3.8 or higher
- [Streamlit](https://streamlit.io/)
- [Hugging Face API](https://huggingface.co/)

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/IthavinduU/ThinkSync.git
    cd ThinkSync
    ```

2. Install the required dependencies:

    ```bash
    pip install -r requirements.txt
    ```

3. Set up your Hugging Face credentials:
   
   You can provide Hugging Face credentials via Streamlit's secret management. To do this:
   
   - Go to `Secrets` in your Streamlit app.
   - Add your Hugging Face credentials as:
   
    ```
    [secrets]
    EMAIL = "your_email_here"
    PASS = "your_password_here"
    ```

## Usage

To start the chatbot, run the Streamlit app using:

```bash
streamlit run app.py
