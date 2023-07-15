import streamlit as st


s=input ("enter the value:")
reverse=s[::-1]
  
if(s==reverse):
    print("it is a palindrom")
else:
    print("it is not a palindrom")
