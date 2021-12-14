from flask import Flask, request
import pickle

print('Start')
app = Flask(__name__)

print('Pickle Load')
#Load pickle file
clf = pickle.load(open('Bank_note.pkl', 'rb'))

@app.route('/')
def welcome():
    print('Welcome')
    return 'Welcome All'

@app.route('/predict/')
def predict_note():
    print('Predict')
    skewness = request.args.get('skewness')
    variance = request.args.get('variance')
    kurtosis = request.args.get('kurtosis')
    entrophy = request.args.get('entrophy')
    y_pred = clf.predict([[skewness, variance, kurtosis, entrophy]])
    return 'The predicted value is : ' + str(y_pred)

if __name__ == '__main__':
    print('Main')
    app.run()

