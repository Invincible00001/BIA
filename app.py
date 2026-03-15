import streamlit as st
from agent import run_agent

st.title("Founder Business Intelligence Agent")

st.write("Ask questions about Deals or Work Orders")

query = st.chat_input("Ask a business question")

if query:

    st.chat_message("user").write(query)

    answer, trace = run_agent(query)

    st.chat_message("assistant").write(answer)

    st.subheader("Agent Action Trace")

    for step in trace:
        st.write("•", step)