import re
from kivy.core.text import LabelBase
from kivy.uix.screenmanager import ScreenManager, Screen
from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
import mysql.connector
from kivy.metrics import dp
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.lang import Builder
import mysql.connector
from kivymd.uix.screen import MDScreen
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.uix.image import Image
from datetime import date
from kivymd.uix.dialog import MDDialog
from kivymd.uix.toolbar import MDTopAppBar
from pyzbar.pyzbar import decode
import cv2
from kivy.graphics.texture import Texture
from kivymd.uix.button import MDFlatButton
import time
from collections import OrderedDict
from kivymd.uix.behaviors import FakeRectangularElevationBehavior
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp
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

Window.size = (310, 580)

class DropdownButton(MDFloatLayout, Button):
    pass

class SearchBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

class NavBar(FakeRectangularElevationBehavior, MDFloatLayout):
    pass

TopTool_Example = """

MDBoxLayout:
    orientation: "vertical"

MDIconButton:
    icon: "arrow-left"
    pos_hint: {"center_y": .95}
    user_font_size: "30sp"
    theme_text_color: "Custom"
    text_color: rgba(26, 24, 58, 255)
    on_release:
        app.root.transition.direction = "right"
        app.root.current = "bottom"    
"""
class Example(Screen):
    def __init__(self, **kwargs):
        super(Example,self).__init__(**kwargs)
    #    layout=MDBoxLayout(orientation='vertical')
    #    TopBar = MDTopAppBar(title = "QRScanner", font_name= "Poppins/Poppins-SemiBold.ttf", font_size= "26sp", pos_hint= {"center_x": .5, "center_y": .1}, text_color = (0.49, 0.498, 0.498, 1), left_action_items = ([["arrow-left-circle-outline", lambda x : app.root.current = "bottom"]]))
       #, left_action_items = [["arrow-left-circle-outline", lambda *args : setattr(self.manager, "current", "third")]]
       #ViewReport = MDFlatButton(text = "View Report", on_press = self.MovetoFourScreen, pos_hint = {'center_x': 0.5, 'center_y': 0.2})
        TopTools = Builder.load_string(TopTool)
        self.add_widget(TopTools)
        database1 = mysql.connector.Connect(host="localhost", user="root", password="Test123", database= "siva")
        mycursor1 = database1.cursor()
        mycursor2 = database1.cursor()
        mycursor3 = database1.cursor()
        mycursor4 = database1.cursor()
        
        mycursor1.execute("SELECT id FROM canteen_table ")
        myresult = mycursor1.fetchall()
        
        mycursor2.execute("SELECT  entryDateTime FROM canteen_table ")
        myresult2 = mycursor1.fetchall()
        
        mycursor3.execute("SELECT food_category FROM canteen_table ")
        myresult3 = mycursor1.fetchall()
        
        mycursor4.execute("SELECT stud_name FROM canteen_table ")
        myresult4 = mycursor1.fetchall()
        
        result = []
        result2= []
        result3 = []
        result4 = []
        
        for i in range(0,len(myresult)):
            result.extend(myresult[i])
            result2.extend(myresult2[i])
            result3.extend(myresult3[i])
            result4.extend(myresult4[i])
            
        
        self.data_tables = MDDataTable(
            use_pagination=True,
            check=True,
            column_data=[
                ("No.", dp(30)),
                ("date", dp(30)),
                ("food", dp(30)),
                ("name", dp(30)),
            ],
            row_data=[
                (
                   result[i],
                    result2[i],
                    result3[i],
                    result4[i],
                )for i in range(0,len(result)) ],
            
            sorted_on="Schedule",
            sorted_order="ASC",
            elevation=2,
        )
        self.data_tables.bind(on_row_press=self.on_row_press)
        self.data_tables.bind(on_check_press=self.on_check_press)
        self.add_widget(self.data_tables)
   

    def on_row_press(self, instance_table, instance_row):
        '''Called when a table row is clicked.'''

        print(instance_table, instance_row)

    def on_check_press(self, instance_table, current_row):
        '''Called when the check box in the table row is checked.'''

        print(instance_table, current_row)

    # Sorting Methods:
    # since the https://github.com/kivymd/KivyMD/pull/914 request, the
    # sorting method requires you to sort out the indexes of each data value
    # for the support of selections.
    #
    # The most common method to do this is with the use of the builtin function
    # zip and enumerate, see the example below for more info.
    #
    # The result given by these funcitons must be a list in the format of
    # [Indexes, Sorted_Row_Data]

    def sort_on_signal(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][2]))

    def sort_on_schedule(self, data):
        return zip(
            *sorted(
                enumerate(data),
                key=lambda l: sum(
                    [
                        int(l[1][-2].split(":")[0]) * 60,
                        int(l[1][-2].split(":")[1]),
                    ]
                ),
            )
        )

    def sort_on_team(self, data):
        return zip(*sorted(enumerate(data), key=lambda l: l[1][-1]))
    
class LoginPage(MDApp):

    btn_color = ListProperty((177/255, 35/255, 65/255, 1))
    regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    database = mysql.connector.Connect(host="localhost", user="root", password="Test123", database= "siva")
    cursor = database.cursor()
    def __init__(self, **kwargs):
       super(LoginPage,self).__init__(**kwargs)
    
    def build(self):
        global screen_manager
        screen_manager = ScreenManager()
        screen_manager.add_widget(Builder.load_file("pre-splash.kv"))
        screen_manager.add_widget(Builder.load_file("main.kv"))
        screen_manager.add_widget(Builder.load_file("login.kv"))
        screen_manager.add_widget(Builder.load_file("signup.kv"))
        screen_manager.add_widget(QrScanner(name = "QrScanner"))
        screen_manager.add_widget(Builder.load_file("details.kv"))
        screen_manager.add_widget(Builder.load_file("bottom.kv"))
        screen_manager.add_widget(Builder.load_file("Admin_page.kv"))
        screen_manager.add_widget(Example(name = "Example"))
        return screen_manager
    
    def set_snackLunch(self, category, stud_roll, stud_name):

        try:
            Today_Date = date.today() # current date and time
            date_string = Today_Date.strftime("%Y-%m-%d")
            connections = Db_Operations()
            val = connections.Last_Date(stud_roll, category)
            if val == date_string:
                print("User Already bought!")
                self.dialog = MDDialog(
                    text="User already bought " + category + " today.",
                    buttons=[
                        MDFlatButton(
                            text="Ok",
                            on_press = self.RemainSameScreen
                        ),
                    ],)
                self.dialog.open()
            else:
                self.cursor.execute(f"INSERT INTO canteen_table (entryDateTime, food_category, stud_roll, stud_name) VALUES( '{date_string}', ' {category.strip()}', '{stud_roll}', '{stud_name}')")     
                self.database.commit() #this is importnt to insert query to database
                print("Values successfully inserted!")
                print(date_string)
        except Exception as e:
            print(e)
        finally:
            print("Send data function ends here")
            self.root.current = "QrScanner"
            
    def RemainSameScreen(self, *args):
        self.dialog.dismiss(force=True)

    def on_start(self):
        Clock.schedule_once(self.login, 2)

    def login(self, *args):
     screen_manager.current = "main"

    def get_id(self, instance):
        for id, widget in instance.parent.parent.parent.ids.items():
            if widget.__self__ == instance:
                return id
     
    def change_color(self,instance):
        if instance in self.root.ids.values():
            current_id = list(self.root.ids.keys())[list(self.root.ids.values()).index(instance)]
            
            for i in range(4):
                if f"nav_icon{i+1}" == current_id:
                    self.root.ids[f"nav_icon{i+1}"].text_color = 0, 0, 0, 1
                
                else:
                    self.root.ids[f"nav_icon{i+1}"].text_color = 1, 0, 0, 0
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
        engine = create_engine('mysql://root:@@Harishvenkat2000@@localhost/silverpos')

        # Write the DataFrame to the database
        df.to_sql('student_table', engine, if_exists='replace')

    
    def send_data(self, name, canteen_name, user_name, passw, apprights):
       #here is the function to send data from python to mysql
       try:
               self.cursor.execute(f"INSERT INTO login_table (name, canteen_name, user_name, passw, AppRights) VALUES('{name.text}', '{canteen_name.text}', '{user_name.text}', '{passw.text}', '{apprights.text}')")     
               self.database.commit() #this is importnt to insert query to database
               name.text = ""
               canteen_name.text = ""
               user_name.text = ""
               passw.text = ""
               apprights.text = ""
               print("Values successfully inserted!")
       except:
            print("There was an error while Adding Values")
       finally:
            print("Send data function ends here")
            self.root.current = "login"

    def receive_data(self, name, password):
        #here is the function to receive data from mysql to python and validate it with text field text
        self.cursor.execute("SELECT * FROM login_table")
        name_list = []
        for i in self.cursor.fetchall():
            name_list.append(i[3])
        if name.text in name_list and name.text !="":
            self.cursor.execute(f"SELECT passw FROM login_table WHERE user_name='{name.text}'")
            for j in self.cursor:
                if password.text == j[0]:
                    connections = Db_Operations()
                    AppRights = connections.Check_Apprights(name.text, password.text)
                    if AppRights == 'User':
                        print("You have Successfully Logged In !!")
                        self.root.current = "bottom"
                        Canteen_name = connections.Get_CanteenName(name.text, password.text)
                        self.manager.get_screen("bottom").ids.Canteen_Name.text = Canteen_name
                        #screen_manager.get_screen('bottom').ids.username.hint_text = name.text
                        #self.manager.get_screen("bottom").ids.username.text = name.text
                    else:
                        self.root.current = "Admin"
                else:
                    print("Incorrect Password")
        else:
            print("Invalid Username")
        
    # def Show_DataTable(self):
    #     self.root.current = "DataTable"

class Db_Operations:
    def __init__(self):
        self.mydb = mysql.connector.connect(
            host='localhost',
            user='root',
            passwd='Test123',
            database='siva'
        )
        self.mycursor = self.mydb.cursor()
        self.studRoll = ""

    def get_studentDetails(self):
        _student = OrderedDict()
        _student['studRoll'] = {}
        global studRolls
        studRolls = []
        sql = "SELECT * FROM student_table"
        self.mycursor.execute(sql)
        students = self.mycursor.fetchall()
        for student in students:
            studRolls.append(student[1])
        users_length = len(studRolls)
        idx = 0
        while idx < users_length:
            _student['studRoll'][idx] = studRolls[idx]
            idx += 1
    
    def set_rollno(self, rollno):
        self.studRoll = rollno
        print("Roll Number: "+ self.studRoll)
        _stud = OrderedDict()
        _stud['studName'] = {}
        global studName
        studName = ''
        sql = "SELECT * FROM student_table WHERE studRoll = '" +  rollno + "'"
        self.mycursor.execute(sql)
        studs = self.mycursor.fetchall()
        for stud in studs:
            studName = f'{studName}{stud[2]}'
        print("N: "+studName)
        print("N: " + rollno)
        return studName
    
    def Last_Date(self, studentRoll, category):
        LDate = ''
        sql = "SELECT MAX(entryDateTime) FROM canteen_table WHERE stud_roll = '" + studentRoll + "' AND food_category = '" + category + "'"
        self.mycursor.execute(sql)
        LDates = self.mycursor.fetchall()
        for LDat in LDates:
            LDate = f'{LDate}{LDat[0]}'
        print("Last Time Student Ate on: " + LDate)
        return LDate
    
    def Check_Apprights(self, user_name, password):
        AppRight = ''
        sql = "SELECT AppRights FROM login_table WHERE user_name='"+user_name+"' AND passw = '"+password+"'"
        self.mycursor.execute(sql)
        AppRights = self.mycursor.fetchall()
        for AppRigh in AppRights:
            AppRight = f'{AppRight}{AppRigh[0]}'
        print("The user is a " + AppRight)
        return AppRight
    
    def Get_CanteenName(self, user_name, password):  
        Canteen_name = ""
        sql = "SELECT canteen_name FROM login_table WHERE user_name = '" + user_name + "' AND passw = '" + password + "'"
        self.mycursor.execute(sql)
        Canteen_names = self.mycursor.fetchall()
        for Canteen in Canteen_names:
            Canteen_name = f'{Canteen_name}{Canteen[0]}'
        print("The Canteen Name is: " + Canteen_name)
        return Canteen_name
    
    def Get_FullName(self, user_name, password):
        FullName = ""
        sql = "SELECT name FROM login_table WHERE user_name = '" + user_name + "' AND passw = '" + password + "'"
        self.mycursor.execute(sql)
        FullNames = self.mycursor.fetchall()
        for Name in FullNames:
            FullName = f'{FullName}{Name[0]}'
        print('The Full Name is: ' + FullName)
        return FullName
TopTool = """

MDBoxLayout:
    orientation: "vertical"

    MDIconButton:
        icon: "arrow-left"
        pos_hint: {"center_y": .95}
        user_font_size: "30sp"
        theme_text_color: "Custom"
        text_color: rgba(26, 24, 58, 255)
        on_release:
            app.root.transition.direction = "right"
            app.root.current = "bottom"

    MDLabel:
        text: "                          Scan QR"
        font_name: "Poppins"   
        font_size: "18sp"
        pos_hint: {"center_x" : .5}

    MDLabel:
        text: " "
        font_name: "Poppins"   
        font_size: "18sp"	
    MDLabel:
        text: " "
        font_name: "Poppins"   
        font_size: "18sp"
    MDLabel:
        text: " "
        font_name: "Poppins"   
        font_size: "18sp"

"""

class QrScanner(Screen):
    def __init__(self, **kwargs):
       super(QrScanner,self).__init__(**kwargs)
    #    layout=MDBoxLayout(orientation='vertical')
    #    TopBar = MDTopAppBar(title = "QRScanner", font_name= "Poppins/Poppins-SemiBold.ttf", font_size= "26sp", pos_hint= {"center_x": .5, "center_y": .1}, text_color = (0.49, 0.498, 0.498, 1), left_action_items = ([["arrow-left-circle-outline", lambda x : app.root.current = "bottom"]]))
       #, left_action_items = [["arrow-left-circle-outline", lambda *args : setattr(self.manager, "current", "third")]]
       #ViewReport = MDFlatButton(text = "View Report", on_press = self.MovetoFourScreen, pos_hint = {'center_x': 0.5, 'center_y': 0.2})
       TopTools = Builder.load_string(TopTool)
       self.add_widget(TopTools)
       self.image=Image()
       self.add_widget(self.image)
        #self.save_img_button=(MDFillRoundFlatButton(text="Detect URL",pos_hint={'center_x':0.5,'center_y':0.3},size_hint=(None,None)))
        #self.save_img_button.bind(on_press=self.take_picture)
        #layout.add_widget(self.save_img_button)
       self.capture=cv2.VideoCapture(0)
       self.detector = cv2.QRCodeDetector()
       Clock.schedule_interval(self.load_video,1.0/30.0)
       #self.add_widget(ViewReport)

    def load_video(self,*args):
        ret,frame=self.capture.read()
        for code in decode(frame):
            print(code.data.decode('utf-8'))
            time.sleep(0.5)
            connections = Db_Operations()
            values = connections.get_studentDetails()
            if code.data.decode('utf-8') in studRolls:
                global studentRollnumber
                studentRollnumber = code.data.decode('utf-8')
                val = connections.set_rollno(studentRollnumber)
                self.manager.get_screen("details").ids.student_name.text = val.title()
                self.MovetoFourScreen(studentRollnumber)
            else:
               self.dialog = MDDialog(
                text="Invalid QR",
                buttons=[
                    MDFlatButton(
                        text="Ok",
                        on_press = self.RemainSameScreen
                    ),
                ],)
               self.dialog.open()
        self.image_frame=frame
        buffer=cv2.flip(frame,0).tobytes()
        texture=Texture.create(size=(frame.shape[1],frame.shape[0]), colorfmt='bgr')
        texture.blit_buffer(buffer, colorfmt='bgr', bufferfmt='ubyte')
        self.image.texture = texture
    
    def RemainSameScreen(self, *args):
        self.dialog.dismiss(force=True)

    def MovetoFourScreen(self, roll_no):
        self.manager.get_screen("details").ids.roll_number.text = roll_no
        self.manager.current = "details"

if __name__ == "__main__":
    LabelBase.register(name="Poppins", fn_regular="C:\\Users\\Welcome\\Downloads\\Poppins\\Poppins-Bold.ttf")
    LabelBase.register(name="MPoppins", fn_regular="C:\\Users\\Welcome\\Downloads\\Poppins\\Poppins-Medium.ttf")
    LabelBase.register(name="SPoppins", fn_regular="C:\\Users\\Welcome\\Downloads\\Poppins\\Poppins-SemiBold.ttf")
    LabelBase.register(name="BPoppins", fn_regular="C:\\Users\\Welcome\\Downloads\\Poppins\\Poppins-Regular.ttf")
    LoginPage().run()