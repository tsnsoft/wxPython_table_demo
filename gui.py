# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.grid


###########################################################################
## Class MainFrameBase
###########################################################################

class MainFrameBase(wx.Frame):

    def __init__(self, parent):
        wx.Frame.__init__(self, parent, id=wx.ID_ANY, title=u"wxGrid", pos=wx.DefaultPosition, size=wx.Size(500, 300),
                          style=wx.CLOSE_BOX | wx.DEFAULT_FRAME_STYLE | wx.TAB_TRAVERSAL)

        self.SetSizeHints(wx.Size(500, 300), wx.Size(500, 300))

        bSizer2 = wx.BoxSizer(wx.VERTICAL)

        self.m_staticText2 = wx.StaticText(self, wx.ID_ANY, u"Работа с таблицей", wx.DefaultPosition, wx.DefaultSize, 0)
        self.m_staticText2.Wrap(-1)

        bSizer2.Add(self.m_staticText2, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        self.m_grid1 = wx.grid.Grid(self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0)

        # Grid
        self.m_grid1.CreateGrid(5, 5)
        self.m_grid1.EnableEditing(True)
        self.m_grid1.EnableGridLines(True)
        self.m_grid1.EnableDragGridSize(False)
        self.m_grid1.SetMargins(0, 0)

        # Columns
        self.m_grid1.EnableDragColMove(False)
        self.m_grid1.EnableDragColSize(True)
        self.m_grid1.SetColLabelSize(30)
        self.m_grid1.SetColLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Rows
        self.m_grid1.EnableDragRowSize(True)
        self.m_grid1.SetRowLabelSize(80)
        self.m_grid1.SetRowLabelAlignment(wx.ALIGN_CENTER, wx.ALIGN_CENTER)

        # Label Appearance

        # Cell Defaults
        self.m_grid1.SetDefaultCellAlignment(wx.ALIGN_LEFT, wx.ALIGN_TOP)
        bSizer2.Add(self.m_grid1, 0, wx.ALL, 5)

        self.m_staticText_Sum = wx.StaticText(self, wx.ID_ANY, u"нажмите на кнопки ниже", wx.DefaultPosition,
                                              wx.DefaultSize, 0)
        self.m_staticText_Sum.Wrap(-1)

        bSizer2.Add(self.m_staticText_Sum, 0, wx.ALIGN_CENTER | wx.ALL, 5)

        bSizer3 = wx.BoxSizer(wx.HORIZONTAL)

        self.m_button3 = wx.Button(self, wx.ID_ANY, u"Случайные", wx.DefaultPosition, wx.DefaultSize, 0)

        self.m_button3.SetDefault()
        self.m_button3.SetFont(
            wx.Font(wx.NORMAL_FONT.GetPointSize(), wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL,
                    False, wx.EmptyString))

        bSizer3.Add(self.m_button3, 0, wx.ALL, 5)

        bSizer3.Add((0, 0), 1, wx.EXPAND, 5)

        self.m_button7 = wx.Button(self, wx.ID_ANY, u"Сумма", wx.DefaultPosition, wx.DefaultSize, 0)
        bSizer3.Add(self.m_button7, 0, wx.ALL, 5)

        bSizer2.Add(bSizer3, 1, wx.EXPAND, 2)

        self.SetSizer(bSizer2)
        self.Layout()

        self.Centre(wx.BOTH)

        # Connect Events
        self.Bind(wx.EVT_CLOSE, self.OnCloseFrame)
        self.m_button3.Bind(wx.EVT_BUTTON, self.onRand)
        self.m_button7.Bind(wx.EVT_BUTTON, self.onSum)

    def __del__(self):
        pass

    # Virtual event handlers, overide them in your derived class
    def OnCloseFrame(self, event):
        event.Skip()

    def onRand(self, event):
        event.Skip()

    def onSum(self, event):
        event.Skip()
