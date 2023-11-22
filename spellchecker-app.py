import streamlit as st
import nltk
from nltk.metrics.distance import edit_distance
from nltk.corpus import words

nltk.download('words')
english_words = set(words.words())

def get_closest_word(word):
    min_distance = float('inf')
    closest_word = None
    for w in english_words:
        distance = edit_distance(word, w)
        if distance < min_distance:
            min_distance = distance
            closest_word = w
    return closest_word

def spell_checker_game():
    st.title("Spell Checker Game")

    user_input = st.text_input("Enter a word (or type 'quit' to exit):").lower()

    if user_input == 'quit':
        st.success("Thank you for playing! Exiting the game.")
        return

    if user_input in english_words:
        st.success("Correct! '{}' is a valid English word.".format(user_input))
    else:
        closest_word = get_closest_word(user_input)
        st.warning("Did you mean '{}'?".format(closest_word))

if __name__ == "__main__":
    spell_checker_game()
