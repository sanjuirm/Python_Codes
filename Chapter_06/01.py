def song(animal,sound):
    return'old MacDonald had a farm,Ee-igh,Ee-igh,oh!\nAnd on that farm he had a' + animal +',Ee-igh,Ee-igh,oh!\nWith a' + sound + ',' + sound + ' here and a' + sound + ',' + sound + 'there.\nHere a' + sound + ',there a' + sound + ',everywhere a' + sound + ',' + sound + '.\nold MacDonald had a farm,Ee-igh,Ee-igh,oh!'
    

def main():
    for i in range(5):
        pet=input('Enter Animal type:')
        sound=input('Enter voice:')
        lyrcs=song(pet,sound)
        print(lyrcs)
main()
