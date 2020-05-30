'''
f = open(filename(or filepath), mode, buffer)            # buffer id just a number and is optional, if we do not provide buffer, then python automaticall takes 4096 or 8092 as buffer
f.close()

modes for text files:
w   -   Write Mode, it deletes the previous data and writes the new data into the file
r   -   Read Mode,  it reads the file from very beginning upto the end of file.
a   -   Append Mode, it adds on the new data after the old data, i.e. it do not deleted the previous data, but adds on the new data after the old one
w+  -   Read and Write Mode
r+  -   Read, Write and Append Mode
a+  -   Append and Read Mode
x   -   Exclusive or Exclusive Creation Mode, Once you open a file in this mode a new file will be created for you exclusively, and if a file already exists with the same name then an error will be thrown



modes for binary files:
wb
rb
ab
w+b
r+b
a+b
xb
'''