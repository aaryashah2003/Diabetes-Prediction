A Flask web application that uses machine learning models to make predictions based on user input, featuring a simple interface with landing, form, and result pages.”# 🧠 Machine Learning Web Application
This project is a Flask web application that utilizes machine learning models to make predictions based on user input. The application has a simple and intuitive interface, allowing users to submit forms and receive results based on the predictions made by the model. The core features of the project include a landing page, a form page, and a result page, all of which are handled by the `app.py` file. The application relies on a machine learning model loaded from the `multi.pkl` file, which is used to make predictions based on user input.

## 🚀 Features
- **Landing Page**: A simple landing page that welcomes users and provides a link to the form page.
- **Form Page**: A page where users can submit forms with their input, which is then processed by the application.
- **Result Page**: A page that displays the results of the prediction made by the machine learning model.
- **Machine Learning Model**: A model loaded from the `multi.pkl` file, which is used to make predictions based on user input.
- **User Input Processing**: The application processes user input and creates a Pandas DataFrame, which is then used to make predictions.

## 🛠️ Tech Stack
* **Frontend**: HTML, CSS, JavaScript
* **Backend**: Flask, Python
* **Database**: None
* **Machine Learning**: Scikit-learn, XGBoost, Joblib
* **Dependencies**: NumPy, Pandas, Pickle
* **Package Manager**: Poetry
* **Build Tool**: Replit

## 📦 Installation
To install the project, follow these steps:
1. **Prerequisites**: Python 3.8 or later, Replit, Flask, XGBoost, and Joblib.
2. **Installation**: Run `poetry install` to install the dependencies specified in the `pyproject.toml` file.
3. **Running locally**: Run `python app.py` to start the Flask development server.

## 💻 Usage
1. **Access the landing page**: Open a web browser and navigate to `http://0.0.0.0:81`.
2. **Submit a form**: Click on the link to the form page and submit a form with your input.
3. **View the results**: The application will display the results of the prediction made by the machine learning model.

## 📂 Project Structure
```markdown
.
├── app.py
├── main.py
├── model.json
├── multi.pkl
├── pyproject.toml
├── static
│   ├── css
│   ├── js
│   └── ...
├── templates
│   ├── index.html
│   ├── form.html
│   ├── result.html
│   └── ...
└── ...
```
