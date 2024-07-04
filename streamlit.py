#!/usr/bin/env python
# coding: utf-8

# In[1]:


# pip install --trusted-host pypi.org --trusted-host files.pythonhosted.org streamlit


# In[3]:


# import streamlit as st

# st.write("Wordle")
# # w11 = st.text_area(label = "",max_chars=1)
# # st.write("The first letter is ", w11)
# [c1,c2,c3,c4,c5] = st.columns(5)
# with c1:
#     w11 = st.text_input(label = "",max_chars=1, key="w11")
# with c2:
#     w12 = st.text_input(label = "",max_chars=1, key="w12")
# with c3:
#     w13 = st.text_input(label = "",max_chars=1, key="w13")
# with c4:
#     w14 = st.text_input(label = "",max_chars=1, key="w14")
# with c5:
#     w15 = st.text_input(label = "",max_chars=1, key="w15")

import streamlit as st
from random import choice

# List of possible words
word_list = ["apple", "grape", "berry", "peach", "melon"]

# Select a random word to guess
if 'word_to_guess' not in st.session_state:
    st.session_state.word_to_guess = choice(word_list)

if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'attempts' not in st.session_state:
    st.session_state.attempts = []

st.title("Wordle Game")

# Function to check guess
def check_guess(guess, word_to_guess):
    feedback = ["gray"] * 5
    for i in range(5):
        if guess[i] == word_to_guess[i]:
            feedback[i] = "green"
        elif guess[i] in word_to_guess:
            feedback[i] = "yellow"
    return feedback

# Input for user guess
with st.form(key='guess_form', clear_on_submit=True):
    guess = st.text_input("Enter your guess:", max_chars=5).lower()
    submit_button = st.form_submit_button(label='Submit Guess')

if submit_button:
    if len(guess) == 5 and guess.isalpha():
        feedback = check_guess(guess, st.session_state.word_to_guess)
        st.session_state.attempts.append((guess, feedback))
        if guess == st.session_state.word_to_guess:
            st.session_state.submitted = True
    else:
        st.error("Please enter a valid 5-letter word.")

# Display attempts with colored feedback
for attempt, feedback in st.session_state.attempts:
    # Injecting CSS to color the input boxes based on feedback
    colored_guess = ""
    for i, char in enumerate(attempt):
        color = feedback[i]
        colored_guess += f'<span class="letter-{color}">{char.upper()}</span>'
    st.markdown(f'<div class="guess">{colored_guess}</div>', unsafe_allow_html=True)

if st.session_state.submitted:
    st.success(f"Congratulations! You guessed the word: {st.session_state.word_to_guess.upper()}")
    if st.button("Play Again"):
        st.session_state.word_to_guess = choice(word_list)
        st.session_state.submitted = False
        st.session_state.attempts = []

# Injecting CSS styles
st.markdown("""
<style>
    .letter-green {
        background-color: #6aaa64;
        color: white;
        padding: 5px;
        margin: 2px;
        border-radius: 3px;
    }
    .letter-yellow {
        background-color: #c9b458;
        color: white;
        padding: 5px;
        margin: 2px;
        border-radius: 3px;
    }
    .letter-gray {
        background-color: #787c7e;
        color: white;
        padding: 5px;
        margin: 2px;
        border-radius: 3px;
    }
    .guess {
        display: flex;
        justify-content: center;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)
