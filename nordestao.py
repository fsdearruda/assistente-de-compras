import requests

auth = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJ2aXBjb21tZXJjZSIsImF1ZCI6ImFwaS1hZG1pbiIsInN1YiI6IjZiYzQ4NjdlLWRjYTktMTFlOS04NzQyLTAyMGQ3OTM1OWNhMCIsImlhdCI6MTY0MjM0NDk4NiwidmVyIjoxLCJjbGllbnQiOm51bGwsIm9wZXJhdG9yIjpudWxsLCJvcmciOiI1MiJ9.ACvJkpRbjOsiuz4SJSdaKAvxAck1jtoqh_AjOxdgydhGyKoKLM1C9YHM2wBjjhikq8VdSnQ_lCcRYQ8bpB4vUg"


def search_term(term, quantity=1):
    res = requests.get(
        f"https://api.lojaonline.nordestao.com.br/v1/loja/buscas/produtos/filial/1/centro_distribuicao/1/termo/{term}/rapida", headers={"Authorization": auth})

    data = res.json().get("data").get("produtos")

    # Caso não encontre o item
    if data == []:
        return None

    # Pegando segundo item da lista porque o primeiro é um item mais caro e irrelevante
    product = data[1]

    return {
        "termo": term,
        "descricao": product.get("descricao"),
        "quantidade": quantity,
        "preco": float(product.get("preco")),
        "total": float(product.get("preco")) * quantity,
        "em_oferta": product.get("em_oferta"),
        "link": 'https://www.lojaonline.nordestao.com.br/produtos/detalhe/' + str(product.get("produto_id"))
    }
