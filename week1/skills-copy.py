"""Skills Assessment: Lists.

To work on an item, uncomment the entire function (including the docstring)
and then run this script. It should output an error that the newly-uncommented
function is now failing its tests.

Edit the function body until you have a solution and the test passes, and then
move on to the next function.

This assessment is DUE TO YOUR ADVISOR BY SUNDAY EVENING.
"""


def all_odd(number_list):
    """Return a list of only the odd numbers in the input list."""
    for i in number_list:
        if i%2 == 0:
            number_list.pop()
    return number_list



def all_even(number_list):
    for i in number_list:
        if i%2 != 0:
            number_list.pop()
    return number_list



def print_indeces(my_list):
    """Print the index of each list item, followed by the item itself."""
    new_list = []
    for i in my_list:
        new_list.append(i)
        print len(new_list)-1, i


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters."""
    for i in word_list:
        if len(i) <= 4:
            word_list.pop()
    return word_list
        

def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it."""
    number_list.sort()
    if len(number_list) !=0:
        smallest = number_list[0]
        return smallest
    return None


def largest_int(number_list):
    """Find the largest integer in a list of integers and return it."""
    if len(number_list) !=0:
        largest = number_list[0]
        for i in number_list:
            if i > largest:
                largest = i
        return largest
    return None


def halvesies(number_list):
    """Return list of numbers from input list, each divided by two."""
    half_list = []
    for i in number_list:
        float(i)
        half_list.append(float(i)*0.5)
    return half_list    


def word_lengths(word_list):
    """Return the length of words in the input list."""
    length_list = []
    for i in word_list:
        length_list.append(len(i))
    return length_list


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list."""
    x = 0
    for i in number_list:
        x+=i
    return x


def mult_numbers(number_list):
    if 0 in number_list:
        return 0
    else:
        x = 1
        for i in number_list:
            x*=i
        return x


def join_strings(word_list):
    x = ''
    for i in word_list:
        x += i
    return x


def average(number_list):
   return sum_numbers(number_list)/float(len(number_list))


##############################################################################
# END OF SKILLS TEST; YOU CAN STOP HERE OR YOU CAN WORK ON ADVANCED PROBLEMS


# def advanced_join_strings(list_of_words):
#     """Return a single string with each word from the input list
#     separated by a comma.
#
#         >>> advanced_join_strings(["Labrador", "Poodle", "French Bulldog"])
#         'Labrador, Poodle, French Bulldog'
#
#     If there's only one thing in the list, it should return just that
#     thing, of course:
#
#         >>> advanced_join_strings(["Pretzel"])
#         'Pretzel'
#
#     """
#
#     return ""


##############################################################################
# You can ignore everything after here

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
