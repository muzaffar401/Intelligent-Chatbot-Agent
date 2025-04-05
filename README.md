
# 🤖 Multi-Agent Chatbot by Muzaffar Ahmed

## Overview
This project is a multi-agent chatbot created using **Streamlit**, **Gemini API** (via `AsyncOpenAI`), and **Python**. The chatbot features different agents, each designed to handle specific tasks, such as greeting, motivation, compliments, jokes, life advice, random facts, Python code generation, and wisdom quotes.

Users can interact with different agents by selecting them from a set of predefined buttons. Once an agent is selected, users can input their queries, and the chatbot will respond accordingly based on the agent's behavior.

### Project Features:
- **Multiple agents**: Choose from a list of agents, each with specific behavior and tasks.
- **Asynchronous calls**: Uses `AsyncOpenAI` to interact with the Gemini API asynchronously.
- **Streamlit UI**: Interactive user interface for easy interaction.
- **Customizable system prompts**: Each agent has its own system prompt that defines how it should respond.

---

## Technologies Used
- **Streamlit**: Used to build the web interface.
- **Gemini API (via `AsyncOpenAI`)**: Used for handling AI responses asynchronously.
- **Python**: The main programming language used for the backend logic.
- **dotenv**: Loads environment variables like API keys securely.
- **UV**: Used for managing project dependencies.

---

## Setup Instructions

### Prerequisites:
1. **Python 3.x** (Ensure Python is installed on your system).
2. **Gemini API Key**: You must have an API key for the Gemini API, which you can obtain by following the setup instructions provided by Google.

### Installing Dependencies

1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/muzaffar401/Intelligent-Chatbot-Agent.git
   cd Intelligent-Chatbot-Agent
   ```

2. Install the required dependencies:
   - Ensure you have `uv` installed for managing Python dependencies. If `uv` is not installed, you can install it via:
     ```bash
     pip install uv
     ```
   - Add the required dependencies using `uv`:
     ```bash
     uv add streamlit openai python-dotenv
     ```

### Environment Setup

1. **Create a `.env` file** in the root of your project directory and add your Gemini API key:
   ```plaintext
   GEMINI_API_KEY=your_api_key_here
   ```

2. The **Gemini API key** is required to interact with the API, and it is stored in the `.env` file for security.

---

## Running the Project

To run the project locally:

1. Navigate to the project directory:
   ```bash
   cd Intelligent-Chatbot-Agent
   ```

2. Start the Streamlit app:
   ```bash
   streamlit run Advance_Agent.py
   ```

3. Once the app is running, open your web browser and go to `http://localhost:8501` to access the chatbot.

---

## Usage

1. **Select an Agent**: You can choose an agent from the available options (e.g., Greeting Agent, Motivation Agent, etc.). Each agent has its own behavior.
   
2. **Interact with the Agent**: Once you select an agent, type your query or message in the input box. The selected agent will respond based on its pre-defined behavior.

3. **Available Agents**:
   - **Greeting Agent**: Responds with greetings and farewells.
   - **Motivation Agent**: Gives motivational quotes when you're feeling down.
   - **Compliment Agent**: Gives you a unique compliment when requested.
   - **Joke Agent**: Tells a fun and short joke when asked.
   - **Life Advice Agent**: Offers a meaningful life lesson when asked for advice.
   - **Random Facts Agent**: Shares interesting random facts when asked.
   - **Wisdom Quotes Agent**: Shares thoughtful and inspiring wisdom quotes.
   - **Python Code Generator Agent**: Generates Python code for various tasks (e.g., functions, calculators).

---

## Code Structure

### 1. `Advance_Agent.py`
This is the main file that runs the Streamlit app. It handles the UI and interacts with the Gemini API to provide responses from the selected agent.

### 2. `.env`
Contains sensitive information like your **Gemini API key**. This file should be added to `.gitignore` to ensure that sensitive information is not pushed to version control systems.

### 3. `requirements.txt`
This file lists all the dependencies used in the project. When deploying to a server or another environment, this file is used to install the necessary packages:
```txt
streamlit
openai
python-dotenv
```

---

## Project Architecture

1. **Streamlit UI**: The frontend is built using Streamlit to provide a responsive and interactive interface for the user.
   
2. **Backend Logic**: The backend uses the Gemini API to generate responses based on the user’s input. Each agent has a specific system prompt that customizes its behavior.

3. **Asynchronous Communication**: The application makes asynchronous calls to the Gemini API, ensuring the UI remains responsive while waiting for responses.

4. **Custom CSS**: Injects custom CSS styles to enhance the look and feel of the agent selection buttons and other UI components.

---

## Contribution

1. **Fork** the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. **Commit** your changes (`git commit -m 'Added new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

---

## License

This project is licensed under the MIT License.

---

## Acknowledgements

- **Muzaffar Ahmed**: The creator of this project and the various agent behaviors.
- **Streamlit**: For providing an excellent framework for building web apps.
- **Gemini API**: For the underlying AI model that powers the chatbot agents.

---

## Contact

If you have any questions, feel free to reach out at [muzaffarahmed@example.com](mailto:ma9400667@gmail.com).
