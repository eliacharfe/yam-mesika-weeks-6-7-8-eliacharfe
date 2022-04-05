

def group_by(func, iterable):
    """
    Gets a function and an iterable and returns a dictionary which the keys are what the function
    returns on the item of the iterable and the value is a list of the items that the result
    on those items it is this key.
    Possible input:   len, ["hi", "bye", "yo", "try"]
    Output:           {2: ["hi", "yo"], 3: ["bye", "try"]}
    :param func: A function.
    :param iterable: An iterable.
    :return: Dictionary of key and value like explained.
    """
    dictionary_group_by_func = {}
    for item in iterable:
        if func(item) in dictionary_group_by_func:
            dictionary_group_by_func[func(item)].append(item)
        else:
            dictionary_group_by_func[func(item)] = [item]
    return dictionary_group_by_func


if __name__ == '__main__':
    print(group_by(len, ["hi", "bye", "yo", "try"]))




# {func(item): item if func(item) in ... else [item] for item in iterable}