import streamlit as st
import random

# ----------------------------
# Guessing Game Section
# ----------------------------
def guessing_game_section():
    st.title("🎯 Guessing Game")

    game_mode = st.selectbox("Choose the game mode:", ["User Guessing", "Machine Guessing"])

    if game_mode == "User Guessing":
        user_guessing_game()
    else:
        machine_guessing_game()

# ----------------------------
# User Guessing Game
# ----------------------------
def user_guessing_game():
    st.header("🧑‍💻 User Guessing Game")

    min_range = st.number_input("Enter the minimum value:", value=1)
    max_range = st.number_input("Enter the maximum value:", value=100)

    # Store the secret number in session_state so it doesn't change
    if 'secret_number' not in st.session_state or st.session_state.min_range != min_range or st.session_state.max_range != max_range:
        st.session_state.secret_number = random.randint(min_range, max_range)
        st.session_state.attempts = 0
        st.session_state.min_range = min_range
        st.session_state.max_range = max_range

    guess = st.number_input(f"Guess a number between {min_range} and {max_range}:", value=min_range)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess == st.session_state.secret_number:
            st.success(f"🎉 Congratulations! You guessed the number {st.session_state.secret_number} "
                       f"in {st.session_state.attempts} attempts.")
            del st.session_state.secret_number  # reset for a new game
        elif guess < st.session_state.secret_number:
            st.warning("📈 Try a higher number.")
        else:
            st.warning("📉 Try a lower number.")

# ----------------------------
# Machine Guessing Game
# ----------------------------
def machine_guessing_game():
    st.header("🤖 Machine Guessing Game")
    st.write("**Rules:**")
    st.write("1. Think of a number and set a range for it.")
    st.write("2. The computer will try to guess your number.")
    st.write("3. Tell the computer if it should guess higher or lower.")

    min_range = st.number_input("Enter the minimum value:", value=1)
    max_range = st.number_input("Enter the maximum value:", value=100)

    # Initialize game
    if 'guess' not in st.session_state or st.session_state.min_range_m != min_range or st.session_state.max_range_m != max_range:
        st.session_state.min_range_m = min_range
        st.session_state.max_range_m = max_range
        st.session_state.guess = (min_range + max_range) // 2

    st.write(f"💻 Computer guesses: **{st.session_state.guess}**")

    feedback = st.selectbox("Your feedback:", ["Too High", "Too Low", "Correct"])

    if st.button("Submit Feedback"):
        if feedback == "Too High":
            st.session_state.max_range_m = st.session_state.guess - 1
        elif feedback == "Too Low":
            st.session_state.min_range_m = st.session_state.guess + 1

        if feedback == "Correct":
            st.success(f"🎯 The computer guessed your number: {st.session_state.guess}")
            del st.session_state.guess  # reset for new game
        else:
            st.session_state.guess = (st.session_state.min_range_m + st.session_state.max_range_m) // 2

# ----------------------------
# Portfolio Section
# ----------------------------
def portfolio_section():
    st.markdown(
        """
        <section style="background: linear-gradient(135deg, #00c6ff, #0072ff); color: white; padding: 50px 20px; font-family: 'Poppins', sans-serif; border-radius: 10px;">
          <div style="max-width: 1000px; margin: auto; text-align: center;">
            <h1 style="font-size: 40px; font-weight: bold; margin-bottom: 10px;">
              Hello, I'm <span style="color: #ffeb3b;">Sathish Kumar</span>
            </h1>
            <h3 style="font-size: 20px; font-weight: 300; margin-bottom: 10px;">🚀 Aspiring AI & Data Science Enthusiast</h3>
            <h3 style="color: #00ff99; font-weight: 500; margin-bottom: 30px;">🎯 My Aim: To Become a Successful Data Scientist</h3>
            
            <p style="font-size: 18px; line-height: 1.8; max-width: 800px; margin: auto;">
              I am currently pursuing my <strong>2nd year in Artificial Intelligence and Data Science</strong> 🎓. 
              Passionate about blending creativity with technology, I enjoy solving problems through AI, 
              exploring data patterns, and building innovative projects that make an impact.
            </p>
            
            <div style="display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; margin-top: 40px;">
              <div style="background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 10px; width: 250px;">
                <h4 style="color: #ffeb3b;">💡 Skills</h4>
                <ul style="list-style: none; padding: 0; margin: 0; text-align: left;">
                  <li>Python, C Programming</li>
                  <li>Machine Learning Basics</li>
                  <li>Data Visualization</li>
                  <li>Web Development (HTML, CSS)</li>
                </ul>
              </div>
              
              <div style="background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 10px; width: 250px;">
                <h4 style="color: #ffeb3b;">🎯 Goals</h4>
                <ul style="list-style: none; padding: 0; margin: 0; text-align: left;">
                  <li>Become a Data Scientist</li>
                  <li>Contribute to open-source AI projects</li>
                  <li>Build AI-powered apps</li>
                  <li>Work with top tech companies</li>
                </ul>
              </div>
              
              <div style="background: rgba(255, 255, 255, 0.1); padding: 20px; border-radius: 10px; width: 250px;">
                <h4 style="color: #ffeb3b;">📬 Contact</h4>
                <ul style="list-style: none; padding: 0; margin: 0; text-align: left;">
                  <li>Email: <a href="mailto:sathishkumar@example.com" style="color: white;">sathishkumar@example.com</a></li>
                  <li>LinkedIn: <a href="#" style="color: white;">linkedin.com/in/sathishkumar</a></li>
                  <li>GitHub: <a href="#" style="color: white;">github.com/sathishkumar</a></li>
                </ul>
              </div>
            </div>
          </div>
        </section>
        """,
        unsafe_allow_html=True
    )

# -------------------------
# Main App
# ----------------------------
def main():
    st.sidebar.title("Navigation")
    choice = st.sidebar.selectbox("Choose a section:", ["Portfolio", "Guessing Game"])

    if choice == "Portfolio":
        portfolio_section()
    else:
        guessing_game_section()

if __name__ == "__main__":
    main()
