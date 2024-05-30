from libqtile import qtile
from libqtile.config import Group, Key
from libqtile.lazy import lazy

def get_keybindings(mod: str, groups: list[Group]) -> list[Key]:
    keys:list[Group] = []
    
    for i in groups:
        keys.extend([
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod1 + shift + group number = move focused window to group
            Key(
                [mod, "shift"],
                i.name, 
                lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name),
            ),
            # mod + ctrl + group number = move focused window to group and switch to group
            Key(
                [mod, "control"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
        ]) 
    
    # Add key bindings to switch VTs in Wayland.
    for vt in range(1, 8):
        keys.append(
            Key(
                ["control", "mod1"],
                f"f{vt}",
                lazy.core.change_vt(vt).when(func=lambda: qtile.core.name == "wayland"),
                desc=f"Switch to VT{vt}",
            )
        )
        
    return keys