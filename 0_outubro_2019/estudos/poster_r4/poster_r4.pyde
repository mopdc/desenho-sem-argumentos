"""
Poster desenho() #0_outubro_2019
https://desenho.lugaralgum.com (para licenças, créditos e agradecimentos!)
"""

from __future__ import division
from random import choice, seed
from elementos import casinha, estrela, olho, grade
add_library('pdf')

def setup():
    global s
    size(1122, 1122) 
    s = random_seed(191020) # use random_seed() para sortear uma seed!
    noLoop()

def draw():
    background(255)
    beginRecord(PDF, 'poster_seed{}.pdf'.format(s))
    rectMode(CENTER)
    strokeJoin(ROUND)
    poster(width / 2., height / 2., 6, width - 70)
    endRecord()

def poster(xo, yo, divisoes, dim_total, elemento=None):
    """
    Faça desenho do poster usando subdivisões recursivas.
    """
    dim = dim_total / divisoes   # dimensão de célula da grade
    offset = (dim - dim_total) / 2
    for i in range(divisoes):
        x = xo + offset + dim * i
        for j in range(divisoes):
            y = yo + offset + dim * j
            sel_elemento = choice((0, 1, 2, 3, 4))
            if elemento is not None:  # elemento grade regular
                desenha_elemento(x, y, dim, elemento)
            elif dim > 20 and random(10) < 8:  # subdivisão
                poster(x, y, 3, dim)  # com a função poster!
            elif 20 > dim > 15 and random(10) < 8:  # também 
                # +3 não permite estrela e casas preenchidas
                poster(x, y, 3, dim * 2, sel_elemento + 3) 
            else:  # faz um elemento "sozinho"
                desenha_elemento(x, y, dim, sel_elemento)
    if divisoes == 6:  # uma vez só, na maior grade apenas
        w_olho = dim_total / 18  # dimensão do quadrado olho
        x_olho = random(w_olho, dim_total / 2)
        y_olho = random(dim_total / 2, dim_total - w_olho)
        fill(0)
        square(x_olho, y_olho, w_olho)
        olho(x_olho, y_olho, w_olho * .9)

def desenha_elemento(x, y, w, seletor):
    """
    Posicione, ajuste atributos e selecione
    elementos de desenho, invocando as funções
    como definidas no verso do pôster:
    estrela(), casinha() 
    """ 
    stroke(0)
    strokeWeight(.5)
    if seletor == 0:  # estrela em preto
        fill(0)
        num_pontas = choice((5, 7, 9))
        ra = w * .35
        rb = choice((w * .25, w * .15, w * .075))
        estrela(x, y, num_pontas, ra, rb)
    elif seletor == 1:  # casinha branca
        fill(255)
        casinha(x, y, w)
    elif seletor == 2:  # casinha preta
        fill(0) 
        casinha(x, y, w)
    elif 3 <= seletor < 5: 
        noFill()  # casinha sem preenchimento
        casinha(x, y, w)
    else: # seletor 5 ou maior
        pass  # não desenha nada!

def keyPressed():
    redraw()
    print(random_seed())

def random_seed(s=None):
    if s is None:
        s = int(random(100000))
    randomSeed(s)  # Processing random seed setup
    seed(s)  # Python random seed setup
    return s
