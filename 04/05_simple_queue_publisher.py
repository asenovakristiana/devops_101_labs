import streamlit as st
from persistqueue import SQLiteQueue as Queue

# Create or connect to the queue
queue = Queue("message_queue", auto_commit=True)

# Streamlit UI for publishing messages
st.title("Message Publisher")
message = st.text_input("Enter a message:")

if st.button("Send Message"):
    if message:
        queue.put(message)
        st.success("Message added to the queue.")
    else:
        st.warning("Please enter a message.")