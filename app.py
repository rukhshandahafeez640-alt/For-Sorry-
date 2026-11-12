import streamlit as st
import streamlit.components.v1 as components
import textwrap

# ==============================================================================
# 1. PAGE CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="Dear Faria ❤️ | A Letter From My Heart",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 2. SESSION STATE MANAGEMENT
# ==============================================================================
if "stage" not in st.session_state:
    st.session_state.stage = "intro"

if "response_choice" not in st.session_state:
    st.session_state.response_choice = None

def go_to_letter():
    st.session_state.stage = "letter"

def restart_experience():
    st.session_state.stage = "intro"
    st.session_state.response_choice = None

# ==============================================================================
# 3. DIRECT INJECTED CSS (ALL ANIMATIONS, GLASSMORPHISM, FONTS)
# ==============================================================================
custom_css = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400;1,600&family=Great+Vibes&family=Outfit:wght@300;400;500;600&family=Playfair+Display:ital,wght@0,500;0,700;1,400;1,600&display=swap');

#MainMenu {visibility: hidden;}
footer {visibility: hidden;}
header {visibility: hidden;}
.stDeployButton {display: none;}
div[data-testid="stDecoration"] {display: none;}

/* Full background animation */
.stApp {
    background: linear-gradient(135deg, #fff0f5 0%, #fce4ec 25%, #ede7f6 50%, #e8eaf6 75%, #fce4ec 100%) !important;
    background-size: 400% 400% !important;
    animation: gradientFlow 18s ease infinite !important;
    font-family: 'Outfit', sans-serif !important;
    color: #3d314a !important;
    overflow-x: hidden !important;
    min-height: 100vh !important;
}

@keyframes gradientFlow {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}

/* Floating particle canvas */
.particle-container {
    position: fixed;
    top: 0;
    left: 0;
    width: 100vw;
    height: 100vh;
    pointer-events: none;
    z-index: 0;
    overflow: hidden;
}

.petal, .floating-heart, .sparkle-star {
    position: absolute;
    opacity: 0.75;
    animation-timing-function: linear;
    animation-iteration-count: infinite;
}

/* Falling flower petals */
.petal {
    background: radial-gradient(ellipse at center, #ffccd5 0%, #ffb3c1 70%, #ff8fa3 100%);
    border-radius: 80% 0 55% 50% / 55% 0 80% 50%;
    filter: drop-shadow(0 2px 5px rgba(255, 143, 163, 0.3));
    animation-name: fallAndSway;
}

@keyframes fallAndSway {
    0% { transform: translate3d(0, -10vh, 0) rotate(0deg) scale(0.8); opacity: 0; }
    15% { opacity: 0.8; }
    85% { opacity: 0.8; }
    100% { transform: translate3d(120px, 110vh, 0) rotate(360deg) scale(1); opacity: 0; }
}

/* Floating hearts */
.floating-heart {
    font-size: 1.4rem;
    animation-name: floatUpHeart;
    filter: drop-shadow(0 0 6px rgba(244, 143, 177, 0.4));
}

@keyframes floatUpHeart {
    0% { transform: translate3d(0, 105vh, 0) scale(0.6); opacity: 0; }
    20% { opacity: 0.8; }
    80% { opacity: 0.8; }
    100% { transform: translate3d(-60px, -10vh, 0) scale(1.1); opacity: 0; }
}

/* Twinkling stars */
.sparkle-star {
    background: radial-gradient(circle, #ffffff 10%, #ffebee 80%);
    border-radius: 50%;
    box-shadow: 0 0 8px 2px rgba(255, 255, 255, 0.9), 0 0 16px 4px rgba(225, 190, 231, 0.7);
    animation-name: starTwinkle;
    animation-direction: alternate;
}

@keyframes starTwinkle {
    0% { transform: scale(0.3); opacity: 0.2; }
    100% { transform: scale(1.3); opacity: 0.95; }
}

/* Glassmorphism Containers */
.magical-wrapper {
    position: relative;
    z-index: 1;
    max-width: 820px;
    margin: 0 auto;
    padding: 2rem 1rem 5rem 1rem;
}

.glass-card {
    background: rgba(255, 255, 255, 0.48);
    backdrop-filter: blur(20px);
    -webkit-backdrop-filter: blur(20px);
    border: 1px solid rgba(255, 255, 255, 0.75);
    border-radius: 28px;
    padding: 2.5rem 2rem;
    box-shadow: 0 16px 40px rgba(186, 104, 200, 0.16);
    margin-bottom: 2.5rem;
    transition: transform 0.4s ease, box-shadow 0.4s ease;
    animation: fadeInSlideUp 0.9s ease-out both;
}

.glass-card:hover {
    transform: translateY(-4px);
    box-shadow: 0 22px 50px rgba(186, 104, 200, 0.25);
}

@keyframes fadeInSlideUp {
    0% { opacity: 0; transform: translateY(30px); }
    100% { opacity: 1; transform: translateY(0); }
}

/* Typography */
.hero-title {
    font-family: 'Great Vibes', cursive !important;
    font-size: 4.5rem !important;
    color: #8e24aa !important;
    text-align: center;
    margin: 0.5rem 0 0 0;
    line-height: 1.1;
    text-shadow: 0 3px 15px rgba(142, 36, 170, 0.2);
}

.hero-subtitle {
    font-family: 'Playfair Display', serif !important;
    font-size: 1.35rem !important;
    font-style: italic;
    color: #635373;
    text-align: center;
    letter-spacing: 1.5px;
    margin-bottom: 2rem;
}

.section-title {
    font-family: 'Playfair Display', serif !important;
    font-size: 2rem !important;
    font-weight: 600 !important;
    color: #6a1b9a !important;
    text-align: center;
    margin-bottom: 1.2rem;
}

.section-title::after {
    content: "🌸";
    display: block;
    font-size: 1.1rem;
    margin-top: 6px;
    opacity: 0.8;
}

.card-body-text {
    font-size: 1.18rem;
    line-height: 1.9;
    color: #4a3b59;
    text-align: center;
    font-weight: 400;
}

.highlight-text {
    color: #ad1457;
    font-weight: 600;
}

/* Typing Header */
.typing-title {
    font-family: 'Playfair Display', serif;
    font-size: 3rem;
    font-weight: 700;
    color: #7b1fa2;
    text-align: center;
    margin-bottom: 1.5rem;
}

/* Cards for Section 3 */
.miss-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(200px, 1fr));
    gap: 1.2rem;
    margin-top: 1.5rem;
}

.miss-card {
    background: rgba(255, 255, 255, 0.7);
    border: 1px solid rgba(255, 255, 255, 0.9);
    border-radius: 20px;
    padding: 1.5rem 1rem;
    text-align: center;
    transition: all 0.35s ease;
    box-shadow: 0 8px 24px rgba(186, 104, 200, 0.08);
}

.miss-card:hover {
    transform: translateY(-6px) scale(1.02);
    background: rgba(255, 255, 255, 0.95);
    box-shadow: 0 16px 32px rgba(186, 104, 200, 0.2);
}

.miss-icon {
    font-size: 2.2rem;
    margin-bottom: 0.5rem;
    display: inline-block;
}

.miss-card-heading {
    font-family: 'Playfair Display', serif;
    font-size: 1.15rem;
    color: #6a1b9a;
    font-weight: 600;
}

/* Heart animation */
.big-heart {
    font-size: 4.8rem;
    text-align: center;
    margin: 1rem 0;
    animation: heartPulse 1.8s infinite;
}

@keyframes heartPulse {
    0% { transform: scale(1); }
    14% { transform: scale(1.22); }
    28% { transform: scale(1); }
    42% { transform: scale(1.22); }
    70% { transform: scale(1); }
}

/* Streamlit Buttons styling */
div.stButton > button {
    background: linear-gradient(135deg, #ec407a 0%, #ab47bc 100%) !important;
    color: #ffffff !important;
    font-family: 'Outfit', sans-serif !important;
    font-size: 1.15rem !important;
    font-weight: 500 !important;
    padding: 0.8rem 2.2rem !important;
    border-radius: 50px !important;
    border: none !important;
    box-shadow: 0 10px 25px rgba(236, 64, 122, 0.38) !important;
    transition: all 0.35s ease !important;
    cursor: pointer !important;
    display: block !important;
    margin: 1rem auto !important;
}

div.stButton > button:hover {
    transform: translateY(-3px) scale(1.03) !important;
    box-shadow: 0 16px 35px rgba(171, 71, 188, 0.5) !important;
    background: linear-gradient(135deg, #f06292 0%, #ba68c8 100%) !important;
}

.celebrate-card {
    background: linear-gradient(135deg, rgba(255, 240, 245, 0.95), rgba(243, 229, 245, 0.95));
    border: 2px solid #f8bbd0;
    border-radius: 24px;
    padding: 2rem;
    text-align: center;
    box-shadow: 0 15px 40px rgba(233, 30, 99, 0.2);
    margin-top: 1.8rem;
    animation: fadeInSlideUp 0.6s ease-out;
}

/* Floating Audio Player */
.audio-bar {
    position: fixed;
    bottom: 20px;
    right: 20px;
    background: rgba(255, 255, 255, 0.85);
    backdrop-filter: blur(12px);
    border: 1px solid rgba(255, 255, 255, 0.9);
    padding: 6px 14px;
    border-radius: 50px;
    display: flex;
    align-items: center;
    gap: 8px;
    z-index: 9999;
    box-shadow: 0 8px 25px rgba(0, 0, 0, 0.1);
}
</style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# Helper function to prevent indentation codeblock issue
def render_html(html_str):
    st.markdown(textwrap.dedent(html_str), unsafe_allow_html=True)

# Background Particles
particles_html = """
<div class="particle-container">
<div class="petal" style="left: 5%; width: 18px; height: 18px; animation-duration: 9s; animation-delay: 0s;"></div>
<div class="petal" style="left: 20%; width: 14px; height: 14px; animation-duration: 12s; animation-delay: 2s;"></div>
<div class="petal" style="left: 35%; width: 20px; height: 20px; animation-duration: 10s; animation-delay: 4s;"></div>
<div class="petal" style="left: 50%; width: 16px; height: 16px; animation-duration: 11s; animation-delay: 1s;"></div>
<div class="petal" style="left: 68%; width: 22px; height: 22px; animation-duration: 13s; animation-delay: 3s;"></div>
<div class="petal" style="left: 85%; width: 15px; height: 15px; animation-duration: 9.5s; animation-delay: 5s;"></div>
<div class="floating-heart" style="left: 12%; animation-duration: 8s; animation-delay: 1s;">💖</div>
<div class="floating-heart" style="left: 28%; animation-duration: 11s; animation-delay: 3s;">🌸</div>
<div class="floating-heart" style="left: 58%; animation-duration: 9.5s; animation-delay: 0s;">💕</div>
<div class="floating-heart" style="left: 75%; animation-duration: 12s; animation-delay: 4.5s;">✨</div>
<div class="sparkle-star" style="top: 15%; left: 12%; width: 5px; height: 5px; animation-duration: 2.2s;"></div>
<div class="sparkle-star" style="top: 30%; left: 45%; width: 5px; height: 5px; animation-duration: 3s; animation-delay: 0.8s;"></div>
<div class="sparkle-star" style="top: 10%; left: 82%; width: 4px; height: 4px; animation-duration: 2.5s; animation-delay: 1.5s;"></div>
<div class="sparkle-star" style="top: 70%; left: 85%; width: 6px; height: 6px; animation-duration: 2.8s; animation-delay: 1.1s;"></div>
<div class="sparkle-star" style="top: 85%; left: 22%; width: 4px; height: 4px; animation-duration: 3.2s; animation-delay: 0.5s;"></div>
</div>
"""
render_html(particles_html)

# Floating Music Player
audio_html = """
<div class="audio-bar">
<span style="font-size: 0.85rem; color: #6a1b9a; font-weight: 500;">🎵 Music</span>
<audio controls loop style="height: 28px; width: 160px;">
<source src="https://cdn.pixabay.com/download/audio/2022/05/16/audio_c97690196d.mp3?filename=tender-piano-112191.mp3" type="audio/mp3">
</audio>
</div>
"""
render_html(audio_html)

# ==============================================================================
# VIEW 1: INTRO PAGE
# ==============================================================================
if st.session_state.stage == "intro":
    render_html('<div class="magical-wrapper">')

    intro_box = """
    <div class="glass-card" style="text-align: center; margin-top: 6vh; padding: 3.5rem 2rem;">
        <h1 class="typing-title">Dear Faria...</h1>
        <div style="margin-top: 1.5rem;">
            <p style="font-size: 1.35rem; line-height: 2.1; color: #4a3b59; font-weight: 300;">
                This isn't just a website.<br>
                <span style="font-family: 'Playfair Display', serif; font-size: 1.6rem; color: #8e24aa; font-weight: 600;">
                    It's my heart written in words.
                </span><br>
                Please read it till the end.
            </p>
            <div style="font-size: 2.2rem; margin-top: 1.2rem;">🌸 ✉️ 🌸</div>
        </div>
    </div>
    """
    render_html(intro_box)

    _, col_btn, _ = st.columns([1, 1.2, 1])
    with col_btn:
        if st.button("Read My Heart ❤️", key="enter_btn", on_click=go_to_letter):
            pass

    render_html('</div>')

# ==============================================================================
# VIEW 2: THE FULL LETTER
# ==============================================================================
elif st.session_state.stage == "letter":
    render_html('<div class="magical-wrapper">')

    header_html = """
    <div style="text-align: center; margin-bottom: 2.5rem;">
        <h1 class="hero-title">Dear Faria ❤️</h1>
        <p class="hero-subtitle">A Letter From My Heart</p>
    </div>
    """
    render_html(header_html)

    # Section 1
    sec1 = """
    <div class="glass-card">
        <h2 class="section-title">I'm Truly Sorry</h2>
        <div class="card-body-text">
            I know I disappointed you.<br><br>
            You invited me to meet you, and I couldn't come.<br><br>
            I understand that it hurt you.<br><br>
            <span class="highlight-text">I wish I could go back and change that moment.</span><br><br>
            <strong style="font-size: 1.3rem; color: #ad1457;">I'm deeply sorry.</strong>
        </div>
    </div>
    """
    render_html(sec1)

    # Section 2
    sec2 = """
    <div class="glass-card">
        <h2 class="section-title">You Mean So Much To Me</h2>
        <div class="card-body-text">
            You are not just my friend.<br><br>
            <span style="font-family: 'Great Vibes', cursive; font-size: 3rem; color: #8e24aa; display: block; margin: 0.5rem 0;">
                You are my best friend.
            </span>
            Our friendship means more to me than you probably realize.<br><br>
            I never wanted to hurt you.
        </div>
    </div>
    """
    render_html(sec2)

    # Section 3
    sec3 = """
    <div class="glass-card">
        <h2 class="section-title">What I Miss</h2>
        <p style="text-align: center; color: #635373; font-style: italic; margin-bottom: 1.5rem;">
            Every single day feels incomplete without our bond...
        </p>
        <div class="miss-grid">
            <div class="miss-card">
                <span class="miss-icon">💬</span>
                <div class="miss-card-heading">Talking to You</div>
                <p style="color: #6a5375; font-size: 0.95rem; margin-top: 6px;">I miss talking to you.</p>
            </div>
            <div class="miss-card">
                <span class="miss-icon">✨</span>
                <div class="miss-card-heading">Laughing With You</div>
                <p style="color: #6a5375; font-size: 0.95rem; margin-top: 6px;">I miss laughing with you.</p>
            </div>
            <div class="miss-card">
                <span class="miss-icon">🕊️</span>
                <div class="miss-card-heading">Sharing Everything</div>
                <p style="color: #6a5375; font-size: 0.95rem; margin-top: 6px;">I miss sharing everything with you.</p>
            </div>
            <div class="miss-card">
                <span class="miss-icon">🌸</span>
                <div class="miss-card-heading">Our Friendship</div>
                <p style="color: #6a5375; font-size: 0.95rem; margin-top: 6px;">I miss our friendship.</p>
            </div>
        </div>
    </div>
    """
    render_html(sec3)

    # Section 4
    sec4 = """
    <div class="glass-card">
        <h2 class="section-title">My Promise</h2>
        <div class="card-body-text">
            I cannot promise that I will never make mistakes.<br><br>
            <span class="highlight-text">But I promise that I will learn from them.</span><br><br>
            I promise to value your feelings more.<br><br>
            <strong>I promise to become a better friend.</strong>
        </div>
    </div>
    """
    render_html(sec4)

    # Section 5
    sec5 = """
    <div class="glass-card">
        <h2 class="section-title">One Last Thing...</h2>
        <div class="card-body-text" style="font-size: 1.25rem; line-height: 2;">
            I know forgiveness cannot be forced.<br>
            It can only be given.<br><br>
            If your heart is still hurting,<br>
            I completely understand.<br><br>
            <em>But if there is even a tiny place for me in your heart...</em><br><br>
            <span style="font-size: 1.4rem; color: #8e24aa; font-weight: 600;">
                Please give our friendship another chance. 🌸
            </span>
        </div>
    </div>
    """
    render_html(sec5)

    # Final Card
    final_card = """
    <div class="glass-card" style="text-align: center; border: 2px solid rgba(248, 187, 208, 0.95);">
        <div class="big-heart">💖</div>
        <p style="font-family: 'Playfair Display', serif; font-size: 1.6rem; font-style: italic; color: #6a1b9a; line-height: 1.6; margin-bottom: 1.5rem;">
            "Some friendships are too precious to lose over one mistake.<br>
            I hope ours is one of them."
        </p>
    </div>
    """
    render_html(final_card)

    # Action Buttons
    b_col1, b_col2 = st.columns(2)
    with b_col1:
        if st.button("❤️ Yes, I Forgive You", key="forgive_btn"):
            st.session_state.response_choice = "forgiven"
            st.balloons()

    with b_col2:
        if st.button("💌 Let's Talk Again", key="talk_btn"):
            st.session_state.response_choice = "talk"
            st.snow()

    # Confetti & Response
    if st.session_state.response_choice == "forgiven":
        components.html(
            """
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
            <script>
                var end = Date.now() + 4 * 1000;
                var interval = setInterval(function() {
                    if (Date.now() > end) return clearInterval(interval);
                    confetti({ startVelocity: 30, spread: 360, ticks: 60, origin: { x: Math.random(), y: Math.random() - 0.2 } });
                }, 200);
            </script>
            """,
            height=0,
            width=0
        )
        forgive_msg = """
        <div class="celebrate-card">
            <div style="font-size: 3.5rem;">🎉 🌸 💖</div>
            <h3 style="font-family: 'Great Vibes', cursive; font-size: 3.2rem; color: #ad1457; margin: 0.5rem 0;">
                Thank you.
            </h3>
            <p style="font-size: 1.35rem; color: #4a3b59; line-height: 1.8;">
                You just made my day.<br><br>
                <strong>I promise to always treasure our friendship.</strong>
            </p>
        </div>
        """
        render_html(forgive_msg)

    elif st.session_state.response_choice == "talk":
        talk_msg = """
        <div class="celebrate-card">
            <div style="font-size: 3rem;">💌 ☕ ✨</div>
            <h3 style="font-family: 'Playfair Display', serif; font-size: 2.2rem; color: #6a1b9a; margin: 0.5rem 0;">
                I'm Right Here
            </h3>
            <p style="font-size: 1.3rem; color: #4a3b59; line-height: 1.8;">
                Whenever you are ready, I'd love to talk and listen to everything you have to say.
            </p>
        </div>
        """
        render_html(talk_msg)

    st.markdown("<div style='height: 35px;'></div>", unsafe_allow_html=True)
    _, r_col, _ = st.columns([1.5, 1, 1.5])
    with r_col:
        if st.button("↺ Re-read", key="reset_btn", on_click=restart_experience):
            pass

    render_html('</div>')
