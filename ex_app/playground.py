# AUTOGENERATED! DO NOT EDIT! File to edit: ../ex_nbs/07_playground.ipynb.

# %% auto 0
__all__ = ['playground_homepage', 'playground_navbar', 'page']

# %% ../ex_nbs/07_playground.ipynb 1
from fasthtml.common import *
from fasthtml.components import Uk
from fh_frankenui.components import *
from fasthtml.components import Uk_icon
from fasthtml.svg import *
from fh_matplotlib import matplotlib2fasthtml
import numpy as np
from pathlib import Path
import matplotlib.pylab as plt

# %% ../ex_nbs/07_playground.ipynb 8
from fasthtml.common import *
from fh_frankenui.components import *

def playground_navbar():
    preset_options = [
        "Grammatical Standard English",
        "Summarize for a 2nd grader",
        "Text to command",
        "Q&A",
        "English to other languages",
        "Parse unstructured data",
        "Classification",
        "Natural language to Python",
        "Explain code",
        "Chat",
        "More examples"
    ]
    
    preset_select = UkSelect(
        *Options(preset_options),
        cls="h-9 w-[200px] lg:w-[300px]",
        name="preset",
        placeholder="Load a preset",
        searchable=True
    )
    
    save_modal = Modal(
        UkInput(label="Name", id="name"),
        UkInput(label="Description", id="description"),
        header=UkModalTitle("Save preset",
            P("This will save the current playground state as a preset which you can access later or share with others.",
              cls=("mt-1.5", TextT.muted_sm))),
        footer=UkButton("Save", cls=(UkButtonT.primary, "uk-modal-close")),
        id="save"
    )
    
    save_button = UkButton("Save", cls=UkButtonT.secondary, uk_toggle="#save")
    view_code_button = UkButton("View Code", cls=UkButtonT.secondary, uk_toggle="#demo")
    
    share_dropdown = Div(
        H3("Share preset", cls="text-lg font-semibold"),
        P("Anyone who has this link and an OpenAI account will be able to view this.", cls=("mt-1.5", TextT.muted_sm)),
        Div(
            UkInput(value="https://platform.openai.com/playground/p/7bbKYQvsVkNmVb8NGcdUOLae?model=text-davinci-003", readonly=True, cls="flex-1"),
            UkButton(Span(uk_icon="icon: copy"), cls=(UkButtonT.primary, "uk-drop-close"), uk_toggle="#demo"),
            cls="flex items-center space-x-2 pt-4"
        ),
        cls="uk-drop uk-dropdown w-[520px] p-4",
        uk_drop="mode: click; pos: bottom-right;"
    )
    
    share_button = UkButton("Share", cls=UkButtonT.secondary)
    
    more_options_dropdown = Div(
        Ul(cls="uk-dropdown-nav")(
            Li(A("Content filter preferences", cls="uk-drop-close", href="#demo", uk_toggle=True)),
            Li(cls="uk-nav-divider"),
            Li(A("Delete preset", cls="uk-drop-close text-destructive", href="#demo", uk_toggle=True))
        ),
        cls="uk-drop uk-dropdown",
        uk_drop="mode: click; pos: bottom-right"
    )
    
    more_options_button = UkButton(Span(uk_icon="icon: more"), cls=UkButtonT.secondary)
    
    navbar = Div(
        H2("Playground", cls="text-lg font-semibold"),
        Div(
            preset_select,
            save_button,
            save_modal,
            view_code_button,
            share_button,
            share_dropdown,
            more_options_button,
            more_options_dropdown,
            cls="flex w-full flex-1 items-center justify-end space-x-2"
        ),
        cls="flex h-16 items-center justify-between border-b border-border px-8 py-4"
    )
    
    return navbar

# Example usage:
# playground_navbar()

# %% ../ex_nbs/07_playground.ipynb 10
from fasthtml.common import *
from fh_frankenui.components import *

def page():
    navbar = playground_navbar()
    
    main_content = Div(
        Div(
            Textarea(
                cls="uk-textarea h-full p-4",
                placeholder="Write a tagline for an ice cream shop",
                readonly=True
            ),
            cls="flex-1"
        ),
        Div(cls="w-[200px] flex-none"),
        cls="flex h-[700px] gap-x-6 px-8 py-6"
    )
    
    bottom_buttons = Div(
        UkButton("Submit", cls=UkButtonT.primary, uk_toggle="#demo"),
        UkButton(Uk_icon(icon="history"), cls=UkButtonT.secondary, uk_toggle="#demo"),
        cls="flex gap-x-2 px-8 py-6 pt-0"
    )
    
    return Div(
        navbar,
        main_content,
        bottom_buttons
    )

# %% ../ex_nbs/07_playground.ipynb 11
playground_homepage = page()