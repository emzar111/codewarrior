
def unique_in_order(iterable):
    result = []
    iterable = list(iterable)
    if iterable:
        result.append(iterable[0])
        for i in iterable:
            if result[-1] != i:
                result += i
        return result
    return result


