#!/usr/bin/python

import csv

csvfile = open('wordlist.csv', 'r')
rowreader = csv.reader(csvfile, delimiter='\t')
for row in rowreader:
    if len(row) == 0:
        continue
    if row[0][0] == '*':
        continue

    morph = row[3].split(' ')
    w = row[2]
    w = w.replace(' ', '_')

    out = w + ': '
    if (morph[0] == 'subst'):
        out += 'noun '
        if (len(morph) < 4):
            continue
        if ('ent' in morph):
            out += 'singular '
        elif ('fl' in morph):
            out += 'plural '

        if ('appell' in morph):
            out += 'common '
        elif ('prop' in morph):
            out += 'proper '

        if ('be' in morph):
            out += 'definite '
        elif ('ub' in morph):
            out += 'indefinite '

        print(out)
