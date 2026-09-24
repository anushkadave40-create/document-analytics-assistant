import streamlit as st


def initialize_memory():

    if "messages" not in st.session_state:

        st.session_state.messages = []


def add(role, message):

    st.session_state.messages.append({

        "role": role,

        "content": message

    })


def clear():

    st.session_state.messages = []


def history():

    return st.session_state.messages
