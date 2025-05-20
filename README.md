# MonsterUI

MonsterUI is a UI framework for FastHTML for building beautiful web interfaces with minimal code. It combines the simplicity of Python with the power of Tailwind. Perfect for data scientists, ML engineers, and developers who want to quickly turn their Python code into polished web apps without the complexity of traditional UI frameworks. Follows semantic HTML patterns when possible.

MonsterUI adds the following  Tailwind-based libraries [Franken UI](https://franken-ui.dev/) and [DaisyUI](https://daisyui.com/) to FastHTML, as well as Python's [Mistletoe](https://github.com/miyuchina/mistletoe) for Markdown, [HighlightJS](https://highlightjs.org/) for code highlighting, and [Katex](https://katex.org/) for latex support.

# Getting Started


## Installation

To install this library, uses

`pip install MonsterUI`

## Getting Started

### TLDR

Run `python file.py` on this to start:

``` python
from fasthtml.common import *
from monsterui.all import *

# Choose a theme color (blue, green, red, etc)
hdrs = Theme.blue.headers()

# Create your app with the theme
app, rt = fast_app(hdrs=hdrs)

@rt
def index():
    socials = (('github','https://github.com/AnswerDotAI/MonsterUI'),
               ('twitter','https://twitter.com/isaac_flath/'),
               ('linkedin','https://www.linkedin.com/in/isaacflath/'))
    return Titled("Your First App",
        Card(
            H1("Welcome!"),
            P("Your first MonsterUI app", cls=TextPresets.muted_sm),
            P("I'm excited to see what you build with MonsterUI!"),
            footer=DivLAligned(*[UkIconLink(icon,href=url) for icon,url in socials])))

serve()
```

## LLM context files

Using LLMs for development is a best practice way to get started and
explore. While LLMs cannot code for you, they can be helpful assistants.
You must check, refactor, test, and vet any code any LLM generates for
you - but they are helpful productivity tools. Take a look inside the
`llms.txt` file to see links to particularly useful context files!

- [llms.txt](https://raw.githubusercontent.com/AnswerDotAI/MonsterUI/refs/heads/main/docs/llms.txt): Links to what is included
- [llms-ctx.txt](https://raw.githubusercontent.com/AnswerDotAI/MonsterUI/refs/heads/main/docs/llms-ctx.txt): MonsterUI Documentation Pages
- [API list](https://raw.githubusercontent.com/AnswerDotAI/MonsterUI/refs/heads/main/docs/apilist.txt): API list for MonsterUI (included in llms-ctx.txt)
- [llms-ctx-full.txt](https://raw.githubusercontent.com/AnswerDotAI/MonsterUI/refs/heads/main/docs/llms-ctx-full.txt): Full context that includes all api reference pages as markdown

In addition you can add `/md` (for markdown) to a url to get a markdown representation and `/rmd` for rendered markdown representation (nice for looking to see what would be put into context.

### Step by Step

To get started, check out:

1.  Start by importing the modules as follows:

``` python
from fasthtml.common import *
from monsterui.all import *
```

2.  Instantiate the app with the MonsterUI headers

``` python
app = FastHTML(hdrs=Theme.blue.headers())

# Alternatively, using the fast_app method
app, rt = fast_app(hdrs=Theme.slate.headers())
```

> *The color option can be any of the theme options available out of the
> box*

> `katex` and `highlightjs` are not included by default. To include them set `katex=True` or `highlightjs=True` when calling `.headers`. (i.e. `Theme.slate.headers(katex=True)`)*

From here, you can explore the API Reference & examples to see how to
implement the components. You can also check out these demo videos to as
a quick start guide:

- MonsterUI [documentation page and Tutorial
  app](https://monsterui.answer.ai/tutorial_app)
- Isaac & Hamel : [Building his website’s team
  page](https://youtu.be/22Jn46-mmM0)
- Isaac & Audrey : [Building a blog](https://youtu.be/gVWAsywxLXE)
- Isaac : [Building a blog](https://youtu.be/22NJgfAqgko)

More resources and improvements to the documentation will be added here
soon!
