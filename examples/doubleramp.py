import numpy as np
import pandas as pd
from vrplot import bar3d

# TODO: Try with -1 to 1
X, Y = np.linspace(0, 1, 10), np.linspace(0, 1, 10)
xx, yy = np.meshgrid(X, Y)
zz = xx*yy
size = xx

df = pd.DataFrame({'x': xx.flatten(), 'y': yy.flatten(), 'z': zz.flatten(), "size": size.flatten()})
df = df[df['size'] != 0]

fig = bar3d(df, x='x', z='z', height="y", size_multiplier=2)
fig.user_position = (0, 0, 2)
fig.save('examples/output/doubleramp.html')