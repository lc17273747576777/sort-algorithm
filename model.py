import math
# import numpy as np

def M_sort(Ain, Bin):
    L = len(Ain)
    Cout = [0]*2 * L
    i, j = 0, 0
    for n in range(0, 2*L):
        if i >= L:
            Cout[n] = Bin[j]
            j += 1
        elif j >= L:
            Cout[n] = Ain[i]
            i += 1
        elif Ain[i] <= Bin[j]:
            Cout[n] = Ain[i]
            i += 1
        elif Ain[i] > Bin[j]:
            Cout[n] = Bin[j]
            j += 1
    return Cout

def compensate(Din):
    Ld = len(Din)
    K = int(math.pow(2,math.ceil(math.log2(Ld))))
    num_compensate = K-Ld
    # comp=np.zeros(num_compensate)
    # Dout=np.array(Din)
    Dout = [0]*K
    for d in range(0, K):
        if d < Ld:
            Dout[d] = Din[d]
        else:
            Dout[d] = 0
    return Dout, num_compensate

def sort_single(Ein):
    Le = len(Ein)
    Le_half = int(Le / 2)
    A_Ein = [0] * Le_half
    B_Ein = [0] * Le_half
    for i in range(0, Le_half):
        A_Ein[i] = Ein[i]
        B_Ein[i] = Ein[i + Le_half]

    if Le==2 or Le==1:
        return M_sort(A_Ein, B_Ein)
    else:
        return M_sort(sort_single(A_Ein), sort_single(B_Ein))

def sort_process(Fin):
    if len(Fin)==1:
        return Fin
    F, comF = compensate(Fin)

    Fout = sort_single(F)
    if comF!=0:
        Fend = [0] * (len(Fout)-comF)
        for ii in range(0, len(Fout)-1):
            Fend[ii] = Fout[ii+comF]
    else:
        Fend=Fout
    return Fend


G1=[12,3,4,11,22,51,23]
Gout = sort_process(G1)
print(Gout)
G2=[12,3,4,5,6,7,3]
Gout = sort_process(G2)
print(Gout)
G3=[16,23,32,56,34,42,12,95,32,235,46,234,73,42,90,61]
Gout = sort_process(G3)
print(Gout)
G4=[12,3]
Gout = sort_process(G4)
print(Gout)
G5=[1]
Gout = sort_process(G5)
print(Gout)