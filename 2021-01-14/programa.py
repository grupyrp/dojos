import unittest


MAP = {
    "A": "2",
    "B": "2",
    "C": "2",
    "D": "3",
    "E": "3",
    "F": "3",
    "G": "4",
    "H": "4",
    "I": "4",
    "J": "5",
    "K": "5",
    "L": "5",
    "M": "6",
    "N": "6",
    "O": "6",
    "P": "7",
    "Q": "7",
    "R": "7",
    "S": "7",
    "T": "8",
    "U": "8",
    "V": "8",
    "W": "9",
    "X": "9",
    "Y": "9",
    "Z": "9"
}

NASA_MAP = (
            ("ABC","2"),
            ("DEF","3"),
            ("GHI","4"),
            ("JKL","5"),
            ("MNO","6"),
            ("PQRS","7"),
            ("TUV","8"),
            ("WXYZ","9")
)


def spaceX_text_to_number(text):
    phone_number = []

    for x in text:
        for letters, number in NASA_MAP:
            if x in letters:
                phone_number.append(number)
                break
        else:
            phone_number.append(x)

    return "".join(phone_number)

def nasa_text_to_number(text):
    phone_number = []

    for t in text:
        try:
            number = MAP[t]
        except KeyError:
            number = t
        phone_number.append(number)

    return "".join(phone_number)

def map_text_to_number(text):
    phone_number = ""

    for t in text:
        phone_number += MAP.get(t, t)
    return phone_number



class DojoTestCase(unittest.TestCase):
    def test_home_text_to_number(self):
        result = map_text_to_number("HOME")
        expected_result = "4663"

        self.assertEqual(result, expected_result)

    def test_abc(self):
        result = map_text_to_number("ABC")

        self.assertEqual(result, "222")

    def test_ab(self):
        result = map_text_to_number("AB")

        self.assertEqual(result, "22")

    def test_abd(self):
        result = map_text_to_number("ABD")

        self.assertEqual(result, "223")

    def test_abd(self):
        result = map_text_to_number("1-ABG")

        self.assertEqual(result, "1-224")

    def test_dojo1(self):
        result = map_text_to_number("1-HOME-SWEET-HOME ")
        self.assertEqual(result, "1-4663-79338-4663 ")


class DojoNasaTestCase(unittest.TestCase):
    def test_home_text_to_number(self):
        result = nasa_text_to_number("HOME")
        expected_result = "4663"

        self.assertEqual(result, expected_result)

    def test_abc(self):
        result = nasa_text_to_number("ABC")

        self.assertEqual(result, "222")

    def test_ab(self):
        result = nasa_text_to_number("AB")

        self.assertEqual(result, "22")

    def test_abd(self):
        result = nasa_text_to_number("ABD")

        self.assertEqual(result, "223")

    def test_abd(self):
        result = nasa_text_to_number("1-ABG")

        self.assertEqual(result, "1-224")

    def test_dojo1(self):
        result = nasa_text_to_number("1-HOME-SWEET-HOME ")
        self.assertEqual(result, "1-4663-79338-4663 ")

    def test_nasa_tuple(self):
        result = spaceX_text_to_number("1-HOME-SWEET-HOME ")
        self.assertEqual(result, "1-4663-79338-4663 ")


class DojoSpacexTupleTestCase(unittest.TestCase):
    def test_home_text_to_number(self):
        result = spaceX_text_to_number("HOME")
        expected_result = "4663"

        self.assertEqual(result, expected_result)

    def test_abc(self):
        result = spaceX_text_to_number("ABC")

        self.assertEqual(result, "222")

    def test_ab(self):
        result = spaceX_text_to_number("AB")

        self.assertEqual(result, "22")

    def test_abd(self):
        result = spaceX_text_to_number("ABD")

        self.assertEqual(result, "223")

    def test_abd(self):
        result = spaceX_text_to_number("1-ABG")

        self.assertEqual(result, "1-224")

    def test_dojo1(self):
        result = spaceX_text_to_number("1-HOME-SWEET-HOME ")
        self.assertEqual(result, "1-4663-79338-4663 ")

    def test_nasa_tuple(self):
        result = spaceX_text_to_number("1-HOME-SWEET-HOME ")
        self.assertEqual(result, "1-4663-79338-4663 ")

if __name__ == "__main__":
    unittest.main()



