#!/usr/bin/python
# -*- coding: UTF-8 -*-
# Created by w23ta0 on 16-3-22


import base64
import wx
import wx.xrc

###########################################################################
## Class MyFrame1
###########################################################################

class MyFrame1 ( wx.Frame ):

    def __init__( self, parent ):
        wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"hex+base64 加解密工具", pos = wx.DefaultPosition, size = wx.Size( -1,-1 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

        self.SetSizeHintsSz( wx.Size( -1,-1 ), wx.Size( -1,-1 ) )
        self.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOWTEXT ) )
        self.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BTNFACE ) )

        bSizer1 = wx.BoxSizer( wx.VERTICAL )

        bSizer1.SetMinSize( wx.Size( 500,400 ) )
        self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"hex+base64 加解密工具", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText1.Wrap( -1 )
        self.m_staticText1.SetFont( wx.Font( 12, 70, 90, 90, False, u"微软雅黑" ) )

        bSizer1.Add( self.m_staticText1, 0, wx.ALL|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"input", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText2.Wrap( -1 )
        bSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )

        self.m_textCtrl1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_textCtrl1, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        self.m_staticline1 = wx.StaticLine( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.LI_HORIZONTAL )
        bSizer1.Add( self.m_staticline1, 0, wx.EXPAND |wx.ALL, 5 )

        self.m_staticText3 = wx.StaticText( self, wx.ID_ANY, u"ouput", wx.DefaultPosition, wx.DefaultSize, 0 )
        self.m_staticText3.Wrap( -1 )
        bSizer1.Add( self.m_staticText3, 0, wx.ALL, 5 )

        self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
        bSizer1.Add( self.m_textCtrl2, 1, wx.ALL|wx.EXPAND|wx.ALIGN_CENTER_HORIZONTAL, 5 )

        gbSizer1 = wx.GridBagSizer( 0, 0 )
        gbSizer1.SetFlexibleDirection( wx.BOTH )
        gbSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

        self.m_button1 = wx.Button( self, wx.ID_ANY, u"加密", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.m_button1, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

        self.m_button2 = wx.Button( self, wx.ID_ANY, u"解密", wx.DefaultPosition, wx.DefaultSize, 0 )
        gbSizer1.Add( self.m_button2, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


        bSizer1.Add( gbSizer1, 0, wx.ALIGN_CENTER_HORIZONTAL|wx.TOP|wx.BOTTOM, 5 )


        self.SetSizer( bSizer1 )
        self.Layout()
        bSizer1.Fit( self )
        self.m_statusBar1 = self.CreateStatusBar( 1, wx.ST_SIZEGRIP, wx.ID_ANY )

        self.Centre( wx.BOTH )

        # Connect Events
        self.m_textCtrl1.Bind( wx.EVT_TEXT, self.m_textCtrl1OnText )
        self.m_textCtrl2.Bind( wx.EVT_TEXT, self.m_textCtrl2OnText )
        self.m_button1.Bind( wx.EVT_BUTTON, self.m_button1OnButtonClick )
        self.m_button2.Bind( wx.EVT_BUTTON, self.m_button2OnButtonClick )

    def __del__( self ):
        pass


    # Virtual event handlers, overide them in your derived class
    def m_textCtrl1OnText( self, event ):
        event.Skip()

    def m_textCtrl2OnText( self, event ):
        event.Skip()

    def m_button1OnButtonClick( self, event ):
        event.Skip()
        input=self.m_textCtrl1.GetValue()
        a=base64.b64encode(input)
        b=a.encode("hex")
        self.m_textCtrl2.SetValue(b)


    def m_button2OnButtonClick( self, event ):
        event.Skip()
        input=self.m_textCtrl1.GetValue()
        a1=input.decode("hex")
        b1=base64.b64decode(a1)
        self.m_textCtrl2.SetValue(b1)



class App(wx.App):
    def OnInit(self):
        frame = MyFrame1(None)
        frame.Show()
        return True
if __name__ == '__main__':
    app = App()
    app.MainLoop()

#b='5833524a5a575a6d626d3130566d56744e476c334f48343d0a'
#a1=b.decode("hex")
#b1=base64.b64decode(a1)
#print a1
#print b1


