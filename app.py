
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="For Roz 💗")

st.title("🎀 A Very Important Website 🎀")
st.write("Only one person is allowed to enter...")

name = st.text_input("State your name 👀")

if name:
    if name.strip().lower() in ["roselyn", "roz"]:

        st.success("IDENTITY CONFIRMED ✅")
        st.write("Welcome, birthday girl!!")

        answer = st.radio(
            "Who is the coolest (and shortest) person ever?",
            ["Choose one...", "Some random person",
             "Another random person", "Roz obviously"]
        )

        if answer == "Roz obviously":
            st.write("Wow u are very correct")

            if st.button("Open your present 🎁"):

                st.balloons()
                st.write("Drawing your present...")

                t = np.linspace(0, 2*np.pi, 300)

                x = 16*np.sin(t)**3
                y = (13*np.cos(t)
                     - 5*np.cos(2*t)
                     - 2*np.cos(3*t)
                     - np.cos(4*t))

                fig, ax = plt.subplots()
                ax.fill(x, y, color="hotpink")
                ax.plot(x, y, color="deeppink")
                ax.axis("equal")
                ax.axis("off")

                st.pyplot(fig)
                plt.close(fig)

                st.subheader("HAPPY BIRTHDAY ROZ!!! 💗")
                st.write("You're genuinely one of my favorite people.")
                st.write("I'm so glad we're best friends.")
                st.write("Love you lots!! 💕")

        elif answer != "Choose one...":
            st.error("WRONG ANSWER BRU 😭 Try again.")

    else:
        st.error("ACCESS DENIED 🚨")
        st.write("This website is for Roz only!")
