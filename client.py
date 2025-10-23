#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Client:
	def __init__(self, firstname : str, lastname: str) :
		self.firstname = firstname
		self.lastname = lastname
		self.order = []