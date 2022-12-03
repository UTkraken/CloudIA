import pandas as pd


def get_total_jobs():
    df_jobs = pd.read_excel('./static/1039_sdes_emplois_economie_maritime_2017.xlsx', 'nbr_emplois_domaine')
    nb_jobs = df_jobs['Métropole'].sum()
    df_med_jobs = pd.read_excel('./static/1039_sdes_emplois_economie_maritime_2017.xlsx', 'nbr_emplois_ZELitto')
    med_jobs = df_med_jobs[(df_med_jobs['Façade'] == 'ZE littorales Méditerranée')]
    med_jobs = med_jobs['Total emplois']
    df_paca_jobs = pd.read_excel('./static/1039_sdes_emplois_economie_maritime_2017.xlsx', 'nbr_emplois_domaine_region')
    paca_jobs = df_paca_jobs[(df_paca_jobs['Région'] == 'PACA')]
    paca_jobs_count = paca_jobs['Emplois'].sum()
    paca_domains = paca_jobs['Domaine'].drop_duplicates()

    info = {
        'nb_jobs': nb_jobs,
        'mde_jobs': med_jobs,
        'paca_jobs_count': paca_jobs_count
    }

    return info