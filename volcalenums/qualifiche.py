from enum import Enum

class QualificaType(str, Enum):
    aff_CENTRALINISTA = 'Aff. CENTRALINISTA'
    aff_SOCC = 'Aff. SOCCORRITORE-ESECUTORE'
    aff_TS = 'Aff. TRASPORTO SANITARIO'
    aff_TSS = 'Aff. TRASPORTO SANITARIO SEMPLICE'
    AMMINISTRAZIONE = 'AMMINISTRAZIONE'
    ASSEMBLEA_SOCI = 'ASSEMBLEA SOCI'
    AUDITORE_CONSIGLIO_DIRETTIVO = 'AUDITORE CONSIGLIO DIRETTIVO'
    AUDITORE_DIREZIONE_SERVIZI = 'AUDITORE DIREZIONE SERVIZI'
    AUTISTA_A = 'AUTISTA A - Emergenza'
    AUTISTA_A1 = 'AUTISTA A1 - TS Ambulanza'
    AUTISTA_A2 = 'AUTISTA A2 - TSS Furgone Finestrato'
    AUTISTA_A3 = 'AUTISTA A3 - TSS Auto Attrezzata'
    AUTISTA_A4 = 'AUTISTA A4 - TSS Auto'
    AUTISTA_A5 = 'AUTISTA A5 - No Paziente'
    AUTISTA_SP = 'AUTISTA SERVIZIO ALLA PERSONA'
    BLSD_SSE = 'BLSD SSE'
    BLSD_TS = 'BLSD TS'
    BLSD_TSS = 'BLSD TSS'
    CENTRALINISTA = 'CENTRALINISTA'
    CONSIGLIO_DIRETTIVO = 'CONSIGLIO DIRETTIVO'
    DIREZIONE_SERVIZI = 'DIREZIONE SERVIZI'
    FORMAZIONE_AUTISTA = 'FORMAZIONE AUTISTA'
    FORMAZIONE_SOCCORRITORE = 'FORMAZIONE SOCCORRITORE'
    LAVANDERIA = 'LAVANDERIA'
    GESTIONE_TURNI_SERVIZI = 'GESTIONE TURNI E SERVIZI'
    MANUTENZIONE_AUTOMEZZI = 'MANUTENZIONE AUTOMEZZI'
    MANUTENZIONE_DAE = 'MANUTENZIONE DAE'
    MANUTENZIONE_IT = 'MANUTENZIONE IT'
    MANUTENZIONE_SEDE = 'MANUTENZIONE SEDE'
    MATERIALE_SANITARIO = 'MATERIALE SANITARIO'
    MEDICO = 'MEDICO'
    PATENTE_B = 'PATENTE B'
    RIUNIONE_ESTERNA = 'RIUNIONE ESTERNA'
    RIUNIONE_INTERNA = 'RIUNIONE INTERNA'
    SERVIZIO_ALLA_PERSONA = 'SERVIZIO ALLA PERSONA'
    SERVIZIO_CIVILE = 'SERVIZIO CIVILE'
    SERVIZIO_EMERGENZA = 'SERVIZIO EMERGENZA'
    SERVIZIO_GARA = 'SERVIZIO GARA'
    SERVIZIO_INTERNO = 'SERVIZIO INTERNO'
    SOCC = 'SOCCORRITORE-ESECUTORE (120h)'
    SOCC_CAPO = 'CAPOEQUIPAGGIO'
    TRASPORTO_NON_SANITARIO = 'TRASPORTO NON SANITARIO'
    TS = 'TRASPORTO SANITARIO TS (46h)'
    TSS = 'TRASPORTO SANITARIO SEMPLICE TSS (16h)'
    TRUCCATORE = 'TRUCCATORE'
    VESTIARIO = 'VESTIARIO'



def shortenQualifica(qualifica: QualificaType) -> str:
    if qualifica == QualificaType.aff_CENTRALINISTA:
        return 'Aff. C'
    elif qualifica == QualificaType.aff_SOCC:
        return 'Aff. S'
    elif qualifica == QualificaType.aff_TS:
        return 'Aff. TS'
    elif qualifica == QualificaType.aff_TSS:
        return 'Aff. TSS'
    elif qualifica == QualificaType.AMMINISTRAZIONE:
        return qualifica
    elif qualifica == QualificaType.ASSEMBLEA_SOCI:
        return qualifica
    elif qualifica == QualificaType.AUDITORE_CONSIGLIO_DIRETTIVO:
        return qualifica
    elif qualifica == QualificaType.AUDITORE_DIREZIONE_SERVIZI:
        return qualifica
    elif qualifica == QualificaType.AUTISTA_A:
        return 'A'
    elif qualifica == QualificaType.AUTISTA_A1:
        return 'A1'
    elif qualifica == QualificaType.AUTISTA_A2:
        return 'A2'
    elif qualifica == QualificaType.AUTISTA_A3:
        return 'A3'
    elif qualifica == QualificaType.AUTISTA_A4:
        return 'A4'
    elif qualifica == QualificaType.AUTISTA_A5:
        return 'A5'
    elif qualifica == QualificaType.AUTISTA_SP:
        return qualifica
    elif qualifica == QualificaType.BLSD_SSE:
        return qualifica
    elif qualifica == QualificaType.BLSD_TS:
        return qualifica
    elif qualifica == QualificaType.BLSD_TSS:
        return qualifica
    elif qualifica == QualificaType.CENTRALINISTA:
        return 'C'    
    elif qualifica == QualificaType.CONSIGLIO_DIRETTIVO:
        return qualifica
    elif qualifica == QualificaType.DIREZIONE_SERVIZI:
        return qualifica
    elif qualifica == QualificaType.FORMAZIONE_AUTISTA:
        return qualifica
    elif qualifica == QualificaType.FORMAZIONE_SOCCORRITORE:
        return qualifica
    elif qualifica == QualificaType.LAVANDERIA:
        return qualifica
    elif qualifica == QualificaType.GESTIONE_TURNI_SERVIZI:
        return qualifica
    elif qualifica == QualificaType.MANUTENZIONE_AUTOMEZZI:
        return qualifica
    elif qualifica == QualificaType.MANUTENZIONE_DAE:
        return qualifica
    elif qualifica == QualificaType.MANUTENZIONE_IT:
        return qualifica
    elif qualifica == QualificaType.MANUTENZIONE_SEDE:
        return qualifica
    elif qualifica == QualificaType.MATERIALE_SANITARIO:
        return qualifica
    elif qualifica == QualificaType.MEDICO:
        return qualifica
    elif qualifica == QualificaType.PATENTE_B:
        return qualifica
    elif qualifica == QualificaType.RIUNIONE_ESTERNA:
        return qualifica
    elif qualifica == QualificaType. RIUNIONE_INTERNA:
        return qualifica
    elif qualifica == QualificaType.SERVIZIO_ALLA_PERSONA:
        return qualifica
    elif qualifica == QualificaType.SERVIZIO_CIVILE:
        return qualifica
    elif qualifica == QualificaType.SERVIZIO_EMERGENZA:
        return qualifica
    elif qualifica == QualificaType.SERVIZIO_GARA:
        return qualifica
    elif qualifica == QualificaType.SERVIZIO_INTERNO:
        return qualifica
    elif qualifica == QualificaType.SOCC:
        return 'SE'
    elif qualifica == QualificaType.SOCC_CAPO:
        return 'CAP'
    elif qualifica == QualificaType.TRASPORTO_NON_SANITARIO:
        return qualifica
    elif qualifica == QualificaType.TS:
        return 'TS'
    elif qualifica == QualificaType.TSS:
        return 'TSS'
    elif qualifica == QualificaType.TRUCCATORE:
        return qualifica
    elif qualifica == QualificaType.VESTIARIO:
        return qualifica
    else:
        raise Exception("Received qualifica not supported")