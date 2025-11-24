import requests
import os
from tqdm import tqdm

def criar_diretorio_se_nao_existir(path):
    if not os.path.exists(path):
        print(f"Criando diretório: {path}")
        os.makedirs(path)

def baixar_arquivo(url, destino):
    if os.path.exists(destino):
        print(f"Arquivo já existe, pulando download: {os.path.basename(destino)}")
        return True
        
    print(f"Baixando de {url} para {destino}...")
    try:
        with requests.get(url, stream=True, timeout=120) as r:
            r.raise_for_status()
            total_size_in_bytes = int(r.headers.get('content-length', 0))
            block_size = 1024
            progress_bar = tqdm(total=total_size_in_bytes, unit='iB', unit_scale=True, desc=os.path.basename(destino))
            with open(destino, 'wb') as f:
                for chunk in r.iter_content(block_size):
                    progress_bar.update(len(chunk))
                    f.write(chunk)
            progress_bar.close()
            if total_size_in_bytes != 0 and progress_bar.n != total_size_in_bytes:
                print("ERRO: Algo deu errado durante o download.")
                return False
        return True
    except requests.exceptions.RequestException as e:
        print(f"Erro ao baixar {url}: {e}")
        return False

def baixar_proposicoes_votadas_csv(anos):
    URL_BASE = "https://dadosabertos.camara.leg.br/arquivos/"
    DIR_DADOS_BRUTOS = "votacoesVotos"
    criar_diretorio_se_nao_existir(DIR_DADOS_BRUTOS)

    print("\n--- BAIXANDO ARQUIVOS CSV DE DADOS ---")
    for ano in anos:
        # Download de Votações CSV
        url_votacoes = f"{URL_BASE}votacoes/csv/votacoes-{ano}.csv"
        destino_votacoes = os.path.join(DIR_DADOS_BRUTOS, f"votacoes-{ano}.csv")
        baixar_arquivo(url_votacoes, destino_votacoes)

        # Download de Proposições CSV
        url_proposicoes = f"{URL_BASE}proposicoes/csv/proposicoes-{ano}.csv"
        destino_proposicoes = os.path.join(DIR_DADOS_BRUTOS, f"proposicoes-{ano}.csv")
        baixar_arquivo(url_proposicoes, destino_proposicoes)

        # Download de VotaçõesVotos CSV
        url_votacoes_votos = f"{URL_BASE}votacoesVotos/csv/votacoesVotos-{ano}.csv"
        destino_votacoes_votos = os.path.join(DIR_DADOS_BRUTOS, f"votacoesVotos-{ano}.csv")
        baixar_arquivo(url_votacoes_votos, destino_votacoes_votos)

if __name__ == "__main__":
    ANOS_DE_INTERESSE = range(2019, 2023)
    baixar_proposicoes_votadas_csv(ANOS_DE_INTERESSE)