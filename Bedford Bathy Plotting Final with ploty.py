#!/usr/bin/env python
# coding: utf-8

# In[1]:


import plotly.graph_objects as go

import pandas as pd

# Read data from a csv
z_data = pd.read_csv('bathy_bedford.csv')

fig = go.Figure(data=[go.Surface(z=z_data.values)])

fig.update_layout(title='Bedford Basin Elevation', autosize=True,
                   width=900, height=900,
                   margin=dict(l=65, r=50, b=65, t=90))

fig.show()


# In[2]:


#  cmap=plt.cm.viridis, linewidth=0.2


# In[4]:


fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))


# # Surface Plot With Contours

# In[5]:


import plotly.graph_objects as go

import pandas as pd

# Read data from a csv
z_data = pd.read_csv('bathy_bedford.csv')

fig = go.Figure(data=[go.Surface(z=z_data.values)])
fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))
fig.update_layout(title='Bedford Basin Elevation', autosize=True,
                   width=900, height=900,
                   margin=dict(l=65, r=50, b=65, t=90))

fig.show()


# In[6]:


import plotly.graph_objects as go
import numpy as np
import pandas as pd

# Read data from a csv
z_data = pd.read_csv('bathy_bedford.csv')


# In[7]:


z = z_data.values
sh_0, sh_1 = z.shape
x, y = np.linspace(44.66875, 44.74791667, sh_0), np.linspace(-63.69791667, -63.52708333, sh_1)


# In[8]:


x


# In[9]:


y


# In[10]:


import plotly.graph_objects as go
import pandas as pd
import numpy as np
# Read data from a csv
z_data = pd.read_csv('bathy_bedford.csv')
z = z_data.values
sh_0, sh_1 = z.shape
x, y = np.linspace(44.66875, 44.74791667, sh_0), np.linspace(-63.69791667, -63.52708333, sh_1)
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))
fig.update_layout(title='Bedford Basin Elevation', autosize=True,
                  width=900, height=900, 
                  margin=dict(l=65, r=50, b=65, t=90))
fig.update_layout=dict(xaxis=dict(title='Latitude'),
                  yaxis=dict(title='Longitude'))
fig.show()


# # Configure Surface Contour Levels

# In[11]:


import plotly.graph_objects as go
import pandas as pd
import numpy as np

# Read data from a csv
z_data = pd.read_csv('bathy_bedford.csv')
z = z_data.values
sh_0, sh_1 = z.shape
x, y = np.linspace(44.66875, 44.74791667, sh_0), np.linspace(-63.69791667, -63.52708333, sh_1)
# fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])

fig = go.Figure(go.Surface(
    contours = {
        "x": {"show": True, "start": 44.66875, "end": 44.74791667, "size": 0.04, "color":"white"},
        "z": {"show": True, "start": -63.69791667, "end": -63.52708333, "size": 0.05}
    },
    z=z, x=x, y=y))
fig.update_layout(
        scene = {
            "xaxis": {"nticks": 20},
            "zaxis": {"nticks": 8},
            'camera_eye': {"x": 0, "y": -1, "z": 0.5},
            "aspectratio": {"x": 1, "y": 1, "z": 0.2}
        })
fig.show()


# In[12]:


import plotly.graph_objects as go
import pandas as pd
import numpy as np
# Read data from a csv
z_data = pd.read_csv('bathy_bedford.csv')
z = z_data.values
sh_0, sh_1 = z.shape
x, y = np.linspace(44.66875, 44.74791667, sh_0), np.linspace(-63.69791667, -63.52708333, sh_1)
fig = go.Figure(data=[go.Surface(z=z, x=x, y=y)])
fig.update_traces(contours_z=dict(show=True, usecolormap=True,
                                  highlightcolor="limegreen", project_z=True))
fig.update_layout(title='Bedford Basin Elevation',xaxis_title="Latitude", 
                  yaxis_title="Longitude",autosize=False,
                  width=900, height=900, 
                  margin=dict(l=65, r=50, b=65, t=90))
fig.update_layout(scene = dict(
                    xaxis_title='Latitude',
                    yaxis_title='Longitude',
                    zaxis_title='Elevation'),
                    margin=dict(r=20, b=10, l=10, t=10))  
# fig.update_layout(color='Elevation')
fig.update_layout(coloraxis_colorbar=dict(
    title="Elevation",
    thicknessmode="pixels", thickness=50,
    lenmode="pixels", len=200,
    yanchor="top", y=1,
    ticks="outside", ticksuffix="",
    dtick=5
))
fig.show()


# In[14]:


import numpy as np
import plotly.graph_objs as go

# define time and space data
x = np.linspace(-10, 10, 400)
t = np.linspace(0, 4*np.pi, 200)
xx, tt = np.meshgrid(x, t)
f1 = 1/np.cosh(xx + 3) * np.exp(1j*2.3*tt)

# visualize
fig = go.Figure(go.Surface(z=np.real(f1), x=xx, y=tt))
# fig.update_traces(contours_z=dict(show=True, usecolormap=True,
#                                   highlightcolor="limegreen", project_z=True))
fig.update_layout(title='Plot Title',autosize=True,
                  width=900, height=900, 
                  margin=dict(l=65, r=50, b=65, t=90))
fig.update_layout(scene = dict(
                    xaxis_title='X-axis Title',
                    yaxis_title='Y-axis Title',
                    zaxis_title='Z-axis Title'))                    
fig.show()


# # Appendix Bathy Data

# In[25]:


z_data

