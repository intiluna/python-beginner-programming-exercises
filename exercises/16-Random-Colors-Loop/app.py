import random

def get_color(color_number=4):
    # making sure is a number and not a string
    color_number = int(color_number)

    switcher={
                  0:'red',
                  1:'yellow',
                  2:'blue',
                  3:'green',
                  4:'black'
              }
    return switcher.get(color_number,"Invalid Color Number")


def get_allStudentColors():
    ramdom_number = random.randint(0,4)
    example_color = get_color(ramdom_number)
    students_array = []
    #your loop here
    for i in range(1,11):
        #print(i)
        ramdom_number = random.randint(0,3)
        example_color = get_color(ramdom_number)
        students_array.append(example_color)
        #print(ramdom_number)
        #print(example_color)
    return students_array


print(get_allStudentColors())