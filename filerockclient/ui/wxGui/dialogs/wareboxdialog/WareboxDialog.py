# generated by wxGlade 0.6.3 on Fri Aug 31 12:34:34 2012

import wx
from filerockclient.ui.wxGui import Messages
# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode

# end wxGlade


class DirPickerCtrl(wx.DirPickerCtrl):

    def __init__(self, *args, **kwds):
        super(DirPickerCtrl, self).__init__(*args, **kwds)

    def GetValue(self):
        return self.GetPath()

    def SetValue(self, value):
        return self.SetPath(value)


class WareboxDialog(wx.Dialog):

    def __init__(self, warebox_path, *args, **kwds):
        # begin wxGlade: WareboxDialog.__init__
        # end wxGlade
        kwds["style"] = wx.DEFAULT_DIALOG_STYLE | wx.RESIZE_BORDER
#        kwds["size"] = (400, 90)
        wx.Dialog.__init__(self, *args, **kwds)

        self.message_label = wx.StaticText(self,
                                           -1,
                                           Messages.WAREBOX_DIALOG_MESSAGE)
#        self.label_1 = wx.StaticText(self,
#                                     -1,
#                                     Messages.WAREBOX_DIALOG_LABEL)

        self.setFontBold(self.message_label)
#        self.setFontBold(self.label_1)

        self.warebox_ctrl = DirPickerCtrl(self,
                                          -1,
                                          "",
                                          style=wx.DIRP_USE_TEXTCTRL)

        self.__set_properties()
        self.__do_layout()
        self.warebox_ctrl.SetPath(warebox_path.strip())

    def __set_properties(self):
        # begin wxGlade: WareboxDialog.__set_properties
        self.SetTitle(Messages.WAREBOX_DIALOG_TITLE)
        _icon = wx.EmptyIcon()
        _icon.CopyFromBitmap(wx.Bitmap("./data/images/FileRock.ico",
                                       wx.BITMAP_TYPE_ANY))
        self.SetIcon(_icon)
        # end wxGlade
        _icon = wx.Icon("./data/images/FileRock.ico", wx.BITMAP_TYPE_ICO)
        self.SetIcon(_icon)
        self.SetMinSize((400, -1))
        self.SetMaxSize((600, -1))

    def __do_layout(self):

        # begin wxGlade: WareboxDialog.__do_layout
        # end wxGlade
        sizer_1 = wx.BoxSizer(wx.VERTICAL)
        sizer_2 = wx.FlexGridSizer(1, 1, 0, 5)
        sizer_1.Add(self.message_label, 0, wx.ALL |
                                           wx.EXPAND |
                                           wx.ALIGN_CENTER_HORIZONTAL |
                                           wx.ALIGN_CENTER_VERTICAL, 10)
#        sizer_2.Add(self.label_1, 0, wx.ALIGN_CENTER_HORIZONTAL |
#                                     wx.ALIGN_CENTER_VERTICAL, 0)
        sizer_2.Add(self.warebox_ctrl, 1, wx.EXPAND, 0)
        sizer_2.AddGrowableCol(0)
        sizer_1.Add(sizer_2, 1, wx.RIGHT |
                                wx.LEFT |
                                wx.EXPAND, 10)
        sizer_1.Add(self.CreateStdDialogButtonSizer(wx.OK), 0,
                    wx.ALL |
                    wx.ALIGN_CENTER_HORIZONTAL |
                    wx.ALIGN_CENTER_VERTICAL, 10)
        self.SetSizer(sizer_1)
        sizer_1.Fit(self)
        self.Layout()
        self.Centre()

    def setFontBold(self, label):
        font = label.GetFont()
        font.SetWeight(wx.FONTWEIGHT_BOLD)
        label.SetFont(font)

# end of class WareboxDialog

