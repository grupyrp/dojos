
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
    assert parsed[0].items == [5, 75, 25]

def test_number_cases():
    number_cases = int(input_str.split('\n')[0])
    parsed = parse_input(input_str)
    assert number_cases == len(parsed)

def test_

class Store:
    def __init__(self, credit, items):
        self.credit = credit
        self.items = items
  
def parse_input(input_str):
    input_list = input_str.split('\n')
    number_cases = int(input_list.pop(0))
    store_list = []
    for j in range(number_cases):
        credit = int(input_list.pop(0))
        n_items = int(input_list.pop(0))
        items = map(int, input_list.pop(0).split())

        store_list.append(Store(credit, items))

    return store_list
        
