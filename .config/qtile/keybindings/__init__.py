from libqtile.config import Group, Key

import keybindings.workspace as ws
import keybindings.windows as win
import keybindings.applications as apps

def get_keybindings(mod: str, terminal: str,groups: list[Group]) -> list[Key]:
    return [
        *ws.get_keybindings(mod, groups),
        *win.get_keybindings(mod),
        *apps.get_keybindings(mod, terminal)
    ]