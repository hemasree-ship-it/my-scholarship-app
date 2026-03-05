import streamlit as st

# 1. Page Config - Using a standard title and layout
st.set_page_config(page_title="ScholarGate AI", page_icon="🎓", layout="wide")

# 2. Enhanced CSS - Clean, Symmetric, and Trustworthy
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #fcfcfd; }
    
    /* Center and Style Title */
    .main-header { text-align: center; color: #1e293b; font-size: 38px; font-weight: 700; margin-bottom: 5px; }
    .sub-header { text-align: center; color: #64748b; font-size: 16px; margin-bottom: 30px; }
    
    /* Professional Card UI */
    .scholarship-card {
        padding: 24px;
        border-radius: 12px;
        background-color: white;
        border: 1px solid #e2e8f0;
        border-left: 6px solid #2563eb;
        margin-bottom: 20px;
        box-shadow: 0 4px 6px -1px rgba(0, 0, 0, 0.05), 0 2px 4px -1px rgba(0, 0, 0, 0.06);
    }
    
    /* Button Styling */
    .stButton>button {
        border-radius: 8px;
        font-weight: 600;
        background-color: #2563eb;
        color: white;
        transition: all 0.3s ease;
    }
    .stButton>button:hover { background-color: #1d4ed8; border-color: #1d4ed8; }
    
    /* Input field spacing */
    div.stBlock { padding: 10px; }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER SECTION ---
st.markdown("<div class='main-header'>ScholarGate AI</div>", unsafe_allow_html=True)
st.markdown("<div class='sub-header'>Verified Scholarship Intelligence Platform</div>", unsafe_allow_html=True)

# --- PROGRESS INDICATOR ---
# This makes it feel professional and symmetric
step = st.select_slider("Application Progress", options=["Personal Info", "Academic Profile", "Results"])
st.divider()

# --- FORM STRUCTURE ---
if step == "Personal Info":
    st.subheader("👤 Basic Information")
    with st.container():
        col1, col2 = st.columns(2)
        with col1:
            name = st.text_input("Full Name", placeholder="As per official documents")
            age = st.number_input("Age", 15, 30, 18)
        with col2:
            current_class = st.selectbox("Current Level of Study", ["10th", "12th", "UG (B.Tech/B.Sc)", "PG (M.Tech)", "PhD"])
            gender = st.radio("Gender", ["Male", "Female", "Other"], horizontal=True)
    st.info("Tip: Enter your name exactly as it appears on your Aadhar card for faster verification.")

elif step == "Academic Profile":
    st.subheader("📚 Academic & Financial Background")
    with st.container():
        c1, c2 = st.columns(2)
        with c1:
            m10 = st.number_input("10th Standard Marks (%)", 0, 100, 80)
            m12 = st.number_input("12th Standard Marks (%)", 0, 100, 80)
        with c2:
            inc = st.number_input("Family Annual Income (₹)", 0, 2500000, 400000)
            skills = st.multiselect("Special Categories", ["Sports", "NCC/NSS", "Coding", "Arts", "Differently Abled"])
    
    st.markdown("---")
    st.write("#### Document Verification")
    st.file_uploader("Upload Marksheet/Income Certificate for AI validation", type=["pdf", "png", "jpg"])

elif step == "Results":
    st.subheader("💰 Personalized Matches")
    # For demo purposes, we define dummy variables if they aren't saved in session
    # In a real app, you'd use st.session_state
    
    if st.button("Analyze & Find Scholarships ✨"):
        with st.spinner("AI is scanning national databases..."):
            import time
            time.sleep(1.5) # Simulates AI processing
            
            results = [
                {"name": "National Scholarship Portal (NSP)", "min": 75, "link": "https://scholarships.gov.in/", "desc": "Official Government of India portal for all central schemes."},
                {"name": "Reliance Foundation Scholars", "min": 80, "link": "https://www.reliancefoundation.org/", "desc": "Prestigious grant for high-achieving undergraduate students."}
            ]
            
            # This makes the output look symmetric and clean
            for s in results:
                st.markdown(f"""
                <div class="scholarship-card">
                    <h3 style="color: #1e293b; margin-top: 0;">{s['name']}</h3>
                    <p style="color: #475569;">{s['desc']}</p>
                    <p><b>Status:</b> ✅ You are Eligible</p>
                    <a href="{s['link']}" target="_blank" style="text-decoration: none;">
                        <div style="background-color: #10b981; color: white; padding: 10px 20px; border-radius: 6px; display: inline-block; font-weight: bold;">
                            Go to Application Portal →
                        </div>
                    </a>
                </div>
                """, unsafe_allow_html=True)
            st.balloons()

# --- SIDEBAR ALERTS ---
with st.sidebar:
    st.markdown("### 🔔 Live Notifications")
    st.success("**Tata Grant 2026** is now live!")
    st.error("**Deadline Alert:** NSP closes in 48 hours.")
    st.divider()
    st.markdown("🔍 *Our AI checks for new scholarships every 6 hours.*")
