import streamlit as st
import pickle
import pandas as pd

st.set_page_config(
    page_title="Student Performance Predictor",
    page_icon="🎓"
)

# Load trained model
with open("student_model.pkl", "rb") as file:
    model = pickle.load(file)

st.title("🎓 Student Performance Predictor")
st.write("Predict a student's final score using academic and lifestyle information.")

st.sidebar.header("Student Details")

study_hours = st.sidebar.slider("Study Hours per Day", 0.0, 12.0, 4.0)
attendance = st.sidebar.slider("Attendance (%)", 0, 100, 80)
previous_score = st.sidebar.slider("Previous Score", 0, 100, 75)
assignments = st.sidebar.slider("Assignments Completed", 0, 10, 7)
sleep_hours = st.sidebar.slider("Sleep Hours", 0.0, 12.0, 7.0)

input_data = pd.DataFrame({
    "study_hours": [study_hours],
    "attendance": [attendance],
    "previous_score": [previous_score],
    "assignments_completed": [assignments],
    "sleep_hours": [sleep_hours]
})

if st.button("Predict Final Score"):
    prediction = model.predict(input_data)[0]
    prediction = max(0, min(100, prediction))

    st.success(f"Predicted Final Score: {prediction:.2f}%")

    if prediction >= 40:
        st.info("Result: PASS ✅")
    else:
        st.warning("Result: NEEDS IMPROVEMENT ⚠️")

st.markdown("---")
st.caption("Built with Python, Pandas, Scikit-learn and Streamlit")
