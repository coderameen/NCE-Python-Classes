from sklearn.linear_model import LinearRegression
import pandas as pd
import pickle

#2. read csv file
df = pd.read_csv("cgpa.csv")
print(df.head())

#3. x(input) and y(output) axis
x = df.drop(columns=['cgpa'])
# print(x)
y = df.cgpa
print(y)

#4.
#call the algorithm
model = LinearRegression()
#Train
model.fit(x,y)

# #output
# pred = model.predict([[10,2]])
# print("The cgpa of student is : ",pred)


#pickle.dump(gpr, open(filename, 'wb')) 
pickle.dump(model, open('model.pkl','wb'))
