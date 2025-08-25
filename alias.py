import streamlit as st
import random

# Your word list
words = ["apple", "banana", "cherry", "dog", "elephant", "frog", "guitar"]

# Keep state across button clicks
if "remaining_words" not in st.session_state:
    st.session_state.remaining_words = words.copy()

st.title("🎲 Random Word Picker")

if st.button("Pick a Word"):
    if st.session_state.remaining_words:
        word = random.choice(st.session_state.remaining_words)
        st.write(f"👉 Your word is: **{word}**")
        st.session_state.remaining_words.remove(word)
    else:
        st.write("All words have been used!")
