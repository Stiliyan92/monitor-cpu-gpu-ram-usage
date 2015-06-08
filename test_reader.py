import unittest

from proc_read import ProcReader

class TestPC(unittest.TestCase):

    def setUp(self):
        self.pr = ProcReader()

    def test_get_meminfo_returns_dict(self):
        self.assertIsInstance(self.pr.get_meminfo(), dict)

    def test_get_cpuinfo_returns_dict(self):
        self.assertIsInstance(self.pr.get_cpuinfo(), dict)

if __name__ == '__main__':
    unittest.main()
