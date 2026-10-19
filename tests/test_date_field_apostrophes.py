import os
import unittest

from mailmerge import MailMerge


class DateFieldApostrophesTest(unittest.TestCase):
    """
    A non-merge field whose instruction has unbalanced quotes, e.g. DATE \\@"MMMM d', 'yyyy",
    must not prevent the document from loading.
    """

    def setUp(self):
        self.path = os.path.dirname(__file__)

    def test_date_field_with_apostrophes(self):
        with MailMerge(os.path.join(self.path, "test_date_field_apostrophes.docx")) as document:
            self.assertEqual(document.get_merge_fields(), {"ENAM", "DNAML"})
