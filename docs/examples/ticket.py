"""MonsterUI Help Desk Example - Professional Dashboard with DaisyUI components"""
from fasthtml.common import *
from monsterui.all import *
from datetime import datetime

app, rt = fast_app(hdrs=Theme.blue.headers(daisy=True))

def TicketSteps(step):
    return Steps(
        LiStep("Submitted", data_content="📝",
               cls=StepT.success if step > 0 else StepT.primary if step == 0 else StepT.neutral),
        LiStep("In Review", data_content="🔎",
               cls=StepT.success if step > 1 else StepT.primary if step == 1 else StepT.neutral),
        LiStep("Processing", data_content="⚙️",
               cls=StepT.success if step > 2 else StepT.primary if step == 2 else StepT.neutral),
        LiStep("Resolved", data_content="✅",
               cls=StepT.success if step > 3 else StepT.primary if step == 3 else StepT.neutral),
        cls="w-full")

def StatusBadge(status):
    styles = {'high': AlertT.error, 'medium': AlertT.warning,'low': AlertT.info}
    alert_type = styles.get(status, AlertT.info)
    return Alert(f"{status.title()} Priority", cls=(alert_type,"w-32 shadow-sm"))

def TicketCard(id, title, description, status, step, department):
    return Card(
        CardHeader(
            DivFullySpaced(
                Div(H3(f"#{id}", cls=TextT.muted), 
                    H4(title), 
                    cls='space-y-2'),
                StatusBadge(status))),
        CardBody(
            P(description, cls=(TextT.muted, "mb-6")),
            DividerSplit(cls="my-6"),
            TicketSteps(step),
            DividerSplit(cls="my-6"), 
            DivFullySpaced(
                Div(Strong("Department"),
                    P(department),
                    cls=('space-y-3', TextPresets.muted_sm)),
                Div(Strong("Last Updated"),
                    P(Time(datetime.now().strftime('%b %d, %H:%M'))),
                    cls=('space-y-3', TextPresets.muted_sm)),
                Button("View Details", cls=ButtonT.primary),
                cls='mt-6')),
        cls=CardT.hover)

def NewTicketModal():
    return Modal(
        ModalHeader(H3("Create New Support Ticket")),
        ModalBody(
            Alert(
                DivLAligned(UkIcon("info"), Span("Please provide as much detail as possible to help us assist you quickly.")),
                cls=(AlertT.info,"mb-4")),
            Form(
                Grid(LabelInput("Title", id="title", placeholder="Brief description of your issue"),
                     LabelSelect(Options("IT Support", "HR", "Facilities", "Finance"), label="Department", id="department")),
                LabelSelect(Options("Low", "Medium", "High"), label="Priority Level",  id="priority"),
                LabelTextArea("Description", id="description", placeholder="Please provide detailed information about your issue"),
                DivRAligned(
                    Button("Cancel", cls=ButtonT.ghost, data_uk_toggle="target: #new-ticket"),
                    Button(Loading(cls=LoadingT.spinner), "Submit Ticket", cls=ButtonT.primary, data_uk_toggle="target: #success-toast; target: #new-ticket")),
                cls='space-y-8')),
            id="new-ticket")

@rt
def index():
    tickets = [
        {'id': "TK-1001", 'title': "Cloud Storage Access Error", 
         'description': "Unable to access cloud storage with persistent authorization errors. Multiple users affected across marketing department.",
         'status': 'high', 'step': 2, 'department': 'IT Support'},
        {'id': "TK-1002", 'title': "Email Integration Issue", 
         'description': "Exchange server not syncing with mobile devices. Affecting external client communications.",
         'status': 'medium', 'step': 1, 'department': 'IT Support'},
        {'id': "TK-1003", 'title': "Office Equipment Setup", 
         'description': "New department printer needs configuration and network integration. Required for upcoming client presentation.",
         'status': 'low', 'step': 0, 'department': 'Facilities'}
    ]

    return Title("Help Desk Dashboard"), Container(
        Section(
            DivFullySpaced(
                H2("Active Tickets"),
                Button(UkIcon("plus-circle", cls="mr-2"), "New Ticket", cls=ButtonT.primary, data_uk_toggle="target: #new-ticket"),
                cls='mb-8'),
            Grid(*[TicketCard(**ticket) for ticket in tickets], cols=1),
            cls="my-6"),
        NewTicketModal(),
        Toast(DivLAligned(UkIcon('check-circle', cls='mr-2'), "Ticket submitted successfully! Our team will review it shortly."), id="success-toast", alert_cls=AlertT.success, cls=(ToastHT.end, ToastVT.bottom)),
        Loading(htmx_indicator=True, type=LoadingT.dots, cls="fixed top-0 right-0 m-4"),
        cls="mx-auto max-w-7xl"
    )   

serve()