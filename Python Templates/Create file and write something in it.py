import tempfile

# create a temporary file and write some data to it
fp = tempfile.TemporaryFile()
fp.write(b'Hello world!')
# read data from file
fp.seek(0)
fp.read()
b'Hello world!'
# close the file, it will be removed
fp.close()

# create a temporary file using a context manager
with tempfile.TemporaryFile() as fp:
    fp.write(b'Hello world!')
    fp.seek(0)
    fp.read()
b'Hello world!'

# file is now closed and removed

# create a temporary directory using the context manager
with tempfile.TemporaryDirectory() as tmpdirname:
    print('created temporary directory', tmpdirname)

# directory and contents have been removed
