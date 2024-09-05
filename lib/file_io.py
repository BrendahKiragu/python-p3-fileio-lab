def write_file(file_name, file_content):
    with open(f"{file_name}.txt", mode='w', encoding='utf-8') as write_file:
        write_file.write(file_content)
    pass

def append_file(file_name, append_content):
    with open(f"{file_name}.txt", mode='a', encoding='utf-8') as append_file:
        append_file.write(append_content)
    pass

def read_file(file_name):
    with open(f"{file_name}.txt", mode='r', encoding='utf-8') as read_file:
        for line in read_file:
            print(line)
    

    
write_file("log_file", 'hello world. Am written by python.')    
append_file("log_file", " Whoa! Python appended me!")
read_file("log_file")
