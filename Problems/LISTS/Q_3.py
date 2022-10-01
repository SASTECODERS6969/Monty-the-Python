#WAP TO CHECK IF A PARTICULAR ELEMENT EXISTS IN A LIST
def element_checker(element, list):
    for i in list:
        if i == element:
            print(element, "exists in the List")
            break
        else:
            print(element, "Does not exist in the List")

element_checker(23, [34, 456, 645, "YajnanaHD", 23, 45])