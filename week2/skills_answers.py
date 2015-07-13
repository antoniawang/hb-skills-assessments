# To work on the advanced problems, set to True
ADVANCED = True


def count_unique(input_string):
    text = input_string
    words = text.split()
    keys = set(words)
    dictionary = dict.fromkeys(keys,0)

    
    for word in words:
        dictionary[word] +=1

    return dictionary    


def find_common_items(list1, list2):
    common_items_list = sorted(list1 + list2)
    common_items_set = set(common_items_list)
    for item in common_items_set:
        common_items_list.remove(item)

    return common_items_list   

#Antonia comment: this problem was confusing because the example result seems inconsistent with the logic of the instructions



def find_unique_common_items(list1, list2):
    set1 = set(list1)
    set2 = set(list2)
    common_items_set = (set1 & set2)
    common_items_list = list(common_items_set)
    return common_items_list



def get_sum_zero_pairs(input_list):
    sum_zero_pairs = []
    input_list.sort()
    for number in input_list:
        if number*-1 in input_list:
            pair = sorted([number, number*-1])
            print pair
            if pair not in sum_zero_pairs:
                sum_zero_pairs.append(pair)

    return sum_zero_pairs        


def remove_duplicates(words):
    unique_words = []
    for word in words:
        if word not in unique_words:
            unique_words.append(word)
    
    return unique_words

def encode(phrase):
    replace_tuples = [("e","p"),
                      ("a","d"),
                      ("t","o"),
                      ("i","u")]

    for old_char,new_char in replace_tuples:
        phrase = phrase.replace(old_char,new_char)
    return phrase

def sort_by_word_length(words):
    """Given list of words, return list of ascending [(len, [words])].

    Given a list of words, return a list of tuples, ordered by word-length.
    Each tuple should have two items--the length of the words for that
    word-length, and the list of words of that word length.

    For example:

        >>> sort_by_word_length(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['ok', 'an']), (3, ['day']), (5, ['apple'])]

    """
    words.sort(key = len)

    length_set = set([len(word) for word in words])
    list_of_tuples = []
    for i in length_set:
        tup = (i,[word for word in words if len(word)==i])
        list_of_tuples.append(tup)
    return list_of_tuples    




def get_pirate_talk(phrase):

    pirate_dictionary = { "sir" : "matey",
                          "hotel" : "fleabag inn",
                          "student" : "swabbie",
                          "boy" : "matey",
                          "madam" : "proud beauty",
                          "professor" : "foul blaggart",
                          "restaurant" : "galley",
                          "your" : "yer",
                          "excuse" : "arr",
                          "students"  : "swabbies",
                          "are" : "be",
                          "lawyer" : "foul blaggart",
                          "the" : "th'",
                          "restroom" : "head",
                          "my" : "me",
                          "hello" : "avast",
                          "is" : "be",
                          "man" : "matey"
                          }

    

    for english_word, pirate_word in pirate_dictionary.iteritems():
        phrase = phrase.replace(english_word,pirate_word)

    return phrase


# End of skills. See below for advanced problems.
# To work on them, set ADVANCED=True at the top of this file.
############################################################################


def adv_get_top_letter(input_string):
 
  
#     Given a list of words, return a list of tuples, ordered by word-length.
#     Each tuple should have two items--a number that is a word-length,
#     and the list of words of that word length. In addition to ordering
#     the list by word length, order each sub-list of words alphabetically.
#     Now try doing it with only one call to .sort() or sorted(). What does the
#     optional "key" argument for .sort() and sorted() do?

#     For example:

#         >>> adv_alpha_sort_by_word_length(["ok", "an", "apple", "a", "day"])
#         [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]

#     """
    words.sort(key = len)

    length_set = set([len(word) for word in words])
    list_of_tuples = []
    for i in length_set:
        tup = (i,[word for word in words if len(word)==i])
        list_of_tuples.append(tup)
    return list_of_tuples 


##############################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is just used to print dictionaries in key-alphabetical
    # order, and is only used for our documentation tests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join("%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is used only
    # for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)

if __name__ == "__main__":
    print
    import doctest
    for k, v in globals().items():
        if k[0].isalpha():
            if k.startswith('adv_') and not ADVANCED:
                continue
            a = doctest.run_docstring_examples(v, globals(), name=k)
    print "** END OF TEST OUTPUT"
    print
