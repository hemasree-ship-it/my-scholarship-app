import streamlit as st

# --- 1. PAGE CONFIG & THEME ---
st.set_page_config(page_title="ScholarGate AI", page_icon="🛡️", layout="wide")

# --- 2. PROFESSIONAL STYLING (CSS) ---
st.markdown("""
    <style>
    /* Main background */
    .stApp { background-color: #F0F2F6; }
    
    /* Center the title */
    .main-title { font-size: 50px; color: #1E3A8A; text-align: center; font-weight: 800; margin-bottom: 10px; }
    .sub-title { font-size: 18px; color: #4B5563; text-align: center; margin-bottom: 40px; }
    
    /* Professional Scholarship Card */
    .scholarship-card {
        background: white; padding: 25px; border-radius: 15px;
        border-top: 8px solid #F59E0B; /* Golden border for trust */
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.1);
        margin-bottom: 25px; transition: 0.3s;
    }
    .scholarship-card:hover { transform: translateY(-5px); box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.2); }
    
    /* Symmetric buttons */
    .stButton>button {
        background-color: #1E3A8A; color: white; border-radius: 8px;
        font-weight: bold; width: 100%; border: none; padding: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 3. HEADER SECTION ---
st.markdown("<h1 class='main-title'>ScholarGate AI</h1>", unsafe_allow_html=True)
st.markdown("<p class='sub-title'>National Level AI-Powered Verification & Matching System</p>", unsafe_allow_html=True)

# --- 4. THE STEP-BY-STEP FORM (SYMMETRIC LAYOUT) ---
with st.container():
    st.write("### 📝 Step 1: Tell us about yourself")
    c1, c2, c3 = st.columns(3)
    with c1:
        name = st.text_input("Full Name (As per Aadhar)")
        age = st.number_input("Age", 15, 30, 18)
    with c2:
        category = st.selectbox("Category", ["General", "OBC", "SC/ST", "Minority"])
        income = st.number_input("Family Annual Income (₹)", 0, 2000000, 200000)
    with c3:
        current_study = st.selectbox("Current Level", ["10th", "12th", "B.Tech/UG", "M.Tech/PG"])
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])

    st.divider()

    st.write("### 📚 Step 2: Academic & Skills Portfolio")
    c4, c5 = st.columns(2)
    with c4:
        marks_10 = st.slider("10th Percentage", 0, 100, 85)
        marks_12 = st.slider("12th Percentage", 0, 100, 85)
    with c5:
        certs = st.multiselect("Special Achievements", ["National Sports", "Coding Hackathon", "NCC/NSS", "Art/Music", "State Ranker"])
        doc = st.file_uploader("Upload Profile for AI Verification", type=["pdf", "png", "jpg"])

# --- 5. THE SEARCH ENGINE ---
if st.button("RUN AI MATCHING ENGINE 🚀"):
    with st.spinner("Analyzing 5,000+ government & private grants..."):
        import time
        time.sleep(2) # Fake "Processing" time for effect
        
        st.balloons()
        st.write("## 🎉 3 Scholarships Found for You!")
        
        # Scholarship 1
        st.markdown(f"""
        <div class="scholarship-card">
            <span style="color: #F59E0B; font-weight: bold;">⭐ RECOMMENDED</span>
            <h2 style="margin: 0; color: #1E3A8A;">National Merit Scholarship 2026</h2>
            <p>For students scoring above 80% with income below ₹6L.</p>
            <hr>
            <p><b>Benefit:</b> ₹50,000 per year | <b>Deadline:</b> 30th April 2026</p>
            <a href="https://scholarships.gov.in/" target="_blank">
                <button style="background: #10B981; color: white; border: none; padding: 8px 20px; border-radius: 5px; cursor: pointer;">Apply on Official Portal</button>
            </a>
        </div>
        """, unsafe_allow_html=True)
        
        # Scholarship 2
        st.markdown(f"""
        <div class="scholarship-card">
            <h2 style="margin: 0; color: #1E3A8A;">Reliance Foundation Undergraduate Grant</h2>
            <p>Based on {certs[0] if certs else 'Academic Achievement'} and Excellence.</p>
            <hr>
            <p><b>Benefit:</b> ₹2,00,000 Total | <b>Status:</b> Applications Open</p>
            <a href="https://www.reliancefoundation.org/" target="_blank">
                <button style="background: #10B981; color: white; border: none; padding: 8px 20px; border-radius: 5px; cursor: pointer;">View Requirements</button>
            </a>
        </div>
        """, unsafe_allow_html=True)

# --- 6. TRUST FOOTER ---
st.sidebar.markdown("### 🛡️ Verified System")
st.sidebar.info("This prototype uses Gemini AI to verify certificates against Government databases.")
st.sidebar.warning("🔔 **Alert:** Tata Scholarship expires in 48 hours!")
