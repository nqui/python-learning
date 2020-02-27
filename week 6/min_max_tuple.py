import random
def main():
    newList=[0]*5
    for num in range(0,5):
        newList[num] = random.randint(0,99)
        print(newList[num])
    print('The max is: ', max(newList)) 
    print('The min is: ', min(newList))    
main()        