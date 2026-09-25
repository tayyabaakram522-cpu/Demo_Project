import streamlit as st
import random

st.title("🎯 Number Guessing Game")
st.write("Guess a number between 1 and 10!")

# Create a random number once
if "number" not in st.session_state:
    st.session_state.number = random.randint(1, 10)

guess = st.number_input(
    "Enter your guess:",
    min_value=1,
    max_value=10,
    step=1
)

if st.button("Check Guess"):
    if guess == st.session_state.number:
        st.success("🎉 Correct! You guessed the number!")
    elif guess < st.session_state.number:
        st.info("📈 Too low! Try again.")
    else:
        st.warning("📉 Too high! Try again.")

if st.button("🔄 New Game"):
    st.session_state.number = random.randint(1, 10)
    st.rerun()