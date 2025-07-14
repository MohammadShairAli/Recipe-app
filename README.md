# Recipe App

This is a Dockerized Django-based recipe app where authorized users can view, share, edit, and delete recipes.

## Setup Instructions

Follow these steps to set up the project:

1. Install Docker

Make sure you have Docker Desktop installed and running on your system: https://www.docker.com/products/docker-desktop/

2. Clone the Repository

git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name

3. Build the Docker Image

docker build -t myapp .

4. Run the Docker Container

docker run -p 8000:8000 myapp

5. Visit the App

Open your browser and go to:
http://localhost:8000

The container will automatically:
- Make migrations (if needed)
- Apply database migrations
- Start the Django development server

## Email Configuration

If email functionality is required, open the project's settings.py and update the following lines:

EMAIL_HOST_USER = "your-email@example.com"
EMAIL_HOST_PASSWORD = "your-email-password"

Make sure to keep your email credentials private and never push them to GitHub. You can use any email service like Gmail or others for EMAIL_HOST_USER and EMAIL_HOST_PASSWORD.

## Notes

- You no longer need to install Python or set up a virtual environment manually — Docker handles everything.
- Ensure port 8000 is not already in use. If it is, use another port like this:

docker run -p 8001:8000 myapp

- Optionally, you can create a .env file and load credentials securely in production environments.
