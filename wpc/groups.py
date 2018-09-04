from __future__ import print_function
import win32net
import pywintypes
import wpc.conf
from wpc.group import Group


class Groups(object):
    def __init__(self):
        self.groups = []

    # TODO need to call with level GROUP_INFO_3.  This will get SID and save the slow call to LookupAccountName.
    def get_all(self):
        if not self.groups:
            try:
                level = 0
                resume = 0
                while True:
                    grouplist, total, resume = win32net.NetGroupEnum(wpc.conf.remote_server, level, resume, 999999)
                    for u in grouplist:
                        try:
                            sid, name, type = wpc.conf.cache.LookupAccountName(wpc.conf.remote_server, u['name'])
                            self.groups.append(Group(sid))
                        except:
                            print("[E] failed to lookup sid of %s" % Group['name'])
                    if resume == 0:
                        break
            except pywintypes.error as e:
                print("[E] %s: %s" % (e[1], e[2]))
            try:
                level = 0
                resume = 0
                while True:
                    grouplist, total, resume = win32net.NetLocalGroupEnum(wpc.conf.remote_server, level, resume, 999999)
                    for u in grouplist:
                        try:
                            sid, name, type = wpc.conf.cache.LookupAccountName(wpc.conf.remote_server, u['name'])
                            self.groups.append(Group(sid))
                        except:
                            print("[E] failed to lookup sid of %s" % Group['name'])
                    if resume == 0:
                        break
            except pywintypes.error as e:
                print("[E] %s: %s" % (e[1], e[2]))
        return self.groups
