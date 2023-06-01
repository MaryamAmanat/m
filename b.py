import streamlit as st
import sqlite3
from session_state import SessionState

# Connect to the SQLite database
conn = sqlite3.connect('user.db')
c = conn.cursor()

# Create a users table if it doesn't exist
c.execute('''CREATE TABLE IF NOT EXISTS users
             (username TEXT PRIMARY KEY, password TEXT)''')
conn.commit()

# Function to create a new user
def create_user(username, password):
    try:
        c.execute("INSERT INTO users VALUES (?, ?)", (username, password))
        conn.commit()
        st.success("User created successfully!")
    except sqlite3.IntegrityError:
        st.error("Username already exists!")

# Function to validate user credentials
def validate_user(username, password):
    c.execute("SELECT * FROM users WHERE username=?", (username,))
    result = c.fetchone()
    if result:
        stored_password = result[1]
        if password == stored_password:
            return True
    return False

# Sign up section
def signup():
    st.subheader("Create a new account")
    new_username = st.text_input("Username")
    new_password = st.text_input("Password", type="password")

    if st.button("Sign Up"):
        if new_username and new_password:
            create_user(new_username, new_password)
        else:
            st.warning("Please enter a username and password.")

# Log in section
def login(session):
    st.subheader("Log in to your account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Log In"):
        if validate_user(username, password):
            session.logged_in = True
            session.username = username
        else:
            st.error("Invalid username or password.")

# Main app
def main():
    st.title("Career Counseling App with User Authentication")
    st.write("Welcome to the Career Counseling App!")

    session_state = SessionState(logged_in=False, username=None)

    if session_state.logged_in:
        career_counseling_app(session_state)
    else:
        login(session_state)
        if session_state.logged_in:
            career_counseling_app(session_state)

# Career Counseling App
def career_counseling_app(session):
    st.header("Career Counseling App")
    st.write(f"Welcome, {session.username}! Customize your career options!")

    # The rest of the app code goes here
    # ...

# Run the app
if __name__ == '__main__':
    main()
