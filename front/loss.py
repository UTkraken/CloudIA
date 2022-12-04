from collections import Counter
import os

from cloudIA import settings


def selector(interrest, caractere, working_place, filiere):
    if caractere == 'sportif':
        caractere = ['aventure', 'logistique', 'decouverte']
    if caractere == 'altruiste':
        caractere = ['rencontre', 'aventure', 'tech']
    if caractere == 'cerebral':
        caractere = ['decouverte', 'logistique', 'tech']
    if caractere == 'organisateur':
        caractere = ['logistique', 'decouverte', 'animaux']
    if caractere == 'curieux':
        caractere = ['decouverte', 'aventure', 'tech']
    if caractere == 'amoureuxdelanature':
        caractere = ['agriculture', 'animaux', 'construction']

    if working_place == 'bateau':
        working_place = ['aventure', 'rencontre', 'animaux', 'tech', 'construction', 'decouverte']
    if working_place == 'port':
        working_place = ['logistique', 'tech', 'construction']
    if working_place == 'bureau':
        working_place = ['logistique', 'tech', 'animaux', 'decouverte', 'construction']
    if working_place == 'exploitation':
        working_place = ['logistique', 'agricole', 'animaux']

    if filiere == 'logistique':
        filiere = ['logistique', 'aventure', 'construction', 'rencontre']
    if filiere == 'portuaire':
        filiere = ['logistique', 'aventure', 'construction']
    if filiere == 'navale':
        filiere = ['logistique', 'tech', 'construction', 'rencontre', 'decouverte']
    if filiere == 'marchand':
        filiere = ['logistique', 'aventure', 'tech']
    if filiere == 'maintenance':
        filiere = ['tech', 'logistique', 'construction']
    if filiere == 'securite':
        filiere = ['aventure', 'tech', 'decouverte']
    if filiere == 'tech':
        filiere = ['tech', 'decouverte', 'animaux']

    # interrest = [interrest]
    print(interrest)
    print(caractere)
    print(working_place)
    print(filiere)
    result = interrest + caractere + working_place + filiere

    print(result)
    result.sort()

    print(result)
    final = Counter(result)

    return final

