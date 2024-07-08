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
import os
import streamlit as st
from random import choice
from english_words import get_english_words_set
web2lowerset = get_english_words_set(['web2'], lower=True)
valid_words = [x for x in web2lowerset if len(x)==5]

# #Download necessary nltk data if not already present
# os.system("python additional_libraries_downloader.py")

# import nltk
# nltk.download('wordnet')
# nltk.download('omw-1.4')
# from nltk.corpus import wordnet
# Check if the word is a valid English word
# def is_valid_word(word):
#     return bool(wordnet.synsets(word))


# List of possible words
# word_list = ["apple", "grape", "berry", "peach", "melon"]
word_list = ['about',
 'above',
 'abuse',
 'actor',
 'acute',
 'admit',
 'adopt',
 'adult',
 'after',
 'again',
 'agent',
 'agree',
 'ahead',
 'alarm',
 'album',
 'boost',
 'booth',
 'bound',
 'brain',
 'brand',
 'bread',
 'break',
 'breed',
 'brief',
 'bring',
 'broad',
 'broke',
 'brown',
 'build',
 'built',
 'debut',
 'delay',
 'depth',
 'doing',
 'doubt',
 'dozen',
 'draft',
 'drama',
 'drawn',
 'dream',
 'dress',
 'drill',
 'drink',
 'drive',
 'drove',
 'dying',
 'eager',
 'early',
 'earth',
 'eight',
 'elite',
 'empty',
 'enemy',
 'enjoy',
 'enter',
 'judge',
 'known',
 'label',
 'large',
 'laser',
 'later',
 'laugh',
 'layer',
 'learn',
 'lease',
 'least',
 'leave',
 'legal',
 'level',
 'light',
 'limit',
 'peace',
 'panel',
 'phase',
 'phone',
 'photo',
 'piece',
 'pilot',
 'pitch',
 'place',
 'plain',
 'plane',
 'plant',
 'plate',
 'point',
 'pound',
 'sheet',
 'shelf',
 'shell',
 'shift',
 'shirt',
 'shock',
 'shoot',
 'short',
 'shown',
 'sight',
 'since',
 'sixty',
 'sized',
 'skill',
 'sleep',
 'slide',
 'small',
 'smart',
 'smile',
 'smith',
 'smoke',
 'solid',
 'solve',
 'sorry',
 'sound',
 'south',
 'space',
 'upset',
 'urban',
 'usage',
 'usual',
 'valid',
 'value',
 'video',
 'virus',
 'visit',
 'alert',
 'alike',
 'alive',
 'allow',
 'alone',
 'along',
 'alter',
 'among',
 'anger',
 'angle',
 'angry',
 'apart',
 'apple',
 'apply',
 'arena',
 'buyer',
 'cable',
 'calif',
 'carry',
 'catch',
 'cause',
 'chain',
 'chair',
 'chart',
 'chase',
 'cheap',
 'check',
 'chest',
 'chief',
 'child',
 'entry',
 'equal',
 'error',
 'event',
 'every',
 'exact',
 'exist',
 'extra',
 'faith',
 'false',
 'fault',
 'fibre',
 'field',
 'fifth',
 'fifty',
 'fight',
 'final',
 'first',
 'fixed',
 'flash',
 'fleet',
 'floor',
 'fluid',
 'focus',
 'force',
 'metal',
 'local',
 'logic',
 'loose',
 'lower',
 'lucky',
 'lunch',
 'lying',
 'magic',
 'major',
 'maker',
 'march',
 'music',
 'match',
 'mayor',
 'meant',
 'power',
 'press',
 'price',
 'pride',
 'prime',
 'print',
 'prior',
 'prize',
 'proof',
 'proud',
 'prove',
 'queen',
 'sixth',
 'quiet',
 'quite',
 'spare',
 'speak',
 'speed',
 'spend',
 'spent',
 'split',
 'spoke',
 'sport',
 'staff',
 'stage',
 'stake',
 'start',
 'state',
 'steam',
 'steel',
 'stick',
 'still',
 'stock',
 'stone',
 'stood',
 'store',
 'storm',
 'story',
 'strip',
 'stuck',
 'study',
 'stuff',
 'whole',
 'whose',
 'woman',
 'train',
 'world',
 'worry',
 'worse',
 'worst',
 'would',
 'argue',
 'arise',
 'array',
 'aside',
 'asset',
 'audio',
 'audit',
 'avoid',
 'award',
 'aware',
 'badly',
 'baker',
 'bases',
 'basic',
 'basis',
 'china',
 'chose',
 'civil',
 'claim',
 'class',
 'clean',
 'clear',
 'click',
 'clock',
 'close',
 'coach',
 'coast',
 'could',
 'count',
 'court',
 'forth',
 'forty',
 'forum',
 'found',
 'frame',
 'frank',
 'fraud',
 'fresh',
 'front',
 'fruit',
 'fully',
 'funny',
 'giant',
 'given',
 'glass',
 'globe',
 'going',
 'grace',
 'grade',
 'grand',
 'grant',
 'grass',
 'great',
 'green',
 'gross',
 'media',
 'might',
 'minor',
 'minus',
 'mixed',
 'model',
 'money',
 'month',
 'moral',
 'motor',
 'mount',
 'mouse',
 'mouth',
 'movie',
 'needs',
 'never',
 'radio',
 'raise',
 'range',
 'rapid',
 'ratio',
 'reach',
 'ready',
 'refer',
 'right',
 'rival',
 'river',
 'quick',
 'stand',
 'roman',
 'rough',
 'style',
 'sugar',
 'suite',
 'super',
 'sweet',
 'table',
 'taken',
 'taste',
 'taxes',
 'teach',
 'teeth',
 'texas',
 'thank',
 'theft',
 'their',
 'theme',
 'there',
 'these',
 'thick',
 'thing',
 'think',
 'third',
 'those',
 'three',
 'threw',
 'throw',
 'tight',
 'waste',
 'watch',
 'water',
 'wheel',
 'where',
 'which',
 'while',
 'white',
 'vital',
 'beach',
 'began',
 'begin',
 'begun',
 'being',
 'below',
 'bench',
 'billy',
 'birth',
 'black',
 'blame',
 'blind',
 'block',
 'blood',
 'board',
 'cover',
 'craft',
 'crash',
 'cream',
 'crime',
 'cross',
 'crowd',
 'crown',
 'curve',
 'cycle',
 'daily',
 'dance',
 'dated',
 'dealt',
 'death',
 'group',
 'grown',
 'guard',
 'guess',
 'guest',
 'guide',
 'happy',
 'harry',
 'heart',
 'heavy',
 'hence',
 'night',
 'horse',
 'hotel',
 'house',
 'human',
 'ideal',
 'image',
 'index',
 'inner',
 'input',
 'issue',
 'irony',
 'juice',
 'joint',
 'newly',
 'noise',
 'north',
 'noted',
 'novel',
 'nurse',
 'occur',
 'ocean',
 'offer',
 'often',
 'order',
 'other',
 'ought',
 'paint',
 'paper',
 'party',
 'round',
 'route',
 'royal',
 'rural',
 'scale',
 'scene',
 'scope',
 'score',
 'sense',
 'serve',
 'seven',
 'shall',
 'shape',
 'share',
 'sharp',
 'times',
 'tired',
 'title',
 'today',
 'topic',
 'total',
 'touch',
 'tough',
 'tower',
 'track',
 'trade',
 'treat',
 'trend',
 'trial',
 'tried',
 'tries',
 'truck',
 'truly',
 'trust',
 'truth',
 'twice',
 'under',
 'undue',
 'union',
 'unity',
 'until',
 'upper',
 'wound',
 'write',
 'wrong',
 'wrote',
 'yield',
 'young',
 'youth',
 'worth',
 'voice']

# Select a random word to guess
if 'word_to_guess' not in st.session_state:
    st.session_state.word_to_guess = choice(word_list)
if 'submitted' not in st.session_state:
    st.session_state.submitted = False
if 'attempts' not in st.session_state:
    st.session_state.attempts = []
if 'attempt_count' not in st.session_state:
    st.session_state.attempt_count = 0
if 'game_over' not in st.session_state:
    st.session_state.game_over = False

st.title("Wordle Game")
st.write("created by - Khush Tailor")

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
    col1, col2, col3, col4, col5 = st.columns([1, 1, 1, 1, 1])
    with col1:
        submit_button = st.form_submit_button(label='Submit Guess')
    with col5:
        reset_button = st.form_submit_button(label='Reset Game')

# if submit_button:
#     if len(guess) == 5 and guess.isalpha() and (guess in valid_words) and (attempt_count<6):
#         attempt_count+=1
#         st.write(attempt_count)
#         feedback = check_guess(guess, st.session_state.word_to_guess)
#         st.session_state.attempts.append((guess, feedback))
#         if guess == st.session_state.word_to_guess:
#             st.session_state.submitted = True
#     elif attempt_count == 6:
#         st.error("Sorry! you have reached maximum atempts.")
#     else:
#         st.error("Please enter a valid 5-letter word.")
if submit_button and not st.session_state.game_over:
    if len(guess) == 5 and guess.isalpha() and guess in valid_words:
        feedback = check_guess(guess, st.session_state.word_to_guess)
        st.session_state.attempts.append((guess, feedback))
        st.session_state.attempt_count += 1
        if guess == st.session_state.word_to_guess:
            st.session_state.submitted = True
            st.session_state.game_over = True
            st.success(f"Congratulations! You guessed the word: {st.session_state.word_to_guess.upper()}")
        elif st.session_state.attempt_count == 6:
            st.session_state.game_over = True
            st.error(f"Game Over! The word was: {st.session_state.word_to_guess.upper()}")
    else:
        st.error(f"{guess} is not a valid word. Please enter a valid 5-letter word.")

if reset_button:
    st.session_state.word_to_guess = choice(word_list)
    st.session_state.submitted = False
    st.session_state.attempts = []
    st.session_state.attempt_count = 0
    st.session_state.game_over = False

# Display attempts with colored feedback
for attempt, feedback in st.session_state.attempts:
    # Injecting CSS to color the input boxes based on feedback
    colored_guess = ""
    for i, char in enumerate(attempt):
        color = feedback[i]
        colored_guess += f'<span class="letter-{color}">{char.upper()}</span>'
    st.markdown(f'<div class="guess">{colored_guess}</div>', unsafe_allow_html=True)

# if st.session_state.submitted:
# #     st.success(f"Congratulations! You guessed the word: {st.session_state.word_to_guess.upper()}")
#     if st.button("Play Again"):
#         st.session_state.word_to_guess = choice(word_list)
#         st.session_state.submitted = False
#         st.session_state.attempts = []

# Injecting CSS styles
st.markdown("""
<style>
    .letter-green {
        background-color: #6aaa64;
        color: white;
        padding: 7px;
        margin: 4px;
        border-radius: 3px;
    }
    .letter-yellow {
        background-color: #c9b458;
        color: white;
        padding: 7px;
        margin: 4px;
        border-radius: 3px;
    }
    .letter-gray {
        background-color: #787c7e;
        color: white;
        padding: 7px;
        margin: 4px;
        border-radius: 3px;
    }
    .guess {
        display: flex;
        justify-content: center;
        margin-bottom: 10px;
    }
</style>
""", unsafe_allow_html=True)
