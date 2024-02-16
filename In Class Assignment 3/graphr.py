import matplotlib.pyplot as plt

def plot_rline(X,y, predicts, whichset):
    viz_train = plt
    viz_train.scatter(X, y, color='red')
    #viz_train.plot(X_train, regressor.predict(X_train), color='blue')
    viz_train.plot(X, predicts, color='blue')
    viz_train.title('Salary VS Experience (' + whichset + ' set)')
    viz_train.xlabel('Year of Experience')
    viz_train.ylabel('Salary')
    viz_train.show()
    filename = 'save' + whichset + '.png'
    viz_train.savefig(filename)


