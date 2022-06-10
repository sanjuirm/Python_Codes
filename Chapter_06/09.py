def grade(score):
    while True:
        if score>=90 and score<=100:
            return 'A'
        if score>=80 and score<=89:
            return 'B'
        if score>=70 and score<=79:
            return 'C'
        if score>60 and score<=69:
            return 'D'
        if  score<=60:
            return 'F'
        else:
            print('\nWrong GP!!! Try Agin.')

def main():
    n=eval(input('\nEnter Grade Point(0-100): '))
    GD=grade(n)
    print('Grade Point is:',GD)

main()

