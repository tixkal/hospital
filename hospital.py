import tkinter import*
from tkinter import ttk
import random
import time;
import datetime
import tkinter.messagebox

class Hospital:

    def __init__(self,root):
        self.root =root
        self.root.title("Hospital Management Sytem")
        self/root/geometry("1350x750+0+0")
        self.root.configure(background='powder blue')

       cmbNameTablets=stringvar()
       Ref = Stringvar()
       Dose =Stringvar()
       NumberTablets=StringVar()
       Lot=StringVar()
       IssuedDate=StringVar()
       ExpDate=StringVar()
       DailyDose=StringVar()
       PossibleSideEffects=StringVar()
       FurtherInfo=StringVar()
       DrivingUsingMachines=StringVar()
       StorageAdvise=StringVar()
       HowtouseMedication=StringVar()
       PatientID=StringVar()
       NHSNumber=StringVar()
       PatientName=StringVar()
       DateofBirth=StringVar()
       PatientAddress=StringVar()
       Prescription=StringVar()
       #===============================================FUNCTION DECLARATION=============================

       def iExit():
           iExit=tkinter.messagebox.askyesno("hospital management ssytem","confrim if you want to exit")
           if iExit >0:
               root.destroy()
               return

       def iPrescription():

           self.txtPrescription.insert(END,'Name of Tablets: \t\t\t\t' + cmnNameTablets.get() + "\n")
           self.txtPrescription.insert(END,'Reference No: \t\t\t\t' + Ref.get()+ "n")
           self.txtPrescription.insert(END,'Dose: \t\t\t\t' + Dose.get() + "\n")
           self.txtPrescription.insert(END,'Name of Tablets: \t\t\t\t' + NumberTablets.get() + "\n")
           self.txtPrescription.insert(END,'Lot: \t\t\t\t' + Lot.get() + "\n")
           self.txtPrescription.insert(END,'IssuedDate: \t\t\t\t' + IssuedDate.get() + "\n")
           self.txtPrescription.insert(END,'Exp. Date: \t\t\t\t' + Exp. Date.get() + "\n")
           self.txtPrescription.insert(END,'DailyDose: \t\t\t\t' + DailyDose.get() + "\n")
           self.txtPrescription.insert(END,'PossibleSideEffects: \t\t\t\t' + PossibleSideEffects.get() + "\n")
           self.txtPrescription.insert(END,'FurtherInfo: \t\t\t\t' + FurtherInfo.get() + "\n")
           self.txtPrescription.insert(END,'StorageAdvice: \t\t\t\t' + StorageAdvice.get() + "\n")
           self.txtPrescription.insert(END,'Driving or Using Machines: \t\t\t\t' + DrivingUsingMachines.get() + "\n")
           self.txtPrescription.insert(END,'How To Use Medication: \t\t\t\t' + How To Use Medication.get() + "\n")
           self.txtPrescription.insert(END,'PatientID: \t\t\t\t' + PatientID.get() + "\n")
           self.txtPrescription.insert(END,'NHS Number: \t\t\t\t' + NHSNumber.get() + "\n")
           self.txtPrescription.insert(END,'Patient Name: \t\t\t\t' + PatientName.get() + "\n")
           self.txtPrescription.insert(END,'Date Of Birth: \t\t\t\t' + Date Of Birth.get() + "\n")
           self.txtPrescription.insert(END,'PatientAddress: \t\t\t\t' + PatientAddres.get() + "\n")
          return

       def iReceipt():

           return

       def iDelete():

           cmbNameTablets.set("")
           self.cboNameTablet.current(0)
           Ref.set("")
           Dose.set("") 
           NumberTablets.set("")
           Lot.set("")
           IssuedDate.set("")
           ExpDate.set("")
           DailyDose.set("")
           PossibleSideEffects.set("")
           FurtherInfo.set("")
           StorageAdvise.set("")
           HowtouseMedication.set("")
           PatientID.set("")
           PatientName.set("")
           DOB.set("")
           PatientAddress.set("")
           self.txtPrescription.delete("1.0",END)
           self.txtFrameDetail.delete("1.0",END)
           
           return

       def iReset():

           cmbNameTablets.set("")
           self.cboNameTablet.current(0)
           Ref.set("")
           Dose.set("") 
           NumberTablets.set("")
           Lot.set("")
           IssuedDate.set("")
           ExpDate.set("")
           DailyDose.set("")
           PossibleSideEffects.set("")
           FurtherInfo.set("")
           StorageAdvise.set("")
           HowtouseMedication.set("")
           PatientID.set("")
           PatientName.set("")
           DOB.set("")
           PatientAddress.set("")
           selftxtPrescription.delete("1.0",END)
           self.txtFrameDetail.delete("1.0",END)

           return
       #======================================FRAME===============================================
       MainFrame =Frame(self.root)
       MainFrame.grid()

       TitleFrame = Frame(MainFrame, bd=20, width=1300, padx=20, relief=RIDGE)
       TitleFrame.pack(side=TOP)

       self.lbTitle =Label(TitleFrame, Font=('arial', 40,'bold') text="HospitalManangement System\t",padx=8)
       self.lbtitle.grid()

       FrameDetail =Frame(MainFrame, bd=20, width=1300, height=500, padx=20, relief=RIDGE)
       FrameDetail.pack(side=Bottom)

       ButtonFrame=Frame(MainFrame, bd=20, width=1300, height=50, padx=20, relief=RIDGE)
       ButtonFrame.pack(side=Bottom)

       DataFrame=Frame(DataFrame, bd=20, width=1300, padx-20, relief=RIDGE)
       DataFrame.pack(side=Bottom)
       
       DataFrameLEFT=LabelFrame(DataFrame, bd=20, width=1300, padx-20, relief=RIDGE
                           Font=('arial', 40,'bold') text="Patient Info:",)
       DataFrameLEFT.pack(side=LEFT)
       
       DataFrameRIGHT=LabelFrame(DataFrame, bd=20, width=1300, padx-20, relief=RIDGE
                                 , Font=('arial', 40,'bold') text="Prescription:",)
       DataFrameRIGHT.pack(side=RIGHT)

       self.lblNameTablet =Label(DataFrameLEFT, Font=('arial', 40,'bold') text="Name Of Tablet:",padx=2)
       self.lblNameTablet.grid(row=0. column=0,sticky=W)

       self.cboNameTablet=ttk.ComboBox(DataFrameLEFT,textvariable=cmbNameTablets, state='readonly')
                                        font=('arial', 12,'bold'), width=20)
       self.cboNameTablet['Value']={'','Ibuprofen','Co-codamol','Paracetamol','Amlodipine'}
       self.cboNameTablet.current(0)
       self.cboNameTablet.grid(row=0, column=0)

       self.lblFurther Info =Label(DataFrameLEFT, font=('arial', 40,'bold') text="Further Info:",padx=2)
       self.lblFurther Info.grid(row=0. column=2,sticky=W)
       self.txtFurther Info=Entry(DataFrameLEFT, font=('arial', 40,'bold'),textvariable = FurtherInfo)
       self.txtFurther Info.grid(row=0. column=3,sticky=W)

       self.lblRef =Label(DataFrameLEFT, font=('arial', 40,'bold') text="Reference No:",padx=2)
       self.lblRef.grid(row=1. column=0,sticky=W)
       self.txtRef=Entry(DataFrameLEFT, font=('arial', 40,'bold'),textvariable = Ref)
       self.txtRef.grid(row=1. column=1,sticky=W)

       self.lblStorage =Label(DataFrameLEFT, font=('arial', 40,'bold') text="Storage Advice:",padx=2)
       self.lblStorage.grid(row=1. column=2,sticky=W)
       self.txtStorage=Entry(DataFrameLEFT, font=('arial', 40,'bold'),textvariable = StorageAdvise)
       self.txtStorage.grid(row=1. column=3,sticky=W)

       self.lblDose =Label(DataFrameLEFT, font=('arial', 40,'bold') text="Dose:",padx=2)
       self.lblDose.grid(row=2. column=0,sticky=W)
       self.txtDose=Entry(DataFrameLEFT, font=('arial', 40,'bold'),textvariable = Dose )
       self.txtDose.grid(row=2. column=1,sticky=W)

       self.lblDUseMachine =Label(DataFrameLEFT, font=('arial', 40,'bold') text="DUseMachine:",padx=2)
       self.lblDUseMachine.grid(row=2. column=2,sticky=W)
       self.txtDUseMachine=Entry(DataFrameLEFT, font=('arial', 40,'bold'),textvariable = DrivingUsingMachines) )
       self.txtDUseMachine.grid(row=2. column=3,sticky=W)

       self.lblNoOfTablets =Label(DataFrameLEFT, font=('arial', 40,'bold') text="NoOfTablets:",padx=2)
       self.lblNoOfTablets.grid(row=2. column=0,sticky=W)
       self.txtNoOfTablets=Entry(DataFrameLEFT, font=('arial', 40,'bold'),textvariable = NumberTablets)
       self.txtNoOfTablets.grid(row=2. column=1,sticky=W)

       self.lblUseMedication =Label(DataFrameLEFT, font=('arial', 40,'bold') text="Driving Machines:",padx=2)
       self.lblUseMedication.grid(row=3. column=2,sticky=W)
       self.txtUseMedication=Entry(DataFrameLEFT, font=('arial', 40,'bold'),textvariable = HowtoUseMedication)
       self.txtUseMedication.grid(row=3. column=3,sticky=W)

       self.lblLot =Label(DataFrameLEFT, font=('arial', 40,'bold') text="Lot:",padx=2)
       self.lblLot.grid(row=4. column=0,sticky=W)
       self.txtLot=Entry(DataFrameLEFT, font=('arial', 40,'bold'),textvariable =Lot)
       self.txtLot.grid(row=4. column=1,sticky=W)

       self.lblIssuedDate =Label(DataFrameLEFT, font=('arial', 40,'bold') text="IssuedDate:",padx=2)
       self.lblIssuedDate.grid(row=4. column=0,sticky=W)
       self.txtIssuedDate=Entry(DataFrameLEFT, font=('arial', 40,'bold'),textvariable =IssuedDate)
       self.txtIssuedDate.grid(row=4. column=1,sticky=W)

       self.lblNHSNumber =Label(DataFrameLEFT, font=('arial', 40,'bold') text="NHS Number:",padx=2)
       self.lblNHSNumber.grid(row=5. column=2,sticky=W)
       self.txtNHSNumber=Entry(DataFrameLEFT, font=('arial', 40,'bold'),textvariable =NHSNumber)
       self.txtNHSNumber.grid(row=5. column=3,sticky=W)

       self.lblExpDate =Label(DataFrameLEFT, font=('arial', 40,'bold') text="ExpDate:",padx=2)
       self.lblExpDate.grid(row=6. column=2,sticky=W)
       self.txtExpDate=Entry(DataFrameLEFT, font=('arial', 40,'bold'),textvariable =ExpDate)
       self.txtExpDate.grid(row=6. column=3,sticky=W)

       self.lblPatientName =Label(DataFrameLEFT, font=('arial', 40,'bold') text="Patient Name:",padx=2)
       self.lblPatientName.grid(row=6. column=2,sticky=W)
       self.txtPatientName=Entry(DataFrameLEFT, font=('arial', 40,'bold'),textvariable =PatientName)
       self.txtPatientName.grid(row=6. column=3,sticky=W)

       self.lblDailyDose =Label(DataFrameLEFT, font=('arial', 40,'bold') text="Daily Dose:",padx=2)
       self.lblDailyDose.grid(row=7. column=0,sticky=W)
       self.txtDailyDose=Entry(DataFrameLEFT, font=('arial', 40,'bold'),textvariable =DailyDose)
       self.txtDailyDose.grid(row=7. column=1,sticky=W)

       self.lblDateofBirth =Label(DataFrameLEFT, font=('arial', 40,'bold') text="DateofBirth:",padx=2)
       self.lblDateofBirth.grid(row=7. column=2,sticky=W)
       self.txtDateofBirth=Entry(DataFrameLEFT, font=('arial', 40,'bold'),textvariable =DateofBirth)
       self.txtDateofBirth.grid(row=7. column=3,sticky=W)

       self.lblSideEffects =Label(DataFrameLEFT, font=('arial', 40,'bold') text="Side Effects:",padx=2)
       self.lblSideEffects.grid(row=8, column=0,sticky=W)
       self.txtSideEffects=Entry(DataFrameLEFT, font=('arial', 40,'bold'),textvariable =SideEffects)
       self.txtSideEffects.grid(row=8, column=1,sticky=W)

       self.lblPatientAddress =Label(DataFrameLEFT, font=('arial', 40,'bold') text="Patient Address:",padx=2)
       self.lblPatientAddress.grid(row=8, column=2,sticky=W)
       self.txtPatientAddress=Entry(DataFrameLEFT, font=('arial', 40,'bold'),textvariable =PatientAddress)
       self.txtPatientAddress.grid(row=8, column=3,sticky=W)

       #==========================================DATAFRAMERIGHT=================================
       
       self.txtPrescription=Text(DataFrameRIGHT, font=('arial', 40,'bold') ,padx=2)
       self.txtPrescription.grid(row=0, column=0)

       #==========================================BUTTONFRAME=================================
       self.btnPrescription=Button(ButtonFrame, text='Prescription',font=('arial', 12,'bold', width= 9,
                                    command=iPrescription)
       self.btnPrescription.grid(row=0,column=0)
       self.btnReceipt=Button(ButtonFrame, text='Receipt',font=('arial', 12,'bold', width= 9,
                               command=iReceipt)
       self.btnReceipt.grid(row=0,column=1)
       self.btnDelete=Button(ButtonFrame, text='Delete',font=('arial', 12,'bold', width= 9,
                              command=iDelete)
       self.btnDelete.grid(row=0,column=2)                            
       self.btnReset=Button(ButtonFrame, text='Reset',font=('arial', 12,'bold', width= 9,
                             command=iReset)
       self.btnReset.grid(row=0,column=3)                           
       self.btnExit=Button(ButtonFrame, text='Exit',font=('arial', 12,'bold', width= 9,
                            command=iExit)
       self.btnExit.grid(row=0,column=4)                                                                   

       #===========================================FRAMEDETAIL==============================
         
       self.lblLable =Label(FrameDetail, Font=('arial', 10,'bold') ,
        text="Name of Tablets\tReferenceNo.\t Dosage\t No of Tablets\t Lot\t Issued Date\t Exp. Date\
\tDaily Dose\tStorage Adv.\tNHS Number\t Patient Name\t DOB\t Address",)
       self.lblLabel.grid(row=0, column=0)  


       self.txtFrameDetail=Text(DataFrameRIGHT, font=('arial', 40,'bold') ,padx=2)
       self.txtFrameDetail.grid(row=1, column=0)        
       
       

       
       
       

       

       

       

       
       
if__name__=='__main__':
    root= Tk()
    application = Hospital (root)
    root.mainloop()
       
       
    
        
       
