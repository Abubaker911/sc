import streamlit as st
from autocorrect import Speller

def autocorrect_text(input_text):
    spell = Speller()
    corrected_text = spell(input_text)
    return corrected_text

def main():
    st.title("Text Autocorrect App")
    
    # Get user input
    user_input = st.text_area("Enter text:")

    # Perform autocorrection
    corrected_output = autocorrect_text(user_input)

    # Display corrected output
    st.write("Autocorrected Text:")
    st.write(corrected_output)

if __name__ == "__main__":
    main()
