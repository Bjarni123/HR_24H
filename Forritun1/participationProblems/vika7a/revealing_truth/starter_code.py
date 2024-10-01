from typing import List, Tuple


def list_to_bool_tuple(a_list: List[str]) -> Tuple[bool]:
    """Returns a tuple with each element in the list converted to bool.

    First converts any integers to int.
    """
    final_list = []
    for element in a_list:
        try:
            final_list.append(bool(int(element)))
        except:
            final_list.append(bool(element))

    return tuple(final_list)