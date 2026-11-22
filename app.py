
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

st.title("A little birthday surprise :)")

name = st.text_input("What's your name?")

if name:
    if name.lower().strip() in ["roselyn", "roz"]:
        st.write("HAPPY BIRTHDAY ROZ!! 🎉")
        st.write("I made you something...")

        if st.button("Click here 💗"):
            t = np.linspace(0, 2 * np.pi, 300)

            x = 16 * np.sin(t)**3
            y = (13 * np.cos(t)
                 - 5 * np.cos(2*t)
                 - 2 * np.cos(3*t)
                 - np.cos(4*t))

            fig, ax = plt.subplots()
            ax.plot(x, y, color="hotpink", linewidth=3)
            ax.fill(x, y, color="pink")
            ax.axis("equal")
            ax.axis("off")

            st.pyplot(fig)

            st.write("Happy birthday to my favorite Roz!")
            st.write("So glad we're best friends :)")
            st.balloons()
    else:
        st.write("Hmm... this isn't for you 🤨")
