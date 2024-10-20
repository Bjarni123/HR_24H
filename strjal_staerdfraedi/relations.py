# T-117-STR1 Discrete Mathematics I
# Template for Individual assignment 5

# Problem 1a)
def is_reflexive(defined_set, relation_on_set):
    # Create an empty set to hold what elements hold the same values
    pairs = set()

    # Loop over the element and if they hold the same value then i add that value to the pairs set
    for element in relation_on_set:
        if element[0] == element[1]:
            pairs.add(element[0])

    # if the defined set and relation set are the same that means that the relation_on_set holds all values of the defined set
    return set(defined_set) == pairs


# Problem 1b)
def is_symmetric(relation_on_set):
    """ the_dict = dict()

    for element in relation_on_set:
        if element[0] != element[1]:
            element_list = [str(value) for value in element]
            dict_key = "".join(sorted(element_list))
            if dict_key in the_dict:
                the_dict[dict_key] += 1
            else:
                the_dict[dict_key] = 1
        
    for value in the_dict.values():
        if value != 2:
            return False
        
    return True """


    # I create a variable to hold the last value
    last_value = None

    # Loop through all elements
    for element in relation_on_set:

        # if the values are the same, I skip
        if element[0] == element[1]:
            continue

        # If last value is empty, it means that we just finished 2 symmetries(or this is the first element)
        # Therefore, I update the last element and then skip to the next element
        if not last_value:
            last_value = element
            continue

        # Now we have made sure that the element does not hold 2 of the same values, and that the last_value is not empty
        # If the reverse of the element is not the same as the last value, It means that the relation_on_set is not symmetric
        element_reversed = list(element)[::-1]
        last_value_list = list(last_value)
        if not (element_reversed == last_value_list):
            return False
        
        last_value = None

    # We need to know if there is a value at the end that has not gone through, if the last_value is empty,
    # it means that we didn't have a value in the end that didn't go through the check. And then i return accordingly
    return not bool(last_value)


        

        


print(is_symmetric([(1, 1), (1, 3), (2, 2), (2, 3), (3, 3), (4, 4)])) #         False
print(is_symmetric([('Alice','Bob'),('Bob','Alice')])) #                        True
print(is_symmetric([(1, 2), (2, 1), (2, 3), (3, 2), (1, 3), (3, 1)])) #         True
print(is_symmetric([(1, 2), (2, 1), (3, 3), (4, 4), (1, 3)])) #                 False

# Problem 1c)
def is_antisymmetric(relation_on_set):
    # I create a variable to hold the last value
    last_value = None

    # Loop through all elements
    for element in relation_on_set:

        # if the values are the same, I skip
        if element[0] == element[1]:
            continue

        # If last value is empty, it means that we just finished 2 symmetries(or this is the first element)
        # Therefore, I update the last element and then skip to the next element
        if not last_value:
            last_value = element
            continue

        # Now we have made sure that the element does not hold 2 of the same values, and that the last_value is not empty
        # If the reverse of the element is not the same as the last value, It means that the relation_on_set is not symmetric
        element_reversed = list(element)[::-1]
        last_value_list = list(last_value)
        if not (element_reversed == last_value_list):
            return True
        
        last_value = None

    # We need to know if there is a value at the end that has not gone through, if the last_value is empty,
    # it means that we didn't have a value in the end that didn't go through the check. And then i return accordingly
    return False

# Problem 1d)
def is_transitive(relation_on_set):
    return #TODO Implement

# Problem 2    
def is_equivalence_relation(defined_set, relation_on_set):
    return #TODO Implement

# Problem 3
def composite_relations(relation1, relation2):
    return True

# Problem 4a)
def aces_in_relation_a(A):
    return #TODO Implement

# Problem 4b)
def aces_in_relation_b(A):
    return #TODO Implement

# Problem 4c)
def aces_in_relation_c(A):
    return #TODO Implement
   
# Problem 4d)
def aces_in_relation_d(A):
    return #TODO Implement
    
# Problem 5e)
def aces_in_relation_e(A):
    return #TODO Implement































            