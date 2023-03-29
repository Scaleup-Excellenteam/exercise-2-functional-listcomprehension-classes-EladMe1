def group_by(f, it):
    """ f, a function that maps elements of it to keys, and it, an iterable of elements.
     The function returns a dictionary that groups the elements of it by the keys returned by f.

The function iterates over it and applies f to each element, storing the result in res.
 If res is not already a key in the dictionary the_dict,
 it creates a new key with an empty list as its value, and appends var to the list.
 If res is already a key in the_dict, it simply appends var to the existing list.
       """

    the_dict = {}
    for var in it:
        res = f(var)
        if res not in the_dict:
            the_dict[res] = [var]
        else:
            the_dict[res].append(var)
    return the_dict

