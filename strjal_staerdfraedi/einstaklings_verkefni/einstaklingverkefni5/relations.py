# T-117-STR1 Discrete Mathematics I
# Template for Individual assignment 5

"""
Sorry in advance, I try to explain the problems to the best of my abilites.

I try to provide examples for each problem
"""

# ---------------------------------------------------------------------------------------------------------------------------------------

"""
                                                Explanation 1A
reflexive means that for all values in the defined set, 
there is an element in the relation on set that has both the values as the value from the defined set

Example 1:
defined_set = [1, 2, 3]
relation_on_set = [(1, 1), (1, 2), (2, 2), (3, 3)]
Outcome: True

Here all the values from the defined set(1, 2, 3) are all as a double value in the relation_on_set
1 = (1, 1)
2 = (2, 2)
3 = (3, 3)

Example 2:
defined_set = [1, 2]
relation_on_set = [(1, 2), (2, 1), (2, 2)]
Outcome: False

All the values in the defined_set that should appear in relation_on_set:
1 = (1, 1)
2 = (2, 2)

but here we are still missing (1, 1) from the relation_on_set and therefore the outcome is False


All other values, f.x. (1, 2) have no impact on if its reflexive
"""

# Problem 1a)
def is_reflexive(defined_set, relation_on_set):
    # I loop through every single value in the defined_set
    for value in defined_set:
        # And if value is not as (value, value) is not in the set, I return False
        if (value, value) not in relation_on_set:
            return False
    
    # If it makes it out of the loop without returning false, it means that it's reflexive and therefore, return True
    return True

# ---------------------------------------------------------------------------------------------------------------------------------------

"""

A relation_on_set is symmetric when every reverse of an element in it is also in the relation_on_set

Example 1:
relation_on_set = [(1, 2), (2, 1)]
Outcome: True

Here the outcome is true, since for every element in the relation_on_set, 
there exists a reverse of it. (1, 2) becomes (2, 1) and that is in the set as well

Example 2:
relation_on_set = [(1, 2), (2, 1), (2, 3)]
Outcome: False

Here the outcome is false, since the element (2, 3) does not have an inverse of it in the relation_on_set which is (3, 2)
                                                                                            
"""


# Problem 1b)
def is_symmetric(relation_on_set):
    # I loop through every element in the set
    for element in relation_on_set:
        # If the reverse of the element is not in the relation_on_set, I return False
        if element[::-1] not in relation_on_set:
            return False

    # If all reverses of elements are in the relation_on_set, means that it is symmetric, and return True
    return True 

# ---------------------------------------------------------------------------------------------------------------------------------------
       
# 1B test cases

""" 
print(is_symmetric([(1, 1), (1, 3), (2, 2), (2, 3), (3, 3), (4, 4)])) #         False
print(is_symmetric([('Alice','Bob'),('Bob','Alice')])) #                        True
print(is_symmetric([(1, 2), (2, 1), (2, 3), (3, 2), (1, 3), (3, 1)])) #         True
print(is_symmetric([(1, 2), (2, 1), (3, 3), (4, 4), (1, 3)])) #                 False
"""

# ---------------------------------------------------------------------------------------------------------------------------------------

"""
A relation_on_set in anti-symmetric if no reverses of element are in the set, excluding doubles of value, f.x. (a, a) or (b, b)

Example 1:
relation_on_set = [(1, 1), (1, 3), (2, 2), (2, 3), (3, 3), (4, 4)]
Outcome: True

Since there are no reverses of element in the set, It is true.
we have (1, 3) but there is not (3, 1)

Example 2:
relation_on_set = [(1, 2), (2, 1)]
Outcome: False

Since the inverse of (1, 2) is (2, 1) and (2, 1) is in the set the outcome is False
"""

# Problem 1c)
def is_antisymmetric(relation_on_set):
    # Loop through all elements
    for element in relation_on_set:
        # if it does not hold the same value and the reverse of it is in the set I return False
        if element[0] != element[1] and element[::-1] in relation_on_set:
            return False
        
    # If no elements that does not hold the same values and have the inverse of it in the set I return True
    return True
    

# 1C Test cases
""" 
print(is_antisymmetric([(1, 1), (1, 3), (2, 2), (2, 3), (3, 3), (4, 4)])) # True
print(is_antisymmetric([('Alice','Bob'),('Bob','Alice')])) #                False
"""

# ---------------------------------------------------------------------------------------------------------------------------------------

"""
The relation_on_set is transitive if the for every element (a, b) and every element (b, c) there exists (a, c). 
Exclude double values, f.x. (a, a)

Example 1:
relation_on_set = [(1, 2), (2, 3), (1, 3)]
Outcome: True

we start with element1(1, 2) and find a value that has 2 as the first value. The only element in that has that in this set is
element2(2, 3). We attempt to find if there is an element that has the first value from element1 and second value from element2 
which is (1, 3) and is in this set. therefore, we return true
"""

# Problem 1d)
def is_transitive(relation_on_set):
    # Loop throught the elements
    for element in relation_on_set:
        # we exclude double values
        if element[0] != element[1]:

            # Take down the first and second values of the element
            first_value = element[0]
            second_value = element[1]

            # loop through every element again
            for second_element in relation_on_set:
                # If there exists an element that share the second value in element1 and first value in element2
                # and there does not exists a an element that has the first value in element1 as it's first value
                # and the second value as the second value in element 2, Means that the set in not transitive
                if second_element[0] == second_value and (first_value, second_element[1]) not in relation_on_set:
                    return False
            
    # If it does not return False, means that the set is transitive
    return True

# 1D test cases
""" 
print(is_transitive([('Alice', 'Bob'), ('Bob', 'Charlie'), ('Charlie', 'Alice')])) # False
"""

# ---------------------------------------------------------------------------------------------------------------------------------------

# Problem 2    

"""
there is an equivalance relation if it reflexive, symmetric and transitive. So we use the functions from 1 to check if they all check out
and return accordingly
"""

def is_equivalence_relation(defined_set, relation_on_set):
    # If it's reflexive, symmetric and transitive I return True
    if is_reflexive(defined_set, relation_on_set) and is_symmetric(relation_on_set) and is_transitive(relation_on_set):
        return True
    else:
        # Otherwise False
        return False

# 2 test cases
""" 
print(is_equivalence_relation(['Alice', 'Bob', 'Charlie'], [('Alice', 'Bob'), ('Bob', 'Alice'), ('Charlie', 'Charlie')])) #         False
print(is_equivalence_relation([1, 2, 3, 4], [(1, 2), (2, 1), (3, 3), (4, 4), (1, 3)])) #                                            False
print(is_equivalence_relation(['Apple', 'Banana', 'Cherry'], [('Apple', 'Banana'), ('Banana', 'Cherry'), ('Cherry', 'Apple')])) #   False
print(is_equivalence_relation([1, 2, 3], [(1, 2), (2, 3), (1, 3)])) #                                                               False
"""

# ---------------------------------------------------------------------------------------------------------------------------------------

# Problem 3
def composite_relations(relation1, relation2):
    return_value = list()

    for relation1_element in relation1:
        relation1_value1 = relation1_element[0]
        relation1_value2 = relation1_element[1]

        for relation2_element in relation2:
            relation2_value1 = relation2_element[0]
            relation2_value2 = relation2_element[1]
            if relation1_value2 == relation2_value1:
                element_to_append = (relation1_value1, relation2_value2)
                if element_to_append not in return_value:
                    return_value.append(element_to_append)

    return return_value
            
# 3 test cases
""" 
print(composite_relations([(2, 1), (3, 1), (3, 2), (4, 2)], [(1, 2), (1, 3), (2, 3), (2, 4), (3, 1)]) == [(2, 2), (2, 3), (3, 2), (3, 3), (3, 4), (4, 3), (4, 4)], composite_relations([(2, 1), (3, 1), (3, 2), (4, 2)], [(1, 2), (1, 3), (2, 3), (2, 4), (3, 1)]))
print(composite_relations([('b','c'),('a','a'),('a','c'),('c','b')], [('b','a'),('a','c')]) == [('a', 'c'), ('c', 'a')], composite_relations([('b','c'),('a','a'),('a','c'),('c','b')], [('b','a'),('a','c')]))
"""

# ---------------------------------------------------------------------------------------------------------------------------------------

# Problem 4a) {(a, b) | a = 0}
def aces_in_relation_a(A):
    aces_counter = 0

    for element in A:
        if element == 0:
            aces_counter += len(A)

    return aces_counter
    
# 4A test cases
"""
print(aces_in_relation_a([1, 2, 3, 4]))
"""

# ---------------------------------------------------------------------------------------------------------------------------------------

# Problem 4b) {(a, b) | a = b + 1}
def aces_in_relation_b(A):
    len_A = len(A)
    return (len_A - 1)

# ---------------------------------------------------------------------------------------------------------------------------------------

# Problem 4c) {(a, b) | a ≥ b}
def aces_in_relation_c(A):
    the_sum = 0
    for add_to_sum in range(1, len(A) + 1):
        the_sum += add_to_sum

    return the_sum

# ---------------------------------------------------------------------------------------------------------------------------------------

# Problem 4d) {(a, b) | a + b = 1000}
def aces_in_relation_d(A):
    len_A = len(A)

    if len_A < 500:
        return 0
    else:
        a_plus_b = 1000
        highest_possible_aces = a_plus_b - 1 # change a_plus_b if a + b should be something else 
        possibly_wrong_return_value = 1 + ((len_A - 500) * 2)
        return min(possibly_wrong_return_value, highest_possible_aces)

# 4d test cases
"""     
print(aces_in_relation_d([x for x in range(1, 1683)]))
"""

# ---------------------------------------------------------------------------------------------------------------------------------------

# Problem 4e) {(a, b) | a + b ≥ 1001}
def aces_in_relation_e(A):
    len_A = len(A)

    if len_A <= 500:
        return 0
    else:
        # The total sum of a_n = a_n-1 + 3 + 4 x n-1
        n = len_A - 500
        plus = 4
        add_to_sum = 3
        sum_of_a = 3
        for x in range(1, n):
            add_to_sum += plus
            if x >= 499:
                plus = 2
            sum_of_a += add_to_sum

        return sum_of_a

# 4E test cases
"""    
print( aces_in_relation_e([x for x in range(1, 1230 + 1)]) == 1013400, aces_in_relation_e([x for x in range(1, 1230 + 1)])) # 1013400
print( aces_in_relation_e([x for x in range(1, 1753 + 1)]) == 2573509, aces_in_relation_e([x for x in range(1, 1753 + 1)])) # 2573509
print( aces_in_relation_e([x for x in range(1, 1114 + 1)]) == 741496,  aces_in_relation_e([x for x in range(1, 1114 + 1)])) # 741496
print( aces_in_relation_e([x for x in range(1, 1757 + 1)]) == 2587549, aces_in_relation_e([x for x in range(1, 1757 + 1)])) # 2587549
print( aces_in_relation_e([x for x in range(1, 1788 + 1)]) == 2697444, aces_in_relation_e([x for x in range(1, 1788 + 1)])) # 2697444
print( aces_in_relation_e([x for x in range(1, 1405 + 1)]) == 1474525, aces_in_relation_e([x for x in range(1, 1405 + 1)])) # 1474525
print( aces_in_relation_e([x for x in range(1, 1625 + 1)]) == 2141125, aces_in_relation_e([x for x in range(1, 1625 + 1)])) # 2141125
print( aces_in_relation_e([x for x in range(1, 1561 + 1)]) == 1937221, aces_in_relation_e([x for x in range(1, 1561 + 1)])) # 1937221

print(aces_in_relation_e([x for x in range(1, 1092 + 1)])) # 692964

"""
            