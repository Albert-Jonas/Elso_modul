import wx
import random
from wx.adv import Animation, AnimationCtrl

class PlayAnimation(wx.Frame):
    def __init__(self, title):
        xPos = random.randint(0,1024)
        yPos = random.randint(0,768)
        super().__init__(parent = None, title = title, size = (502,263), pos = (xPos, yPos))
        self.panel = wx.Panel(self)

        wrapper = wx.BoxSizer(wx.VERTICAL)
        sizer = wx.FlexGridSizer(rows = 2, cols = 1, vgap = 5, hgap = 5)

        anim = Animation("gif2.gif")
        anim_ctrl = AnimationCtrl(self.panel, wx.ID_ANY, anim)
        anim_ctrl.Play()