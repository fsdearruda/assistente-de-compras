# Assistente de compras

Utiliza da api do [Nordestão](https://www.nordestao.com.br/?redirect) para obter os preços dos produtos na sua lista do [Google Keep](https://www.google.com/keep/) e calcular uma estimativa do valor total da compra.

O valor estimado é exibido no final da lista como um item marcado como concluído.

## Logs

Os logs são salvos no arquivo `items.json` na pasta `/logs` neste formato:

```json
[
  {
    "termo": "string", // Nome do item na lista do Google Keep
    "descricao": "string", // Descrição do item encontrado no Nordestão
    "quantidade": "int", // Quantidade do item na lista do (se especificado)
    "preco": "float", // Preço do item encontrado no Nordestão
    "total": "float", // Preço total do item (preco * quantidade)
    "em_oferta": "boolean", // Se o item está em oferta
    "link": "https://www.lojaonline.nordestao.com.br/produtos/detalhe/{product_id}" // Link do item encontrado no Nordestão
  },
    ...
]
```

## Dependências

- [Python 3](https://www.python.org/downloads/)
- [requests](https://requests.readthedocs.io/en/latest/)
- [tqdm](https://github.com/tqdm/tqdm/)
- [json](https://docs.python.org/3/library/json.html)
- [gkeepapi](https://github.com/kiwiz/gkeepapi)

## Instalação

1. Clone o repositório
2. Instale as dependências
3. Adicione o arquivo `config.json` na pasta raiz do projeto
4. Dentro do arquivo `config.json` adicione as seguintes informações:

   ```json
   {
     "email": "~email do google keep~",
     "password": "~senha do google keep~",
     "list_id": "~id da lista do google keep~"
   }
   ```

   Para obter o id da lista, basta acessar o [Google Keep](https://keep.google.com/) e clicar no menu de opções da lista desejada. O id estará na url.

5. Execute o arquivo `main.py`
