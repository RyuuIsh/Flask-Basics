# 🚀 Flask Web App with Blueprints
This project demonstrates how to build a Flask web application, starting from a basic app and extending it using Blueprints for a modular structure.

## Features
- Basic Flask Web App – Simple routes (`/`, `/bye`, `/username/<name>/<int:number>`) 🌍
- Blueprints Implementation – Organized routes into separate modules 📂
- Main Routes (`/`, `/about`) – General app pages 🌐
- User Routes (`/user/profile`, `/user/settings`) – User-specific pages 👤

## Tech Stack
- Python 🐍 – Backend logic
- Flask 🌎 – Web framework
- Blueprints 🏗 – Modular architecture

## Project Structure
```
/flask_web_app
│── /routes
│   │── __init__.py
│   │── main.py
│   │── user.py
│── app.py
```
## 1️⃣ Basic Flask Web App
`app.py` (Basic Flask App)

## 2️⃣ Flask Blueprints Implementation
Blueprints allow us to break a large Flask app into smaller, manageable modules.

`app.py` (Main Application File)

`routes/__init__.py`
*(Leave this file empty; it makes `routes` a package.)*

`routes/main.py` (Main Routes Blueprint)
`routes/user.py` (User Routes Blueprint)

## Setup & Usage
### Clone the Repository
```
git clone https://github.com/yourusername/Flask-Web-App.git
cd Flask-Web-App
```

### Install Dependencies
```
pip install flask
```

### Run the App
```
python app.py
```
💡 Open `http://127.0.0.1:5000/` in your browser!
📌 Endpoints:
1. Basic Routes:
- `/` → Home Page
- `/bye` → Simple "Bye" Response
- `/username/<name>/<number>` → Dynamic Greeting
2. Blueprint Routes:
- `/about` → About Page
- `/user/profile` → User Profile
- `/user/settings` → User Settings

## Future Enhancements
- Add User Authentication 🔐
- Implement Database Integration 🗄
- Create an API with Flask-RESTful 🚀

💙 Master Flask Development with Blueprints! 🚀










