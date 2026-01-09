import streamlit as st
from decision_logic import compare_paths

st.set_page_config(page_title="SmartPath – EdTech Referee", layout="centered")

st.title("🎓 SmartPath")
st.subheader("AI-guided learning path comparison")

goal = st.selectbox(
    "What is your learning goal?",
    ["Programming", "Data Science", "AI / ML", "Exam Preparation"]
)

level = st.selectbox(
    "Your experience level?",
    ["Beginner", "Intermediate", "Advanced"]
)

style = st.selectbox(
    "Preferred learning style?",
    ["Visual", "Reading", "Hands-on"]
)

if st.button("Compare Learning Paths"):
    paths, insight = compare_paths(goal, level, style)

    st.markdown("## 📊 Learning Path Comparison")

    for path, details in paths.items():
        with st.expander(path):
            st.markdown("**Pros:**")
            for p in details["pros"]:
                st.write(f"- {p}")

            st.markdown("**Cons:**")
            for c in details["cons"]:
                st.write(f"- {c}")

    st.markdown("## 🧠 Smart Insight")
    st.info(insight)