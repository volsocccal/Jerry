import time 
import pandas as pd

from parser import volontariParser
from volcalenums import QualificaType
from constraintsChecker.hasQualifica import getAllVolontariWithQualifica

from parser.volontariParser import parseElencoTotaleQualificheFormazione


def readDf(INPUT_FOLDER: str, fileName: str):
    path = INPUT_FOLDER + '//' + fileName
    print("Reading " + path)
    df = pd.read_excel(path, sheet_name="Report")
    df.drop(df.tail(1).index,inplace=True) # Remove Last Row
    print(" ")
    time.sleep(0.3)
    return df


def main():

    INPUT_FOLDER = "data//"
    
    # Log Start Time
    start_time = time.process_time()

    # Read Anagraphic DF
    df_elenco_totale = readDf(INPUT_FOLDER, "elenco_anagrafiche_qualifiche.xlsx")

    # Read Formazione
    df_formazione = readDf(INPUT_FOLDER, "elenco_formazione.xlsx")

    # Parse DF Elenco Totale and DF Formazione
    dictVolontari = parseElencoTotaleQualificheFormazione(df_elenco_totale, df_formazione)

    # Produce Elenchi Qualifiche
    autisti_A = getAllVolontariWithQualifica(dictVolontari, QualificaType.AUTISTA_A)

    # Read Servizi
    df_elenco_servizi = readDf(INPUT_FOLDER, "elenco_servizi.xlsx")
    df_elenco_servizi.drop(['GG', 'Partenza', 'Arrivo', 'Km inizio', 'Km fine', 'Km', 'Assistiti', 'N. Serv.', 'F. Viag.', 'Importo', 'Per.Fatturazione'], axis=1,inplace=True)
    df_elenco_servizi['Intervento'] = df_elenco_servizi['Intervento'].str.replace('IN CONVENZIONE', 'ALLA PERSONA')

    # Read TURNI
    df_elenco_turni = readDf(INPUT_FOLDER, "elenco_turni.xlsx")
    
    # Read PRESENZE
    df_presenze = readDf(INPUT_FOLDER, "elenco_presenze.xlsx")

    # Output Folder
    OUTPUT_FOLDER = "output//"

    # Log End Time
    end_time = time.process_time()
    
    # Print Time
    time.sleep(0.5) 
    print("")
    print("All Done :), took ", str(end_time - start_time), " secs]")

if __name__ == "__main__":
    main()