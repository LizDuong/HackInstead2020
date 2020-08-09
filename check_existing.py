def check_id(id):
    if check_if_string_in_file('id_file.txt', id):
        return False
    else:
        with open('id_file.txt', 'a+') as file_object:
            file_object.write('\n')
            file_object.write(id)
    return True



def check_if_string_in_file(file_name, string_to_search):

    with open(file_name, 'r') as read_obj:
        for line in read_obj:
            if string_to_search in line:
                return True
    return False