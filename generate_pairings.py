import json

root = 'Broad'

keywords1 = ['Cre recombinase', 'adipocyte', 'adipocyte stem cell', 'lineage tracing', 'mouse model']

authors1 = ['Elise Jeffery', 'Ryan Berry', 'Christopher D Church', 'Songtao Yu', 'Brett A Shook', 'Valerie Horsley', 'Evan D Rosen', 'Matthew S Rodeheffer']

keywords2 = ['T2D', 'dexamethasone', 'TNF', 'Jhdm2a', 'adipocyte', 'adipogenesis', 'BTBR']

authors2 = ['Sona Kang', 'Linus T. Tsai', 'Yiming Zhou', 'Adam Evertts', 'Su Xu', 'Michael J. Griffin', 'Robbyn Issner', 'Holly J. Whitton', 'Benjamin A. Garcia', 'Charles B. Epstein', 'Tarjei S. Mikkelsen', 'Evan D. Rosen']

keywords3 = ['Peroxisome', 'PPARG', 'LOF', 'T2D', 'P12A', 'NHLBI', 'preadipocytes', 'SGBS']

authors3 = ['Amit R. Majithia', 'Jason Flannick', 'Peter Shahinian', 'Michael Guo', 'Mark-Anthony Bray', 'Pierre Fontanillas', 'Stacey B. Gabriel', 'GoT2D Consortium', 'Evan D. Rosen', 'David Altshuler']

if __name__ == '__main__':
    output_list = zip(keywords1, authors1)
    output_list.extend(zip(keywords2, authors2))
    output_list.extend(zip(keywords3, authors3))

    output = open('outputpairs.txt', 'w')

    output.write(json.dumps(output_list))
