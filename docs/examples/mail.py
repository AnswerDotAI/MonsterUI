"""FrankenUI Mail Example"""

from fasthtml.common import *
from monsterui.all import *
from fasthtml.svg import *
import pathlib, json
from datetime import datetime

def NavItem(icon, text, quantity=None):
    cls = 'flex items-center space-x-2 rounded-md px-3 py-2 text-sm font-medium hover:bg-accent hover:text-accent-foreground'
    content = [UkIcon(icon), Span(text)]
    if quantity:
        content.append(Span(quantity, cls='ml-auto text-background bg-primary rounded-full px-2 py-0.5 text-xs'))
    return Li(A(*content, href='#', cls=cls))

def NavGroup(items):
    return Nav(cls='uk-nav-default space-y-3')(*[NavItem(i, t, q) for i, t, q in items if q or t != 'Trash'])

sidebar_group1 = (('home', 'Inbox', '128'), ('file-text', 'Drafts', '9'), (' arrow-up-right', 'Sent', ''),
    ('ban', 'Junk', '23'), ('trash', 'Trash', ''), ('folder', 'Archive', ''))

sidebar_group2 = (('globe','Social','972'),('info','Updates','342'),('messages-square','Forums','128'),
    ('shopping-cart','Shopping','8'),('shopping-bag','Promotions','21'),)

def MailSbLi(icon, title, cnt): 
    return Li(A(DivLAligned(
        Span(UkIcon(icon)),Span(title),P(cnt,cls=TextFont.muted_sm),cls='space-x-2')))

sidebar = Container(NavContainer(
    NavHeaderLi(H3("Email")),
    Li(UkSelect(map(Option, ('alicia@example.com','alicia@gmail.com', 'alicia@yahoo.com')),cls='my-4')),
    *[MailSbLi(i, t, c) for i, t, c in sidebar_group1],
    NavDividerLi(),
    *[MailSbLi(i, t, c) for i, t, c in sidebar_group2],
    cls='space-y-6'))


mail_data = json.load(open(pathlib.Path('data/mail.json')))

def format_date(date_str):
    date_obj = datetime.fromisoformat(date_str)
    return date_obj.strftime("%Y-%m-%d %I:%M %p")

def MailItem(mail):
    cls_base = 'relative rounded-lg border border-border p-3 text-sm hover:bg-accent'
    cls = f"{cls_base} {'bg-muted' if mail == mail_data[0] else ''} {'tag-unread' if not mail['read'] else 'tag-mail'}"
    
    return Li(cls=cls)(
        Div(cls='flex w-full flex-col gap-1')(
            Div(cls='flex items-center')(
                Div(cls='flex items-center gap-2')(
                    Div(mail['name'], cls='font-semibold'),
                    Span(cls='flex h-2 w-2 rounded-full bg-blue-600') if not mail['read'] else ''),
                Div(format_date(mail['date']), cls='ml-auto text-xs')),
            A(mail['subject'], cls=TextFont.bold_sm, href=f"#mail-{mail['id']}"),
            Div(mail['text'][:100] + '...', cls=TextFont.muted_sm),
            Div(cls='flex items-center gap-2')(
                *[A(label, cls=f"uk-label relative z-10 {'uk-label-primary' if label == 'work' else ''}", href='#')
                  for label in mail['labels']])))

def MailList(mails): return Ul(cls='js-filter space-y-2 p-4 pt-0')(*[MailItem(mail) for mail in mails])

def MailContent():
    return Div(cls='flex flex-col',uk_filter="target: .js-filter")(
        Div(cls='flex px-4 py-2 ')(
            H3('Inbox'),
            TabContainer(Li(A("All Mail",href='#', role='button'),cls='uk-active', uk_filter_control="filter: .tag-mail"), 
                         Li(A("Unread",href='#', role='button'),                   uk_filter_control="filter: .tag-unread"), 
                         alt=True, cls='ml-auto max-w-40', )),
        Div(cls='flex flex-1 flex-col')(
            Div(cls='p-4')(
                Div(cls='uk-inline w-full')(
                    Span(cls='uk-form-icon text-muted-foreground')(UkIcon('search')),
                    Input(placeholder='Search'))),
            Div(cls='flex-1 overflow-y-auto max-h-[600px]')(MailList(mail_data))))

def IconNavItem(*d): return [Li(A(UkIcon(o[0],uk_tooltip=o[1]))) for o in d]  
def IconNav(*c,cls=''): return Ul(cls=f'uk-iconnav {cls}')(*c)

def MailDetailView(mail):
    return Div(cls='flex flex-col')(
        Div(cls='flex h-14 flex-none items-center border-b border-border p-2')(
            Div(cls='flex w-full justify-between')(
                Div(cls='flex gap-x-2 divide-x divide-border')(
                    IconNav(*IconNavItem(('folder','Archive'),('ban','Move to junk'),('trash','Move to trash'))),
                    IconNav(Li(A(UkIcon('clock'), uk_tooltip='Snooze')), cls='pl-2')),
                Div(cls='flex')(# divide-x divide-border gap-x-2
                    IconNav(
                        *IconNavItem(('reply','Reply'),('reply','Reply all'),('forward','Forward')),
                        Li(A(UkIcon('ellipsis-vertical',button=True))),
                        DropDownNavContainer(
                            Li(A("Mark as unread")),
                            Li(A("Star read")),
                            Li(A("Add Label")),
                            Li(A("Mute Thread"))))))),
        Div(cls='flex-1')(
            Div(cls='flex items-start p-4')(
                Div(cls='flex items-start gap-4 text-sm')(
                    Span(mail['name'][:2], cls='flex h-10 w-10 items-center justify-center rounded-full bg-muted'),
                    Div(cls='grid gap-1')(
                        Div(mail['name'], cls=TextT.bold),
                        Div(mail['subject'], cls='text-xs'),
                        Div(cls=TextT.small)(
                            Span('Reply-To:', cls=TextT.normal),
                            f" {mail['email']}"))),
                Div(format_date(mail['date']), cls=(TextFont.muted_sm,'ml-auto'))),
            Div(cls='flex-1 space-y-4 border-t border-border p-4 text-sm')(P(mail['text']))),
        Div(cls='flex-none space-y-4 border-t border-border p-4')(
            TextArea(id='message', placeholder=f"Reply {mail['name']}"),
            Div(cls='flex justify-between')(
                    LabelSwitch('Mute this thread',id='mute'), # cls='inline-flex items-center gap-x-2 text-xs'
                Button('Send', cls=ButtonT.primary))))

def mail_homepage():
    return Div(cls='flex divide-x divide-border')(
        sidebar,
        Grid(MailContent(),
             MailDetailView(mail_data[0]),
             cols=2, gap=0, cls='flex-1 divide-x divide-border'))

mail_homepage = mail_homepage()
