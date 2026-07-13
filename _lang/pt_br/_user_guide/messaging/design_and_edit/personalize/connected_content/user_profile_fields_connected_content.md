---
nav_title: Puxando dados do perfil do usuário
article_title: Puxar dados do perfil do usuário em chamadas de Connected Content
page_order: 3
description: "Este artigo aborda como puxar perfis de usuários em suas chamadas de Connected Content e melhores práticas envolvendo modelagem Liquid."
toc_headers: h2
---

# Puxar dados do perfil do usuário em chamadas de Connected Content {#pull-user-profile-data-in-connected-content-calls}

> Esta página aborda como puxar perfis de usuário para suas chamadas de Connected Content e as melhores práticas envolvendo a modelagem Liquid.

## Pré-requisitos {#prerequisites}

Se uma resposta de Connected Content contiver campos do perfil de usuário (dentro de uma tag de personalização Liquid), esses valores devem ser definidos anteriormente na mensagem com Liquid, antes da chamada de Connected Content, para que o retorno do Liquid seja renderizado corretamente. Da mesma forma, a flag `:rerender` deve ser incluída na requisição. A flag `:rerender` funciona apenas em um nível de profundidade, ou seja, ela não se aplica a tags de Connected Content aninhadas.

## Modelagem Liquid em chamadas de Connected Content {#liquid-templating-in-connected-content-calls}

Para personalização, a Braze obtém os campos do perfil de usuário antes de passá-los para o Liquid. Portanto, se a resposta do Connected Content contiver campos do perfil de usuário, eles devem ser definidos previamente.

Por exemplo, se esta fosse a chamada de Connected Content:
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}

A resposta do Connected Content é {% raw %}`Your language is ${language}`{% endraw %}. O conteúdo exibido neste exemplo é `Hi Jon, your language is`.

O idioma em si não será processado pelo modelo. Isso acontece porque a Braze precisa saber quais campos recuperar do usuário antes de fazer a chamada de Connected Content.

Para renderizar o retorno do Liquid corretamente, você deve incluir a tag {% raw %}`${language}`{% endraw %} em qualquer lugar da requisição, conforme mostrado no trecho de código a seguir. O pré-processador Liquid saberá que deve buscar o atributo "language" do usuário para tê-lo pronto para a modelagem da resposta.

{%raw%}
```liquid
Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}

{% alert important %}
Lembre-se de que a opção da flag `:rerender` funciona apenas em um nível de profundidade. Se a resposta do Connected Content contiver mais tags de Connected Content ou tags de catálogo, a Braze não renderizará novamente essas tags adicionais.
{% endalert %}

## Melhores práticas {#best-practices}

### Use `json_escape` com tags Liquid que possam quebrar o formato JSON {#use-json_escape-with-liquid-tags-that-could-break-the-json-format}

Ao usar `:rerender`, adicione o filtro `json_escape` a qualquer tag Liquid que possa potencialmente quebrar o formato JSON. Se suas tags Liquid contiverem caracteres que quebram o formato JSON, toda a resposta do Connected Content será interpretada como texto e inserida na mensagem, e nenhuma das variáveis será salva.

Por exemplo, se a propriedade de evento `message` no exemplo da seção a seguir contiver caracteres que possam quebrar o formato JSON, adicione o filtro `json_escape` como neste exemplo:

{% raw %}
```liquid
[{
"message":"{{event_properties.${message} | json_escape}}"
}]
```
{% endraw %}