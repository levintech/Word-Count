import os

def is_legal(chr):
    if chr >= 'a' and chr <= 'z':
        return True
    elif chr >= 'A' and chr <= 'Z':
        return True
    elif chr >= '0' and chr <= '9':
        return True
    elif chr == '\'' or chr == '-':
        return True
    
    return False

def clean_word(word):
    legal_chrs = [chr for chr in word if is_legal(chr)]
    return ''.join(legal_chrs).lower()

if __name__=='__main__':

    popular_words = {}
    alphabet_words = {}

    # Open the file with input name
    file_name = input("Type the file name : ")

    file_path = os.getcwd() + '\\' + file_name
    print("File path is : %s" % file_path)

    with open(file_path, 'r') as file_object:
        file_content = file_object.read()
        word_list = file_content.split()
        print("Original text\n", word_list)
        cleaned_word_list = [clean_word(word) for word in word_list]
        print("Cleaned text\n", cleaned_word_list)

        result_dict = {}
        for word in cleaned_word_list:
            if word in result_dict.keys():
                result_dict[word] += 1
            else:
                result_dict[word] = 1

        print("Result Dictionary\n", result_dict)

        # sort by word count
        popular_words = dict(sorted(result_dict.items(), key=lambda x:x[1], reverse=True))
        print("Most Popular word list\n", popular_words)

        # sort by alphabet
        alphabet_words = dict(sorted(result_dict.items(), key=lambda x:x[0]))
        print("Alphabet word list\n", popular_words)
    
    # Save the result to file
    file_path = os.getcwd() + '\\' + "most_popular.txt"
    with open(file_path, 'w+') as file_object:
        for key in popular_words.keys():
            file_object.write(key + ', ' + str(popular_words[key]) + '\n')

    file_path = os.getcwd() + '\\' + "alphabetical.txt"
    with open(file_path, 'w+') as file_object:
        for key in alphabet_words.keys():
            file_object.write(key + ', ' + str(alphabet_words[key]) + '\n')
