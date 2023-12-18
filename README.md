# Breast Cancer Prediction Model with Django

This is the final project of the **Harvard CS50 Course - Inroduction to Web Programming Using Python and Javascript**, the **Breast Cancer Predictor**. This project aims to provide a Breast Cancer Prediction Model implemented using Django, HTML, CSS, JavaScript, and Python. The model predicts the type of breast cancer based on input features, and the web interface allows users to interact with the model easily.

## Technologies Used

- Django: A high-level Python web framework for rapid development.
- HTML: Markup language for creating the structure of the web pages.
- CSS: Stylesheet language for designing the appearance of the web pages.
- JavaScript: Programming language for enhancing user interactivity.
- Python: Backend language for building the predictive model.
- RESTful API: Utilized to handle communication between the frontend and backend.
- Sqlite: Database Instance used for storing data.
  
## Project Structure

The project is organized as follows:

- **/cancerpredictor**: Django app containing the backend and frontend logic.
  - **/static**: Folder for static files such as CSS and JavaScript.
  - **/templates**: HTML templates for rendering the web pages.
  - **/views.py**: Python file containing backend logic and API endpoints.
  - **/models.py**: Definition of the breast cancer prediction model.
  - **/urls.py**: URL configurations for the app.

## Models
- **User**: Used AbstractUser model for storing the user's general information such as first name, username, etc.
- **PateintData**: Used for storing user's info and the outcome of the test process i.e, Benign(B) or Malignant(M)
- **Message**: Used for storing the message left by the user for us.

## Web Pages
- **Login/ Signup Page**: Gateway to enter the main website
- **Home Page**: Gives a brief description of the breast cancer and its remedies.
- **Prediction Page**: Used for entering the input and viewing the predicted outcome.
- **About Us Page**: Gives a short description of the motivation behind this project.
- **Contact Us Page**: Used for getting feedback from the users.

## Installation

1. Clone the repository:

```bash
git clone https://github.com/vasu2901/final.git
cd final
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Run migrations:

```bash
python manage.py migrate
```

4. Start the development server:

```bash
python manage.py runserver
```

Visit http://127.0.0.1:8000/ in your web browser to access the application.

## Usage

1. Open the web application in your browser.
2. Login to your application and go to Prediction web page.
3. Enter the relevant features for breast cancer prediction.
4. Click the "Submit" button to submit the input to the backend.
5. View the predicted result on the webpage.


## JavaScript API Calls

The JavaScript in the frontend is responsible for making API call to the backend for predicting the type of breast cancer. Once we click on the submit button, an API call is made to the backend
submitting the form values and returning the result in JSON format.

```javascript

Happy coding!