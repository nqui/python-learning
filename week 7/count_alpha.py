def main():
    name = input('Enter a name: ')
    c = input('Enter the character to search:')
    count=0
    for letter in name:
        if letter == c:
            count+=1
    print(count)

main()    