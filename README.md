```
# 📝 Blog App

A full-featured blog application built with Django and PostgreSQL, allowing users to create, manage, and interact with posts.

## 🚀 Features

- **User Authentication**: Register, login, change password, and reset password.
- **Post Management**: Add, update, and delete posts.
- **Media Support**: Upload profile pictures and multiple images per post.
- **Engagement**: Like and comment on posts.

## 🛠 Tech Stack

- **Backend**: Python, Django
- **Database**: PostgreSQL
- **Frontend**: Django templates, HTML, CSS, JavaScript

## 📂 Installation

1. Clone the repository:
   ```sh
   git clone https://github.com/mevadasmit/BlogApp.git
   cd blog-app
   ```

2. Create and activate a virtual environment:
   ```sh
   python -m venv venv
   source venv/bin/activate
   On Windows use `venv\Scripts\activate`
   ```

3. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```

4. Apply migrations:
   ```sh
   python manage.py migrate
   ```

5. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```

6. Run the server:
   ```sh
   python manage.py runserver
   ```

7. Open the app in your browser:
   ```
   http://127.0.0.1:8000/
   ```


## 📜 License

This project is licensed under the MIT License.
```
