from typing import TypeVar, Sequence

T = TypeVar('T')


def get_first_item(l: Sequence[T]) -> T:
    return l[0]


print(get_first_item([1, 2, 3, 4]))
print(get_first_item((2.0, 3.0, 4.0)))
print(get_first_item('ABC'))
