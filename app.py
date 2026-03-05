import streamlit as st
import time

st.set_page_config(page_title="ScholarGate AI", page_icon="🎓", layout="wide")

# ---------- SESSION STATE ----------
if "step" not in st.session_state:
    st.session_state.step = 1

# ---------- CSS ----------
st.markdown("""
<style>

body{
background:#f4f7fc;
}

.header-box{
background:linear-gradient(135deg,#1a73e8,#3b82f6);
padding:35px;
border-radius:18px;
text-align:center;
color:white;
box-shadow:0px 10px 25px rgba(0,0,0,0.15);
margin-bottom:25px;
}

.header-title{
font-size:42px;
font-weight:700;
margin-bottom:8px;
}

.header-sub{
font-size:18px;
opacity:0.95;
}

.button-row{
display:flex;
justify-content:center;
gap:20px;
margin-top:20px;
}

.stButton>button{
border-radius:25px;
height:45px;
width:180px;
font-size:16px;
font-weight:500;
}

</style>
""", unsafe_allow_html=True)
# ---------- HEADER ----------
st.markdown("""
<div class="header-box">

<div class="header-title">
🎓 ScholarGate AI
</div>

<div class="header-sub">
AI-powered scholarship discovery platform for Indian students
</div>

</div>
""", unsafe_allow_html=True)

# ---------- STEP INDICATOR ----------
steps = st.columns(3)

steps[0].write("### 1️⃣ Personal Info")
steps[1].write("### 2️⃣ Academic Profile")
steps[2].write("### 3️⃣ Results")

# ---------- STEP 1 ----------
if st.session_state.step == 1:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Personal Information")

    col1, col2 = st.columns(2)

    with col1:
        st.session_state.name = st.text_input("Full Name")
        st.session_state.age = st.number_input("Age",15,30,18)

    with col2:
        st.session_state.gender = st.selectbox("Gender",["Male","Female","Other"])
        st.session_state.category = st.selectbox("Category",["General","OBC","SC","ST","EWS"])

    st.session_state.state = st.selectbox(
        "State of Domicile",
        ["Telangana","Andhra Pradesh","Karnataka","Tamil Nadu","Other"]
    )

    st.markdown("</div>", unsafe_allow_html=True)

    if st.button("Next ➜"):
        col1, col2, col3 = st.columns([1,1,1]
                                      with col2:
                                          next_btn = st.button("Next ➜")

# ---------- STEP 2 ----------
elif st.session_state.step == 2:

    st.markdown('<div class="card">', unsafe_allow_html=True)

    st.subheader("Academic Profile")

    col1,col2 = st.columns(2)

    with col1:
        st.session_state.marks10 = st.number_input("10th Marks %",0,100,85)
        st.session_state.marks12 = st.number_input("12th Marks %",0,100,85)

    with col2:
        st.session_state.income = st.number_input("Family Annual Income ₹",0,2000000,300000)
        st.session_state.skills = st.multiselect(
            "Skills",
            ["Coding","Sports","NCC","Music","None"]
        )

    st.file_uploader("Upload Marks Card")

    st.markdown("</div>", unsafe_allow_html=True)

    col1,col2 = st.columns(2)

    with col1:
        if st.button("⬅ Back"):
            st.session_state.step = 1
            st.rerun()

    with col2:
        if st.button("Next ➜"):
            st.session_state.step = 3
            st.rerun()

# ---------- STEP 3 ----------
elif st.session_state.step == 3:

    st.markdown("""
    <div class="matchbox">
    ✨ AI Powered Matching
    <br><br>
    Our AI analyzes your academic profile and income
    to find scholarships you are eligible for.
    </div>
    """, unsafe_allow_html=True)

    if st.button("Find My Scholarships 🔎"):

        with st.spinner("AI analyzing your profile..."):
            time.sleep(2)

        scholarships = [

        {
        "name":"National Scholarship Portal",
        "min":80,
        "income":600000,
        "link":"https://scholarships.gov.in/"
        },

        {
        "name":"Reliance Foundation Scholarship",
        "min":75,
        "income":800000,
        "link":"https://www.reliancefoundation.org/"
        },

        {
        "name":"Tata Scholarship",
        "min":85,
        "income":500000,
        "link":"https://www.tatatrusts.org/"
        }

        ]

        matches = []

        for s in scholarships:
            if st.session_state.marks12 >= s["min"] and st.session_state.income <= s["income"]:
                matches.append(s)

        if matches:

            st.success(f"We found {len(matches)} scholarships for you!")

            for s in matches:

                st.markdown(f"""
                <div class="card">

                <h3>{s['name']}</h3>

                Eligible based on your marks and income.

                <br><br>

                <a href="{s['link']}" target="_blank">
                <button style="background:#1a73e8;color:white;border:none;padding:10px 20px;border-radius:20px;">
                Apply Now
                </button>
                </a>

                </div>
                """, unsafe_allow_html=True)

        else:
            st.warning("No scholarships matched your profile.")

    if st.button("⬅ Back"):
        col1, col2, col3 = st.columns([1,1,1])
        with col1:
        back_btn = st.button("⬅ Back")
        with col3:
        next_btn = st.button("Next ➜")
