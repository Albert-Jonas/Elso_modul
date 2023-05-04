import wx
import random
import time
from wx.adv import Animation, AnimationCtrl
import PlayAnimation


class Window(wx.Frame):
    def __init__(self, title):
        super().__init__(parent = None, title = title, size = (480,240), style=wx.MAXIMIZE_BOX | wx.SYSTEM_MENU | wx.CAPTION |	 wx.CLOSE_BOX)
        self.panel = wx.Panel(self)
        

        wrapper = wx.BoxSizer(wx.VERTICAL)
        sizer = wx.GridBagSizer(50, 80)
        button = wx.Button(self.panel, label = "Press me!")
        button.SetBitmap(wx.Bitmap("detonator.bmp"))
        button.SetBackgroundColour("white")
       


        button.Bind(wx.EVT_BUTTON, self.OnClick)

        sizer.Add(button, pos = (1, 1))

        wrapper.Add(sizer, proportion = 1, flag = wx.ALL | wx.EXPAND, border = 10)
        self.panel.SetSizer(wrapper)

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)
        self.Center()
        self.Show()
      
    activeAnimations = []

    def OnClick(self, e):
        widget = e.GetEventObject()
        widget.SetLabel("BUMM!")
        widget.SetBitmap(wx.Bitmap("explosion.bmp"))

        if len(self.activeAnimations) < 7:
            self.activeAnimations.append(PlayAnimation.PlayAnimation("Animation"))
            self.activeAnimations[-1].Show()
        else:
            widget.SetSize((250,30))
            widget.SetLabel("Sajna csak 7 van egy instance-ban")
    
    def OnCloseWindow(self, event):
        new_list = [item.Close() for item in self.activeAnimations]
        self.Destroy()



app = wx.App()
window = Window("WxPython Példa")
app.MainLoop()
