#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from client import Client
from shop import Shop 

shop = Shop()

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
    return int(category)

def format_array(list_product):
    format_dict = {}
    for index, product in enumerate(list_product):
        format_dict[index + 1] = product  
    return format_dict

# def choose_product 

def main():
    continu = True
    while continu:
        numNav = nav_question()
        print(numNav)
        if numNav == 2:
            ask_name()
            continu_buy_product = True
            while continu_buy_product:
                test = shop.get_products_by_category(product_category())
                format_array_product = format_array(test)
                print(format_array_product)
            # 'poid'
            # 'compare'
            # 'append dans client.order'
            # 'si fini'
            # ----------------------------------------
            # 'on recupere client.order', Client
            # 'addition de client.order' , Cleint
            # cree la classe ticket : , Ticket
            # classe Clent cree un list Ticket instancie, Ticket
            # 'creer un ticket + total + nom, prenom' , Client
            # 'bilan.append(ticket)'
            # 'retour dans nav_question'
main()