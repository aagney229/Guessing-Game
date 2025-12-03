import streamlit as st
import random

st.title("🔢 Simple Guessing Game")

# Initialize the secret number in session state
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 100)
    st.session_state.msg = ""

# User input
guess = st.number_input("Enter your guess (1–100):", min_value=1, max_value=100, step=1)

if st.button("Guess"):
    if guess < st.session_state.secret:
        st.session_state.msg = "Too low! Try a higher number."
    elif guess > st.session_state.secret:
        st.session_state.msg = "Too high! Try a lower number."
    else:
        st.session_state.msg = "🎉 Correct! Click *Reset Game* to play again."

st.write(st.session_state.msg)

# Reset button
if st.button("Reset Game"):
    st.session_state.secret = random.randint(1, 100)
    st.session_state.msg = "Game reset! Make a new guess."

