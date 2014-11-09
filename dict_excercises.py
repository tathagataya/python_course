#!/usr/bin/env python -utt
# coding: utf-8

from datetime import datetime
import os



	
def choose_by_dict(key, d):
	'''
	Аналог метода словаря d.get(key) - возвращает
	элемент словаря по ключу - в случае, если такого
	элемента нет, выдает None - вместо возбуждения
	исключения
	
	Вопрос 4: упростите, убрав else
	'''
	if key in d:
		return d[key]
	else:
		return None
		
		
		
# 5. Создать функцию, берущую из словаря значение по ключу,
#    Если такого ключа нет, то выдавать значение из заданного
#    кортежа значений по-умолчанию. Значения из него брать по
#    очереди.




def take_from_dict(d, key):
	'''
	Выдает значение словаря по ключу и удаляет его из словаря
	- аналог метода словаря d.pop(key)
	
	Вопрос 6: исправить МНОГО ошибок, добавить значение по-умолчанию
	'''
	return d[key]
	if key not in d:
		del d[key]
		
		
		
		
def insert_in_dict_if_no(d, key, value):
	'''
	Аналог метода словаря d.setdefault(key, default)
	'''
	if key in d:
		return d[key]
	else:
		d[key] = value
		return value
		
## 7. Создать по аналогии функцию, добавляющую значение в
##    список, только если такого значения там нет
## 8. Создать функцию, фильтрующую список по списку "банлиста",
##    То есть если элемент присутствует в банлисте, то удалять
##	  элемент из списка





def del_list_item_by_index(lst, i):
	'''
	Удаляет элемент по индексу
	
	Вопрос 9: добавить проверку на существование элемента
	'''
	del lst[i]
	
	
	
	
def del_list_item(lst, x):
	'''
	Аналог метода списка lst.remove(x)
	
	Вопрос 10: добавить проверки и исправить кое-что еще...
	
	Вопрос 11: сравнить поведение с поведением lst.remove(x), в чем разница?
	'''
	for i, a in enumerate(lst):
		if a == x:
			del lst[i]
			
			
		
if __name__=='__main__':
	# При запуске модуля как программы посчитаем размер текущей
	# директории и выведем на экран

	print u'Размер директории "%s" = %d байт' % (
		os.path.abspath('.'),
		calc_dir_size('.'),
	)