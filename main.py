#coding:utf-8
import os

file_contact = "contact.txt"

#this function allows to display all contacts from the text file
def display_contact():
	#open the file and read the file "contact.txt"
	with open(file=file_contact, mode="r", encoding='utf8') as f:
		#here we check if the file is empty we return empty
		#otherwise we display contacts
		if os.stat(file_contact).st_size == 0:
		 	print("нет контактов")
		else:
			print("имя\tфамилия\tочество\tорганизации\tтелефон_рабочий\tтелефон_личный")
			for contact in f:
				print(contact)



#Here the function allows to add new contact
def add_contact():
	#open the file and append new contact
	with open(file=file_contact, mode="a", encoding='utf8') as f:
		#data we want to add for every contact
		name                 = input("имя:")
		surname              = input("фамилия:")
		patronymic           = input("очество:")
		compagny_name        = input("название организации:")
		work_phone_number    = int(input("телефон рабочий:"))
		private_phone_number = int(input("телефон личный:"))
		f.write(f"{name}\t{surname}\t{patronymic}\t{compagny_name}\t{work_phone_number}\t{private_phone_number}\n")
		print("контакт добаблено")



#this function allows to edit contact added already 
def edit_contact():
	#field to enter the define contact we want to edit
	edit_data = input("зайти имя который хотите редактировать:")

	#open and read data from contact.txt by line
	with open(file=file_contact, mode="r", encoding='utf8') as f:
		contact = f.readlines()

	#find the index of contact and the names'contact from the file
	index =int()
	name  = ""
	for item in contact:
		if edit_data in item:
			index+=contact.index(item)
			name += edit_data

	#check if the index and the name exist in the file
	if name:
		try:
			data_list = contact[index].split()

			name                 = input(f"имя:")
			surname              = input(f"фамилия:")
			patronymic           = input(f"очество:")
			compagny_name        = input(f"название организации:")
			work_phone_number    = input(f"телефон рабочий:")
			private_phone_number = input(f"телефон личный:")

			#here we check if the user leave the fields empty 
			#we rewrite old data otherwise edit data in the case the contact 
			#is not in the file we can modify

			if name == "" and surname == "" and patronymic =="" and compagny_name == "" and work_phone_number == "" and private_phone_number == "":
				contact[index]= f"{data_list[0]}\t{data_list[1]}\t{data_list[2]}\t{data_list[3]}\t{data_list[4]}\t{data_list[5]}\n"
				with open(file=file_contact, mode="w", encoding='utf8') as f:	
					f.writelines(contact)
				display_contact()
			else:
				contact[index]= f"{name}\t{surname}\t{patronymic}\t{compagny_name}\t{work_phone_number}\t{private_phone_number}\n"
				with open(file=file_contact, mode="w", encoding='utf8') as f:	
					f.writelines(contact)
					print("контакт обноблено")
				display_contact()
		except:
			pass
			
	else:
		print("Not found")

#function allows to search contact by name
def search_contact():
	search_name = input("найти имя:")
	with open(file=file_contact, mode="r", encoding='utf8') as f:
		contact = f.readlines()

		#check if the name and the index exist in the file
		index =int()
		name  = ""
		for item in contact:
			if search_name in item:
				index+=contact.index(item)
				name += search_name
		if name:
			print("имя\tфамилия\tочество\tорганизации\tтелефон_рабочий\tтелефон_личный")
			print(contact[index])
		else:
			print("не найдено")


#this is the mai function to run the code
def main():
	while True:
		choice = int(input("1.вывод контакт\n2.Добавлять новый контак\n3.редактировать контакт\n4.пойск контакт\n5.выйти\nвыбираете номер:"))
		if choice == 1:
			display_contact()
		elif choice == 2:
			add_contact()
		elif choice == 3:
			edit_contact()
		elif choice == 4:
			search_contact()
		elif choice == 5:
			choose=input("хотите выйти? 'да' или 'нет':")
			if choose == "да":
				break
			else:
				pass
		else:
			break

#running the script 
if __name__ == '__main__':
	main()