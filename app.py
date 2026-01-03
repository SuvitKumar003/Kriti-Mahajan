import streamlit as st
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="For Kriti ❤️",
    page_icon="❤️",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
body {
    background: linear-gradient(to bottom right, #ffdde1, #ee9ca7);
}
.main {
    background-color: rgba(255, 255, 255, 0.85);
    padding: 30px;
    border-radius: 20px;
}
.title {
    text-align: center;
    font-size: 50px;
    font-weight: bold;
    color: #c9184a;
}
.subtitle {
    text-align: center;
    font-size: 22px;
    color: #6a040f;
}
.text {
    font-size: 20px;
    color: #370617;
    line-height: 1.7;
}
.footer {
    text-align: center;
    font-size: 16px;
    color: #6a040f;
    margin-top: 40px;
}
.heart {
    text-align: center;
    font-size: 40px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- CONTENT ----------------
st.markdown("<div class='main'>", unsafe_allow_html=True)

st.markdown("<div class='title'>Kriti ❤️</div>", unsafe_allow_html=True)
st.markdown("<div class='subtitle'>Thank you for the most beautiful college life</div>", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown("""
<div class='text'>
Kriti,  
I don’t think words are enough, but still I want to try.

Thank you for walking into my life and turning my college years into memories I’ll carry forever.  
Every laugh, every late-night talk, every small moment with you made these years special in a way nothing else could.

You were not just a part of my college life —  
you <b>defined</b> it.
</div>
""", unsafe_allow_html=True)

st.markdown("<br><br>", unsafe_allow_html=True)

# ---------------- EYES SECTION ----------------
st.markdown("<div class='subtitle'>About Your Eyes ✨</div>", unsafe_allow_html=True)

st.markdown("""
<div class='text'>
Your eyes…  
They don’t just look beautiful — they <i>feel</i> beautiful.

There’s calm in them when I’m lost,  
warmth in them when I’m tired,  
and magic in them that I can never explain.

I’ve seen entire sunsets fade,  
but none of them compare  
to a single moment of you looking at me.
</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- MEMORY BUTTON ----------------
if st.button("💖 Click to know what you mean to me"):
    st.success(
        "You are my comfort, my happiness, and the reason my college life became unforgettable 💕"
    )

st.markdown("<br>", unsafe_allow_html=True)

# ---------------- FOOTER ----------------
today = datetime.now().strftime("%d %B %Y")

st.markdown(f"""
<div class='footer'>
Made with ❤️ by Suvit <br>
{today}
</div>
""", unsafe_allow_html=True)

st.markdown("<div class='heart'>❤️ ❤️ ❤️</div>", unsafe_allow_html=True)

st.markdown("</div>", unsafe_allow_html=True)
