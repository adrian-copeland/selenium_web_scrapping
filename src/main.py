import utils_etl as etl
#from src import utils_scrapping as scrapp

import warnings
warnings.filterwarnings("ignore", category=UserWarning, module="openpyxl")

def run():
    folder_downloads = './../lists_downloaded'
    table_all_stores = './../EnterpriseSummary_111225_169.xlsx'
    final_path = './../results/'
    hours_considered = 1
    etl.online_offline_process(
        folder_connectplus_downloads_path=folder_downloads, 
        table_all_stores_path=table_all_stores, 
        final_storage_path=final_path,
        N=hours_considered)
    print('Procees successfull!')


if __name__ == "__main__":
    run()    