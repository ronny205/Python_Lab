def passw(passwd):
    SpecialSym=['@', '$', '#', '&']
    val = True

    if len(passwd)<6:
        print('Password should contain more than 6 character')
        val=False
    if len(passwd)>8:
        print('Password should contain less than 8 character')
        val=False
    if not any(char.isdigit() for char in passwd):
        print('Password should contain at least 1 number')
        val=False
    if not any(char.islower()for char in passwd):
        print('Password should contain at least 1 lower case letter')
        val=False
    if not any(char in SpecialSym for char in passwd):
        print('Password shoul contain at least 1 special character @#&$')
        val=False
    if val:
        return val
def main():
    passwd='Rohan@12'
    if(passw(passwd)):
        print("Password is valid")
    else:
        print("Password is invalid")

if __name__=='__main__':
    main()