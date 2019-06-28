#!/usr/bin/env python

#import subprocess
import time
from ctypes import CDLL
import ChoubsLogging


choubs_logger = ChoubsLogging.myLogger("walking_reminder")
logger = choubs_logger.get_logger()

# loginPF = CDLL('/System/Library/PrivateFrameworks/
# login.framework/Versions/Current/login')
# result = loginPF.SACLockScreenImmediate()

if __name__ == "__main__":
    logger.info("sleep...")
    time.sleep(60)
    logger.info("wake up...")
    '''
    subprocess.call('/System/Library/CoreServices/Menu\ Extras/
    User.menu/Contents/Resources/CGSession -suspend', shell=True)
    '''
    loginPF = CDLL('/System/Library/PrivateFrameworks/login.framework/Versions/Current/login')
    result = loginPF.SACLockScreenImmediate()
    logger.info("Lock screen result: {}".format(result))
    logger.info("Locked...")