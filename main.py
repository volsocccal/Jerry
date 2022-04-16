import time 
import pandas as pd


def readAnagrafiche() -> pd.Dataframe:
    elenco_totale_path = "elenco_anagrafiche_qualifiche.xlsx"
    print("Reading " + elenco_totale_path)
    df_elenco_totale = pd.read_excel(elenco_totale_path, sheet_name="Report")
    df_elenco_totale.drop(df_elenco_totale.tail(1).index,inplace=True) # Remove Last Row
    print(" ")
    time.sleep(0.3)
    return df_elenco_totale

def readServizi() -> pd.Dataframe:
    elenco_servizi_path = "elenco_servizi.xlsx"
    print("Reading " + elenco_servizi_path)
    df_elenco_servizi = pd.read_excel(elenco_servizi_path, sheet_name="Report")
    df_elenco_servizi.drop(df_elenco_servizi.tail(1).index,inplace=True) # Remove Last Row
    df_elenco_servizi.drop(['GG', 'Partenza', 'Arrivo', 'Km inizio', 'Km fine', 'Km', 'Assistiti', 'N. Serv.', 'F. Viag.', 'Importo', 'Per.Fatturazione'], axis=1,inplace=True)
    #df_elenco_servizi_personale = elaborate_servizi(df_elenco_servizi)
    print(" ")
    time.sleep(0.3)
    return df_elenco_servizi


def main():
    
    # Log Start Time
    start_time = time.process_time()

    # Read Anagraphic DF
    df_elenco_totale = readAnagrafiche()

    # Read Servizi
    df_elenco_servizi = readServizi()

    # Read TURNI
    elenco_turni_path = "elenco_turni.xlsx"
    print("Reading " + elenco_turni_path)
    df_elenco_turni = pd.read_excel(elenco_turni_path, sheet_name="Report")
    df_elenco_turni.drop(df_elenco_turni.tail(1).index,inplace=True) # Remove Last Row
    print(" ")
    time.sleep(0.3)
    
     # Read PRESENZE
    elenco_presenze_path = "elenco_presenze.xlsx"
    print("Reading " + elenco_presenze_path)
    df_presenze = pd.read_excel(elenco_presenze_path, sheet_name="Report")
    df_presenze.drop(df_presenze.tail(1).index,inplace=True) # Remove Last Row
    print(" ")
    time.sleep(0.3)

    # Output Folder
    OUTPUT_FOLDER = "../../Tommy Data/"

    # Log End Time
    end_time = time.process_time()
    
    # Print Time
    time.sleep(0.5) 
    print("")
    print("All Done :), took ", str(end_time - start_time), " secs]")

if __name__ == "__main__":
    main()