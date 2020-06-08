# -*- coding: utf-8 -*-
import csv
class Contact:

	def __init__(self, name, phone, email):
		self.name=name 
		self.phone=phone
		self.email=email

class ContactBook:
	def __init__(self):
		self._contacts=[]

	def add (self, name, phone, email):
		contact= Contact(name, phone, email)
		self._contacts.append(contact)
		self._save()

	def delete(self,name):
		for idx, contact in enumerate(self._contacts):
			if contact.name.lower()== name.lower():
				del self._contacts[idx]
				print('Se ha eliminado el contacto {}'.format(name))
				break
		self._save()

	def search(self,name):
		for contact in self._contacts:
			if contact.name.lower()== name.lower():
				self._print_contact(contact)
				break
		else:
			self._not_found()


	def _not_found(self):
		print('***********************')
		print(' Usuario no encontrado!')
		print('***********************')

	
	def show_all(self):
		print('  C O N T A C T O S ')
		print('______________________')
		for contact in self._contacts:
			self._print_contact(contact)
	def update(self,name):
		for contact in self._contacts:
			if contact.name.lower()==name.lower():
				print('Ingrese los nuevos valores')
				name=str(input('Escribe el nombre de contacto: '))
				phone=str(input('Escribe el tel de contacto: '))
				email=str(input('Escribe el email de contacto: '))
				contact.name=name 
				contact.phone=phone 
				contact.email=email 
				print('Contacto Actualizado!')
				self._print_contact(contact)
		self._save()

	def _print_contact(self, contact):
		print('---------------------------------')
		print('Nombre:  {}'.format(contact.name))
		print('Phone:   {}'.format(contact.phone))
		print('Email:   {}'.format(contact.email))

	def _save(self):
		with open('contacts.csv', 'w' ) as f:
			writer=csv.writer(f)
			writer.writerow(('name', 'phone', 'email'))
			for contact in self._contacts:
				writer.writerow((contact.name, contact.phone, contact.email))
def run():
	contact_book=ContactBook()
	contact_schema=['name','phone','email']
	with open('contacts.csv', 'r') as f:
		reader=csv.DictReader(f, fieldnames=contact_schema)
		for idx, row in enumerate(reader):
			if idx==0:
				continue
			contact_book.add(row['name'],row['phone'],row['email'])

	while True:
		comm=(str(input('''
			Que deseas hacer?
			[A] Añadir contacto
			[U] Actualizar contacto
			[B] Buscar contacto
			[E] Eliminar contacto
			[L] Listar contactos
			[S] SALIR
			''')))
		if (comm=='a' or comm=='A'):
			name=str(input('Escribe el nombre de contacto:'))
			phone=str(input('Escribe el tel de contacto:'))
			email=str(input('Escribe el email de contacto:'))
			contact_book.add(name,phone, email)

		if (comm=='u' or comm=='U'):
			name=str(input('Escribe el nombre de contacto que desea actualizar: '))
			contact_book.update(name)

		if (comm=='b' or comm=='B'):
			name=str(input('Buscar contacto: '))
			contact_book.search(name)

		if (comm=='e' or comm=='E'):
			name=str(input('Escribe el nombre de contacto que desea eliminar: '))
			contact_book.delete(name)

		if (comm=='l' or comm=='L'):
			contact_book.show_all()
		if (comm=='s' or comm=='S'):
			pass
if __name__ =='__main__':
	run()
