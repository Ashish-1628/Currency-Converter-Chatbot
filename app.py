from flask import Flask, request, jsonify
import freecurrencyapi

app = Flask(__name__)

API_KEY = "USE-NGROK-API-KEY"

client = freecurrencyapi.Client(API_KEY)
@app.route('/', methods=['GET'])
def home():
    return "Currency Bot Webhook Running"

@app.route('/', methods=['POST'])
def index():

    data = request.get_json()

    params = data.get('queryResult', {}).get('parameters', {})

    source_currency = params['unit-currency']['currency']
    amount = float(params['unit-currency']['amount'])
    target_currency = params['currency-name']

    try:

        rates = client.latest(
            base_currency=source_currency,
            currencies=[target_currency]
        )

        rate = rates['data'][target_currency]

        converted_amount = amount * rate

        response = {
            "fulfillmentText":
                f"{amount} {source_currency} = {converted_amount:.2f} {target_currency}"
        }
        print("Source:", source_currency)
        print("Amount:", amount)
        print("Target:", target_currency)

        return jsonify(response)

    except Exception as e:

        return jsonify({
            "fulfillmentText": f"Error: {str(e)}"
        })

if __name__ == "__main__":
    app.run(debug=True)