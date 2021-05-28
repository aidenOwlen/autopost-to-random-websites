from tkinter import *
from tkinter import filedialog
from tkinter.scrolledtext import ScrolledText
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import bs4 as bs
import time
import lxml



class Interface:
    fenetre = Tk()
    NameName = []
    EmailName = []
    NameId = []
    EmailId = []
    NameClass = []
    EmailClass = []
    CommentClass = []
    CommentId = []
    CommentName = []
    Failed = False
    report = "Can't retrieve : "
    OurMessage = ""
    SubjectName = []
    SubjectId = []
    TriesN = 0
    TriesE = 0
    TriesC = 0
    report2 = "There maybe a problem with : "
    Captcha = ""
    Wait = True
    SubmitBut = []
    
    def __init__(self):
        
        xcan = Canvas(self.fenetre, width = 800, height = 600,bg = "dark grey")
        xcan.grid(row=0,column=0)
        xcan.create_window(5,30,anchor =NW, window=Label(self.fenetre, text = "Name", bg = "dark grey",fg ="dark red"))
        xcan.create_window(5,70,anchor =NW, window=Label(self.fenetre, text = "Email", bg = "dark grey",fg = "dark red"))
        xcan.create_window(183,110,anchor =NW, window=Label(self.fenetre, text = "Message", bg = "dark grey",fg = "dark blue"))

        self.Name = Entry(self.fenetre, width = 57)
        xcan.create_window(50,30,anchor =NW,window = self.Name)

        self.Email = Entry(self.fenetre, width = 57)
        xcan.create_window(50,70,anchor =NW,window = self.Email)

        self.Message = ScrolledText(self.fenetre ,width = 48,height=10)
        xcan.create_window(5,130,anchor=NW, window=self.Message)
        

        self.Load = Button(self.fenetre,text="Load websites",bg="dark grey",width = 54,command = self.load)

        xcan.create_window(5,371, anchor=NW, window=self.Load)

        self.websites = ScrolledText(self.fenetre, width = 48, height = 10)
        xcan.create_window(5,401,anchor=NW,window=self.websites)

        xcan.create_window(553,110,anchor=NW,window=Label(self.fenetre,text= "History", bg ="dark grey", fg = "dark green"))
        self.history = ScrolledText(self.fenetre, width = 41, height = 27)
        xcan.create_window(410,130,anchor=NW,window=self.history)

        self.Start = Button(self.fenetre, text = "Start", bg = "dark grey", width = 104,command = self.start)
        xcan.create_window(5,570,anchor=NW,window=self.Start)
        lipa = open("History.txt", "r")
        rlipa = lipa.read()
        self.history.insert(0.0, rlipa)
        self.fenetre.mainloop()
    def load(self):
        reper = filedialog.askopenfilename()
        fichier = open(reper, "r")
        self.websites.delete(0.0,END)
        self.websites.insert(0.0,fichier.read())
        fichier.close()
    def start(self):
        self.nom = self.Name.get()
        self.lemail = self.Email.get()
        self.lemessage = self.Message.get(0.0,END)
        self.our_subject = self.lemessage[0:8]
        self.driver = webdriver.Chrome()
        self.w = WebDriverWait(self.driver,10)
        self.Urls = self.websites.get(0.0,END)
        self.Urls = self.Urls.split("\n")
        for self.p in self.Urls:
            self.go()
    def go(self):
        self.driver.get(self.p)
        self.pp = self.driver.current_url
        self.soup = bs.BeautifulSoup(self.driver.page_source,"html.parser")
        self.m = self.soup.find_all("input")
        if re.search("captcha|Captcha|CAPTCHA",str(self.soup)) is not None:
            self.Captcha = "Captcha detected in source code"
        else:
            self.Captcha = "No captcha detected"
        for s in self.m:
            if re.search("Name|name|NAME|Author|AUTHOR|author",str(s.get("name"))) is not None:
                self.NameName.append(str(s.get("name")))           

            if re.search("email|Email|EMAIL|e-mail|e mail|E-mail|E-MAIL|E-Mail|E mail|E MAIL",str(s.get("name"))) is not None:
                self.EmailName.append(str(s.get("name")))

            if re.search("Name|name|NAME|Author|AUTHOR|author",str(s.get("id"))) is not None:
                self.NameId.append(str(s.get("id")))
                
            if re.search("email|Email|EMAIL|e-mail|e mail|E-mail|E-MAIL|E-Mail|E mail|E MAIL",str(s.get("id"))) is not None:
                self.EmailId.append(str(s.get("id")))

            if re.search("Name|name|NAME|Author|AUTHOR|author",str(s.get("class"))) is not None:
                self.NameClass.append(str(s.get("class")))
                
            if re.search("email|Email|EMAIL|e-mail|e mail|E-mail|E-MAIL|E-Mail|E mail|E MAIL",str(s.get("class"))) is not None:
                self.EmailClass.append(str(s.get("class")))

            if re.search("Name|name|NAME|Author|AUTHOR|author",str(s.get("placeholder"))) is not None:
                try:
                    self.NameId.append(str(s.get("id")))
                except:
                    pass
                try:
                    self.NameClass.append(str(s.get("class")))
                except:
                    pass
                try:
                    self.NameName.append(str(s.get("name")))
                except:
                    pass

            if re.search("Subject|subject|SUBJECT",str(s.get("name"))):
                self.SubjectName.append(str(s.get("name")))

            if re.search("Subject|SUBJECT|subject",str(s.get("id"))):
                self.SubjectId.append(str(s.get("id")))

            if re.search("email|Email|EMAIL|e-mail|e mail|E-mail|E-MAIL|E-Mail|E mail|E MAIL",str(s.get("placeholder"))) is not None:
                try:
                    self.EmailId.append(str(s.get("id")))
                except:
                    pass
                try:
                    self.EmailClass.append(str(s.get("class")))
                except:
                    pass
                try:
                    self.EmailName.append(str(s.get("name")))
                except:
                    pass

            if re.search("Comment|comment|COMMENT|message|MESSAGE|Message",str(s.get("placeholder"))) is not None:
                try:
                    self.CommentId.append(str(s.get("id")))
                except:
                    pass
                try:
                    self.CommentClass.append(str(s.get("class")))
                except:
                    pass
                try:
                    self.CommentName.append(str(s.get("name")))
                except:
                    pass    
                
            if str(s.get("type")) == "email":
                
                try:
                    self.EmailName.append(str(s.get("name")))
                except:
                    pass
                try:
                    self.EmailId.append(str(s.get("id")))
                except:
                    pass
                try:
                    self.EmailClass.append(str(s.get("class")))
                except:
                    pass
        self.d = self.soup.find_all("textarea")
        for x in self.d:
            try:
                self.CommentId.append(str(x.get("id")))
            except:
                pass
            try:
                self.CommentName.append(str(x.get("name")))
            except:
                pass
            try:
                self.CommentClass.append(str(x.get("class")))
            except:
                pass

        if ( len(self.NameName) == 0 and len(self.NameId) ==0 and len(self.NameClass) == 0 ):
            self.Failed = True
            self.report += "Name / "

            
        if  ( len(self.EmailName) == 0 and len(self.EmailId) == 0  and len(self.EmailClass) == 0):
            self.Failed = True
            self.report+= "Email / "


        if ( len(self.CommentId) == 0 and len(self.CommentName) == 0 and len(self.CommentClass) == 0 ):
            self.Failed = True
            self.report+= "Message / "

        if self.Failed == True:
            self.Our_Message = report
            self.Wait = False
        else:
            self.Our_Message = ""
            for i in self.NameName:# FILLING NAME
                try:
                    tempVn = self.driver.find_element_by_name(i)
                    tempVn.clear()
                    tempVn.send_keys(self.nom)
                except:
                    self.TriesN += 1
            for i in self.NameId:
                try:
                    tempVi = self.driver.find_element_by_id(i)
                    tempVi.clear()
                    tempVi.send_keys(self.nom)
                except:
                    self.TriesN += 1


            for i in self.EmailName:
                try:
                    tempVEN = self.driver.find_element_by_name(i)
                    tempVEN.clear()
                    tempVEN.send_keys(self.lemail)
                except:
                    self.TriesE += 1
            for i in self.EmailId:
                try:
                    tempVEI = self.driver.find_element_by_id(i)
                    tempVEI.clear()
                    tempVEI.send_keys(self.lemail)
                except:
                    self.TriesE += 1
            for i in self.CommentId:
                try:
                    tempCI = self.driver.find_element_by_id(i)
                    tempCI.clear()
                    tempCI.send_keys(self.lemessage)
                except:
                    self.TriesC += 1

            for i in self.CommentName:
                try:
                    tempCM = self.driver.find_element_by_name(i)
                    tempCM.clear()
                    tempCM.send_keys(self.lemessage)
                except:
                    self.TriesC += 1

            for i in self.CommentClass:
                try:
                    tempClassC = self.driver.find_element_by_name(i)
                    tempClassC.clear()
                    tempClassC.send_keys(self.lemessage)
                except:
                    self.TriesC += 1

            for i in self.NameClass:
                try:
                    tempClassN = self.driver.find_element_by_class_name(i)
                    tempClassN.clear()
                    tempClassN.send_keys(self.nom)
                except:
                    self.TriesN += 1

            for i in self.EmailClass:
                try:
                    tempClassE = self.driver.find_element_by_class_name(i)
                    tempClassE.clear()
                    tempClassE.send_keys(self.lemail)
                except:
                    self.TriesE +=1

            for i in self.SubjectName:
                try:
                    tempSubjName = self.driver.find_element_by_name(i)
                    tempSubjName.clear()
                    tempSubjName.send_keys(self.our_subject)
                except:
                    pass

            for i in self.SubjectId:
                try:
                    tempSubjId = self.driver.find_element_by_id(i)
                    tempSubjId.clear()
                    tempSubjId.send_keys(self.our_subject)
                except:
                    pass
            Clicked = False
                

            self.li = self.driver.find_elements_by_tag_name("input")
            for j in self.li:
                try:
                    if j.get_attribute("type") == "submit":
                        self.SubmitBut.append(j)
                        print("appended")
                        
                        
                except:
                    pass
            if len(self.SubmitBut) == 0:
                Clicked = False

            if len(self.SubmitBut) >= 2:
                try:
                    for o in self.SubmitBut:
                        if re.search("Submit|SUBMIT|submit|Send Message|send message|Send message|SEND MESSAGE|send|Send|SEND",str(o.get_attribute("value"))) is not None:
                            print("here")
                            try:
                                
                                o.click()
                                Clicked = True
                            except:
                                try:
                                    o.submit()
                                    Clicked = True
                                except:
                                    pass
                except:
                    pass
            else:
                print("we're here")
                try:
                    self.SubmitBut[0].click()
                except:
                    try:
                        self.SubmitBut[0].submit()
                    except:
                        Clicked = False
                    
                        
                        
                
            if Clicked == False:
                print("clicked = false")
                for j in self.li:
                    try:
                        if j.get_attribute("type") == "image":
                            try:
                                j.submit()
                                Clicked = True
                            except:
                                try:
                                    j.click()
                                    Clicked = True
                                except:
                                    Clicked = False
                    except:
                        Clicked = False

            if self.TriesN >= 3:
                self.report2 += "Name field"
            elif self.TriesE >=3:
                self.report2 += "Email field"
            elif self.TriesC >= 3:
                self.report2 += "Comment field"
            elif Clicked == False:
                self.report2 += "Submit Button"
            else:
                self.report2 = "Sucess !"

            t = 0
            while t <= 10:
                if self.driver.current_url != self.pp:
                    break
                time.sleep(1)
                t += 1
                

           
            
                            
                      

            fi = open("history.txt", "a")
            fi.write("{} : {} // {} // {} \n\n".format(self.p,self.OurMessage,self.report2,self.Captcha))
            fi.close()
            self.report2 = "There maybe a problem with : "
            self.OurMessage = ""
            self.TriesN = 0
            self.TriesE = 0
            self.TriesC = 0
            self.Captcha = ""
            self.SubmitBut = []
            self.Wait = True
                
                    
                
                    

        

                    
                    
            
            
        
        
        
    

Interface()


