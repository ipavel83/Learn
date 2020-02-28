from collections import Counter

def is_list_a_contains_list_b(main, sub):
    cMain = Counter(main)
    cSub = Counter(sub)
    cMain.subtract(cSub)
    for i in cMain.values():
        if i<0:
            return False
    return True


if __name__=='__main__':
    assert is_list_a_contains_list_b([], [])
    assert is_list_a_contains_list_b([1,2,3], [])
    assert is_list_a_contains_list_b([1,2,3], [3,2])
    assert is_list_a_contains_list_b([1,2,3,2], [2,2])
    assert not is_list_a_contains_list_b([1], [2])
    assert not is_list_a_contains_list_b([1,2,3], [2,3,2])
    
    print("all asserts ok")
    