# email-to-excel-automation
Step 1: Create venv:
python -m venv venv
Step 2: Activate venv:
.\venv\Scripts\activate
You'll see (venv) in your terminal.
Step 3: Install dependencies:
pip install anthropic python-dotenv openpyxl pytest
pip freeze > requirements.txt
Step 4: Create .env file:
ANTHROPIC_API_KEY=actual-key-here

ai-automation-portfolio/
├── venv/
├── .env
├── .gitignore
├── README.md
├── requirements.txt
├── data/
│   └── sample_invoice_email.txt    ← fake invoice email
├── invoice_extractor.py            ← Claude extracts data
├── excel_writer.py                 ← writes to Excel
├── main.py                         ← runs the full workflow
└── tests/
    ├── test_invoice_extractor.py
    └── test_excel_writer.py