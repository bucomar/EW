import math as m

def q_ww(k, du):
    ''' SW | Q_ww [l/s] = k * SQRT(DU) '''
    qww = k*m.sqrt(du)
    return qww


def q_tot(q_ww, q_c, q_p):
    ''' SW | Q_tot [l/s] = Q_ww + Q_C + Q_P '''
    q_tot = q_ww + q_c + q_p
    return p_tot


def c_e(q_r, a_u):
    ''' RW | C_e Endabflussbeiwert = Q_r / A_U '''
    c_e = q_r / a_u
    return c_e

def a_u(a_e, c_m):
    '''  RW | A_U [m2] Angeschlossene undurchlässige Fläche = A_E * C_m '''
    a_u = a_e * c_m
    return a_u

def q_r():
    ''' RW | Q_r [l/s] = r_DT * C_m * A_U * 1 / 10000 '''
    a_u = a_e * c_m
    return a_u


