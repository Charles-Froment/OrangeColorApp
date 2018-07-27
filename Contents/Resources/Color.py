#-*- coding: utf-8 -*-
#--- Charles Froment ---
from tkinter import *
import time
import pickle

class MainApplication:
	def __init__(self,window):
		self.window=window
		self.MinimizeMode=Frame(self.window)
		self.FullMode=Frame(self.window)

		#----- Users preferences ------
		FichierUserPreference=open('UserPreference_data.dat','rb')
		self.TabUserPreference=pickle.load(FichierUserPreference)
		FichierUserPreference.close()

		if self.TabUserPreference['MinimizeMode']==True:
			self.MinimizeMode.grid()
			self.FullMode.grid_forget()
		else:
			self.FullMode.grid()
			self.MinimizeMode.grid_forget()
		
		#Menu
		MenuBar=Menu(window)
		OptionMenu=Menu(MenuBar)
		OptionMenu.add_command(label='Switch UI',command=self.RemoveGrid)
		MenuBar.add_cascade(label='Option',menu=OptionMenu)
		window.configure(menu=MenuBar)
		
		#------- Minimize UI mode --------
		self.ColorList=['#000000','#FFFFFF','#F16E00','#595959','#8F8F8F','#D6D6D6','#4BB4E6','#50BE87','#FFB4E6',
		'#A885D8','#FFD200','#085EBD','#0A6E31','#FF8AD4','#492191','#FFB400',
		'#B5E8F7','#B8EBD6','#FFE8F7','#D9C2F0','#FFF6B6','#482E26','#62342D','#714E46','#C19372','#F4CFB2','#FFF6B6',
		'#FFE8F7','#32C832','#CD3C14','#527EDB','#FFCC00']

		for IndexColors in self.ColorList:
			MinimizeColors=Label(self.MinimizeMode,bg=IndexColors,width=11,font=('HelveticaNeue',5),pady=5)
			MinimizeColors.bind('<Button-1>',self.ChangeColor)
			MinimizeColors.grid()

		#------- Full UI mode --------
		#---------- Header Bar ----------
		self.text1=Label(self.FullMode,text='Orange Colors',font=('Helvetica 12 bold'))
		self.text1.grid(row=0,column=1,columnspan=4,sticky='W',pady=(10,0))

		#Two empty columns on left and right
		self.LeftWhiteBloc=Label(self.FullMode,font='HelveticaNeueBold',width=1)
		self.LeftWhiteBloc.grid(row=0,column=0,rowspan=12,sticky='W',pady=(10,0))

		self.RightWhiteBloc2=Label(self.FullMode,font='HelveticaNeueMedium',width=1)
		self.RightWhiteBloc2.grid(row=0,column=13,rowspan=12,sticky='W',pady=(10,0))

		#---------- color/title part ----------
		self.text2=Label(self.FullMode,text='Core colors black',font=('HelveticaNeue',10))
		self.text2.grid(row=1,column=1,columnspan=4,sticky='W')
		#-- line 1
		self.c1=Label(self.FullMode,bg='#000000',text='#000000',width=7,height=1,font=('HelveticaNeueThin',9),fg='white')
		self.c1.grid(row=3,column=2,padx=1,pady=(5,1))
		self.c1.bind('<Button-1>',self.ChangeColor)
		self.c2=Label(self.FullMode,bg='#FFFFFF',text='#FFFFFF',width=7,height=1,font=('HelveticaNeue',9),fg='#4A4A4A')
		self.c2.grid(row=3,column=3,padx=1,pady=(5,1))
		self.c2.bind('<Button-1>',self.ChangeColor)
		self.c3=Label(self.FullMode,bg='#F16E00',text='#F16E00',width=7,height=1,font=('HelveticaNeue',9),fg='white')
		self.c3.grid(row=3,column=4,padx=1,pady=(5,1))
		self.c3.bind('<Button-1>',self.ChangeColor)
		#--
		self.text3=Label(self.FullMode,text='Core colors',font=('HelveticaNeue',10))
		self.text3.grid(row=4,column=1,columnspan=4,sticky='W',pady=(5,0))
		#-- line 2
		self.c4=Label(self.FullMode,bg='#595959',text='#595959',width=7,height=1,font=('HelveticaNeue',9),fg='white')
		self.c4.grid(row=5,column=2,padx=1,pady=1)
		self.c4.bind('<Button-1>',self.ChangeColor)
		self.c5=Label(self.FullMode,bg='#8F8F8F',text='#8F8F8F',width=7,height=1,font=('HelveticaNeue',9),fg='#4A4A4A')
		self.c5.grid(row=5,column=3,padx=1,pady=1)
		self.c5.bind('<Button-1>',self.ChangeColor)
		self.c6=Label(self.FullMode,bg='#D6D6D6',text='#D6D6D6',width=7,height=1,font=('HelveticaNeue',9),fg='#4A4A4A')
		self.c6.grid(row=5,column=4,padx=1,pady=1)
		self.c6.bind('<Button-1>',self.ChangeColor)
		#--
		self.text3=Label(self.FullMode,text='Supporting colors',font=('HelveticaNeue',10))
		self.text3.grid(row=6,column=1,columnspan=4,sticky='W',pady=(5,0))
		#-- line 4
		self.c10=Label(self.FullMode,bg='#4BB4E6',text='#4BB4E6',width=7,height=1,font=('HelveticaNeue',9),fg='#4A4A4A')
		self.c10.grid(row=8,column=2,padx=1,pady=1)
		self.c10.bind('<Button-1>',self.ChangeColor)
		self.c11=Label(self.FullMode,bg='#50BE87',text='#50BE87',width=7,height=1,font=('HelveticaNeue',9),fg='#4A4A4A')
		self.c11.grid(row=8,column=3,padx=1,pady=1)
		self.c11.bind('<Button-1>',self.ChangeColor)
		self.c12=Label(self.FullMode,bg='#FFB4E6',text='#FFB4E6',width=7,height=1,font=('HelveticaNeue',9),fg='#4A4A4A')
		self.c12.grid(row=8,column=4,padx=1,pady=1)
		self.c12.bind('<Button-1>',self.ChangeColor)
		self.c13=Label(self.FullMode,bg='#A885D8',text='#A885D8',width=7,height=1,font=('HelveticaNeue',9),fg='#4A4A4A')
		self.c13.grid(row=8,column=5,padx=1,pady=1)
		self.c13.bind('<Button-1>',self.ChangeColor)
		self.c14=Label(self.FullMode,bg='#FFD200',text='#FFD200',width=7,height=1,font=('HelveticaNeue',9),fg='#4A4A4A')
		self.c14.grid(row=8,column=6,padx=(1,5),pady=1)
		self.c14.bind('<Button-1>',self.ChangeColor)
		#-- line 3
		self.c15=Label(self.FullMode,bg='#085EBD',text='#085EBD',width=7,height=1,font=('HelveticaNeue',9),fg='white')
		self.c15.grid(row=7,column=2,padx=1,pady=1)
		self.c15.bind('<Button-1>',self.ChangeColor)
		self.c16=Label(self.FullMode,bg='#0A6E31',text='#0A6E31',width=7,height=1,font=('HelveticaNeue',9),fg='white')
		self.c16.grid(row=7,column=3,padx=1,pady=1)
		self.c16.bind('<Button-1>',self.ChangeColor)
		self.c17=Label(self.FullMode,bg='#FF8AD4',text='#FF8AD4',width=7,height=1,font=('HelveticaNeue',9),fg='white')
		self.c17.grid(row=7,column=4,padx=1,pady=1)
		self.c17.bind('<Button-1>',self.ChangeColor)
		self.c18=Label(self.FullMode,bg='#492191',text='#492191',width=7,height=1,font=('HelveticaNeue',9),fg='white')
		self.c18.grid(row=7,column=5,padx=1,pady=1)
		self.c18.bind('<Button-1>',self.ChangeColor)
		self.c19=Label(self.FullMode,bg='#FFB400',text='#FFB400',width=7,height=1,font=('HelveticaNeue',9),fg='white')
		self.c19.grid(row=7,column=6,padx=(1,5),pady=1)
		self.c19.bind('<Button-1>',self.ChangeColor)
		#-- line 5
		self.c16=Label(self.FullMode,bg='#B5E8F7',text='#B5E8F7',width=7,height=1,font=('HelveticaNeue',9),fg='#4A4A4A')
		self.c16.grid(row=9,column=2,padx=1,pady=1)
		self.c16.bind('<Button-1>',self.ChangeColor)
		self.c17=Label(self.FullMode,bg='#B8EBD6',text='#B8EBD6',width=7,height=1,font=('HelveticaNeue',9),fg='#4A4A4A')
		self.c17.grid(row=9,column=3,padx=1,pady=1)
		self.c17.bind('<Button-1>',self.ChangeColor)
		self.c18=Label(self.FullMode,bg='#FFE8F7',text='#FFE8F7',width=7,height=1,font=('HelveticaNeue',9),fg='#4A4A4A')
		self.c18.grid(row=9,column=4,padx=1,pady=1)
		self.c18.bind('<Button-1>',self.ChangeColor)
		self.c19=Label(self.FullMode,bg='#D9C2F0',text='#D9C2F0',width=7,height=1,font=('HelveticaNeue',9),fg='#4A4A4A')
		self.c19.grid(row=9,column=5,padx=1,pady=1)
		self.c19.bind('<Button-1>',self.ChangeColor)
		self.c20=Label(self.FullMode,bg='#FFF6B6',text='#FFF6B6',width=7,height=1,font=('HelveticaNeue',9),fg='#4A4A4A')
		self.c20.grid(row=9,column=6,padx=(1,5),pady=1)
		self.c20.bind('<Button-1>',self.ChangeColor)
		#--
		self.text4=Label(self.FullMode,text='Skin tones',font=('HelveticaNeue',10))
		self.text4.grid(row=10,column=1,columnspan=4,sticky='W',pady=(5,0))
		#-- line 6
		self.c21=Label(self.FullMode,bg='#482E26',text='#482E26',width=7,height=1,font=('HelveticaNeue',9),fg='white')
		self.c21.grid(row=11,column=2,padx=1,pady=1)
		self.c21.bind('<Button-1>',self.ChangeColor)
		self.c22=Label(self.FullMode,bg='#62342D',text='#62342D',width=7,height=1,font=('HelveticaNeue',9),fg='white')
		self.c22.grid(row=11,column=3,padx=1,pady=1)
		self.c22.bind('<Button-1>',self.ChangeColor)
		self.c23=Label(self.FullMode,bg='#714E46',text='#714E46',width=7,height=1,font=('HelveticaNeue',9),fg='white')
		self.c23.grid(row=11,column=4,padx=1,pady=1)
		self.c23.bind('<Button-1>',self.ChangeColor)
		self.c24=Label(self.FullMode,bg='#C19372',text='#C19372',width=7,height=1,font=('HelveticaNeue',9),fg='#4A4A4A')
		self.c24.grid(row=11,column=5,padx=1,pady=1)
		self.c24.bind('<Button-1>',self.ChangeColor)
		self.c25=Label(self.FullMode,bg='#F4CFB2',text='#F4CFB2',width=7,height=1,font=('HelveticaNeue',9),fg='#4A4A4A')
		self.c25.grid(row=11,column=6,padx=(1,5),pady=1)
		self.c25.bind('<Button-1>',self.ChangeColor)
		self.c26=Label(self.FullMode,bg='#FFF6B6',text='#FFF6B6',width=7,height=1,font=('HelveticaNeue',9),fg='#4A4A4A')
		self.c26.grid(row=12,column=2,pady=(0,1))
		self.c26.bind('<Button-1>',self.ChangeColor)
		#-- line 7
		self.c27=Label(self.FullMode,bg='#FFE8F7',text='#FFE8F7',width=7,height=1,font=('HelveticaNeue',9),fg='#4A4A4A')
		self.c27.grid(row=12,column=3,pady=(0,1))
		self.c27.bind('<Button-1>',self.ChangeColor)
		#--
		self.text5=Label(self.FullMode,text='Functional colors',font=('HelveticaNeue',10))
		self.text5.grid(row=13,column=1,columnspan=4,sticky='W',pady=(5,0))
		#-- line 8
		self.c28=Label(self.FullMode,bg='#32C832',text='#32C832',width=7,height=1,font=('HelveticaNeue',9))
		self.c28.grid(row=14,column=2,pady=(0,16))
		self.c28.bind('<Button-1>',self.ChangeColor)
		self.c29=Label(self.FullMode,bg='#CD3C14',text='#CD3C14',width=7,height=1,font=('HelveticaNeue',9),fg='white')
		self.c29.grid(row=14,column=3,pady=(0,16))
		self.c29.bind('<Button-1>',self.ChangeColor)
		self.c30=Label(self.FullMode,bg='#527EDB',text='#527EDB',width=7,height=1,font=('HelveticaNeue',9))
		self.c30.grid(row=14,column=4,pady=(0,16))
		self.c30.bind('<Button-1>',self.ChangeColor)
		self.c31=Label(self.FullMode,bg='#FFCC00',text='#FFCC00',width=7,height=1,font=('HelveticaNeue',9))
		self.c31.grid(row=14,column=5,pady=(0,16))
		self.c31.bind('<Button-1>',self.ChangeColor)

		self.text6=Label(self.FullMode,text='Made with love by Charles',font=('HelveticaNeue',7),fg='#4A4A4A')
		self.text6.grid(row=15,column=1,columnspan=4,sticky='W',pady=(0,5))
	#---------- Global function ----------

	def ChangeColor(self,event):
		window.clipboard_clear()
		#Click event
		#nettoyer le cache!!!!!!!!!!
		event.widget.configure(state=ACTIVE)
		window.update()
		time.sleep(0.08)
		event.widget.configure(state=NORMAL)
		
		#Copy to the clipboard
		
		CopyColor=event.widget.cget('bg')
		WithoutHash=CopyColor.replace('#','')
		Clipboard=window.clipboard_append(WithoutHash)

	def RemoveGrid(self):
		InfoMinimizeMode=self.MinimizeMode.grid_info()
		InfoFullMode=self.FullMode.grid_info()

		if InfoMinimizeMode=={}:
			self.MinimizeMode.grid()
			self.FullMode.grid_forget()
			self.TabUserPreference['MinimizeMode']=True
			self.SaveUserPreference()
		else:
			self.MinimizeMode.grid_forget()
			self.FullMode.grid()
			self.TabUserPreference['MinimizeMode']=False
			self.SaveUserPreference()

	def SaveUserPreference(self):
		FichierUserPreference=open('UserPreference_data.dat','wb')
		pickle.dump(self.TabUserPreference,FichierUserPreference)
		FichierUserPreference.close()


window=Tk()
window.title('Orange Colors')
window.resizable(0,0)
window.attributes('-topmost',True)

#Let's go
MainApplication(window)
window.mainloop()
window.quit()
