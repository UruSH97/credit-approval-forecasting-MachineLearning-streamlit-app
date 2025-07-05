
# 🏦 Credit Card Approval Prediction (ML + Streamlit)

This is an end-to-end machine learning project that predicts whether a credit card application should be approved or denied based on applicant data. The model is trained using the UCI Credit Approval dataset and deployed as a web app using Streamlit.

---

## 🚀 Project Highlights

- 📂 Dataset: [UCI Credit Approval Dataset](https://archive.ics.uci.edu/dataset/27/credit+approval)
- 🧹 Preprocessing: Imputation, Encoding, Log Transformation, Scaling
- 📊 EDA: Countplots, Boxplots, Correlation Heatmap
- 🧠 Models: Logistic Regression, Random Forest, SVM, Gradient Boosting, XGBoost
- 🔍 Tuning: GridSearchCV for best model performance
- 🌐 Deployment: Interactive web app using Streamlit
- 📦 Export: Model and scaler serialized with `joblib`

---

## 🧪 How to Run

### 🔹 1. Clone the Repository

```bash
git clone https://github.com/yourusername/credit-card-approval-prediction.git
cd credit-card-approval-prediction
```

### 🔹 2. Install Requirements

```bash
pip install -r requirements.txt
```

### 🔹 3. Run the Jupyter Notebook

```bash
jupyter notebook Credit_Card_Approval_With_Comments.ipynb
```

### 🔹 4. Launch Streamlit App

```bash
streamlit run app.py
```

---

## 📊 Features Used

| Feature           | Description                          |
|-------------------|--------------------------------------|
| Age               | Age of applicant                     |
| IncomeLog         | Log-transformed income               |
| CreditScoreLog    | Log-transformed credit score         |
| DebtLog           | Log-transformed existing debt        |
| Employed          | Employment status                    |
| PriorDefault      | History of defaulting                |
| YearsEmployed     | Work experience in years             |
| EducationLevel    | Encoded education level              |
| BankCustomer      | Whether applicant is a bank customer |
| Married           | Marital status                       |
| Citizen           | Citizenship category                 |
| Ethnicity         | Ethnicity category                   |
| Male              | Gender                               |

---

## 📁 Project Structure

```
credit-card-approval-prediction/
│
├── app.py                            # Streamlit app
├── credit_model.pkl                  # Trained model file
├── scaler.pkl                        # Trained scaler
├── requirements.txt                  # Python dependencies
├── Credit_Card_Approval_With_Comments.ipynb  # Annotated ML notebook
├── README.md                         # Project documentation
```

---

## ✅ Model Performance

- **Best Model:** Random Forest (~85% accuracy)
- Confusion matrix and classification reports included
- Hyperparameters tuned via GridSearchCV

---

## 🙋‍♀️ Author

**Uroosha Rahat**  
📫 [LinkedIn](www.linkedin.com/in/uroosharahat) | 📁 [GitHub][(https://github.com/UruSH97))]

---

## 📌 Future Improvements

- Add Explainable AI (e.g., SHAP)
- Enable API-based real-time predictions
- Add logging and error monitoring

---

## ⭐ Contributions Welcome

If you'd like to improve this project or contribute features, feel free to fork and submit a pull request! 🚀
