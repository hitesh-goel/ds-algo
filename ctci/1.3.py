# write method to replace all the spaces in a string with %20. Given also the true lenght in the end.

# Solutions
# 1. Create a new string and append the chaacters until a space came. Instead of space append the %20 value. As well keep on increment the counter to validate it.
# 2. InPlace replace the space with chars


def in_place_replace(str):
    i = 0
    while i < len(str):
        if str[i] == " ":
            str[i+2:] = str[i+1:len(str)-2]
            str[i:i+2] = "%20"
            i+=2
        else:
            i+=1
    return str


def main():
    str = "hi hi  "
    print(in_place_replace(str))

if __name__ == "__main__":
    main()
