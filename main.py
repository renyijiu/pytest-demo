# coding=utf-8
import argparse

import pytest

from plugins import pytest_custom_plugin

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        prog='pytest-report',
        description='Use pytest to discover tests and generate a report',
        epilog='Text at the bottom of help')
    parser.add_argument('-o', '--output', required=True, type=str, help='the output report file to write to')
    args = parser.parse_args()

    if args.output is None:
        print("No Or Invalid output file specified")
        exit(1)

    pytest.main(["--collect-only", "-q"], plugins=[pytest_custom_plugin.CustomPlugin(args.output)])
    print "Save test report to: " + args.output
