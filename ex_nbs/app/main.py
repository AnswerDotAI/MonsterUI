"""FrankenUI Tasks Example"""

# AUTOGENERATED! DO NOT EDIT! File to edit: ../99_main.ipynb.

# %% auto 0
__all__ = ['Iconnavfix', 'app', 'tasks', 'cards', 'dashboard', 'forms', 'music', 'auth', 'playground', 'mail', 'home']

# %% ../99_main.ipynb
from fasthtml.common import *
import fasthtml.common as fh
from fh_frankenui.components import *
from fh_frankenui.core import *
from fasthtml.components import Uk_theme_switcher

# %% ../99_main.ipynb
from tasks import tasks_homepage
from cards import cards_homepage
from dashboard import dashboard_homepage
from forms import forms_homepage
from music import music_homepage
from auth import auth_homepage
from playground import playground_homepage
from mail import mail_homepage

# %% ../99_main.ipynb
Iconnavfix = fh.Script('''
window.setEmptyATagSize = function() {
    const emptyATags = document.querySelectorAll('a:empty');
    emptyATags.forEach(tag => {
        tag.style.height = '0';
        tag.style.width = '0';
        tag.style.display = 'inline-block';
    });
}

// Run on load and after any dynamic content changes
window.addEventListener('load', setEmptyATagSize);
document.addEventListener('htmx:afterSettle', setEmptyATagSize);
''')

# %% ../99_main.ipynb
app = FastHTML(hdrs=(Iconnavfix,*Theme.blue.headers()),debug=True,default_hdrs=False)

# %% ../99_main.ipynb
@app.route('/tasks')
def tasks(): return tasks_homepage

@app.route('/cards')
def cards(): return cards_homepage

@app.route('/dashboard')
def dashboard(): return dashboard_homepage

@app.route('/forms')
def forms(): return forms_homepage

@app.route('/music')
def music(): return music_homepage

@app.route('/auth')
def auth(): return auth_homepage

@app.route('/playground')
def playground(): return playground_homepage

@app.route('/mail')
def mail(): return mail_homepage

# %% ../99_main.ipynb
@app.route('/')
def home():
    sidebar_items = ["Tasks", "Cards", "Dashboard", "Form", "Music", "Auth", "Playground", "Mail", "Theme"]

    sidebar = NavContainer(map(lambda x: Li(A(x)),sidebar_items),
                uk_switcher="connect: #main-nav; animation: uk-animation-fade",
                cls=(NavT.primary,"space-y-4 p-4 w-1/10"))

    content = Div(cls="flex-1")(
        Ul(id="main-nav", cls="uk-switcher w-full")(
            Li(tasks_homepage),
            Li(cards_homepage),
            Li(dashboard_homepage),
            Li(forms_homepage),
            Li(music_homepage),
            Li(auth_homepage),
            Li(playground_homepage),
            Li(mail_homepage),   
            Li(Uk_theme_switcher())
        ))
    return Body(cls="bg-background text-foreground")(Div(cls="flex w-full")(sidebar,content))          


# %% ../99_main.ipynb
serve()
