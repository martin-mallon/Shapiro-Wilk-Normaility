# Shapiro Wilk Normality Checks

<br>

<p align="center" width="100%">
    <img width="85%" src="/Shapiro_Wilk_Normality/shapiro.png">
</p>

<br>

## Overview
  
This project uses the Shapiro-Wilk test to detect significant deviations from normality. From the <code>scipy.stats</code> library, the <code>shapiro</code> function assesses the normality of a series of data, represented by a <i>p</i>-value. This is accompanied by two visual representations of the data using <code>seaborn</code>'s <code>histplot</code> and <code>scipy.stat</code>'s <code>probplot</code> (QQ plot).

<br>

## Shapiro

* Import ```shapiro``` and pass the data series as an argument. This will produce the *p*-value that is used to assess normality.

    ```Python
    # shapiro
    from scipy.stats import shapiro
    stat, p = shapiro(data)
    ```

<br>

## Logical Statement

* The Shapiro-Wilk logic follows, and is represented by:

    * Hypothesis - "Shapiro-Wilk detects significant deviations from normality." 
        * Alternative Hypothesis Ha - "This data is not normally distributed."
        * Null Hypothesis H0 - "This data is normally distributed."
        
    * a - Statistical significance, e.g. &alpha; = 5%, sig = 95%.
    
    * p-value - Determines if H0 if rejected or not:
        * p < a - e.g. 2%, enough confidence to reject H0, therefore Ha is accepted (data is not normal).
        * p >= a - e.g. 8%, insufficient confidence to reject H0, therefore Ha is rejcted (data is normal).


            ```Python
            # logic
            if p>0.05:
                nml = 'Normal'
            else:
                nml = 'Not Normal'
            ```

<br>

## Histogram

* A histogram represents the distribution of the data, with the *p*-value and ```nml``` results passed as title arguments. Normally distributed data follows the classic bell curve shape.

    ```Python
    # histogram
    import seaborn as sns
    import matplotlib.pyplot as plt
    g = sns.histplot(data=data, stat='probability',
                     element='step', kde=True)
    g.set_title(f'P-value = {round(p*100, 1)}% ({nml})')
    plt.show()
    ```
    
 <br>

## QQ Plot

* A QQ plot compares the quantiles of the ```data``` (represented by the scatter) and the theoretical normal distribution (represented by the line). Normally distributed data will follow the theoretical line.

    ```Python
    # qq
    from scipy.stats import probplot
    g = probplot(data, dist='norm', plot=plt)
    plt. show()
    ```
