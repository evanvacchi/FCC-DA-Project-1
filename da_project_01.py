import numpy as np

def calculate(lst):
    try:
        v1 = np.array(lst[0:3])
        v2 = np.array(lst[3:6])
        v3 = np.array(lst[6:])
        arr = np.vstack((v1, v2, v3))
        d = dict()
        ma1 = np.mean(arr, axis=0).tolist()
        ma2 = np.mean(arr, axis=1).tolist()
        fm = np.mean(arr)
        d['mean'] = [ma1, ma2, fm]
        va1 = np.var(arr, axis=0).tolist()
        va2 = np.var(arr, axis=1).tolist()
        fv = np.var(arr)
        d['variance'] = [va1, va2, fv]
        sda1 = np.std(arr, axis=0).tolist()
        sda2 = np.std(arr, axis=1).tolist()
        fsd = np.std(arr)
        d['standard deviation'] = [sda1, sda2, fsd]
        mxa1 = np.max(arr, axis=0).tolist()
        mxa2 = np.max(arr, axis=1).tolist()
        fmx = np.max(arr)
        d['max'] = [mxa1, mxa2, fmx]
        mna1 = np.min(arr, axis=0).tolist()
        mna2 = np.min(arr, axis=1).tolist()
        fmn = np.min(arr)
        d['min'] = [mna1, mna2, fmn]
        suma1 = np.sum(arr, axis=0).tolist()
        suma2 = np.sum(arr, axis=1).tolist()
        fsum = np.sum(arr)
        d['sum'] = [suma1, suma2, fsum]
        # print(d)
        return(d)
    except ValueError:
        if len(lst) < 9:
            raise ValueError('List must contain nine numbers.')


test = [0,1,2,3,4,5,6,7,8]
calculate(test)
