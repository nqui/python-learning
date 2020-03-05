def main():
    string = input('Enter a parameter and its value: ')
    string = string.strip()
    
    if string.isalnum() and len(string)>1:
        parameter = string[0]
        if parameter.isalpha:
            print('The parameter is: ', parameter)
        else:
            print('Parameter name error.')
        
        value = string[1:]
        if value.isdigit():
            value = float(value)
            print('The value is: ', format(value,'0.2f'))
        else:
            print('Value error.')
    else:
        print('There is something wrong in the data')
             
main()    