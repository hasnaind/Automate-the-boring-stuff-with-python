# Automate-the-boring-stuff-with-python
Python Practice
Chapter # 3 
Practice Projects
# The Collatz Sequence Programe
def collatz(number):
    if number%2==0 and number>0:
        number=number/2
        return(number)
    else:
        number=3*number+1
        return(number)
def fun():
    while True:
        try:
            number=int(input('enter an integer'))
            break
        except:
            print('you must have to enter an integer')
    if number==1:
        print(number)
    while number!=1:
        number=collatz(number)
        print(int(number))
