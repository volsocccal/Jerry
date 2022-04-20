import time 
import pandas as pd


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

    # Read Servizi
    df_elenco_servizi = readDf(INPUT_FOLDER, "elenco_servizi.xlsx")
    df_elenco_servizi.drop(['GG', 'Partenza', 'Arrivo', 'Km inizio', 'Km fine', 'Km', 'Assistiti', 'N. Serv.', 'F. Viag.', 'Importo', 'Per.Fatturazione'], axis=1,inplace=True)

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