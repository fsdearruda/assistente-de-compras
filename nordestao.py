import requests

auth = "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzUxMiJ9.eyJpc3MiOiJ2aXBjb21tZXJjZSIsImF1ZCI6ImFwaS1hZG1pbiIsInN1YiI6IjZiYzQ4NjdlLWRjYTktMTFlOS04NzQyLTAyMGQ3OTM1OWNhMCIsImlhdCI6MTY0MjM0NDk4NiwidmVyIjoxLCJjbGllbnQiOm51bGwsIm9wZXJhdG9yIjpudWxsLCJvcmciOiI1MiJ9.ACvJkpRbjOsiuz4SJSdaKAvxAck1jtoqh_AjOxdgydhGyKoKLM1C9YHM2wBjjhikq8VdSnQ_lCcRYQ8bpB4vUg"

units = ["mg", "g", "kg"]


def search_term(term, quantity=1):

    if quantity < 1:  # Verificando a quantidade é válida
        quantity = 1

    res = requests.get(
        f"https://api.lojaonline.nordestao.com.br/v1/loja/buscas/produtos/filial/1/centro_distribuicao/1/termo/{term}/rapida", headers={"Authorization": auth})

    data = res.json().get("data").get("produtos")

    # Caso não encontre o item
    if data == []:
        return None

    # Pegando segundo item da lista porque o primeiro é um item mais caro e irrelevante
    product = data[1]

    formatted_product = {
        "termo": term,
        "descricao": product.get("descricao"),
        "quantidade": quantity,
        "unidade": product.get("unidade_sigla"),
        "preco_unidade": float(product.get("preco")),
        "preco": float(product.get("preco")),
        "total": float(product.get("preco")) * quantity,
        "em_oferta": product.get("em_oferta"),
        "link": 'https://www.lojaonline.nordestao.com.br/produtos/detalhe/' + str(product.get("produto_id"))
    }

    if formatted_product.get("unidade") == "KG":

        term_unit = term.split(" ")[-1].lower()

        # Achando a unidade do item
        for unit in units:
            if unit in term_unit:
                term_unit = term_unit.replace(unit, ""), unit
                break

        # Convertendo unidade para kg
        if term_unit[1] == "g":
            term_unit = float(term_unit[0]) / 1000
        elif term_unit[1] == "mg":
            term_unit = float(term_unit[0]) / 1000000

        # Calculando o preço por kg
        newPrice = float(term_unit * product.get("preco_original"))
        # Adicionando o novo preço e total
        formatted_product["preco_unidade"] = product.get("preco_original")
        formatted_product["preco"] = newPrice
        formatted_product["total"] = newPrice * quantity

    return formatted_product
