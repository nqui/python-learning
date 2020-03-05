def main():
    name = input('Enter a name: ')
    title = 'Dr.'
    if title not in name:
        name = title +' ' + name
       
    print('Now the name is: ',name)

main()    