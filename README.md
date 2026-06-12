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

```bash
pip install -r requirements.txt
```

### 3. Run Flask Application

```bash
python app.py
```

### 4. Start ngrok

```bash
ngrok http 5000
```

### 5. Configure Dialogflow Webhook

Paste the ngrok HTTPS URL into the Dialogflow Fulfillment Webhook settings.

---

## 📸 Screenshots

### Telegram Bot D<img width="1247" height="968" alt="telegram-bot-talks png" src="https://github.com/user-attachments/assets/83538511-ab42-4eea-b787-208a51c87cd9" />
emo


Add screenshot here

### Dialogflow Intent

Add screenshot here

### Entity Extraction

Add screenshot here

### System Architecture

Add screenshot here

---

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
