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

# Career Counseling App
def career_counseling_app():
    st.title("Career Counseling App")
    st.write("Welcome to the Career Counseling App!")
    
    # Add your app code here
    # ...
    # ...
    
   
    
    # Hobbies section
    st.header("Hobbies")
    st.write("Select your hobbies:")
    hobbies = st.multiselect("Choose hobbies", [
        "Painting",
        "Playing an instrument",
        "Sports",
        "Cooking",
        "Writing",
        "Photography"
    ])
    
    # Interests section
    st.header("Interests")
    st.write("Select your interests:")
    interests = st.multiselect("Choose interests", [
        "Technology",
        "Art and Design",
        "Business and Finance",
        "Healthcare",
        "Education",
        "Environment"
    ])
    
    # Favorite subjects section
    st.header("Favorite Subjects")
    st.write("Select your favorite subjects:")
    favorite_subjects = st.multiselect("Choose favorite subjects", [
        "Mathematics",
        "Science",
        "History",
        "Literature",
        "Computer Science",
        "Art"
    ])
    
    # Career suggestion section
    st.header("Career Suggestions")
    st.write("Based on your selections, here are some career suggestions:")
    
    if "Painting" in hobbies and "Art and Design" in interests:
        st.subheader("Fine Artist")
        st.write("Description: As a fine artist, you can express your creativity through various artistic mediums such as painting, sculpture, or mixed media.")
        st.write("Specialties: Abstract art, landscape painting, portrait drawing")
        st.write("---")
        
    if "Playing an instrument" in hobbies and "Art and Design" in interests:
        st.subheader("Musician")
        st.write("Description: As a musician, you can pursue a career in playing an instrument, composing music, or performing in bands or orchestras.")
        st.write("Specialties: Piano, guitar, violin")
        st.write("---")
        
    if "Sports" in hobbies and "Healthcare" in interests:
        st.subheader("Sports Physiotherapist")
        st.write("Description: As a sports physiotherapist, you can work with athletes to prevent and treat sports-related injuries, helping them to recover and enhance their performance.")
        st.write("Specialties: Sports rehabilitation, injury prevention")
        st.write("---")
        
    # Add more career suggestions based on the user's choices
    
    

# Main app
def main():
    st.title("User Authentication and Career Counseling App")
    st.write("Welcome to the app!")

    # Sidebar navigation
    page = st.sidebar.radio("Navigation", ("Login", "Signup","career_counseling_ap"))
    if page == "Login":
      if login():  # Check if login is successful
        career_counseling_app()
    elif page == "Signup":
      signup()



# Run the app
if __name__ == '__main__':
    main()
   
