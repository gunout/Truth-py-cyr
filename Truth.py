#!/usr/bin/env python3
"""
truth_cyrillic.py - Analyse complète d'un mot cyrillique
Affiche les conversions, propriétés mathématiques, hashs, etc. pour un texte cyrillique
"""

import math
import hashlib
import crcmod
import base64
from datetime import datetime
import sys

# Alphabet cyrillique complet
ALPHABET_CYRILLIQUE = {
    'А': 1, 'Б': 2, 'В': 3, 'Г': 4, 'Д': 5, 'Е': 6, 'Ё': 7, 'Ж': 8, 'З': 9, 'И': 10,
    'Й': 11, 'К': 12, 'Л': 13, 'М': 14, 'Н': 15, 'О': 16, 'П': 17, 'Р': 18, 'С': 19, 'Т': 20,
    'У': 21, 'Ф': 22, 'Х': 23, 'Ц': 24, 'Ч': 25, 'Ш': 26, 'Щ': 27, 'Ъ': 28, 'Ы': 29, 'Ь': 30,
    'Э': 31, 'Ю': 32, 'Я': 33
}

ALPHABET_INVERSE = {v: k for k, v in ALPHABET_CYRILLIQUE.items()}

def encoder_mot_cyrillique(mot):
    """
    Encode un mot cyrillique en séquence numérique
    """
    mot = mot.upper().strip()
    resultat = []
    
    for lettre in mot:
        if lettre in ALPHABET_CYRILLIQUE:
            numero = ALPHABET_CYRILLIQUE[lettre]
            resultat.append(str(numero))
        elif lettre.isalpha():
            # Si c'est une lettre latine
            numero = ord(lettre) - ord('A') + 1
            resultat.append(str(numero))
    
    return '.'.join(resultat)

def decoder_sequence_cyrillique(sequence):
    """
    Décode une séquence numérique en mot cyrillique
    """
    nombres = sequence.split('.')
    mot_decode = []
    
    for nombre in nombres:
        if nombre.isdigit():
            numero = int(nombre)
            if 1 <= numero <= 33:
                lettre = ALPHABET_INVERSE[numero]
                mot_decode.append(lettre)
            elif 1 <= numero <= 26:
                # Lettre latine
                lettre = chr(numero + ord('A') - 1)
                mot_decode.append(lettre)
    
    return ''.join(mot_decode)

def mot_vers_nombre(mot):
    """
    Convertit un mot cyrillique en un nombre unique (somme des codes)
    """
    mot = mot.upper().strip()
    total = 0
    
    for lettre in mot:
        if lettre in ALPHABET_CYRILLIQUE:
            total += ALPHABET_CYRILLIQUE[lettre]
    
    return total

def sequence_vers_nombre(sequence):
    """
    Convertit une séquence numérique en un nombre unique (somme)
    """
    nombres = sequence.split('.')
    total = 0
    
    for nombre in nombres:
        if nombre.isdigit():
            total += int(nombre)
    
    return total

def analyser_mot_cyrillique(mot):
    """
    Analyse complète d'un mot cyrillique
    """
    results = {}
    
    # Informations de base
    results['mot_original'] = mot
    results['mot_majuscules'] = mot.upper()
    results['mot_minuscules'] = mot.lower()
    results['longueur_mot'] = len(mot)
    
    # Encodage cyrillique
    results['sequence_cyrillique'] = encoder_mot_cyrillique(mot)
    results['valeur_numerique'] = mot_vers_nombre(mot)
    
    # Décodage (pour vérification)
    results['mot_decode'] = decoder_sequence_cyrillique(results['sequence_cyrillique'])
    
    # Propriétés du texte
    results['est_palindrome'] = est_palindrome(mot)
    results['nombre_voyelles'] = compter_voyelles_cyrilliques(mot)
    results['nombre_consonnes'] = compter_consonnes_cyrilliques(mot)
    results['lettres_uniques'] = lettres_uniques(mot)
    
    # Analyse numérique basée sur la valeur totale
    nombre = results['valeur_numerique']
    results.update(analyser_nombre(nombre))
    
    return results

def analyser_nombre(nombre):
    """
    Analyse complète d'un nombre (adaptée de truth.py)
    """
    results = {}
    
    # Conversion de base
    results['decimal'] = nombre
    results['hexadecimal'] = hex(nombre)[2:].upper()
    results['binary'] = bin(nombre)[2:]
    results['octal'] = oct(nombre)[2:]
    
    # Propriétés mathématiques
    results['parity'] = "Odd" if nombre % 2 else "Even"
    results['factors'] = factorize(nombre)
    results['prime_status'] = "Prime" if is_prime(nombre) else "Composite"
    results['digit_sum'] = sum(int(d) for d in str(nombre))
    results['digit_count'] = len(str(nombre))
    results['square'] = nombre ** 2
    results['cube'] = nombre ** 3
    results['square_root'] = math.sqrt(nombre) if nombre >= 0 else float('nan')
    
    # Hash et cryptographie
    results['md5'] = hashlib.md5(str(nombre).encode()).hexdigest()
    results['sha256'] = hashlib.sha256(str(nombre).encode()).hexdigest()
    results['base64'] = base64.b64encode(str(nombre).encode()).decode()
    
    return results

def est_palindrome(mot):
    """Vérifie si le mot est un palindrome"""
    mot = mot.upper().replace(' ', '')
    return mot == mot[::-1]

def compter_voyelles_cyrilliques(mot):
    """Compte les voyelles cyrilliques"""
    voyelles = 'АЕЁИОУЫЭЮЯ'
    mot = mot.upper()
    return sum(1 for lettre in mot if lettre in voyelles)

def compter_consonnes_cyrilliques(mot):
    """Compte les consonnes cyrilliques"""
    consonnes = 'БВГДЖЗЙКЛМНПРСТФХЦЧШЩ'
    mot = mot.upper()
    return sum(1 for lettre in mot if lettre in consonnes)

def lettres_uniques(mot):
    """Retourne les lettres uniques du mot"""
    return ''.join(sorted(set(mot.upper())))

def factorize(n):
    """Factorise un nombre"""
    if n < 2:
        return [n]
    
    factors = []
    d = 2
    while d * d <= n:
        while n % d == 0:
            factors.append(d)
            n //= d
        d += 1
    if n > 1:
        factors.append(n)
    return factors

def is_prime(n):
    """Vérifie si un nombre est premier"""
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

def afficher_table_cyrillique():
    """Affiche la table de correspondance cyrillique"""
    print("\n" + "="*60)
    print("TABLE DE CORRESPONDANCE ALPHABET CYRILLIQUE")
    print("="*60)
    
    alphabet = list(ALPHABET_CYRILLIQUE.items())
    
    for i in range(0, len(alphabet), 6):
        ligne = alphabet[i:i+6]
        for lettre, num in ligne:
            print(f"{lettre}={num:2d}", end="  ")
        print()

def afficher_resultats(results):
    """Affiche les résultats de manière formatée"""
    print("="*80)
    print(f"ANALYSE COMPLÈTE DU MOT CYRILLIQUE: '{results['mot_original']}'")
    print("="*80)
    
    print("\nINFORMATIONS GÉNÉRALES")
    print(f"    Mot original : {results['mot_original']}")
    print(f"    En majuscules : {results['mot_majuscules']}")
    print(f"    En minuscules : {results['mot_minuscules']}")
    print(f"    Longueur du mot : {results['longueur_mot']} caractères")
    print(f"    Est un palindrome : {'Oui' if results['est_palindrome'] else 'Non'}")
    
    print("\nANALYSE LINGUISTIQUE")
    print(f"    Nombre de voyelles : {results['nombre_voyelles']}")
    print(f"    Nombre de consonnes : {results['nombre_consonnes']}")
    print(f"    Lettres uniques : {results['lettres_uniques']}")
    
    print("\nENCODAGE CYRILLIQUE")
    print(f"    Séquence numérique : {results['sequence_cyrillique']}")
    print(f"    Mot décodé (vérification) : {results['mot_decode']}")
    print(f"    Valeur numérique totale : {results['valeur_numerique']}")
    
    print("\nANALYSE NUMÉRIQUE DE LA VALEUR TOTALE")
    print(f"    Décimal : {results['decimal']}")
    print(f"    Hexadécimal : {results['hexadecimal']}")
    print(f"    Binaire : {results['binary']}")
    print(f"    Octal : {results['octal']}")
    
    print(f"\n    Parité : {results['parity']}")
    print(f"    Facteurs : {', '.join(map(str, results['factors']))}")
    print(f"    Premier ou composé : {results['prime_status']}")
    print(f"    Somme des chiffres : {results['digit_sum']}")
    print(f"    Nombre de chiffres : {results['digit_count']}")
    
    print(f"\n    Carré : {results['square']}")
    print(f"    Cube : {results['cube']}")
    print(f"    Racine carrée : {results['square_root']:.4f}")
    
    print("\nHASH ET CRYPTOGRAPHIE")
    print(f"    MD5 : {results['md5']}")
    print(f"    SHA-256 : {results['sha256']}")
    print(f"    Base64 : {results['base64']}")
    
    # Affichage détaillé de l'encodage
    print("\nDÉTAIL DE L'ENCODAGE LETTRE PAR LETTRE")
    mot = results['mot_original'].upper()
    for i, lettre in enumerate(mot):
        if lettre in ALPHABET_CYRILLIQUE:
            code = ALPHABET_CYRILLIQUE[lettre]
            print(f"    {i+1:2d}. {lettre} = {code:2d}")
        elif lettre.isalpha():
            code = ord(lettre) - ord('A') + 1
            print(f"    {i+1:2d}. {lettre} (latin) = {code:2d}")
        else:
            print(f"    {i+1:2d}. {lettre} (autre)")

def main():
    if len(sys.argv) != 2:
        print("Usage: python truth_cyrillic.py <mot_cyrillique>")
        print("Exemple: python truth_cyrillic.py ПРИВЕТ")
        print("Exemple: python truth_cyrillic.py \"16.1.25.19\" (pour décoder)")
        sys.exit(1)
    
    entree = sys.argv[1].strip()
    
    try:
        # Vérifier si c'est une séquence numérique
        if '.' in entree and all(part.isdigit() for part in entree.split('.')):
            # C'est une séquence à décoder et analyser
            mot_decode = decoder_sequence_cyrillique(entree)
            print(f"🔓 Séquence décodée : {entree} → {mot_decode}")
            results = analyser_mot_cyrillique(mot_decode)
        else:
            # C'est un texte à analyser
            results = analyser_mot_cyrillique(entree)
        
        afficher_resultats(results)
        
        # Afficher la table de correspondance à la fin
        afficher_table_cyrillique()
        
    except Exception as e:
        print(f"❌ Erreur : {e}")
        sys.exit(1)

def interface_interactive():
    """
    Interface interactive pour analyser plusieurs mots
    """
    print("=== Analyseur Complet de Mots Cyrilliques ===")
    print("Analyse linguistique, encodage, propriétés mathématiques, hashs")
    print("\nCommandes:")
    print("  - Entrez un mot cyrillique pour l'analyser")
    print("  - Entrez une séquence numérique pour la décoder et l'analyser")
    print("  - 'table' pour afficher la table de correspondance")
    print("  - 'quit' pour quitter")
    print("-" * 60)
    
    while True:
        try:
            entree = input("\nEntrez un mot ou une séquence : ").strip()
            
            if entree.lower() == 'quit':
                print("До свидания! (Au revoir !)")
                break
            elif entree.lower() == 'table':
                afficher_table_cyrillique()
                continue
            
            if not entree:
                continue
            
            # Analyser l'entrée
            if '.' in entree and all(part.isdigit() for part in entree.split('.')):
                mot_decode = decoder_sequence_cyrillique(entree)
                print(f"🔓 Séquence décodée : {entree} → {mot_decode}")
                results = analyser_mot_cyrillique(mot_decode)
            else:
                results = analyser_mot_cyrillique(entree)
            
            # Afficher un résumé
            print(f"\n📊 RÉSUMÉ POUR '{results['mot_original']}':")
            print(f"   Séquence: {results['sequence_cyrillique']}")
            print(f"   Valeur totale: {results['valeur_numerique']}")
            print(f"   Longueur: {results['longueur_mot']} caractères")
            print(f"   Palindrome: {'Oui' if results['est_palindrome'] else 'Non'}")
            print(f"   MD5: {results['md5'][:16]}...")
            
            voir_complet = input("\nVoir l'analyse complète? (o/n): ").strip().lower()
            if voir_complet in ['o', 'oui', 'y', 'yes']:
                afficher_resultats(results)
                
        except KeyboardInterrupt:
            print("\n\nДо свидания! (Au revoir !)")
            break
        except Exception as e:
            print(f"❌ Erreur : {e}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Mode interactif
        interface_interactive()
    else:
        # Mode ligne de commande
        main()
