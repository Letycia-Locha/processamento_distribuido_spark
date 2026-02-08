import requests

# URL de dados abertos da CVM (Informações diárias de fundos)
# Este é um link direto para o arquivo CSV de um dia específico
url = "https://dados.cvm.gov.br/dados/FI/DOC/INF_DIARIO/DADOS/inf_diario_fi_202401.zip"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

try:
    print("Iniciando download dos dados da CVM...")
    response = requests.get(url, headers=headers, stream=True)
    response.raise_for_status()

    with open("dados_cvm_raw.zip", "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
            
    print("✅ Arquivo dados_cvm_raw.zip baixado com sucesso!")

except Exception as e:
    print(f"❌ Erro ao baixar dados da CVM: {e}")