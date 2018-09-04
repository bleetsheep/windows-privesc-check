from wpc.file import File as File


class Files(object):
    def __init__(self):
        self.files = []
    
    # for wpc.file objects, not strings
    def add(self, file):
        self.files.append(file)
        
    def add_by_name(self, name):
        f = File(name)
        self.add(f) 
    
    def get_names(self):
        return map(lambda x: x.name, self.get_files())

    def get_files(self):
        return self.files

    def get_files_by_path(self, ext):
        # TODO
        pass
    
    def get_files_by_extension(self, exts):
        # TODO
        pass
    
    def get_files_writable_by_user(self, users):
        # TODO
        pass
    
    def get_files_writable_by_all_except(self, users):
        # TODO
        pass
