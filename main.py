from invoice_extractor import read_email, extract_invoice_data
from excel_writer import write_invoice_to_excel

def main():
    # Step 1 - read email
    email = read_email("data/sample_invoice_email.txt")
    print("✓ Email read")
    
    # Step 2 - extract data with Claude
    invoice_data = extract_invoice_data(email)
    print("✓ Data extracted")
    print(invoice_data)
    
    # Step 3 - write to Excel
    output_path = write_invoice_to_excel(invoice_data)
    print(f"✓ Excel saved to {output_path}")

if __name__ == "__main__":
    main()