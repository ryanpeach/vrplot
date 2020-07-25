import numpy as np
import pandas as pd
from vrplot import scatter3d, line3d

t = np.linspace(0, 2*np.pi, 100)
x = t * np.cos(t)
y = t * np.sin(t)
z = t * np.cos(t)
size = t / 100

df = pd.DataFrame({'x': x, 'y': y, 'z': z, "size": size})
df = df[df['size']!=0]

fig = scatter3d(df, x='x', y='y', z='z', point_size="size")
fig += line3d(df, x='x', y='y', z='z')
fig.user_position = (0, 0, 10)
fig.save('examples/output/archimedeanspiral.html')