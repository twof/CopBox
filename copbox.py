"""Called with a file path. Moves the file to a new folder, registers
apple script watchers
"""


import argparse, os, random

parser = argparse.ArgumentParser(description='Relocate a file')

parser.add_argument('-random_location', action='store_true')
parser.add_argument('--relocate_file', type=str)


def choose_random_location():
    return random_walk(os.path.expanduser('~/'), random.randint(1, 10))

def is_blacklisted(path):
    if path.startswith('.'):
        return True
    if path == 'Applications':
        return True
    if '.app' in path:
        return True
    return False

def random_walk(path, remaining_depth):
    if remaining_depth == 0:
        return path
    paths = os.listdir(path)
    paths = [p for p in paths if not is_blacklisted(p)]
    paths = [os.path.join(path, p) for p in paths]
    paths = [p for p in paths if os.path.isdir(p)]    
    if len(paths) == 0:
        return path
    nextdir = random.choice(paths)
    return random_walk(nextdir, remaining_depth - 1)

def relocate_file_locally(path):
    new_path = os.path.join(choose_random_location(),
                            os.path.split(path)[-1])
    print('Old path: %s, new path: %s' %(path, new_path))
    os.rename(path, new_path)
    os.system(f"/usr/bin/osascript /Users/fnord/Documents/AppleScript/CopBox/CLArguments.scpt {os.path.split(new_path)[0]} /Users/fnord/Documents/AppleScript/CopBox/CLFolderAction.scpt")

def relocate_file_remotely(path):
    raise NotImplementedError

def relocate_file(path):
    remote_file_threshhold = 0.1
#    if random.random() < remote_file_threshhold:
#        relocate_file_remotely(path)
#    else:
    relocate_file_locally(path)
    

if __name__ == '__main__':
    args = parser.parse_args()
    if args.random_location:
        print(choose_random_location())
    if args.relocate_file:
        relocate_file(args.relocate_file)

    
    
