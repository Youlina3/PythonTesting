# Write a function that provides change directory (cd) function for an abstract file system.

# Notes:

# Root path is '/'.
# Path separator is '/'.
# Parent directory is addressable as '..'.
# Directory names consist only of English alphabet letters (A-Z and a-z).
# The function should support both relative and absolute paths.
# The function will not be passed any invalid paths.
# Do not use built-in path-related functions.
# For example:

# path = Path('/a/b/c/d')
# path.cd('../x')
# print(path.current_path)
# should display '/a/b/c/x'.

class Path:
    def __init__(self, path):
        self.current_path = path

    def cd(self, new_path):
        split_curr = self.current_path.split('/')
        split_new = new_path.split('/')
        
        if split_new[0] == '':
            self.current_path = new_path
        
        for m in split_new:
            if m != '..':
                split_curr.append(m)
            else:
                split_curr.pop()
        self.current_path = '/'.join([m for m in split_curr])
            
           

path = Path('/a/b/c/d')
path.cd('e/h')
print(path.current_path)#current_path要改成

