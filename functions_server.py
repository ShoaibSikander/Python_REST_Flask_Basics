def function_home_page():
    resp = '***** Welcome to Home Page *****'
    return resp

def function_page_1():
    resp = "You are on Page 1"
    return resp

def function_page_2():
    resp = "You are on Page 2"
    return resp

def function_page_3():
    resp = "You are on Page 3"
    return resp

def function_page_4():
    resp = "You are on Page 4"
    return resp

def function_person_info():
    resp = "You are Person Info Page"
    return resp

def function_person_detail(first_name, last_name, age, height):
    print('First Name: ', first_name)
    print('Last Name: ', last_name)
    print('Age: ', age)
    print('Height: ', height)
    resp = first_name+' '+last_name
    return resp