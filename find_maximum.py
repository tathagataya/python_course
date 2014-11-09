#!/usr/bin/python -utt
# coding: utf-8

from datetime import datetime
import os
import random

def find_maximum(lst):
	'''
	Эта функция - аналог функции max - находит
	максимальный элемент в списке
	
	Вопрос 1: найдите ошибку и исправьте
		'''
	if len(lst) == 0:
		return None

	max_a = lst[0]
	
	for a in lst:
		if a > max_a:
			max_a = a
	return max_a
	
## 2. Создать функции:
##      find_minimum       - находит минимальный элемент
def find_minimum(lst):
	if len(lst) == 0:
		return None

	min_a = lst[0]
	
	for a in lst:
		if a < min_a:
			min_a = a
	return min_a	


##      calc_same_count    - считает количество таких же элементов (
##                           добавить второй аргумент, с которым сравнивать)
def calc_same_count(lst, ethalon):
	equal_elements_found = 0
	for i in lst:
		if i == ethalon: # if operator==(i, ethalon):
			equal_elements_found += 1
	return equal_elements_found

##      sort			   - сортирует от минимального к максимальному
##		limit_values_upper - все элементы меньше заданного приравнивает к заданному
def limit_values_upper(lst, lower_limit):
	ret = []
	for i in lst:
		#print 'Checking element ', i, 'list state', lst
		if i < lower_limit:
			#print 'element below bound, changing'
			i = lower_limit
			#print 'Element after', i, 'List after change', lst
		ret.append(i)
	return ret


##		limit_values_lower - все элементы больше заданного приравнивает к заданному
def limit_values_lower(lst, upper_limit):
	ret = []
	for i in lst:
		#print 'Checking element ', i, 'list state', lst
		if i > upper_limit:
			#print 'element below bound, changing'
			i = upper_limit
			#print 'Element after', i, 'List after change', lst
		ret.append(i)
	return ret


##		limit_in_range     - по аналогии лимитирует в диапазоне от и до
def limit_in_range(lst, lower_limit, upper_limit):
	ret=[]
	for i in lst:
		if i < lower_limit:
			i=lower_limit
		elif i > upper_limit:
			i=upper_limit
		ret.append(i)
	return ret

def limit_in_range2(lst, lower_limit, upper_limit):
	ret = limit_values_lower(lst, upper_limit)
	return limit_values_upper(ret, lower_limit)

## 3. Уровень 2:
##		make_groups		   - задается размер группы, список делится на списки со
##							 значениями, укладывающимися в этот размер
##		make_groups_dicts  - то же в общий словарь, ключ словаря - это кортеж с
##						     минимумом и максимумом группы
##		make_sorted_groups - группы в списке, отсортировать по количеству элементов

def generate_random_list(lst):
	for i in range(0, 10):
		lst.append(random.randrange(0, 100, 1))
if __name__=='__main__':
	lst = []
	generate_random_list(lst)
	print 'Initial list', lst
	lst = limit_in_range2(lst, 25, 75)
	print 'Limited values:', lst

