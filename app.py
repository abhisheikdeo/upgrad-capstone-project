from flask import Flask, render_template, request, redirect, url_for
from sklearn.feature_extraction.text import TfidfVectorizer, TfidfTransformer
from scipy import sparse
import pandas as pd
import numpy as np
import pickle
import warnings

warnings.filterwarnings('ignore')

app = Flask(__name__)

df = pd.read_csv("./Model/user_final_ratings.csv")
df.set_index('reviews_username', inplace=True)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/recommend", methods=['POST'])
def recommend():
    user_name = request.form.get('userName')
    try:
        prediction = df.loc[user_name].sort_values(ascending=False)[0:10]
    except Exception as e:
        print(f"Exception : {e}")
        return render_template('index.html', OUTPUT=ValueError)

    return render_template('index.html', OUTPUT=str(prediction))


if __name__ == "__main__":
    app.run(debug=True)
