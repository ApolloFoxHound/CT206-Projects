# Dictionaries and Sets
# https://www.cse.msu.edu/~cse231/PracticeOfComputingUsingPython/06_Dictionaries/DocRetrieval/
# Doc Retrieval
# This file utilizes the provided ap_docs.txt that was given in the assignment.

import string


def make_dict(filename):
    file_obj = open(filename, 'r')
    curr_doc = 0
    word_dict = {}
    doc_dict = {}
    text = ''
    for line in file_obj:
        if '<NEW DOCUMENT>' in line:
            # end of doc reached. Store doc_num:text in doc_dict
            doc_dict[str(curr_doc)] = text
            text = ''
            curr_doc += 1  # increment the document number
        else:
            # split the line into individual words and sanitize
            word_list = line.lower().split()
            text += line
            for word in word_list:
                word = word.strip(string.punctuation)
                if word == '':
                    continue
                # build inverted index
                if word in word_dict:
                    word_dict[word].add(curr_doc)
                else:
                    new_set = set()
                    new_set.add(curr_doc)
                    word_dict[word] = new_set

    file_obj.close()
    return word_dict, doc_dict


def search(keyword_str, index):
    key_words = keyword_str.lower().split()
    intersect_docs = None
    for word in key_words:
        if word not in index:
            return []
        elif intersect_docs is None:
            intersect_docs = index[word]
        else:
            # find intersection of all keyword sets
            intersect_docs = index[word].intersection(intersect_docs)
    return list(intersect_docs)


def prompt():
    print('What would you like to do?')
    print('1. Search for documents')
    print('2. Read Document')
    print('3. Quit Program')
    return input('>').lower()


def main():
    index, docs = make_dict('ap_docs.txt')
    # Asks user for input
    user_input = prompt()
    while user_input != '3':
        if user_input == '1': 
            search_terms = input('Enter search words:')
            found_docs = search(search_terms, index)
            if len(found_docs) == 0:
                print('No documents fit that search')
            else:
                print()
                print('Documents fitting search:', )
                for doc_num in found_docs:
                    print(str(doc_num), end=' ')
                print()
                print()
        elif user_input == '2':
            doc_num = input('Enter document number:')
            if doc_num not in docs:
                print('Document not found.')
            else:
                print('Document #' + doc_num)
                print('-' * 25)
                print(docs[doc_num].strip())
                print('-' * 25)
                print()
        elif user_input != '3':
            print('Invalid selection. Try again.')
        user_input = prompt()


main()
