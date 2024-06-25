from libqtile import bar
from qtile_extras import layout, widget
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

groups = [Group(name=g[0], label=g[1]) for g in zip("123456789", "⓵⓶⓷⓸⓹⓺⓻⓼⓽")]

keys = get_keybindings(mod, terminal, groups)
mouse = get_mouse_bindings(mod)

colors = get_colors()

TRANSLUCENT_HEX = f"{colors[0]}.40"

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
    fontsize=10,
    padding=8
)
extension_defaults = widget_defaults.copy()

rounded_decoration = RectDecoration(
    group=True,
    use_widget_background=True,
    radius=10,
    padding_y=6,
    filled=True,
)

spacer0 = widget.Spacer(background=TRANSLUCENT_HEX)
spacer1 = widget.Spacer(background=TRANSLUCENT_HEX, length=8)

with open(os.path.expanduser("~/.cache/wal/wal")) as f:
    wallpaper = os.path.expanduser(f.read().strip())
 
screens = [
    Screen( 
        wallpaper=wallpaper,
        wallpaper_mode='fill',
        top=bar.Bar(
            [
                spacer1,
                modify(
                    AppName,
                    font="Font Awesome 6 Brands Regular",
                    fontsize=10,
                    default_name='Desktop',
                    fmt='{}',
                    format='{name}',
                    foreground=colors[7],
                    background=f'{colors[6]}.20',
                    decorations=[rounded_decoration],
                ),
                spacer1,
                widget.GlobalMenu(
                    foreground=colors[7],
                    background=f'{colors[6]}.20',
                    decorations=[rounded_decoration],
                    menu_background=colors[0],
                    menu_foreground=colors[7],
                    menu_foreground_disabled = colors[6],
                    separator_colour=colors[6],
                    menu_border=colors[7],
                    menu_border_width=1,
                ),
                spacer0,
                # NB Systray is incompatible with Wayland, consider using StatusNotifier instead
                # widget.StatusNotifier(),
                # widget.Systray(
                #     foreground=colors[7],
                #     decorations=[rounded_decoration],
                #     padding=10,
                # ),
                spacer1,
                widget.GroupBox(
                    fontsize=12,
                    background=f'{colors[6]}.20',
                    active=f'{colors[4]}.90',
                    inactive=colors[7],
                    block_highlight_text_color=colors[1],
                    this_current_screen_border=f'{colors[6]}.00',
                    highlight_method="block",
                    decorations=[rounded_decoration],
                    padding=0,
                ),
                spacer0,
                widget.PulseVolume(
                    foreground=colors[7],
                    background=colors[0],
                    decorations=[rounded_decoration],
                ),
                widget.Visualiser(
                    channels="stereo",
                    bar_colour=f'{colors[7]}.60',
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
                widget.CurrentLayoutIcon(
                    foreground=colors[7],
                    background=colors[0],
                    use_mask=True,
                    scale=0.4,
                    decorations=[rounded_decoration],
                ),
                spacer1,
                widget.QuickExit(
                    font="Symbols Nerd Font Mono",
                    default_text=' ⏻ ',
                    foreground=colors[7],
                    background=f'{colors[6]}.20',
                    decorations=[rounded_decoration],
                ),
                spacer1,
            ],
            36,
            margin=[0, 0, 10, 0],
            background=TRANSLUCENT_HEX,
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
