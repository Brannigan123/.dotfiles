from libqtile.config import Key
from libqtile.lazy import lazy

def get_keybindings(mod: str) -> list[Key]:
    return [
        # Move window focus
        Key([mod], "Left", lazy.layout.left(), desc="Move focus to left"),
        Key([mod], "Right", lazy.layout.right(), desc="Move focus to right"),
        Key([mod], "Down", lazy.layout.down(), desc="Move focus down"),
        Key([mod], "Up", lazy.layout.up(), desc="Move focus up"),
        
        # Move windows around
        Key([mod, "shift"], "Left", lazy.layout.shuffle_left(), desc="Move window to the left"),
        Key([mod, "shift"], "Right", lazy.layout.shuffle_right(), desc="Move window to the right"),
        Key([mod, "shift"], "Down", lazy.layout.shuffle_down(), desc="Move window down"),
        Key([mod, "shift"], "Up", lazy.layout.shuffle_up(), desc="Move window up"),
        
        # Resize Windows
        Key([mod, "control"], "Left", lazy.layout.grow_left(), desc="Grow window to the left"),
        Key([mod, "control"], "Right", lazy.layout.grow_right(), desc="Grow window to the right"),
        Key([mod, "control"], "Down", lazy.layout.grow_down(), desc="Grow window down"),
        Key([mod, "control"], "Up", lazy.layout.grow_up(), desc="Grow window up"),
        Key([mod, "control"], "space", lazy.layout.normalize(), desc="Reset all window sizes"),
        
        # Toggle between different layouts
        Key([mod], "Tab", lazy.next_layout(), desc="Toggle between layouts"),
        Key([mod],"f",lazy.window.toggle_fullscreen(),desc="Toggle fullscreen on the focused window"),
        Key([mod], "t", lazy.window.toggle_floating(), desc="Toggle floating on the focused window"),
    ]