def main():
    string = input('Enter a string: ')
    n = len(string)
    print('The length of the string is: ', n)
    if n%2==0:
        pos = int(n/2) 
    else:
        pos = int((n+1)/2)
    
    ch = string[pos-1]
    print('The center letter is: ',ch)

main()    