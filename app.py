import streamlit as st
import google.generativeai as genai
import random


api_key = "AIzaSyALNYu5js8raZ5ccF_W2MDdqPNq0frAoGs"
genai.configure(api_key=api_key)

generation_config = {
    "temperature": 0.75,
    "top_p": 0.95,
    "top_k": 64,
    "max_output_tokens": 8192,
    "response_mime_type": "text/plain",
}


def get_joke():
    jokes = [
        "Why don't programmers like nature? It has too many bugs.",
        "Why do Java developers wear glasses? Because they don't see sharp.",
        "How many programmers does it take to change a light bulb? None, that's a hardware problem.",
        "Why did the developer go broke? Because he used up all his cache.",
        "Why do programmers prefer dark mode? Because light attracts bugs!",
    ]
    return random.choice(jokes)



def generate_recipe(topic, word_count):
    try:
        st.write("🍽 Generating your recipe...")        
        st.write(f"🤖 While I work on your blog, here's a joke for you: \n\n {get_joke()}")

        chat_session = genai.GenerativeModel("gemini-1.5-flash").start_chat()

        prompt = f"Write a recipe blog on '{topic}' with {word_count} words."
        response = chat_session.send_message(prompt)

        st.success("✅ Your recipe is ready!")
        return response.text
    except Exception as e:
        st.error(f"Error generating blog: {e}")
        return None




def main():
    st.title("Flavour Fusion: AI-Driven Recipe Blogging 🍲🤖")

    st.write("### Generate AI-powered recipe blogs with ease!")

    topic = st.text_input("Enter your recipe topic:", placeholder="e.g., Vegan Chocolate Cake")
    word_count = st.number_input("Word count:", min_value=100, max_value=2000, step=100)

    if st.button("Generate Recipe"):
        if topic and word_count:
            recipe = generate_recipe(topic, word_count)
            if recipe:
                st.text_area("Generated Recipe:", recipe, height=300)
                st.download_button("Download Recipe", recipe, file_name=f"{topic}.txt")
        else:
            st.warning("Please enter a topic and word count.")

if __name__ == "__main__":
    main()