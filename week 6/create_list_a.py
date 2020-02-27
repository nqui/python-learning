import random
def main():
    l = int(input('Enter the length of the list: '))
    newList=[0]*l
    for num in range(0,l):
        newList[num] = random.randint(1,10)
        print(newList[num])
    
    index=0
    while newList[index]<=8:
        newList[index]=99
        print(newList[index])
        index += 1
        
main()        