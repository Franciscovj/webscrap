# Web Scraping para Dados de Jogadores

Este projeto realiza a extração de dados de uma página web contendo informações sobre jogadores, usando Selenium e BeautifulSoup. Os dados extraídos são salvos em um arquivo Excel para posterior análise.

## URL do Projeto

O script está configurado para extrair dados da seguinte URL:

[Serie A Estatísticas](https://fbref.com/pt/comps/24/stats/Serie-A-Estatisticas)

## Pré-requisitos

Certifique-se de que você tem os seguintes pacotes instalados:

- `pandas`
- `selenium`
- `beautifulsoup4`
- `webdriver_manager`
- `openpyxl` (para salvar o arquivo Excel)

Você pode instalar esses pacotes usando `pip`:

```bash
pip install pandas selenium beautifulsoup4 webdriver_manager openpyxl
