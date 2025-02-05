from fastapi import FastAPI, Form
from fastapi.responses import HTMLResponse
from dotenv import load_dotenv
import google.generativeai as genai  # Using your working alias
from google.protobuf.json_format import MessageToDict
import os

# Load environment variables from your .env file
load_dotenv("/Users/vedangbhardwaj/Desktop/work_mode/insurance_cancellation_project/insurance_cancellations/.env", override=True)

# Configure the API key
genai.configure(api_key=os.getenv("PALM_API_KEY"))

# Instantiate your working Gemini model
MODEL_NAME = "gemini-1.5-flash"
model = genai.GenerativeModel(MODEL_NAME)

app = FastAPI()

# Simple HTML form for policy input
html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Coverage Gap Analyzer</title>
    <style>
        body { font-family: Arial, sans-serif; margin: 40px; text-align: center; }
        textarea { width: 80%; height: 150px; margin-top: 10px; }
        button { padding: 10px 20px; margin-top: 10px; }
        .result { margin-top: 20px; padding: 10px; border: 1px solid #ddd; background: #f9f9f9; display: inline-block; text-align: left; width: 80%; }
    </style>
</head>
<body>
    <h2>Coverage Gap Analyzer (Gemini)</h2>
    <form action="/analyze" method="post">
        <textarea name="policy_text" placeholder="Paste your policy text here..."></textarea><br>
        <button type="submit">Analyze Policy</button>
    </form>
    <div class="result">
        <h3>Analysis Result:</h3>
        <p>{{result}}</p>
    </div>
</body>
</html>
"""

@app.get("/", response_class=HTMLResponse)
def home():
    # Show the form with a placeholder message
    return html_form.replace("{{result}}", "Submit a policy to analyze.")

@app.post("/analyze", response_class=HTMLResponse)
def analyze_policy(policy_text: str = Form(...)):
    """
    Constructs a detailed prompt instructing the model to analyze a motor vehicle insurance policy.
    The prompt requests an analysis of coverage gaps in Motor Truck Cargo (MTC), Auto Liability (AL),
    and Auto Physical Damage (APD) while considering FMCSA data.
    """
    # Ensure the policy text is a string
    policy_text_str = str(policy_text)
    
    # Build the detailed prompt
    prompt = (
        "You are an expert insurance analyst. Analyze the following motor vehicle insurance policy and "
        "highlight any coverage gaps, focusing on Motor Truck Cargo (MTC), Auto Liability (AL), and Auto Physical Damage (APD). "
        "Also, incorporate any relevant FMCSA data insights regarding trucking operations.\n\n"
        f"{policy_text_str}"
    )

    # Generate a response using the Gemini API
    response = model.generate_content(prompt)
    print(response)
    
    # Extract the generated text from the response
    analysis_result = "No response from model."
    # Directly extract the text from the first candidate's first content part
    try:
        analysis_result = response.candidates[0].content.parts[0].text
    except Exception as e:
        analysis_result = f"Error extracting result: {e}"

    # Replace the placeholder in the HTML with the analysis result
    return html_form.replace("{{result}}", analysis_result)
