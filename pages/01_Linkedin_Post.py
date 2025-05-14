import requests  # type: ignore
import streamlit as st  # type: ignore
import json

# Set your Groq Cloud API key here
groq_api_key = "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"
api_url = "https://api.groq.com/openai/v1/chat/completions"

def generate_linkedIn_post(post_topic, post_tone, profession):
    headers = {
        "Authorization": f"Bearer {groq_api_key}",
        "Content-Type": "application/json"
    }
    
    prompt = f"Create a professional LinkedIn post about {post_topic} in a {post_tone} tone, tailored for a {profession}, and include emojis."

    data = {
        "model": "llama-3.3-70b-versatile",
        "messages": [{"role": "user", "content": prompt}]
    }
    
    response = requests.post(api_url, headers=headers, json=data)
    
    if response.status_code == 200:
        result = response.json()
        post_content = result["choices"][0]["message"]["content"]
        return post_content
    else:
        st.error(f"Error: {response.status_code} - {response.text}")
        return None

# Streamlit UI
st.title("🚀 LinkedIn Post Generator")
st.write("Generate an engaging LinkedIn post using the **LLaMA model on Groq Cloud**.")

post_topic = st.text_input("📌 Enter the topic for your LinkedIn post:")

post_tone = st.selectbox("🎭 Choose the tone of your post:", ["Formal", "Friendly", "Exciting"])

profession = st.selectbox("💼 Select your profession:", ["Software Engineer", "Marketing Manager", "Data Scientist"])

# Generate Post Button
if st.button("✨ Generate LinkedIn Post"):
    if post_topic:
        st.write(f"### ✍️ Here's your LinkedIn post about **{post_topic}**:")
        
        post_content = generate_linkedIn_post(post_topic, post_tone, profession)
        if post_content:
            st.write(post_content)
    else:
        st.warning("⚠️ Please enter a topic to generate the post.")
