def calorific_value_volume(Q, C): #рассчёт объёмной теплотворной способности
    Qf = 0
    for i in range(max(len(Q), len(C)):
        Qf += Q[i]*C[i]
    return Qf

def calorific_value_mass_gas(Q, C, Mi, n): #рассчёт объёмной теплотворной способности через массу для газа
    Qf = 0; M = 0
    for i in range(max(len(Q), len(C), len(M)):
        M += C[i]/Mi[i] 
    for i in range(max(len(Q), len(C), len(M)):
        Qf += Q[i]*C[i]*M*n
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

def calorific_mass_value_gas(Q, C, Mi, n): #рассчёт массовой теплотворной способности через объём для газа
    Qf = 0; M = 0
    for i in range(max(len(Q), len(C), len(M)):
        M += C[i]*M[i] 
    for i in range(max(len(Q), len(C), len(M)):
        Qf += Q[i]*C[i]/M/n
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
    return A
