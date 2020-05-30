'''Deserializing the object using Pickle'''

import pickle

f = open('student.dat','rb')
obj = pickle.load(f)
    # Now, 'obj' is a deserialized object
obj.display()
f.close()

'''Pickle: The process of writing an object to stream'''