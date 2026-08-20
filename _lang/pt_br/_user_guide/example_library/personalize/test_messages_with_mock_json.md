---
nav_title: Testar mensagens com JSON simulado
article_title: Testar mensagens com JSON simulado na prévia
page_order: 1
page_type: reference
description: "Use capture e json_parse do Liquid para simular Connected Content ou JSON de entrada no criador de mensagem sem precisar lançar uma Campaign ou enviar mensagens de teste."
---

# Testar mensagens com JSON simulado na prévia {#test-messages-with-mock-json-in-preview}

> Simule JSON de API ou de entrada dentro da sua mensagem com `capture` e `json_parse` para validar o Liquid e o layout na prévia do criador antes de lançar uma Campaign, disparar um Canvas ou chamar o Connected Content em tempo real.

## Sobre este exemplo {#about-this-example}

A Flash & Thread, uma marca fictícia de varejo de roupas, cria mensagens que dependem de respostas de Connected Content, variáveis de contexto do Canvas ou dados de perfil em array de objetos. Disparar chamadas de API reais ou lançar Campaigns a cada iteração torna o desenvolvimento mais lento.

Esse padrão incorpora uma carga útil JSON simulada no corpo da mensagem, armazena-a com `capture` e depois a analisa com `json_parse` para que o Liquid possa referenciar campos estruturados na seção **Prévia** — sem uma chamada de Connected Content em tempo real, entrada no Canvas disparada por API ou envio de teste.

Use isso durante o desenvolvimento da mensagem. Ele não substitui testes de ponta a ponta com disparos reais, envios de teste ou [prévia de jornadas de usuários]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths) no Canvas.

## Considerações {#considerations}

- Essa abordagem suporta a prévia do criador durante o desenvolvimento. Execute envios de teste e verificações de jornada ao vivo antes de lançar para os clientes.
- Um bloco `capture` sozinho armazena JSON como uma string. Referencie campos somente depois de aplicar **`json_parse`** — caso contrário, a saída da prévia pode ficar em branco.
- O JSON simulado deve ser válido. JSON inválido faz com que `json_parse` falhe ou retorne estruturas inesperadas.
- Substitua ou remova blocos simulados antes do lançamento, ou proteja o Liquid de produção para que os dados simulados sejam usados apenas na prévia (por exemplo, com um sinalizador de comentário que você exclui antes de entrar em produção).
- Os snippets de Liquid neste artigo são exemplos. Teste nos seus canais e com os formatos reais da sua carga útil.
- Para Connected Content em produção, remova o bloco simulado e use sua tag de URL ao vivo. Consulte [Fazendo uma chamada de API]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call).

## Configuração {#setup}

Este exemplo simula uma resposta de listagem de produtos no estilo Connected Content para um e-mail que itera sobre `listings`.

### Etapa 1: Capturar JSON simulado na mensagem {#step-1-capture-mock-json-in-the-message}

Use `capture` para armazenar a string JSON. Use sintaxe JSON válida dentro do bloco (aspas duplas em chaves e valores de string).

{% raw %}
```liquid
{% capture mock_response %}
{
  "success": true,
  "listings": [
    {
      "id": 45731,
      "name": "Summit Trail Jacket",
      "image_url": "https://example.com/images/trail-jacket.png",
      "price": {
        "actual": "89.00",
        "currency": "USD"
      },
      "link": "https://example.com/products/trail-jacket",
      "product_category": "Outerwear",
      "properties": {
        "size": "L",
        "colour": "Navy",
        "limited_edition": false
      },
      "out_of_stock": false
    }
  ]
}
{% endcapture %}
```
{% endraw %}

### Etapa 2: Analisar o JSON com json_parse {#step-2-parse-json-with-json_parse}

Atribua a estrutura analisada a uma variável que você referencia no restante da mensagem.

{% raw %}
```liquid
{% assign response_json = mock_response | json_parse %}
```
{% endraw %}

Sem `json_parse`, a notação de ponto na string capturada (por exemplo, {% raw %}`{{ mock_response.listings }}`{% endraw %}) normalmente renderiza em branco na prévia.

### Etapa 3: Referenciar campos analisados no Liquid {#step-3-reference-parsed-fields-in-liquid}

Itere sobre o array analisado e renderize os campos como faria para uma resposta de API em tempo real.

{% raw %}
```liquid
{% for listing in response_json.listings %}
{{ listing.name }} — {{ listing.price.actual }} {{ listing.price.currency }}
{% endfor %}
```
{% endraw %}

Acesse a seção **Prévia** no criador de mensagem e confirme se os campos são renderizados.

### Etapa 4: Aplicar o mesmo padrão a outras estruturas JSON {#step-4-apply-the-same-pattern-to-other-json-shapes}

Use o mesmo fluxo de `capture` + `json_parse` para simular:

| Dados que você quer testar | Estrutura JSON simulada |
| --- | --- |
| Variáveis de contexto do Canvas | Objeto com as chaves de propriedade que sua mensagem espera |
| Array de objetos em um perfil | Array JSON de objetos com as mesmas chaves do seu atributo personalizado |
| Resposta de Connected Content | JSON de API de exemplo salvo de uma chamada anterior bem-sucedida |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Dados que você quer testar e estrutura JSON" }

Substitua as variáveis simuladas por Liquid de produção (variáveis de contexto do Canvas, atributos personalizados ou tags de Connected Content) antes de lançar.

## Artigos relacionados {#related-articles}

- [Enviar mensagens de teste]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages)
- [Prévia de jornadas de usuários no Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/preview_user_paths)
- [Filtros avançados de Liquid (`json_parse`)]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/advanced_filters)
- [Connected Content]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content)
- [Array de objetos]({{site.baseurl}}/user_guide/data/activation/attributes/array_of_objects)
- [Variáveis de contexto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables)