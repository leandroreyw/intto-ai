import streamlit as st
import requests

# Use the deployed FastAPI backend URL
FASTAPI_URL = "https://your-backend.onrender.com"

st.title("🤖 InTTOVATOR AI - Customer Discovery Assistant")

st.subheader("💡 Example Questions")
st.write("- What is the biggest challenge you face in [problem area]?")
st.write("- Can you describe a recent experience where you encountered this issue?")
st.write("- How do you currently solve this problem?")

question = st.text_input("Enter your question:")

if st.button("Ask AI"):
    if question:
        response = requests.post(f"{FASTAPI_URL}/ask", json={"question": question})
        if response.status_code == 200:
            answer = response.json().get("response", "No response received.")
            st.write("### 🎯 AI Response:")
            st.success(answer)
        else:
            st.error("❌ Error: Unable to reach the AI server.")
    else:
        st.warning("⚠️ Please enter a question.")