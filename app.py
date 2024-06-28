############################################################################################################
# Importing Libraries

import streamlit as st
import hmac
import logging
import config
from openai import OpenAI

############################################################################################################
# Streamlit app layout

# Set the page to wide or centered mode
st.set_page_config(layout="centered")

############################################################################################################
# Password protection
def check_password():
    """Returns `True` if the user has the correct password."""

    def password_entered():
        """Checks whether a password entered by the user is correct."""
        if hmac.compare_digest(st.session_state["password"], st.secrets["general"]["password"]):
            st.session_state["password_correct"] = True
            del st.session_state["password"]  # Don't store the password.
        else:
            st.session_state["password_correct"] = False

    # Return True if the password is validated.
    if st.session_state.get("password_correct", False):
        return True

    # Show input for password.
    st.text_input(
        "Password", type="password", on_change=password_entered, key="password"
    )
    if "password_correct" in st.session_state:
        st.error("😕 Password incorrect")
    return False

if not check_password():
    st.stop()  # Do not continue if check_password is not True.

############################################################################################################
# Streamlit app layout
st.title(config.app_title)
st.caption(config.app_author)
# st.markdown(config.intro_para)
with st.expander("INSTRUCTIONS:"):
    st.markdown(config.instructions)

############################################################################################################
# ChatGPT

# Initialize the OpenAI client
client = OpenAI(api_key=st.secrets["api_keys"]["OPENAI_API_KEY"])

# Initialize the session state variables if they don't exist
if "openai_model" not in st.session_state:
    st.session_state["openai_model"] = config.ai_model

if "messages" not in st.session_state:
    st.session_state.messages = []

# Add system role message to the context but not to the UI
context_messages = [{"role": "system", "content": config.system_role_message}] + st.session_state.messages

# Display user and assistant messages only
for message in st.session_state.messages:
    if message["role"] in ["user", "assistant"]:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

if prompt := st.chat_input("How can I help you today?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        stream = client.chat.completions.create(
            model=st.session_state["openai_model"],
            messages=context_messages + [{"role": "user", "content": prompt}],
            temperature=config.temperature,
            max_tokens=config.max_tokens,
            frequency_penalty=config.frequency_penalty,
            presence_penalty=config.presence_penalty,
            stream=True,
        )
        response = st.write_stream(stream)
    st.session_state.messages.append({"role": "assistant", "content": response})

st.markdown(config.warning_message, unsafe_allow_html=True)

############################################################################################################

# Resources and About Sections in the Sidebar

st.sidebar.title("Resources")

for resource in config.resources:
    with st.sidebar:
        with st.expander(resource["title"]):
            st.markdown(f"Description: {resource['description']}")
            st.markdown(f"[Link]({resource['url']})")

# Footer
with st.sidebar:
    st.markdown("---")

    st.title("About")

   # Using the config objects in your Streamlit app
    st.markdown(config.app_creation_message, unsafe_allow_html=True)
    st.markdown(config.app_repo_license_message, unsafe_allow_html=True)