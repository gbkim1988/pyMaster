# python builtins library
import os
import sys
import hashlib
import json
import time
from itertools import cycle

# pypi library
import optparse
# import pprint # print well-organized data
from termcolor import colored, cprint  # print colored text into console
from virus_total_apis import ApiError, PublicApi, PrivateApi
from pymongo import MongoClient
from pprint import pprint

# user defined library
from binary_walker import file_to_strings  # transform binary file to string
from directory_walker import search_directory, get_file_list  # get certain file list

__description__ = 'Binary Harmless Check'
__author__ = 'gbkim1988@gmail.com'
__version__ = '0.0.1'
__date__ = '2017/06/27'

normalBold = lambda x: cprint(x, 'white', attrs=['bold'])
warningBold = lambda x: cprint(x, 'yellow', attrs=['bold'])
criticalBold = lambda x: cprint(x, 'red', attrs=['bold'])
messageBold = lambda x: cprint(x, 'green', attrs=['bold'])

normal = lambda x: cprint(x, 'white')
warning = lambda x: cprint(x, 'yellow')
critical = lambda x: cprint(x, 'red')
message = lambda x: cprint(x, 'green')

MONGODB_URI_SCHEME = 'mongodb://localhost:27017/'
MONGODB_HOST_PORT  = ('localhost', 27017)
MONGODB_DATABASE = 'PyVirusTotal'
MONGODB_COLLECTIONS = 'hash_scan_result'
MONGODB_SCAN_HISTORY = 'virustotal_scan_file_history'

BUF_SIZE = 65536

VIRUSTOTAL_ACCOUNT = [
        {'apikey':'019e873e55cd2ebcd6abaaf56e9567d76a7de2c16f1814633bcab65e08f97558', # account apikey
         'email':'stealhacker@naver.com', # account email address
         'valid':True # account validation check, default true
         },
        {'apikey':'cb7f89522d8cf3de33f53721715fb2967d3c81cf56942372d8609653993557ab',
         'email':'gbkim1988@gmail.com',
         'valid':True
         },
        {'apikey':'6a1d0013bc6765ad2ed112409aa5f1775a7c129b9a05a99e4b55bff5abe07a9f',
         'email':'gbkim1988@naver.com',
         'valid':True
         },
        {'apikey':'599939893f9be53ea33558fa97973319ab902170bfdfe81afc5a7c7a5008ee65',
         'email':'crazyhacks@naver.com',
         'valid':True
         },
        {'apikey':'128886fa32943dc5f9d4d0b574cbe7ae6f7029b384a650f147000e516cb3936b',
         'email':'gbkim@yes24.com',
         'valid':True
         },
    #
    ]

def binary_sha256(filename):
    sha256 = hashlib.sha256()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha256.update(data)
    return sha256.hexdigest()

def binary_sha1(filename):
    sha1 = hashlib.sha1()
    with open(filename, 'rb') as f:
        while True:
            data = f.read(BUF_SIZE)
            if not data:
                break
            sha1.update(data)
    return sha1.hexdigest()

def scan_virus_total(target_file_list):
    '''
    if there is no hash result, then do file upload
    :param filename: absolute file path, no exceptions
    :return: there is no return
    '''
    conn = MongoClient(MONGODB_URI_SCHEME)
    db = conn[MONGODB_DATABASE]
    collections = db[MONGODB_COLLECTIONS]
    history = db[MONGODB_SCAN_HISTORY]
    time_elapsed = [10, 15, 20, 30]
    time_elapsed_pool = cycle(time_elapsed)
    init_time_pool = cycle(time_elapsed)
    valid_account_list = list(filter(lambda x: x['valid'] == True, VIRUSTOTAL_ACCOUNT))
    account_number = len(valid_account_list)
    valid_account_pool = cycle(valid_account_list)
    counter = 0
    init = valid_account_list[-1]['apikey']
    for dir_path in target_file_list:
        for filename in target_file_list[dir_path]:
            sha1 = binary_sha1(filename)
            while True:
                apikey = next(valid_account_pool)['apikey']
                if init == apikey:
                    elapsed = next(init_time_pool)
                    messageBold("    wait for time elapsed (%d)" % elapsed)
                    time.sleep(elapsed)
                vt = PublicApi(apikey)
                resp = vt.get_file_report(sha1)
                resp_code = resp.get('response_code', -1)
                normalBold("# %s -> scan (%d)" % (filename, resp_code))
                if resp_code == 204:
                    # exceeded request rate limit (4 request / min)
                    epoch = next(time_elapsed_pool)
                    if epoch == 30:
                        criticalBold("there is no virustotal response")
                        break
                    messageBold("    Wait for time elapsed (%d)" % epoch)
                    time.sleep(epoch)
                    break
                elif resp_code == 200:
                    scan_report = resp.get('results')
                    scan_resp_code = scan_report.get('response_code')
                    if scan_resp_code == 1:
                        # pymongo code is here
                        resp['filename'] = filename
                        collections.insert(resp)
                        break
                    elif scan_resp_code == 0:
                        # pending, or has no data in virustotal, so that upload file
                        tmp = vt.scan_file(filename)
                        tmp['filename'] = filename
                        history.insert(tmp)
                        continue
                    elif scan_resp_code == -2:
                        warningBold("    Resource is pending for check")
                        pprint(resp)
                        break
                    else:
                        warningBold("    No Normal Response Code From VirusTotal ")
                        warningBold(json.dump(resp, sort_keys=True, indent=4))
                        break
                elif resp_code == -1:
                    # connection error
                    criticalBold('VirusTotal Response >>>>>>')
                    pprint(resp)
                    criticalBold('<<<<<<')
                    continue

                # add for trace
                resp['filepath'] = filename
            #

def get_virustotal_result(apikey, hash, filename=None):
    pass

def validate_virus_total_account():
    normal("<*> VirusTotal API KEY Validation")
    EICAR = "X5O!P%@AP[4\PZX54(P^)7CC)7}$EICAR-STANDARD-ANTIVIRUS-TEST-FILE!$H+H*".encode('utf-8')
    # EICAR_MD5 = hashlib.md5(EICAR).hexdigest()
    # EICAR_SHA1 = hashlib.sha1(EICAR).hexdigest()
    EICAR_SHA256 = hashlib.sha256(EICAR).hexdigest()
    for account in VIRUSTOTAL_ACCOUNT:
        vt = PublicApi(account['apikey'])
        try:
            vt_response = vt.get_file_report(EICAR_SHA256)
            normal("email : %s" % account['email'])
            normal("apikey : %s" % account['apikey'])
            if int(vt_response['response_code'] / 100) == 5:
                account['valid'] = False
                warning("valid : False")
                critical(vt_response['error'])
            elif int(vt_response['response_code'] / 100) == 4:
                account['valid'] = False
                warning("valid : False")
                critical(vt_response['error'])
            else:
                account['valid'] = True
                messageBold("valid : True")
        except:
            pass

def parse_args():
    oparser = optparse.OptionParser(usage="usage : %prog [options] [dirpath]\n" + __description__,
                                    version='%prog ' + __version__)
    oparser.add_option('-r', '--recursion', action='store_true', default=False,
                       help='recursive directory search')
    oparser.add_option('-s', '--search', type='string', default=False,
                       dest="search_pattern",
                       help='directory search regex pattern')
    oparser.add_option('-v', '--verbose', action='store_true', default=False,
                       help='verbose output with decoder errors')

    (options, args) = oparser.parse_args()

    if len(args) != 1:
        oparser.print_help()
        print('')
        print('  Source code has no copyright.')
        print('  @gbkim1988@gmail.com')
    return options, args

def main():
    (options, args) = parse_args()
    target_file_list = dict()
    validate_virus_total_account()
    if options.recursion:
        if options.search_pattern is None:
            target_file_list = search_directory(args[0])
        else:
            target_file_list = search_directory(args[0], options.search_pattern)
    else:
        target_file_list = get_file_list(args[0])

    scan_virus_total(target_file_list)

if __name__ == "__main__":
    main()
