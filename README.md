# Formgeine (Backend)

An AI-powered assistant designed to make navigating complex government forms in India simple and stress-free. This repository contains the backend server that acts as the "brain" for the Co-Pilot .

---

## The Problem

Applying for a passport, filing taxes, or accessing government services in India often involves filling out long, complicated forms filled with confusing jargon. For millions of citizens—students, senior citizens, and even the tech-savvy—this process is intimidating. A single mistake can lead to long delays and immense frustration. This "bureaucratic friction" is a major barrier to accessing essential services.

## Our Solution

**Formgeine** is an intelligent assistant that acts as a friendly expert, guiding users through these forms in real-time. This backend powers the Co-Pilot, providing instant, accurate, and multi-modal answers to user queries. Instead of feeling lost, the user feels empowered and confident.

### Core Features
* **Intelligent Form Guidance:** Leverages **GPT-4-Turbo** to provide clear, simple explanations for complex government terminology and processes.
* **Multi-Modal Vision:** Utilizes **GPT-4-Vision** to analyze screenshots of form sections, allowing users to simply point at what they don't understand.
* **Secure by Design:** The backend processes queries on the fly and does not store any personal user data or uploaded documents.
* **scalable Foundation:** Built with a lightweight Flask server, ready to support a full-featured browser extension frontend.

---

##  Tech Stack

* **Backend:** Python 3.10+
* **Framework:** Flask
* **AI:** OpenAI API (GPT-4-Turbo & GPT-4-Vision)
* **Dependencies:** `Flask`, `python-dotenv`, `openai`, `flask-cors`

---

##  Getting Started

Follow these instructions to get the backend server running on your local machine.

### Prerequisites
* Python 3.10 or higher
* An OpenAI API Key

### Installation & Setup

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/your-username/formgenie.git](https://github.com/your-username/formgenie.git)
    cd formgenie
    ```

2.  **Create a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3.  **Install the required packages:**
    ```bash
    pip install Flask python-dotenv openai flask-cors
    ```

4.  **Set up your environment variables:**
    * Create a file named `.env` in the root of the project folder.
    * Add your OpenAI API key to this file:
    ```
    OPENAI_API_KEY="sk-your_secret_api_key_here"
    ```

5.  **Run the server:**
    ```bash
    python app.py
    ```
    The server will start running on `http://127.0.0.1:5000`. You'll see a confirmation message in your terminal that the OpenAI client was initialized successfully.

---

##  API Usage & Demo

You can test the API using `curl` from your terminal.

### Endpoint: `/api/ask`
* **Method:** `POST`
* **Body (JSON):**
    * `prompt` (string, required): The user's question.
    * `image_data_url` (string, optional): A base64-encoded data URL of the image for vision queries.

#### **Example 1: Text-Only Query**

This simulates a user asking a simple text question.

```bash
curl -X POST -H "Content-Type: application/json" \
-d '{"prompt": "What does Non-ECR mean on a passport application?"}' \
[http://127.0.0.1:5000/api/ask](http://127.0.0.1:5000/api/ask)

```
#### **Response**

```bash
{
  "answer": "It means 'Emigration Check Not Required'. This is for people who meet certain educational or professional criteria. If you have a Bachelor's Degree or higher, you are typically eligible. You should check 'Yes' on the form and be prepared to show a copy of your degree certificate."
}

```
--- 

## Future Steps

* Develop the full browser extension frontend using React or vanilla JavaScript.
* Integrate the chrome.tabs.captureVisibleTab API on the frontend to create a seamless screenshot experience.
* Expand the system prompt and RAG knowledge base to cover a wider range of government forms.
