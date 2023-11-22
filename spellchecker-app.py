import streamlit as st

# Sample set of valid words
valid_words = {"example", "streamlit", "python", "spell", "checker", "app"}

def get_closest_word(word):
    return min(valid_words, key=lambda valid_word: levenshtein_distance(word, valid_word))

def levenshtein_distance(s1, s2):
    if len(s1) > len(s2):
        s1, s2 = s2, s1

    distances = range(len(s1) + 1)
    for index2, char2 in enumerate(s2):
        new_distances = [index2 + 1]
        for index1, char1 in enumerate(s1):
            if char1 == char2:
                new_distances.append(distances[index1])
            else:
                new_distances.append(1 + min((distances[index1], distances[index1 + 1], new_distances[-1])))
        distances = new_distances

    return distances[-1]

def spell_check(text):
    words = text.split()
    corrected_words = [get_closest_word(word) if word not in valid_words else word for word in words]
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
