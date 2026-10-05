# 🎓 Student Performance Prediction

A simple Machine Learning project that predicts a student's final score using academic and lifestyle features.

## 📌 Project Overview

This project uses a Random Forest Regression model to predict a student's final score based on:

- Study hours
- Attendance
- Previous score
- Assignments completed
- Sleep hours

A Streamlit web application provides an easy interface for making predictions.

## 🛠️ Technologies Used

- Python
- Pandas
- Scikit-learn
- Random Forest Regression
- Streamlit

## 📂 Project Structure

```text
student-performance-prediction/
│
├── student_performance.csv
├── train_model.py
├── app.py
├── requirements.txt
├── student_model.pkl
└── README.md
```

## ⚙️ How to Run

### 1. Clone the repository

```bash
git clone YOUR_GITHUB_REPOSITORY_URL
cd student-performance-prediction
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Train the model

```bash
python train_model.py
```

This creates `student_model.pkl`.

### 4. Start Streamlit

```bash
streamlit run app.py
```

The application will open in your browser.

## 🤖 Machine Learning Algorithm

Random Forest Regression is used because it can learn non-linear relationships between multiple student-related features and the final score.

## 📊 Input Features

| Feature | Description |
|---|---|
| Study Hours | Daily study hours |
| Attendance | Attendance percentage |
| Previous Score | Previous examination score |
| Assignments Completed | Number of completed assignments |
| Sleep Hours | Average daily sleep |

## 🎯 Output

The application predicts the student's final score and displays a PASS/NEEDS IMPROVEMENT result.

## 🚀 Future Improvements

- Use a larger real-world dataset
- Add more student features
- Compare multiple ML algorithms
- Deploy the Streamlit application online

## 👩‍💻 Author

Student Performance Prediction - Data Science / Machine Learning Project
