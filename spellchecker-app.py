import streamlit as st
from spellchecker import SpellChecker

# Initialize the spellchecker
spell = SpellChecker()

def spell_check(text):
    words = text.split()
    misspelled = spell.unknown(words)
    
    # Correct misspelled words
    corrected_text = ' '.join(spell.correction(word) if word in misspelled else word for word in words)
    
    return corrected_text

def main():
    st.title("Spell Checker App")
    st.write("Enter a sentence to check and correct spelling:")

    user_input = st.text_area("Input your text:")
    
    if st.button("Check and Correct"):
        result = spell_check(user_input)
        st.success("Corrected Text:")
        st.write(result)

if __name__ == "__main__":
    main()
