from libqtile.config import Key
from libqtile.lazy import lazy

import os

def get_keybindings(mod: str, terminal: str) -> list[Key]:
    home_dir = os.path.expanduser("~")
    
    return [
        Key([mod], "q", lazy.window.kill(), desc="Kill focused window"),
        Key([mod, "control"], "r", lazy.reload_config(), desc="Reload the config"),
        Key([mod, "control"], "q", lazy.shutdown(), desc="Shutdown Qtile"),
        
        Key([mod], "r", lazy.spawncmd(), desc="Spawn a command using a prompt widget"),
        
        Key([mod], "Return", lazy.spawn(terminal), desc="Launch terminal"),
        Key([mod], "space", lazy.spawn("ulauncher"), desc="Open Application Launcher"),
        
        Key([], "Print", lazy.spawn(f"scrot -s '{home_dir}/Pictures/Screenshots/Screenshot %Y-%m-%d %H_%M_%S.png'"), desc="Take a screenshot"),
    ]