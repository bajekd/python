import unittest
from mobiles_emails_searcher import mobile_numbers_searcher, mails_searcher


class TestScript(unittest.TestCase):
    def test_phone_regex_matches(self):
        self.assertRegex('123-456.789', r'''(?x)            # allow to test regex with re.VERBOSE flag)
                                        (\+?\d{1,3})?       # country prefix, group 0
                                        (\s|-|\.)?          # separator, group 1
                                        (\d{3})             # first 3 digit, group 2
                                        (\s|-|\.)?          # separator, group 3
                                        (\d{3})             # middle 3 digit, group 4   
                                        (\s|-|\.)?          # separator, group 5
                                        (\d{3})             # last 3 digit, group 6     
                                        ''')
        self.assertRegex('+48 123-456.789', r"(\+?\d{1,3})?(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{3})")
        self.assertRegex('48123.456 789', r"(\+?\d{1,3})?(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{3})")

    def test_phone_regex_not_matches(self):
        self.assertNotRegex('+48 123 456 78', r"(\+?\d{1,3})?(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{3})(\s|-|\.)?(\d{3})")

    def test_mail_regex_matches(self):
        self.assertRegex('test@test.t-est.pl', r'''(?x)                 # allow to test regex with re.VERBOSE flag)
                                                [a-zA-Z0-9._%+-]+       # username
                                                @                       # @ symbol
                                                [a-zA-Z0-9.-]+          # domain name
                                                \.[a-zA-Z]{2,3}         # .top-lvl domain
                                                ''')

    def test_mail_regex_not_matches(self):
        self.assertNotRegex('test@test.t-est.p', r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,3}")

    def test_mobile_numbers_searcher(self):
        text = '''During the 1940s, as new and more powerful computing machines such as the Atanasoff–Berry computer and
                +31 333.333.333The world's first computer science degree program, the Cambridge Diploma in Computer
                Science,222-222-222began at the University of C'''
        results = mobile_numbers_searcher(text)
        self.assertListEqual(['+31 333 333 333', ' 222 222 222'], results)

    def test_mails_searcher(self):
        text = '''During the 1940s, as new and more powerful computing machines such as the Atanasoff–Berry computer and
                   have_a_nice_day@hello-world.in The world's first computer science degree program, the Cambridge
                   Diploma in Computer Science,testuser@testdomain.combegan at the University of C'''
        results = mails_searcher(text)

        self.assertListEqual(['have_a_nice_day@hello-world.in', 'testuser@testdomain.com'], results)


if __name__ == '__main__':
    unittest.main()




