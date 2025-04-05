# Import necessary libraries
import os  # Used to interact with the operating system, such as loading environment variables
import asyncio  # Used to work with asynchronous code (non-blocking)
import streamlit as st  # Streamlit library to build the web app
from openai import AsyncOpenAI  # Gemini API client (similar to OpenAI API client) for async requests

# Load environment variables from Streamlit secrets
gemini_api_key = st.secrets["GEMINI_API_KEY"]  # Retrieve the GEMINI_API_KEY from Streamlit secrets

# Initialize the Gemini-compatible client (using AsyncOpenAI for asynchronous calls)
client = AsyncOpenAI(
    api_key=gemini_api_key,  # Pass the Gemini API key to the client
    base_url="https://generativelanguage.googleapis.com/v1beta/openai",  # Set the Gemini API base URL
)

# Define the list of agents available in the app with associated emojis
AGENTS = {
    "Greeting Agent": "👋",
    "Motivation Agent": "💪",
    "Compliment Agent": "😊",
    "Joke Agent": "😂",
    "Life Advice Agent": "🧠",
    "Random Facts Agent": "🤓",
    "Python Code Generator Agent": "🐍",
    "Wisdom Quotes Agent": "📜",
}

# Define system prompts for each agent to provide them with a specific behavior
def get_system_prompt(agent_mode: str) -> str:
    prompts = {
        "Greeting Agent": """
        You are the Greeting Agent created by Muzaffar Ahmed.
        When someone says 'hi', 'hello', or any greeting, respond with: "Assalamu Alaikum from Muzaffar Ahmed 👋".
        When someone says 'bye', 'goodbye', or any farewell, respond with: "Allah Hafiz from Muzaffar Ahmed 👋".
        For all other inputs, respond: "Muzaffar is here just for greetings. I can't answer anything else, sorry 😅."
        """,
        "Motivation Agent": """
        You are the Motivation Agent created by Muzaffar Ahmed.
        When someone expresses sadness, failure, or demotivation, respond with a powerful, short motivational quote.
        For any other input, say: "This agent only delivers motivation when needed."
        """,
        "Compliment Agent": """
        You are the Compliment Agent created by Muzaffar Ahmed.
        When someone asks for a compliment (e.g., "compliment me", "say something nice"), respond with a unique, kind compliment.
        Otherwise, say: "I only give compliments when asked nicely 😄."
        """,
        "Joke Agent": """
        You are the Joke Agent created by Muzaffar Ahmed.
        When someone asks for a joke (e.g., "Tell me a joke", "Make me laugh"), respond with a fun and short joke.
        Otherwise, say: "I only tell jokes when asked."
        """,
        "Life Advice Agent": """
        You are the Life Advice Agent created by Muzaffar Ahmed.
        When someone asks for advice (e.g., "What should I do in life?", "I need advice"), give a short but meaningful life lesson.
        For anything else, respond: "I can only give life advice when asked."
        """,
        "Random Facts Agent": """
        You are the Random Facts Agent created by Muzaffar Ahmed.
        When someone asks for a random fact (e.g., "Give me a random fact", "Tell me something interesting"), share a fun, educational, and surprising fact.
        For anything else, say: "I only share random facts when asked."
        """,
        "Wisdom Quotes Agent": """
        You are the Wisdom Quotes Agent created by Muzaffar Ahmed.
        When someone asks for a wisdom quote (e.g., "Give me a quote", "Say something wise"), share a thoughtful and inspiring quote.
        For anything else, say: "I only share wisdom when asked."
        """,
        "Python Code Generator Agent": """
        You are a Python Code Generator Agent created by Muzaffar Ahmed.
        Your job is to generate clean, readable, and efficient Python code.

        ✅ Guidelines:
        - Only respond with Python code (no extra explanations unless explicitly asked).
        - Use comments to explain key parts of the code.
        - For basic requests, keep the code short and beginner-friendly.
        - For advanced tasks, break down the problem and write modular code.
        - Avoid unnecessary complexity.

        🔒 Never execute dangerous commands or suggest anything harmful.

        💡 Example prompts: 
        - "Write a Python function to sort a list."
        - "Generate a simple calculator in Python."
        - "Give me Python code to scrape a website."

        If someone asks for non-code topics, respond:
        "I'm here only to generate Python code. Please ask me something Pythonic 🐍."
        """
    }
    # Return the prompt based on the selected agent mode, or a default message if no match
    return prompts.get(agent_mode, "You are a silent agent.")

# Async function to get a response from the Gemini API based on user input and selected agent
async def get_gemini_response(user_input: str, agent_mode: str) -> str:
    try:
        system_prompt = get_system_prompt(agent_mode)  # Get the system prompt for the agent
        # Make an asynchronous API call to Gemini with system prompt and user input
        response = await client.chat.completions.create(
            model="gemini-2.0-flash",  # Specify the model to use
            messages=[  # Define the conversation message history
                {"role": "system", "content": system_prompt},  # System message with the agent's behavior
                {"role": "user", "content": user_input},  # User's input message
            ],
        )
        # Return the response from Gemini
        return response.choices[0].message.content
    except Exception as e:
        # Handle any exceptions and return the error message
        return f"Error: {str(e)}"

# Streamlit UI setup
st.set_page_config(page_title="🤖 Multi-Agent by Muzaffar Ahmed", layout="centered")  # Set the title and layout of the page
st.title("🤖 Multi-Agent Chatbot by Muzaffar Ahmed")  # Set the main title of the app
st.markdown("### Choose an Agent:")  # Add a subtitle asking to choose an agent

# Inject custom CSS to style the buttons for agent selection
st.markdown("""
    <style>
    div.stButton > button {
        background-color: #0d47a1;  /* Dark blue */
        border: none;
        color: white;
        padding: 14px 20px;
        font-size: 16px;
        font-weight: bold;
        border-radius: 12px;
        margin: 10px;
        width: 100%;
        height: 80px;
        transition: all 0.3s ease;
        box-shadow: 2px 2px 8px rgba(0,0,0,0.15);
    }

    div.stButton > button:hover {
        transform: scale(1.05);
        box-shadow: 0 0 12px #42a5f5;  /* Blue glow */
        background-color: #1565c0;
        color: #ffffff;
        text-decoration: none;
        cursor: pointer;
    }

            
    div.stButton > button:active {
        transform: scale(0.95);
        box-shadow: inset 2px 2px 5px rgba(0,0,0,0.2);
        background-color: #0b3d91;
    }
    </style>
""", unsafe_allow_html=True)  # Allow HTML in Streamlit to inject custom styles

# Display the agent selection buttons
selected_agent = st.session_state.get("selected_agent", None)  # Retrieve the currently selected agent from session state
cols = st.columns(4)  # Create a grid with 4 columns for buttons

# Loop through the agents and display buttons for each agent
for i, (agent, emoji) in enumerate(AGENTS.items()):
    with cols[i % 4]:  # Place the button in a grid column
        # When an agent button is clicked, set the selected agent in session state
        if st.button(f"{emoji} {agent}", key=agent):
            st.session_state["selected_agent"] = agent
            selected_agent = agent

# If an agent is selected, display the agent name and input field
if selected_agent:
    st.markdown(f"### 🧠 Talking to: **{selected_agent}**")  # Display the selected agent's name
    user_input = st.text_input("💬 Your message:")  # Input field for the user to enter their message
    if user_input:  # If the user has entered a message
        with st.spinner("Thinking..."):  # Show a spinner while waiting for the response
            # Get the Gemini response asynchronously and display it
            response = asyncio.run(get_gemini_response(user_input, selected_agent))
            st.success("Response:")  # Show success message
            st.write(response)  # Display the response from Gemini
else:
    st.info("👆 Select an agent to start chatting.")  # Display message to select an agent if none is selected
