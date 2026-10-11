def welcome():
    print("Hey Wellcome from Shahid ")

print(__name__)


# when we use if __name__ == "__main__": 
# this after code of this line will 
# only execute wen we run this file.
# but not execute in file where we use it
if __name__ == "__main__":
    welcome()