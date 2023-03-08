#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px


# In[ ]:


DataMath = pd.read_csv("Maths.csv")
DataPort = pd.read_csv("Portuguese.csv")
DataPort['subject'] = 'Portuguese'
DataMath['subject'] = 'Math'


# In[ ]:


df = pd.concat([DataMath, DataPort])


# In[ ]:


grade = []
for G3 in df["G3"]:
    if G3 < 10 : grade.append("F")
    elif G3 < 12 : grade.append("E")
    elif G3 < 14 : grade.append("D")
    elif G3 < 16 : grade.append("C")
    elif G3 < 18 : grade.append("B")
    else: grade.append("A")

df["Grade"] = grade


# In[ ]:


st.title("Test van eigen grafieken")


# In[ ]:


InputDalc = st.checkbox("Select alcohol usage during week",
                       ("1","2","3","4","5"))


# In[ ]:


DalcSelect = df[df[Dalc] == InputDalc]


# In[ ]:


fig1 = px.pie(data_frame = df,
      values = "health",
      names = "health")


# In[ ]:


st.plotly_chart(fig1)


# In[ ]:


fig2 = px.scatter(data_frame=df,
          x = "absences",
          y = "goout",
          color = "Grade")


# In[ ]:


st.plotly_chart(fig2)

