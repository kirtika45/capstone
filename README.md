# Capstone-Project
<h2>Identification of Vehicle Insurance and Pollution Certificate Validity at Toll Gates</h2>

## Overview
This project focuses on automating the verification of vehicle insurance, pollution certificates and fitness check at toll gates using RFID-based FASTag technology and Electronic Product Code (EPC). The system aims to streamline toll operations and ensure compliance with regulatory requirements for vehicles.

## Objectives
- Automate the verification process for vehicle insurance and pollution certificates.
- Integrate RFID (FASTag) technology for seamless identification of vehicles.
- Reduce manual intervention and improve toll gate efficiency.
- Ensure compliance with traffic and environmental regulations.

## Features
- **RFID Integration:** Utilize FASTag technology for vehicle identification.
- **Database Connectivity:** Access vehicle insurance and pollution certificate details in real-time.
- **Automated Alerts:** Notify authorities about non-compliant vehicles.
- **Scalable Architecture:** Designed to handle high traffic volumes efficiently.

## Technologies Used
- **Programming Languages:** Python, SQL
- **Hardware:** RFID readers and FASTag-enabled vehicles
- **Frameworks and Libraries:**
  - Flask / Django (for web integration)
  - Pandas
  - NumPy
- **Databases:** MySQL / PostgreSQL

## Architecture
1. **Data Collection:**
   - Vehicle details fetched using FASTag EPC.
   - Integration with insurance and pollution certificate databases.
2. **Verification Process:**
   - Real-time comparison of vehicle details with regulatory compliance data.
3. **Alerts and Notifications:**
   - Automatic flagging of non-compliant vehicles.
4. **Dashboard:**
   - Centralized platform for monitoring vehicle compliance and toll operations.

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/kirtika45/capstone.git
   ```
2. Navigate to the project directory:
   ```bash
   cd capstone
   ```
3. Install dependencies:
   ```bash
   pip install flask
   pip install twilio
   ```
4. Set up the database by running the migration scripts:
   ```bash
   python manage.py migrate
   ```

## Usage
1. Start the server:
   ```bash
   python app.py
   ```
2. Access the web dashboard at `http://localhost:8000`.
3. Place RFID-enabled vehicles near the reader to verify compliance.

## Results
- Automated verification system capable of processing vehicles in real-time.
- Significant reduction in manual intervention at toll gates.
- Enhanced compliance with environmental and insurance regulations.

## Future Work
- Integrate with cloud services for large-scale deployment.
- Develop a mobile application for real-time monitoring by authorities.

## Contributors
- **Your Name**: [Kirtika Sharma](https://github.com/kirtika45)
- **Teammate Name**: [Sai Teja](https://github.com/Saikukatla)

## License
This project is licensed under the [MIT License](LICENSE).

---
Feel free to contribute to the project or raise issues for further improvement!

