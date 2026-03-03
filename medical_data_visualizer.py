import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

# 1
med_da= pd.read_csv('medical_examination.csv')

# 2
med_da["overweight"]= ((med_da["weight"]/((med_da["height"]/100)**2))>25).astype(int)
# 3
med_da["cholesterol"] = (med_da["cholesterol"] > 1).astype(int)
med_da["gluc"] = (med_da["gluc"] > 1).astype(int)

# 4
def draw_cat_plot():

    med_da_cat=pd.melt(med_da, id_vars=["cardio"], value_vars=["cholesterol", "gluc", "smoke", "alco", "active", "overweight"])

    med_da_cat_group=(
        med_da_cat
        .groupby(["cardio", "variable", "value"])
        .size()
        .reset_index(name="total")
    )

    med_da_cat_group_long=sns.catplot(
        data=med_da_cat_group,
        x="variable",
        y="total",
        hue="value",
        col="cardio",
        kind="bar"
    )

    med_da_cat_group_long.set_axis_labels("variable", "total")
    
    fig=med_da_cat_group_long.fig
    
    fig.savefig('catplot.png')
    return fig

# 10
def draw_heat_map():
    med_da_heat=med_da[
    (med_da["ap_lo"] <= med_da["ap_hi"]) &
    (med_da['height'] >= med_da['height'].quantile(0.025)) &
    (med_da['height'] <= med_da['height'].quantile(0.975)) &
    (med_da['weight'] >= med_da['weight'].quantile(0.025)) &
    (med_da['weight'] <= med_da['weight'].quantile(0.975))
    ]

    corr = med_da_heat.corr()
    mask = np.triu(np.ones_like(corr, dtype=bool))
    fig, ax = plt.subplots(figsize=(12, 10))
    

    # 15
    sns.heatmap(
    corr,
    mask=mask,
    annot=True,
    fmt=".1f",
    square=True,
    ax=ax
    )


    # 16
    fig.savefig('heatmap.png')
    return fig
