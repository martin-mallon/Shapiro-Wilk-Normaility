# libraries
import seaborn as sns
import matplotlib.pyplot as plt

# style variables
font_size = 12
style_use = 'seaborn-whitegrid'
grey = '#595959'
grey_fade = '#E2E2E2'

# style params
style_params = {
                # font
                'font.family':'consolas', 
                'text.color':grey,
                
                # fig title
                'figure.titlesize': font_size*3,
                
                # ax
                'axes.titlesize': font_size*2,
                'axes.titlepad': 20,
    
                # axis
                'axes.labelsize': font_size,
                'xtick.labelsize': font_size,
                'ytick.labelsize': font_size,
                'axes.labelcolor':grey,
                'xtick.color':grey,
                'ytick.color':grey,
    
                # spines
                'axes.edgecolor':grey_fade,
                'axes.spines.bottom':True,
                'axes.spines.left':False,
                'axes.spines.right':False,
                'axes.spines.top':False,
    
                # grid
                'axes.grid':True,
                'grid.color':grey_fade,
                'grid.alpha':0.8,

                # legend
                'legend.fontsize': font_size,
                'legend.loc': 'best'
                }

# update style
su = plt.style.use(style_use)
sp = plt.rcParams.update(style_params)