"""FrankenUI Playground Example built with MonsterUI (original design by ShadCN)"""

from fasthtml.common import *
from monsterui.all import *
from fasthtml.svg import *

app, rt = fast_app(hdrs=Theme.blue.headers())

preset_options = ["Grammatical Standard English", "Summarize for a 2nd grader",
        "Text to command","Q&A","English to other languages","Parse unstructured data",
        "Classification","Natural language to Python","Explain code","Chat","More examples"]

def playground_navbar():
    save_modal = Modal(
        ModalTitle("Save preset"),
        P("This will save the current playground state as a preset which you can access later or share with others.",cls=("mt-1.5", TextPresets.muted_sm)),
        LabelInput("Name",        id="name"), 
        LabelInput("Description", id="description"),
        ModalCloseButton("Save", cls=ButtonT.primary),
        id="save")
    
    share_dd = Div(cls="space-y-6 p-4")(
        H3("Share preset"),
        P("Anyone who has this link and an OpenAI account will be able to view this.", cls=TextPresets.muted_sm),
        Div(Input(value="https://platform.openai.com/playground/p/7bbKYQvsVkNmVb8NGcdUOLae?model=text-davinci-003", readonly=True),
            Button(UkIcon('copy'), cls=(ButtonT.primary, "uk-drop-close",'mt-4'))))

    rnav = Div(
        UkSelect(*Options(*preset_options), name='preset', optgroup_label="Examples",
                 placeholder='Load a preset', searchable=True, cls='h-9 w-[200px] lg:w-[300px]'),
        Button("Save",         cls=ButtonT.secondary, data_uk_toggle="#save"),save_modal,
        Button("View Code",    cls=ButtonT.secondary),
        Button("Share",        cls=ButtonT.secondary),DropDownNavContainer(share_dd),
        Button(UkIcon(icon="ellipsis"), cls=ButtonT.secondary),
        DropDownNavContainer(
            Li(A("Content filter preferences")),
            NavDividerLi(),
            Li(A("Delete preset", cls="text-destructive")),
        uk_dropdown="mode: click"))
    
    return NavBar(title=H4('Playground'),nav_links=rnav)

rsidebar = NavContainer(
    UkSelect(
        Optgroup(map(Option,("text-davinci-003", "text-curie-001", "text-babbage-001", "text-ada-001")),label='GPT-3'),
        Optgroup(map(Option,("code-davinci-002", "code-cushman-001")),label='Codex'),
        label="Model",
        searchable=True),
    LabelRange(label='Temperature'),
    LabelRange(label='Maximum Length'),
    LabelRange(label='Top P'),
    cls='space-y-6 mt-8')

@rt
def index(): 
    navbar = playground_navbar()
    main_content = Div(
        Div(cls="flex-1")(
            Textarea(cls="uk-textarea h-full p-4", placeholder="Write a tagline for an ice cream shop")),
            cls="flex h-[700px] p-8 w-4/5")
    
    bottom_buttons = Div(
        Button("Submit", cls=ButtonT.primary),
        Button(UkIcon(icon="history"), cls=ButtonT.secondary),
        cls="flex gap-x-2")
    
    return Title("Playground Example"),Div(navbar, Div(cls="flex w-full")(main_content, rsidebar), bottom_buttons)

serve()
