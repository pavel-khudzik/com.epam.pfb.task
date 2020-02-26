import unittest
import tagcounter.utils.dbapi as db
from tagcounter.utils.siteprocessing import log_site, get_tag_count

class TestTagcounter(unittest.TestCase):

    def test_log(self):
        """
        Function tests logging of site's name with datetime
            format of record: YYYY-MM-DD HH-MI-SS,MIS SITE_NAME
        """
        test_site = 'test.tst'
        log_site(test_site)
        with open('tagcounter.log', 'r') as f:
            ln = f.readline()

        self.assertEqual(test_site, ln.split()[2])

    def test_tag_count(self):
        """
        Function tests counting of tags on site
            base function return dictionary: tag_name: count
        """
        test_site = '<html><header>some header 1</header><header>some header 2</header></html>'
        test_dict = {'html': 1, 'header': 2}
        get_tag_count(test_site)

        self.assertEqual(test_dict, get_tag_count(test_site))

    def test_db(self):
        """
        Function tests saving record and read it in/from DB
            record structure: second domain | url | date of check | tags info
        """

        test_rec = ('second_domain', 'url', '2020-02-02', 'tags_info')
        db.drop_table()
        db.add_record(test_rec)

        self.assertEqual(test_rec, db.select_table('url')[0])


if __name__ == '__main__':
    unittest.main()
