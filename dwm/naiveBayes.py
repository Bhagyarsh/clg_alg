data=[ ["age","income","student","c_rating","buy"],
       ["youth","high","no","fair","no"],
       ["youth","high","no","excellent","no"],
       ["middle_aged","high","no","fair","yes"],
       ["senior","medium","no","fair","yes"],
       ["senior","low","yes","fair","yes"],
       ["senior","low","yes","excellent","no"],
       ["middle_aged","low","yes","excellent","yes"],
       ["youth","medium","no","fair","no"],
       ["youth","low","yes","fair","yes"],
       ["senior","medium","yes","fair","yes"],
       ["youth","medium","yes","excellent","yes"],
       ["middle_aged","medium","no","excellent","yes"],
       ["middle_aged","high","yes","fair","yes"],
       ["ssenior","medium","no","excellent","no"]
]
data[0]
def find_probablity(data,col_name=None,col_ind=None):
    sam = 0
    p_y = 0
    p_x = 0
    for index,values in enumerate(data):
        if index is not 0 and col_name is None:
            if f"{values[4]}" == "yes":
                sam+=1
                p_y+=1
            else :
                sam+=1
                p_x+=1
        else :
            if index is not 0 and col_name == values[col_ind]:
                if f"{values[4]}" == "yes":

                    sam+=1
                    p_y+=1
                else :
                    sam+=1
                    p_x+=1

    if col_name:
        print(f"Probablity for {data[0][col_ind]}={col_name} yes:{p_y} no:{p_x}" )
    return (p_y/sam,p_x/sam,col_name,sam)


def print_data(data):
    for index,values in enumerate(data):
        print(f"{index} {values}")
    py ,pn , _ ,sam = find_probablity(data)
    print(f"total Probablity of  buy computer {py}")
    print(f"total Probablity of  buy computer {pn}")

def predict_yes_no(age,income,student,c_rating):
    py_age ,pn_age , _ ,sam = find_probablity(data,age,0)
    py_income ,pn_income , _ ,sam = find_probablity(data,income,1)
    py_student ,pn_student , _ ,sam = find_probablity(data,student,2)
    py_c_rating ,pn_c_rating , _ ,sam = find_probablity(data,c_rating,3)
    py,pn =py_age*py_income*py_student*py_c_rating , pn_age*pn_income*pn_student*pn_c_rating
    buy = None
    if py > pn:
        buy = True
    elif py > pn:
        buy = False

    return py,pn,buy
print_data(data)
print(predict_yes_no("middle_aged","medium","yes","excellent"))
