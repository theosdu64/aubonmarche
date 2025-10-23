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
    print((nom, prenom))

def product_category():
    category = input('quel category de produit ? (1 : Legume, 2: Fruit)')
    print(category)

def main():
    continu = True
    while continu:
        numNav = nav_question()
        print(numNav)
        if numNav == 2:
            ask_name()
            product_category()

main()