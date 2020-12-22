import paramiko as paramiko
import cv2
import paramiko as pm
import datetime as dt
import os
import stat
import sys
import json

client = paramiko.SSHClient()

host_ip = '172.22.64.12'
port = 22
username = 'lab'
password = '123.com'

client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client.connect(host_ip, port, username, password, timeout=500)
sftp_client = client.open_sftp()

# 获取transport传输实例, sftp服务器 ip + 端口号
tran = pm.Transport((host_ip, port))
# 连接ssh服务器, user + password
tran.connect(username='lab', password='123.com')
# 获取sftp实例
sftp = pm.SFTPClient.from_transport(tran)


def getRemoteFiles(remoteDir):
    # 加载sftp服务器文件对象(根目录)
    filesAttr = sftp.listdir_attr(remoteDir)

    try:
        # foreach遍历
        for fileAttr in filesAttr:
            # # 文件最后修改时间, 精确到天yyyymmdd
            # file_dt = dt.datetime.fromtimestamp(
            #     fileAttr.st_mtime).strftime('%Y%m%d')
            # # 判断该文件是否在下载时间范围内, 昨天零点=< dt < 今天零点
            # if file_dt >= yesterday and file_dt < today:
            # 判断是否为目录
            if stat.S_ISDIR(fileAttr.st_mode):
                # 1.当是文件夹时
                # 计算子文件夹在ftp服务器上的路径
                son_remoteDir = remoteDir + '/' + fileAttr.filename
                # 生成器, 迭代调用函数自身
                yield from getRemoteFiles(son_remoteDir)
            else:
                # 2.当是文件时
                # 生成器, 添加"路径+文件名"到迭代器"
                yield remoteDir + '/' + fileAttr.filename
    except Exception as e:
        print('getAllFilePath exception:', e)


# json_home = '/APP/zmj/test_sftp/json'
# json_files = getRemoteFiles(json_home)
#
# for file in json_files:
#     remote_file = sftp_client.open(file,'r+')
#     print(file)
#     with open(os.path.join('D:/work_source/test_env/sftp/output', os.path.basename(file)), 'w') as wf:
#         for l in remote_file:
#             wf.write(l.strip('\n'))
#             print(l.strip("\n"))



img_home = '/APP/zmj/test_sftp/img'
img_files = getRemoteFiles(img_home)
for img in img_files:
    remote_file = sftp_client.open(img, 'r+')
    print(img)
    for s in remote_file:
        print(s)