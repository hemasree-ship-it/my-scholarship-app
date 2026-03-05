import streamlit as st

# Setup Page Appearance
st.set_page_config(page_title="Scholar-Match Pro", layout="wide")

# --- CUSTOM CSS FOR PROFESSIONAL LOOK ---
st.markdown("""
    <style>
    .main { background-color: #f5f7f9; }
    .stButton>button { width: 100%; border-radius: 20px; height: 3em; background-color: #007bff; color: white; }
    .scholarship-card { padding: 20px; border-radius: 10px; background-color: white; border-left: 5px solid #007bff; margin-bottom: 20px; box-shadow: 2px 2px 10px rgba(0,0,0,0.1); }
    </style>
    """, unsafe_allow_html=True)

st.title("🎓 Scholar-Match AI")
st.info("Complete your profile to unlock national and international scholarships.")

# --- MULTI-STEP FORM ---
tab1, tab2, tab3 = st.tabs(["👤 Personal Info", "📚 Academic Profile", "💰 Found Scholarships"])

with tab1:
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name")
        age = st.number_input("Age", 10, 30)
    with col2:
        current_class = st.selectbox("Current Class/Year", ["10th", "12th", "B.Tech 1st Year", "B.Tech 2nd Year", "Other"])
        gender = st.radio("Gender", ["Male", "Female", "Other"], horizontal=True)

with tab2:
    st.subheader("Marks & Certificates")
    col3, col4 = st.columns(2)
    with col3:
        marks_10 = st.number_input("10th Marks (%)", 0, 100)
        marks_12 = st.number_input("12th Marks (%)", 0, 100)
    with col4:
        income = st.number_input("Family Annual Income (₹)", 0, 2000000)
        certificates = st.multiselect("Special Skills/Certs", ["Sports (National)", "NCC", "Coding", "Music", "None"])
    
    # File Uploader for "Look"
    st.file_uploader("Upload Marks Card (Optional for AI Verification)", type=["pdf", "jpg", "png"])

with tab3:
    if st.button("Generate Matching Scholarships ✨"):
        # Simple Example Database with links
        results = [
            {"name": "National Scholarship Portal (NSP)", "min": 80, "link": "https://scholarships.gov.in/", "desc": "Govt of India merit support."},
            {"name": "Reliance Foundation Grant", "min": 75, "link": "https://www.reliancefoundation.org/", "desc": "Private grant for undergraduate students."}
        ]
        
        found = False
        for s in results:
            if marks_12 >= s["min"] and income <= 600000:
                found = True
                # Professional "Card" UI
                st.markdown(f"""
                <div class="scholarship-card">
                    <h3>✅ {s['name']}</h3>
                    <p>{s['desc']}</p>
                    <p><b>Steps:</b> Register on portal -> Upload Documents -> Get Verified</p>
                    <a href="{s['link']}" target="_blank">Click Here to Apply Directly</a>
                </div>
                """, unsafe_allow_html=True)
        
        if not found:
            st.warning("No matches yet. Try updating your profile details.")

# Sidebar for Notifications
st.sidebar.header("🔔 Live Alerts")
st.sidebar.success("New: Tata Scholarship 2026 is now OPEN!")
st.sidebar.info("Deadline: NSP closes in 4 days.")
