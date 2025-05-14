import os
import groq
import streamlit as st
import graphviz

# Streamlit UI
st.title("AI-Powered Visual Generator 🎨")

# User Input: Select Visualization Type
visual_type = st.selectbox("Choose Visualization Type:", ["Mindmap", "Flowchart", "Diagram"])

# User Input: Enter Prompt
user_prompt = st.text_area("Enter your topic or concept:", "Artificial Intelligence")

# User Input: Choose Node Style
node_style = st.selectbox("Choose Node Style:", ["circle", "box", "ellipse"])

# User Input: Choose Edge Style
edge_style = st.selectbox("Choose Edge Style:", ["solid", "dashed", "dotted"])

# User Input: Select Node Color
node_color = st.color_picker("Pick a color for the nodes", "#3498db")

# Load Groq API Key
api_key = "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"


# Initialize Groq Client
client = groq.Client(api_key=api_key)

# Define system prompt
system_prompt = f"""
You are an AI that generates structured {visual_type} diagrams using DOT language.
- Use {node_style} nodes.
- Use {edge_style} edges.
- Apply color {node_color} for the nodes.
- Ensure correct Graphviz DOT syntax.
- Output only valid DOT code without explanations.
"""

if st.button("Generate Visual"):
    with st.spinner("Generating your visual... ⏳"):
        try:
            response = client.chat.completions.create(
                model="llama-3.3-70b-versatile",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": user_prompt}
                ],
                temperature=0.5
            )

            # Extract and clean DOT code
            dot_code = response.choices[0].message.content.strip("```dot").strip("```")

            # Render and Display Graphviz Diagram (Only the Visuals)
            st.graphviz_chart(dot_code)

        except Exception as e:
            st.error(f"Failed to generate visuals: {e}")
