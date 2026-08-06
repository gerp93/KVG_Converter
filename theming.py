"""Applies VisualAssault (https://github.com/gerp93/VisualAssault) color
themes to the RTF to PDF Converter's Tkinter UI.

Unlike KVGrainy (mostly ttk widgets), this app's UI is built from plain
tk widgets (Frame/Label/Entry/Button), so theming here walks the widget
tree and configures each widget's own background/foreground options
directly instead of going through ttk.Style.
"""
import tkinter as tk
from tkinter import ttk

from visual_assault_tkinter import THEMES

THEME_NAMES = {theme_id: data["name"] for theme_id, data in THEMES.items()}
DEFAULT_LABEL = "System Default"

_defaults = {"widgets": [], "ttk_theme": None}

# Options to snapshot/restore, per widget class. Anything a widget doesn't
# actually support is skipped via the try/except in _get/_set below.
_TRACKED_OPTIONS = ("background", "foreground", "activebackground", "activeforeground", "insertbackground")


def _walk(widget):
    yield widget
    for child in widget.winfo_children():
        yield from _walk(child)


def _get(widget, option):
    try:
        return widget.cget(option)
    except tk.TclError:
        return None


def capture_defaults(root: tk.Misc) -> None:
    """Snapshot the native look before any theme is applied, so 'System
    Default' can restore it exactly. Call once, after the full UI (including
    all menus) has been built."""
    widgets = []
    for widget in _walk(root):
        values = {opt: _get(widget, opt) for opt in _TRACKED_OPTIONS}
        values = {opt: val for opt, val in values.items() if val is not None}
        widgets.append((widget, values))
    _defaults["widgets"] = widgets
    _defaults["ttk_theme"] = ttk.Style(root).theme_use()


def _theme_values_for(widget, theme: dict) -> dict:
    """Map a widget's supported options to theme colors, by widget class."""
    if isinstance(widget, tk.Menu):
        return {
            "background": theme["surface"],
            "foreground": theme["foreground"],
            "activebackground": theme["buttonHover"],
            "activeforeground": theme["foreground"],
        }
    if isinstance(widget, tk.Entry):
        return {
            "background": theme["surface"],
            "foreground": theme["foreground"],
            "insertbackground": theme["foreground"],
        }
    if isinstance(widget, tk.Button):
        return {
            "background": theme["buttonBackground"],
            "foreground": theme["foreground"],
            "activebackground": theme["buttonHover"],
            "activeforeground": theme["foreground"],
        }
    if isinstance(widget, (tk.Frame, tk.Label, tk.Tk, tk.Toplevel)):
        return {"background": theme["background"], "foreground": theme["foreground"]}
    return {}


def apply_theme(root: tk.Misc, theme_id) -> None:
    """Apply a VisualAssault theme by id, or pass None to restore the
    defaults captured by capture_defaults()."""
    if theme_id is None:
        for widget, values in _defaults["widgets"]:
            for option, value in values.items():
                try:
                    widget.configure(**{option: value})
                except tk.TclError:
                    pass
        ttk.Style(root).theme_use(_defaults["ttk_theme"])
        return

    theme = THEMES[theme_id]
    for widget, _ in _defaults["widgets"]:
        for option, value in _theme_values_for(widget, theme).items():
            try:
                widget.configure(**{option: value})
            except tk.TclError:
                pass

    style = ttk.Style(root)
    style.theme_use("clam")
    style.configure(
        "TProgressbar",
        background=theme["accentBlue"],
        troughcolor=theme["surface"],
        bordercolor=theme["border"],
    )
