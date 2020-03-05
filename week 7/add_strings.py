def main():
    nameA = input('Enter a name: ')
    nameB = input('Enter a second name: ')
    if len(nameA)<7 and len(nameB)<7:
        newName1 = nameA + ' ' + nameB
        print('newName1 is: ', newName1)
    else:
        print('The length restrictions are not met.')
            

main()    