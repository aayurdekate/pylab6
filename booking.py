import re
from datetime import datetime

def validate_travel_booking(name, passport_number, phone, email, departure_date, payment_method):

    if not re.fullmatch(r"[A-Za-z\s]+", name):
        return "Invalid name. Name should only contain alphabetic characters and spaces."
    
    if not re.fullmatch(r"[A-Za-z0-9]{9}", passport_number):
        return "Invalid passport number. It should be alphanumeric and exactly 9 characters long."
    
    if not re.fullmatch(r"\d{10}", phone):
        return "Invalid phone number. It should be a valid 10-digit number."
    
    if not re.fullmatch(r"[^@]+@[^@]+\.[^@]+", email):
        return "Invalid email address format."
    
    try:
        datetime.strptime(departure_date, "%d/%m/%Y")
    except ValueError:
        return "Invalid departure date. It should be in the format dd/mm/yyyy."
    
    if payment_method not in ['credit', 'debit', 'netbanking']:
        return "Invalid payment method. Accepted methods are 'credit', 'debit', or 'netbanking'."
    
    return "All validations passed."

print(validate_travel_booking("Ayur Dekate", "A12345678", "1234567890", "ayur@example.com", "12/09/2024", "credit"))
