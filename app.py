import streamlit as st
import time

# PAGE CONFIG
st.set_page_config(
    page_title="ScholarMatch AI",
    page_icon="🎓",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.main {
    background-color: #f4f6f9;
}

.header-box{
    background-color:#ffffff;
    padding:20px;
    border-radius:10px;
    box-shadow:0px 4px 12px rgba(0,0,0,0.08);
    margin-bottom:20px;
}

.stButton>button{
    width:100%;
    border-radius:25px;
    height:45px;
    font-size:16px;
    background-color:#1a73e8;
    color:white;
}

.scholarship-card{
    background:white;
    padding:20px;
    border-radius:12px;
    margin-bottom:20px;
    border-left:6px solid #1a73e8;
    box-shadow:0px 4px 10px rgba(0,0,0,0.08);
}

.badge{
    background:#e8f0fe;
    color:#1a73e8;
    padding:4px 10px;
    border-radius:15px;
    font-size:12px;
}

.footer{
    text-align:center;
    color:gray;
    margin-top:40px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div class="header-box">
<h1>🎓 ScholarMatch AI</h1>
<p>AI-powered scholarship discovery platform for Indian students.</p>
<span class="badge">Verified Opportunities</span>
<span class="badge">Government & Private Grants</span>
<span class="badge">Secure Profile</span>
</div>
""", unsafe_allow_html=True)

st.info("Complete your profile to unlock scholarships that match your eligibility.")

# ---------- PROGRESS BAR ----------
progress = st.progress(0)

# ---------- TABS ----------
tab1, tab2, tab3 = st.tabs(["👤 Personal Info", "📚 Academic Profile", "🏆 Scholarship Matches"])

# ---------- TAB 1 ----------
with tab1:

    st.subheader("Basic Details")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        age = st.number_input("Age", 10, 30)

    with col2:
        current_class = st.selectbox(
            "Current Class",
            ["10th", "12th", "B.Tech 1st Year", "B.Tech 2nd Year", "Other"]
        )

        gender = st.radio(
            "Gender",
            ["Male", "Female", "Other"],
            horizontal=True
        )

    progress.progress(30)

# ---------- TAB 2 ----------
with tab2:

    st.subheader("Academic Information")

    col3, col4 = st.columns(2)

    with col3:
        marks_10 = st.number_input("10th Marks (%)", 0, 100)
        marks_12 = st.number_input("12th Marks (%)", 0, 100)

    with col4:
        income = st.number_input("Family Annual Income (₹)", 0, 2000000)

        certificates = st.multiselect(
            "Skills / Achievements",
            ["Sports (National)", "NCC", "Coding", "Music", "None"]
        )

    st.file_uploader(
        "Upload Marks Card (Optional Verification)",
        type=["pdf", "jpg", "png"]
    )

    progress.progress(70)

# ---------- TAB 3 ----------
with tab3:

    st.subheader("AI Scholarship Matching")

    if st.button("Find My Scholarships 🔎"):

        with st.spinner("AI is analyzing your eligibility..."):
            time.sleep(2)

        results = [
            {
                "name": "National Scholarship Portal (NSP)",
                "min": 80,
                "link": "https://scholarships.gov.in/",
                "desc": "Government of India scholarship program supporting meritorious students."
            },
            {
                "name": "Reliance Foundation Scholarship",
                "min": 75,
                "link": "https://www.reliancefoundation.org/",
                "desc": "Private merit-based grant for undergraduate students."
            }
        ]

        found = False

        for s in results:

            if marks_12 >= s["min"] and income <= 600000:

                found = True

                st.markdown(f"""
                <div class="scholarship-card">
                <h3>✅ {s['name']}</h3>
                <p>{s['desc']}</p>

                <p><b>Eligibility:</b> Minimum {s['min']}% marks</p>
                <p><b>Steps:</b> Register → Upload Documents → Verification</p>

                <a href="{s['link']}" target="_blank">Apply on Official Website</a>
                </div>
                """, unsafe_allow_html=True)

        if not found:
            st.warning("No scholarships matched your profile yet. Try updating your details.")

    progress.progress(100)

# ---------- SIDEBAR ----------
st.sidebar.header("🔔 Scholarship Alerts")

st.sidebar.success("New: Tata Scholarship 2026 OPEN")

st.sidebar.info("Deadline: NSP closes in 4 days")

st.sidebar.write("---")

st.sidebar.write("📊 Platform Stats")
st.sidebar.write("Students Helped: **12,000+**")
st.sidebar.write("Scholarships Listed: **150+**")

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
<p>ScholarMatch AI • Helping students discover funding opportunities</p>
<p>Disclaimer: Always verify scholarship details on official websites.</p>
</div>
""", unsafe_allow_html=True)
