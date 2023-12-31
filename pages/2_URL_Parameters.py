import streamlit as st
st.set_page_config(
    layout="centered", page_title="URL Parameters", initial_sidebar_state="auto")

# Henter variabler ind fra URL'en i get_parms (python variablen),
# som er en dictionary. Her kan være flere Key / Values i.
# Dvs. flere variabler i en dictionary variable.

get_parms = st.experimental_get_query_params()

# Skriver get_parms (alle variabler) ud (husk det er en dictionary)
st.write(f"""
    # URL variable
    {str(get_parms)}
""")


# Fjerner " og ' fra strengen
def strip_quotes(str: str) -> str:
    return_string = str.replace('"', "").replace("'", "")
    return (return_string)

if ('Name' in get_parms) and ('Email' in get_parms):
    # Opretter en Form i streamlit, som hedder Unsubscribe
    with st.form("Unsubscribe"):
        # Tildeler get_parms['Name'] variablen til Name (python variablen)
        Name = strip_quotes(get_parms['Name'][0])
        # Laver et tekst input felt, som er pre-udfyldt Name variablen (python variablen) 
        form_name = st.text_input(label="Name:",value=Name, disabled=True)
        # Tildeler get_parms['Email'] variablen til Email (python variablen)
        Email = strip_quotes(get_parms['Email'][0])
        # Laver et tekst input felt, som er pre-udfyldt Email variablen (python variablen) 
        form_email = st.text_input(label="Email:",value=Email, disabled=True,)

        # Laver en submitknap, som så submitter formen
        form_submit = st.form_submit_button(label="Unsubscribe", type="primary")
    
        if form_submit:
            st.info(f"{form_name} with {form_email} is now unsubscribed")