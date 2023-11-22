import streamlit as st
import enchant

# Initialize the spellchecker
spell_checker = enchant.Dict("en_US")

def spell_check(text):
    words = text.split()
    corrected_words = [spell_checker.suggest(word)[0] if not spell_checker.check(word) else word for word in words]
    corrected_text = ' '.join(corrected_words)
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
