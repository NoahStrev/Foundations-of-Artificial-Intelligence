import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# ************  Step 1.  Load the dataset  ***************************
df = pd.read_csv('ADPT.csv')
#df = pd.read_csv('TSLA.csv')
#df = pd.read_csv('NVDA.csv')
#df = pd.read_csv('AMZN.csv')
pd.set_option('display.max_columns', None);
print(df)
print()
print(df.describe())
print()

# *************  Step 2: Prepare the data  ***************************
# Trim the data:
# The ‘Date’ column will be converted to a DateIndex and
# the ‘Adj Close’ will be the only numerical values we keep.
# Everything else is getting dropped.
# Reindex data using a DateIndex
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

print()
print('*****************************')
# Keep only the 'Adj Close' Value
df = df[['Adj Close']]
# Re-inspect data
print(df)
print(df.info())

# ****************Step 3: Let’s plot our data to get a visualization ******
import matplotlib.pyplot as plt
# plot data
df.plot()
plt.show()

# *************** Step 4: Adding Technical Indicators  *******************
# To add our technical indicators we’ll be using the pandas_ta library.
# To get started, let’s add an exponential moving average (EMA) to our data:
import pandas_ta
# Add EMA to dataframe by appending
# Note: pandas_ta integrates seamlessly into # our existing dataframe
# pip install pandas_ta

df.ta.ema(close='Adj Close', length=10, append=True)
print()
print(df)
print(df.info())
# we now have a new column in our data titled “EMA_10.”
# This is our newly-calculated value representing the exponential
# moving average calculated over a 10-day period.
# # Print the first 10 entries of our data
print(df.head(10))
# the first 9 entries in our data will have a NaN value since
# there weren’t proceeding values from which the EMA could be calculated.
# so drop all the rows where we have NaN values
# Drop the first n-rows
df = df.iloc[10:]
# View our newly-formed dataset
print(df.head(10))
# Now we’re ready to start developing our regression model
# to see how effective the EMA is at predicting the price of the stock.
# First, let’s take a quick look at a plot of our data now to get an
# idea of how the EMA value tracks with the adjusted closing price.
df.plot()
plt.show()

# ********************  Step 5: Test-Train Split  ****************************
# Split data into testing and training sets
X_train, X_test, y_train, y_test = train_test_split(df[['Adj Close']], df[['EMA_10']], test_size=.2)
# Take a look at the test and train datasets:
print()
print('Test set:')
print(X_test.describe())
print()
print('Train set:')
print(X_train.describe())

# *******************  Step 6: Training the Model  ***************************
from sklearn.linear_model import LinearRegression
# Create Regression Model
model = LinearRegression()
# Train the model
model.fit(X_train, y_train)
# Use model to make predictions
y_pred = model.predict(X_test)

# ********************* Step 7:  Assess the model  *********************
# assess how well our model fits our data by examining our model coefficients
# and some statistics like the mean absolute error (MAE) and coefficient of
# determination (r2).
print()
from sklearn.metrics import mean_squared_error, r2_score, mean_absolute_error
# Printout relevant metrics
print("Model Coefficients:", model.coef_)
print("Mean Absolute Error:", mean_absolute_error(y_test, y_pred))
print("R-square:", r2_score(y_test, y_pred))
# a lower MAE value is better, and the closer our R-square value is to 1.0 the better

