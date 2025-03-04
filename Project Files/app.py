import streamlit as st
import google.generativeai as genai
import random
import os

# Set page config
st.set_page_config(page_title="Flavour Fusion: AI-Driven Recipe Blogging", layout="wide")

# Get API Key from environment variable
API_KEY = os.getenv("GOOGLE_API_KEY")
if not API_KEY:
    st.error("API Key is missing! Set it as GOOGLE_API_KEY in environment variables.")
    st.stop()

# Configure Gemini API
genai.configure(api_key=API_KEY)

# Function to generate a programmer joke
def get_joke():
    jokes = [
        "Why don't programmers like nature? It has too many bugs.",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Why did the developer go broke? Because he used up all his cache."
    ]
    return random.choice(jokes)

# Function to generate a recipe blog
def generate_recipe(user_input, word_count):
    try:
        st.write("🍲 Generating your recipe...")

        # Show a joke while generating the recipe
        st.write(f"💡 While I work on your blog, here's a joke: *{get_joke()}*")

        # Start chat session with Gemini model
        chat_session = genai.GenerativeModel("gemini-1.5-flash").start_chat()
        
        response = chat_session.send_message(f"Write a recipe blog on {user_input} in {word_count} words.")

        st.success("✅ Your recipe is ready!")
        return response.text

    except Exception as e:
        st.error(f"Error generating blog: {e}")
        return None

# Streamlit UI
st.title("🍽️ Flavour Fusion: AI-Driven Recipe Blogging")
st.write("Create AI-generated recipe blogs effortlessly!")

# User input fields
user_input = st.text_input("🔍 Enter your recipe topic:", placeholder="Vegan Chocolate Cake")
word_count = st.slider("📝 Select word count:", 500, 2000, 1000)

# Generate button
if st.button("Generate Recipe"):
    if user_input:
        recipe = generate_recipe(user_input, word_count)
        if recipe:
            st.subheader("📜 Generated Recipe Blog")
            st.write(recipe)
    else:
        st.warning("⚠️ Please enter a recipe topic.")

# Footer
st.markdown("---")
st.write("🔗 Created with ❤️ using Streamlit & Google Generative AI")
