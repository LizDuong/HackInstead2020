def check_id(id):
    with open('id_file.txt', 'a+') as file_object:
        if id in file_object.read():
            return False
        else:
            file_object.write('\n')
            file_object.write(id)
            return True
