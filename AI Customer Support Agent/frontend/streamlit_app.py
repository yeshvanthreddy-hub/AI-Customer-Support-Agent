import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from backend.agents.smart_support_agent import run_smart_support_agent

st.title("💼 AI Customer Support Agent")

query = st.text_input("Describe your issue:")

if st.button("Get Help"):
    if query:
        st.write("⚡ Using Smart AI...")  # DEBUG

        response = run_smart_support_agent(query)

        st.write(response)
    else:
        st.warning("Please enter your issue")