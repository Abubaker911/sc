import streamlit as st
from spellchecker import SpellChecker

def spell_check(text):
    spell = SpellChecker()
    # Split the input text into words
    words = text.split()
    
    # Find and correct misspelled words
    corrected_text = []
    for word in words:
        corrected_text.append(spell.correction(word))
    
    # Join the corrected words back into a sentence
    result = ' '.join(corrected_text)
    return result

def main():
    st.title("Spellchecker App")
    
    # Input textarea for the user to enter text
    user_input = st.text_area("Enter text for spellchecking:", "")
    
    if st.button("Check Spelling"):
        # Perform spell check when the button is clicked
        result = spell_check(user_input)
        st.markdown(f"**Corrected Text:**\n{result}")

if __name__ == "__main__":
    main()

