from ftplib import FTP
import tarfile
import os
import shutil

ftp = FTP('ted.europa.eu')
ftp.login('guest', 'guest')
ftp.cwd('/daily-packages/2020/11')

daily_list = ftp.nlst()
current_list = os.listdir('/Users/jamssheaton/PycharmProjects/MVP/ted_data')
def diff(list1, list2):
  return (list(list(set(list1) - set(list2)) + list(set(list2) - set(list1))))

t = diff(current_list, daily_list)
t.pop(0)
print(t)

def download(file):
  for x in file:
    with open(x, 'wb') as f:
      ftp.retrbinary('RETR ' + x, f.write)
      print('downloaded ' + x)
      shutil.move(x, 'ted_data')
  else:
    print('you have all of the documents')


def unpack(file):
  for v in file:
    tar = tarfile.open(f'ted_data/{v}')
    tar.extractall('ted_data')
    print('unpacked ' + v)

def delete(file):
  for d in file:
    os.remove(f'ted_data/{d}')
    print(f'deleted {d}')


download(daily_list)


unpack(daily_list)


delete(daily_list)
