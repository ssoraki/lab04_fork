def count_common_elements(*lists):
    element_count = {}

    for list in lists:
        for element in list:
            element_count[element] = element_count.get(element, 0) + 1
    common_elements = {elem: count for elem, count in element_count.items() if count == len(lists)}
    return common_elements


if __name__ == "__main__":
    list1 = [1, 2, 3, 4]
    list2 = [2, 3, 4, 5]
    list3 = [3, 4, 5, 6]

    result = count_common_elements(list1, list2, list3)
    print("Общие элементы:", *result)