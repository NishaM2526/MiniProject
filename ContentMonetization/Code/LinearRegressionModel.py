
import os
from xml.parsers.expat import model

from joblib import Parallel, delayed
import joblib
import Preprocess as pp
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.model_selection import train_test_split

base_dir = os.path.dirname(os.path.join(os.path.dirname(__file__), os.pardir, os.pardir))
file_path = os.path.join(base_dir, "Data", "linear_regression_model.pkl")

def model_training():
    df = pp.data_preprocessing()
    X = df.drop(['ad_revenue_usd'], axis=1)
    y = df['ad_revenue_usd']

    x_train, x_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
    model = LinearRegression()
    # train the model
    model.fit(x_train, y_train)
    train_prediction = model.predict(x_train)
    test_prediction = model.predict(x_test)

    print(f"Linear Regression - Train MSE :: {mean_squared_error(y_train, train_prediction)}")
    print(f"Linear Regression - Test MSE :: {mean_squared_error(y_test, test_prediction)}")

    print(f"Linear Regression - Train R2 :: {r2_score(y_train, train_prediction)}")
    print(f"Linear Regression - Test R2 :: {r2_score(y_test, test_prediction)}")
    joblib.dump(model,file_path)

model_training()