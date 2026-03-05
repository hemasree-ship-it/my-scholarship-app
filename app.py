import streamlit as st

# 1. The Title - Make it look professional!
st.set_page_config(page_title="Scholar-AI", page_icon="🎓")
st.title("🎓 Scholar-AI: Your Grant Matchmaker")
st.subheader("Helping you find the money for your dreams.")

# 2. The Inputs - Ask the student for their details
name = st.text_input("What is your name?")
marks = st.slider("What was your 12th Grade percentage?", 0, 100, 75)
income = st.number_input("Family Annual Income (in ₹)", value=500000)

# 3. The Database - (Like a small digital diary of scholarships)
scholarships = [
    {"name": "National Merit Support", "min_marks": 85, "max_income": 600000, "amt": "₹50,000"},
    {"name": "Udaan Scholarship (Girls only)", "min_marks": 70, "max_income": 300000, "amt": "₹30,000"},
    {"name": "Tech Future Grant", "min_marks": 60, "max_income": 800000, "amt": "₹25,000"}
]

# 4. The Matchmaker Logic
if st.button("Find My Scholarships! ✨"):
    st.write(f"### Hello {name}, here is what we found:")
    matches = [s for s in scholarships if marks >= s['min_marks'] and income <= s['max_income']]
    
    if matches:
        for m in matches:
            st.success(f"✅ **{m['name']}** - You can get **{m['amt']}**!")
    else:
        st.warning("No perfect matches yet, but don't give up! Try checking local NGO grants.")
