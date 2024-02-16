import pandas as pd
import warnings
warnings.filterwarnings("ignore")

def cardatasetsense(cars):
    print("\nHere is information on the dataset with which we are working:")
    print(type(cars))
    pd.set_option('display.max_columns', None)
    print('****  Input data ******')
    print(cars)
    print()
    print('Get a sense as to how balanced the data is:')
    print('Number of US brand recommendations = {}'.format(len(cars[cars['brand'] ==' US.'])))
    print('Number of Japan brand recommendations = {}'.format(len(cars[cars['brand'] ==' Japan.'])))
    print('Number of Eur brand recommendations = {}'.format(len(cars[cars['brand'] ==' Europe.'])))
    print()
    print('Number of data records and columns of data: ' , cars.shape)
    print('Missing values?', cars.isnull().sum())
    print()
    print('**********************************************************************')
    print()

def print_splits(X, y,which) :
    if (which == 1):
        print()
        print('*******************  TRAINING  **************************')
        print()
        print('X_train data:')
        print(X)
        print('y_train columns:')
        print(y.columns.tolist())
        print('y train data:')
        print(y)
        print()
    elif(which == 2):
        print()
        print('*******************  TESTING  **************************')
        print()
        print('X_test data:')
        print(X)
        print('y_test columns:')
        print(y.columns.tolist())
        print('y test data:')
        print(y)
        print()
    else: print('*******ERROR  -- invalid value: ', which)

def print_feature(rf, X_train) :
    print('Features sorted by their score:')
    print(sorted(zip(map(lambda x: round(x,4), rf.feature_importances_), X_train), reverse=True))
    # if super small then insignificant and could drop
    # but we will not...

def display_predicted(A,B) :
   res = pd.concat([A, B.set_index(A.index)], axis=1)
   print(res.to_string())

def recode_brand(cars) :
    brand_mapping = {' US.':1
                    ,' Japan.': 2
                    ,' Europe.': 3
                    }
    cars = cars.assign(brand = cars.brand.map(brand_mapping))
    return cars

def print_prediction(prediction, probabilities) :
    print('*** NEW PREDICTION: **********')
    print()
    print(prediction)
    brand = ''
    for x in range(len(prediction)):
        if prediction[x] ==1 :
            brand +=" US "
        elif prediction[x]  ==2 :
            brand += " Japan "
        else:
            brand += " Europe "
    print('which means that brand is: ', brand)
    print('Probabilities of US and Japan and Europe respectively:')
    print(probabilities)
    print()
          
        
   
