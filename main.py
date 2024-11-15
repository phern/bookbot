path_to_file = 'books/frankenstein.txt'


def main():
    with open(path_to_file) as f:
        file_contents = f.read()
        infoDump(file_contents)

def infoDump(file_contents):
    print(f'--- Begin report of {path_to_file} ---')
    print(countWords(file_contents))
    print('\n')
    allCharCountPrint(reverse_sort(countChars(file_contents)))
    print('--- End report ---')

#takes dictionary 
def allCharCountPrint(dictionary):
    for key in dictionary:
        print(f'The {key} was found {dictionary[key]} times')

# takes dictionary returns dictionary
# sorts the dictionary descending, excluding special chars and numbers
def reverse_sort(char_dict):
    clean_dict = {key: value for key, value in char_dict.items() if key.isalpha()}
    sorted_by_count = sorted(clean_dict.items(), key=lambda x:x[1], reverse=True)
    return dict(sorted_by_count)

# takes string returns int
def countWords(file_contents):
    count = len(file_contents.split())
    return count

# takes file returns dictionary
# updates dictionary for every character in input
def countChars(file_contents):
    char_dict = {}
    for i in file_contents:
        char = i.lower()
        if char not in char_dict:
            char_dict.update({char: 0})
            char_dict.update({char: char_dict[char] + 1})
        else:
            char_dict.update({char: char_dict[char] + 1})

    return char_dict

main()
