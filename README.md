# CivicReport India

A community-driven platform for reporting and tracking local infrastructure issues.

## Project Overview
- Map-based reporting system
- Community verification system
- Authority collaboration platform
- Issue tracking and analytics

### How It's Being Built

This project is being built with a lot Vibe coding. We have the vision, and we're using AI to write the code and bring it to life.

## Requirements

- Python 3.10+ (tested on Python 3.13, but 3.10+ should work)
- pip (Python package manager)
- Git (for cloning the repo)
- Linux (Should work on mac and windows, but the commands might be slightly different (especially for activating the virtual environment).)
- Node.js & npm (optional, only if you want to hack on frontend assets)

## How to Run Locally (for total beginners)

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/civicreport-India.git
   cd civicreport-India
   ```

2. **Set up a Python virtual environment**
   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **Install Python dependencies**
   ```bash
   pip install -r requirements.txt
   ```
   > If you don't see a `requirements.txt`, just run:
   > ```bash
   > pip install django
   > ```

4. **Set up the database**
   ```bash
   python manage.py migrate
   ```

5. **Create an admin user (so you can log in to /admin)**
   ```bash
   python manage.py createsuperuser
   ```
   > Follow the prompts for username, email, password.

6. **Run the server**
   ```bash
   python manage.py runserver
   ```
   > Now open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

7. **(Optional) Collect static files for production**
   ```bash
   python manage.py collectstatic
   ```
   > Not needed for local dev, but good to know for deployment.

---

## Hosting/Deployment

For now, this guide is for running on your own machine. If you want to put it online, you're welcome.

We'll add full deployment guides soon!

---


