
list = [5000,2000,1000,500,200,100,50,20,10,5,3,1]
def bankomat(list):
    user_request = int(input('Vvedite nominal: '))
    if user_request in list:
        print('Vozmite babki!')
    else:
        print("Neverno!")

bankomat(list)