# Tests for cine.py

import os
from datetime import datetime
import unittest
import nose
import numpy as np
import pims
import pims.cine

tests_path, _ = os.path.split(os.path.abspath(__file__))

class _common_cine_sample_tests(object):
    """Test the .cine reader on a sample file."""
    def setUp(self):
        self.cin = pims.open(self.sample_filename, **self.options)

    def tearDown(self):
        self.cin.close()

    def test_type(self):
        assert isinstance(self.cin, pims.cine.Cine)

    def test_metadata_smoke(self):
        assert len(self.cin)
        assert self.cin.frame_rate
        assert len(self.cin.frame_shape) == 2


class test_legacy_cine_sample(_common_cine_sample_tests, unittest.TestCase):
    def setUp(self):
        self.sample_filename = os.path.join(tests_path, 'data',
                                            'cine_legacy.cine')
        if not os.path.exists(self.sample_filename):
            raise nose.SkipTest('Legacy sample cine file not found. '
                                'Skipping.')

        self.options = {}
        super(test_legacy_cine_sample, self).setUp()

    def test_length(self):
        assert len(self.cin) == 97


# class test_new_cine_sample(_common_cine_sample_tests, unittest.TestCase):
#     """Tests for the newer format only"""
#     def setUp(self):
#         self.sample_filename = os.path.join(tests_path, 'data',
#                                             'cine_xxxx.cin')
#         if not os.path.exists(self.sample_filename):
#             raise nose.SkipTest('Newer sample cine file not found. '
#                                 'Skipping.')
#         super(test_new_cine_sample, self).setUp()
#
#     def test_new_file_info(self):
#         """Tests based on the specific file in the repo."""
#         c = self.cin
#         pass



