import os
import uuid
import shutil


def update_links():
    # initialize variables
    dotfiles_local_repo_path = os.path.expanduser("~/.dotfiles")
    include_list_filepath = os.path.join(dotfiles_local_repo_path, ".include")
    include_list = []

    # read .include file if it exists
    if os.path.exists(include_list_filepath):
        with open(include_list_filepath) as include_list_file:
            include_list = include_list_file.read().splitlines()

    # loop through all files listed in .include file
    for file in include_list:
        target = os.path.join(dotfiles_local_repo_path, file)
        symbol =  os.path.join(os.path.expanduser("~"), file)
        if os.path.exists(target):
            if os.path.lexists(symbol) :
                if os.path.realpath(symbol) == target: continue
                print(f"Updating symbolic link: {symbol} -> {target}")
                tmp_link = f"{symbol}-tmp-{uuid.uuid4().hex}"
                backup = f"{symbol}-backup-{uuid.uuid4().hex}"
                os.symlink(target, tmp_link)
                os.rename(symbol, backup)
                try:
                    os.rename(tmp_link, symbol)
                except:
                    os.rename(backup, symbol)
                if os.path.isfile(backup) or os.path.islink(backup):
                    os.remove(backup)
                elif os.path.isdir(backup):
                    shutil.rmtree(backup)
            else:
                print(f"Creating symbolic link: {symbol} -> {target}")
                print(os.path.exists(symbol))
                os.symlink(target, symbol)
                
                
if __name__ == "__main__":                
    update_links()