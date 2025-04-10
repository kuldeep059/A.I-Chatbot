# Tech Support Chatbot

This repository contains the code for a simple tech support chatbot built using Python (NLTK) and Flask, with a basic HTML/JavaScript frontend.

## Overview

This chatbot is designed to answer common questions related to tech services offered, such as website designing, printer services, computer services, custom PC builds, laptop services, and social media handling. It uses basic keyword matching and synonym replacement to understand user queries and provide relevant responses.

## Files in the Repository

* **`chatbot.py`**: Contains the core logic of the chatbot, including intent recognition, response generation, and handling of synonyms.
* **`app.py`**: A Flask application that exposes the chatbot as an API endpoint (`/chat`).
* **`index.html`**: A simple HTML file providing a user interface to interact with the chatbot via a web browser.

* ## Screenshot

![Chatbot Interface](https://github.com/kuldeep059/A.I-Chatbot/blob/main/Project%20Image.png)

*A screenshot of the chatbot interface in action.*


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
    This will start the Flask server, usually on `http://127.0.0.1:5001/`.

4.  **Open `index.html` in your web browser:** Navigate to the location of the `index.html` file in your file system and open it with your browser. Alternatively, if you have the root route configured in `app.py`, you can go to `http://127.0.0.1:5001/` in your browser.

5.  **Interact with the chatbot:** Type your questions in the input field and click "Send". The chatbot's responses will appear in the chat window.

## Deployment

To host this chatbot online, you'll need to deploy the frontend and backend separately.

## Contributing

Feel free to contribute to this project by submitting pull requests with bug fixes, improvements, or new features.

## License

[Your License Here (e.g., MIT License)]

---

**Note:** Replace `<repository_url>` with the actual URL of your GitHub repository and `[Your License Here (e.g., MIT License)]` with the appropriate license information if you choose to include one. You can also add more details about the chatbot's functionality, limitations, or future enhancements.
