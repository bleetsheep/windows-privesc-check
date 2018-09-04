from wpc.drive import Drive
import win32api
import win32con
import win32file


class Drives(object):
    def get_fixed_drives(self):
        for d in win32api.GetLogicalDriveStrings().split("\x00")[0:-1]:
            if win32file.GetDriveType(d) == win32con.DRIVE_FIXED or win32file.GetDriveType(d) == 4:
                yield Drive(d)
