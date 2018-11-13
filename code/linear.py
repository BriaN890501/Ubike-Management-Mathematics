#Import Linear Regression model from scikit-learn.
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import pickle 

def linear_regression_train(data, power):
    #initialize predictors:
    predictors=['x']
    if power>=2:
        predictors.extend(['x_%d'%i for i in range(2,power+1)])
    
    #Fit the model
    linreg = LinearRegression(normalize=True)
    linreg.fit(data[predictors],data['y'])
    y_pred = linreg.predict(data[predictors])

    #Save the model(need to creat save directory first)
    with open('save/linreg_x_%d.pickle'%power, 'wb') as f:
        pickle.dump(linreg, f)

    #Return the result in pre-defined format
    rss = sum((y_pred-data['y'])**2)
    ret = [rss]
    ret.extend([linreg.intercept_])
    ret.extend(linreg.coef_)
    return ret
    
def linear_regression_valid(data, power):
    #initialize predictors:
    predictors=['x']
    if power>=2:
        predictors.extend(['x_%d'%i for i in range(2,power+1)])

    #Read model
    with open('save/linreg_x_%d.pickle'%power, 'rb') as f:
        linreg = pickle.load(f)
   
    #Predict
    y_pred = linreg.predict(data[predictors])


    #Return the result in pre-defined format
    rss = sum((y_pred-data['y'])**2)
    ret = [rss]
    ret.extend([linreg.intercept_])
    ret.extend(linreg.coef_)
    return ret