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
    return 3
 
def ask_name():
    nom = input('Quel est votre nom ? ')
    prenom = input('Quel est votre prénom ? ')
    client = Client(prenom, nom)
    print(f"Bonjour {prenom} {nom}")
    return client

def product_category():
    category = input('Quelle catégorie de produit ? (1: Légume, 2: Fruit) : ')
    return int(category)

def print_panier(panier):
    print_line()
    print("Contenu du panier :")
    print_line()
    print(f"{'Produit':<20} | {'Unité(s)':<8} | {'Prix (€)':<8} | {'Client':<10}")
    print_line()

    for item in panier:
        print(f"{item['product']:<20} | "
              f"{item['unite']:<8} | "
              f"{item['prix']:<8.2f} | "
              f"{item['name']:<10}")

    print("-" * 50)
    
def print_ticket(panier):
    if not panier:
        print("Le panier est vide.")
        return

    client_name = panier[0]['name']
    total = sum(item['prix'] for item in panier)

    print("-" * 50)
    print(f"Ticket de caisse - Client : {client_name}")
    print("-" * 50)
    print(f"{'Produit':<20} | {'Qté':<5} | {'Prix (€)':<10}")
    print("-" * 50)

    for item in panier:
        print(f"{item['product']:<20} | "
              f"{item['unite']:<5} | "
              f"{item['prix']:<10.2f}")

    print("-" * 50)
    print(f"{'Total TTC':<20} | {'':<5} | {total:<10.2f}")
    print("-" * 50)
   

def format_array(list_product):
    format_dict = {}
    format_dict_clean = {}

    print_line()
    print("Détails des produits :")
    print_line()

    for index, product in enumerate(list_product):
        num = index + 1
        format_dict[num] = product
        format_dict_clean[num] = product['name']

        print(f"{num:>2} | {product['name']:<20} | Stock: {product['stock']:<8} | Prix: {product['prix']}")

    print_line()
    return format_dict_clean

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
        print(f'vous avez choisi {numNav}')
        
        if numNav == 1:
            print("Bilan des commandes :")
            shop.get_bilan()
            
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
                choix.append(choose_product_str)
                poid = choose_poid()
                print_line()
                print(f'Vous souhaitez {poid} kg/piece de {choose_product_str}')
                choix.append(poid)
                price = shop.buy_product(choix[0], choix[1])
                client.order.append({
                    'prix': price,
					'product': choix[0],
					'unite': choix[1],
					'name': client.firstname          
				})
                print_panier(client.order)
                choix = []

                continuer = input("Continuer les achats ? (o/n) : ")
                if continuer.lower() != 'o': 
                    continu_buy_product = False
                    shop.tickets.append(client.order.copy())
                    
                    print("Le client a payé voici son reçu")
                    print_ticket(client.order)
                    client = None 
        
        elif numNav == 3:  
            print("Fini")
            continu = False  
        
        else:
            print("Choix invalide, veuillez réessayer.")


main()	
