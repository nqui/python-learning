import random
def main():
    newList=[0]*5
    total=0
    for num in range(0,5):
        newList[num] = random.randint(0,99)    
        total += newList[num]
        print(newList[num])
    print('\n The average is: ', total/5)
main()        