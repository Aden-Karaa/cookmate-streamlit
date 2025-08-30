import streamlit as st
import google.generativeai as genai

# Directly using your API key (for local testing only)
genai.configure(api_key="AIzaSyC1qv_URnyKEbXuyYfmy-A6x4CnEpoWUBs")

model = genai.GenerativeModel("gemini-2.5-flash")

def get_recipe(ingredients):
    prompt = f"Suggest a creative, beginner-friendly recipe using only these ingredients: {ingredients}. Include a fun name and simple instructions."
    response = model.generate_content(prompt)
    return response.text

# Streamlit UI
st.title("🍳 CookMate AI")
st.write("Tell me what ingredients you have, and I’ll whip up a recipe!")

ingredients = st.text_input("Enter your ingredients (comma-separated):")

if ingredients:
    st.info("🧠 CookMate AI is cooking up a recipe...")
    recipe = get_recipe(ingredients)
    st.subheader("🍽️ Here's your dish:")
    st.write(recipe)
