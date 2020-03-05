def main():
    string = input('Enter a URL: ')
    string = string.strip()
    n = string.find('//')
    print(n)
    data = string[n+2:]
    data = data.rstrip('/')
    print(data)
             
main()    