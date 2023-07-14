# file handling
# read, writing and appending 

import os

dummy_file_path = "topic.txt"

print(os.getcwd())

if os.access(dummy_file_path, os.W_OK):
    print("You have write permissions in the directory.")
else:
    print("You do not have write permissions in the directory.")


def write_file(file_path):
    with open(file_path, 'w') as file:
        file.write("Hello from the app")   

try:
    write_file(dummy_file_path)
except Exception as e:
    print("An error occurred:", str(e))



     

# def file_exists(file_path):
 #   if os.path.exists(file_path):
  #    return True
  #   # perform reading poeration 
  #  else:
  #   raise Exception(f"{file_path} does not exist")
    

# def read_file(file_path):
#    with open(file_path, 'r') as file:
#        content = file.read()
 #   return content
    


# try:
    # file_exists(file_path)
   #  dummy_content = read_file(dummy_file_path)
    # print(dummy_content)
# except Exception as err:
   #  print(str(err))
    
    
    
    


# print("file exists or not", os.path.exists(file_path))