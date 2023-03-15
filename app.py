from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get')
def get_bot_response():
    user_text = request.args.get('msg')

    if 'who are you' in user_text.lower():
        return 'I am Smart Doctor. How Can I suggest You?'
    elif 'help' in user_text.lower():
        return 'Please say your problem or disease name'
    elif 'hi' in user_text.lower():
        return 'Hellow, I am Smart Doctor.'
    elif 'sick' in user_text.lower():
        return 'Say about your feelings.'
    elif 'fever' in user_text.lower():
        return "For fever need to eat Napa. Drink plenty of fluids, particularly water. Avoid taking cold baths or showers."
    elif 'headache' in user_text.lower():
        return 'For headache need to eat Tufnil 200mg. Drink plenty of water. get plenty of rest if you have a cold or the flu, try to relax because stress can make headaches worse'
    elif 'unhealthy' in user_text.lower():
        return 'For unhealthy you need balanced diet and take proper exercise.'
    else:
        return 'I did not understand what you said. Please say specific disease name.'

if __name__ == '__main__':
    app.run(port=7000)
