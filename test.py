import urllib2
import lxml.html
import unittest
import main

class Test(unittest.TestCase):
    
    def test(self):
        content = main.getCachedPage()
        got = main.pageToListNames(content)
        wanted = ['alumni',
 'announce',
 'barnraising',
 'board',
 'bpw-staff',
 'campus-amherst-staff',
 'campus-announce',
 'campus-berkeley-staff',
 'campus-boston-summer-staff',
 'campus-chicago-staff',
 'campus-columbia-staff',
 'campus-cornell-staff',
 'campus-gmu-staff',
 'campus-harvard-staff',
 'campus-iub-staff',
 'campus-jhu-staff',
 'campus-morris-staff',
 'campus-neiu-staff',
 'campus-osu-staff',
 'campus-portland-staff',
 'campus-princeton-staff',
 'campus-purdue-staff',
 'campus-rpi-staff',
 'campus-rutgers-staff',
 'campus-uiuc-staff',
 'campus-uofa-staff',
 'campus-wellesley-staff',
 'ccsf-campus-staff',
 'cpw-staff',
 'devel',
 'discuss',
 'events',
 'foss-outreach-la',
 'fundraising-2014',
 'greenhouse',
 'hba-django-planning',
 'monitoring',
 'monitoring-private',
 'mpw-staff',
 'npw-staff',
 'openadvice',
 'openadvice-announce',
 'osctc-planning',
 'pdxpw-staff',
 'pedagogy',
 'peers',
 'penn',
 'phlpw-staff',
 'publicity',
 'pydata-outreach-staff',
 'wfs-india',
 'wmf-outreach-staff']
        self.assertEqual(wanted, got)
    	
if __name__ == "__main__":
    unittest.main()
