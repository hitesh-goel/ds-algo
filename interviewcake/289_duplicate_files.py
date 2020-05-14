# https://www.interviewcake.com/question/python3/find-duplicate-files


def find_duplicates():
    # GO through all the directories of the file system
    # use the iterative approach to save stack calls
    # So use stack to store all the directories
    # if while iteration we encounter with a file store the contents of the file
    # to save space hash the contents of the files while reading the file
    # to get the more specifics, get the file bytes from start middle and end using file.seek to seek
    # hash the seeked contents of the file
    # store this hash in already scanned files
    # if there is another file with same content then hash will match
    # store these matched hash file paths in a tuple and save the tuple to dictionary
    # return the dictionary
    return []


def main():
    pass


if __name__ == '__main__':
    main()
