#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Client:
	def __init__(self, firstname : str, lastname: str) :
		self.firstname = firstname
		self.lastname = lastname
		self.order = []

	def get_total_order(self) :

		total_order = 0
		for item in self.order :
			total_order += item.prix
		return total_order