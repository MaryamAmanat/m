import streamlit as st
import sqlite3

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
def login():
    st.subheader("Log in to your account")
    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Log In"):
        if validate_user(username, password):
            st.success(f"Logged in as {username}!")
            career_counseling_app()
        else:
            st.error("Invalid username or password.")
            
career_options = {
    'Hobby': {
        'Sports': ['Athlete', 'Sports Coach', 'Sports Journalist'],
        'Music': ['Musician', 'Music Teacher', 'Sound Engineer'],
        'Cooking': ['Chef', 'Food Critic', 'Culinary Instructor']
    },
    'Interest': {
        'Technology': ['Software Developer', 'Data Scientist', 'IT Consultant'],
        'Art': ['Artist', 'Graphic Designer', 'Art Director'],
        'Science': ['Scientist', 'Researcher', 'Pharmacist']
    },
    'Subject': {
        'Mathematics': ['Mathematician', 'Financial Analyst', 'Statistician'],
        'Language': ['Translator', 'Copywriter', 'Interpreter'],
        'History': ['Historian', 'Archaeologist', 'Curator']
    }
}

# Career Counseling App
def career_counseling_app():
    st.title("Career Counseling App")
    st.write("Welcome to the Career Counseling App!")

    # Get user inputs
    hobbies = st.multiselect("Select your hobbies", list(career_options['Hobby'].keys()))
    interests = st.multiselect("Select your interests", list(career_options['Interest'].keys()))
    subjects = st.multiselect("Select your favorite subjects", list(career_options['Subject'].keys()))

    # Show suggested careers based on user inputs
    st.subheader("Suggested Careers")
    suggested_careers = set()
    for hobby in hobbies:
        suggested_careers.update(career_options['Hobby'].get(hobby, []))
    for interest in interests:
        suggested_careers.update(career_options['Interest'].get(interest, []))
    for subject in subjects:
        suggested_careers.update(career_options['Subject'].get(subject, []))

    if len(suggested_careers) > 0:
        for career in suggested_careers:
            st.write("- " + career)
    else:
        st.write("No suggested careers based on your inputs.")

def about_us():
    st.title("About Us")
    st.write("Welcome to the Career Counseling App!")
    st.write("This app is designed to help you explore various career options based on your hobbies, interests, and favorite subjects.")
    st.write("We provide personalized career suggestions to assist you in making informed decisions about your future.")
    st.write("Feel free to explore the app and discover exciting career paths!")

# Main app
def main():
    st.title("User Authentication and Career Counseling App")
    st.write("Welcome to the app!")

    # Sidebar navigation
    page = st.sidebar.radio("Navigation", ("Login", "Signup", "Career Counseling", "About Us"))

    if page == "Login":
        login()
    elif page == "Signup":
        signup()
    elif page == "Career Counseling":
        if login():  # Check if login is successful
            career_counseling_app()
    elif page == "About Us":
        about_us()

# Run the app
if __name__ == '__main__':
    main()
    career_counseling_app()
         # Call career_counseling_app outside of main()
    


   
