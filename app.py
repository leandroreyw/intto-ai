import streamlit as st
import requests

st.title("🤖 InTTOVATOR AI - Customer Discovery Assistant")

# Create a list to store saved responses
if "saved_responses" not in st.session_state:
    st.session_state.saved_responses = []

# User input
question = st.text_input("Enter your question:")

if st.button("Ask AI"):
    if question:
        response = requests.post("http://127.0.0.1:8000/ask", json={"question": question})
        if response.status_code == 200:
            answer = response.json().get("response", "No response received.")
            st.write("### 🎯 AI Response:")
            st.success(answer)
            if st.button("💾 Save Response"):
                st.session_state.saved_responses.append(answer)
        else:
            st.error("❌ Error: Unable to reach the AI server.")
    else:
        st.warning("⚠️ Please enter a question.")

# Display saved responses
if st.session_state.saved_responses:
    st.subheader("📁 Saved Responses")
    for idx, saved in enumerate(st.session_state.saved_responses):
        st.write(f"{idx + 1}. {saved}")