import streamlit as st
import time

# ---------- PAGE CONFIG ----------
st.set_page_config(
    page_title="ScholarGate AI",
    page_icon="🎓",
    layout="wide"
)

# ---------- CUSTOM CSS ----------
st.markdown("""
<style>

.main{
background-color:#f4f6fb;
}

.header-box{
background:white;
padding:25px;
border-radius:12px;
box-shadow:0 4px 14px rgba(0,0,0,0.08);
margin-bottom:25px;
}

.step-box{
background:white;
padding:20px;
border-radius:12px;
box-shadow:0 4px 12px rgba(0,0,0,0.06);
margin-bottom:20px;
}

.match-box{
background:#1f2a44;
color:white;
padding:25px;
border-radius:14px;
margin-bottom:20px;
}

.result-card{
background:white;
padding:25px;
border-radius:14px;
box-shadow:0px 6px 18px rgba(0,0,0,0.1);
margin-bottom:20px;
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

.stButton>button{
width:100%;
height:45px;
border-radius:25px;
background:#1a73e8;
color:white;
font-size:16px;
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

<h2>🎓 ScholarGate AI</h2>
<p>Scholarship Intelligence Hub</p>

<span class="badge">✔ Secure</span>
<span class="badge">✔ Verified</span>
<span class="badge">✔ Govt & Private Scholarships</span>

</div>
""", unsafe_allow_html=True)

st.caption("Built for students who miss scholarships due to lack of awareness.")

# ---------- STEPS ----------
st.markdown("### Step 1 → Step 4 Process")

steps = st.columns(4)

steps[0].info("👤 Personal Info")
steps[1].info("📚 Academic Profile")
steps[2].info("📄 Documents")
steps[3].info("🏆 Results")

# ---------- TABS ----------
tab1, tab2, tab3 = st.tabs([
"👤 Personal Info",
"📚 Academic Profile",
"🏆 Results"
])

# ---------- PERSONAL INFO ----------
with tab1:

    st.markdown("### Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        name = st.text_input("Full Name (as per documents)")
        age = st.number_input("Age", 15, 30, 18)

    with col2:
        gender = st.selectbox(
            "Gender",
            ["Male", "Female", "Other"]
        )

        category = st.selectbox(
            "Category",
            ["General", "OBC", "SC", "ST", "EWS"]
        )

    state = st.selectbox(
        "State of Domicile",
        ["Andhra Pradesh", "Telangana", "Karnataka", "Tamil Nadu", "Other"]
    )

    disability = st.checkbox(
        "I have a disability (eligible for additional scholarships)"
    )

# ---------- ACADEMIC PROFILE ----------
with tab2:

    st.markdown("### Academic Details")

    col3, col4 = st.columns(2)

    with col3:
        marks10 = st.number_input("10th Marks (%)", 0, 100, 85)
        marks12 = st.number_input("12th Marks (%)", 0, 100, 85)

    with col4:
        income = st.number_input("Family Annual Income (₹)", 0, 2000000, 300000)

        skills = st.multiselect(
            "Achievements / Skills",
            ["Coding", "Sports", "NCC", "Music", "None"]
        )

    st.file_uploader(
        "Upload Marks Card (optional verification)",
        type=["pdf", "jpg", "png"]
    )

# ---------- RESULTS ----------
with tab3:

    st.markdown("""
    <div class="match-box">
    ✨ AI Powered Matching
    <br><br>
    Our intelligent system analyzes your profile against
    government and private scholarships to find the best matches.
    </div>
    """, unsafe_allow_html=True)

    if st.button("Find My Scholarships 🔎"):

        with st.spinner("AI analyzing your profile..."):
            time.sleep(2)

        scholarships = [

            {
            "name":"National Scholarship Portal (NSP)",
            "min":80,
            "income":600000,
            "desc":"Government of India merit scholarship",
            "link":"https://scholarships.gov.in/"
            },

            {
            "name":"Reliance Foundation Scholarship",
            "min":75,
            "income":800000,
            "desc":"Private merit based undergraduate grant",
            "link":"https://www.reliancefoundation.org/"
            },

            {
            "name":"Tata Scholarship",
            "min":85,
            "income":500000,
            "desc":"Support for high performing students",
            "link":"https://www.tatatrusts.org/"
            }

        ]

        matches = []

        for s in scholarships:

            if marks12 >= s["min"] and income <= s["income"]:

                score = min(
                    100,
                    int((marks12/s["min"])*50 + (600000/income)*50)
                )

                s["score"] = score
                matches.append(s)

        if matches:

            st.balloons()

            st.success(
                f"🎉 Great news {name}! "
                f"We found {len(matches)} scholarships for you."
            )

            for s in matches:

                st.markdown(f"""
                <div class="result-card">

                <h3 style="color:#1a73e8;">{s['name']}</h3>

                <p>{s['desc']}</p>

                <b>AI Match Score:</b> ⭐ {s['score']}%

                <br><br>

                <a href="{s['link']}" target="_blank">
                <button style="
                background:#1a73e8;
                color:white;
                border:none;
                padding:10px 20px;
                border-radius:20px;
                cursor:pointer;
                ">
                Apply Now
                </button>
                </a>

                </div>
                """, unsafe_allow_html=True)

            st.divider()

            report = f"""
ScholarGate AI Report

Student: {name}

Eligible Scholarships:
{", ".join([m['name'] for m in matches])}

Generated using ScholarGate AI
"""

            st.download_button(
                "📄 Download Eligibility Report",
                report,
                file_name="Scholarship_Report.txt"
            )

        else:

            st.warning(
            "No scholarships matched your profile currently."
            )

# ---------- FOOTER ----------
st.markdown("""
<div class="footer">
ScholarGate AI • Helping students discover funding opportunities
</div>
""", unsafe_allow_html=True)
