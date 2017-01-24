import pygame

from .obj import BorderPanel
from .text import SimpleText

class Button(BorderPanel):
    def __init__(
        self,
        text,
        event,
        font=None,
        font_size=26,
        fg_color='default_button_fg',
        bg_color='default_button_bg',
        border_color = 'default_button_border',
        hi_bg_color='default_button_hi_bg',
        hi_fg_color='default_button_hi_fg',
        hi_border_color='default_button_hi_border',
        in_padding = 0,
        out_padding = 1,
        border = 1,
        ):
        self.btn_text = text
        self.btn_fg_color = fg_color
        self.btn_bg_color = bg_color
        self.btn_border_color = border_color
        self.btn_hi_bg_color = hi_bg_color
        self.btn_hi_fg_color = hi_fg_color
        self.btn_hi_border_color = hi_border_color

        self.btn_event = event

        BorderPanel.__init__(self,self.btn_bg_color,self.btn_border_color,in_padding,out_padding,border)

        self.btn_text_obj = SimpleText(text,font,font_size,self.btn_bg_color,self.btn_fg_color)

        self.add_child(self.btn_text_obj)

    def handle_motion(self,position,rect):
        self.btn_text_obj.set_bg(self.btn_hi_bg_color)
        self.btn_text_obj.set_fg(self.btn_hi_fg_color)

    def handle_leave(self):
        self.btn_text_obj.set_bg(self.btn_bg_color)
        self.btn_text_obj.set_fg(self.btn_fg_color)

    def handle_click(self,position,rect,button):
        self.btn_event(self,position,rect,button)
