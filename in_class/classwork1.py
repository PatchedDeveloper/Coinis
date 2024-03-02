#classwork

def task_1(n):

    if len(n) == 6:
             first = int(n[0])
             second = int(n[1])
             third = int(n[2])
             fourth = int(n[3])
             fifth = int(n[4])
             sixth = int(n[5])

             if first * third + 2 + sixth == second + fourth * fifth:
               print(True)
             else:
                print(False)
    else:
        print('wrong number')


task_1(input('Enter a 6 digit number: '))