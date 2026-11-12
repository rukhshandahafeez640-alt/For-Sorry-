import streamlit as st
import streamlit.components.v1 as components
import os

# ==============================================================================
# 1. STREAMLIT PAGE CONFIGURATION
# ==============================================================================
st.set_page_config(
    page_title="Dear Faria ❤️ | A Letter From My Heart",
    page_icon="🌸",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ==============================================================================
# 2. STATE MANAGEMENT
# ==============================================================================
if "stage" not in st.session_state:
    st.session_state.stage = "intro"  # 'intro' or 'letter'

if "response_choice" not in st.session_state:
    st.session_state.response_choice = None

def go_to_letter():
    st.session_state.stage = "letter"

def restart_experience():
    st.session_state.stage = "intro"
    st.session_state.response_choice = None

# ==============================================================================
# 3. LOAD CSS & INJECT MAGICAL BACKGROUND PARTICLES
# ==============================================================================
def load_css():
    css_file = os.path.join(os.path.dirname(__file__), "styles.css")
    if os.path.exists(css_file):
        with open(css_file, "r", encoding="utf-8") as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

load_css()

# HTML & CSS Particle generator (falling petals, floating hearts, twinkling stars)
particles_html = """
<div class="particle-container">
    <!-- Falling Petals -->
    <div class="petal" style="left: 5%; width: 18px; height: 18px; animation-duration: 9s; animation-delay: 0s;"></div>
    <div class="petal" style="left: 18%; width: 14px; height: 14px; animation-duration: 12s; animation-delay: 2s;"></div>
    <div class="petal" style="left: 32%; width: 20px; height: 20px; animation-duration: 10s; animation-delay: 4s;"></div>
    <div class="petal" style="left: 48%; width: 16px; height: 16px; animation-duration: 11s; animation-delay: 1s;"></div>
    <div class="petal" style="left: 65%; width: 22px; height: 22px; animation-duration: 13s; animation-delay: 3s;"></div>
    <div class="petal" style="left: 78%; width: 15px; height: 15px; animation-duration: 9.5s; animation-delay: 5s;"></div>
    <div class="petal" style="left: 90%; width: 19px; height: 19px; animation-duration: 11.5s; animation-delay: 0.5s;"></div>

    <!-- Floating Hearts -->
    <div class="floating-heart" style="left: 10%; animation-duration: 8s; animation-delay: 1s;">💖</div>
    <div class="floating-heart" style="left: 25%; animation-duration: 11s; animation-delay: 3s;">🌸</div>
    <div class="floating-heart" style="left: 55%; animation-duration: 9.5s; animation-delay: 0s;">💕</div>
    <div class="floating-heart" style="left: 72%; animation-duration: 12s; animation-delay: 4.5s;">✨</div>
    <div class="floating-heart" style="left: 88%; animation-duration: 8.5s; animation-delay: 2s;">💖</div>

    <!-- Twinkling Stars -->
    <div class="sparkle-star" style="top: 15%; left: 12%; width: 4px; height: 4px; animation-duration: 2.2s;"></div>
    <div class="sparkle-star" style="top: 25%; left: 40%; width: 5px; height: 5px; animation-duration: 3s; animation-delay: 0.8s;"></div>
    <div class="sparkle-star" style="top: 10%; left: 82%; width: 4px; height: 4px; animation-duration: 2.5s; animation-delay: 1.5s;"></div>
    <div class="sparkle-star" style="top: 50%; left: 8%; width: 5px; height: 5px; animation-duration: 3.5s; animation-delay: 0.2s;"></div>
    <div class="sparkle-star" style="top: 70%; left: 85%; width: 6px; height: 6px; animation-duration: 2.8s; animation-delay: 1.1s;"></div>
    <div class="sparkle-star" style="top: 85%; left: 22%; width: 4px; height: 4px; animation-duration: 3.2s; animation-delay: 0.5s;"></div>
    <div class="sparkle-star" style="top: 60%; left: 60%; width: 5px; height: 5px; animation-duration: 2.6s; animation-delay: 1.9s;"></div>
</div>
"""
st.markdown(particles_html, unsafe_allow_html=True)

# Optional royalty-free ambient piano track for emotional background atmosphere
audio_component = """
<div class="audio-bar">
    <span style="font-size: 0.9rem; color: #6a1b9a; font-weight: 500;">🎵 Ambient Mood</span>
    <audio controls loop style="height: 28px; width: 170px;">
        <source src="https://cdn.pixabay.com/download/audio/2022/05/16/audio_c97690196d.mp3?filename=tender-piano-112191.mp3" type="audio/mp3">
        Your browser does not support the audio element.
    </audio>
</div>
"""
st.markdown(audio_component, unsafe_allow_html=True)


# ==============================================================================
# 4. VIEW: INTRO PAGE
# ==============================================================================
if st.session_state.stage == "intro":
    st.markdown('<div class="magical-wrapper">', unsafe_allow_html=True)

    st.markdown(
        """
        <div class="glass-card" style="text-align: center; margin-top: 5vh; padding: 3.5rem 2.5rem;">
            <div class="typing-container">
                <span class="typing-text">Dear Faria...</span>
            </div>
            
            <div class="fade-in-slow" style="margin-top: 2rem;">
                <p style="font-size: 1.35rem; line-height: 2.1; color: #4a3b59; font-weight: 300;">
                    This isn't just a website.<br>
                    <span style="font-family: 'Playfair Display', serif; font-size: 1.55rem; color: #8e24aa; font-weight: 600;">
                        It's my heart written in words.
                    </span><br>
                    Please read it till the end.
                </p>
                <div style="font-size: 2.2rem; margin-top: 1rem;">🌸 ✉️ 🌸</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    _, col_btn, _ = st.columns([1, 1.2, 1])
    with col_btn:
        if st.button("Read My Heart ❤️", key="enter_letter_btn", on_click=go_to_letter):
            pass

    st.markdown('</div>', unsafe_allow_html=True)


# ==============================================================================
# 5. VIEW: THE HEARTFELT LETTER
# ==============================================================================
elif st.session_state.stage == "letter":
    st.markdown('<div class="magical-wrapper">', unsafe_allow_html=True)

    # Header
    st.markdown(
        """
        <div style="text-align: center; margin-bottom: 2rem;">
            <h1 class="hero-title">Dear Faria ❤️</h1>
            <p class="hero-subtitle">A Letter From My Heart</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------------------------
    # SECTION 1: I'm Truly Sorry
    # --------------------------------------------------------------------------
    st.markdown(
        """
        <div class="glass-card">
            <h2 class="section-title">I'm Truly Sorry</h2>
            <div class="card-body">
                I know I disappointed you.<br><br>
                You invited me to meet you, and I couldn't come.<br><br>
                I understand that it hurt you, and seeing you upset breaks my own heart.<br><br>
                <span class="highlight-text">I wish I could go back and change that moment.</span><br><br>
                <strong style="font-size: 1.3rem; color: #ad1457;">I am deeply, truly sorry.</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------------------------
    # SECTION 2: You Mean So Much To Me
    # --------------------------------------------------------------------------
    st.markdown(
        """
        <div class="glass-card">
            <h2 class="section-title">You Mean So Much To Me</h2>
            <div class="card-body">
                You are not just my friend.<br><br>
                <span style="font-family: 'Great Vibes', cursive; font-size: 2.8rem; color: #8e24aa; display: block; margin: 0.5rem 0;">
                    You are my best friend.
                </span>
                Our friendship means more to me than you probably realize.<br><br>
                I never, ever wanted to hurt you or make you feel undervalued.
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------------------------
    # SECTION 3: What I Miss
    # --------------------------------------------------------------------------
    st.markdown(
        """
        <div class="glass-card">
            <h2 class="section-title">What I Miss</h2>
            <p style="text-align: center; color: #635373; font-style: italic; margin-bottom: 1.5rem;">
                Every single day feels incomplete without our bond...
            </p>
            <div class="miss-grid">
                <div class="miss-card">
                    <span class="miss-icon">💬</span>
                    <h3 class="miss-title">Talking to You</h3>
                    <p style="color: #6a5375; font-size: 0.95rem; margin-top: 6px;">
                        The endless random talks, late night banter, and checking in on each other.
                    </p>
                </div>
                <div class="miss-card">
                    <span class="miss-icon">✨</span>
                    <h3 class="miss-title">Laughing with You</h3>
                    <p style="color: #6a5375; font-size: 0.95rem; margin-top: 6px;">
                        Those genuine, stomach-hurting laughs that make everything feel light again.
                    </p>
                </div>
                <div class="miss-card">
                    <span class="miss-icon">🕊️</span>
                    <h3 class="miss-title">Sharing Everything</h3>
                    <p style="color: #6a5375; font-size: 0.95rem; margin-top: 6px;">
                        Trusting you with my unfiltered thoughts, worries, and silly daily stories.
                    </p>
                </div>
                <div class="miss-card">
                    <span class="miss-icon">🌸</span>
                    <h3 class="miss-title">Our Friendship</h3>
                    <p style="color: #6a5375; font-size: 0.95rem; margin-top: 6px;">
                        The rare comfort of knowing someone understands you like no one else.
                    </p>
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------------------------
    # SECTION 4: My Promise
    # --------------------------------------------------------------------------
    st.markdown(
        """
        <div class="glass-card">
            <h2 class="section-title">My Promise</h2>
            <div class="card-body">
                I cannot promise that I will never make mistakes.<br><br>
                <span class="highlight-text">But I promise that I will learn from them.</span><br><br>
                I promise to value your feelings more, protect your trust, and show up when it matters.<br><br>
                <strong>I promise to become a better friend to you every single day.</strong>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------------------------
    # SECTION 5: One Last Thing...
    # --------------------------------------------------------------------------
    st.markdown(
        """
        <div class="glass-card">
            <h2 class="section-title">One Last Thing...</h2>
            <div class="card-body" style="font-size: 1.2rem; line-height: 2;">
                I know forgiveness cannot be forced.<br>
                It can only be given.<br><br>
                If your heart is still hurting, I completely understand.<br>
                Take all the time you need.<br><br>
                <em>But if there is even a tiny place for me in your heart...</em><br><br>
                <span style="font-size: 1.35rem; color: #8e24aa; font-weight: 600;">
                    Please give our friendship another chance. 🌸
                </span>
            </div>
        </div>
        """,
        unsafe_allow_html=True
    )

    # --------------------------------------------------------------------------
    # FINAL SECTION & INTERACTIVE BUTTONS
    # --------------------------------------------------------------------------
    st.markdown(
        """
        <div class="glass-card" style="text-align: center; border: 2px solid rgba(248, 187, 208, 0.9);">
            <div class="big-heart">💖</div>
            <p style="font-family: 'Playfair Display', serif; font-size: 1.6rem; font-style: italic; color: #6a1b9a; line-height: 1.6; margin-bottom: 1.8rem;">
                "Some friendships are too precious to lose over one mistake.<br>
                I hope ours is one of them."
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    # Interactive choice buttons
    btn_col1, btn_col2 = st.columns(2)

    with btn_col1:
        if st.button("❤️ Yes, I Forgive You", key="forgive_btn"):
            st.session_state.response_choice = "forgiven"
            st.balloons()

    with btn_col2:
        if st.button("💌 Let's Talk Again", key="talk_btn"):
            st.session_state.response_choice = "talk"
            st.snow()

    # Dynamic Feedback based on Faria's choice
    if st.session_state.response_choice == "forgiven":
        components.html(
            """
            <script src="https://cdn.jsdelivr.net/npm/canvas-confetti@1.6.0/dist/confetti.browser.min.js"></script>
            <script>
                var duration = 4.5 * 1000;
                var animationEnd = Date.now() + duration;
                var defaults = { startVelocity: 30, spread: 360, ticks: 60, zIndex: 99999 };

                function randomInOut(min, max) {
                    return Math.random() * (max - min) + min;
                }

                var interval = setInterval(function() {
                    var timeLeft = animationEnd - Date.now();
                    if (timeLeft <= 0) {
                        return clearInterval(interval);
                    }
                    var particleCount = 50 * (timeLeft / duration);
                    confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInOut(0.1, 0.3), y: Math.random() - 0.2 } }));
                    confetti(Object.assign({}, defaults, { particleCount, origin: { x: randomInOut(0.7, 0.9), y: Math.random() - 0.2 } }));
                }, 250);
            </script>
            """,
            height=0,
            width=0
        )

        st.markdown(
            """
            <div class="celebrate-card">
                <div style="font-size: 3.5rem;">🎉 🌸 💖</div>
                <h3 style="font-family: 'Great Vibes', cursive; font-size: 3.2rem; color: #ad1457; margin: 0.5rem 0;">
                    Thank You, Faria.
                </h3>
                <p style="font-size: 1.35rem; color: #4a3b59; line-height: 1.8; margin: 0 auto; max-width: 600px;">
                    You just made my day brighter than words could ever describe.<br><br>
                    <strong>I promise to always treasure our friendship and never take you for granted.</strong>
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    elif st.session_state.response_choice == "talk":
        st.markdown(
            """
            <div class="celebrate-card">
                <div style="font-size: 3rem;">💌 ☕ ✨</div>
                <h3 style="font-family: 'Playfair Display', serif; font-size: 2.2rem; color: #6a1b9a; margin: 0.5rem 0;">
                    I'm Right Here Whenever You're Ready
                </h3>
                <p style="font-size: 1.25rem; color: #4a3b59; line-height: 1.8; margin: 0 auto; max-width: 600px;">
                    Send me a message whenever you feel comfortable.<br>
                    I can't wait to hear your voice and listen to everything you have to say.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # Optional reset button
    st.markdown("<div style='height: 40px;'></div>", unsafe_allow_html=True)
    _, reset_col, _ = st.columns([1.5, 1, 1.5])
    with reset_col:
        if st.button("↺ Re-read From Beginning", key="restart_btn", on_click=restart_experience):
            pass

    st.markdown('</div>', unsafe_allow_html=True)
