# Grading.py

def main():
    scale_Chart=['F','F','D','C','B','A']

    while True:
        n=eval(input('Enter Grade Point(0-5): '))
        if n<=5:
            break
        else:
            print('Wrong GP!!! Try Agin.')
    
    print('The Grade is: ',scale_Chart[n])

main()