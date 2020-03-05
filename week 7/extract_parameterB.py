def main():
    string = input('Enter a parameter and its value: ')
    string = string.strip()
    data = string.split()
    print(data)
    parameter = data[0]
    value = float(data[1])
    print('The parameter is: ', parameter)
    print('The value is: ', format(value,'0.2f'))
             
main()    