#!/usr/bin/env python3
# coding=utf-8
from random import randint

import wx
import wx.xrc

from gui import MainFrameBase


class MainFrame(MainFrameBase):

    def onRand(self, event):
        row = 0
        col = 0
        while row < self.m_grid1.GetNumberRows():
            while col < self.m_grid1.GetNumberCols():
                random_num = randint(0, 11)
                self.m_grid1.SetCellValue(row, col, "%d" % random_num)
                col += 1
            row += 1
            col = 0

    def onSum(self, event):
        row = 0
        col = 0
        sum = 0
        while row < self.m_grid1.GetNumberRows():
            while col < self.m_grid1.GetNumberCols():
                try:
                    sum = sum + int(self.m_grid1.GetCellValue(row, col))
                except:
                    pass
                col += 1
            row += 1
            col = 0
        self.m_staticText_Sum.SetLabel("Сумма = " + "%d" % sum)

    def OnCloseFrame(self, event):
        self.Destroy()


def main():
    app = wx.App(False)
    frame = MainFrame(None)
    frame.Show(True)
    app.MainLoop()


if __name__ == '__main__':
    main()
