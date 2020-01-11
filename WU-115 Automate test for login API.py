from unittest import TestCase
import unittest
print('WU-115 Automate test for login API')
class TestStringMethods(unittest.TestCase):
    def test_me(self):
        # import requetss 
        url = 'https://api.worldunited.com/dev/auth/login'
        data = '''{"email" : "mjkpzarf@grr.la", "password": "Password123"}'''
        headers = {'Content-Type': 'application/json'}
        response = requests.post(url, data=data, headers=headers)
        self.assertTrue(response.headers.get('Access-Control-Allow-Origin'),'*')
if __name__ == '__main__':
    unittest.main()