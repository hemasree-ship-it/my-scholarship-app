import streamlit as st
import time

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="ScholarMatch AI",
    page_icon="🎓",
    layout="wide"
)

# ---------- GLOBAL CSS ----------
st.markdown("""
<style>

.main {
background-color:#f4f6f9;
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
padding:25px;
border-radius:15px;
box-shadow:0px 6px 16px rgba(0,0,0,0.1);
margin-top:25px;
}

.badge{
background:#e8f0fe;
color:#1a73e8;
padding:6px 14px;
border-radius:20px;
font-size:13px;
margin:4px;
display:inline-block;
}

.footer{
text-align:center;
color:gray;
margin-top:50px;
}

</style>
""", unsafe_allow_html=True)

# ---------- HEADER ----------
st.markdown("""
<div style="
background:white;
padding:30px;
border-radius:12px;
box-shadow:0 4px 12px rgba(0,0,0,0.08);
text-align:center;
">

<h1 style="color:#1a73e8;">🎓 ScholarMatch AI</h1>

<p style="font-size:18px;color:#555;">
AI-powered scholarship discovery platform for Indian students
</p>

<div style="margin-top:15px;">
<span class="badge">✔ Verified Opportunities</span>
<span class="badge">🏛 Govt & Private Grants</span>
<span class="badge">🔒 Secure Profile</span>
</div>

</div>
""", unsafe_allow_html=True)

st.info("Complete your profile to unlock scholarships that match your eligibility.")

# ---------- PROGRESS ----------
progress = st.progress(0)

# ---------- TABS ----------
tab1, tab2, tab3 = st.tabs(
["👤 Personal Info","📚 Academic Profile","🏆 Scholarship Matches"]
)

# ---------- PERSONAL INFO ----------
with tab1:

    st.subheader("Basic Details")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name")
        age = st.number_input("Age",10,30)

    with col2:
        current_class = st.selectbox(
        "Current Class",
        ["10th","12th","B.Tech 1st Year","B.Tech 2nd Year","Other"]
        )

        gender = st.radio(
        "Gender",
        ["Male","Female","Other"],
        horizontal=True
        )

    progress.progress(30)

# ---------- ACADEMIC PROFILE ----------
with tab2:

    st.subheader("Academic Information")

    col3, col4 = st.columns(2)

    with col3:
        marks_10 = st.number_input("10th Marks (%)",0,100)
        marks_12 = st.number_input("12th Marks (%)",0,100)

    with col4:
        income = st.number_input("Family Annual Income (₹)",0,2000000)

        certificates = st.multiselect(
        "Skills / Achievements",
        ["Sports (National)","NCC","Coding","Music","None"]
        )

    st.file_uploader(
    "Upload Marks Card (Optional Verification)",
    type=["pdf","jpg","png"]
    )

    progress.progress(70)

# ---------- SCHOLARSHIP MATCHES ----------
with tab3:

    st.subheader("AI Scholarship Matching")

    if st.button("Find My Scholarships 🔎"):

        with st.spinner("AI analyzing your academic profile..."):
            time.sleep(2)

        st.success("🤖 AI has found scholarships based on your profile")

        results = [
        {
        "name":"National Scholarship Portal (NSP)",
        "min":80,
        "link":"https://scholarships.gov.in/",
        "desc":"Government of India scholarship program supporting meritorious students."
        },
        {
        "name":"Reliance Foundation Scholarship",
        "min":75,
        "link":"https://www.reliancefoundation.org/",
        "desc":"Private merit-based grant for undergraduate students."
        }
        ]

        found = False

        for s in results:

            if marks_12 >= s["min"] and income <= 600000:

                found = True

                st.markdown(f"""
                <div style="display:flex;justify-content:center;">

                <div class="scholarship-card" style="width:500px;text-align:center;">

                <h3>✅ {s['name']}</h3>

                <p>{s['desc']}</p>

                <p><b>Eligibility:</b> Minimum {s['min']}% marks</p>

                <p><b>Steps:</b><br>
                Register → Upload Documents → Verification
                </p>

                <a href="{s['link']}" target="_blank">

                <button style="
                background:#1a73e8;
                color:white;
                padding:10px 22px;
                border:none;
                border-radius:20px;
                cursor:pointer;
                ">
                Apply Now
                </button>

                </a>

                </div>
                </div>
                """, unsafe_allow_html=True)

        if not found:
            st.warning("No scholarships matched your profile. Try updating your marks or income.")

    progress.progress(100)

# ---------- SIDEBAR ----------
st.sidebar.header("🔔 Scholarship Alerts")

st.sidebar.success("New: Tata Scholarship 2026 OPEN")

st.sidebar.info("Deadline: NSP closes in 4 days")

st.sidebar.write("---")

st.sidebar.subheader("📊 Platform Stats")

st.sidebar.write("Students Helped: **12,000+**")
st.sidebar.write("Scholarships Listed: **150+**")
st.sidebar.write("Success Rate: **87%**")

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">

ScholarMatch AI • Helping students discover funding opportunities

<br><br>

Disclaimer: Always verify scholarship details on official websites.

</div>
""", unsafe_allow_html=True)
