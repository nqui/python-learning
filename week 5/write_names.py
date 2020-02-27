def main():
    outfile = open('names.txt','w')
    n = input('enter a name or 0 to exit: ')
    while(n != '0'):
        outfile.write(n + '\n')
        n = input('enter a name or 0 to exit: ')
    outfile.close
main()