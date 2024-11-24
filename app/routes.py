from flask import Blueprint, jsonify
from app.services.email_service import send_email_gmail
from app.services.qr_service import generate_qr_code
from app.services.pdf_service import generate_pdf

main_bp = Blueprint('main', __name__)

names = ["Mohamed Aashir", "Atheeb Hussain"]
colleges = ["Schedrix", "Schedrix"]
emails = ["tmohamedaashir@gmail.com", "atheebvalued@gmail.com"]

@main_bp.route('/send_emails', methods=['POST'])
def send_emails_for_od():
    for i in range(len(names)):
        name = names[i]
        college = colleges[i]
        email = emails[i]

        qr_data = f"Email: {email}, Category: {college}"
        qr_code_path = f"./qr_code_{name}.png"
        pdf_path = f"./output_{name}.pdf"

        generate_qr_code(qr_data, qr_code_path)
        generate_pdf(name, qr_code_path, pdf_path)

        send_email_gmail(name, email, qr_code_path, pdf_path)

    return jsonify({"message": "Emails sent successfully"}), 200
