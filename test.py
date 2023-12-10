import lib


def test_count_common_elements():
    list1 = [1, 2, 3, 4]
    list2 = [2, 3, 4, 5]
    list3 = [3, 4, 5, 6]

    result = lib.count_common_elements(list1, list2, list3)
    print("Общие элементы:", *result)


test_count_common_elements()