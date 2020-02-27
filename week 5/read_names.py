def main():
    n = open('names.txt','r')
    content = n.read()
    print(content)
    n.close()
main()