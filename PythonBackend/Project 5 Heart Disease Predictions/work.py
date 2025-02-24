import pickle

model = pickle.load(open('model.pkl','rb'))

pred = model.predict([[54,1,0,122,286,0,0,116,1,3.2,1,2,2]])
print(pred[0])