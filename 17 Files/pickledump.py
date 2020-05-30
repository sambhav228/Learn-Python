'''Serializing'''
import pickle, student

f = open("student.dat","wb")
s = student.Student(201851024, 'Anubhav Madhav', 100)
pickle.dump(s,f)            # dumped using pickle
f.close()