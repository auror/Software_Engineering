import wx
import lol

globe = []
class check(wx.Frame):

    def __init__(self,parent,id):
        wx.Frame.__init__(self,parent,id,'Software Coverage Analyser',size=(600,600))
        panel = wx.Panel(self)
        test = wx.TextEntryDialog(None,"No: of Test Paths",'Test Paths','path')
        if test.ShowModal() == wx.ID_OK:
            path = test.GetValue()
        path = long(path)
        Master = []
        j = path
        i = 0
        while path:
            test = wx.TextEntryDialog(None,"Enter",'Test Path ' +str(i+1),'path')
            if test.ShowModal() == wx.ID_OK:
                x = test.GetValue()
                x = str(x)
                y = x.split(',')
                y = [int(k) for k in y]
                Master.append(y)
            path-=1
            i+=1
        globe = Master
        i = 0
        while j:
            wx.StaticText(panel,-1,'Test Path ' +str(i+1)+': '+str(Master[i]),(10,10*2*i))
            j-=1
            i+=1
        Results = lol.ulti(Master)

        i = 1
        for ha in Results:
            wx.StaticText(panel,-1,'Coverage values',(100,100))
            wx.StaticText(panel,-1,'Generation '+str(i)+': '+str(ha),(100,100+20*i))
            i+=1

        button = wx.Button(panel,label='Exit',pos=(500,500),size=(50,50))
        button.Bind(wx.EVT_BUTTON,self.onClose)
        self.Bind(wx.EVT_BUTTON,self.closebutton,button)
        self.Bind(wx.EVT_CLOSE,self.closewindow)

    def closebutton(self,event):
        self.Close(True)

    def closewindow(self,event):
        self.Destroy()
    def onClose(self,event):
        self.Destroy()

        

if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = check(parent=None,id=-1)
    frame.Show()
    app.MainLoop()
