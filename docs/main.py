from fasthtml.common import *
from functools import partial
from monsterui.all import *
from fasthtml.components import Uk_theme_switcher
from utils import render_nb
from pathlib import Path
from toolslm.download import read_html,html2md
from starlette.responses import PlainTextResponse
import httpx

def _not_found(req, exc):
    _path = req.url.path.rstrip('/')
    if _path.endswith('.md') or _path.endswith('.rmd'):
        url = f'https://monsterui.answer.ai{_path[:-3].rstrip("/").rstrip(".")}'.rstrip("/").rstrip(".")
        try:
            r = httpx.head(url, follow_redirects=True, timeout=1.0)
            if r.status_code < 400:  # Accept 2xx and 3xx status codes
                if _path.endswith('.rmd') or _path.endswith('/rmd'): return Container(render_md(read_html(url, sel='#content')))
                elif _path.endswith('.md') or _path.endswith('/md'): return PlainTextResponse(read_html(url, sel='#content'))
        except (httpx.TimeoutException, httpx.NetworkError): pass    
    return _create_page(
        Container(Card(CardBody(H1("404 - Page Not Found"), P("The page you're looking for doesn't exist.")))),
        req,
        None)


app,rt = fast_app(exception_handlers={404:_not_found}, pico=False, 
                  hdrs=(*Theme.blue.headers(highlightjs=True,apex_charts=True), Link(rel="icon", type="image/x-icon", href="/favicon.ico"),
                        Link(rel="stylesheet", href="/custom_theme.css", type="text/css")), 
                  )

def is_htmx(request=None): 
    "Check if the request is an HTMX request"
    return request and 'hx-request' in request.headers

def _create_page(content, # The content to display (without the layout/sidebar)
                 request, # Request object to determine if HTMX request
                 sidebar_section, # The open section on the sidebar
                 ):
    "Makes page load sidebar if direct request, otherwise loads content only via HTMX"
    if is_htmx(request): return content
    else: return with_layout(sidebar_section, content)

def with_layout(sidebar_section, content):
    "Puts the sidebar and content into a layout"
    return Title(f"MonsterUI"), Div(cls="flex flex-col md:flex-row w-full")(
            Button(UkIcon("menu",50,50,cls='mt-4'), cls="md:hidden mb-4", data_uk_toggle="target: #mobile-sidebar"),
            Div(sidebar(sidebar_section), id='mobile-sidebar', hidden=True),
            Div(cls="md:flex w-full")(
                Div(sidebar(sidebar_section), cls="hidden md:block w-1/5 max-w-52"),
                Div(content, cls='md:w-4/5 w-full mr-5', id="content", )))


###
# Build the Example Pages
###
 
from examples.tasks import index as tasks_homepage
from examples.cards import index as cards_homepage
from examples.dashboard import index as dashboard_homepage
from examples.forms import index as forms_homepage
from examples.music import index as music_homepage
from examples.auth import index as auth_homepage
from examples.playground import index as playground_homepage
from examples.mail import index as mail_homepage
from examples.scrollspy import index as scrollspy_homepage
from examples.ticket import index as ticket_homepage
def _example_route(name, homepage, o:str, request=None):
    match o:
        case 'code' | 'rmd': return Div(render_md(f'''```python\n\n{open(f'examples/{name}.py').read()}\n\n```'''))
        case 'md': return PlainTextResponse(open(f'examples/{name}.py').read())
        case _: return _create_example_page(homepage, request)

_create_example_page = partial(_create_page, sidebar_section='Examples')

@rt('/scrollspy')
@rt('/scrollspy/{o}')
def scrollspy(o:str='', request=None): return _example_route('scrollspy', Div(DivRAligned(A("See Code",href='/scrollspy/code',cls='m-4 uk-btn'+ButtonT.default)),scrollspy_homepage()), o, request)

@rt('/ticket')
@rt('/ticket/{o}')
def ticket(o:str='', request=None): return _example_route('ticket', Div(DivRAligned(A("See Code",href='/ticket/code',cls='m-4 uk-btn'+ButtonT.default)),ticket_homepage()), o, request)

@rt('/tasks')
@rt('/tasks/{o}')
def tasks(o:str='', request=None): return _example_route('tasks', Div(DivRAligned(A("See Code",href='/tasks/code',cls='m-4 uk-btn'+ButtonT.default)),tasks_homepage()), o, request)

@rt('/cards')
@rt('/cards/{o}')
def cards(o:str, request=None): return _example_route('cards', Div(DivRAligned(A("See Code",href='/cards/code',cls='m-4 uk-btn'+ButtonT.default)),cards_homepage()), o, request)

@rt('/dashboard')
@rt('/dashboard/{o}')
def dashboard(o:str, request=None): return _example_route('dashboard', Div(DivRAligned(A("See Code",href='/dashboard/code',cls='m-4 uk-btn'+ButtonT.default)),dashboard_homepage()), o, request)

@rt('/forms')
@rt('/forms/{o}')
def forms(o:str, request=None): return _example_route('forms', Div(DivRAligned(A("See Code",href='/forms/code',cls='m-4 uk-btn'+ButtonT.default)),forms_homepage()), o, request)

@rt('/music')
@rt('/music/{o}')
def music(o:str, request=None): return _example_route('music', Div(DivRAligned(A("See Code",href='/music/code',cls='m-4 uk-btn'+ButtonT.default)),music_homepage()), o, request)

@rt('/auth')
@rt('/auth/{o}')
def auth(o:str, request=None): return _example_route('auth', Div(DivRAligned(A("See Code",href='/auth/code',cls='m-4 uk-btn'+ButtonT.default)),auth_homepage()), o, request)

@rt('/playground')
@rt('/playground/{o}')
def playground(o:str, request=None): return _example_route('playground', Div(DivRAligned(A("See Code",href='/playground/code',cls='m-4 uk-btn'+ButtonT.default)),playground_homepage()), o, request)

@rt('/mail')
@rt('/mail/{o}')    
def mail(o:str, request=None): return _example_route('mail', Div(DivRAligned(A("See Code",href='/mail/code',cls='m-4 uk-btn'+ButtonT.default)),mail_homepage()), o, request)

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
    return _create_page(Container(content), request=request, sidebar_section='API Reference')

@rt('/api_ref/{o}/md')
def api_route_md(request, o:str):
    if o not in reference_fns: raise HTTPException(404)
    content = getattr(api_reference, o)()
    return PlainTextResponse(html2md(to_xml(content)))

@rt('/api_ref/{o}rmd')
def api_route_md(request, o:str):
    if o not in reference_fns: raise HTTPException(404)
    content = getattr(api_reference, o)()
    return Div(render_md(html2md(to_xml(content))))

###
# Build the Guides Pages
###
@rt('/tutorial_spacing')
@rt('/tutorial_spacing/{o}')
def tutorial_spacing(o:str='', request=None): 
    if o=='md': return PlainTextResponse(read_html(f'https://monsterui.answer.ai/tutorial_spacing', sel='#content'))
    if o=='rmd': return Div(render_md(read_html(f'https://monsterui.answer.ai/tutorial_spacing', sel='#content')))
    return _create_page(render_nb('guides/Spacing.ipynb'), request, 'Guides')
@rt('/tutorial_layout')
@rt('/tutorial_layout/{o}')
def tutorial_layout(o:str='', request=None): 
    if o=='md': return PlainTextResponse(read_html(f'https://monsterui.answer.ai/tutorial_layout', sel='#content'))
    if o=='rmd': return Div(render_md(read_html(f'https://monsterui.answer.ai/tutorial_layout', sel='#content')))
    return _create_page(render_nb('guides/Layout.ipynb'), request,  'Guides',)

###
# Build the Theme Switcher Page
###

@rt
def theme_switcher(request): 
    return _create_page(Div(ThemePicker(custom_themes=[("Grass", "#10b981")]),cls="p-12"), request, None)

###
# Build the Getting Started Pages
###

gs_path = Path('getting_started')

@rt('/tutorial_app')
@rt('/tutorial_app/{o}')
def tutorial_app(o:str='', request=None):
    pass
    if o=='md': return PlainTextResponse(read_html(f'https://monsterui.answer.ai/tutorial_app', sel='#content'))
    if o=='rmd': return Div(render_md(read_html(f'https://monsterui.answer.ai/tutorial_app', sel='#content')))
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
            cls=ListT.decimal+TextT.lg
        ),
        render_md("""> Tip:  Try adding `import fasthtml.common as fh`, so you can replace things with the base fasthtml components to see what happens!
For example, try replacing `H4` with `fh.H4` or `Button` with `fh.Button`."""),
        Divider(),
        app_rendered)
    return _create_page(content, request, 'Getting Started')

@rt('/')
@rt('/{o}')
def index(o:str='', request=None):
    if o=='md': return PlainTextResponse(read_html(f'https://monsterui.answer.ai/getting_started', sel='#content'))
    if o=='rmd': return Div(render_md(read_html(f'https://monsterui.answer.ai/getting_started', sel='#content')))
    content = Container(render_md(open(gs_path/'GettingStarted.md').read()))
    return _create_page(content, request,  'Getting Started')

###
# Build the Sidebar
###

def sidebar(open_section):
    def create_li(title, href):
        return Li(A(title,hx_target="#content", hx_get=href, hx_push_url='true'))

    return NavContainer(
        NavParentLi(
            A(DivFullySpaced("Getting Started", )),
            NavContainer(create_li("Getting Started", index),
                         create_li("Tutorial App", tutorial_app),
                         parent=False),
            cls='uk-open' if open_section=='Getting Started' else ''
        ),
        NavParentLi(
            A(DivFullySpaced("API Reference", )),
            NavContainer(
                *[create_li(fname2title(o), f"/api_ref/{o}") for o in reference_fns],
                parent=False,  
            ),
            cls='uk-open' if open_section=='API Reference' else ''
        ),
        NavParentLi(
            A(DivFullySpaced('Guides', )),
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
            A(DivFullySpaced('Examples', )),
            NavContainer(
                *[create_li(title, href) for title, href in [
                    ('Task', '/tasks/'),
                    ('Card', '/cards/'),
                    ('Dashboard', '/dashboard/'),
                    ('Form', '/forms/'),
                    ('Music', '/music/'),
                    ('Auth', '/auth/'),
                    ('Playground', '/playground/'),
                    ('Mail', '/mail/'),
                    ('Ticket', '/ticket/'),
                    ('Scrollspy', '/scrollspy/'),
                ]],
                parent=False
            ),
            cls='uk-open' if open_section=='Examples' else ''
        ),
        create_li("Theme", theme_switcher),
        uk_nav=True,
        cls=(NavT.primary, "space-y-4 p-4 w-full md:w-full")
    )

serve()
