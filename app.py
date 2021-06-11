from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
model = pickle.load(open('finalized_model.sav','rb'))


@app.route('/')
def home():
    return render_template('body.html')

@app.route('/sheldon_says',methods=['GET'])
def sheldon_says(): 
    output = model.make_sentence()
    return render_template('body.html',prediction_text='Sheldon tells you that:  {}'.format(output))

if __name__ == "__main__":
    app.run(debug=True)
    