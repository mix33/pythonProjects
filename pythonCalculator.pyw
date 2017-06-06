# coding:gbk
import wx
def op1(event):
    finename.write('1')
def op2(event):
    finename.write('2')
def op3(event):
    finename.write('3')
def op4(event):
    finename.write('+')
def op5(event):
    finename.write('4')
def op6(event):
    finename.write('5')
def op7(event):
    finename.write('6')
def op8(event):
    finename.write('-')
def op9(event):
    finename.write('7')
def op10(event):
    finename.write('8')
def op11(event):
    finename.write('9')
def op12(event):
    finename.write('*')
def op13(event):
    finename.write('.')
def op14(event):
    finename.write('0')
def op15(event):
    finename.write('/')
def resultvalue(event):
    res = eval(finename.GetValue())
    finename.SetValue(str(res))
def d(event):
    finename.Clear()
    finename.write('0')
def c(event):
    valueres = finename.GetValue()
    finename.SetValue(valueres[:-1])
#################################################################################
app = wx.App()
win = wx.Frame(None, title=u"计算器", size=(420, 200))
panel = wx.Panel(win)
def Anniu(str1):
    return wx.Button(panel, label=str1)
def Bind(bt, op):
    bt.Bind(wx.EVT_BUTTON, op)
[bt1, bt2, bt3,
 bt4, bt5, bt6,
 bt7, bt8, bt9,
 bt10, bt11, bt12,
 bt13, bt14, bt15,
 bt16, bt17, bt18] = [Anniu("1"), Anniu("2"), Anniu("3"),
                      Anniu("+"), Anniu("4"), Anniu("5"),
                      Anniu("6"), Anniu("-"), Anniu("7"),
                      Anniu("8"), Anniu("9"), Anniu("*"),
                      Anniu("."), Anniu("0"), Anniu("="),
                      Anniu("/"), Anniu("CL"), Anniu("DEL"), ]

Bind(bt1, op1), Bind(bt2, op2),
Bind(bt3, op3), Bind(bt4, op4),
Bind(bt5, op5), Bind(bt6, op6),
Bind(bt7, op7), Bind(bt8, op8),
Bind(bt9, op9), Bind(bt10, op10),
Bind(bt11, op11), Bind(bt12, op12),
Bind(bt13, op13), Bind(bt14, op14),
Bind(bt15, resultvalue), Bind(bt16, op15),
Bind(bt17, d), Bind(bt18, c),
###################################################################################
finename = wx.TextCtrl(panel)
s1_box, s2_box, s3_box, s4_box, = wx.BoxSizer(wx.VERTICAL), wx.BoxSizer(wx.VERTICAL), wx.BoxSizer(wx.VERTICAL), wx.BoxSizer(wx.VERTICAL)

def add(bbtt, box=s1_box, proportion=0.1):
    box.Add(bbtt, proportion=1, flag=wx.EXPAND | wx.ALL, border=1)
add(bt1)
add(bt5)
add(bt9)
add(bt13)
add(bt2, box=s2_box)
add(bt6, box=s2_box)
add(bt10, box=s2_box)
add(bt14, box=s2_box)
add(bt3, box=s3_box)
add(bt7, box=s3_box)
add(bt11, box=s3_box)
add(bt15, box=s3_box)
add(bt4, box=s4_box)
add(bt8, box=s4_box)
add(bt12, box=s4_box)
add(bt16, box=s4_box)
v1_box = wx.BoxSizer(wx.VERTICAL)
v_box = wx.BoxSizer()
s_box = wx.BoxSizer(wx.VERTICAL)
add(bt17, v1_box)
add(bt18, v1_box)
add(s1_box, v_box)
add(s2_box, v_box)
add(s3_box, v_box)
add(s4_box, v_box)
add(v1_box, v_box)
add(finename, s_box)
add(v_box, s_box)
panel.SetSizer(s_box)
win.Show()
app.MainLoop()
