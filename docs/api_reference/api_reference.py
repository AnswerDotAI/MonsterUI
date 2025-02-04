"""Reference to all FrankenUI Components"""

from fasthtml.common import *
from monsterui.all import *
# from nbdev.showdoc import *
from utils import create_flippable_card, fn2code_string
from enum import EnumType
from collections.abc import Callable

'''
Any variable starting with docs_ is a function that generates a section of the API reference.

These are automatically added to the docs sidebar so you don't have to do anything other than add the function using create_doc_section.
'''
from inspect import signature, getdoc, getsourcefile, getsourcelines

# Utilities
def get_github_url(func):
    "Create GitHub URL for function, assuming AnswerDotAI/MonsterUI repo"
    file = getsourcefile(func).split('MonsterUI/')[-1]
    line = getsourcelines(func)[-1]
    file = file.replace('/opt/venv/lib/python3.12/site-packages/','')
    return f"https://github.com/AnswerDotAI/MonsterUI/blob/main/{file}#L{line}"

def get_github_url(func):
    "Create GitHub URL for function, assuming AnswerDotAI/MonsterUI repo"
    try:
        file = getsourcefile(func)
        line = getsourcelines(func)[-1]
        
        # Get path after monsterui/ (case insensitive)
        file = file.lower()
        if 'monsterui/' in file:
            file = file.split('monsterui/')[-1]
        elif 'site-packages/' in file:
            file = file.split('site-packages/')[-1]
            
        return f"https://github.com/AnswerDotAI/MonsterUI/blob/main/monsterui/{file}#L{line}"
    except:
        return None
    
from fastcore.docments import docments, docstring, get_name
def show_doc(func) -> str:
    "Convert a Google-style docstring to markdown"
    params = docments(func, args_kwargs=True)
    funcname = get_name(func)
    doc = docstring(func)
    par, ret = None, None
    if params:
        par = Div(Strong('Params'), 
                  Ul(*[Li(render_md(f"`{name}` {desc if desc else ''}",class_map_mods={'p':'leading-relaxed'}), cls='') for name, desc in params.items() if name != 'return'], cls='uk-list-disc space-y-2 mb-6 ml-6'))
    if 'return' in params and params['return']: ret = render_md(f"**Returns:** {params['return']}") 
    return Div(
        DivFullySpaced(
            render_md(f"### {funcname}"),
            A("Source", href=get_github_url(func), cls='text-primary hover:text-primary-focus underline')),
        Pre(Code(f"{funcname}{signature(func)}",
                 cls='hljs language-python px-1 block overflow-x-auto'),
                 cls='bg-base-200 rounded-lg p-4 mb-6'),
        Div(Blockquote(render_md(doc), cls='pl-4 border-l-4 border-primary mb-6'), par, ret, cls='ml-10'))

def enum_to_html_table(enum_class):
    "Creates a compact multi-column table display for enum documentation"
    items = list(enum_class.__members__.items())
    n_cols = min(4, max(2, round((len(items) ** 0.5))))
    
    # Create header/cell pairs with borders
    def make_pair(opt, val, i): 
        border = 'border-l border-base-300 pl-4' if i > 0 else ''
        return [Th('Option', cls=border), Th('Value')] if opt == 'header' else [Td(opt, cls=border), Td(val)]
    
    # Build rows with padding for incomplete final row
    rows = []
    for i in range(0, len(items), n_cols):
        cells = []
        for j in range(n_cols):
            name, val = items[i + j] if i + j < len(items) else ('', '')
            cells.extend(make_pair(name, val.value if val else '', j))
        rows.append(Tr(*cells))

    return Div(
        Hr(cls='uk-divider-icon my-2'),
        DivFullySpaced(H3(enum_class.__name__, cls='my-2'), P(I(enum_class.__doc__), cls='text-sm')),
        Table(
            Thead(Tr(*make_pair('header', '', 0) * n_cols)),
            Tbody(*rows),
            cls=(TableT.hover, 'uk-table-small uk-table-justify uk-table-middle')))

def render_content(c):
    "Renders content by type"
    if isinstance(c, str):        return render_md(c) # Strings are rendered as markdown
    elif isinstance(c, EnumType): return enum_to_html_table(c) # Enums are rendered as tables
    elif isinstance(c, FT):       return c # FastHTML tags are rendered as themselves
    elif isinstance(c, tuple): # Tuples are rendered as cards with source and output that can be flipped
        extra_cls = c[2] if len(tuple(c)) == 3 else None
        return create_flippable_card(c[0], c[1], extra_cls)
    elif isinstance(c, Callable): # Callables are rendered as documentation via show_doc
        return show_doc(c)
        # _html = show_doc(c, renderer=BasicHtmlRenderer)._repr_html_()
        # return NotStr(apply_classes(_html, class_map_mods={"table":'uk-table uk-table-hover uk-table-small'}))
    else: return c

def create_doc_section(*content, title):
    return lambda: Titled(H1(title,cls='mb-10'), *map(render_content, content))

def string2code_string(code: str) -> tuple: return eval(code), code

# Sliders

def ex_sliders_1():
    return Slider(*[Img(src=f'https://picsum.photos/200/200?random={i}') for i in range(10)])

def ex_sliders_2():
    def _card(i): return Card(H3(f'Card {i}'), P(f'Card {i} content'))
    return Slider(*[_card(i) for i in range(10)])

def ex_sliders_3():
    def _card(i): return Card(H3(f'Card {i}'), P(f'Card {i} content'))
    return Slider(*[_card(i) for i in range(10)], items_cls='gap-10', uk_slider='autoplay: true; autoplay-interval: 1000')

docs_sliders = create_doc_section(
    "Here is a simple example of a slider:",
    fn2code_string(ex_sliders_1),
    "Here is a slider with cards:",
    fn2code_string(ex_sliders_2),
    "Here is a slider with cards and autoplay:",
    fn2code_string(ex_sliders_3),
    "Typically you want to use the `Slider` component, but if you need more control you can use the `SliderContainer`, `SliderItems`, and `SliderNav` components.",
    Slider,
    SliderContainer,
    SliderItems,
    SliderNav,
    title="Sliders")

# Buttons

def ex_buttons(): 
    return Grid(
        Button("Default"),
        Button("Primary",   cls=ButtonT.primary),
        Button("Secondary", cls=ButtonT.secondary),
        Button("Danger",    cls=ButtonT.danger),
        Button("Text",      cls=ButtonT.text),
        Button("Link",      cls=ButtonT.link),
        Button("Ghost",     cls=ButtonT.ghost),
        )

def ex_links(): 
    return Div(cls='space-x-4')(
        A('Default Link'),
        A('Muted Link', cls=AT.muted),
        A('Text Link',  cls=AT.text),
        A('Reset Link', cls=AT.reset),
        A('Primary Link', cls=AT.primary),
        A('Classic Link', cls=AT.classic),)

docs_button_link = create_doc_section(
    Div(id='button'), # for linking to in release post
    fn2code_string(ex_buttons),
    fn2code_string(ex_links),
    Button, 
    ButtonT, 
    AT,
    title="Buttons & Links")

# Theme

def ex_theme_switcher():
    from fasthtml.components import Uk_theme_switcher
    return Uk_theme_switcher()

docs_theme_headers = create_doc_section( 
   """
   To get headers with a default theme use `hdrs=Theme.<color>.headers()`.  For example for the blue theme you would use `hdrs=Theme.blue.headers()`.  The theme integrated together different frameworks and allows tailwind, FrankenUI, HighlighJS, and DaisyUI components to work well together.
   
   Tailwind, FrankenUI and DaisyUI are imported by default.  You must use DaisyUI headers to use anything in the `daisy` module, and FrankenUI headers to use anything in the `franken` module.

   HighlightJS is not added by default, but you can add it by setting `highlightjs=True` in the headers function.  The `render_md` function will use HighlightJS for code blocks.
   
   Theme options are:""",
    Card(Grid(map(P,Theme)),cls='mb-8'),
    H3("Theme Picker", id='theme'),
    fn2code_string(ex_theme_switcher),
    "Themes are controlled with `bg-background text-foreground` classes on the `Body` tag.  `fast_app` and `FastHTML` will do this for you automatically so you typically do not have to do anything",
    fast_app,
    FastHTML,
    title="Headers")

# Typography

def ex_headings():
    return Div(
        Titled("Titled"),
        H1("Level 1 Heading (H1)"), 
        H2("Level 2 Heading (H2)"), 
        H3("Level 3 Heading (H3)"), 
        H4("Level 4 Heading (H4)"),
        H5("Level 5 Heading (H5)"),
        H6("Level 6 Heading (H6)"),
        )


def ex_semantic_elements():
    return Div(
        H2("Semantic HTML Elements Demo"),
        # Text formatting examples
        P("Here's an example of ", Em("emphasized (Em)"), " and ", Strong("strong (Strong)"), " text."),
        P("Some ", I("italic text (I)"), " and ", Small("smaller text (Small)"), " in a paragraph."),
        P("You can ", Mark("highlight (Mark)"), " text, show ", Del("deleted (Del)"), " and ", 
          Ins("inserted (Ins)"), " content."),
        P("Chemical formulas use ", Sub("subscripts (Sub)"), " and ", Sup("superscripts (Sup)"), 
          " like H", Sub("2"), "O."),
        # Quote examples
        Blockquote(
            P("The only way to do great work is to love what you do."),
            Cite("Steve Jobs (Cite)")),
        P("As Shakespeare wrote, ", Q("All the world's a stage (Q)"), "."),
        # Time and Address
        P("Posted on ", Time("2024-01-29", datetime="2024-01-29")),
        Address(
            "Mozilla Foundation (Address)",
            Br(),
            "331 E Evelyn Ave (Address)",
            Br(),
            "Mountain View, CA 94041 (Address)",
            Br(),
            "USA (Address)"),
        # Technical and definition examples
        P(
            Dfn("HTML (Dfn)"), " (", 
            Abbr("HyperText Markup Language (Abbr)", title="HyperText Markup Language"), 
            ") is the standard markup language for documents designed to be displayed in a web browser."),
        P("Press ", Kbd("Ctrl (Kbd)"), " + ", Kbd("C (Kbd)"), " to copy."),
        P("The command returned: ", Samp("Hello, World! (Samp)")),
        P("Let ", Var("x (Var)"), " be the variable in the equation."),
        # Figure with caption
        Figure(
            PicSumImg(),
            Caption("Figure 1: An example image with caption (Caption)")),
        # Interactive elements
        Details(
            Summary("Click to show more information (Summary)"),
            P("This is the detailed content that is initially hidden (P)")),
        # Data representation
        P(
            Data("123 (Data)", value="123"), " is a number, and here's a Meter showing progress: ",
            Meter(value=0.6, min=0, max=1)),
        P(
            "Temperature: ",
            Meter(value=-1, min=-10, max=40, low=0, high=30, optimum=21),
            " (with low/high/optimum values)"),
        P(
            Data("€42.00", value="42"), 
            " - price example with semantic value"),
        # Output example
        P("Form calculation result: ", Output("The sum is 42 (Output)", form="calc-form", for_="num1 num2")),
        # Meta information example
        Section(
            H3("Blog Post Title (H3)"),
            Small("By John Doe • 5 min read (Small)"),
            P("Article content here...")),
        # Text decoration examples
        P("This text has ",U("proper name annotation (U)"), " and this is ",S("outdated information (S)"), " that's been superseded."),
        cls='space-y-4'
    )


def ex_textpresets():
    return Grid(*[Div(P(f"This is {preset.name} text", cls=preset.value)) for preset in TextPresets])

def ex_textt():
    return Grid(*[Div(P(f"This is {s.name} text", cls=s.value)) for s in TextT])

def ex_other():
    return Div(
        CodeSpan("This is a CodeSpan element"),
        Blockquote("This is a blockquote element"),
        CodeBlock("#This is a CodeBlock element\n\ndef add(a,b): return a+b"))

docs_typography = create_doc_section(
    P("Ready to go semantic options that cover most of what you need based on the HTML spec"),
    fn2code_string(ex_headings),
    fn2code_string(ex_semantic_elements),
    fn2code_string(ex_other),
    P("Styling text is possibly the most common style thing to do, so we have a couple of helpers for discoverability inside python.  `TextPresets` is intended to be combinations are are widely applicable and used often, where `TextT` is intended to be more flexible options for you to combine together yourself."),
    H5("TextPresets.*"),
    fn2code_string(ex_textpresets),
    H5("TextT.*"),
    fn2code_string(ex_textt),
    H3("API Reference"),
    TextPresets,
    TextT,
    H1, H2, H3, H4, H5, H6, 
    CodeSpan, Blockquote, CodeBlock, 
    Em, Strong, I, Small, Mark, Sub, Sup, Del, Ins,
    Dfn, Abbr, Q, Kbd, Samp, Var,
    Figure, Caption,
    Details, Summary,
    Meter, Data, Output,
    Address, Time,
    title="Text Style")


# Notifications
def ex_alerts1(): return Alert("This is a plain alert")

def ex_alerts2(): return Alert("Your purchase has been confirmed!", cls=AlertT.success)

def ex_alerts3():
    return Alert(
        DivLAligned(UkIcon('triangle-alert'), 
                    P("Please enter a valid email.")),
        cls=AlertT.error)

def ex_toasts1():
    return Toast("First Example Toast", cls=(ToastHT.start, ToastVT.bottom))

def ex_toasts2():
    return Toast("Second Example Toast", alert_cls=AlertT.info)

docs_notifications = create_doc_section(
    H3("Alerts"),
    P("The simplest alert is a div wrapped with a span:"),
    fn2code_string(ex_alerts1),
    P("Alert colors are defined by the alert styles:"),
    fn2code_string(ex_alerts2), 
    P("It often looks nice to use icons in alerts: "),
    fn2code_string(ex_alerts3),
    Alert, AlertT, 
    DividerLine(),
    H3("Toasts"),
    P("To define a toast with a particular location, add horizontal or vertical toast type classes:"),
    fn2code_string(ex_toasts1), 
    P("To define toast colors, set the class of the alert wrapped by the toast:"),
    fn2code_string(ex_toasts2),
    Toast, ToastHT, ToastVT,
    title="Alerts & Toasts")

# Containers

def ex_articles():
    return Article(
        ArticleTitle("Sample Article Title"), 
        ArticleMeta("By: John Doe"),
        P('lorem ipsum dolor sit amet consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.'))

def ex_containers():
    return Container(
        "This is a sample container with custom styling.",
        cls=ContainerT.xs,
        style="background-color: #FFA500; color: #000000")


docs_containers = create_doc_section(
    ArticleMeta,
    ArticleTitle,
    Article,
    fn2code_string(ex_articles),
    Container,
    ContainerT,
    fn2code_string(ex_containers),
    Section,
    SectionT,
    title="Articles, Containers & Sections"
)

# Cards

def ex_card():
    return Card(
        Form(LabelInput("Input"),
             LabelRange("Range")),
        header=Div(
            CardTitle("Header"),
            P("A card with header and footer",cls=TextPresets.muted_sm)),
        footer=DivLAligned(Button("Footer Submit Button")))



def Tags(cats): return Div(cls='space-x-2')(map(Label, cats))

def ex_card2_wide():
    def Tags(cats): return DivLAligned(map(Label, cats))

    return Card(
        DivLAligned(
            A(Img(src="https://picsum.photos/200/200?random=12", style="width:200px"),href="#"),
            Div(cls='space-y-3 uk-width-expand')(
                H4("Creating Custom FastHTML Tags for Markdown Rendering"),
                P("A step by step tutorial to rendering markdown in FastHTML using zero-md inside of DaisyUI chat bubbles"),
                DivFullySpaced(map(Small, ["Isaac Flath", "20-October-2024"]), cls=TextT.muted),
                DivFullySpaced(
                    Tags(["FastHTML", "HTMX", "Web Apps"]),
                    Button("Read", cls=(ButtonT.primary,'h-6'))))),
        cls=CardT.hover)

def ex_card2_tall():
    def Tags(cats): return DivLAligned(map(Label, cats))

    return Card(
        Div(
            A(Img(src="https://picsum.photos/400/200?random=14"), href="#"),
            Div(cls='space-y-3 uk-width-expand')(
                H4("Creating Custom FastHTML Tags for Markdown Rendering"),
                P("A step by step tutorial to rendering markdown in FastHTML using zero-md inside of DaisyUI chat bubbles"),
                DivFullySpaced(map(Small, ["Isaac Flath", "20-October-2024"]), cls=TextT.muted),
                DivFullySpaced(
                    Tags(["FastHTML", "HTMX", "Web Apps"]),
                    Button("Read", cls=(ButtonT.primary,'h-6'))))),
        cls=CardT.hover)

def ex_card3():
    def team_member(name, role, location="Remote"):
        return Card(
            DivLAligned(
                DiceBearAvatar(name, h=24, w=24),
                Div(H3(name), P(role))),
            footer=DivFullySpaced(
                DivHStacked(UkIcon("map-pin", height=16), P(location)),
                DivHStacked(*(UkIconLink(icon, height=16) for icon in ("mail", "linkedin", "github")))))
    team = [
        team_member("Sarah Chen", "Engineering Lead", "San Francisco"),
        team_member("James Wilson", "Senior Developer", "New York"),
        team_member("Maria Garcia", "UX Designer", "London"),
        team_member("Alex Kumar", "Product Manager", "Singapore"),
        team_member("Emma Brown", "DevOps Engineer", "Toronto"),
        team_member("Marcus Johnson", "Frontend Developer", "Berlin")
    ]
    return Grid(*team, cols_sm=1, cols_md=1, cols_lg=2, cols_xl=3)

docs_cards = create_doc_section(
    H3("Example Usage"),
    fn2code_string(ex_card),
    (*fn2code_string(ex_card2_wide),'uk-visible@s'),
    (*fn2code_string(ex_card2_tall),'uk-hidden@s'),
    fn2code_string(ex_card3),
    H3("API Reference"),
    Card,
    CardTitle,
    CardT,
    P("The remainder of these are only needed if you're doing something really special.  They are used in the `Card` function to generate the boilerplate for you.", cls='my-6'),
    CardContainer,
    CardHeader,
    CardBody,
    CardFooter,
    title="Cards"
)

# Lists

def ex_lists():
    list_options = [(style,str(cls)) for style,cls in ListT.__members__.items()]
    lists = [Div(H4(f"{style} List:"), Ul(Li("Item 1"), Li("Item 2"), cls=cls)) for style, cls in list_options]
    return Grid(*lists)

docs_lists = create_doc_section(
    fn2code_string(ex_lists),
    ListT,
    title="Lists")

# Forms

def ex_formlabel(): 
    return FormLabel("Form Label")

def ex_input(): 
    return Div(
        Input(placeholder="Enter text"), 
        LabelInput(label="Input", id='myid'))

def ex_checkbox(): 
    return Div(
        CheckboxX(), 
        LabelCheckboxX(label="Checkbox", id='checkbox1'))

def ex_range(): 
    return Div(
        Range(), 
        LabelRange(label="Range", id='range1'))

def ex_switch(): 
    return Div(
        Switch(id="switch"), 
        LabelSwitch(label="Switch", id='switch'))

def ex_textarea(): 
    return Div(
        TextArea(placeholder="Enter multiple lines of text"), 
        LabelTextArea(label="TextArea", id='myid'))

def ex_radio(): 
    return Div(
        Radio(name="radio-group", id="radio1"), 
        LabelRadio(label="Radio", id='radio1',cls='flex items-center space-x-4'))

def ex_ukselect(): 
    return Div(
        UkSelect(map(Option, ["Option 1", "Option 2", "Option 3"])),
        LabelUkSelect(map(Option, ["Option 1", "Option 2", "Option 3"]), label="UkSelect", id='myid'))

def ex_select(): 
    return Div(
        Select(map(Option, ["Option 1", "Option 2", "Option 3"])),
        LabelSelect(map(Option, ["Option 1", "Option 2", "Option 3"]), label="Select", id='myid'))

def ex_progress(): 
    return Progress(value=20, max=100)

def ex_form():
    relationship = ["Parent",'Sibling', "Friend", "Spouse", "Significant Other", "Relative", "Child", "Other"]
    return Div(cls='space-y-4')(
        DivCentered(
            H3("Emergency Contact Form"),
            P("Please fill out the form completely", cls=TextPresets.muted_sm)),
        Form(cls='space-y-4')(
            Grid(LabelInput("First Name",id='fn'), LabelInput("Last Name",id='ln')),
            Grid(LabelInput("Email",     id='em'), LabelInput("Phone",    id='ph')),
            H3("Relationship to patient"),
            Grid(*[LabelCheckboxX(o) for o in relationship], cols=4, cls='space-y-3'),
            LabelInput("Address",        id='ad'),
            LabelInput("Address Line 2", id='ad2'),
            Grid(LabelInput("City",      id='ct'), LabelInput("State",    id='st')),
            LabelInput("Zip",            id='zp'),
            DivCentered(Button("Submit Form", cls=ButtonT.primary))))

docs_forms = create_doc_section(
    H3("Example Form"),
    P(f"This form was live coded in a 5 minute video ",
          A("here",href="https://www.loom.com/share/0916e8a95d524c43a4d100ee85157624?start_and_pause=1", 
            cls=AT.muted), cls=TextPresets.muted_sm),
    fn2code_string(ex_form),
    FormLabel,
    fn2code_string(ex_formlabel),
    Input,
    fn2code_string(ex_input),
    LabelInput,
    LabelCheckboxX,
    LabelSwitch,
    LabelRange,
    LabelTextArea,
    LabelRadio,
    LabelSelect,
    LabelUkSelect,
    Progress,
    fn2code_string(ex_progress),
    Radio,
    fn2code_string(ex_radio),
    CheckboxX,
    fn2code_string(ex_checkbox),
    Range,
    fn2code_string(ex_range),
    Switch,
    fn2code_string(ex_switch),
    TextArea,
    fn2code_string(ex_textarea),
    Select,
    fn2code_string(ex_select),
    UkSelect,
    fn2code_string(ex_ukselect),
    Legend,
    Fieldset,
    title="Forms")

# Modals

def ex_modal():
    return Div(
        Button("Open Modal",data_uk_toggle="target: #my-modal" ),
        Modal(ModalTitle("Simple Test Modal"), 
              P("With some somewhat brief content to show that it works!", cls=TextPresets.muted_sm),
              footer=ModalCloseButton("Close", cls=ButtonT.primary),id='my-modal'))

docs_modals = create_doc_section(
    H3("Example Modal"),
    fn2code_string(ex_modal),
    Modal,
    ModalCloseButton,
    P("The remainder of the Modal functions below are used internally by the `Modal` function for you.  You shouldn't need to use them unless you're doing something really special."),
    ModalTitle,
    ModalFooter,
    ModalBody,
    ModalHeader,
    ModalDialog,
    ModalContainer,
    title="Modals")

# Layout

def ex_grid():
    return Grid(
        Div(
            P("Column 1 Item 1"), 
            P("Column 1 Item 2"), 
            P("Column 1 Item 3")),
        Div(
            P("Column 2 Item 1"), 
            P("Column 2 Item 2"), 
            P("Column 2 Item 3")),
        Div(
            P("Column 3 Item 1"), 
            P("Column 3 Item 2"), 
            P("Column 3 Item 3")))

def ex_product_grid():
    products = [
        {"name": "Laptop", "price": "$999", "img": "https://picsum.photos/200/100?random=1"},
        {"name": "Smartphone", "price": "$599", "img": "https://picsum.photos/200/100?random=2"},
        {"name": "Headphones", "price": "$199", "img": "https://picsum.photos/200/100?random=3"},
        {"name": "Smartwatch", "price": "$299", "img": "https://picsum.photos/200/100?random=4"},
        {"name": "Tablet", "price": "$449", "img": "https://picsum.photos/200/100?random=5"},
        {"name": "Camera", "price": "$799", "img": "https://picsum.photos/200/100?random=6"},
    ]
    
    product_cards = [
        Card(
            Img(src=p["img"], alt=p["name"], style="width:100%; height:100px; object-fit:cover;"),
            H4(p["name"], cls="mt-2"),
            P(p["price"], cls=TextPresets.bold_sm),
            Button("Add to Cart", cls=(ButtonT.primary, "mt-2"))
        ) for p in products
    ]
    
    return Grid(*product_cards, cols_lg=3)

def ex_fully_spaced_div():
    return DivFullySpaced(
        Button("Left", cls=ButtonT.primary),
        Button("Center", cls=ButtonT.secondary),
        Button("Right", cls=ButtonT.danger)
    )

def ex_centered_div():
    return DivCentered(
        H3("Centered Title"),
        P("This content is centered both horizontally and vertically.")
    )

def ex_l_aligned_div():
    return DivLAligned(
        Img(src="https://picsum.photos/100/100?random=1", style="max-width: 100px;"),
        H4("Left Aligned Title"),
        P("Some text that's left-aligned with the title and image.")
    )

def ex_r_aligned_div():
    return DivRAligned(
        Button("Action", cls=ButtonT.primary),
        P("Right-aligned text"),
        Img(src="https://picsum.photos/100/100?random=3", style="max-width: 100px;")
    )

def ex_v_stacked_div():
    return DivVStacked(
        H2("Vertical Stack"),
        P("First paragraph in the stack"),
        P("Second paragraph in the stack"),
        Button("Action Button", cls=ButtonT.secondary)
    )

def ex_h_stacked_div():
    return DivHStacked(
        Div(H4("Column 1"), P("Content for column 1")),
        Div(H4("Column 2"), P("Content for column 2")),
        Div(H4("Column 3"), P("Content for column 3"))
    )

docs_layout = create_doc_section(
    P("This page covers `Grid`s, which are often used for general structure, `Flex` which is often used for layout of components that are not grid based, padding and positioning that can help you make your layout look good, and dividers that can help break up the page", cls=TextPresets.muted_sm),
    H2("Grid"),
    fn2code_string(ex_grid),
    Grid,
    H4("Practical Grid Example"),
    fn2code_string(ex_product_grid),
    H2("Flex"),
    P("Play ", 
      A("Flex Box Froggy", href="https://flexboxfroggy.com/", cls=AT.muted), 
      " to get an understanding of flex box.",
      cls=TextPresets.muted_sm),
    DivFullySpaced,
    fn2code_string(ex_fully_spaced_div),
    DivCentered,
    fn2code_string(ex_centered_div),
    DivLAligned,
    fn2code_string(ex_l_aligned_div),
    DivRAligned,
    fn2code_string(ex_r_aligned_div),
    DivVStacked,
    fn2code_string(ex_v_stacked_div),
    DivHStacked,
    fn2code_string(ex_h_stacked_div),
    FlexT,

    H2("Padding and Positioning"),
    PaddingT,
    PositionT,
    title="Layout")

# Dividers

def ex_dividers():
    return Div(
        P("Small Divider"),
        Divider(cls=DividerT.sm),
        DivCentered(
            P("Vertical Divider"),
            Divider(cls=DividerT.vertical)),
        DivCentered("Icon Divider"),
        Divider(cls=DividerT.icon))

def ex_dividersplit():
    return DividerSplit(P("Or continue with", cls=TextPresets.muted_sm))

def ex_dividerline(): 
    return DividerLine()

docs_dividers = create_doc_section(
    Divider,
    DividerT,
    fn2code_string(ex_dividers),
    DividerSplit,
    fn2code_string(ex_dividersplit),
    DividerLine,
    fn2code_string(ex_dividerline),
    title="Dividers")

# Navigation

def ex_nav1():
    mbrs1 = [Li(A('Option 1'), cls='uk-active'), Li(A('Option 2')), Li(A('Option 3'))]
    return NavContainer(*mbrs1)

def ex_nav2():
    mbrs1 = [Li(A('Option 1'), cls='uk-active'), Li(A('Option 2')), Li(A('Option 3'))]
    mbrs2 = [Li(A('Child 1')), Li(A('Child 2')),Li(A('Child 3'))]

    return NavContainer(
        NavHeaderLi("NavHeaderLi"),
        *mbrs1,
        Li(A(href='')(Div("Subtitle Ex",NavSubtitle("NavSubtitle text to be shown")))),
        NavDividerLi(),
        NavParentLi(
            A('Parent Name'),
            NavContainer(*mbrs2,parent=False),
             ),
    )

def ex_navbar1():
    return NavBar(title='My Blog', 
                  nav_links={'Page1':'/rt1','Page2':'/rt2','Page3':'/rt3'}, 
                  active='Page2')

def ex_navbar2():
    nav_content = (Li(A(Input(placeholder='search'))), 
                   Li(A(UkIcon("rocket"))), Li(A('Page1',href='/rt1')), 
                   Li(A("Page2", href='/rt3')))
    
    return NavBar(title=DivLAligned(Img(src='/api_reference/logo.svg'),UkIcon('rocket',height=30,width=30)), 
                  nav_links=nav_content)

def ex_navbar3():
    mbrs1 = [Li(A('Option 1'), cls='uk-active'), Li(A('Option 2')), Li(A('Option 3'))]
    mbrs2 = [Li(A('Child 1')), Li(A('Child 2')),Li(A('Child 3'))]

    lnav = NavBarNav(
        Li(cls='uk-active')(A(NavBarSubtitle("Title","Subtitle"),href='')),
        Li(A("Parent",href=''),
          NavBarNavContainer(
              Li(cls='uk-active')(A("Active",href='')),
              Li(A("Item",href='')),
              Li(A("Item",href='')))),
        Li(A(Button("A Button",cls=ButtonT.primary))))

    rnav = NavBarNav(
        Li(A("DropDown",NavBarParentIcon(),href=''),
            NavBarNavContainer(
                NavHeaderLi("NavHeaderLi"),
                *mbrs1,
                Li(A(href='')(Div("Subtitle Ex",NavSubtitle("NavSubtitle text to be shown")))),
                NavDividerLi(),
                NavParentLi(
                    A('Parent Name'),
                    NavContainer(*mbrs2,parent=False)))),
        Li(A(Input(placeholder='search', cls='w-20'))))
    
    return NavBarContainer(
        NavBarLSide(lnav),
        NavBarCenter(Img(src='/api_reference/logo.svg')),
        NavBarRSide(rnav))

def ex_navdrop():
    return Div(
        Button("Open DropDown"),
        DropDownNavContainer(Li(A("Item 1",href=''),Li(A("Item 2",href='')))))

def ex_tabs1():
    return Container(
        TabContainer(
            Li(A("Active",href='#', cls='uk-active')),
            Li(A("Item",href='#')),
            Li(A("Item",href='#')),
            Li(A("Disabled",href='#', cls='uk-disabled')),
            uk_switcher='connect: #component-nav; animation: uk-animation-fade',
            alt=True),
         Ul(id="component-nav", cls="uk-switcher")(
            Li(H1("Tab 1")),
            Li(H1("Tab 2")),
            Li(H1("Tab 3"))))

def ex_tabs2():
    return Container(
        TabContainer(
            Li(A("Active",href='javascript:void(0);', cls='uk-active')),
            Li(A("Item",href='javascript:void(0);')),
            Li(A("Item",href='javascript:void(0);')),
            Li(A("Disabled", cls='uk-disabled'))))

docs_navigation = create_doc_section(
    H1("Nav, NavBar, DowDownNav, and Tab examples"),
    Divider(),
    H2("Nav"),
    fn2code_string(ex_nav1),
    fn2code_string(ex_nav2),
    H2("Navbars", id='navbars'),
    "Fully responsive simple navbar using the high level API and dicts to let MonsterUI do it all for you.  This will collapse to a hamburger menu on mobile devices",
    fn2code_string(ex_navbar1),
    "Pass your own components to the high level navbar API for more flexibility.  This will collapse to a hamburger menu on mobile devices",
    fn2code_string(ex_navbar2),
    "The final example shows a more complex navbar that lets you specify everything yourself.  You are responsible for everything, including responsiveness",
    fn2code_string(ex_navbar3),
    H2("Drop Down Navs"),
    fn2code_string(ex_navdrop),
    H2("Tabs"),
    fn2code_string(ex_tabs2),
    P("A tabs can use any method of navigation (htmx, or href).  However, often these are use in conjunction with switchers do to this client side", cls=TextPresets.muted_sm),
    fn2code_string(ex_tabs1),
    H1("API Docs"),
    NavBar,
    TabContainer,
    NavContainer,
    NavT,
    NavCloseLi,
    NavSubtitle,
    NavHeaderLi,
    NavDividerLi,
    NavParentLi,
    NavBarCenter,
    NavBarRSide,
    NavBarLSide,
    NavBarContainer,
    NavBarNav,
    NavBarSubtitle,
    NavBarNavContainer,
    NavBarParentIcon,
    DropDownNavContainer,
    title="Navigation")

# Steps


def ex_steps2():
    return Steps(
        LiStep("Account Created", cls=StepT.primary),
        LiStep("Profile Setup", cls=StepT.neutral),
        LiStep("Verification", cls=StepT.neutral),
        cls="w-full")
def ex_steps3():
    return Steps(
    LiStep("Project Planning", cls=StepT.success, data_content="📝"),
    LiStep("Design Phase", cls=StepT.success, data_content="💡"),
    LiStep("Development", cls=StepT.primary, data_content="🛠️"),
    LiStep("Testing", cls=StepT.neutral, data_content="🔎"),
    LiStep("Deployment", cls=StepT.neutral, data_content="🚀"),
    cls=(StepsT.vertical, "min-h-[400px]"))

docs_steps = create_doc_section(
    fn2code_string(ex_steps2),
    fn2code_string(ex_steps3),
    H1("API Docs"),
    Steps,
    StepsT,
    LiStep,
    StepT,
    title="Steps")
# Tables

def ex_tables0():
    return Table(
        Thead(Tr(Th('Name'),    Th('Age'), Th('City'))),
        Tbody(Tr(Td('Alice'),   Td('25'),  Td('New York')),
              Tr(Td('Bob'),     Td('30'),  Td('San Francisco')),
              Tr(Td('Charlie'), Td('35'),  Td('London'))),
        Tfoot(Tr(Td('Total'),   Td('90'))))

def ex_tables1():
    header =  ['Name',    'Age', 'City']
    body   = [['Alice',   '25',  'New York'],
              ['Bob',     '30',  'San Francisco'],
              ['Charlie', '35',  'London']]
    footer =  ['Total',   '90']
    return TableFromLists(header, body, footer)

def ex_tables2():
    def body_render(k, v):
        match k.lower():
            case 'name': return Td(v, cls='font-bold')
            case 'age':  return Td(f"{v} years")
            case _:      return Td(v)

    header_data = ['Name',          'Age',     'City']
    body_data   =[{'Name': 'Alice', 'Age': 30, 'City': 'New York'},
                  {'Name': 'Bob',   'Age': 25, 'City': 'London'}]

    return TableFromDicts(header_data, body_data, 
        header_cell_render=lambda v: Th(v.upper()), 
        body_cell_render=body_render)

docs_tables = create_doc_section(
    fn2code_string(ex_tables0),
    fn2code_string(ex_tables1),
    fn2code_string(ex_tables2),
    Table,
    TableFromLists,
    TableFromDicts,
    TableT,
    Tbody,
    Th,
    Td,    
    title="Tables")

# Icons

def ex_dicebear():
    return DivLAligned(
        DiceBearAvatar('Isaac Flath',10,10),
        DiceBearAvatar('Aaliyah',10,10),
        DiceBearAvatar('Alyssa',10,10))

def ex_picsum():
    return Grid(PicSumImg(100,100), PicSumImg(100,100, blur=6),PicSumImg(100,100, grayscale=True))

def ex_icon():
    return Grid(
        UkIcon('chevrons-right', height=15, width=15),
        UkIcon('bug',            height=15, width=15),
        UkIcon('phone-call',     height=15, width=15),
        UkIcon('maximize-2',     height=15, width=15),
        UkIcon('thumbs-up',      height=15, width=15),)        

def ex_iconlink():
    return DivLAligned(
        UkIconLink('chevrons-right'),
        UkIconLink('chevrons-right', button=True, cls=ButtonT.primary))

docs_icons_images = create_doc_section(
    H1("Avatars"),
    fn2code_string(ex_dicebear),
    DiceBearAvatar,
    H1("PlaceHolder Images"),
    fn2code_string(ex_picsum),
    PicSumImg,
    H1("Icons"),
    P("Icons use Lucide icons - you can find a full list of icons in their docs.", cls=TextPresets.muted_sm),
    fn2code_string(ex_icon),
    UkIcon,
    fn2code_string(ex_iconlink),
    UkIconLink,
    title="Icons")

# Markdown

def ex_markdown():
    md = '''# Example Markdown

+ With **bold** and *italics*
+ With a [link](https://github.com)

### And a subheading

> This is a blockquote
'''
    return render_md(md)


def ex_applyclasses():
    return apply_classes('<h1>Hello, World!</h1><p>This is a paragraph</p>')

docs_markdown = create_doc_section(
    fn2code_string(ex_markdown),
    P("This uses the `apply_classes` function, which can be used to apply classes to html strings"),
    apply_classes,
    fn2code_string(ex_applyclasses),
    title="Markdown + HTML Frankification")

def ex_loading1():
    return Loading()

def ex_loading2():
    types = [LoadingT.spinner, LoadingT.dots, LoadingT.ring, LoadingT.ball, LoadingT.bars, LoadingT.infinity]
    sizes = [LoadingT.xs, LoadingT.sm, LoadingT.md, LoadingT.lg]
    rows = [Div(*[Loading((t,s)) for s in sizes], cls='flex gap-4') for t in types]
    return Div(*rows, cls='flex flex-col gap-4')

docs_loading = create_doc_section(
    fn2code_string(ex_loading1),
    fn2code_string(ex_loading2),
    Loading,
    LoadingT,
    title="Loading")

