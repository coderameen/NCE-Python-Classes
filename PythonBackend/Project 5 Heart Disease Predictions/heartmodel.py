from sklearn.naive_bayes import MultinomialNB
import pandas as pd
import pickle

#read dataset
df = pd.read_csv("heart.csv")
# print(df.head())

# print(df.isnull().sum())
# x = df.drop(columns=['target'])
#.iloc[rows,columns]
x = df.iloc[:,:-1]
print(x.head())

# y = df.target
y = df.iloc[:,-1]
print(y)

#Train and testing
from sklearn.model_selection import train_test_split
x_train,x_test,y_train,y_test = train_test_split(x,y,test_size=0.2)

print(len(x))
print("traiing>>",len(x_train))
print("testing>>",len(x_test))


#call the algorithm
# from sklearn.naive_bayes import MultinomialNB
model = MultinomialNB()

#Training
model.fit(x_train,y_train)

#output
pred = model.predict([[71,0,0,112,149,0,1,125,0,1.6,1,0,2]])

# if pred[0] == 1:
#     print("You have heart disease!!")
# else:
#     print("you don't")


pickle.dump(model,open('model.pkl','wb'))