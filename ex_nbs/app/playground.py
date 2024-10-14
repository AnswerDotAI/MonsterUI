# AUTOGENERATED! DO NOT EDIT! File to edit: ../ex_nbs/07_playground.ipynb.

# %% auto 0
__all__ = ['preset_options', 'playground_homepage', 'playground_navbar', 'page']

# %% ../ex_nbs/07_playground.ipynb
from fasthtml.common import *
from fasthtml.components import Uk
from fh_frankenui import *
from fasthtml.components import Uk_icon
from fasthtml.svg import *
from fh_matplotlib import matplotlib2fasthtml
import numpy as np
from pathlib import Path
import matplotlib.pylab as plt

# %% ../ex_nbs/07_playground.ipynb
preset_options = ["Grammatical Standard English", "Summarize for a 2nd grader",
        "Text to command","Q&A","English to other languages","Parse unstructured data",
        "Classification","Natural language to Python","Explain code","Chat","More examples"]

# %% ../ex_nbs/07_playground.ipynb
def playground_navbar():
    save_modal = Modal(
        ModalTitle("Save preset"),
        P("This will save the current playground state as a preset which you can access later or share with others.",cls=("mt-1.5", TextFont.muted_sm)),
        LabelInput("Name", id="name"), 
        LabelInput("Description", id="description"),
        ModalCloseButton("Save", cls=(ButtonT.primary)),
        id="save")
    
    share_dd = Div(cls="space-y-6")(
        H3("Share preset"),
        P("Anyone who has this link and an OpenAI account will be able to view this.", cls=TextFont.muted_sm),
        Div(cls='flex space-x-2')(
            Input(value="https://platform.openai.com/playground/p/7bbKYQvsVkNmVb8NGcdUOLae?model=text-davinci-003", readonly=True, cls="flex-1"),
            Button(UkIcon('copy'), cls=(ButtonT.primary, "uk-drop-close"))))#flex items-center space-x-2 pt-4 bbmx-6 my-6

    rnav = Div(cls='flex items-center space-x-2')(
        Select(*Options(*preset_options), name='preset', optgroup_label="Examples",
                 placeholder='Load a preset', searchable=True, cls='h-9 w-[200px] lg:w-[300px]'),
        Button("Save", cls=ButtonT.secondary, uk_toggle="#save"),
        save_modal,
        Button("View Code", cls=ButtonT.secondary),
        UkDropdownButton(share_dd,label="Share", btn_cls=ButtonT.secondary,dd_cls='p-6'),
        UkDropdownButton(A("Content filter preferences", href="#demo"), 
                         None, # divider
                         A("Delete preset", cls="text-destructive", href="#demo"),
            label=UkIcon('ellipsis'), btn_cls=ButtonT.secondary,))
    
    return UkNavbar(lnav=H4('Playground'),rnav=rnav,cls='p-2')

# %% ../ex_nbs/07_playground.ipynb
def page():
    navbar = playground_navbar()
    
    main_content = Div(
        Div(cls="flex-1")(Textarea(cls="uk-textarea h-full p-4", placeholder="Write a tagline for an ice cream shop",readonly=True),),
        Div(cls="w-[200px] flex-none"),
        cls="flex h-[700px] gap-x-6 px-8 py-6")
    
    bottom_buttons = Div(
        Button("Submit", cls=ButtonT.primary, uk_toggle="#demo"),
        Button(UkIcon(icon="history"), cls=ButtonT.secondary, uk_toggle="#demo"),
        cls="flex gap-x-2 px-8 py-6 pt-0")
    
    return Div(navbar, main_content, bottom_buttons)

# %% ../ex_nbs/07_playground.ipynb
playground_homepage = page()