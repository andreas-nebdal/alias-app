import streamlit as st
import random

# word list

words = [
    "Levollinen", "Hilpeä", "Luottavainen", "Hellä", "Uhmakas", "Katkera", "Haikea", "Murheellinen",
    "Kiitollinen", "Ilahtunut", "Tyyni", "Suuttunut", "Helpottunut", "Mustasukkainen", "Avuton",
    "Hämmentynyt", "Epävarma", "Vapaa", "Onnellinen", "Epätoivoinen", "Ystävällinen", "Arvostava",
    "Uppoutunut", "Surullinen", "Yksinäinen", "Apea", "Nolostunut", "Katuva", "Häpeilevä",
    "Turhautunut", "Välinpitämätön", "Rento", "Kostonhaluinen", "Riemastunut", "Ylpeä", "Kiukkuinen",
    "Kyllästynyt", "Pettynyt", "Pitkästynyt", "Ärtynyt", "Pelokas", "Toiveikas", "Innostunut",
    "Rauhallinen", "Tunteellinen", "Huolestunut", "Jännittynyt", "Myötätuntoinen", "Harmistunut",
    "Raivostunut", "Tyytyväinen", "Iloinen", "Tuohtunut", "Vihainen", "Rohkea", "Päättäväinen",
    "Sisukas", "Itsevarma", "Kateellinen", "Kauhistunut", "Huvittunut", "Levoton", "Epäluuloinen"
]

# Keep state across button clicks
if "remaining_words" not in st.session_state:
    st.session_state.remaining_words = words.copy()

st.title("🎲 Random Word Picker")

if st.button("Pick a Word"):
    if st.session_state.remaining_words:
        word = random.choice(st.session_state.remaining_words)
        st.write(f"👉 Your word is: **{word}**")
        st.session_state.remaining_words.remove(word)
    else:
        st.write("All words have been used!")

