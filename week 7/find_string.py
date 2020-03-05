def main():
    string = input('Enter a string: ')
    substring = input('Enter a substring: ')
    if substring in string:
        print('The substring is present')
    else:
        print('The substring is absent')
             
main()    