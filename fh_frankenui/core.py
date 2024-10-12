"""The building blocks to the UI"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../lib_nbs/01_core.ipynb.

# %% auto 0
__all__ = ['ButtonT', 'ContainerT', 'LabelT', 'LinkT', 'PaddingT', 'PositionT', 'SectionT', 'TextT', 'FlexT', 'GridT', 'CardT',
           'TableT', 'stringify', 'str2ukcls', 'VEnum', 'create_uk_enum', 'UkGenericComponent', 'Button', 'H1', 'H2',
           'H3', 'H4', 'Alert', 'Article', 'ArticleTitle', 'ArticleMeta', 'Container', 'Input', 'Select', 'Radio',
           'CheckboxX', 'Range', 'Toggle_switch', 'TextArea', 'Switch', 'Label', 'FormLabel', 'Link', 'List',
           'ModalContainer', 'ModalDialog', 'ModalHeader', 'ModalBody', 'ModalFooter', 'ModalTitle', 'ModalCloseButton',
           'Modal', 'Nav', 'NavBarContainer', 'NavBarNav', 'Placeholder', 'Progress', 'Section', 'Sticky', 'Theme',
           'TextFont', 'UkIcon', 'DiceBearAvatar', 'Grid', 'ResponsiveGrid', 'FullySpacedDiv', 'CenteredDiv',
           'LAlignedDiv', 'RAlignedDiv', 'VStackedDiv', 'HStackedDiv', 'SpaceBetweenDiv', 'GenericLabelInput',
           'LabelInput', 'LabelRadio', 'LabelCheckboxX', 'LabelRange', 'LabelToggle_switch', 'LabelTextArea',
           'LabelSwitch', 'LabelSelect', 'UkIconButton', 'Options', 'UkSelect', 'UkDropdownButton', 'UkHSplit',
           'UkHLine', 'UkNavDivider', 'UkNavbarDropdown', 'UkNavbar', 'UkSidebar', 'NavTab', 'UkTab', 'CardTitle',
           'CardHeader', 'CardBody', 'CardFooter', 'CardContainer', 'Card', 'Table', 'Td', 'Th', 'Tr', 'Thead', 'Tbody',
           'TableFromLists', 'TableFromDicts', 'UkFormSection']

# %% ../lib_nbs/01_core.ipynb
import fasthtml.common as fh
from fasthtml.common import is_listy, Div, P, Span, Script, FastHTML, FT, to_xml, show
from fasthtml.svg import Svg
from enum import Enum
from fasthtml.components import Uk_select,Uk_input_tag
from functools import partial
from itertools import zip_longest
from typing import Union, Tuple, Optional
from fastcore.all import *
import copy

# %% ../lib_nbs/01_core.ipynb
# need a better name, stringify might be too general for what it does 
def stringify(o # String, Tuple, or Enum options we want stringified
             ): # String that can be passed FT comp args (such as `cls=`)
    "Converts input types into strings that can be passed to FT components"  
    if is_listy(o): return ' '.join(map(str,o)) if o else ""
    return o.__str__()

# %% ../lib_nbs/01_core.ipynb
def str2ukcls(base, txt): 
    return f"uk-{base}-{txt.replace('_', '-')}".strip('-')

# %% ../lib_nbs/01_core.ipynb
class VEnum(Enum): 
    def __add__(self, other):   return stringify((self, other))
    def __radd__(self, other):  return stringify((other, self)) 
    def __str__(self): return self.value
    
    def __new__(cls, value, doc=None):
        member = str.__new__(cls)  # Use str as the base class
        member._value_ = value
        if doc is not None:
            member.__doc__ = doc
        return member

# %% ../lib_nbs/01_core.ipynb
def create_uk_enum(name, options, custom={}, enum_doc=None):
    def getval(a): return custom[a] if a in custom.keys() else a
    opts = {}
    for option in options:
        if isinstance(option, tuple): key, doc = option
        else: key, doc = option, None
        opts[key] = (str2ukcls(name.rstrip('T').lower(), getval(key)), doc)
    
    enum_class = VEnum(name, opts, type=str)
    if enum_doc:
        enum_class.__doc__ = enum_doc
    return enum_class


# %% ../lib_nbs/01_core.ipynb
def UkGenericComponent(component_fn, *c, cls=(), **kwargs):
    " Create a new component based on a basic HTML component for use with FrankenUI"
    return component_fn(cls=cls, **kwargs)(*c)

# %% ../lib_nbs/01_core.ipynb
ButtonT = create_uk_enum('ButtonT',('default','ghost', 'text','link',
                                    ('primary', 'Uses primary color from these'),
                                    ('secondary', 'Uses secondary color from theme'),
                                    ('danger', 'Red danger button'),
                                    ),
                        enum_doc="Style Options for Button from https://franken-ui.dev/docs/button")

# %% ../lib_nbs/01_core.ipynb
def Button(
           *c:str|FT,                     # Components to go inside the Button
           cls:str|Enum=ButtonT.default,  # cls for the Button (see ButtonT for style options)
           **kwargs                       # any other kwargs will be passed to the button 
          )-> FT:                         # Button w/ `type=button` and `uk-button` cls
    "A Button with Uk Styling"
    return UkGenericComponent(fh.Button,*c, cls=('uk-button',stringify(cls)), type='button', **kwargs)

# %% ../lib_nbs/01_core.ipynb
def H1(*c:FT|str,       # Components to go inside the Heading
       cls:Enum|str|tuple=(),   # cls for the Heading
       **kwargs  # any other kwargs will be passed to the Heading
      )->FT: # Heading with `class=uk-h1` cls
    "A H1 with Uk Styling"
    return UkGenericComponent(fh.H1, *c, cls=('uk-h1',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def H2(*c:FT|str,       # Components to go inside the Heading
       cls:Enum|str|tuple=(),   # cls for the Heading
       **kwargs  # any other kwargs will be passed to the Heading
      )->FT: # Heading with `class=uk-h2` cls
    "A H2 with Uk Styling"
    return UkGenericComponent(fh.H2, *c, cls=('uk-h2',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def H3(*c:FT|str,       # Components to go inside the Heading
       cls:Enum|str|tuple=(),   # cls for the Heading
       **kwargs  # any other kwargs will be passed to the Heading
      )->FT: # Heading with `class=uk-h3` cls
    "A H1 with Uk Styling"
    return UkGenericComponent(fh.H1, *c, cls=('uk-h1',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def H4(*c:FT|str,       # Components to go inside the Heading
       cls:Enum|str|tuple=(),   # cls for the Heading
       **kwargs  # any other kwargs will be passed to the Heading
      )->FT: # Heading with `class=uk-h4` cls
    "A H4 with Uk Styling"
    return UkGenericComponent(fh.H4, *c, cls=('uk-H4',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def Alert(*c, cls=(), **kwargs): 
    return UkGenericComponent(Div, *c, cls=('uk-alert',stringify(cls)), uk_alert=True, **kwargs)

# %% ../lib_nbs/01_core.ipynb
def Article(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Article, *c, cls=('uk-article',stringify(cls)), **kwargs)

def ArticleTitle(*c, cls=(), **kwargs):
    return UkGenericComponent(H1, *c, cls=('uk-article-title',stringify(cls)), **kwargs)

def ArticleMeta(*c, cls=(), **kwargs):
    return UkGenericComponent(P, *c, cls=('uk-article-meta',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
ContainerT = create_uk_enum('ContainerT',('xsmall','small','large','xlarge','expand'))

# %% ../lib_nbs/01_core.ipynb
def Container(*c, cls=(), **kwargs): 
    return UkGenericComponent(Div, *c, cls=('uk-container',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def Input(*c, cls=(), **kwargs): 
    return UkGenericComponent(fh.Input, *c, cls=('uk-input',stringify(cls)), **kwargs)
def Select(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Select, *c, cls=('uk-select',stringify(cls)), **kwargs)
def Radio(*c, cls=(), **kwargs): 
    return UkGenericComponent(fh.Input, *c, cls=('uk-radio',stringify(cls)), type='radio', **kwargs)
def CheckboxX(*c, cls=(), **kwargs): 
    return UkGenericComponent(fh.Input, *c, cls=('uk-checkbox',stringify(cls)), type='checkbox', **kwargs)
def Range(*c, cls=(), **kwargs): 
    return UkGenericComponent(fh.Input, *c, cls=('uk-range',stringify(cls)), type='range', **kwargs)
def Toggle_switch(*c, cls=(), **kwargs): 
    return UkGenericComponent(fh.Input, *c, cls=('uk-toggle-switch',stringify(cls)), type='checkbox', **kwargs)
def TextArea(*c, cls=(), **kwargs): 
    return UkGenericComponent(fh.Textarea, *c, cls=('uk-textarea',stringify(cls)), **kwargs)
def Button(*c, cls=ButtonT.default,  **kwargs):
    return UkGenericComponent(fh.Button,*c, cls=('uk-button',stringify(cls)), type='button', **kwargs)
def Switch(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Input, *c, cls=('uk-toggle-switch',stringify(cls)), type='checkbox', **kwargs)

# %% ../lib_nbs/01_core.ipynb
LabelT = create_uk_enum('LabelT', ('primary', 'secondary', 'danger'))

# %% ../lib_nbs/01_core.ipynb
def Label(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Label, *c, cls=('uk-label',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def FormLabel(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Label, *c, cls=('uk-form-label',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
LinkT = create_uk_enum('LinkT', ('muted', 'text', 'reset'))

# %% ../lib_nbs/01_core.ipynb
def Link(*c, cls=(), **kwargs):  
    return UkGenericComponent(fh.A, *c, cls=('uk-link',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def Link(*c, cls=(), **kwargs):
    cls = stringify(cls)
    if 'uk-link' not in cls: cls = (cls, 'uk-link')
    return UkGenericComponent(fh.A, *c, cls=cls, **kwargs)

# %% ../lib_nbs/01_core.ipynb
def List(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Ul, *c, cls=('uk-list',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def ModalContainer(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Div, *c, cls=('uk-modal-container',stringify(cls)), uk_modal=True, **kwargs)

def ModalDialog(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Div, *c, cls=('uk-modal-dialog',stringify(cls)), **kwargs)

def ModalHeader(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Div, *c, cls=('uk-modal-header',stringify(cls)), **kwargs)

def ModalBody(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Div, *c, cls=('uk-modal-body',stringify(cls)), **kwargs)

def ModalFooter(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Div, *c, cls=('uk-modal-footer',stringify(cls)), **kwargs)

def ModalTitle(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.H2, *c, cls=('uk-modal-title',stringify(cls)), **kwargs)

def ModalCloseButton(*c, cls=(), **kwargs):
    return UkGenericComponent(Button, *c, cls=('uk-modal-close',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def Modal(*c,
        header=None,          # Components that go in the header
        footer=None,          # Components that go in the footer
        cls=(),               # class for outermost container
        dialog_cls=(),        # classes for the dialog
        header_cls='p-6',     # classes for the header
        body_cls='space-y-6', # classes for the body
        footer_cls=(),        # classes for the footer
        id='',                # id for the outermost container
        **kwargs              # classes for the outermost container
        ):
    cls, dialog_cls, header_cls, body_cls, footer_cls = map(stringify, (cls, dialog_cls, header_cls, body_cls, footer_cls))
    res = []
    if header: res.append(ModalHeader(cls=header_cls)(header))
    res.append(ModalBody(cls=body_cls)(*c))
    if footer: res.append(ModalFooter(cls=footer_cls)(footer))
    return ModalContainer(ModalDialog(*res, cls=dialog_cls), cls=cls, id=id, **kwargs)

# %% ../lib_nbs/01_core.ipynb
def Nav(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Ul, *c, cls=('uk-nav',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def NavBarContainer(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Div, *c, cls=('uk-navbar-container',stringify(cls)), uk_navbar=True, **kwargs)

def NavBarNav(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Nav, *c, cls=('uk-navbar-nav',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
PaddingT = create_uk_enum('PaddingT', (
    'xsmall', 'small', 'default', 'medium', 'large', 'xlarge',
    'remove', 'remove_top', 'remove_bottom', 'remove_left', 'remove_right', 'remove_vertical', 'remove_horizontal'
), {'default':''})

# %% ../lib_nbs/01_core.ipynb
PositionT = create_uk_enum('PositionT', (
    'top', 'bottom', 'left', 'right','top_left', 'top_center', 'top_right','center', 'center_left', 'center_right',
    'bottom_left', 'bottom_center', 'bottom_right','center_horizontal', 'center_vertical'))

# %% ../lib_nbs/01_core.ipynb
def Placeholder(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Div, *c, cls=('uk-placeholder',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def Progress(*c, cls=(), value="", max="", **kwargs):
    return UkGenericComponent(fh.Progress, *c, value=value, max=max, cls=('uk-progress',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
SectionT = create_uk_enum('SectionT', (
    'default', 'muted', 'primary', 'secondary',
    'xsmall', 'small', 'large', 'xlarge', 'remove_vertical'
))

# %% ../lib_nbs/01_core.ipynb
def Section(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Div, *c, cls=('uk-section',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def Sticky(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Div, *c, cls=stringify(cls), uk_sticky=True, **kwargs)

# %% ../lib_nbs/01_core.ipynb
class Theme(Enum):
    slate = "slate"
    stone = "stone"
    gray = "gray"
    neutral = "neutral"
    red = "red"
    rose = "rose"
    orange = "orange"
    green = "green"
    blue = "blue"
    yellow = "yellow"
    violet = "violet"
    zinc = "zinc"

    def headers(self):
        js = (Script(src="https://cdn.tailwindcss.com"),
              Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit.min.js"),
              Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit-icons.min.js"),
              Script(type="module", src="https://unpkg.com/franken-wc@0.0.6/dist/js/wc.iife.js")
              )
        _url = f"https://unpkg.com/franken-wc@0.0.6/dist/css/{self.value}.min.css"
        return (*js, Link(rel="stylesheet", href=_url))

# %% ../lib_nbs/01_core.ipynb
TextT = create_uk_enum('TextT', (
    'lead', 'meta', 'italic', # Style
    'small', 'default', 'large', #Font Size
    'light', 'normal', 'bold', 'lighter', 'bolder', # Font Weight
    'capitalize', 'uppercase', 'lowercase', #Text transform
    'decoration_none', # Text decoration
    'muted', 'primary', 'secondary', 'success', 'warning', 'danger', # Color
    'left', 'right', 'center', 'justify', # Alignment
    'top', 'middle', 'bottom', 'baseline', # Vertical alignment
    'truncate', 'break_', 'nowrap' # Wrapping
))

# %% ../lib_nbs/01_core.ipynb
class TextFont(VEnum):
    muted_sm = stringify((TextT.muted, TextT.small))
    bold_sm = stringify((TextT.bold, TextT.small))

# %% ../lib_nbs/01_core.ipynb
def UkIcon(icon,    # Icon name from https://getuikit.com/docs/icon
           ratio=1, # Icon ratio/size 
           cls=()   # Span classes
          ):        # Span with Icon
    "Creates a Span with the given icon"
    return Span(uk_icon=f"icon: {icon}; ratio: {ratio}",cls=stringify(cls))

# %% ../lib_nbs/01_core.ipynb
# def Img(*args, data_src="", cls=(), **kwargs):
#     return UkGenericComponent(fh.Div, *args, data_src=data_src, uk_img=True, cls=stringify(cls), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def DiceBearAvatar(seed_name, # Seed name (ie 'Isaac Flath')
                   h,         # Height 
                   w          # Width
                  ):          # Span with Avatar
    url = 'https://api.dicebear.com/8.x/lorelei/svg?seed='
    return Span(cls=f"relative flex h-{h} w-{w} shrink-0 overflow-hidden rounded-full bg-accent")(
            fh.Img(cls="aspect-square h-full w-full", alt="Avatar", src=f"{url}{seed_name}"))

# %% ../lib_nbs/01_core.ipynb
FlexT = create_uk_enum('FlexT', (
    'block', 'inline',
    'left', 'center', 'right', 'between', 'around', # horizontal
    'stretch', 'top', 'middle', 'botton', # Vertical
    'row', 'row_reverse', 'col', 'col_reverse', # Direction
    'nowrap', 'wrap', 'wrap_reverse' # Wrap
), {'block':''})

# %% ../lib_nbs/01_core.ipynb
GridT = create_uk_enum('GridT', ('small', 'medium', 'large', 'collapse'))

# %% ../lib_nbs/01_core.ipynb
def Grid(*c,      # Divs/Containers that should be divided into a grid
         cols=3,  # Number of columns
         cls=GridT.small,  # Additional classes for Grid Div
         **kwargs # Additional args for Grid Div
        ):
    """Creates a grid with the given number of columns, often used for a grid of cards"""
    cls = stringify(cls)
    return Div(cls=(f'grid grid-cols-{cols}',cls), **kwargs)(*c)

# %% ../lib_nbs/01_core.ipynb
def ResponsiveGrid(*c, sm=1, md=2, lg=3, xl=4, gap=2, cls='', **kwargs):
    "Creates a responsive grid with the given number of columns for different screen sizes"
    return Div(cls=f'grid grid-cols-{sm} md:grid-cols-{md} lg:grid-cols-{lg} xl:grid-cols-{xl} gap-{gap} ' + stringify(cls), **kwargs)(*c)

# %% ../lib_nbs/01_core.ipynb
def FullySpacedDiv(*c,                # Components
                   cls='uk-width-1-1',# Classes for outer div
                   **kwargs           # Additional args for outer div
                  ):                  # Div with spaced components via flex classes
    "Creates a flex div with it's components having as much space between them as possible"
    cls = stringify(cls)
    return Div(cls=(FlexT.block,FlexT.between,FlexT.middle,cls), **kwargs)(*c)

# %% ../lib_nbs/01_core.ipynb
def CenteredDiv(*c,      # Components
                cls=(),  # Classes for outer div
                **kwargs # Additional args for outer div
               ): # Div with components centered in it
    "Creates a flex div with it's components centered in it"
    cls=stringify(cls)
    return Div(cls=(FlexT.block,FlexT.col,FlexT.middle,FlexT.center,cls),**kwargs)(*c)

# %% ../lib_nbs/01_core.ipynb
def LAlignedDiv(*c,      # Components
                cls=(),  # Classes for outer div
                **kwargs # Additional args for outer div
               ): # Div with components aligned to the left
    "Creates a flex div with it's components aligned to the left"
    cls=stringify(cls)
    return Div(cls=(FlexT.block,FlexT.left,FlexT.middle,cls), **kwargs)(*c)

# %% ../lib_nbs/01_core.ipynb
def RAlignedDiv(*c,      # Components
                cls=(),  # Classes for outer div
                **kwargs # Additional args for outer div
               ): # Div with components aligned to the right
    "Creates a flex div with it's components aligned to the right"
    cls=stringify(cls)
    return Div(cls=(FlexT.block,FlexT.right,FlexT.middle,cls), **kwargs)(*c)

# %% ../lib_nbs/01_core.ipynb
def VStackedDiv(*c, cls='', **kwargs):
    cls=stringify(cls)
    return Div(cls=(FlexT.block,FlexT.col,FlexT.middle,cls), **kwargs)(*c)

# %% ../lib_nbs/01_core.ipynb
def HStackedDiv(*c, cls='', **kwargs):
    cls=stringify(cls)
    return Div(cls=(FlexT.block,FlexT.row,FlexT.middle,cls), **kwargs)(*c)

# %% ../lib_nbs/01_core.ipynb
def SpaceBetweenDiv(*c, cls='', **kwargs):
    cls = stringify(cls)
    return Div(cls=(FlexT.block,FlexT.between,FlexT.middle,cls), **kwargs)(*c)

# %% ../lib_nbs/01_core.ipynb
def GenericLabelInput(
               label:str|FT,
               input_fn, 
               lbl_cls='',
               input_cls='',
               container=Div, 
               container_cls='',
               id='',
                **kwargs
                ):
    "`Div(Label,Input)` component with Uk styling injected appropriately. Generally you should higher level API, such as `UkTextArea` which is created for you in this library"
    if isinstance(label, str) or label.tag != 'label': 
        label = FormLabel(cls=stringify(lbl_cls), fr=id)(label)
    inp = input_fn(id=id, cls=stringify(input_cls), **kwargs)        
    if container: return container(label, inp, cls=stringify(container_cls))
    return label, inp

# %% ../lib_nbs/01_core.ipynb
@delegates(GenericLabelInput, but=['input_fn'])
def LabelInput(*args, **kwargs): return GenericLabelInput(*args, input_fn=Input, **kwargs)

# %% ../lib_nbs/01_core.ipynb
@delegates(GenericLabelInput, but=['input_fn'])
def LabelRadio(*args, **kwargs): return GenericLabelInput(*args, input_fn=Radio, **kwargs)

# %% ../lib_nbs/01_core.ipynb
@delegates(GenericLabelInput, but=['input_fn'])
def LabelCheckboxX(*args, **kwargs): return GenericLabelInput(*args, input_fn=CheckboxX, **kwargs)

# %% ../lib_nbs/01_core.ipynb
@delegates(GenericLabelInput, but=['input_fn'])
def LabelRange(*args, **kwargs): return GenericLabelInput(*args, input_fn=Range, **kwargs)

# %% ../lib_nbs/01_core.ipynb
@delegates(GenericLabelInput, but=['input_fn'])
def LabelToggle_switch(*args, **kwargs): return GenericLabelInput(*args, input_fn=Toggle_switch, **kwargs)

# %% ../lib_nbs/01_core.ipynb
@delegates(GenericLabelInput, but=['input_fn'])
def LabelTextArea(*args, **kwargs): return GenericLabelInput(*args, input_fn=TextArea, **kwargs)

# %% ../lib_nbs/01_core.ipynb
@delegates(GenericLabelInput, but=['input_fn'])
def LabelSwitch(*args, **kwargs): return GenericLabelInput(*args, input_fn=Switch, **kwargs)

# %% ../lib_nbs/01_core.ipynb
def LabelSelect(*option,
               label:str|FT,
               lbl_cls='',
               input_cls='',
               container=Div, 
               container_cls='',
               id='',
                **kwargs
                ):
    "`Div(Label,Input)` component with Uk styling injected appropriately. Generally you should higher level API, such as `UkTextArea` which is created for you in this library"
    if isinstance(label, str) or label.tag != 'label': 
        label = FormLabel(lbl_cls=stringify(lbl_cls), fr=id)(label)
    inp = Select(*option, id=id, cls=stringify(input_cls), **kwargs)        
    if container: return container(label, inp, cls=stringify(container_cls))
    return label, inp

# %% ../lib_nbs/01_core.ipynb
def UkIconButton(*c, sz='small', cls=(), **kwargs):
    "Creates an `IconButton` with uk styling"
    if sz not in ('small','medium','large'): raise ValueError(f"Invalid size '{sz}'. Must be 'small', 'medium', or 'large'.")
    return Button(cls=f'uk-icon-button uk-icon-button-{sz} ' + stringify(cls), **kwargs)(*c)

# %% ../lib_nbs/01_core.ipynb
def Options(*c,                    # Content for an `Option`
            selected_idx:int=None, # Index location of selected `Option`
            disabled_idxs:set=None # Idex locations of disabled `Options`
           ):
    "Helper function to wrap things into `Option`s for use in `UkSelect`"
    return [fh.Option(o,selected=i==selected_idx, disabled=disabled_idxs and i in disabled_idxs) for i,o in enumerate(c)]

# %% ../lib_nbs/01_core.ipynb
def UkSelect(*option,            # Options for the select dropdown (can use `Options` helper function to create)
             label=(),           # String or FT component for the label
             lbl_cls=(),         # Additional classes for the label
             inp_cls=(),         # Additional classes for the select input
             cls=('space-y-2',), # Classes for the outer div
             id="",              # ID for the select input
             name="",            # Name attribute for the select input
             placeholder="",     # Placeholder text for the select input
             searchable=False,   # Whether the select should be searchable
             **kwargs):          # Additional arguments passed to Uk_select
    "Creates a select dropdown with uk styling"
    lbl_cls, inp_cls, cls = map(stringify, (lbl_cls, inp_cls, cls))
    if label: 
        lbl = FormLabel(cls=f'{lbl_cls}', fr=id)(label) 
    select = Uk_select(*option, cls=inp_cls, uk_cloak=True, id=id, 
                       name=name, placeholder=placeholder, searchable=searchable, **kwargs)
    return Div(cls=cls)(lbl, select) if label else Div(cls=cls)(select)

# %% ../lib_nbs/01_core.ipynb
def _UkDropdownButtonOptions(opt_grps, opt_hdrs=None):
    res = []
    for g,h in zip_longest(opt_grps, tuplify(opt_hdrs)):
        if h: res.append(Li(cls="uk-nav-header")(h if isinstance(h,FT) else Div(h)))
        if isinstance(g,(list,tuple)): res += list(map(Li, g))
        else: res.append(Li(g))
    return res

# %% ../lib_nbs/01_core.ipynb
def UkDropdownButton(
    *opt_grp,        # List of options to be displayed in the dropdown
    opt_hdrs=None,  # List of headers for each option group, or None
    label=None,     # String, FT component, or None for the `Button`
    btn_cls=ButtonT.default,  # Button class(es)
    cls=(),         # Parent div class
    dd_cls=(),      # Class that goes on the dropdown container
    icon='triangle-down',  # Icon to use for the dropdown
    icon_cls='',    # Additional classes for the icon
    icon_position='right'  # Position of the icon: 'left' or 'right'
    ):
    dd_cls, btn_cls, cls, icon_cls = map(stringify, (dd_cls, btn_cls, cls, icon_cls))
    icon_component = UkIcon(icon, cls=icon_cls) if icon else None
    btn_content = [] if label is None else [label]
    if icon_component: btn_content.insert(0 if icon_position == 'left' else len(btn_content), icon_component)
    btn = Button(cls=btn_cls)(*btn_content)
    dd = Div(uk_dropdown='mode: click; pos: bottom-right', cls='uk-dropdown uk-drop ' + dd_cls)(
        Ul(cls='uk-dropdown-nav')(*_UkDropdownButtonOptions(opt_grp, opt_hdrs)))
    return Div(cls=cls)(Div(cls='flex items-center space-x-4')(btn, dd))

# %% ../lib_nbs/01_core.ipynb
def UkHSplit(*c, cls=(), line_cls=(), text_cls=()):
    # Divider FrankenUI stuff
    cls, line_cls, text_cls = map(stringify,(cls, line_cls, text_cls))
    return Div(cls='relative ' + cls)(
        Div(cls="absolute inset-0 flex items-center " + line_cls)(Span(cls="w-full border-t border-border")),
        Div(cls="relative flex justify-center " + text_cls)(Span(cls="bg-background px-2 ")(*c)))

# %% ../lib_nbs/01_core.ipynb
def UkHLine(lwidth=2, y_space=4): return Div(cls=f"my-{y_space} h-[{lwidth}px] w-full bg-secondary")

# %% ../lib_nbs/01_core.ipynb
def UkNavDivider(): return fh.Li(cls="uk-nav-divider")

# %% ../lib_nbs/01_core.ipynb
def UkNavbarDropdown(*c, label, href='#', cls='', has_header=False, **kwargs):
    fn = lambda x: Li(item, cls='uk-drop-close', href='#demo', uk_toggle=True)
    flattened = []
    for i, item in enumerate(c):
        if i > 0: flattened.append(Li(cls="uk-nav-divider"))
        if isinstance(item, (list,tuple)): flattened.extend(map(Li, item))
        else: flattened.append(Li(item, cls="uk-nav-header" if i == 0 and has_header else None, uk_toggle=True))
    return (fh.Li(cls=cls, **kwargs)(
                fh.A(label, cls='uk-drop-close', href='#', uk_toggle=True), 
                Div(cls='uk-navbar-dropdown', uk_dropdown="mode: click; pos: bottom-left")(fh.Ul(cls='uk-nav uk-dropdown-nav')(*flattened))))

# %% ../lib_nbs/01_core.ipynb
def _NavBarSide(n, s):
    def add_class(item):
        if isinstance(item, str): return Li(cls='uk-navbar-item')(item)
        else: item.attrs['class'] = f"{item.attrs.get('class', '')} uk-navbar-item".strip()
        return item
    return Div(cls=f'uk-navbar-{s}')(Ul(cls='uk-navbar-nav')(*map(add_class, tuplify(n))))

# %% ../lib_nbs/01_core.ipynb
def UkNavbar(lnav: fh.Sequence[Union[str, FT]]=None, 
             rnav: fh.Sequence[Union[str, FT]]=None, 
             cls='',
             **kwargs
            ) -> FT:
    return Div(cls='uk-navbar-container uk-width-1-1 relative z-10 '+ stringify(cls), uk_navbar=True, **kwargs)(
             _NavBarSide(lnav,'left') if lnav else '',
             _NavBarSide(rnav,'right') if rnav else '')

# %% ../lib_nbs/01_core.ipynb
def UkSidebar(*ul,                 # Each Ul can be it's own section.  Use A for links!
              cls='space-y-4 p-4', # Classes for outer container
              **kwargs             # Kwargs for outer container
             ):
    "Creates a styled sidebar component"
    styles = ('uk-nav-default', 'uk-nav-primary','uk-nav-secondary')
    sidebar = []
    for section in tuplify(ul):
        section = copy.deepcopy(section)
        _sattrs = section.attrs
        if 'class' not in _sattrs: _sattrs['class'] = ''
        if 'uk-nav' not in _sattrs: _sattrs['class'] += ' uk-nav '
        if not any(x in styles for x in _sattrs['class'].split()): _sattrs['class'] += ' uk-nav-default '
        sidebar.append(section)  
    return Div(cls=cls, **kwargs)(*sidebar)

# %% ../lib_nbs/01_core.ipynb
def NavTab(text, active=False):
    return Li(cls="uk-active" if active else " ")(A(text, href="#demo", uk_toggle=True))

def UkTab(*items, maxw=96, cls='', **kwargs):
    cls = stringify(cls)
    return Ul(cls=f"uk-tab-alt max-w-{maxw} "+cls,**kwargs)(*[NavTab(item, active=i==0) for i, item in enumerate(items)])

# %% ../lib_nbs/01_core.ipynb
CardT = create_uk_enum('CardT',('default', 'primary', 'secondary', 'danger'))

# %% ../lib_nbs/01_core.ipynb
def CardTitle(*c, cls=(), **kwargs):
    return UKGenericComponent(fh.Div, *c, cls=('uk-card-title',stringify(cls)), **kwargs)

def CardHeader(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Div, *c, cls=('uk-card-header',stringify(cls)), **kwargs)

def CardBody(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Div, *c, cls=('uk-card-body',stringify(cls)), **kwargs)

def CardFooter(*c, cls=(), **kwargs):
    return UkGenericComponent(fh.Div, *c, cls=('uk-card-footer',stringify(cls)), **kwargs)

def CardContainer(*c, cls=CardT.default, **kwargs):
    return UkGenericComponent(fh.Div, *c, cls=('uk-card',stringify(cls)), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def Card(*c, # Components that go in the body
        header=None, # Components that go in the header
        footer=None,  # Components that go in the footer
        body_cls='space-y-6', # classes for the body
        header_cls=(), # classes for the header
        footer_cls=(), # classes for the footer
        cls=(), #class for outermost component
        **kwargs # classes that for the card itself
        ):
    header_cls, footer_cls, body_cls, cls = map(stringify, (header_cls, footer_cls, body_cls, cls))
    res = []
    if header: res.append(CardHeader(cls=header_cls)(header))
    res.append(CardBody(cls=body_cls)(*c))
    if footer: res.append(CardFooter(cls=footer_cls)(footer))
    return CardContainer(cls=cls, **kwargs)(*res)

# %% ../lib_nbs/01_core.ipynb
TableT = create_uk_enum("TableT", ('divider', 'striped', 'hover', 'small', 'large', 
                                    'justify', 'middle','responsive',))

# %% ../lib_nbs/01_core.ipynb
def Table(*args, cls=(TableT.middle, TableT.divider, TableT.hover, TableT.small), **kwargs): 
    return fh.Table(cls=('uk-table', stringify(cls)), *args, **kwargs)

# %% ../lib_nbs/01_core.ipynb
def _TableCell(Component, *args, cls=(), shrink=False, expand=False, small=False, **kwargs):
    cls = stringify(cls)
    if shrink: cls += ' uk-table-shrink'
    if expand: cls += ' uk-table-expand'
    if small: cls += ' uk-table-small'
    return Component(*args,cls=cls, **kwargs)

@delegates(_TableCell, but=['Component'])
def Td(*args,**kwargs):  return _TableCell(fh.Td, *args, **kwargs)
@delegates(_TableCell, but=['Component'])
def Th(*args,**kwargs): return _TableCell(fh.Th, *args, **kwargs)

def Tr(*cells, cls=(), **kwargs):  return fh.Tr(*cells, cls=stringify(cls), **kwargs)
def Thead(*rows, cls=(), **kwargs): return fh.Thead(*rows, cls=stringify(cls), **kwargs)
def Tbody(*rows, cls=(), **kwargs): return fh.Tbody(*rows, cls=stringify(cls), **kwargs)

# %% ../lib_nbs/01_core.ipynb
def TableFromLists(header_data, body_data, footer_data=None, 
                   header_cell_render=Th,body_cell_render=Td, footer_cell_render=Td,
                   cls=(TableT.middle, TableT.divider, TableT.hover, TableT.small), **kwargs):
    
    return Table(
                Thead(Tr(*map(header_cell_render, header_data))),
                Tbody(*[Tr(*map(body_cell_render, r)) for r in body_data]),
                Tfoot(Tr(*map(footer_cell_render, footer_data))) if footer_data else '',
                cls=stringify(cls),    
                **kwargs)

# %% ../lib_nbs/01_core.ipynb
def TableFromDicts(header_data:Sequence, body_data:Sequence[dict], footer_data=None, 
                   header_cell_render=Th, body_cell_render=lambda k,v : Td(v), footer_cell_render=lambda k,v : Td(v),
                   cls=(TableT.middle, TableT.divider, TableT.hover, TableT.small), **kwargs):
    
    return Table(
        Thead(Tr(*[header_cell_render(h) for h in header_data])),
        Tbody(*[Tr(*[body_cell_render(k, r) for k in header_data]) for r in body_data]),
        Tfoot(Tr(*[footer_cell_render(k, footer_data.get(k.lower(), '')) for k in header_data])) if footer_data else '',
        cls=stringify(cls),    
        **kwargs
    )

# %% ../lib_nbs/01_core.ipynb
def UkFormSection(title, description, *c, button_txt='Update', outer_margin=6, inner_margin=6):
    return Div(cls=f'space-y-{inner_margin} py-{outer_margin}')(
        Div(H3(title), P(description, cls=TextFont.bold_sm)),
        UkHSplit(), *c,
        Div(Button(button_txt, cls=ButtonT.primary)) if button_txt else None)
