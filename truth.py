#!/usr/bin/env python3
"""
truth_cyrillic.py - Analyse complète de mots cyrilliques
Affiche les conversions, propriétés mathématiques, hashs, etc.
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
    
    # Propriétés arithmétiques et algébriques
    results['english_words'] = number_to_english(nombre)
    results['parity'] = "Нечетное (Odd)" if nombre % 2 else "Четное (Even)"
    results['factors'] = factorize(nombre)
    results['prime_status'] = "Простое (Prime)" if is_prime(nombre) else "Составное (Composite)"
    results['divisible_by_8'] = [nombre * i for i in range(2, 10)]
    results['multiplied_by_2'] = nombre * 2
    results['divided_by_2'] = nombre / 2
    results['previous_primes'] = find_previous_primes(nombre, 8)
    results['digit_sum'] = sum(int(d) for d in str(nombre))
    results['digit_count'] = len(str(nombre))
    results['log10'] = math.log10(nombre) if nombre > 0 else float('inf')
    results['natural_log'] = math.log(nombre) if nombre > 0 else float('inf')
    results['fibonacci'] = is_fibonacci(nombre)
    results['next_number'] = nombre + 1
    results['previous_number'] = nombre - 1
    
    # Puissances et racines
    results['square'] = nombre ** 2
    results['cube'] = nombre ** 3
    results['square_root'] = math.sqrt(nombre) if nombre >= 0 else float('nan')
    results['cube_root'] = nombre ** (1/3)
    
    # Trigonométrie
    results['sin_deg'] = math.sin(math.radians(nombre))
    results['cos_deg'] = math.cos(math.radians(nombre))
    results['tan_deg'] = math.tan(math.radians(nombre))
    results['sin_rad'] = math.sin(nombre)
    results['cos_rad'] = math.cos(nombre)
    results['tan_rad'] = math.tan(nombre)
    results['deg_to_rad'] = math.radians(nombre)
    results['rad_to_deg'] = math.degrees(nombre)
    
    # Hash et cryptographie
    results['md5'] = hashlib.md5(str(nombre).encode()).hexdigest()
    results['crc32'] = crc32_hash(str(nombre))
    results['sha256'] = hashlib.sha256(str(nombre).encode()).hexdigest()
    results['sha1'] = hashlib.sha1(str(nombre).encode()).hexdigest()
    results['base64'] = base64.b64encode(str(nombre).encode()).decode()
    
    # Programmation
    results['c_hex'] = f"0x{results['hexadecimal']}"
    results['delphi_hex'] = f"${results['hexadecimal']}"
    
    # Date et temps (si c'est un timestamp UNIX raisonnable)
    results['unix_time'] = unix_to_datetime(nombre)
    
    # Internet
    results['ipv4'] = number_to_ipv4(nombre)
    
    # Couleur
    results['color_hex'] = f"#{results['hexadecimal'].zfill(6)}"
    results['rgb'] = hex_to_rgb(results['hexadecimal'])
    
    return results

def number_to_english(n):
    """Convertit un nombre en mots anglais"""
    if n == 0:
        return "ноль (zero)"
    
    units = ["", "один (one)", "два (two)", "три (three)", "четыре (four)", "пять (five)", "шесть (six)", "семь (seven)", "восемь (eight)", "девять (nine)"]
    teens = ["десять (ten)", "одиннадцать (eleven)", "двенадцать (twelve)", "тринадцать (thirteen)", "четырнадцать (fourteen)", "пятнадцать (fifteen)", "шестнадцать (sixteen)", "семнадцать (seventeen)", "восемнадцать (eighteen)", "девятнадцать (nineteen)"]
    tens = ["", "", "двадцать (twenty)", "тридцать (thirty)", "сорок (forty)", "пятьдесят (fifty)", "шестьдесят (sixty)", "семьдесят (seventy)", "восемьдесят (eighty)", "девяносто (ninety)"]
    thousands = ["", "тысяча (thousand)", "миллион (million)", "миллиард (billion)"]
    
    def convert_hundreds(num):
        if num == 0:
            return ""
        elif num < 10:
            return units[num]
        elif num < 20:
            return teens[num - 10]
        elif num < 100:
            return tens[num // 10] + (" " + units[num % 10] if num % 10 != 0 else "")
        else:
            return units[num // 100] + " сто (hundred)" + (" " + convert_hundreds(num % 100) if num % 100 != 0 else "")
    
    if n < 0:
        return "отрицательный (negative) " + number_to_english(-n)
    
    parts = []
    chunk_count = 0
    
    while n > 0:
        chunk = n % 1000
        if chunk != 0:
            part = convert_hundreds(chunk)
            if chunk_count > 0:
                part += " " + thousands[chunk_count]
            parts.append(part)
        n //= 1000
        chunk_count += 1
    
    return " ".join(reversed(parts))

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

def find_previous_primes(n, count):
    """Trouve les nombres premiers précédents"""
    primes = []
    candidate = n - 1
    while len(primes) < count and candidate > 1:
        if is_prime(candidate):
            primes.append(candidate)
        candidate -= 1
    return primes

def is_fibonacci(n):
    """Vérifie si un nombre est dans la suite de Fibonacci"""
    if n < 0:
        return False
    x = 5 * n * n
    return math.isqrt(x + 4) ** 2 == x + 4 or math.isqrt(x - 4) ** 2 == x - 4

def crc32_hash(data):
    """Calcule le CRC32"""
    crc32 = crcmod.predefined.Crc('crc-32')
    crc32.update(data.encode())
    return crc32.hexdigest()

def unix_to_datetime(timestamp):
    """Convertit un timestamp UNIX en datetime"""
    try:
        if 0 <= timestamp <= 2000000000:  # Timestamps UNIX raisonnables
            return datetime.fromtimestamp(timestamp).strftime('%A, %d %B %Y at %H:%M:%S UTC')
    except (ValueError, OSError):
        pass
    return "Неверная или вне диапазона метка времени (Invalid or out-of-range timestamp)"

def number_to_ipv4(n):
    """Convertit un nombre en IPv4"""
    if 0 <= n <= 0xFFFFFFFF:
        return f"{(n >> 24) & 0xFF}.{(n >> 16) & 0xFF}.{(n >> 8) & 0xFF}.{n & 0xFF}"
    return "Неверный IPv4 адрес (Invalid IPv4 address)"

def hex_to_rgb(hex_str):
    """Convertit une valeur hex en RGB"""
    hex_str = hex_str.zfill(6)
    try:
        r = int(hex_str[0:2], 16)
        g = int(hex_str[2:4], 16)
        b = int(hex_str[4:6], 16)
        return (r, g, b)
    except ValueError:
        return (0, 0, 0)

def afficher_table_cyrillique():
    """Affiche la table de correspondance cyrillique"""
    print("\n" + "="*60)
    print("ТАБЛИЦА СООТВЕТСТВИЯ КИРИЛЛИЦЫ")
    print("CYRILLIC CORRESPONDENCE TABLE")
    print("="*60)
    
    alphabet = list(ALPHABET_CYRILLIQUE.items())
    
    for i in range(0, len(alphabet), 5):
        ligne = alphabet[i:i+5]
        for lettre, num in ligne:
            print(f"{lettre}={num:2d}", end="  ")
        print()

def afficher_resultats(results):
    """Affiche les résultats de manière formatée"""
    print("="*80)
    print(f"ПОЛНЫЙ АНАЛИЗ КИРИЛЛИЧЕСКОГО СЛОВА: '{results['mot_original']}'")
    print(f"COMPLETE ANALYSIS OF CYRILLIC WORD: '{results['mot_original']}'")
    print("="*80)
    
    print("\nОБЩАЯ ИНФОРМАЦИЯ (General Information)")
    print(f"    Исходное слово : {results['mot_original']}")
    print(f"    В верхнем регистре : {results['mot_majuscules']}")
    print(f"    В нижнем регистре : {results['mot_minuscules']}")
    print(f"    Длина слова : {results['longueur_mot']} символов")
    print(f"    Палиндром : {'Да (Yes)' if results['est_palindrome'] else 'Нет (No)'}")
    
    print("\nЛИНГВИСТИЧЕСКИЙ АНАЛИЗ (Linguistic Analysis)")
    print(f"    Количество гласных : {results['nombre_voyelles']}")
    print(f"    Количество согласных : {results['nombre_consonnes']}")
    print(f"    Уникальные буквы : {results['lettres_uniques']}")
    
    print("\nКИРИЛЛИЧЕСКОЕ КОДИРОВАНИЕ (Cyrillic Encoding)")
    print(f"    Числовая последовательность : {results['sequence_cyrillique']}")
    print(f"    Декодированное слово (проверка) : {results['mot_decode']}")
    print(f"    Общая числовая стоимость : {results['valeur_numerique']}")
    
    print("\nЧИСЛОВОЙ АНАЛИЗ ОБЩЕЙ СТОИМОСТИ (Numeric Analysis of Total Value)")
    print(f"    Десятичное : {results['decimal']}")
    print(f"    Шестнадцатеричное : {results['hexadecimal']}")
    print(f"    Двоичное : {results['binary']}")
    print(f"    Восьмеричное : {results['octal']}")
    
    print(f"\n    Четность : {results['parity']}")
    print(f"    Факторы : {', '.join(map(str, results['factors']))}")
    print(f"    Простое или составное : {results['prime_status']}")
    print(f"    Числа, делящиеся на {results['decimal']} : {', '.join(map(str, results['divisible_by_8']))}")
    print(f"    Число {results['decimal']} умноженное на 2 :")
    print(f"        {results['multiplied_by_2']}")
    print(f"    Число {results['decimal']} деленное на 2 :")
    print(f"        {results['divided_by_2']}")
    print(f"    8 простых чисел перед числом :")
    print(f"        {', '.join(map(str, results['previous_primes']))}")
    print(f"    Сумма цифр : {results['digit_sum']}")
    print(f"    Количество цифр : {results['digit_count']}")
    print(f"    Десятичный логарифм для {results['decimal']} :")
    print(f"        {results['log10']}")
    print(f"    Натуральный логарифм для {results['decimal']} :")
    print(f"        {results['natural_log']}")
    print(f"    Число Фибоначчи? :")
    print(f"        {'Да (Yes)' if results['fibonacci'] else 'Нет (No)'}")
    print(f"    Следующее число после {results['decimal']} :")
    print(f"        {results['next_number']}")
    print(f"    Предыдущее число перед {results['decimal']} :")
    print(f"        {results['previous_number']}")
    
    print("\nСТЕПЕНИ, КОРНИ (Powers, Roots)")
    print(f"    {results['decimal']} во второй степени :")
    print(f"        {results['square']}")
    print(f"    {results['decimal']} в третьей степени :")
    print(f"        {results['cube']}")
    print(f"    Квадратный корень из {results['decimal']} :")
    print(f"        {results['square_root']}")
    print(f"    Кубический корень из {results['decimal']} :")
    print(f"        {results['cube_root']}")
    
    print("\nТРИГОНОМЕТРИЧЕСКИЕ ФУНКЦИИ (Trigonometric Functions)")
    print(f"    синус, sin {results['decimal']} градусов, sin {results['decimal']}° :")
    print(f"        {results['sin_deg']:.10f}")
    print(f"    косинус, cos {results['decimal']} градусов, cos {results['decimal']}° :")
    print(f"        {results['cos_deg']:.10f}")
    print(f"    тангенс, tg {results['decimal']} градусов, tg {results['decimal']}° :")
    print(f"        {results['tan_deg']:.10f}")
    
    print("\nХЕШИ, КРИПТОГРАФИЯ (Hashes, Cryptography)")
    print(f"    MD5 : {results['md5']}")
    print(f"    CRC-32 : {results['crc32']}")
    print(f"    SHA-256 : {results['sha256']}")
    print(f"    Base64 : {results['base64']}")
    
    print("\nПРОГРАММИРОВАНИЕ (Programming)")
    print(f"    C++ : {results['c_hex']}")
    print(f"    Delphi : {results['delphi_hex']}")
    
    print("\nИНТЕРНЕТ (Internet)")
    print(f"    IPv4 : {results['ipv4']}")
    
    print("\nЦВЕТ (Color)")
    print(f"    HEX цвет : {results['color_hex']}")
    print(f"    RGB : {results['rgb']}")
    
    # Affichage détaillé de l'encodage
    print("\nПОДРОБНОСТИ КОДИРОВАНИЯ (Encoding Details)")
    mot = results['mot_original'].upper()
    for i, lettre in enumerate(mot):
        if lettre in ALPHABET_CYRILLIQUE:
            code = ALPHABET_CYRILLIQUE[lettre]
            print(f"    {i+1:2d}. {lettre} = {code:2d}")
        elif lettre.isalpha():
            code = ord(lettre) - ord('A') + 1
            print(f"    {i+1:2d}. {lettre} (латинский/latin) = {code:2d}")

def main():
    if len(sys.argv) != 2:
        print("Использование: python truth_cyrillic.py <кириллическое_слово>")
        print("Usage: python truth_cyrillic.py <cyrillic_word>")
        print("Пример: python truth_cyrillic.py ПРИВЕТ")
        print("Пример: python truth_cyrillic.py \"17.18.10.3.6.20\" (для декодирования)")
        sys.exit(1)
    
    entree = sys.argv[1].strip()
    
    try:
        # Vérifier si c'est une séquence numérique
        if '.' in entree and all(part.isdigit() for part in entree.split('.')):
            mot_decode = decoder_sequence_cyrillique(entree)
            print(f"🔓 Декодированная последовательность : {entree} → {mot_decode}")
            results = analyser_mot_cyrillique(mot_decode)
        else:
            results = analyser_mot_cyrillique(entree)
        
        afficher_resultats(results)
        afficher_table_cyrillique()
        
    except Exception as e:
        print(f"❌ Ошибка (Error) : {e}")
        sys.exit(1)

def interface_interactive():
    """
    Interface interactive pour analyser plusieurs mots
    """
    print("=== Полный анализатор кириллических слов ===")
    print("Complete Cyrillic Word Analyzer")
    print("Лингвистический анализ, кодирование, математические свойства, хеши")
    print("Linguistic analysis, encoding, mathematical properties, hashes")
    print("\nКоманды (Commands):")
    print("  - Введите кириллическое слово для анализа")
    print("  - Введите числовую последовательность для декодирования и анализа")
    print("  - 'table' для показа таблицы соответствия")
    print("  - 'quit' для выхода")
    print("-" * 70)
    
    while True:
        try:
            entree = input("\nВведите слово или последовательность : ").strip()
            
            if entree.lower() == 'quit':
                print("До свидания! (Goodbye!)")
                break
            elif entree.lower() == 'table':
                afficher_table_cyrillique()
                continue
            
            if not entree:
                continue
            
            # Analyser l'entrée
            if '.' in entree and all(part.isdigit() for part in entree.split('.')):
                mot_decode = decoder_sequence_cyrillique(entree)
                print(f"🔓 Декодированная последовательность : {entree} → {mot_decode}")
                results = analyser_mot_cyrillique(mot_decode)
            else:
                results = analyser_mot_cyrillique(entree)
            
            # Afficher un résumé
            print(f"\n📊 РЕЗЮМЕ ДЛЯ '{results['mot_original']}':")
            print(f"   Последовательность: {results['sequence_cyrillique']}")
            print(f"   Общая стоимость: {results['valeur_numerique']}")
            print(f"   Длина: {results['longueur_mot']} символов")
            print(f"   Палиндром: {'Да (Yes)' if results['est_palindrome'] else 'Нет (No)'}")
            print(f"   MD5: {results['md5'][:16]}...")
            
            voir_complet = input("\nПоказать полный анализ? (д/н): ").strip().lower()
            if voir_complet in ['д', 'да', 'y', 'yes']:
                afficher_resultats(results)
                
        except KeyboardInterrupt:
            print("\n\nДо свидания! (Goodbye!)")
            break
        except Exception as e:
            print(f"❌ Ошибка (Error) : {e}")

if __name__ == "__main__":
    if len(sys.argv) == 1:
        # Mode interactif
        interface_interactive()
    else:
        # Mode ligne de commande
        main()
