#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
test-virustotal-api
~~~~~~~~~~~~
This module tests the VirusTotal API.
:copyright: (c) 2014 by Josh "blacktop" Maine.
:license: GPLv3, see LICENSE for more details.
"""

from __future__ import print_function

import hashlib
import json
from unittest import TestCase

from virus_total_apis import ApiError, PublicApi

# I created an account to get this API Key for test purposes, please get your own.
API_KEY = '2539516d471d7beb6b28a720d7a25024edc0f7590d345fc747418645002ac47b'

EICAR = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*".encode('utf-8')

EICAR_MD5 = hashlib.md5(EICAR).hexdigest()
EICAR_SHA1 = hashlib.sha1(EICAR).hexdigest()
EICAR_SHA256 = hashlib.sha256(EICAR).hexdigest()


class InitTests(TestCase):

    def test_hash_found(self):
        vt = PublicApi(API_KEY)

        try:
            print(json.dumps(vt.get_file_report('8E7FF6FDA061B782446A5968D43AE32DAF4FAE65'), sort_keys=False, indent=4))
        except Exception as e:
            self.fail(e)

    def test_md5_hash(self):
        vt = PublicApi(API_KEY)

        try:
            print(json.dumps(vt.get_file_report(EICAR_MD5), sort_keys=False, indent=4))
        except Exception as e:
            self.fail(e)

    def test_sha1_hash(self):
        vt = PublicApi(API_KEY)

        try:
            print(json.dumps(vt.get_file_report(EICAR_SHA1), sort_keys=False, indent=4))
        except Exception as e:
            self.fail(e)

    def test_sha256_hash(self):
        vt = PublicApi(API_KEY)

        try:
            print(json.dumps(vt.get_file_report(EICAR_SHA256), sort_keys=False, indent=4))
        except Exception as e:
            self.fail(e)

    def test_hash_not_found(self):
        vt = PublicApi(API_KEY)

        try:
            print(json.dumps(vt.get_file_report('A' * 32), sort_keys=False, indent=4))
        except Exception as e:
            self.fail(e)

    def test_hash_bad_input(self):
        vt = PublicApi(API_KEY)

        try:
            print(json.dumps(vt.get_file_report('This is not a hash'), sort_keys=False, indent=4))
            print(json.dumps(vt.get_file_report(None), sort_keys=False, indent=4))
            print(json.dumps(vt.get_file_report(False), sort_keys=False, indent=4))
            print(json.dumps(vt.get_file_report(-1), sort_keys=False, indent=4))
        except Exception as e:
            self.fail(e)

    def test_bad_creds(self):
        try:
            vt_error = PublicApi()
        except ApiError:
            pass
        else:
            self.fail("Should have raised an ApiError")

    def test_scan_file_binary(self):
        vt = PublicApi(API_KEY)
        vt.scan_file()
        try:
            print(json.dumps(vt.scan_file('virus_total_apis/test/test.exe'), sort_keys=False, indent=4))
        except Exception as e:
            self.fail(e)

    def test_scan_file_binary_filename(self):
        vt = PublicApi(API_KEY)

        try:
            print(json.dumps(
                vt.scan_file('C:\\Users\\YES24\\Desktop\\자료정리\\분류전\\cmd.exe',
                             filename='othertest.exe'),
                sort_keys=False,
                indent=4))
        except Exception as e:
            self.fail(e)

    def test_scan_file_stream(self):
        vt = PublicApi(API_KEY)

        try:
            print(json.dumps(vt.scan_file(EICAR, from_disk=False), sort_keys=False, indent=4))
        except Exception as e:
            self.fail(e)

    def test_scan_file_stream_filename(self):
        vt = PublicApi(API_KEY)

        try:
            print(json.dumps(
                vt.scan_file(EICAR,
                             from_disk=False,
                             filename='my_eicar_file.txt'),
                sort_keys=False,
                indent=4))
        except Exception as e:
            self.fail(e)

    def test_scan_url(self):
        vt = PublicApi(API_KEY)

        try:
            print(json.dumps(vt.scan_url('www.wired.com'), sort_keys=False, indent=4))
        except Exception as e:
            self.fail(e)

    def test_get_url_report(self):
        vt = PublicApi(API_KEY)

        try:
            print(json.dumps(vt.get_url_report('www.wired.com'), sort_keys=False, indent=4))
        except Exception as e:
            self.fail(e)

    def test_get_domain_report(self):
        vt = PublicApi(API_KEY)

        try:
            print(json.dumps(vt.get_domain_report('www.wired.com'), sort_keys=False, indent=4))
        except Exception as e:
            self.fail(e)

    def test_get_ip_report(self):
        vt = PublicApi(API_KEY)

        try:
            print(json.dumps(vt.get_ip_report('23.6.113.133'), sort_keys=False, indent=4))
        except Exception as e:
            self.fail(e)

    def test_rescan_file(self):
        vt = PublicApi(API_KEY)

        try:
            print(json.dumps(vt.rescan_file(EICAR_MD5), sort_keys=False, indent=4))
        except Exception as e:
            self.fail(e)

    def test_put_comments(self):
        vt = PublicApi(API_KEY)
        comment = 'This is just a test of the virus-total-api. https://github.com/blacktop/virustotal-api'
        try:
            print(json.dumps(vt.put_comments(resource=EICAR_MD5, comment=comment), sort_keys=False, indent=4))
        except Exception as e:
            self.fail(e)