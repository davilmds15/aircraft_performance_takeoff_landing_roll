import numpy as np

def ISA(H,DT):
    g0 = 9.80665
    R = 287.053
    gama = 1.4
    mu0 = 1.7894e-5
    
    HB = np.array([0,11000,20000,32000,47000])
    HT = np.array([11000,20000,32000,47000,50000])
    A = np.array([-0.0065,0,0.001,0.0028,0])
    TB = np.array([288.15,216.78,216.66,228.65,270.65])
    
    PB = np.array([101325,22700,5529,868.014,110.906])
    
    
    # a velocidade diminui no gráfico pq o calculo de equilibrio seja ele analitico ou generico
    # é feito para certo rho, mas a medida q o aviao cai o rho aumenta e o calculo de equilibrio 
    # so vale para t = 0, para outro cl teria q calulcar novamente, isso acontece pq o cl é constanta
    # e deveria ser compensado em função da altitude, como isso é dificil, o cl é compensado em função do 
    # gama, mas a velocidade ainda pode apresentar variação
    # a vel e o angulo de tranjetoria variam pq o equilibrio é feito para só t=0, para que fosse diferente 
    # teria q praticar o controle em malha fechada realimentanto o gama, porém é mt difícil
    
    tb = np.empty((5))
    tb = TB + DT
    pb = np.empty((5))
    pb[0] = PB[0]
    pb[1] = PB[0] * (TB[1] / TB[0]) ** (- g0 / (A[0] * R))
    pb[2] = pb[0] * np.exp(- g0 * (HB[2] - HB[1]) / (R * TB[1]))
    pb[3] = pb[1] * (TB[3] / TB[2]) ** (- g0 / (A[2] * R))
    pb[4] = pb[2] * (TB[4] / TB[3]) ** (- g0 / (A[3] * R))
    
    if H < 0:
        T = TB[0]
        p = PB[0]
        rho = p / (R*T)
        a = np.sqrt(gama * R * T)
        mu = mu0
        Hp = 0 
    else:
        if H > 50000:
            T = TB[4]
            p =  pb[3] * np.exp(- g0 * (HT[4] - HB[4]) / (R * TB[4]))
            rho = p / (R*T)
            a = np.sqrt(gama * R * T)
            mu = mu0 * (T / TB[0]) * ((TB[0] + 110) / (T + 110))
            Hp = HB[4] - (R * TB[4] / g0) * np.log(p / pb[3])
        else:
            i = 0
            while H - HT[i] > 0:
                i = i + 1
            T = tb[i] + A[i] * (H - HB[i])
            
            if (i == 1) or (i == 4):
                p = PB[i] * np.exp(- g0 * (H - HB[i]) / (R * tb[i]))
            else:
                p = PB[i] * (T / tb[i]) ** (- g0 / (A[i] * R))
            
            rho = p / (R * T)
            a = np.sqrt(gama * R * T)
            mu = mu0 * (T /  TB[0]) * ((TB[0] + 110) / (T - 110))
            
            
            i = 0
            while p - PB[i +1] < 0:
                i = i + 1
                if i == 4:
                    break
            if (i == 1) or (i == 4):
                Hp = HB[i] - (R * TB[i] / g0) * np.log(p / PB[i])
            else:
                Hp = HB[i] - (TB[i] / A[i]) * ((p / PB[i]) ** (- A[i] * R / g0) - 1)
                
    return T,p,rho,a,mu,Hp
                            
 