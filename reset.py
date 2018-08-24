import pickle

tdo = open('train_data.pkl', 'wb')
tlo = open('train_label.pkl', 'wb')

td = []
tl = []

pickle.dump(td, tdo)
pickle.dump(tl, tlo)

tdo.close()
tlo .close()