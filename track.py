import os
import sys
import shutil
import subprocess
import update_links



def track():
    # initialize variables
    dotfiles_local_repo_path = os.path.expanduser("~/.dotfiles")
    include_list_filepath = os.path.join(dotfiles_local_repo_path, ".include")
    
    if len(sys.argv) > 1:
        with open(include_list_filepath, "a") as include_list_file:
            for rel_path in sys.argv[1:]:
                symbol_path = os.path.join(os.path.expanduser("~"), rel_path)
                if os.path.exists(symbol_path):
                    include_list_file.write(f"{rel_path}\n")
                    target_path = os.path.join(dotfiles_local_repo_path, rel_path)
                    if os.path.realpath(symbol_path) == target_path: continue
                    if os.path.lexists(target_path):
                        if os.path.isfile(target_path) or os.path.islink(target_path):
                            os.remove(target_path)
                        elif os.path.isdir(target_path):
                            shutil.rmtree(target_path)
                    print(f"Copying {symbol_path} -> {target_path}")
                    shutil.copytree(symbol_path, target_path)
                    
        update_links.update_links()
                
                    
if __name__ == "__main__":
    track()