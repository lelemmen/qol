#!/usr/bin/env python3
# -*- coding: utf-8 -*-     # Om Nederlandse woorden te schrijven is utf-8 encodering nodig

import random
import argparse


# Parse de opgegeven argumenten
parser = argparse.ArgumentParser(description="Stel een trainingsprogramma op met functionele oefeningen.")
parser.add_argument('per_week', metavar='W', type=int, help="het aantal trainingen per week")  # nargs niet specifiëren zodat we geen lijst krijgen
parser.add_argument('per_dag_functioneel', metavar='F', type=int, help="het aantal functionele oefeningen per trainingsdag")
parser.add_argument('per_dag_stretches', metavar='S', type=int, help="het aantal stretches per trainingsdag")
parser.add_argument('focus', metavar='f', type=bool, help="ja/nee om een week lang dezelfde training te doen", nargs='?', default=False)
arguments = parser.parse_args()

per_dag_functioneel = arguments.per_dag_functioneel
per_dag_stretches = arguments.per_dag_stretches
aantal_trainingsdagen = arguments.per_week
focus = arguments.focus


# lijsten met functionele oefeningen en stretches
functionele_oefeningen = ['1.1', '1.2',
                          '2.2', '2.3', '2.4', '2.7', '2.8', '2.9', '2.10', '2.11', '2.12', '2.13', '2.14', '2.15', '2.16', '2.17', '2.18', '2.19', '2.20', '2.21', '2.22', '2.23',
                          '3.5', '3.6', '3.9',
                          '4.1', '4.2', '4.3', '4.4', '4.5', '4.6', '4.10', '4.11', '4.12']
stretches = ['1.3',
             '2.1', '2.5', '2.6',
             '3.1',
             '4.7', '4.8', '4.9']


# Bouw willekeurig een trainingsschema op
#   aantal_trainingsdagen keer per_dag_functioneel
training_functioneel = [random.sample(functionele_oefeningen, per_dag_functioneel) for i in range(0, aantal_trainingsdagen + 1)]
#   willekeurig voor of na de grote trainingen
voor_of_na_functioneel = ['voor' if random.choice([True, False]) else 'na' for i in range(0, aantal_trainingsdagen + 1)]
#  aantal_trainingsdagen keer per_dag_stretches
training_stretches = [random.sample(stretches, per_dag_stretches) for i in range(0, aantal_trainingsdagen + 1)]


# Geef de output van het programma aan de gebruiker
if focus:
    print("Je koos voor een week van {} trainingsdagen met de volgende training:".format(aantal_trainingsdagen))
    print("{} de hoofdtraining: \t {} {}".format(voor_of_na_functioneel[0], ' '.join(training_functioneel[0]), ' '.join(training_stretches[0])))
else:
    print("De training van deze week zal zijn:")
    for i in range(aantal_trainingsdagen):
        print("Dag {}, {} de hoofdtraining: \t {} {}".format(i + 1, voor_of_na_functioneel[i], ' '.join(training_functioneel[i]), ' '.join(training_stretches[i])))

