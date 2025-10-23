#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from client import Client

def nav_question():
    result = input("Bilan ou Achetez ou Stoppez(1 ou 2 ou 3)" )
    if result.isdigit() and result != '3':
        res = int(result)
        return res 
    return False
 
def ask_name():
    nom = input('quel est votre nom')
    prenom = input('quel est votre prenom')
    Client(nom, prenom)

# def main():
#     while True
#     ask_name()