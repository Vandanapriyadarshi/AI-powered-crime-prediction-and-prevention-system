# AI-Powered Crime Prediction and Prevention System

This project is an AI-powered crime prediction and prevention system that analyzes live crime reports, social media alerts, and CCTV footage to predict potential crimes and alert law enforcement. The system leverages various technologies, including Apache Kafka, PySpark, and a React-based dashboard.

## Table of Contents

- [Features](#features)
- [Technologies](#technologies)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Features

- Real-time crime report analysis and prediction
- WebSocket notifications for live crime alerts
- Integration with PostgreSQL for data storage
- User-friendly dashboard for viewing crime alerts

## Technologies

- **Backend**:
  - Python
  - PySpark
  - Kafka
  - PostgreSQL
  - WebSockets

- **Frontend**:
  - React
  - Tailwind CSS

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Vandanapriyadarshi/AI-powered-crime-prediction-and-prevention-system.git
   cd AI-powered-crime-prediction-and-prevention-system

  '''
 ## Set up a Python virtual environment (optional but recommended):
- python -m venv .venv
- .venv\Scripts\activate  # On Windows
- source .venv/bin/activate  # On macOS/Linux

## Install required Python packages:
- pip install -r requirements.txt
  
## Navigate to the crime-dashboard directory and install npm packages:
- cd crime-dashboard
- npm start

# Usage
## Start the WebSocket Server:
- python alert_server.py
  
## Run the Crime Streaming System: Open a new terminal and run:
- python crime_streaming.py

## Start the React Dashboard: In another terminal, navigate to the crime-dashboard directory and run: 
- npm start

 # Project Structure
 
AI-powered-crime-prediction-and-prevention-system/
├── crime-dashboard/           # React frontend
├── alert_server.py            # WebSocket server for alerts
├── crime_streaming.py         # Main streaming logic with PySpark
├── stream_reader.py           # Handles reading from Kafka
├── stream_writer.py           # Handles writing to console, DB, and alerts
├── transformations.py         # Data transformations and ML predictions
├── testalert.py               # Test script for sending alerts
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation

## Contributing
Contributions are welcome! Please create a pull request or submit an issue for any improvements or bugs.


## License

### Steps to Create the README

1. Open your code editor.
2. Create a new file named `README.md` in the root directory of your project.
3. Copy and paste the above content into the file.
4. Save the file.

This README provides a clear overview of your project, its features, technologies used, installation instructions, and more. You can modify any section as per your project's specifics!


