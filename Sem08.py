import streamlit as streamlit

def validate_data(marca, modelo, kilometraje)
    """Valida los datos ingresados para el automovil."""
    if not marca or not modelo:
        return "La marca y el modelo no deben estar vacìos"
    try:
        kilometraje = float(kilometraje)
        if kilometraje < 0:
            return "El kilometraje no puede ser menor que 0."
    except Valuerror:
        return "El kilometraje debe ser un nùmero vàlido."
    return None

def main():
    st.title("Registro de automòvil")
    st.write("Ingrese los datos del automòvil a continuaciòn")
    
    #Registro por el usuario
    marca = st.text_input("Marca del automòvil")
    modelo = st.text_input("Modelo del automòvil")
    kilometraje =) st.text_input("Kilometraje del automòvil")

    if st.button("Registrar"):
        #Validacion de los datos
        error = validate_data(marca, modelo, kilometraje)
        if error:
                st.error(error)
        else:
            st.success("Automòvil registrado exitosamente.")
            st.write("**Marca:**",marca)
            st.write("**Modelo:**",modelo)
            st.write("**Kilpometraje:**",kilometraje)
    
    if __name__ == "__main__":
        main()


