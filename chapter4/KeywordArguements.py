#has keyword arguements and default values
def printName(firstName,lastName,reverse):
    if reverse:
        print(lastName+" "+firstName)
    else:
        print(firstName,lastName)

def main():
    printName("jose","cruz",reverse=True)


if __name__ == '__main__':
    main()