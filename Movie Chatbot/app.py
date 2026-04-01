import streamlit as st
st.write("APP RUNNING")
import streamlit as st
from tmdb_api import search_movie, format_movie_info

st.set_page_config(page_title="Movie Info Chatbot", page_icon="🎥")

st.title("🎥 Movie Info Chatbot")
st.caption("Ask me about any movie! Just type the title.")

# Menyimpan histori chat
if "messages" not in st.session_state:
    st.session_state.messages = []

# Menampilkan histori chat sebelumnya
for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

# Input user
if prompt := st.chat_input("Type a movie title..."):

    # Simpan pesan user
    st.session_state.messages.append({
        "role": "user",
        "content": prompt
    })

    # Tampilkan pesan user
    with st.chat_message("user"):
        st.markdown(prompt)

    # Cari data film
    movie = search_movie(prompt)

    if movie:
        reply = format_movie_info(movie)
    else:
        reply = f"Sorry, I couldn't find anything for **{prompt}**."

    # Simpan balasan bot
    st.session_state.messages.append({
        "role": "assistant",
        "content": reply
    })

    # Tampilkan balasan bot
    with st.chat_message("assistant"):
        st.markdown(reply)

