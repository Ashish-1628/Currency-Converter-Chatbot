# 💱 Currency Converter Chatbot

An AI-powered Currency Converter Chatbot that performs real-time currency conversion using natural language queries. The chatbot is integrated with Telegram and uses Dialogflow for Natural Language Processing (NLP), Flask for backend processing, and FreeCurrencyAPI for fetching live exchange rates.

---

## 📌 Features

* Real-time currency conversion
* Natural language query processing
* Telegram Bot integration
* Dialogflow NLP integration
* Flask-based webhook backend
* Live exchange rates using FreeCurrencyAPI
* Supports multiple currencies worldwide

---

## 🛠️ Technologies Used

* Python
* Flask
* Dialogflow ES
* Telegram Bot API
* FreeCurrencyAPI
* ngrok

---

## 🏗️ System Architecture

Telegram User
↓
Telegram Bot
↓
Dialogflow
↓
Flask Webhook
↓
FreeCurrencyAPI
↓
Dialogflow
↓
Telegram User

---

## 🚀 Example Queries

* Convert 100 USD to INR
* Convert 500 GBP to EUR
* Convert 1000 INR to USD
* Convert 50 EUR to JPY
* Convert 250 CAD to AUD

### Sample Response

💱 100 USD = 8750.45 INR

---

## 📂 Project Structure

currency-converter-chatbot/
│
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── LICENSE
│
├── screenshots/
│   ├── telegram-demo.png
│   ├── dialogflow-intent.png
│   ├── entity-extraction.png
│   └── architecture-diagram.png
│
└── docs/
    └── project_report.pdf


## ⚙️ Installation

### 1. Clone the Repository

git clone https://github.com/Ashish-1628e/currency-converter-chatbot.git
cd currency-converter-chatbot


### 2. Install Dependencies

pip install -r requirements.txt


### 3. Run Flask Application

python app.py


### 4. Start ngrok


ngrok http 5000


### 5. Configure Dialogflow Webhook

Paste the ngrok HTTPS URL into the Dialogflow Fulfillment Webhook settings.

---

## 📸 Screenshots

### Telegram Bot D

<img width="600" height="800" alt="telegram-bot-talks png" src="https://github.com/user-attachments/assets/83538511-ab42-4eea-b787-208a51c87cd9" />

### Conversion Example

<img width="1200" height="1400" alt="multiple-conversions png" src="https://github.com/user-attachments/assets/cbfa14c8-598e-4933-960b-cf47fbdb1890" />


### Dialogflow Intent

<img width="1000" height="1200" alt="dialogflow-intent png" src="https://github.com/user-attachments/assets/cbc268ad-310e-48b5-baf9-adcaeb408bc3" />

### Entity Extraction

<img width="1000" height="1200" alt="entity-extraction png" src="https://github.com/user-attachments/assets/1bc30e10-3d81-4a50-85ed-1a3436e4335f" />

### Flask Webhook

<img width="1000" height="1200" alt="flask-webhook png" src="https://github.com/user-attachments/assets/4be23f11-9608-446a-b327-d69829e191ae" />

### Telegram Integration

<img width="1000" height="1200" alt="telegram-integration png" src="https://github.com/user-attachments/assets/fee901d0-e74f-43c2-a831-cbd3ede0cfdf" />


## 🎯 Learning Outcomes

Through this project, the following concepts were explored:

* Natural Language Processing (NLP)
* Dialogflow Intent Creation
* Entity Extraction
* Webhook Integration
* REST API Consumption
* Telegram Bot Development
* Backend Development using Flask
* Real-Time Data Processing

---

## 🔮 Future Enhancements

* Currency exchange history
* Graphical exchange-rate trends
* Multi-language support
* Voice-based currency conversion
* Deployment on cloud platforms such as Render or Railway
* Support for cryptocurrency conversion

---

## 👨‍💻 Author

Ashish Deswal

MCA Student | Machine Learning & Data Science Enthusiast

---

## 📜 License

This project is licensed under the MIT License.
