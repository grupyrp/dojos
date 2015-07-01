
with open('input.txt', 'r') as input_f:
    input_str = input_f.read()


def test_store():
    store = Store(10, [2, 4])
    assert store.credit == 10
    assert store.items == [2, 4]


def test_parser():
    parsed = parse_input(input_str) 
    assert isinstance(parsed, list)
    assert isinstance(parsed[0], Store)


class Store:
    def __init__(self, credit, items):
        self.credit = credit
        self.items = items
  
def parse_input(input_str):
    input_list = input_str.split('\n)')
    for i, line in enumerate(input_str.split('\n')[1::3]):
        c = i 
