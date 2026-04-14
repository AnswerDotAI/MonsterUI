"""FrankenUI Dashboard Example built with MonsterUI (original design by ShadCN)"""

from fasthtml.common import * # Bring in all of fasthtml
import fasthtml.common as fh # Used to get unstyled components
from monsterui.all import * # Bring in all of monsterui, including shadowing fasthtml components with styled components
from fasthtml.svg import *
import numpy as np
import plotly.express as px
import pandas as pd
import numpy as np

app, rt = fast_app(hdrs=Theme.blue.headers())

def generate_chart(num_points=30):
    df = pd.DataFrame({
        'Date': pd.date_range('2024-01-01', periods=num_points),
        'Revenue': np.random.normal(100, 10, num_points).cumsum(),
        'Users': np.random.normal(80, 8, num_points).cumsum(), 
        'Growth': np.random.normal(60, 6, num_points).cumsum()})
    
    fig = px.line(df, x='Date', y=['Revenue', 'Users', 'Growth'],  template='plotly_white', line_shape='spline')
    
    fig.update_traces(mode='lines+markers')
    fig.update_layout(
        margin=dict(l=20, r=20, t=20, b=20), hovermode='x unified',
        showlegend=True, legend=dict(orientation='h', yanchor='bottom', y=1.02,  xanchor='right', x=1),
        plot_bgcolor='rgba(0,0,0,0)', paper_bgcolor='rgba(0,0,0,0)',
        xaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)'),
        yaxis=dict(showgrid=True, gridwidth=1, gridcolor='rgba(0,0,0,0.1)'))
    
    return fig.to_html(include_plotlyjs=True, full_html=False, config={'displayModeBar': False})

def InfoCard(title, value, change): return Card(H3(value),P(change, cls=TextPresets.muted_sm), header = H4(title))

rev = InfoCard("Total Revenue", "$45,231.89", "+20.1% from last month")
sub = InfoCard("Subscriptions", "+2350", "+180.1% from last month")
sal = InfoCard("Sales", "+12,234", "+19% from last month")
act = InfoCard("Active Now", "+573", "+201 since last hour")

info_card_data = [("Total Revenue", "$45,231.89", "+20.1% from last month"),
                   ("Subscriptions", "+2350", "+180.1% from last month"),
                   ("Sales", "+12,234", "+19% from last month"),
                   ("Active Now", "+573", "+201 since last hour")]

top_info_row = Grid(*[InfoCard(*row) for row in info_card_data])

def AvatarItem(name, email, amount):
    return DivFullySpaced(
        DivLAligned(
            DiceBearAvatar(name, 9,9),
            Div(Strong(name, cls=TextT.sm), 
                Address(A(email,href=f'mailto:{email}')))),
        fh.Data(amount, cls="ml-auto font-medium", value=amount[2:]))

recent_sales = Card(
    Div(cls="space-y-8")(
        *[AvatarItem(n,e,d) for (n,e,d) in (
            ("Olivia Martin",   "olivia.martin@email.com",   "+$1,999.00"),
            ("Jackson Lee",     "jackson.lee@email.com",     "+$39.00"),
            ("Isabella Nguyen", "isabella.nguyen@email.com", "+$299.00"),
            ("William Kim",     "will@email.com",            "+$99.00"),
            ("Sofia Davis",     "sofia.davis@email.com",     "+$39.00"))]),
    header=Div(H3("Recent Sales"),Subtitle("You made 265 sales this month.")),
    cls='col-span-3')

teams = [["Alicia Koch"],['Acme Inc', 'Monster Inc.'],['Create a Team']]

opt_hdrs = ["Personal", "Team", ""]

team_dropdown = Div(Select(
    Optgroup(Option("Alicia Koch"), label="Personal Account"),
    Optgroup(Option("Acme Inc"), Option("Monster Inc."), label="Teams"),
    Option("Create a Team")),
    cls='flex items-center')

hotkeys = [('Profile','⇧⌘P'),('Billing','⌘B'),('Settings','⌘S'),('New Team', ''), ('Logout', '')]

def NavSpacedLi(t,s): return NavCloseLi(A(DivFullySpaced(P(t),P(s,cls=TextPresets.muted_sm))))

avatar_dropdown = Div(
      DiceBearAvatar('Alicia Koch',8,8),
      DropDownNavContainer(
          NavHeaderLi('sveltecult',NavSubtitle("leader@sveltecult.com")),
          *[NavSpacedLi(*hk) for hk in hotkeys],))

top_nav = NavBar(
    team_dropdown, *map(A, ["Overview", "Customers", "Products", "Settings"]),
    brand=DivLAligned(avatar_dropdown, Input(placeholder='Search')))

@rt
def index():
    return Title("Dashboard Example"), Container(
        top_nav,
        H2('Dashboard'),
        TabContainer(
            Li(A("Overview"),cls='uk-active'),
            *map(lambda x: Li(A(x)), ["Analytics", "Reports", "Notifications"]),
            alt=True),
        top_info_row,
        Grid(
            Card(Safe(generate_chart(100)), cls='col-span-4'),
            recent_sales,
            gap=4,cols_xl=7,cols_lg=7,cols_md=1,cols_sm=1,cols_xs=1),
        cls=('space-y-4', ContainerT.xl))

serve()
