import streamlit as st
import random

# ----------------------------
# Custom CSS for Styling
# ----------------------------
st.markdown("""
    <style>
    /* Main app background */
    .main {
        background-color: #f4f8fb;
    }

    /* Title style */
    h1, h2, h3, h4 {
        font-family: 'Trebuchet MS', sans-serif;
    }

    /* Card style */
    .card {
        border-radius: 12px;
        padding: 20px;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.2s ease-in-out;
    }
    .card:hover {
        transform: scale(1.03);
    }
    </style>
""", unsafe_allow_html=True)

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

def user_guessing_game():
    st.header("🧑‍💻 User Guessing Game")
    min_range = st.number_input("Enter the minimum value:", value=1)
    max_range = st.number_input("Enter the maximum value:", value=100)

    if 'secret_number' not in st.session_state or st.session_state.min_range != min_range or st.session_state.max_range != max_range:
        st.session_state.secret_number = random.randint(min_range, max_range)
        st.session_state.attempts = 0
        st.session_state.min_range = min_range
        st.session_state.max_range = max_range

    guess = st.number_input(f"Guess a number between {min_range} and {max_range}:", value=min_range)

    if st.button("Submit Guess"):
        st.session_state.attempts += 1
        if guess == st.session_state.secret_number:
            st.success(f"🎉 Congratulations! You guessed the number {st.session_state.secret_number} in {st.session_state.attempts} attempts.")
            del st.session_state.secret_number
        elif guess < st.session_state.secret_number:
            st.warning("📈 Try a higher number.")
        else:
            st.warning("📉 Try a lower number.")

def machine_guessing_game():
    st.header("🤖 Machine Guessing Game")
    st.write("Think of a number and guide the computer to guess it!")

    min_range = st.number_input("Enter the minimum value:", value=1)
    max_range = st.number_input("Enter the maximum value:", value=100)

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
            del st.session_state.guess
        else:
            st.session_state.guess = (st.session_state.min_range_m + st.session_state.max_range_m) // 2

# ----------------------------
# Portfolio Section
# ----------------------------
def portfolio_section():
    st.markdown("""
        <div style='background: linear-gradient(135deg, #00c6ff, #0072ff); padding: 40px; border-radius: 15px; color: white; text-align: center;'>
            <h1>Hello, I'm <span style='color: #ffeb3b;'>Sathish Kumar</span></h1>
            <h3>🚀 Aspiring AI & Data Science Enthusiast</h3>
            <h4 style='color: #00ff99;'>🎯 Aim: To Become a Successful Data Scientist</h4>
            <p>I am currently pursuing my <strong>2nd year in Artificial Intelligence and Data Science</strong> 🎓.<br>
            Passionate about blending creativity with technology, I enjoy solving problems through AI,
            exploring data patterns, and building innovative projects.</p>
        </div>
    """, unsafe_allow_html=True)

       # Skills Section with Hover Effect
    st.markdown(
        """
        <style>
        .skill-card {
            background: linear-gradient(135deg, #ff9a9e, #fad0c4);
            padding: 15px 25px;
            border-radius: 8px;
            font-size: 18px;
            font-weight: bold;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: 0 4px 6px rgba(0,0,0,0.1);
        }
        .skill-card:hover {
            transform: scale(1.1);
            box-shadow: 0 8px 15px rgba(0,0,0,0.2);
        }
        .skill-python {
            background: linear-gradient(135deg, #ffd700, #ffae00);
        }
        .skill-html {
            background: linear-gradient(135deg, #ff6a00, #ffcc70);
        }
        </style>

        <div style='margin-top: 40px; padding: 20px; border-radius: 10px; background: #f7f9fc; text-align:center;'>
            <h2 style='color: #0072ff;'>💡 Skills</h2>
            <div style='display: flex; gap: 20px; justify-content: center; flex-wrap: wrap;'>
                <div class='skill-card skill-python'>🐍 Python</div>
                <div class='skill-card skill-html'>🌐 HTML</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )


    st.markdown("""
        <div class='card' style='margin-top: 30px; background: #fff5e6;'>
            <h2 style='color: #ff6600;'>🎯 Goals</h2>
            <ul style='font-size: 18px; line-height: 1.8;'>
                <li>Become a Data Scientist</li>
                <li>Contribute to open-source AI projects</li>
                <li>Build AI-powered apps</li>
                <li>Work with top tech companies</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

       # Contact Section
    st.markdown(
        """
        <div style='margin-top: 40px; padding: 20px; border-radius: 10px; background: #e3f2fd; text-align: center;'>
            <h2 style='color: #0072ff;'>📬 Contact</h2>
            <a href='mailto:sathishkumar123bk@gmail.com' target='_blank' style='text-decoration: none;'>
                <button style='background: linear-gradient(135deg, #0072ff, #00c6ff); border: none; color: white; padding: 10px 25px; margin: 5px; border-radius: 8px; font-size: 16px; cursor: pointer;'>📧 Email</button>
            </a>
            <a href='https://www.linkedin.com/in/sathish-kumar-8340aa315' target='_blank' style='text-decoration: none;'>
                <button style='background: linear-gradient(135deg, #0a66c2, #0073b1); border: none; color: white; padding: 10px 25px; margin: 5px; border-radius: 8px; font-size: 16px; cursor: pointer;'>💼 LinkedIn</button>
            </a>
            <a href='https://github.com/sathish-BK' target='_blank' style='text-decoration: none;'>
                <button style='background: linear-gradient(135deg, #333, #000); border: none; color: white; padding: 10px 25px; margin: 5px; border-radius: 8px; font-size: 16px; cursor: pointer;'>💻 GitHub</button>
            </a>
        </div>
        """,
        unsafe_allow_html=True
    )

# ----------------------------
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
