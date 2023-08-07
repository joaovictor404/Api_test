import requests
from django.http import JsonResponse
from django.shortcuts import render

def mostrar_dados_api(request):
    # URL da API que você deseja usar
    api_url = 'https://servicodados.ibge.gov.br/api/v3/agregados/482/periodos/-6/variaveis/96|1000096?localidades=N1[all]&classificacao=293[0]|1[0]'
    # Fazendo a requisição à API e obtendo os dados em formato JSON
    response = requests.get(api_url)
    data = response.json()

    # Renderiza o template e passa os dados para o template
    return render(request, 'api/templates.html', {'dados_api': data})

def ibge_data_view(request):
    # Fazer a chamada à API do IBGE para obter dados populacionais do Brasil
    url = 'https://servicodados.ibge.gov.br/api/v3/agregados/482/periodos/-6/variaveis/96|1000096?localidades=N1[all]&classificacao=293[0]|1[0]'
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
    else:
        # Em caso de falha na chamada à API, podemos retornar uma mensagem de erro
        data = {
            "error": "Erro ao acessar a API do IBGE"
        }

    # Retornar a resposta JSON
    return JsonResponse(data, safe=False)