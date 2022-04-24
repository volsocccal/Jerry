import pandas as pd

from core.formazione import Formazione
from core.qualifica import Qualifica
from core.volontario import Volontario



# Headings ELENCO QUALIFICHE
QUALIFICHE_cognome_COL_HEAD = "Cognome"
QUALIFICHE_nome_COL_HEAD = "Nome"
QUALIFICHE_cf_COL_HEAD = "Codice fiscale"
QUALIFICHE_citta_born_COL_HEAD = "Città nascita"
QUALIFICHE_sex_COL_HEAD = "Sesso"
QUALIFICHE_data_born_COL_HEAD = "Data nascita"
QUALIFICHE_citta_residenza_COL_HEAD = "Città residenza"
QUALIFICHE_telefono_COL_HEAD = "Telefono"
QUALIFICHE_cellulare_COL_HEAD = "Cellulare"
QUALIFICHE_email_COL_HEAD = "Email"
QUALIFICHE_squadra_COL_HEAD = "#ID-S"
QUALIFICHE_matricola_COL_HEAD = "Numero"
QUALIFICHE_tipo_qualifica_COL_HEAD = "Qualifica"
QUALIFICHE_data_acq_COL_HEAD = "Data conseguim."
QUALIFICHE_data_renew_COL_HEAD = "Data rinnovo"
QUALIFICHE_data_exp_COL_HEAD = "Data scadenza"
QUALIFICHE_annotazioni_COL_HEAD = "Annotazioni"



# Headings ELENCO FORMAZIONE
FORMAZIONE_cognome_COL_HEAD = "Cognome"
FORMAZIONE_nome_COL_HEAD = "Nome"
FORMAZIONE_cf_COL_HEAD = "Codice fiscale"
FORMAZIONE_citta_born_COL_HEAD = "Luogo nascita"
FORMAZIONE_sex_COL_HEAD = "Sesso"
FORMAZIONE_data_born_COL_HEAD = "Data nascita"
FORMAZIONE_telefono_COL_HEAD = "Telefono"
FORMAZIONE_cellulare_COL_HEAD = "Cellulare"
FORMAZIONE_email_COL_HEAD = "Email"
FORMAZIONE_squadra_COL_HEAD = "#ID-S"
FORMAZIONE_matricola_COL_HEAD = "Numero"
FORMAZIONE_tipo_formazione_COL_HEAD = "Tipo formazione"
FORMAZIONE_data_inizio_COL_HEAD = "Data inizio"
FORMAZIONE_data_fine_COL_HEAD = "Data fine"
FORMAZIONE_esito_COL_HEAD = "Esito"
FORMAZIONE_data_exp_COL_HEAD = "Scadenza"
FORMAZIONE_annotazioni_COL_HEAD = "Annotazioni"


def parseElencoTotaleQualificheFormazione(df_ElencoTotale, df_formazione):

    # Read Formazione
    formazioneDict = generateFormazioneDict(df_formazione)

    # Read Qualifiche
    # Key: matricola
    # Value: List of Qualifiche
    qualificheDict = generateQualificheDict(df_ElencoTotale)

    # Delete Qualifiche Data
    df_ElencoTotale.drop([QUALIFICHE_tipo_qualifica_COL_HEAD, QUALIFICHE_data_acq_COL_HEAD, QUALIFICHE_data_renew_COL_HEAD, QUALIFICHE_data_exp_COL_HEAD, QUALIFICHE_annotazioni_COL_HEAD], axis=1, inplace=True)
    df_ElencoTotale.drop_duplicates(subset = QUALIFICHE_matricola_COL_HEAD, inplace=True)
    df_ElencoTotale.sort_values(by=[QUALIFICHE_matricola_COL_HEAD], inplace=True)


    # Populate Dict Volontari
    volontariDict = dict()
    for matr in df_ElencoTotale[QUALIFICHE_matricola_COL_HEAD]:  # loop through all matricole
        matr_df = df_ElencoTotale[df_ElencoTotale[QUALIFICHE_matricola_COL_HEAD] == matr]
        for index, row in matr_df.iterrows():
            name = row[QUALIFICHE_nome_COL_HEAD] 
            surname = row[QUALIFICHE_cognome_COL_HEAD]
            CF = row[QUALIFICHE_cf_COL_HEAD]
            ID = row[QUALIFICHE_matricola_COL_HEAD] 
            birthdate = row[FORMAZIONE_data_born_COL_HEAD]  
            squadra = row[QUALIFICHE_squadra_COL_HEAD]
            qualifiche = []
            if matr in qualificheDict:
                qualifiche = qualificheDict[matr]
            formazione = []
            if matr in formazioneDict:
                formazione = formazioneDict[matr]            
            volontario = Volontario(name, surname, CF, ID, birthdate, squadra, qualifiche, formazione)
            volontariDict[matr] = volontario

    return volontariDict



# Key: matricola
# Value: List of Formazione
def generateFormazioneDict(df_formazione):
    formazioneDict = dict()
    for matr in df_formazione[FORMAZIONE_matricola_COL_HEAD]:  # loop through all matricole
        matr_df = df_formazione[df_formazione[FORMAZIONE_matricola_COL_HEAD] == matr]
        formazioneList = []
        for index, row in matr_df.iterrows():
            tipoFormazione = row[FORMAZIONE_tipo_formazione_COL_HEAD]
            inizioFormazione = row[FORMAZIONE_data_inizio_COL_HEAD]
            annotazioni = row[FORMAZIONE_annotazioni_COL_HEAD]
            formazione = Formazione(tipoFormazione, inizioFormazione, annotazioni)
            formazioneList.append(formazione)
        formazioneDict[matr] = formazioneList
    return formazioneDict


# Key: matricola
# Value: List of Qualifiche
def generateQualificheDict(df_qualifiche):
    qualificheDict = dict()
    for matr in df_qualifiche[QUALIFICHE_matricola_COL_HEAD]:  # loop through all matricole
        matr_df = df_qualifiche[df_qualifiche[QUALIFICHE_matricola_COL_HEAD] == matr]
        qualificheList = []
        for index, row in matr_df.iterrows():
            tipoQualifica = row[QUALIFICHE_tipo_qualifica_COL_HEAD]
            inizioQualifica = row[QUALIFICHE_data_acq_COL_HEAD]
            fineQualifica = row[QUALIFICHE_data_exp_COL_HEAD]
            annotazioni = row[QUALIFICHE_annotazioni_COL_HEAD]
            qualifica = Qualifica(tipoQualifica, inizioQualifica, fineQualifica, annotazioni)
            qualificheList.append(qualifica)
        qualificheDict[matr] = qualificheList
    return qualificheDict