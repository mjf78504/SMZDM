# -*- coding: utf-8 -*-
"""
#  main.py
Description :
@Author     : Jianfeng
@Date       : 2018/3/11
@Software   : PyCharm
"""

import os
import sys
import time
from apps.SMZDMApp import SmzdmAPP

SMZDMsess = os.getenv('SMZDM_sess')


def smzdmCheckin():
    content_SMZDM = SmzdmAPP().smzdm(SMZDMsess)
    content_SMZDM = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()) + 'SMZDM签到：\n' + content_SMZDM
    return content_SMZDM

if __name__=='__main__':
    try:
        msg = smzdmCheckin()
        exitCode = 0
    except Exception as e:
        print('Error: ' + msg)
        exitCode = 1

    sys.exit(exitCode)