def main():
    outfile = open('sample.txt','w')
    name = input('enter your name: ')
    outfile.write(name + '\n')

    name = input('enter another name: ')
    outfile.write(name + '\n')
    outfile.close

main()