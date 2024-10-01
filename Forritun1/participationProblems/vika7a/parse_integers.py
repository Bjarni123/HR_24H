
def list_to_int_tuple(search_list):
    list_final = []

    for x in search_list:
        try:
            integer = int(x)
            list_final.append(integer)
        except:
            pass

    return (tuple(list_final))