import pandas as pd
from src.modules.scrap import PlayersInfo

url = 'https://fbref.com/pt/comps/24/stats/Serie-A-Estatisticas'


players_info = PlayersInfo(url)

players_info.extract_fbre_data()

df = pd.read_excel('data/players.xlsx')


termos_para_remover = ['Class.', 'Jogador', 'Nação', 'Pos.', 'Equipe', 'Idade', 'Nascimento', 'MP', 'Inícios', 
                       'Min.', '90s', 'Gols', 'Assis.', 'G+A', 'G-PB', 'PB', 'PT', 'CrtsA', 'CrtV', 'xG']


df = df[~df.apply(lambda row: row.astype(str).isin(termos_para_remover).any(), axis=1)]

df.columns = df.columns.str.replace(r'Unnamed: \d+_level_\d+_', '', regex=True)
df.columns = df.columns.str.split('_').str[-1]


df.to_excel('dados_tratados.xlsx', index=False)


