# Tech Support Chatbot

This repository contains the code for a simple tech support chatbot built using Python (NLTK) and Flask, with a basic HTML/JavaScript frontend.

## Overview

This chatbot is designed to answer common questions related to tech services offered, such as website designing, printer services, computer services, custom PC builds, laptop services, and social media handling. It uses basic keyword matching and synonym replacement to understand user queries and provide relevant responses.

## Files in the Repository

* **`chatbot.py`**: Contains the core logic of the chatbot, including intent recognition, response generation, and handling of synonyms.
* **`app.py`**: A Flask application that exposes the chatbot as an API endpoint (`/chat`).
* **`index.html`**: A simple HTML file providing a user interface to interact with the chatbot via a web browser.

## Getting Started

### Prerequisites

* **Python 3.x** installed on your system.
* **Pip** (Python package installer).
* **NLTK (Natural Language Toolkit)** library. You can install it using:
    ```bash
    pip install nltk
    ```
* **Flask** framework. You can install it using:
    ```bash
    pip install Flask
    ```
* **Git Bash** (or any Git client) for version control.

### Installation and Running Locally

1.  **Clone the repository (if you haven't already):**
    ```bash
    git clone <repository_url>
    cd tech-support-chatbot  # Or the name of your repository
    ```

2.  **Navigate to the project directory:**
    ```bash
    cd Ai Chatbot  # Assuming your project directory is named 'Ai Chatbot'
    ```

3.  **Run the Flask development server:**
    ```bash
    python app.py
    ```
    This will start the Flask server, usually on `http://127.0.0.1:5000/`.

4.  **Open `index.html` in your web browser:** Navigate to the location of the `index.html` file in your file system and open it with your browser. Alternatively, if you have the root route configured in `app.py`, you can go to `http://127.0.0.1:5000/` in your browser.

5.  **Interact with the chatbot:** Type your questions in the input field and click "Send". The chatbot's responses will appear in the chat window.

## Deployment

To host this chatbot online, you'll need to deploy the frontend and backend separately.

### Frontend (GitHub Pages - Static Hosting)

1.  Ensure your `index.html`, CSS (if any), and JavaScript files are in your GitHub repository.
2.  Go to your repository on GitHub.
3.  Navigate to **Settings** -> **Pages**.
4.  Under "Source", select the branch you want to use for GitHub Pages (e.g., `main`). You can also choose a specific folder like `/docs` if your frontend files are there.
5.  Click **Save**. GitHub Pages will build and deploy your static files, and you'll get a URL (e.g., `https://<your_username>.github.io/<your_repository_name>/`).

### Backend (Python Hosting Platform)

You'll need a platform that supports running Python applications. Some popular choices include:

* **Heroku:**
    * Create a `requirements.txt` file listing your dependencies (Flask, NLTK).
    * Create a `Procfile` to specify how to run your Flask app (e.g., `web: gunicorn app:app`).
    * Install the Heroku CLI and follow their deployment instructions.
* **PythonAnywhere:**
    * Create an account and upload your project files.
    * Configure a web app with your Flask application.
* **Other platforms:** Render, AWS Elastic Beanstalk, Google Cloud App Engine, Azure App Service.

**Remember to update the `fetch` URL in your `index.html` JavaScript to point to the API endpoint of your deployed Flask backend.**

## Contributing

Feel free to contribute to this project by submitting pull requests with bug fixes, improvements, or new features.

## License

[Your License Here (e.g., MIT License)]

---

**Note:** Replace `<repository_url>` with the actual URL of your GitHub repository and `[Your License Here (e.g., MIT License)]` with the appropriate license information if you choose to include one. You can also add more details about the chatbot's functionality, limitations, or future enhancements.
