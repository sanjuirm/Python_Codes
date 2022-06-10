# Grading(100 Scale).py

def main():
    while True:
        n=eval(input('\nEnter Grade Point(0-100): '))
        if n>=90 and n<=100:
            print('Grade: A')
            break
        if n>=80 and n<=89:
            print('Grade: B')
            break
        if n>=70 and n<=79:
            print('Grade: C')
            break
        if n>60 and n<=69:
            print('Grade: D')
            break
        if  n<=60:
            print('Grade: F')
            break
        else:
            print('\nWrong GP!!! Try Agin.')

main()
            