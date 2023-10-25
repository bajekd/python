import re

import pyperclip


def mobile_numbers_searcher(text):
    mobile_regex = re.compile(r'''
        (\+?\d{1,3})?  # country prefix, group 0
        (\s|-|\.)?     # separator, group 1
        (\d{3})        # first 3 digit, group 2
        (\s|-|\.)?     # separator, group 3
        (\d{3})        # middle 3 digit, group 4
        (\s|-|\.)?     # separator, group 5
        (\d{3})        # last 3 digit, group 6
    ''', re.X)
    mobile_numbers = []

    for groups in mobile_regex.findall(text):
        mobile_number = ' '.join([groups[0], groups[2], groups[4], groups[6]])
        mobile_numbers.append(mobile_number)

    if len(mobile_numbers) <= 0:
        print('No mobile numbers found!')

    return mobile_numbers


def mails_searcher(text):
    mail_regex = re.compile(r'''
        [a-zA-Z0-9._%+-]+  # username
        @                  # @ symbol
        [a-zA-Z0-9.-]+     # domain name
        \.[a-zA-Z]{2,3}    # .top-lvl domain
    ''', re.X)
    mails = []

    for mail in mail_regex.findall(text):
        mails.append(mail)

    if len(mails) <= 0:
        print('No email addresses found!')

    return mails


def print_results(numbers, emails):
    results = numbers + emails
    pyperclip.copy('\n'.join(results))
    print('Copied to clipboard!')


text_to_filter = str(pyperclip.paste())

mobile_numbers = mobile_numbers_searcher(text_to_filter)
mails = mails_searcher(text_to_filter)
print_results(mobile_numbers, mails)
