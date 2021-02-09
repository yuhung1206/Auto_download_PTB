# download PTB file( .mat, .info, .html)
# coding=utf-8

# Codes are partly combined from https://blog.csdn.net/fengzhizi76506/article/details/59229846
#   and https://www.edureka.co/community/31707/how-do-i-use-urllib-to-see-if-a-website-is-404-or-200-in-python

import os
import urllib.request

# -----initialization----- #
save_directory = r"your_storing_path"  # specified storing path


# -----defined 'cbk' function----- #
def cbk(a, b, c):
    per = 100.0 * a * b / c
    if per > 100:
        per = 100
    print
    '%.2f%%' % per
# --------------end--------------- #

# -----read RECORDS.txt(store filename of all records)----- #
# change directory & Get RECORDS.txt
if not os.path.exists(save_directory):
    os.makedirs(save_directory)
os.chdir(save_directory)  # change directory to save_directory
dir = os.path.abspath('.')
url = 'https://archive.physionet.org/physiobank/database/ptbdb/RECORDS'
work_path = os.path.join(dir, 'RECORDS.txt')
urllib.request.urlretrieve(url, work_path, cbk)
# --------------end--------------- #

# -----read RECORDS.txt----- #
f = open("RECORDS.txt", "r")
Data0 = []
Data1 = []
for lines in f.readlines():
    tempData = ""
    tempData = lines.rstrip()  # delete"\n"
    tempData = tempData.split("/")
    Data0.append(tempData[0])  # Patient Num
    Data1.append(tempData[1])  # Record Num => 549 files
f.close()
# print(Data1)

def auto_down(url_func, path):
    try:
        urllib.request.urlretrieve(url_func, path)
    except urllib.error.ContentTooShortError:  # urllib.error.URLError as e:
        print('Network conditions is not good.Reloading.')
        auto_down(url_func, path)  # Try again !!!!

# ----------------------end---------------------- #

# download ".hea file"
url_seg1 = 'https://archive.physionet.org/atm/ptbdb/'
url_seg2 = '/0/e/export/matlab/'
url_seg3 = 'm.hea'
url_seg4 = 'm.info'
url_seg5 = 'm.mat'


# for i in [25]:
for i in range(len(Data0)):
    # create directory
    dir = os.path.abspath('.')
    work_path = os.path.join(dir, Data0[i])
    if not os.path.exists(work_path):
        os.makedirs(work_path)
    print("Create dir:" + work_path)

    # produce url
    patientURL = url_seg1 + Data0[i] + '/' + Data1[i] + url_seg2 + Data1[i] + url_seg3
    # 'https://archive.physionet.org/atm/ptbdb/patient001/s0010_re/0/e/export/matlab/s0010_rem.hea'
    url_Info = url_seg1 + Data0[i] + '/' + Data1[i] + url_seg2 + Data1[i] + url_seg4
    # 'https://archive.physionet.org/atm/ptbdb/patient001/s0010_re/0/e/export/matlab/s0010_rem.info'
    url_Mat = url_seg1 + Data0[i] + '/' + Data1[i] + url_seg2 + Data1[i] + url_seg5
    # 'https://archive.physionet.org/atm/ptbdb/patient001/s0010_re/0/e/export/matlab/s0010_rem.mat'

    # print connection state (e.g. 200, 404, 501...)
    try:
        conn = urllib.request.urlopen(url_Info)
    except urllib.error.HTTPError as e:
        # Return code error (e.g. 404, 501, ...)
        # ...
        print('HTTPError: {}'.format(e.code))
        continue
    except urllib.error.URLError as e:
        # Not an HTTP-specific error (e.g. connection refused)
        # ...
        continue
        print('URLError: {}'.format(e.reason))
    else:
        # 200
        # ...
        print('good connection for .info')
    try:
        conn = urllib.request.urlopen(url_Mat)
    except urllib.error.HTTPError as e:
        # Return code error (e.g. 404, 501, ...)
        # ...
        print('HTTPError: {}'.format(e.code))
        continue
    except urllib.error.URLError as e:
        # Not an HTTP-specific error (e.g. connection refused)
        # ...
        continue
        print('URLError: {}'.format(e.reason))
    else:
        # 200
        # ...
        print('good connection for .mat')

    # e.g. url = 'https://archive.physionet.org/atm/ptbdb/patient021/s0073lre/0/e/export/matlab/s0073lrem.hea'

    print(patientURL)
    dir = os.path.abspath('.')
    HeaName = Data1[i] + '.txt'
    work_path = os.path.join(dir, Data0[i])
    work_path = os.path.join(work_path, HeaName)
    urllib.request.urlretrieve(patientURL, work_path, cbk) #download .hea file
    print('Get .hea_' + str(i))
    # read patient.txt [e.g. s0073lrem.txt]
    file = open(work_path, "r")
    temp = file.readlines()
    file.close()

    # -----download MI .info file to certain directory-----#
    url_Info = url_seg1 + Data0[i] + '/' + Data1[i] + url_seg2 + Data1[i] + url_seg4
    print(url_Info)
    # e.g. url = 'https://archive.physionet.org/atm/ptbdb/patient021/s0073lre/0/10/export/matlab/s0073lrem.info'
    dir = os.path.abspath('.')
    InfoFile = Data1[i] + url_seg4  # filename of .info檔
    work_path = os.path.join(dir, Data0[i])
    work_path = os.path.join(work_path, InfoFile)
    print(work_path)
    urllib.request.urlretrieve(url_Info, work_path, cbk)
    print('Get .info_' + str(i))
    # -----download Patient ".mat file" to certain directory-----#
    url_Mat = url_seg1 + Data0[i] + '/' + Data1[i] + url_seg2 + Data1[i] + url_seg5
    print(url_Mat)
    # e.g. url = 'https://archive.physionet.org/atm/ptbdb/patient021/s0073lre/0/10/export/matlab/s0073lrem.mat'
    dir = os.path.abspath('.')
    MatFile = Data1[i] + url_seg5  # filename of .info檔
    work_path = os.path.join(dir, Data0[i])
    work_path = os.path.join(work_path, MatFile)
    print(work_path)
    auto_down(url_Mat, work_path)
    # urllib.request.urlretrieve(url_Mat, work_path, cbk)
    print('Get .mat_' + str(i))


