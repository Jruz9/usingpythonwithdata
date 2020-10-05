#this script is about the function and scoping
# has an error of being true always
def max_Val(x,y):

    if x.find(y):
        return True
    else:
        return False


def main():
    stringOccurance=max_Val("Hello my friend","Hello my friend is here")
    print(stringOccurance)


if __name__ == '__main__':
    main()
