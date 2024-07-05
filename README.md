# Medication Literacy App

The Medication Literacy App is designed to help users learn about different medications, 
including their brand and generic names, uses, possible side effects, and drug interactions. 
This application leverages the FDA API to fetch medication data and uses ZeroMQ for inter-process communication.

## Features
- Fetch brand and generic names of medications
- Get information on the uses of medications
- Learn about possible side effects
- Understand potential drug interactions

## Technologies Used
- Python: The main programming language
- ZeroMQ: A high-performance asynchronous messaging library used for communication between processes
- requests: A simple HTTP library for Python to make API requests
- FDA API: To fetch medication data

## How to Run
1. **Clone the repository**:
   ```sh
    git clone https://github.com/camillegonzales/medication-literacy-app.git
    cd medication-literacy-app
    ```

2. **Install dependencies**:
    ```sh
    pip install pyzmq requests
    ```
    
3. **Clone and run the drug interaction microservice**:
   The main program uses a microservice made by a teammate to fetch medication interactions.
    ```sh
    git clone https://github.com/tranlex/drug-interaction-microservice.git
    cd drug-interaction-microservice
    pip install zmq requests beautifulsoup4
    python server.py
    ```

5. **Run the servers**:
    Open separate terminal windows for each server script and run them:
    ```sh
    python fetch_names.py
    python fetch_uses.py
    python fetch_side_effects.py
    python fetch_interactions.py
    ```

6. **Run the main application**:
    ```sh
    python main.py
    ```
    
## Usage
- Follow the prompts in the command-line interface to enter a medication name and select the type of information you want to learn.
- The app will communicate with the respective server to fetch and display the requested information.
