import streamlit as st

def calcular(operacion, num1, num2):
    """Realiza la operaciòn especificada entre num1 y num2"""
    try:
        num1 = float(num1)
        num2 = float(num2)
    except ValuError:
        return "Por favor, ingrese nùmeros vàlidos"
    
    if operacion == "Suma":
        return num1+num2
    elif operacion == "Resta":
        return num1-num2
    elif operacion== "Multiplicaciòn":
        return num1*num2
    elif operacion == "Divisiòn":
        if num2 == 0:
            return "Error: no se puede dividir entre o"
        return num1/num2
    else: 
        return "Operacion no vàlida"

def main():
    st.title("Calculadora bàsica")
    st.write("Seleccione la operacion e ingrese los nùmeros")

    #Seleccione la operaciòn
    operacion =  st.selectbox("operaciòn"("Suma", "Resta", "Multiplicaciòn","Diviciòn"))

    #Entradas para los nùmeros 
    num1 = st.text_input("Nùmero1")
    num2 = st.text_input("Nùmero2")

    #Boton para calcular
    if st.button("Calcular")
        Redultado = calcular(operacion, num1, num2)
        st.write("**Resultado:**,resultado")

if __name__ =="__main__":
    main()