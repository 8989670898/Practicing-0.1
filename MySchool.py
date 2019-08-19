import sqlite3
MySchool=sqlite3.connect('Schooltest.db')
cursSchool=MySchool.cursor()
cursSchool.execute(''''CREATETABLEstudent(
StudentIDINTEGERPRIMARYKEYAUTOINCREMENT,
nameTEXT(20)NOTNULL,
ageINTEGER,
marksREAL);''')
MySchool.close()
