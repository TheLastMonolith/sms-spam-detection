from flask import Flask, render_template, request, jsonify
from model import spam_predict


app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    '''
    For rendering results on HTML GUI
    '''
    sms = [str(x) for x in request.form.values()]
    output = spam_predict(sms)

    return render_template('index.html', prediction_text='It\'s a {}'.format(output))

@app.route('/predict_api', methods=['POST'])
def predict_api():
    '''
    For direct API calls thru request
    '''
    data = request.get_json(force=True)
    prediction = spam_predict(list(data.values()))

    # output = prediction[0]
    return jsonify(prediction)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080')