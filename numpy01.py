
__author__ = 'MeatBallCore'

import numpy as np
import pandas as pd
import matplotlib.pylab as plt

#generate arrays in slide 01
arrays = []
a = np.array([1.0,2.0,3.0])
arrays.append([[1],[2],[3],[4],[5],['...']])
arrays.append([[1.1],[1.2],[1.3],[1.4],['...']])
arrays.append([[2.1],[2.2],[2.3],[2.4],['...']])
arrays.append(np.array([1,2,3,4,5]))
arrays.append(np.array([[1,2],[3,4],[5,6],[7,8]]))
arrays.append(np.zeros((3,2), dtype = 'int32'))
arrays.append(np.zeros_like(a))
arrays.append(np.ones((3,2), dtype = 'int32'))
arrays.append(np.ones_like(a))
arrays.append(np.empty((3,2)))
arrays.append(np.empty_like(a))
arrays.append(np.full((3,2), -1, dtype = 'int32'))
arrays.append(np.full_like(a, -1))
arrays.append(np.identity(3, dtype = 'int32'))
arrays.append(np.eye(3, k=0, dtype = 'int32'))
arrays.append(np.eye(3, k=1, dtype = 'int32'))
arrays.append(np.eye(3, k=2, dtype = 'int32'))
arrays.append(np.arange(1, 6, 2))
a = np.array([1, 11, 21])
arrays.append(a)
b = np.array([5, 25, 50])
arrays.append(b)
arrays.append(np.linspace(a, b, 5))
#whether arrays need related empty array
empty = [False, False, False, False, False, True, True, True, True, True, True, True, True, True, True, False, False, False, False, False, False]
#whether array is generated by np
isnp = [False, False, False, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True, True]
#cell colors for arrays
ccolors = ['limegreen',
    'dodgerblue',
    'dodgerblue',
    'gold',
    'coral',
    'olivedrab',
    'teal',
    'olivedrab',
    'teal',
    'olivedrab',
    'teal',
    'olivedrab',
    'teal',
    'orange',
    'peru',
    'peru',
    'peru',
    'hotpink',
    'mediumorchid',
    'mediumorchid',
    'mediumorchid']
#edge colors for arrays
ecolors = ['lightgreen',
    'lightskyblue',
    'lightskyblue',
    'cornsilk',
    'mistyrose',
    'honeydew',
    'lightcyan',
    'honeydew',
    'lightcyan',
    'honeydew',
    'lightcyan',
    'honeydew',
    'lightcyan',
    'bisque',
    'linen',
    'linen',
    'linen',
    'lavenderblush',
    'thistle',
    'thistle',
    'thistle']
#fcolors = ['darkgreen']
#draw arrays
for i in range(len(arrays)):
    fig, ax = plt.subplots()
    fig.patch.set_visible(False)
    ax.axis('off')
    ax.axis('tight')
    #df = pd.DataFrame(a)
    if isnp[i]:
        df = pd.DataFrame(arrays[i])
        cellT = df.values

        if arrays[i].ndim == 1:
            colorlist = [ccolors[i]]
        else:
            colorlist = [ccolors[i]] * arrays[i].shape[1]
        colorlist = [colorlist] * arrays[i].shape[0]

        #bwidth = 0.3 * arrays[i].shape[0]
        if arrays[i].ndim == 1:
            bwidth = 0.25
        else:
            bwidth = 0.25 * arrays[i].shape[1]
    else:
        cellT = arrays[i]
        colorlist = [[ccolors[i]]* len(arrays[i][0])]*len(arrays[i])
        bwidth = 0.25 * len(arrays[i][0])
    #print(colorlist)
    table1 = ax.table(cellText = cellT,
        cellLoc='center',
        cellColours = colorlist,
        bbox=[0,0,bwidth,1])

    table_props = table1.properties()
    table_cells = table_props['child_artists']
    for cell in table_cells:
        cell.set_edgecolor(ecolors[i])
        cell.set_linewidth(4)
        text = cell.get_text()
        text.set_fontsize(20)
        text.set_color('white')
        text.set_fontweight('bold')

    fig.tight_layout()
    filename = 'D:/' + str(i) + '.png'
    plt.savefig(filename)
    #plt.show()

    #related empty array
    if empty[i]:
        if arrays[i].ndim == 1:
            empty_array = [' ']
        else:
            empty_array = [' '] * arrays[i].shape[1]
        empty_array = [empty_array] * arrays[i].shape[0]

        fig, ax = plt.subplots()
        fig.patch.set_visible(False)
        ax.axis('off')
        ax.axis('tight')

        table1 = ax.table(cellText = empty_array,
        cellLoc='center',
        cellColours = colorlist,
        bbox=[0,0,bwidth,1])

        table_props = table1.properties()
        table_cells = table_props['child_artists']
        for cell in table_cells:
            cell.set_edgecolor(ecolors[i])
            cell.set_linewidth(4)
            #text = cell.get_text()
            #text.set_fontsize(20)
            #text.set_color(fcolors[i])
            #text.set_fontweight('bold')

        fig.tight_layout()
        filename = 'D:/' + str(i) + 'empty.png'
        plt.savefig(filename)
        #plt.show()
