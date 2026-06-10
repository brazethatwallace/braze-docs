---
nav_title: Transifex
article_title: Transifex
alias: /partners/transifex/
description: "Este artigo de referência descreve a parceria entre a Braze e a Transifex, uma plataforma de localização que permite automatizar a tradução, liberando suas equipes para se concentrarem em oferecer experiências brilhantes aos clientes."
page_type: partner
search_tag: Partner

---

# Transifex

> A [Transifex](https://www.transifex.com/) possibilita uma localização robusta em toda a sua base de usuários, independentemente do idioma.

_Essa integração é mantida pela Transifex._

## Sobre a integração {#about-the-integration}

A integração da Braze com a Transifex usa Conteúdo conectado para permitir que você extraia uma coleção de strings de recursos e inclua traduções relevantes em suas mensagens, em vez de linhas de formatação condicional baseada em idioma. Isso automatiza a tradução e libera suas equipes para se concentrarem em oferecer experiências brilhantes aos clientes.

{% alert important %}
Em 7 de abril de 2022, a Transifex descontinuou as versões 2 e 2.5 da sua API para abrir caminho para a versão 3. As versões v2 e v2.5 não estão mais operacionais, e as solicitações feitas a elas apresentarão falhas. <br><br>As instruções de integração a seguir refletem a atualização da versão 3. Atualize suas chamadas de Conteúdo conectado de acordo.
{% endalert %}

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Conta Transifex | Uma [conta Transifex](https://www.transifex.com/signin/) é necessária para aproveitar esta parceria. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

A integração da Transifex usa a [API de traduções de recursos](https://developers.transifex.com/reference/get_resource-translations) da Transifex. O cURL a seguir permitirá que você veja se sua conta tem valores de conteúdo associados a traduções.

Primeiro, insira o `<ORGANIZATION_NAME>`, `<PROJECT_NAME>` e `<RESOURCE_NAME>` encontrados na sua conta da Transifex. Em seguida, substitua `<LANGUAGE>` pelo código do idioma pelo qual você deseja filtrar as traduções e `<TRANSIFEX_BEARER_TOKEN>` pelo seu [bearer token](https://developers.transifex.com/reference/api-authentication) da Transifex.

```
curl --request GET \
     --url 'https://rest.api.transifex.com/resource_translations?filter\[resource\]=o:<ORGANIZATION_NAME>:p:<PROJECT_NAME>:r:<RESOURCE_NAME>&filter\[language\]=l:<LANGUAGE>' \
     --header 'Accept: application/vnd.api+json' \
     --header 'Authorization: Bearer 1/<TRANSIFEX_BEARER_TOKEN>'
```

Por exemplo, se seu projeto Transifex estiver localizado em `https://www.transifex.com/appboy-3/french2/french_translationspo/`, o `project_name` será "french2" e o `resource_name` será "french_translationspo".

## Exemplo de mensagem de Conteúdo conectado {#connected-content-message-example}

Este trecho de código de exemplo utiliza a API de tradução de recursos da Transifex e o atributo `language` do usuário. Com base nas suas necessidades, você pode percorrer os objetos string e obter o conteúdo relevante usando o seguinte Liquid: `{{strings.data[X].attributes.strings.other}}`.

{% raw %}
```
{% assign organization = "<ORGANIZATION_NAME>" %}
{% assign project = "<PROJECT_NAME>" %}
{% assign resource = "<RESOURCE_NAME>" %}

{% if {{${language}}} == "en" or {{${language}}} == "it" or {{${language}}} == "de" or {{${language}}} == "another_language_you_support"  %}
{% connected_content
     https://rest.api.transifex.com/resource_translations?filter[resource]=o:{{organization}}:p:{{project}}:r:{{resource}}&filter[language]=l:{{${language}}}
     :method GET
     :headers {
       "Authorization": "Bearer <TRANSIFEX_BEARER_TOKEN>"
  }
     :accept application/vnd.api+json
     :save strings
%}
{% endif %}

{% if {{strings}} != null and {{strings.data[0].attributes.strings.other}} != "" and {{${language}}} != null %}
  {{strings.data[0].attributes.strings.other}}
{% else %}
  {% abort_message('null or blank') %}
{% endif %}
```
{% endraw %}


[16]: [success@braze.com](mailto:success@braze.com)