import pandas

def calorific_value_volume(Q, C): #рассчёт объёмной теплотворной способности
    Qf = 0
    for i in range(max(len(Q), len(C))):
        Qf += Q[i]*C[i]
    return Qf

def calorific_value_mass_gas(Q, C, Mi): #рассчёт объёмной теплотворной способности через массу для газа
    Qf = 0; M = 0
    for i in range(max(len(Q), len(C), len(Mi))):
        M += C[i]/Mi[i] 
    for i in range(max(len(Q), len(C), len(Mi))):
        Qf += Q[i]*C[i]*M*44.643
    return Qf

def calorific_value_mass_liquid(Q, C, p): #рассчёт объёмной теплотворной способности через массу для жидкости
    Qf = 0
    for i in range(max(len(Q), len(C), len(p))):
        Qf += Q[i]*C[i]*p[i]
    return Qf

def calorific_mass_value(Q, C): #рассчёт массовой теплотворной способности
    Qf = 0
    for i in range(max(len(Q), len(C))):
        Qf += Q[i]*C[i]
    return Qf

def calorific_mass_value_gas(Q, C, Mi): #рассчёт массовой теплотворной способности через объём для газа
    Qf = 0; M = 0
    for i in range(max(len(Q), len(C), len(Mi))):
        M += C[i]*Mi[i] 
    for i in range(max(len(Q), len(C), len(Mi))):
        Qf += Q[i]*C[i]/M/44.643
    return Qf

def calorific_mass_value_liquid(Q, C, p): #рассчёт массовой теплотворной способности через массу для жидкости
    Qf = 0
    for i in range(max(len(Q), len(C), len(p))):
        Qf += Q[i]*C[i]/p[i]
    return Qf

def stoichiometric_ratio(K, C, Mi): #рассчёт стехиометрического отношения
    A = 0
    M = 0
    for i in range(max(len(K), len(C))):
        A += K[i]*C[i]
    for i in range(max(len(Q), len(C), len(Mi))):
        M += C[i]*Mi[i] 
    Ma = 2*A*16 + 2*3.76*A*14
    L0 = Ma/M
    return L0

excel_data_df = pandas.read_excel('Ухтинское.xlsx', sheet_name='Ухтинское', usecols=['Состав(в %):',
                                                       'Теплота сгорания', 'Молярная масса', 'Доля кислорода'])
C = excel_data_df['Состав(в %):'].tolist()
Q = excel_data_df['Теплота сгорания'].tolist()
Mi = excel_data_df['Молярная масса'].tolist()
K = excel_data_df['Доля кислорода'].tolist()

j = 0
for i in range(len(Q)):
    if C[i-j] == '-':
        Q.pop(i-j)
        C.pop(i-j)
        Mi.pop(i-j)
        K.pop(i-j)
        j += 1

print(C)
print(Q)
print(Mi)
print(K)

# print whole sheet data
print(excel_data_df)
