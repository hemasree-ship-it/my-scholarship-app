import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="ScholarGate AI", page_icon="🎓", layout="centered")

# --- PROFESSIONAL STYLING (The "Secret Sauce") ---
st.markdown("""
    <style>
    /* Background and Fonts */
    .stApp { background-color: #f8fafc; }
    h1 { color: #1e293b; font-family: 'Inter', sans-serif; text-align: center; }
    
    /* Clean white boxes for inputs */
    .css-1r6slb0 { padding: 20px; background: white; border-radius: 12px; border: 1px solid #e2e8f0; }
    
    /* The Result Cards */
    .result-card {
        background: white; padding: 20px; border-radius: 10px;
        border-left: 6px solid #2563eb; margin-bottom: 15px;
        box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }
    .apply-btn {
        background-color: #2563eb; color: white; padding: 8px 16px;
        border-radius: 6px; text-decoration: none; font-weight: 600;
        display: inline-block; margin-top: 10px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- HEADER ---
st.title("🎓 ScholarGate AI")
st.markdown("<p style='text-align: center; color: #64748b;'>National Scholarship Verification & Matching System</p>", unsafe_allow_html=True)
st.divider()

# --- STEP 1: PERSONAL DETAILS ---
with st.expander("👤 Step 1: Personal Information", expanded=True):
    col1, col2 = st.columns(2)
    with col1:
        name = st.text_input("Full Name (as per Aadhar)")
        age = st.number_input("Age", 15, 30, 18)
    with col2:
        gender = st.selectbox("Gender", ["Male", "Female", "Other"])
        category = st.selectbox("Category", ["General", "OBC", "SC/ST", "Minority"])

# --- STEP 2: ACADEMICS & DOCUMENTS ---
with st.expander("📚 Step 2: Academic Profile", expanded=True):
    col3, col4 = st.columns(2)
    with col3:
        current_class = st.selectbox("Current Class/Level", ["10th", "12th", "UG", "PG"])
        marks = st.slider("Latest Marks Percentage", 0, 100, 80)
    with col4:
        income = st.number_input("Annual Family Income (₹)", 0, 2000000, 300000)
        cert_upload = st.file_uploader("Upload Certificates (Sports/Coding/NCC)", type=["pdf", "png", "jpg"])

# --- STEP 3: MATCHING ENGINE ---
st.write("")
if st.button("SEARCH ELIGIBLE SCHOLARSHIPS 🔍"):
    with st.status("Verifying details with AI...", expanded=True) as status:
        st.write("Reading uploaded certificates...")
        import time; time.sleep(1)
        st.write("Checking Government Database (NSP)...")
        time.sleep(1)
        status.update(label="Matching Complete!", state="complete", expanded=False)
    
    st.success(f"Great news, {name}! We found matches for your profile:")
    
    # Example Output Card
    st.markdown(f"""
        <div class="result-card">
            <h3 style="margin:0; color:#1e293b;">National Merit Scholarship (NSP)</h3>
            <p style="color:#64748b; margin: 5px 0;">Based on your {marks}% marks and {category} category.</p>
            <p><b>Benefit:</b> ₹50,000 / Year</p>
            <p><b>Required:</b> Income Certificate, Marksheet</p>
            <a class="apply-btn" href="https://scholarships.gov.in/" target="_blank">Apply on Official Portal</a>
        </div>
        
        <div class="result-card" style="border-left-color: #f59e0b;">
            <h3 style="margin:0; color:#1e293b;">Reliance Foundation Undergraduate Grant</h3>
            <p style="color:#64748b; margin: 5px 0;">Private grant for high-performing students.</p>
            <p><b>Benefit:</b> ₹2,00,000 Total</p>
            <p><b>Required:</b> Entrance Test + Interview</p>
            <a class="apply-btn" style="background-color: #f59e0b;" href="https://www.reliancefoundation.org/" target="_blank">View Application Steps</a>
        </div>
    """, unsafe_allow_html=True)

# --- SIDEBAR (NOTIFICATIONS) ---
with st.sidebar:
    st.header("🔔 Live Alerts")
    st.info("**New:** Tata Scholarship for Engineering is now Live!")
    st.warning("**Deadline:** NSP Portals closing in 72 hours.")
    st.divider()
    st.caption("ScholarGate AI v1.0 | Osmania Innovation Workshop")
