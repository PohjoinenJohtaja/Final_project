def calorific_value_volume(Q, C): #рассчёт объёмной теплотворной способности
    Qf = 0
    for i in range(max(len(Q), len(C)):
        Qf += Q[i]*C[i]
    return Qf

def calorific_value_mass_gas(Q, C, Mi): #рассчёт объёмной теплотворной способности через массу для газа
    Qf = 0; M = 0
    for i in range(max(len(Q), len(C), len(M)):
        M += C[i]/Mi[i] 
    for i in range(max(len(Q), len(C), len(M)):
        Qf += Q[i]*C[i]*M*44.643
    return Qf

def calorific_value_mass_liquid(Q, C, p): #рассчёт объёмной теплотворной способности через массу для жидкости
    Qf = 0
    for i in range(max(len(Q), len(C), len(p)):
        Qf += Q[i]*C[i]*p[i]
    return Qf

def calorific_mass_value(Q, C): #рассчёт массовой теплотворной способности
    Qf = 0
    for i in range(max(len(Q), len(C)):
        Qf += Q[i]*C[i]
    return Qf

def calorific_mass_value_gas(Q, C, Mi): #рассчёт массовой теплотворной способности через объём для газа
    Qf = 0; M = 0
    for i in range(max(len(Q), len(C), len(M)):
        M += C[i]*M[i] 
    for i in range(max(len(Q), len(C), len(M)):
        Qf += Q[i]*C[i]/M/44.643
    return Qf

def calorific_mass_value_liquid(Q, C, p): #рассчёт массовой теплотворной способности через массу для жидкости
    Qf = 0
    for i in range(max(len(Q), len(C), len(p)):
        Qf += Q[i]*C[i]/p[i]
    return Qf

def stoichiometric_ratio(K, C): #рассчёт стехиометрического отношения
    A = 0
    for i in range(max(len(K), len(C)):
        A += K[i]*C[i]
    Ma = 2*A*16 + 2*3.76*A*14
    L0 = Ma/M #M not declared
    return L0

Molar_mass = {'CH4':16.04, 'C2H6':30.07, 'C3H8':44.10, 'C4H10':58.12, 'C5H12':72.15}
Oxigen_ratio = {'CH4':2, 'C2H6':3.5, 'C3H8':5, 'C4H10':6.5, 'C5H12':8}

