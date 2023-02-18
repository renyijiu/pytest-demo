# coding=utf-8
import json


class CustomPlugin:
    def __init__(self, output_file):
        self.tests = []
        self.output_file = output_file

    def pytest_report_collectionfinish(self, items):
        for item in items:
            self.tests.append(item.nodeid)
        open(self.output_file, "w+").write(json.dumps(self.tests))
