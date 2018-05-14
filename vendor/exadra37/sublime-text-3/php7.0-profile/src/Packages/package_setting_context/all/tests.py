# -*- encoding: utf-8 -*-

"""
Quick tests to test the PackageSettingContext function.

To run them, paste

from package_setting_context.all.tests import main; main()

To reload the tests:

import imp, sys; imp.reload(sys.modules[main.__module__])

To reload the package_setting_context

import imp, sys; imp.reload(sys.modules['package_setting_context.all.package_setting_context'])

in the console, save this file, and the output's in the console!
"""

from .package_setting_context import get_setting
import sublime
import sys

class FakeSettings:

    """Only what's needed"""

    def __init__(self, data):
        self.data = data

    def get(self, key, default=None):
        return self.data.get(key, default)

def main():
    sys.stdout.write('----------------------------------------------\n')
    sys.stdout.write('| PackageSettingContext.tests: Running tests |\n')
    sys.stdout.write('----------------------------------------------\n')
    settings = FakeSettings({
        'first': False,
        'second': 4,
        'third': 'hello',
        'fourth': {
            'this': ['is', {
                'cool': ["right", "?"],
            }]
        },
        'strings': [
            'Hello world!',
            'Hello world',
            'this some sample text :)',
            'and guess what? This is too!'
        ]
    })

    tests = [
        ['package_settings.notice.the.s',                    sublime.OP_EQUAL,              True,                  None],
        ['package_setting.TestSetting.first',                sublime.OP_EQUAL,              False,                 True],
        ['package_setting.TestSetting.second',               sublime.OP_EQUAL,              4,                     True],
        ['package_setting.TestSetting.third',                sublime.OP_NOT_EQUAL,          None,                  True],
        ['package_setting.TestSetting.fourth',               sublime.OP_NOT_EQUAL,          {},                    True],
        ['package_setting.TestSetting.fourth.this.1.cool.1', sublime.OP_EQUAL,              '?',                   True],
        ['package_setting.TestSetting.strings.0',            sublime.OP_REGEX_MATCH,        r'([a-zA-Z]+[ !]){2}', True],
        ['package_setting.TestSetting.strings.1',            sublime.OP_NOT_REGEX_MATCH,    r'([a-zA-Z]+[ !]){2}', True],
        ['package_setting.TestSetting.strings.2',            sublime.OP_REGEX_CONTAINS,     r'is [A-Za-z ]+ sample\s', True],
        ['package_setting.TestSetting.strings.3',            sublime.OP_NOT_REGEX_CONTAINS, r'gu[aio]s{2}', True],
    ]

    for key, operand, operator, expected in tests:
        result = get_setting(key, operand, operator, test_settings=settings)
        if result != expected:
            sys.stdout.write("\nError: the key {!r} return {!r} instead of {!r}".format(key, result, expected))
    sys.stdout.write('\n')
