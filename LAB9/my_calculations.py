# %Writefile my_calculations.py

def working_capital(x, y):
    wc = []
    for i in range(len(x)):
        wc.append(x[i] - y[i])
    return wc

def current_ratio(x, y):
    cr = []
    for i in range(len(x)):
        cr.append(round(x[i] / y[i], 2))
    return cr 

def debt_assets(x, y):
    sx = 0
    sy = 0
    for i in range(len(x)):
        sx += x[i]
        sy += y[i]
    ds = sy / sx
    return round(ds, 3)
