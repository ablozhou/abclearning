##################################################################################
#General:
#  read http://wiki.wxpython.org/index.cgi/UsingXmlResources for more information about how to use xrc
#
#Problems:
#  google "(class 'wxMenuBar') not found ", visit http://aspn.activestate.com/ASPN/Mail/Message/wxPython-users/2242126 ( wxGlade's problem?)
#  google "TypeError: OnExit() takes exactly 2 arguments (1 given)" and visit http://www.gnuenterprise.org/irc-logs/gnue-public.log.2003-02-26 (wxPython's problem?)
#  we *donot* want sash in splitter window to disappear. google "wxSplitterEvent" , get "The sash was double clicked. The default behaviour is to unsplit the window when this happens (unless *the minimum pane size has been set to a value greater than zero*, yes it is what we do in xrc)",
#
#Naming conventions:
#  class._var1 = class shared variable (like static class data member in C++, BTW: see python online help for python's private variables's naming conventions )
#  class.CapitalizeEveryWord = class method
#  class.instance_data_member = instance's data member (like public data member in C++)
#  m_file_shared_variables = variables prefixed with "m_" are shared in a file
#  g_global_shared_variables = variables prefixed with "g_" are global variables
##################################################################################

from wxPython.wx import *
from wxPython.xrc import *
import sys

#the New Job dialog
class dlgNew:
    def __init__(self,ctrl):
        assert(ctrl<>None)
        self.ctrl=ctrl
        self.idc_textmode_txt=self.ctrl.FindWindowById(XRCID("idc_textmode_txt"))
        assert(self.idc_textmode_txt<>None)
        self.idc_new_runnow=self.ctrl.FindWindowById(XRCID("idc_new_runnow"))
        assert(self.idc_new_runnow)
        self.idc_new_jobname=self.ctrl.FindWindowById(XRCID("idc_new_jobname"))
        assert(self.idc_new_jobname<>None)
       
        self.MessageMap(self.ctrl)
           
    def __del__(self):
        #self.ctrl.Destroy()
        pass
       
    def MessageMap(self,ctrl):
        EVT_BUTTON(ctrl, XRCID("idc_new_ok"), self.OnOK)
        EVT_BUTTON(ctrl, XRCID("idc_new_cancel"), self.OnCancel)
        EVT_BUTTON(ctrl, XRCID("idc_new_apply"), self.OnApply)
   
    def OnOK(self,event):
        if self.Validate():
            self.OnApply(event)
            self.ctrl.Close(True)
        else:
            # report error
            pass
   
    def OnCancel(self,event):
        self.ctrl.Close(True)
       
    def OnApply(self,event):
        #save job
       
        #if needed, submit it now
        if self.idc_new_runnow.IsChecked():
            pass
       
    def Validate(self):
        try:
            if self.idc_textmode_txt.GetValue()==None:
                assert(0)
                raise
               
            if self.idc_new_jobname.GetValue()==None:
                assert(0)
                raise  
               
            if not self.IsCmdValid(self.idc_textmode_txt.GetValue()):
                assert(0)
                raise
       
            return True
        except:
            return False
       
    def IsCmdValid(self,txt):
        if txt==None:
            assert(0);
            return False
        return True

class hostList:
    def __init__(self, parent, id):
        assert(parent<>None)
        assert(id<>None)
        self.id=id
        self.ctrl=parent.FindWindowById(self.id)
        assert(self.ctrl<>None)
       
        #init list header
        self.config_column=[  #id; #name; #size; #after filling data we resize
                        [0,"ID", wxLIST_AUTOSIZE_USEHEADER, wxLIST_AUTOSIZE],
                        [1,"Job", wxLIST_AUTOSIZE_USEHEADER, wxLIST_AUTOSIZE],
                        [2,"Work", wxLIST_AUTOSIZE_USEHEADER, wxLIST_AUTOSIZE],
                      ]
        for  c in self.config_column:
            self.ctrl.InsertColumn(c[0],c[1])
            self.ctrl.SetColumnWidth(c[0], c[2])
       
    def Refresh(self,workers):
       
        # filling data
        self.ctrl.DeleteAllItems()
       
       
        for i in range(0,5):
            index = self.ctrl.InsertStringItem(sys.maxint, "") #insert nothing, just get index
            self.ctrl.SetStringItem(index, 0, "val0") #0 means first column
            self.ctrl.SetStringItem(index, 1, "val1")
            self.ctrl.SetStringItem(index, 2, "val2")
               
        # after filling data, resize column
        for c in self.config_column:
            self.ctrl.SetColumnWidth(c[0], c[3])   
           
class jobList:
    def __init__(self, parent, id, details=None):
        assert(parent<>None)
        assert(id<>None)
        self.id=id
        self.ctrl=parent.FindWindowById(self.id)
        assert(self.ctrl<>None)
        self.details=details
       
        #init list header
        self.config_column=[  #id; #name; #size; #after filling data we resize
                        [0,"ID", wxLIST_AUTOSIZE_USEHEADER, wxLIST_AUTOSIZE],
                        [1,"Owner", wxLIST_AUTOSIZE_USEHEADER, wxLIST_AUTOSIZE],
                        [2,"Name", wxLIST_AUTOSIZE_USEHEADER, wxLIST_AUTOSIZE],
                        [3,"Status", wxLIST_AUTOSIZE_USEHEADER, wxLIST_AUTOSIZE],
                        [4,"Work", wxLIST_AUTOSIZE_USEHEADER, wxLIST_AUTOSIZE],
                      ]
        for  c in self.config_column:
            self.ctrl.InsertColumn(c[0],c[1])
            self.ctrl.SetColumnWidth(c[0], c[2])       
       
        self.MessageMap(self.ctrl)
       
           
    def Refresh(self,jobs):
        # data buffer shared by other
       
        #print list_data #debug
        self.ctrl.DeleteAllItems()
       
        for i in range(0,5):
            index = self.ctrl.InsertStringItem(sys.maxint, "") #insert nothing, just get index
            self.ctrl.SetStringItem(index, 0, "val0") #0 means first column
            self.ctrl.SetStringItem(index, 1, "val1")
            self.ctrl.SetStringItem(index, 2, "val2")
            self.ctrl.SetStringItem(index, 3, "val3") # add better conversion to text
            self.ctrl.SetStringItem(index, 4, "val4")
               
        # after filling data, resize column
        for c in self.config_column:
            self.ctrl.SetColumnWidth(c[0], c[3])   


#----- Message Map and Event Handler ----- begin
    def MessageMap(self,ctrl):
        EVT_LIST_ITEM_SELECTED(ctrl,self.id,self.OnItemSelected)
        EVT_LIST_ITEM_DESELECTED(ctrl,self.id,self.OnItemDeselected)
       
    def OnItemSelected(self,event):
        if self.details<>None:
            #dump everything about a job
            self.details.SetValue("rubbish data")
            pass
        pass
       
    def OnItemDeselected(self,event):
        print "OnListItemDeselected" #debug
        if self.details<>None:
            self.details.Clear()
        pass
#----- Message Map and Event Handler ----- end

       
#main application
class myApp(wxApp):
    def OnInit(self):
        #load ctrls from resources
        self.res = wxXmlResource("main.xrc")
        self.idf_main = self.res.LoadFrame(None, "idf_main")
        self.idc_main_menubar = self.res.LoadMenuBar("idc_main_menubar")
        self.idc_main_toolbar=self.res.LoadToolBar(self.idf_main,"idc_main_toolbar")
        self.idc_splitter_twobar=self.idf_main.FindWindowById(XRCID("idc_splitter_twobar"))
        self.idc_status_txt=self.idf_main.FindWindowById(XRCID("idc_status_txt"))
        self.idc_jobs_list1=jobList(self.idf_main,XRCID("idc_jobs_list1"),self.idc_status_txt)
        self.idc_jobs_list2=jobList(self.idf_main,XRCID("idc_jobs_list2"),self.idc_status_txt)
        self.idc_hosts_list1=hostList(self.idf_main,XRCID("idc_hosts_list1"))
        self.idc_hosts_list2=hostList(self.idf_main,XRCID("idc_hosts_list2"))
        self.idd_new=dlgNew(self.res.LoadDialog(self.idf_main,"idd_new"))
       
        # message map,
        self.MessageMap(self.idf_main)
       
        #binding ctrls
        self.idf_main.SetMenuBar(self.idc_main_menubar)
        self.idf_main.SetToolBar(self.idc_main_toolbar)

        self.RefreshAll()
       
        #show time
        self.ShowMe()
        return True
   
    def RefreshAll(self):
        # get full master state
        self.RefreshAllJobList(None)
        self.RefreshAllHostList(None)
        # should alse display queue status somewhere (self.ms.state)
       
    def RefreshAllJobList(self,jobs):
        # jobList is a sequence of jobs (base class mgr.JobBase)
        self.idc_jobs_list1.Refresh(jobs)
        self.idc_jobs_list2.Refresh(jobs)
       
   
    def RefreshAllHostList(self, workers):
        # workers is dict of slave workers (base class mgr.Worker)
        self.idc_hosts_list1.Refresh(workers)
        self.idc_hosts_list2.Refresh(workers)
   
    def ShowMe(self):
        sizer = self.idf_main.GetSizer()
        sizer.Fit(self.idf_main)
        sizer.SetSizeHints(self.idf_main)
        self.idf_main.Show(True)
        self.SetTopWindow(self.idf_main)

    def ShowMe(self):
        sizer = self.idf_main.GetSizer()
        sizer.Fit(self.idf_main)
        sizer.SetSizeHints(self.idf_main)
        self.idf_main.Show(True)
        self.SetTopWindow(self.idf_main)
  
#----- Message Map and Event Handler ----- begin
    def MessageMap(self,ctrl):
        #menu
        EVT_MENU(ctrl, XRCID("idm_main_pause_queue"), self.OnPauseQ)
        EVT_MENU(ctrl, XRCID("idm_main_resume_queue"), self.OnResumeQ)
        EVT_MENU(ctrl, XRCID("idm_main_new"), self.OnNew)
        EVT_MENU(ctrl, XRCID("idm_main_exit"), self.OnBye)
        EVT_MENU(ctrl, XRCID("idm_main_options"), self.OnOptions)
        EVT_MENU(ctrl, XRCID("idm_main_index"), self.OnIndex)
        EVT_MENU(ctrl, XRCID("idm_main_refresh"), self.OnRefresh)
        EVT_MENU(ctrl, XRCID("idm_main_vertical"), self.OnVertical)
        EVT_MENU(ctrl, XRCID("idm_main_about"), self.OnAbout)
       
        #toolbar
        EVT_MENU(ctrl,XRCID("idc_toolbar_new"), self.OnNew) #google "wxToolBar"
       
       
   
    def OnPauseQ(self,event):
        pass
       
    def OnResumeQ(self,event):
        pass
       
    def OnNew(self,event):
        self.idd_new.ctrl.ShowModal()
        self.RefreshAll()
       
    def OnAbout(self,event):
         dlg = wxMessageDialog(self.idf_main, "None\n"
                                      "Version 1.0\n"
                                      "Copyright(C) 2005-2010 Redguardtoo",
                                      "About Me", wxOK | wxICON_INFORMATION)
         dlg.ShowModal()
         dlg.Destroy()


    def OnBye(self,event):
        print "hello, I am OnBye"
        self.idf_main.Close(True)
           
    def OnOptions(self,event):
        print "hello, I am OnOptions"
   
    def OnIndex(self,event):
        print "hello, I am OnIndex"
       
    def OnRefresh(self,event):
        self.RefreshAll()
               
    def OnVertical(self,event):
        if not self.idc_splitter_twobar.IsSplit():
            return
       
        w1=self.idc_splitter_twobar.GetWindow1()
        assert(w1)
        w2=self.idc_splitter_twobar.GetWindow2()
        assert(w2)
       
        s=self.idc_splitter_twobar.GetSplitMode()
       
        #some error
        self.idc_splitter_twobar.Unsplit() #have to , see document
        w1.Show(True) # when unsplitting , one pane hide , now we show them
        w2.Show(True)
        if s==wxSPLIT_VERTICAL:
            self.idc_splitter_twobar.SplitHorizontally(w1,w2)
        elif s==wxSPLIT_HORIZONTAL:
            self.idc_splitter_twobar.SplitVertically(w1,w2)
        else:
            assert(0)
#----- Message Map and Event Handler ----- end            
      
if __name__=="__main__":
    app = myApp(0)
    app.MainLoop()


