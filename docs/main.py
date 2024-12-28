from fasthtml.common import *
from functools import partial
from monsterui.all import *
from fasthtml.components import Uk_theme_switcher
from utils import hjs, render_nb
from pathlib import Path

# Setup the app



app,rt = fast_app(pico=False, hdrs=(*Theme.blue.headers(),*hjs, Link(rel="icon", type="image/x-icon", href="/favicon.ico")))

def is_htmx(request=None): 
    "Check if the request is an HTMX request"
    return request and 'hx-request' in request.headers

def _create_page(content, # The content to display (without the layout/sidebar)
                 request, # Request object to determine if HTMX request
                 sidebar_section # The open section on the sidebar
                 ):
    "Makes page load sidebar if direct request, otherwise loads content only via HTMX"
    if is_htmx(request): return content
    else: return with_layout(sidebar_section, content)

def with_layout(sidebar_section, content):
    "Puts the sidebar and content into a layout"
    return Title(f"MonsterUI {sidebar_section.removeprefix('docs_')}"), Div(cls="flex flex-col md:flex-row w-full")(
            Button(UkIcon("menu",50,50,cls='mt-4'), cls="md:hidden mb-4", uk_toggle="target: #mobile-sidebar"),
            Div(sidebar(sidebar_section), id='mobile-sidebar', hidden=True),
            Div(cls="md:flex w-full")(
                Div(sidebar(sidebar_section), cls="hidden md:block w-1/5"),
                Div(content, cls='md:w-4/5 w-full mr-5', id="content", )))


###
# Build the Example Pages
###
 
from examples.tasks import tasks_homepage
from examples.cards import cards_homepage
from examples.dashboard import dashboard_homepage
from examples.forms import forms_homepage
from examples.music import music_homepage
from examples.auth import auth_homepage
from examples.playground import playground_homepage
from examples.mail import mail_homepage

_create_example_page = partial(_create_page, sidebar_section='Examples')
@rt
def tasks(request=None):      return _create_example_page(tasks_homepage,     request)
@rt
def cards(request=None):      return _create_example_page(cards_homepage,     request)
@rt
def dashboard(request=None):  return _create_example_page(dashboard_homepage, request)
@rt
def forms(request=None):      return _create_example_page(forms_homepage,     request)
@rt 
def music(request=None):      return _create_example_page(music_homepage,     request)
@rt
def auth(request=None):       return _create_example_page(auth_homepage,      request)
@rt
def playground(request=None): return _create_example_page(playground_homepage,request)
@rt
def mail(request=None):       return _create_example_page(mail_homepage,      request) 

###
# Build the API Reference Pages
###

import api_reference.api_reference as api_reference

def fname2title(ref_fn_name): return ref_fn_name[5:].replace('_',' | ').title() 

reference_fns = L([o for o in dir(api_reference) if o.startswith('docs_')])

@rt('/api_ref/{o}')
def api_route(request, o:str):
    if o not in reference_fns: raise HTTPException(404)
    content = getattr(api_reference, o)()
    title = fname2title(o)
    return _create_page(Container(content), 
                        request=request, 
                        sidebar_section='API Reference')


###
# Build the Guides Pages
###

@rt
def tutorial_spacing(request=None): return _create_page(render_nb('guides/Spacing.ipynb'), request, 'Guides')

@rt
def tutorial_layout(request=None): return _create_page(render_nb('guides/Layout.ipynb'), request, 'Guides')

###
# Build the Theme Switcher Page
###

@rt
def theme_switcher(request): 
    return _create_page(Div(Uk_theme_switcher(),cls="p-12"), request, None)

###
# Build the Getting Started Pages
###

gs_path = Path('getting_started')
@rt
def getting_started(request=None):
    content = Container(render_md(open(gs_path/'GettingStarted.md').read()))
    return _create_page(content, request, 'Getting Started')

from getting_started.StylingRulesOfThumb import page as StylingRulesOfThumb

@rt
def styling_rules_of_thumb(request=None): 
    content = Container(StylingRulesOfThumb())
    return _create_page(content, request, 'Getting Started')

@rt
def index(): return getting_started()

@rt
def tutorial_app(request=None):
    app_code = open(gs_path/'app_product_gallery.py').read()
    app_rendered = Div(Pre(Code(app_code)))
    content = Container(cls='space-y-4')(
        H1("Tutorial App"),
        render_md("""This is a heavily commented example of a product gallery app built with MonsterUI for those that like to learn by example.  \
          This tutorial app assumes you have some familiarity with fasthtml apps already, so focuses on what MonsterUI adds on top of fasthtml.
          To make the most out of this tutorial, you should follow these steps:"""),
        Ol(
            Li("Briefly read through this to get an overview of what is happening, without focusing on any details"),
            Li("Install fasthtml and MonsterUI"),
            Li("Copy the code into your own project locally and run it using `python app.py`"),
            Li("Go through the code in detail to understand how it works by experimenting with changing things"),
            cls=ListT.decimal
        ),
        render_md("""> Tip:  Try adding `import fasthtml.common as fh`, so you can replace things with the base fasthtml components to see what happens!
For example, try replacing `H4` with `fh.H4` or `Button` with `fh.Button`."""),
        Divider(),
        app_rendered)
    return _create_page(content, request, 'Getting Started')



###
# Build the Sidebar
###

def sidebar(open_section):
    def create_li(title, href):
        return Li(A(title,hx_target="#content", hx_get=href, hx_trigger='mousedown', hx_push_url='true', href=''))

    return NavContainer(
        NavParentLi(
            A(DivFullySpaced("Getting Started", NavBarParentIcon())),
            NavContainer(create_li("Getting Started", getting_started),
                         create_li("Tutorial App", tutorial_app),
                        #  create_li("Styling", styling_rules_of_thumb),
                         parent=False),
            cls='uk-open' if open_section=='Getting Started' else ''
        ),
        NavParentLi(
            A(DivFullySpaced("API Reference", NavBarParentIcon())),
            NavContainer(
                *[create_li(fname2title(o), f"/api_ref/{o}") for o in reference_fns],
                parent=False,  
            ),
            cls='uk-open' if open_section=='API Reference' else ''
        ),
        NavParentLi(
            A(DivFullySpaced('Guides', NavBarParentIcon())),
            NavContainer(
                *[create_li(title, href) for title, href in [
                    ('Spacing', tutorial_spacing),
                    ('Layout', tutorial_layout),
                ]],
                parent=False
            ),
            cls='uk-open' if open_section=='Guides' else ''
        ),
        
        NavParentLi(
            A(DivFullySpaced('Examples', NavBarParentIcon())),
            NavContainer(
                *[create_li(title, href) for title, href in [
                    ('Task', tasks),
                    ('Card', cards),
                    ('Dashboard', dashboard),
                    ('Form', forms),
                    ('Music', music),
                    ('Auth', auth),
                    ('Playground', playground),
                    ('Mail', mail),
                ]],
                parent=False
            ),
            cls='uk-open' if open_section=='Examples' else ''
        ),
        create_li("Theme", theme_switcher),
        uk_nav=True,
        cls=(NavT.primary, "space-y-4 p-4 w-full md:w-full")
    )


@rt
def _default_button():
    # Route used in release blog post
    return Button("Click me")

@rt
def _primary_button():
    # Routed used in release blog post
    return Button("Click me", cls=ButtonT.primary)

def _layout_ex():
    # Route used in release blog post


    return Div(
        DivLAligned(
            Button("Export"),
            Button("New Entry", cls=ButtonT.primary)),
            Grid(map(TeamCard, products), cols_lg=3))

serve()
