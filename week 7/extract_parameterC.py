def main():
    string = input('Enter the data: ')
    string = string.strip()
    data = string.split()
    print(data)
    parameter = data[0]
    parameter = parameter.lower()
    if parameter[0]=='p': 
        value = float(data[1])
        print('The parameter is pressure.')
        print('The value is: ', format(value,'0.2f'))
    else:
        print('It is not pressure.')
             
main()    