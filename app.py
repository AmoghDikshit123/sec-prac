import streamlit as st
from sklearn.linear_model import LogisticRegression

X=[[1],[2],[3],[4]]
y=[0,1,0,1]
model=LogisticRegression().fit(X,y)
val=st.number_input("Enter a value",value=1.5)
if st.button('predict'):
    pred=model.predict([[val]])
    st.write(f"Prediction:{pred[0]}")