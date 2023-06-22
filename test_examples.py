class TestExample:
    def test_check_math(self):
        a=3
        b=5
        assert a+b==8

    def test_check_math2(self):
        a=3
        b=11
        exp = 16
        assert a+b==exp, f"Sum of a and b is not {exp}"

