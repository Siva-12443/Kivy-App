from kivy.metrics import dp

from kivymd.app import MDApp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.screen import MDScreen
import mysql.connector

class Example(MDApp):
    def build(self):
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
        screen = MDScreen()
        screen.add_widget(self.data_tables)
        return screen

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


Example().run()