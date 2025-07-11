💼 Salary Prediction Project

This project focuses on predicting employee salaries using machine learning techniques based on a variety of features such as education level, years of experience, job title, industry, location, and more. It aims to assist organizations in making informed salary decisions and understanding compensation patterns within their workforce.

🔍 Project Overview

Accurately predicting salaries helps companies optimize compensation strategies and ensures competitiveness in the job market. By leveraging historical salary data and employee attributes, this project builds a model that can estimate expected salaries for new or existing employees.

🛠 Features Used

* Education Level: Highest qualification attained by the employee.
* Years of Experience: Total work experience in years.
* Job Title: Designation or role of the employee.
* Industry: The sector in which the employee works.
* Location: Geographic location of the job.
* Company Size: Size of the company (small, medium, large).
* Certifications: Relevant professional certifications.
* Age: Employee’s age.
* Working Hours: Number of hours worked weekly.
* Crucial Code: A domain-specific code affecting salary (could be skill or department code).

📊 Data Preprocessing

* Removed rows with missing salary values from training data to ensure quality.
* Handled missing values in features:
   * Filled numerical missing values with column means.
   * Filled categorical missing values with the most frequent category (mode).
* Encoded categorical variables using one-hot encoding to convert them into a machine-readable format.
* Scaled all feature values using StandardScaler to normalize data distribution, which improves model performance.

⚙️ Model Building

* Algorithm: Random Forest Regressor
* Parameters: 50 decision trees (n_estimators=50), fixed random_state for reproducibility.
* Training: Data split into 80% training and 20% validation.
* Evaluation Metric: Root Mean Squared Error (RMSE) calculated on validation data to quantify prediction accuracy.


