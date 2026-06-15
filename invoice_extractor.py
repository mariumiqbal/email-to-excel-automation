import json
import re
from anthropic import Anthropic
from dotenv import load_dotenv
import os

load_dotenv()
client = Anthropic(api_key=os.getenv("ANTHROPIC_API_KEY"))

def read_email(path: str) -> str:
    with open(path, "r") as f:
        return f.read()

def extract_invoice_data(email_content: str) -> dict:
    if not email_content:
        raise ValueError("Email content cannot be empty")
    
    prompt = f"""Extract invoice data from this email and respond ONLY with valid JSON.
No explanation, no markdown, just raw JSON with these fields:
- vendor (string)
- invoice_number (string)
- invoice_date (string)
- due_date (string)
- line_items (list of objects with description, quantity, price)
- subtotal (float)
- tax (float)
- total (float)

Email:
{email_content}"""

    message = client.messages.create(
        model="claude-haiku-4-5-20251001",
        max_tokens=1024,
        messages=[{"role": "user", "content": prompt}]
    )
    
    response = message.content[0].text
    clean = re.sub(r'```json|```', '', response).strip()
    return json.loads(clean)

if __name__ == "__main__":
    email = read_email("data/sample_invoice_email.txt")
    data = extract_invoice_data(email)
    print(json.dumps(data, indent=4))