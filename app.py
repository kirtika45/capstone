from flask import Flask, request, render_template
import csv
from datetime import datetime
from twilio.rest import Client

app = Flask(__name__, template_folder=r'C:\Users\user\Desktop\kishi\capstone\templates')

def load_csv(file_path):
    vehicles = []
    with open(file_path, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            vehicles.append(row)
    return vehicles

def validate_date(date_str):
    try:
        return datetime.strptime(date_str, "%d %m %Y")
    except ValueError:
        return None

# Twilio API Configuration
import os
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID")
TWILIO_AUTH_TOKEN = "your_twilio_auth_token"
TWILIO_PHONE_NUMBER = "your_twilio_phone_number"

# Twilio send message function
def send_alert_message(contact_number, message):
    client = Client(TWILIO_ACCOUNT_SID, TWILIO_AUTH_TOKEN)
    try:
        response = client.messages.create(
            body=message,
            from_=TWILIO_PHONE_NUMBER,
            to=contact_number
        )
        print(f"Message sent: {response.sid}")
    except Exception as e:
        print(f"Error sending message: {e}")

@app.route("/", methods=["GET", "POST"])
def validate_vehicle():
    vehicle = None
    insurance_warning = ""
    puc_warning = ""
    fitness_warning = ""

    if request.method == "POST":
        reg_no = request.form["regNo"].strip()
        vehicles = load_csv("data/vehicles.csv")  # Replace with the path to your CSV file
        vehicle = next((v for v in vehicles if v["regNo"] == reg_no), None)

        if vehicle:
            today = datetime.today()
            contact_number = vehicle.get("contact", None)  # Ensure CSV includes a contact column
            alert_messages = []

            # Validate insurance
            insurance_date = validate_date(vehicle.get("insurance_upto", ""))
            if insurance_date and insurance_date < today:
                insurance_warning = f"⚠️ Insurance expired on {insurance_date.strftime('%d/%m/%Y')}. Please renew."
                alert_messages.append(insurance_warning)
            elif insurance_date:
                insurance_warning = f"✔️ Insurance is valid till {insurance_date.strftime('%d/%m/%Y')}"
            else:
                insurance_warning = "⚠️ Invalid Insurance date."

            # Validate PUCC
            puc_date = validate_date(vehicle.get("pucc_upto", ""))
            if puc_date and puc_date < today:
                puc_warning = f"⚠️ PUC expired on {puc_date.strftime('%d/%m/%Y')}. Please renew."
                alert_messages.append(puc_warning)
            elif puc_date:
                puc_warning = f"✔️ PUCC is valid till {puc_date.strftime('%d/%m/%Y')}"
            else:
                puc_warning = "⚠️ Invalid PUC date."

            # Validate fitness
            fitness_date = validate_date(vehicle.get("fitness_upto", ""))
            if fitness_date and fitness_date < today:
                fitness_warning = f"⚠️ Fitness expired on {fitness_date.strftime('%d/%m/%Y')}. Please renew."
                alert_messages.append(fitness_warning)
            elif fitness_date:
                fitness_warning = f"✔️ Fitness is valid till {fitness_date.strftime('%d/%m/%Y')}"
            else:
                fitness_warning = "⚠️ Invalid Fitness date."

            # Send SMS if warnings exist
            if contact_number and alert_messages:
                full_message = f"Vehicle {reg_no} Alerts:\n" + "\n".join(alert_messages)
                send_alert_message(contact_number, full_message)

    return render_template(
        "index1.html",
        vehicle=vehicle,
        insurance_warning=insurance_warning,
        puc_warning=puc_warning,
        fitness_warning=fitness_warning
    )

if __name__ == "__main__":
    app.run(debug=True)
