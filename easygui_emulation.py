from .app import Application
from .text import SimpleText,MultilineText
from .button import Button
from .window import Window
from .splitter import ProportionalVerticalSplitter,RemainingSpaceVerticalSplitter, ProportionalHorizontalSplitter
from .entry import TextEntry
from .obj import BorderPanel
from .choice import ListBox

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

def choicebox(msg='Pick something.',title=' ',choices=()):
    messagebox_provider = MultilineText if '\n' in msg else SimpleText
    message = messagebox_provider(msg,DEFAULT_FONT,DEFAULT_FONT_SIZE)
    message_min = message.suggest_min_metrics()

    message_panel = BorderPanel()
    message_panel.add_child(message)

    window = Window(title,(320,240))
    application=Application(window)

    options_box = ListBox(choices,'',DEFAULT_FONT,DEFAULT_FONT_SIZE)

    

    inside_splitter = RemainingSpaceVerticalSplitter(False,10)
    outside_splitter = RemainingSpaceVerticalSplitter(True)

    inside_splitter.add_child_top(message_panel)
    inside_splitter.add_child_bottom(options_box)

    outside_splitter.add_child_top(inside_splitter)

    select = Button('Select',lambda *args: (application.suggest_quit(return_value=True)) if options_box.selection is not None else None,DEFAULT_FONT,DEFAULT_FONT_SIZE)
    cancel = Button('Cancel',lambda *args: application.suggest_quit(),DEFAULT_FONT,DEFAULT_FONT_SIZE)

    button_splitter = ProportionalHorizontalSplitter(0.5)

    button_splitter.add_child_left(cancel)
    button_splitter.add_child_right(select)

    outside_splitter.add_child_bottom(button_splitter)

    window.add_child(outside_splitter)

    final_window_x = 640 #TODO: Fix this awful hack
    final_window_y = (select.suggest_min_metrics().height)*3 + options_box.suggest_min_metrics().height

    window.fix((final_window_x,final_window_y))

    application.set_text_focus(options_box)

    options_box.set_handler(lambda *args: application.suggest_quit(return_value=True))


    if application.run():
        if options_box.selection is not None:
            return choices[options_box.selection]
        else:
            return None
    else:
        return None