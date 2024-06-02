from qtile_extras import bar, layout, widget
from qtile_extras.widget.decorations import RectDecoration
from qtile_extras.widget import modify
from libqtile.config import Group, Match, Screen
from libqtile.utils import guess_terminal

from keybindings import get_keybindings
from mousebindings import get_mouse_bindings
from colorscheme import get_colors

from bars.widgets.appname import AppName

import os

mod = "mod4"
terminal = guess_terminal()

groups = [Group(i) for i in "123456789"]

keys = get_keybindings(mod, terminal, groups)
mouse = get_mouse_bindings(mod)

colors = get_colors()

floating_layout = layout.Floating(
    border_focus=colors[2],
    border_normal=colors[7],
    border_width=2,
    float_rules=[
        # Run the utility of `xprop` to see the wm class and name of an X client.
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(title="branchdialog"),  # gitk
        Match(title="pinentry"),  # GPG key password entry
    ]
)

layouts = [
    layout.Bsp(border_focus=colors[2], border_normal=colors[7], border_width=2, margin=2),
    layout.MonadTall(border_focus=colors[2], border_normal=colors[7], border_width=2, margin=2),
    layout.RatioTile(border_focus=colors[2], border_normal=colors[7], border_width=2, margin=2),
    floating_layout,
    layout.Zoomy(margin=2),
]

widget_defaults = dict(
    font="JetBrains Mono NL Medium",
    fontsize=12,
    padding=8
)
extension_defaults = widget_defaults.copy()

rounded_decoration = RectDecoration(
    group=True,
    use_widget_background=True,
    radius=4,
    filled=True,
)

spacer0 = widget.Spacer(background="#000000.00")
spacer1 = widget.Spacer(background="#000000.00", length=8)

with open(os.path.expanduser("~/.cache/wal/wal")) as f:
    wallpaper = os.path.expanduser(f.read().strip())
 
screens = [
    Screen( 
        wallpaper=wallpaper,
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                modify(
                    AppName,
                    font="Font Awesome 6 Brands Regular",
                    default_name=' Desktop ',
                    fmt=' {} ',
                    format='{name}',
                    foreground=colors[0],
                    background=colors[4],
                    decorations=[rounded_decoration],
                ),
                spacer1,
                widget.GlobalMenu(
                    foreground=colors[0],
                    background=colors[1],
                    decorations=[rounded_decoration],
                    menu_background=colors[0],
                    menu_foreground=colors[7],
                    menu_foreground_disabled = colors[6],
                    separator_colour=colors[6],
                    menu_border=colors[7],
                    menu_border_width=1,
                ),
                spacer1, 
                widget.CurrentLayoutIcon(
                    foreground=colors[0],
                    background=colors[2],
                    use_mask=True,
                    scale=0.65,
                    decorations=[rounded_decoration],
                ),
                spacer0,
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                widget.StatusNotifier(),
                # widget.Systray(
                #     foreground=colors[7],
                #     decorations=[rounded_decoration],
                #     padding=10,
                # ),
                spacer1,
                widget.GroupBox(
                    foreground=colors[6],
                    background=colors[0],
                    active=colors[1],
                    inactive=colors[7],
                    block_highlight_text_color=colors[0],
                    this_current_screen_border=colors[6],
                    highlight_method="block",
                    decorations=[rounded_decoration],
                    padding=3,
                ),
                spacer1,
                widget.PulseVolume(
                    foreground=colors[4],
                    background=colors[0],
                    decorations=[rounded_decoration],
                ),
                widget.Visualiser(
                    channels="stereo",
                    bar_colour=colors[4],
                    background=colors[0],
                    decorations=[rounded_decoration],
                    bar_height=12,
                    width=55,
                ),
                spacer1,
                widget.Clock(
                    font="Symbols Nerd Font Mono",
                    format="%d.%m.%Y  ⏽  %H:%M:%S",
                    foreground=colors[7],
                    background=colors[0],
                    decorations=[rounded_decoration],
                ),
                spacer1,
                widget.QuickExit(
                    font="Symbols Nerd Font Mono",
                    default_text=' ⏻ ',
                    foreground=colors[0],
                    background=colors[2],
                    decorations=[rounded_decoration],
                ),
            ],
            28,
            margin=[8, 8, 10, 8],
            background="#000000.00",
        ),
    ),
]


dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None

# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
