#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from client import Client
from shop import Shop 

shop = Shop()

def print_line():
    print('-' * 80)

def nav_question():
    result = input("Bilan ou Achetez ou Stoppez(1 ou 2 ou 3) : ")
    if result.isdigit() and result != '3':
        res = int(result)
        return res
    return False
 
def ask_name():
    nom = input('Quel est votre nom ? ')
    prenom = input('Quel est votre prénom ? ')
    client = Client(prenom, nom)
    print(f"Bonjour {prenom} {nom}")
    return client

def product_category():
    category = input('Quelle catégorie de produit ? (1: Légume, 2: Fruit) : ')
    print(category)
    return int(category)

def format_array(list_product):
    format_dict = {}
    for index, product in enumerate(list_product):
        format_dict[index + 1] = product
    print_line()
    print(format_dict)
    print_line()
    return format_dict

def choose_product(array_product): 
    number = int(input(f'Choisir entre 1 et {len(array_product)} : '))
    return number

def choose_poid():
    number = int(input('Choisir poids ou pièce : '))
    return number

def main():
    continu = True
    client = None
    
    while continu:
        numNav = nav_question()
        print(numNav)
        
        if numNav == 1:
            print("Bilan des commandes :")
            for i, ticket in enumerate(shop.tickets, 1):
                print(f"Commande n°{i}: {ticket}")
                       
        elif numNav == 2:
            if client is None:
                client = ask_name()
            
            continu_buy_product = True
            while continu_buy_product:
                choix = []
                product_categories = shop.get_products_by_category(product_category())
                format_array_product = format_array(product_categories)
                number_choose_product = choose_product(format_array_product)
                choose_product_str = format_array_product[number_choose_product]
                print(choose_product_str)
                choix.append(choose_product_str)
                poid = choose_poid()
                print(poid)
                choix.append(poid)
                print(choix)
                test = shop.buy_product(choix[0], choix[1])
                print(test)
                client.order.append({'prix': test, 'product': choix[0], 'unite': choix[1], 'name': client.firstname})
                print('client order')
                print(client.order)

                choix = []

                continuer = input("Continuer les achats ? (o/n) : ")
                if continuer.lower() != 'o': 
                    continu_buy_product = False
                    shop.tickets.append(client.order.copy())
                    print("Commande enregistrée !")
                    print(shop.tickets)
                    client = None 

main()
