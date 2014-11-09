#!/usr/bin/python -utt
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
	#return d[key] if (key in d) else None
	if key in d:
		return d[key]
	#else:
	#	return None
		
		
		
#    Если такого ключа нет, то выдавать значение из заданного
#    кортежа значений по-умолчанию. Значения из него брать по
#    очереди.

#defaults = (1, 2, 3);
#default_elements_fetched = 0;
#defaults[default_elements_fetched % len(defaults)]

def take_from_dict_with_defaults(key, d):
	ret = None
	if key in d:
		ret = d[key]
	else:
		ret = take_from_dict_with_defaults.defaults[take_from_dict_with_defaults.default_elements_fetched % len(take_from_dict_with_defaults.defaults)]
		take_from_dict_with_defaults.default_elements_fetched += 1
	return ret

take_from_dict_with_defaults.defaults = (1, 2, 3);
take_from_dict_with_defaults.default_elements_fetched = 0;	


def take_from_dict(key, d):
	'''
	Выдает значение словаря по ключу и удаляет его из словаря
	- аналог метода словаря d.pop(key)
	
	Вопрос 6: исправить МНОГО ошибок, добавить значение по-умолчанию
	'''
	ret = None
	if key in d:
		ret=d[key]
		del d[key]
	return ret
		
		
		
def insert_in_dict_if_no(key, d, value):
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
	lst = ['a', 'A', 'b', 'B', 'c', 'C']

	insert_in_lst_if_no("a", lst)
	insert_in_lst_if_no("c", lst)
	insert_in_lst_if_no("e", lst)
	insert_in_lst_if_no("e", lst)
	print lst

