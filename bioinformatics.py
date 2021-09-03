#!/usr/bin/env python
# coding: utf-8

# In[17]:


import pandas as pd
import streamlit as st
from PIL import Image
import altair as alt

image=Image.open('3-D_DNA-56a09ae45f9b58eba4b20266.jpg')
st.image(image,use_column_width=True)

st.write("""
# DNA nuceliotide count webapp

This app counts the nucleiotide composition of query dna
""")

st.header('Enter the DNA sequence')

sequence_input=">DNA Query 2\nGAACACGTGGAGGCAAACAGGAAGGTGAAGAAGAACTTATCCTATCAGGACGGAAGGTCCTGTGCTCGGG\nATCTTCCAGACGTCGCGACTCTAAATTGCCCCCTCTGAGGTCAAGGAACACAAGATGGTTTTGGAAATGC\nTGAACCCGATACATTATAACATCACCAGCATCGTGCCTGAAGCCATGCCTGCTGCCACCATGCCAGTCCT"

sequence=st.text_area("sequence input",sequence_input,height=250)
sequnce=sequence.splitlines()
sequence=sequence[1:]
sequence="".join(sequence)

st.header('Input(DNA query)')
sequence

st.header('Output(DNA nuceliotide count)')
st.subheader('1.print dictionary')

def dna_nucleiotide_count(seq):
    d=dict([ 
        ('A',seq.count('A')),
        ('T',seq.count('T')),
        ('G',seq.count('G')),
        ('C',seq.count('C')),    
    ])
    return d

X=dna_nucleiotide_count(sequence)

X

st.subheader('2. Print text')
st.write('There are  ' + str(X['A']) + ' adenine (A)')
st.write('There are  ' + str(X['T']) + ' thymine (T)')
st.write('There are  ' + str(X['G']) + ' guanine (G)')
st.write('There are  ' + str(X['C']) + ' cytosine (C)')

st.subheader('3. Display DataFrame')
df = pd.DataFrame.from_dict(X, orient='index')
df = df.rename({0: 'count'}, axis='columns')
df.reset_index(inplace=True)
df = df.rename(columns = {'index':'nucleotide'})
st.write(df)

st.subheader('display barchat')
p = alt.Chart(df).mark_bar().encode(
    x='nucleotide',
    y='count'
)

p=p.properties(
width=alt.Step(80)
)

st.write(p)


# In[ ]:




