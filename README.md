# Synergy

## Introduction
Synergy is a Django-based web application. This README provides step-by-step instructions to set up the project from scratch, including creating a virtual environment, installing dependencies, applying migrations, and running the server.

---

## Installation Guide

### 1. Clone the Repository
```bash
git clone https://github.com/frankmathewsajan/Synergy.git
cd Synergy
```

### 2. Set Up a Virtual Environment
It is recommended to use a virtual environment to manage dependencies.

For Windows:
```bash
python -m venv venv
venv\Scripts\activate
```

For macOS/Linux:
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
Once inside the virtual environment, install the required dependencies:
```bash
pip install -r requirements.txt
```

---

## Database Setup & Migrations

### 4. Apply Migrations
Django uses migrations to set up the database schema.

```bash
python manage.py migrate
```

If you want to create a superuser for the Django admin panel:
```bash
python manage.py createsuperuser
```
Follow the prompts to set up a username, email, and password.

---

## Running the Server

### 5. Start the Development Server
Run the following command to start the Django development server:
```bash
python manage.py runserver
```
The server will be accessible at:
```
http://127.0.0.1:8000/
```

---

## Environment Variables
Make sure to set up a `.env` file to store sensitive information like database credentials, secret keys, and API keys. Use the `.gitignore` file to prevent committing it to Git.

Example `.env` file:
```
SECRET_KEY=your_secret_key
DEBUG=True
DATABASE_URL=your_database_url
```

To load environment variables, install `django-environ` if not already installed:
```bash
pip install django-environ
```

Then, update `settings.py` to use `.env` variables.

---

## Additional Commands

### Collect Static Files (For Deployment)
```bash
python manage.py collectstatic
```

### Running Tests
```bash
python manage.py test
```

---

## Contributing
If you’d like to contribute, fork the repository and submit a pull request.

---

## License
This project is licensed under the MIT License.

---

## Contact
For any questions or issues, feel free to reach out:
- **GitHub:** [frankmathewsajan](https://github.com/frankmathewsajan)
- **Email:** frankmathewsajan@gmail.com

