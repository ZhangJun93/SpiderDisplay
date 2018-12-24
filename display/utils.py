from display.forms import collection_name_list

def find_collectin_name(name):
    for i in collection_name_list:
        if i[0] == name:
            return i[1]

if __name__ == "__main__":
    print(find_collectin_name("tzjz_spider"))