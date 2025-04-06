# Recipe App

This is a Django-based recipe app where authorized users can view, share, edit, and delete recipes.

## Setup Instructions

Follow these steps to set up the project:

### 1. Install Dependencies

First, make sure you have Python 3.10.11 installed. Then, create and activate a virtual environment (if you haven't already):

```bash
# Create virtual environment (if not already created)
python -m venv venv

# Activate virtual environment
# On Windows
.\venv\Scripts\activate
# On macOS/Linux
source venv/bin/activate

Once your virtual environment is active, install the required dependencies listed in requirements.txt:
pip install -r requirements.txt

2. Configure Email Settings
In the project's settings.py, you'll need to add your email credentials. Since the email and password fields have been removed for security reasons, you will need to provide your own values.
Locate these lines in settings.py:
EMAIL_HOST_USER = ""
EMAIL_HOST_PASSWORD = ""
Replace the empty quotes with your email and password:
EMAIL_HOST_USER = "your-email@example.com"
EMAIL_HOST_PASSWORD = "your-email-password"

3. Migrate Database
Run the migrations to set up your database:
python manage.py migrate

4. Run the Development Server
Start the development server:
python manage.py runserver

Note:
Please make sure to keep your email credentials private and don't share them publicly.
You can use any email service like Gmail or others for EMAIL_HOST_USER and EMAIL_HOST_PASSWORD.