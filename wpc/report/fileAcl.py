from wpc.acelist import AceList


# This is a bit like a file object, but we may be reporting only some of the ACEs from the DACL
class FileAcl:
    def __init__(self, f, a):
        self.acelist = None
        self.filename = None
        self.set_filename(f)
        self.set_acelist(a)

    def set_acelist(self, aces):
        self.acelist = AceList()
        for ace in aces:
            self.acelist.add(ace)

    def set_filename(self, f):
        self.filename = f

    def get_filename(self):
        return self.filename

    def get_acelist(self):
        return self.acelist

    def as_text(self):
        t = ''
        for ace in self.get_acelist().get_aces():
            t += self.get_filename() + ":\n  " + ace.as_text() + "\n"
        return t

    # TODO owner?
