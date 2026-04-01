def first_bad(versions, bad):
    # call is_bad to determine if a version is bad
    # assuming version list is in order (sorted)
    first, last = 1, len(versions) - 1
    bad_version = None
    while first <= last:
        midpoint = (first + last) // 2 # calc mid point using integer division
        if is_bad(versions[midpoint]):
            last = midpoint - 1
            bad_version = versions[midpoint]
        else:
            first = midpoint + 1

    return bad_version

def is_bad(x):
    return True