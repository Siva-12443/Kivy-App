from kivymd.app import MDApp
from kivy.core.text import LabelBase
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.core.window import Window
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivy.uix.screenmanager import ScreenManager,Screen
from kivymd.uix.pickers import MDDatePicker 
import mysql.connector
from datetime import timedelta,datetime
import pandas as pd
import openpyxl
from kivy.uix.scrollview import ScrollView
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.uix.screen import MDScreen
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.snackbar import Snackbar
from kivy.metrics import dp
from kivymd.uix.button import MDFlatButton,MDRaisedButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.card import MDCardSwipe
from kivy.properties import StringProperty
import numpy as np
from kivymd.uix.textfield import MDTextField
import re
from kivymd.uix.card import (
    MDCardSwipe, MDCardSwipeLayerBox, MDCardSwipeFrontBox
)
from kivymd.uix.list import MDList, OneLineListItem
from kivymd.uix.button import MDIconButton
from kivymd.uix.toolbar import MDTopAppBar
from kivymd.uix.datatables import MDDataTable
from PyQt5.QtWidgets import QApplication, QMainWindow, QFileDialog
import pandas as pd
import sys
from sqlalchemy import create_engine


Window.size = (310,580)   

class Screen1(MDScreen):
    pass

class NavBar(FakeRectangularElevationBehavior,MDFloatLayout):
    pass

global from_date,to_date
from_date = [] 
to_date = []
food = []
date = []
date2 = []
date3 = []
date1 = []
lunch = []
lunch1 = []
snaks = []
snaks1 = []
t = []
food1 = []
t1 = []
price = []
price1 = []
delete_Canteen_id = []
delete_Student_id = []
global kk
class AdminPage(MDApp):
    dialog = None
    global  value, value1
    def build(self):
                
        #drop down menu code for report
        menu_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Brief Report", 
                "height": dp(56),
                "on_release": lambda x=f"Brief Report": self.genrate_report(),
               
             } ,
            {"viewclass": "OneLineListItem",
                "text": f"Detailed Report",
                "height": dp(56),
                "on_release": lambda x=f"Detailed Report": self.Detailed_report(),}]
        
        self.menu = MDDropdownMenu(
            items=menu_items,
            elevation=4,
            background_color=(1, 1, 1, 1),
            border_margin=dp(100),
            width_mult=4,
            radius=[24, 0, 24, 0]
        )
        
        #reload page menu
        menu1_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Delete the Selected Items", 
                "height": dp(56),
                "on_release": lambda x=f"Brief Report": self.delete_student_check(),
               
             } ,]
            
        
        self.menu1 = MDDropdownMenu(
            items=menu1_items,
            elevation=4,
            background_color=(1, 1, 1, 1),
            border_margin=dp(100),
            width_mult=4,
            radius=[24, 0, 24, 0]
        )
        
        #dropdown for delete in canteen
        down_items = [
            {
                "viewclass": "OneLineListItem",
                "text": f"Delete the Slected Iteams", 
                "height": dp(56),
                "on_release": lambda x=f"Brief Report": self.delete_canteen_check(),
               
             } ,]
        self.canteen_delete = MDDropdownMenu(
            items=down_items,
            elevation=4,
            background_color=(1, 1, 1, 1),
            border_margin=dp(100),
            width_mult=4,
            radius=[24, 0, 24, 0]
        )
        
        return Builder.load_file("Admin_page.kv")
    
    #canteen delete function
    def delete_canteen_check(self):
        data = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        cursor1 = data.cursor()
        for i in range(0,len(delete_Canteen_id)):
            query = "DELETE FROM canteen_table WHERE id={}".format(delete_Canteen_id[i])
            cursor1.execute(query) 
            data.commit()
            
    #student data delete function        
    def delete_student_check(self):
        data = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        cursor1 = data.cursor()
        for i in range(0,len(delete_Student_id)):
            query = "DELETE FROM student_table WHERE id={}".format(delete_Student_id[i])
            cursor1.execute(query) 
            data.commit()

    #Color Change in NavBar
    def change_color(self,instance):
        if instance in self.root.ids.values():
            current_id = list(self.root.ids.keys())[list(self.root.ids.values()).index(instance)]
            
            for i in range(3):
                if f"nav_icon{i+1}" == current_id:
                    self.root.ids[f"nav_icon{i+1}"].text_color = 1, 0, 0, 1
                    
                else:
                    self.root.ids[f"nav_icon{i+1}"].text_color = 0, 0, 0, 1

    #from date   
    def show_date_picker(self):
        date_dialog = MDDatePicker()
        date_dialog.bind(on_save=self.on_save, on_cancel=self.on_cancel)
        date_dialog.open()
        
    def on_save(self, instance, value, date_range):
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance: <kivymd.uix.picker.MDDatePicker object>;

        :param value: selected date;
        :type value: <class 'datetime.date'>;

        :param date_range: list of 'datetime.date' objects in the selected range;
        :type date_range: <class 'list'>;
        '''
        from_date.append(value)
       
        date_format = "%B %d, %Y"
        textt = value.strftime(date_format)
     
        
        self.text_field = MDTextField(
            pos_hint = {'center_x': .86,'center_y':.7},
        )
        self.text_field.text = str(textt)
        self.root.ids.r_screen.add_widget(self.text_field)
        
    def on_cancel(self, instance, value):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
        
    #to date
    def show_date_picker1(self):
        date_dialog1 = MDDatePicker()
        date_dialog1.bind(on_save=self.on_save1, on_cancel=self.on_cancel1)
        date_dialog1.open()
    
       
    def on_save1(self, instance1, value1, date_range1):
        database1 = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        mycursor1 = database1.cursor()
        
        '''
        Events called when the "OK" dialog box button is clicked.

        :type instance1: <kivymd.uix.picker.MDDatePicker object>;

        :param value1: selected date;
        :type value1: <class 'datetime.date'>;

        :param date_range1: list of 'datetime.date' objects in the selected range;
        :type date_range1: <class 'list'>;
        '''
        
        to_date.append(value1)
        
        date_format = "%B %d, %Y"
        textt = value1.strftime(date_format)
        
        self.text_field = MDTextField(
            pos_hint = {'center_x': .81,'center_y':.6},
        )
        self.text_field.text = str(textt)
        self.root.ids.r_screen.add_widget(self.text_field)  
        
        #total amount text
        
        
        
        #total amount 
        database = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        mycursor = database.cursor()      
        
        mycursor.execute("SELECT entryDateTime FROM canteen_table ")
        myresult = mycursor.fetchall()
            
        for x in myresult:
            date2.append(x)

      
        mycursor1.execute("SELECT food_category FROM canteen_table ")
        
        start_date = from_date[0]
        end_date = to_date[0]
        delta = timedelta(days=1)
        
        while start_date <= end_date:
            dd = start_date
            start_date += delta
            date3.append(dd)            
       
        for y in date2:
            for z in date3:
                if z in y:
                    rr=mycursor1.fetchone()
                    food1.append(rr)
                    t1.append(z)
        
        l = "Lunch"
        s = "Snack"
        lunch_price = 40
        snack_price = 10
        
        for k in food1:
            if l in k: 
                lunch1.append(k)
                price1.append(lunch_price)
            elif s in k:
                print("mkvnd",k)
                snaks1.append(k)
                price1.append(snack_price)
      
        total_amount_lunch = len(lunch1)*40
        total_amount_snacks = len(snaks1)*10
        payment = total_amount_lunch + total_amount_snacks
        
        self.text_field1 = MDTextField(
            pos_hint = {'center_x': .96,'center_y':.5},
        )
        self.text_field1.text = str(payment)
        self.root.ids.r_screen.add_widget(self.text_field1)
        
    def on_cancel1(self, instance1, value1):
        '''Events called when the "CANCEL" dialog box button is clicked.'''
        
    #reload page 
    def reload_page(self):
        sm = ScreenManager()   
        sm.add_widget(Screen1(name='main'))
        sm.current = "main"  
         
    def report(self,obj):
        print("hello world")
    
    #save student data
    def manageuser(self,obj):
        database1 = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        mycursor1 = database1.cursor()
        sql = 'INSERT INTO student_table(ID,studName,studRoll,studDept) VALUES(%s,%s,%s,%s)'
        no = 0
        kk = self.root.ids.StudentName.text
        kk1 = self.root.ids.RollNo.text
        kk2 = self.root.ids.Department.text
        values =[no,kk,kk1,kk2]
        mycursor1.execute(sql,values)
        database1.commit()
        self.dialog.dismiss()
        print(kk,kk1,kk2)

    #update student data
    def UpdateUser(self,obj):
        database11 = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
      
        mycursor11 = database11.cursor()
       
        sql11 = 'UPDATE student_table SET studName =%s ,studRoll=%s,studDept=%s WHERE studRoll=%s'
        
        kk = self.root.ids.StudentName1.text
        kk1 = self.root.ids.RollNo1.text
        kk2 = self.root.ids.Department1.text
        values11 =[kk,kk1,kk2,kk1]
        mycursor11.execute(sql11,values11)
        database11.commit()
        self.dialog1.dismiss()
        print(kk,kk1,kk2)
           
    def home12(self):
        self.screen_manager = ScreenManager()
        screen1 = Screen1(name="Home")
        self.screen_manager.add_widget(screen1)
    
    def dropdown1(self,button1):   
        self.menu1.caller = button1
        self.menu1.open()
    
    #excel file upload
    def excelupload(self):
        app = QApplication(sys.argv)
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("Excel files (*.xlsx)")
        file_dialog.setAcceptMode(QFileDialog.AcceptOpen)
        file_dialog.exec_()
        file_path = file_dialog.selectedFiles()[0] 
        df = pd.read_excel(file_path)

        # Connect to the database using sqlalchemy
        engine = create_engine('mysql+pymysql://root:%40Harishvenkat2000@localhost:3306/silverpos')

        # Write the DataFrame to the database
        df.to_sql('student_table', engine, if_exists='replace')
        
    #report dropdown
    def dropdown(self,button):   
        self.menu.caller = button
        self.menu.open()
        
    #canteen delete drop down call function 
    def Canteendown(self,button):   
        self.canteen_delete.caller = button
        self.canteen_delete.open()
        
    #add close   
    def close(self,obj):
        self.dialog.dismiss()
    
    #update close   
    def close1(self,obj):
        self.dialog1.dismiss()
    
    #add dialog box
    def show_alert_dialog(self):
        kkk = self.root.ids.StudentName.text
        kkk1 = self.root.ids.RollNo.text
        kkk2 = self.root.ids.Department.text 
        print(kkk,kkk1,kkk2)
        if not self.dialog:
            self.dialog = MDDialog(
                title = "Check Data",
                text= "Press Ok to Save",
                buttons=[
                    MDFlatButton(
                        text="Ok",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.manageuser,
                        
                    ),
                    MDRaisedButton(
                        text="DISCARD",
                        md_bg_color = "red" ,
                        on_release=self.close,
                        
                    ),
                ],
            )
        self.dialog.open()
        
    #update dialog box   
    def show_alert_dialog1(self):
        kkk = self.root.ids.StudentName1.text
        kkk1 = self.root.ids.RollNo1.text
        kkk2 = self.root.ids.Department1.text 
        print(kkk,kkk1,kkk2)
        if not self.dialog:
            self.dialog1 = MDDialog(
                title = "Check Data",
                text= "Press Ok to Save",
                buttons=[
                    MDFlatButton(
                        text="Ok",
                        theme_text_color="Custom",
                        text_color=self.theme_cls.primary_color,
                        on_release=self.UpdateUser,
                        
                    ),
                    MDRaisedButton(
                        text="DISCARD",
                        md_bg_color = "red" ,
                        on_release=self.close1,                        
                    ),
                ],
            )
        self.dialog1.open()

    #genrating breif report  
    def genrate_report(self):
        
        database = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        mycursor = database.cursor()
        
        mycursor1 = database.cursor()        
        
        mycursor.execute("SELECT entryDateTime FROM canteen_table ")
        myresult = mycursor.fetchall()
                
        #mycursor1.execute("SELECT food_category FROM canteen_table ")
        
        for x in myresult:
            date.append(x)
         
        mycursor1.execute("SELECT food_category FROM canteen_table ")
        start_date = from_date[0]
        end_date = to_date[0]
        delta = timedelta(days=1)
        while start_date <= end_date:
            dd = start_date
            start_date += delta
            date1.append(dd)            
            
        for y in date:
            for z in date1:
                if z in y:
                    rr=mycursor1.fetchone()
                    food.append(rr)
                    t.append(z)
        
        
        l = "Lunch"
        s = "Snack"
        lunch_price = 40
        snack_price = 10
        
        for k in food:
            if l in k:
                lunch.append(k)
                price.append(lunch_price)
            elif s in k:
                snaks.append(k)
                price.append(snack_price)
        
        dd = list(zip(t,food,price))           
        df = pd.DataFrame(dd,columns=['Date','Food','Cost'])
        df.to_excel("Brief_report{}.xlsx".format(pd.datetime.today().strftime('%y%m%d-%H$M%S')))
               
    #generating detailed report
    
    def Detailed_report(self):
        print("detailed report")
        
        
        
    #swipe to delete student data  
    def on_start(self):
        #data table for canteen delete 
        database1 = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        mycursor1 = database1.cursor()
        mycursor2 = database1.cursor()
        mycursor3 = database1.cursor()
        mycursor4 = database1.cursor()
        
        mycursor1.execute("SELECT idcanteen FROM canteen_table ")
        myresult = mycursor1.fetchall()
        
        mycursor2.execute("SELECT  entryDateTime FROM canteen_table ")
        myresult2 = mycursor1.fetchall()
        
        mycursor3.execute("SELECT food_category FROM canteen_table ")
        myresult3 = mycursor1.fetchall()

        mycursor4.execute("SELECT stud_name FROM canteen_table ")
        myresult4 = mycursor1.fetchall()

        res = []
        result2= []
        result3 = []
        result4 = []
        
        for i in range(0,len(myresult)):
            res.extend(myresult[i])
            result2.extend(myresult2[i])
            result3.extend(myresult3[i])
            result4.extend(myresult4[i])

        self.root.ids.datatable.add_widget(
            MDTopAppBar(
                id = 'button1' ,
                title= "Delete Canteen User",
                anchor_title= "left",
                md_bg_color='red',
                right_action_items = [["dots-vertical", lambda x: self.Canteendown(x)]],
                pos_hint = {"center_y":0.95}))
       
        self.datatables = MDDataTable(
            check=True,
            use_pagination=True,
            rows_num = 10,
            column_data=[
                ("No.", dp(20)),
                ("date", dp(20)),
                ("food", dp(20)),
                ("name", dp(20)),],  
            row_data=[
                (
                    res[i],
                    result2[i],
                    result3[i],
                    result4[i],
                )for i in range(0,len(res))],)   
        
        self.datatables.bind(on_check_press=self.on_check_press)
        self.root.ids.datatable.add_widget(self.datatables)

        #delete table for student data
        
        database = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        my1 = database.cursor()    
        my2 = database.cursor()
        my3 = database.cursor()
        my4 = database.cursor()  
        
        my1.execute("SELECT id FROM student_table ")
        myr1 = my1.fetchall()
        
        my2.execute("SELECT studName FROM student_table ")
        myr2 = my1.fetchall()
        
        my3.execute("SELECT studRoll FROM student_table ")
        myr3 = my1.fetchall()
        
        my4.execute("SELECT studDept FROM student_table ")
        myr4 = my1.fetchall()
        #myresult = mycursor.fetchall()   
                                                                                                  
        rr1 = []
        rr2 = []
        rr3 = []
        rr4 = []
        for i in range(0,len(myr1)):
            rr1.extend(myr1[i])
            rr2.extend(myr2[i])
            rr3.extend(myr3[i])
            rr4.extend(myr4[i])
            
        self.root.ids.md_list.add_widget(
            MDTopAppBar(
                id = 'button1' ,
                title= "Delete User",
                anchor_title= "left",
                md_bg_color='red',
                right_action_items = [["dots-vertical", lambda x: self.dropdown1(x)]],))

        self.student_table = MDDataTable(
            check=True,
            use_pagination=True,
            rows_num = 10,
            column_data=[
                ("No.", dp(20)),
                ("Name", dp(20)),
                ("Roll No", dp(20)),
                ("Dept", dp(20)),],  
            row_data=[
                (
                    rr1[i],
                    rr2[i],
                    rr3[i],
                    rr4[i],
                )for i in range(0,len(rr1))],)
        
        self.student_table.bind(on_check_press=self.on_check_student)
        self.root.ids.md_list.add_widget(self.student_table)
        
    def on_check_press(self, instance_table, current_row):
        '''Called when the check box in the table row is checked.'''
        delete_Canteen_id.append(current_row[0])
        
    def on_check_student(self,instance_table1,current_row1):
        delete_Student_id.append(current_row1[0])

    def remove_item(self, instance):
        database = mysql.connector.Connect(host="localhost", user="root", password="@Harishvenkat2000", database= "silverpos")
        mycursor = database.cursor()
        self.root.ids.md_list.remove_widget(instance.parent.parent)
    
        
if __name__ == "__main__":
    LabelBase.register(name="Poppins", fn_regular="C:\\Users\\hp\\Downloads\\Poppins\\Poppins-Bold.ttf")
    LabelBase.register(name="MPoppins", fn_regular="C:\\Users\\hp\\Downloads\\Poppins\\Poppins-Medium.ttf")
    LabelBase.register(name="SPoppins", fn_regular="C:\\Users\\hp\\Downloads\\Poppins\\Poppins-SemiBold.ttf")
    LabelBase.register(name="BPoppins", fn_regular="C:\\Users\\hp\\Downloads\\Poppins\\Poppins-Regular.ttf")
    AdminPage().run() 