# -*- coding: utf-8 -*- 

import wx
import wx.xrc


class MyFrame1 ( wx.Frame ):
	
	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 233,350 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )
		
		self.SetSizeHintsSz( wx.DefaultSize, wx.DefaultSize )
		
		bSizer1 = wx.BoxSizer( wx.VERTICAL )
		
		self.m_staticText1 = wx.StaticText( self, wx.ID_ANY, u"Result", wx.DefaultPosition, wx.Size( 240,65 ), 0 )
		self.m_staticText1.Wrap( -1 )
		self.m_staticText1.SetFont( wx.Font( 9, 74, 90, 92, False, "Arial Black" ) )
		self.m_staticText1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INACTIVEBORDER ) )
		
		bSizer1.Add( self.m_staticText1, 0, wx.ALL, 5 )
		
		self.m_staticText2 = wx.StaticText( self, wx.ID_ANY, u"Enter evaluation:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText2.Wrap( -1 )
		bSizer1.Add( self.m_staticText2, 0, wx.ALL, 5 )
		
		self.m_textCtrl2 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.Size( 240,65 ), 0 )
		bSizer1.Add( self.m_textCtrl2, 0, wx.ALL, 5 )
		
		self.m_button1 = wx.Button( self, wx.ID_ANY, u"EVALUATE", wx.DefaultPosition, wx.Size( 240,65 ), 0 )
		self.m_button1.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		self.m_button1.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		bSizer1.Add( self.m_button1, 0, wx.ALL, 5 )
		# 
		self.m_button10 = wx.Button( self, wx.ID_ANY, u"CLOSE", wx.DefaultPosition, wx.Size( 240,65 ), 0 )
		self.m_button10.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_ACTIVECAPTION ) )
		self.m_button10.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_INFOTEXT ) )
		
		bSizer1.Add( self.m_button10, 0, wx.ALL, 5 )
		# 
		
		self.SetSizer( bSizer1 )
		self.Layout()
		
		self.Centre( wx.BOTH )
		
		# Connect Events
		self.m_button1.Bind( wx.EVT_BUTTON, self.doEval )
		self.m_button10.Bind( wx.EVT_BUTTON, self.doClose )
	
	def __del__( self ):
		pass
	
	
	# Virtual event handlers, overide them in your derived class
	def doEval( self, event ):
		try:
			result = self.m_textCtrl2.GetValue()
			done = eval(result)
			self.m_staticText1.SetLabel("\n" +str(done))
		except:
			self.m_staticText1.SetLabel("Invalid Expression")
	
	def doClose(self, event):
		self.Close()

app = wx.App()
frame = MyFrame1(None)
frame.Show()
app.MainLoop()