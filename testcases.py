import unittest
import gitparser

class TestGitParser(unittest.TestCase):

    org , n , m = "google",5 ,6
    org1 , n1 , m1 = "facebook",3,5


    def test_google(self):
        gitparser.get_repos(self.org,self.n,self.m)

    def test_facebook(self):
        gitparser.get_repos(self.org1,self.n1,self.m1)

if __name__ == '__main__':
    unittest.main()