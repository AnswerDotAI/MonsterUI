# AUTOGENERATED! DO NOT EDIT! File to edit: ../nbs/03_daisy.ipynb.

# %% auto 0
__all__ = ['AlertT', 'Alert', 'StepsT', 'StepT', 'Steps', 'LiStep', 'ToastHT', 'ToastVT', 'Toast']

# %% ../nbs/03_daisy.ipynb
import fasthtml.common as fh
from .foundations import *
from fasthtml.common import is_listy, Div, P, Span, Script, FastHTML, FT, to_xml, show,fast_app
from fasthtml.svg import *
from fasthtml.components import Uk_theme_switcher, Main
from enum import Enum, auto
from fasthtml.components import Uk_select,Uk_input_tag,Uk_icon
from functools import partial
from itertools import zip_longest
from typing import Union, Tuple, Optional
from fastcore.all import *
import copy, re, httpx
from pathlib import Path

# %% ../nbs/03_daisy.ipynb
class AlertT(VEnum):
    "Alert styles"
    def _generate_next_value_(name, start, count, last_values): return f"alert-{name}"
    info = auto()
    success = auto()
    warning = auto()
    error = auto()

# %% ../nbs/03_daisy.ipynb
def Alert(*c, cls='', **kwargs):
    "Alert informs users about important events."
    return Div(Span(*c), cls=('alert', stringify(cls)), role='alert', **kwargs)

# %% ../nbs/03_daisy.ipynb
class StepsT(VEnum):
    "Options for Steps"
    def _generate_next_value_(name, start, count, last_values): return f'steps-{name}'
    vertical = auto()
    horizonal = auto()

# %% ../nbs/03_daisy.ipynb
class StepT(VEnum):
    'Step styles for LiStep'
    def _generate_next_value_(name, start, count, last_values): return f'step-{name}'
    primary = auto()
    secondary = auto()
    accent = auto() 
    info = auto()
    success = auto()
    warning = auto()
    error = auto()
    neutral = auto()

# %% ../nbs/03_daisy.ipynb
def Steps(*li, cls='', **kwargs):
    "Creates a steps container with horizontal scrolling"
    return Ul(*li, cls=('steps',stringify(cls)), **kwargs)

def LiStep(*c, cls='', **kwargs):
    "Creates a step list item with optional styling"
    """<li data-content="?" class="step step-neutral">Step 1</li>"""
    return Li(*c, cls=('step', stringify(cls)), **kwargs)

# %% ../nbs/03_daisy.ipynb
class ToastHT(VEnum):
    "Horizontal position for Toast"
    def _generate_next_value_(name, start, count, last_values): return f'toast-{name}'
    start = auto()
    center = auto()
    end = auto()

class ToastVT(VEnum):
    "Vertical position for Toast"
    def _generate_next_value_(name, start, count, last_values): return f'toast-{name}'
    top = auto()
    middle = auto()
    bottom = auto()

# %% ../nbs/03_daisy.ipynb
def Toast(*c, cls='', alert_cls='', **kwargs):
    "Toasts are stacked announcements, positioned on the corner of page."
    a = Alert(*c, cls=alert_cls)
    return Div(a, cls=('toast', stringify(cls)), **kwargs)