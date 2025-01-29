import streamlit as st
from langchain.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Initialize the LLM and prompt
prompt_template = ChatPromptTemplate.from_template("You are a helpful AI assistant. User: {user_input} Assistant:")
llm = ChatOpenAI()
chain = prompt_template | llm

#@traceable
def get_response(user_input):
    """Get response from the AI assistant."""
    response = chain.invoke(input={"user_input": user_input})
    return response.content

# Streamlit App
st.set_page_config(page_title="AI Chatbot", page_icon="🤖")

st.title("🤖 AI Chatbot")

st.write("Chat with an AI assistant. Type your message below and press Enter to continue the conversation. Type 'exit' to end.")

# Initialize session state for storing chat history
if "messages" not in st.session_state:
    st.session_state["messages"] = []
    # Add the first AI message
    st.session_state["messages"].append({"role": "assistant", "content": "Hi, how can I help you?"})

if "response" not in st.session_state:
    st.session_state["response"] = None

messages = st.session_state.messages
for msg in messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input(placeholder="Type your message here:"):
    messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    st.session_state["response"] = get_response(prompt)
    with st.chat_message("assistant"):
        messages.append({"role": "assistant", "content": st.session_state["response"]})
        st.write(st.session_state["response"])





