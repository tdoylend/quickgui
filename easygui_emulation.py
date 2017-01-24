from .app import Application
from .text import SimpleText,MultilineText
from .button import Button
from .window import Window
from .splitter import ProportionalVerticalSplitter
from .entry import TextEntry
from .obj import BorderPanel

DEFAULT_FONT = 'Helvetica,Arial'

DEFAULT_FONT_SIZE = 20

def msgbox(msg='(Your message goes here)',title=' ',ok_button='OK'):
    
    messagebox_provider = MultilineText if '\n' in msg else SimpleText
    message = messagebox_provider(msg,DEFAULT_FONT,DEFAULT_FONT_SIZE)
    message_min = message.suggest_min_metrics()

    window_width = int(message_min.width * 1.25)
    window_height = int(message_min.height * 5)

    window = Window(title,(window_width,window_height))

    application = Application(window)

    splitter = ProportionalVerticalSplitter(0.75)

    splitter.add_child_top(message)
    
    button = Button(
        ok_button,
        lambda event_producer,position,rect,button: application.suggest_quit(return_value=ok_button),
        DEFAULT_FONT,
        DEFAULT_FONT_SIZE
    )

    splitter.add_child_bottom(button)

    window.add_child(splitter)

    return application.run()

def enterbox(msg='Enter something.', title=' ', default='',strip=True):
    messagebox_provider = MultilineText if '\n' in msg else SimpleText
    message = messagebox_provider(msg,DEFAULT_FONT,DEFAULT_FONT_SIZE)
    message_min = message.suggest_min_metrics()

    window_width = max(int(message_min.width * 1.25),400)
    window_height = int(message_min.height * 5)

    window = Window(title,(window_width,window_height))

    application = Application(window)

    splitter = ProportionalVerticalSplitter(0.5)

    splitter.add_child_top(message)

    entry = TextEntry(default,DEFAULT_FONT,DEFAULT_FONT_SIZE)

    entry.set_entry_handler(lambda: application.suggest_quit(return_value=True))

    panel = BorderPanel()

    panel.add_child(entry)

    splitter.add_child_bottom(panel)

    application.set_text_focus(entry)

    window.add_child(splitter)

    if application.run():
        return entry.text.strip() if strip else entry.text
    else:
        return None

