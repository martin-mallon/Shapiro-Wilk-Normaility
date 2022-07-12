# Shapiro Wilk Normality Checks

<br>

<p align="center" width="100%">
    <img width="85%" src="/Shapiro_Wilk_Normality/shapiro.png">
</p>

<br>

## Overview
  
This project uses the Shapiro-Wilk test to detect significant deviations from normality and visualise the results. The product ```swt``` is a bespoke function that uses elements of ```scipy.stats``` and ```seaborn``` to perform a significance test and plot the distributions against a theoretical norm, producing a clear result as to whether the data is normal or not. Individual elements of ```swt``` are explored in depth below.

<br>

## Shapiro

* Import ```shapiro``` and pass the data series as an argument. This will produce the *p*-value that is used to assess normality.

    ```Python
    # shapiro
    from scipy.stats import shapiro
    stat, p = shapiro(data)
    ```
    
    ```
    ShapiroResult(statistic=0.9987099170684814, pvalue=0.6952224373817444)
    ```

<br>

## Hypothesis Testing

* The Shapiro-Wilk logic follows, and is represented by:

    * Hypothesis - "Shapiro-Wilk detects significant deviations from normality." 
        * Alternative Hypothesis $H_{a}$ - "This data is not normally distributed."
        * Null Hypothesis $H_{0}$ - "This data is normally distributed."
        
    * $&alpha;$ - Statistical significance, e.g. $&alpha;$ = 5%, sig = 95%.
    
    * $p$-value - Determines if $H_{0}$ if rejected or not:
        * $p < &alpha;$ - e.g. 2%, enough confidence to reject $H_{0}$, therefore $H_{a}$ is accepted (data is not normal).
        * $p >= &alpha;$ - e.g. 8%, insufficient confidence to reject $H_{0}$, therefore $H_{a}$ is rejcted (data is normal).


            ```Python
            # logic
            if p>0.05:
                nml = 'Normal'
            else:
                nml = 'Not Normal'
            ```

* Combine ```p``` and ```nml``` to produce a statement of normality:

    ```Python
    print(f'P-value = {round(p*100, 1)}% ({nml})')
    ```
    
    ```
    P-value = 69.5% (Normal)
    ```
<br>

## Histogram

* A histogram represents the distribution of the data, with ```p``` and ```nml``` results passed as title arguments. Normally distributed data follows the classic bell curve shape.

    ```Python
    # histogram
    import seaborn as sns
    import matplotlib.pyplot as plt
    g = sns.histplot(data=data, stat='probability',
                     element='step', kde=True)
    g.set_title(f'P-value = {round(p*100, 1)}% ({nml})')
    plt.show()
    ```

<p align="center" width="100%">
    <img width="40%" src="/Shapiro_Wilk_Normality/hist.png">
</p>

<br>

## QQ Plot

* A QQ plot compares the quantiles of the ```data``` (represented by the scatter) and the theoretical normal distribution (represented by the line). Normally distributed data will follow the theoretical line.

    ```Python
    # qq
    from scipy.stats import probplot
    g = probplot(data, dist='norm', plot=plt)
    plt. show()
    ```

<p align="center" width="100%">
    <img width="40%" src="/Shapiro_Wilk_Normality/qq.png">
</p>

<br>

## ```swt``` Function

* The ```swt``` function takes five arguments to perform the Shapiro-Wilk test and represent the distributions visually. This function is contained in the ```Shapiro_Wilk_Normality_Check.ipynb``` file and is imported to a workspace using ```from ipynb.fs.full.Shapiro_Wilk_Normality_Check import *```.

    ```Python
    # shapiro wilk test analysis
    def swt(data, a, ttl, n_bins, c):
    
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
    ```
