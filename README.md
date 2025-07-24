# Credit Card Approval Prediction (ML + Streamlit)

This project is a complete machine learning pipeline that predicts whether a credit card application should be approved based on applicant information. The model is trained on the UCI Credit Approval dataset and deployed as an interactive web app using Streamlit.

---

## Project Highlights

- Dataset: UCI Credit Approval Dataset  
- Preprocessing steps include imputation, encoding, log transformation, and scaling  
- Exploratory Data Analysis: count plots, box plots, and correlation heatmaps  
- Models trained and evaluated: Logistic Regression, Random Forest, SVM, Gradient Boosting, and XGBoost  
- Best-performing model selected using GridSearchCV  
- The final model is deployed as a web application using Streamlit  
- Trained model and scaler are serialized using joblib for reuse  

---

## How to Run the Project

1. Clone the repository:

```bash
git clone https://github.com/yourusername/credit-card-approval-prediction.git
cd credit-card-approval-prediction
```

2. Install the required Python packages:

```bash
pip install -r requirements.txt
```

3. Run the Jupyter Notebook to explore the code and model training steps:

```bash
jupyter notebook Credit_Card_Approval_With_Comments.ipynb
```

4. Launch the Streamlit application locally:

```bash
streamlit run app.py
```

---

## Features Used for Prediction

| Feature         | Description                          |
|----------------|--------------------------------------|
| Age            | Age of the applicant                 |
| IncomeLog      | Log-transformed income               |
| CreditScoreLog | Log-transformed credit score         |
| DebtLog        | Log-transformed existing debt        |
| Employed       | Employment status                    |
| PriorDefault   | History of defaulting on loans       |
| YearsEmployed  | Years of work experience             |
| EducationLevel | Encoded education level              |
| BankCustomer   | Whether the applicant is a bank customer |
| Married        | Marital status                       |
| Citizen        | Citizenship category                 |
| Ethnicity      | Ethnic background                    |
| Male           | Gender                               |

---

## Project Structure

```
credit-card-approval-prediction/
├── app.py                                # Streamlit web app
├── credit_model.pkl                      # Trained ML model
├── scaler.pkl                            # Scaler used for preprocessing
├── requirements.txt                      # List of Python dependencies
├── Credit_Card_Approval_With_Comments.ipynb  # Annotated notebook
├── README.md                             # Project documentation
```

---

## Model Performance

- Best model: Random Forest with approximately 85% accuracy on test data  
- Evaluation includes confusion matrix and classification report  
- Hyperparameters optimized using GridSearchCV  

---

## Author

Uroosha Rahat  
GitHub: [https://github.com/UruSH97](https://github.com/UruSH97)

---

## Possible Improvements

- Add explainability using SHAP or similar tools  
- Expose prediction through an API endpoint for integration  
- Implement logging and error tracking for better observability  

---

## Contributions

Open to improvements, new features, or bug fixes. Feel free to fork the repository and submit a pull request.
README_Cre ... pproval.md
Displaying README_Credit_Card_Approval.md.
