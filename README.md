# Coverage Gap Analyzer

Coverage Gap Analyzer is a minimal FastAPI application that leverages Google's Gemini API (via the `google-generativeai` package) to analyze motor vehicle insurance policies. The application is designed to identify potential coverage gaps in key areas such as:

- **Motor Truck Cargo (MTC)**
- **Auto Liability (AL)**
- **Auto Physical Damage (APD)**

Additionally, the analyzer considers relevant FMCSA data insights, making it a valuable tool for insurance analysts, brokers, and carriers to quickly assess and improve their insurance coverage.

## Features

- **Simple Web Interface:** A basic HTML form for users to paste their policy text.
- **Generative AI Analysis:** Uses a Gemini API model (`gemini-1.5-flash`) to generate a detailed analysis.
- **Robust Response Extraction:** Extracts the analysis text from the API response and displays it on the web page.
- **Easy Deployment:** Built using FastAPI, making it lightweight and simple to deploy.

## Prerequisites

- **Python 3.9+**
- **Conda or pip** for managing dependencies
- A valid **Google Generative AI API key** (stored in a `.env` file)

## Installation

1. **Clone the Repository**

   ```bash
   git clone https://github.com/yourusername/coverage-gap-analyzer.git
   cd coverage-gap-analyzer

2. Set Up the Environment
Option A: Using Conda (Recommended)
Create and activate a new conda environment:

```
conda create -n coverage_analyzer python=3.9
conda activate coverage_analyzer
```
Then, install dependencies using the provided requirements.txt
```
pip install -r requirements.txt
```

3. Configure the API Key
Create a .env file in the project root with the following content:
```
PALM_API_KEY=your_google_api_key_here
```

## Running the application 
Start the FastAPI Server
```
uvicorn main:app --reload
```

Open your browser and navigate to:
```
http://127.0.0.1:8000
```

Analyze a Policy

Paste your motor vehicle insurance policy text (including details on MTC, AL, and APD) into the provided textarea.
Click "Analyze Policy".
The application will generate an analysis report and display it on the page.

## Project Structure
```
coverage-gap-analyzer/
├── main.py              # FastAPI application using the Gemini API
├── requirements.txt     # pip dependencies (exported from your conda environment)
├── .env                 # Environment file containing the API key (not committed)
├── README.md            # This file
└── environment.yml      # (Optional) Conda environment file for complete setup
```

