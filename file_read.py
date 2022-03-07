file = open("sample.txt", "r")  # we are using the r = read mode to read the file with creating sample.txt of any file reading
                                # diff modes are there likely, r , w,  a for append
                                # open function is also used to open the sample file we created it!!!
data = file.read()  # read function has been used for this
print(data)