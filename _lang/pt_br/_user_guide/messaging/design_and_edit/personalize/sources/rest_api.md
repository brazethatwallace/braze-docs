---
nav_title: API REST
article_title: API REST
page_order: 1
description: "Saiba como usar o Conteúdo conectado para buscar dados de APIs REST e inseri-los nas suas mensagens para personalização em tempo real."
---

# API REST {#rest-api}

> Busque dados de APIs REST externas diretamente nas suas mensagens no momento do envio usando o [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content). Isso permite personalizar mensagens com informações em tempo real dos seus próprios servidores, serviços de terceiros ou qualquer endpoint de API acessível publicamente.

## Como funciona {#how-it-works}

{% raw %}
O Conteúdo conectado faz uma requisição HTTP para a URL que você especificar e armazena a resposta para que você possa referenciá-la com Liquid. Adicione uma tag `{% connected_content %}` à sua mensagem, e a Braze chamará o endpoint quando a mensagem for enviada.

```liquid
{% connected_content https://api.example.com/user/{{${user_id}}}/recommendations :save recs %}
We think you'll love {{recs.top_pick}}!
```
{% endraw %}

O Conteúdo conectado suporta requisições GET e POST. A Braze exige que o servidor responda em até dois segundos, então projete seus endpoints para baixa latência.

## Casos de uso comuns {#common-use-cases}

| Caso de uso | Descrição |
| --- | --- |
| Recomendações de produtos | Buscar sugestões personalizadas de produtos a partir de um mecanismo de recomendação |
| Preços ou estoque em tempo real | Exibir preços atuais ou níveis de estoque no momento do envio |
| Conteúdo baseado no clima | Buscar dados meteorológicos locais para adaptar o envio de mensagens |
| Saldo de pontos de fidelidade | Mostrar recompensas ou saldos de conta atualizados |
| Feeds de conteúdo | Inserir as últimas postagens de blog, artigos ou notícias |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Casos de uso comuns" }

## Autenticação {#authentication}

A Braze suporta autenticação básica, autenticação por token e OAuth para requisições de Conteúdo conectado. Você pode armazenar credenciais de forma segura no dashboard da Braze em **Configurações** > **Conteúdo conectado** e referenciá-las nas suas chamadas de API.

Para saber mais, consulte [Fazendo uma chamada de API de Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call#authentication-types).

## Tratamento de erros {#error-handling}

Se o endpoint retornar um erro ou expirar o tempo limite, a Braze renderiza uma string vazia no lugar da resposta do Conteúdo conectado. Você pode detectar falhas verificando se a variável salva é nula e, condicionalmente, abortar a mensagem ou exibir um conteúdo de fallback.

Para saber mais, consulte [Abortando o Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/aborting_connected_content).

## Considerações de desempenho {#performance-considerations}

Como a Braze entrega mensagens em alto volume, seu servidor precisa lidar com milhares de conexões simultâneas. Use cache quando apropriado e defina limites de taxa nas suas mensagens para evitar sobrecarregar endpoints externos.

Para a referência completa do Conteúdo conectado, consulte [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content).