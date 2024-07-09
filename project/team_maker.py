#!/usr/bin/env python
# coding: utf-8

# In[ ]:

# import streamlit as st
# import random

# # Initialize session state
# if 'players' not in st.session_state:
#     st.session_state.players = [""] * 12
# if 'ratings' not in st.session_state:
#     st.session_state.ratings = [""] * 12

# # Function to add a new player input field
# def add_player():
#     st.session_state.players.append("")
#     st.session_state.ratings.append("")

# # Function to clear player input fields
# def clear_players():
#     st.session_state.players = [""] * 12
#     st.session_state.ratings = [""] * 12

# # Function to generate fair teams
# def generate_teams(players, ratings):
#     combined = list(zip(players, ratings))
#     combined = [(p, int(r)) for p, r in combined if p and r.isdigit()]  # Filter out invalid entries and convert ratings to integers
#     combined.sort(key=lambda x: x[1], reverse=True)  # Sort by rating, highest first

#     team_a, team_b = [], []
#     sum_a, sum_b = 0, 0

#     for player, rating in combined:
#         if sum_a <= sum_b:
#             team_a.append((player, rating))
#             sum_a += rating
#         else:
#             team_b.append((player, rating))
#             sum_b += rating

#     return team_a, team_b

# # Layout with two columns
# col1, col2 = st.columns(2)

# # Left side for player input
# with col1:
#     st.header("Player Names & Ratings")
#     clear_player_button = st.button("Clear All", on_click=clear_players)
#     add_player_button = st.button("Add Player", on_click=add_player)

#     for i in range(len(st.session_state.players)):
#         col_name, col_rating = st.columns([2, 1])
#         st.session_state.players[i] = col_name.text_input(f"Player {i+1} Name", st.session_state.players[i], key=f"player_{i}")
#         st.session_state.ratings[i] = col_rating.text_input(f"Rating", st.session_state.ratings[i], key=f"rating_{i}")

# # Right side for displaying teams
# with col2:
#     st.header("Fair Teams")
#     if st.session_state.players and st.session_state.ratings:
#         team_a, team_b = generate_teams(st.session_state.players, st.session_state.ratings)

#         col_a, col_b = st.columns(2)

#         with col_a:
#             st.subheader("Team A")
#             for player, rating in team_a:
#                 st.write(f"{player} - Rating: {rating}")

#         with col_b:
#             st.subheader("Team B")
#             for player, rating in team_b:
#                 st.write(f"{player} - Rating: {rating}")
import streamlit as st
import random

# Initialize session state
if 'players' not in st.session_state:
    st.session_state.players = [""] * 12
if 'ratings' not in st.session_state:
    st.session_state.ratings = [""] * 12

# Function to add a new player input field
def add_player():
    st.session_state.players.append("")
    st.session_state.ratings.append("")

# Function to clear player input fields
def clear_players():
    st.session_state.players = [""] * 12
    st.session_state.ratings = [""] * 12

# Function to remove a player input field
def remove_player(index):
    st.session_state.players.pop(index)
    st.session_state.ratings.pop(index)

# Function to generate fair teams
def generate_teams(players, ratings):
    combined = list(zip(players, ratings))
    combined = [(p, int(r)) for p, r in combined if p and r.isdigit()]  # Filter out invalid entries and convert ratings to integers
    combined.sort(key=lambda x: x[1], reverse=True)  # Sort by rating, highest first

    team_a, team_b = [], []
    sum_a, sum_b = 0, 0

    for player, rating in combined:
        if sum_a <= sum_b:
            team_a.append((player, rating))
            sum_a += rating
        else:
            team_b.append((player, rating))
            sum_b += rating

    return team_a, team_b

# Layout with two columns
col1, col2 = st.columns(2)

# Left side for player input
with col1:
    st.header("Player Input")
    clear_player_button = st.button("Clear All", on_click=clear_players)
    add_player_button = st.button("Add Player", on_click=add_player)

    for i in range(len(st.session_state.players)):
        col_name, col_rating, col_remove = st.columns([2, 1, 2])
        st.session_state.players[i] = col_name.text_input(f"Player {i+1} Name", st.session_state.players[i], key=f"player_{i}")
        st.session_state.ratings[i] = col_rating.text_input(f"Rating", st.session_state.ratings[i], key=f"rating_{i}")
        remove_button = col_remove.button("remove", key=f"remove_{i}", on_click=remove_player, args=(i,))

# Right side for displaying teams
with col2:
    st.header("Fair Teams")
    if st.session_state.players and st.session_state.ratings:
        team_a, team_b = generate_teams(st.session_state.players, st.session_state.ratings)

        col_a, col_b = st.columns(2)

        with col_a:
            st.subheader("Team A")
            for player, rating in team_a:
                st.write(f"{player} - Rating: {rating}")

        with col_b:
            st.subheader("Team B")
            for player, rating in team_b:
                st.write(f"{player} - Rating: {rating}")

