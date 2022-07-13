
# shapiro wilk test analysis
def swt(data, a, ttl, n_bins, c):

    # libraries
    from scipy.stats import shapiro, probplot
    import seaborn as sns
    import matplotlib.pyplot as plt
    
    
    # shapiro
    stat, p = shapiro(data)
    
    # normality
    if p>a:
        nml = 'Normal'
    else:
        nml = 'Not Normal'
    
    # viz
    fig, [ax_1, ax_2] = plt.subplots(1, 2, figsize=(18,8), constrained_layout=True)
    plt.suptitle(ttl)
    
    # hist
    sns.histplot(ax=ax_1, data=data, stat='probability',
                 element='step', kde=True, bins=n_bins, alpha=0.2,
                 color=c)
    # qq 
    probplot(data, dist='norm', plot=ax_2)
    
    # format
    ax_1.set_title(f'P-value = {round(p*100, 1)}% ({nml})')
    ax_1.set_xlabel(ax_2.get_ylabel())
    ax_2.get_lines()[1].set_linewidth(2)
    ax_2.get_lines()[1].set_linestyle('--')
    ax_2.get_lines()[0].set_color(c)
    ax_2.get_lines()[0].set_alpha(0.25)
    
    # return
    return plt.show()