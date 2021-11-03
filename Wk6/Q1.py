# .............................

# File: .py
# Author - Muhammed Shafeeq Thottathil
# Version:
# Created Date:  
# Modified Date: 
# Description :
# Listening : 

# ...............................

#create a class name as student
class STUDENT:

    def __init__(self, name, lnum):
        self._name = name
        self._roll = lnum
        print(self._name,self._lnum)

    @property
    def stud_details(self):
        print('Inside property')
        print(self._name,self._lnum)
        return self._name, self.lnum

    @stud_details.setter
    def stud_details(self, name, lnum):
        print("Inside stud_details")
        self._name = name
        self._roll = roll

    @property
    def display_person_details(self):
        print("Name: ".format(self._name))
        print("Roll Number: ".format(self.lnum))

class ROOM:

    def __init__(self, class_num):
        self._class_num = class_num

    @property
    def class_details(self):
        return self._class_num

    @class_details.setter
    def class_details(self, class_num):
        print('Inside class details')
        self._class_num = class_num
        # class_no: int = 4209

    @property
    def display_class_details(self):
        print('Class number: '.format(self._class_num))

class MODULE:

    def __init__(self, mod_num, mod_name):
        self._mod_name = mod_name
        self._mod_num = mod_num

    @property
    def mod_details(self):
        return self._mod_name, self._mod_num

    @mod_details.setter
    def mod_details(self, value):
        print('Inside mod_details')
        self._mod_name = value

    @property
    def display_mod_details(self):
        print("Module name: ".format(self._mod_name))
        print("Module number: ".format(self._mod_num))


