import streamlit as st

# Sample set of valid words
valid_words = {"example", "streamlit", "python", "spell", "checker", "app"}

def spell_check(text):
    words = text.split()
    corrected_words = [valid_word if valid_word in valid_words else f"_{word}_" for word in words]
    corrected_text = ' '.join(corrected_words)
    return corrected_text

def main():
    st.title("Basic Spell Checker App")
    st.write("Enter a sentence to check and correct spelling:")

    user_input = st.text_area("Input your text:")
    
    if st.button("Check and Correct"):
        result = spell_check(user_input.lower())  # Convert to lowercase for case-insensitive comparison
        st.success("Corrected Text:")
        st.write(result)

if __name__ == "__main__":
    main()
