# coding=utf-8

import cal


class TestPrint(object):
    def test_right_print(self):
        assert "Hi, PyCharm" == cal.print_hi("PyCharm")

    def test_wrong_print(self):
        assert "Hi, PyCharm" != cal.print_hi("Hello")

    def test_answer(self):
        assert cal.inc(3) == 5
