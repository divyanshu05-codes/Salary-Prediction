import streamlit as st
import requests

# ================= IBM Cloud Auth Setup ==================
API_KEY = "z8ZcqooiyEDJVLajHBGQKdRzVvLxHVlmHR_RxsOZkxl4"

st.title("💼 Salary Prediction App")
st.write("Enter your job details to predict the salary.")

# Try to fetch token silently
try:
    token_response = requests.post(
        'https://iam.cloud.ibm.com/identity/token',
        data={"apikey": API_KEY, "grant_type": 'urn:ibm:params:oauth:grant-type:apikey'}
    )
    token_response.raise_for_status()
    mltoken = token_response.json()["access_token"]
    header = {'Content-Type': 'application/json', 'Authorization': 'Bearer ' + mltoken}
except Exception as e:
    st.error(f"❌ Failed to get access token: {e}")
    st.stop()

# ================ User Input Form ==================
education = st.selectbox("🎓 Education Level", ["High School", "Bachelors", "Masters", "PhD"])
experience = st.slider("📊 Years of Experience", 0, 40, 5)
job_title = st.selectbox("💼 Job Title", ["Data Scientist", "Software Engineer", "Analyst", "Manager"])
industry = st.selectbox("🏭 Industry", ["IT", "Healthcare", "Education", "Finance"])
location = st.text_input("📍 Location", "New York")
company_size = st.selectbox("🏢 Company Size", ["Small", "Medium", "Large"])
certifications = st.slider("🎖 Number of Certifications", 0, 10, 1)
age = st.slider("🎂 Age", 18, 65, 30)
working_hours = st.slider("⏱ Working Hours per Week", 20, 80, 40)

# Predict button
if st.button("🚀 Predict Salary"):
    st.write("📡 Sending data to IBM Watson ML...")

    # Build payload (include crucial_code with default)
    payload_scoring = {
        "input_data": [
            {
                "fields": [
                    "ID", "education_level", "years_experience", "job_title",
                    "industry", "location", "company_size", "certifications",
                    "age", "working_hours", "crucial_code"
                ],
                "values": [[
                    1, education, experience, job_title, industry, location,
                    company_size, certifications, age, working_hours, "None"
                ]]
            }
        ]
    }

    # Send request to deployed model
    try:
        response_scoring = requests.post(
            'https://au-syd.ml.cloud.ibm.com/ml/v4/deployments/ae34f7e8-64e6-4f62-a5a9-2612d2cbd266/predictions?version=2021-05-01',
            json=payload_scoring,
            headers=header
        )
        response_scoring.raise_for_status()

        prediction = response_scoring.json()
        salary = prediction["predictions"][0]["values"][0][0]
        st.success(f"💰 Predicted Salary: ${salary:,.2f}")

    except Exception as e:
        st.error("❌ Prediction failed.")
        st.code(response_scoring.text)
        st.stop()