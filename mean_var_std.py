import numpy as np

def calculate(list_digs):
    if len(list_digs) !=9:
        raise ValueError("List must contain nine numbers.")
    else:
    
        mtx_list=np.array(list_digs)
        mtxx=mtx_list.reshape(3,3)
        
        calculations={"mean": [], "variance" : [], "standard deviation": [], "max" : [], "min" : [], "sum" : []}
        
        mean1_mtx=np.mean(mtxx, axis=0)
        mean2_mtx=np.mean(mtxx, axis=1)
        mean0_mtx=np.mean(mtxx)
        means=[]
        means.append(mean1_mtx.tolist())
        means.append(mean2_mtx.tolist())
        means.append(mean0_mtx.tolist())
        
        calculations["mean"]=means
        
        var1_mtx=np.var(mtxx, axis=0)
        var2_mtx=np.var(mtxx, axis=1)
        var0_mtx=np.var(mtxx)
        vars=[]
        vars.append(var1_mtx.tolist())
        vars.append(var2_mtx.tolist())
        vars.append(var0_mtx.tolist())
        
        calculations["variance"]=vars
        
        std1_mtx=np.std(mtxx, axis=0)
        std2_mtx=np.std(mtxx, axis=1)
        std0_mtx=np.std(mtxx)
        
        stds=[]
        stds.append(std1_mtx.tolist())
        stds.append(std2_mtx.tolist())
        stds.append(std0_mtx.tolist())
        
        calculations["standard deviation"]=stds
        
        max1_mtx=np.max(mtxx, axis=0)
        max2_mtx=np.max(mtxx, axis=1)
        max0_mtx=np.max(mtxx)
        
        maxs=[]
        
        maxs.append(max1_mtx.tolist())
        maxs.append(max2_mtx.tolist())
        maxs.append(max0_mtx.tolist())
        
        calculations["max"]=maxs
        
        min1_mtx=np.min(mtxx, axis=0)
        min2_mtx=np.min(mtxx, axis=1)
        min0_mtx=np.min(mtxx)
        
        mins=[]
        
        mins.append(min1_mtx.tolist())
        mins.append(min2_mtx.tolist())
        mins.append(min0_mtx.tolist())
        
        calculations["min"]=mins
        
        sum1_mtx=np.sum(mtxx, axis=0)
        sum2_mtx=np.sum(mtxx, axis=1)
        sum0_mtx=np.sum(mtxx)
        
        sums=[]
        
        sums.append(sum1_mtx.tolist())
        sums.append(sum2_mtx.tolist())
        sums.append(sum0_mtx.tolist())
        
        calculations["sum"]=sums
        
        
        
        
        
        
        
            
        
        



    return calculations


