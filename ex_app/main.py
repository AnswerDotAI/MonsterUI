"""FrankenUI Tasks Example"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../ex_nbs/99_main.ipynb.

# %% auto 0
__all__ = ['hdrs', 'app', 'tasks', 'cards', 'auth', 'playground', 'Navbar', 'NavItem', 'NavDropdown', 'UkNavBar', 'home']

# %% ../ex_nbs/99_main.ipynb 2
from fasthtml.common import *
from fh_frankenui.components import *

# %% ../ex_nbs/99_main.ipynb 3
try:
    from fh_frankenui_examples.tasks import tasks_homepage
    from fh_frankenui_examples.cards import cards_homepage
    from fh_frankenui_examples.dashboard import dashboard_homepage
    from fh_frankenui_examples.forms import forms_homepage
    from fh_frankenui_examples.music import music_homepage
    from fh_frankenui_examples.auth import auth_homepage
    from fh_frankenui_examples.playground import playground_homepage
except ImportError:
    from tasks import tasks_homepage
    from cards import cards_homepage
    from dashboard import dashboard_homepage
    from forms import forms_homepage
    from music import music_homepage
    from auth import auth_homepage
    from playground import playground_homepage

# %% ../ex_nbs/99_main.ipynb 9
hdrs = (Script(src="https://cdn.tailwindcss.com"),
        Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit.min.js"),
        Script(src="https://cdn.jsdelivr.net/npm/uikit@3.21.6/dist/js/uikit-icons.min.js"),
        Script(type="module", src="https://unpkg.com/franken-wc@0.0.6/dist/js/wc.iife.js"),
        Link(rel="stylesheet", href="https://unpkg.com/franken-wc@0.0.6/dist/css/blue.min.css"),)

# %% ../ex_nbs/99_main.ipynb 10
app = FastHTML(hdrs=hdrs,debug=True,default_hdrs=False)

# %% ../ex_nbs/99_main.ipynb 12
@app.route('/tasks')
def tasks(): return tasks_homepage

@app.route('/cards')
def cards(): return cards_homepage

@app.route('/forms')
def cards(): return forms_homepage

@app.route('/dashboard')
def cards(): return dashboard_homepage

@app.route('/music')
def cards(): return music_homepage

@app.route('/auth')
def auth(): return auth_homepage

@app.route('/playground')
def playground(): return playground_homepage

# %% ../ex_nbs/99_main.ipynb 15
def Navbar(*c, left=(), center=(), right=(), container=True, transparent=False, sticky=False, cls=(), **kwargs):
    nav_cls = f"uk-navbar-container{'uk-navbar-transparent' if transparent else ''}"
    nav = Nav(cls=nav_cls, uk_navbar=True, **kwargs)(
        Div(cls='uk-navbar-left')(*left) if left else None,
        Div(cls='uk-navbar-center')(*center) if center else None,
        Div(cls='uk-navbar-right')(*right) if right else None,
        *c
    )
    sticky_attrs = {'uk-sticky': 'sel-target: .uk-navbar-container; cls-active: uk-navbar-sticky'} if sticky else {}
    return Div(cls=f"uk-container {stringify(cls)}" if container else stringify(cls), **sticky_attrs)(nav)

def NavItem(label, href='#', active=False, parent=False, cls=()):
    item_cls = f"{'uk-active' if active else ''} {'uk-parent' if parent else ''} {stringify(cls)}".strip()
    return Li(cls=item_cls)(A(href=href)(label))

def NavDropdown(label, items, cls=()):
    return Li(cls=f"uk-parent {stringify(cls)}".strip())(
        A(href='#')(label),
        Div(cls='uk-navbar-dropdown')(Ul(cls='uk-nav uk-navbar-dropdown-nav')(*items))
    )

# %% ../ex_nbs/99_main.ipynb 16
def UkNavBar(*lis):
    return Nav(cls='uk-navbar-left')(
        Ul(cls='uk-navbar-nav')(
        *lis
        ))

# %% ../ex_nbs/99_main.ipynb 18
@app.route('/')
def home():
    nav_items = (('Home', '/'), ('Tasks', '/tasks'), 
                 ('Cards', '/cards'), ('Dashboard', '/dashboard'),
                ('Forms', '/forms'), ('Music', '/music'), ('Authentication', '/auth'),
                ('Playground', '/playground')
                )
    nav_items = [Li()(A(href=r)(n)) for (n,r) in nav_items]
    
    navbar = UkNavBar(*nav_items)
    content = Div(cls='uk-container uk-margin-top')(
        H1('FrankenUI Examples in FastHTML'),
        P('This site showcases the FrankenUI components rebuilt using FastHTML, demonstrating the power and flexibility of our Python wrapper.'),
        P('Explore the Tasks and Cards pages to see examples of FrankenUI components implemented with FastHTML.')
    )
    return navbar, content

# %% ../ex_nbs/99_main.ipynb 19
serve()
