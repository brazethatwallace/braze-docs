---
nav_title: Obter dados do perfil de usuário
article_title: Obter dados do perfil de usuário em chamadas de Conteúdo conectado
page_order: 3
description: "Este artigo aborda como obter perfis de usuário em chamadas de Conteúdo conectado e as práticas recomendadas envolvendo modelos Liquid."
toc_headers: h2
---

# Obter dados do perfil de usuário em chamadas de Conteúdo conectado

> Esta página aborda como obter perfis de usuário em chamadas de Conteúdo conectado e as práticas recomendadas envolvendo modelos Liquid.

## Pré-requisitos

Se uma resposta de Conteúdo conectado contiver campos do perfil de usuário (dentro de uma tag de personalização Liquid), esses valores devem ser definidos anteriormente na mensagem com Liquid, antes da chamada de Conteúdo conectado, para que o retorno do Liquid seja renderizado corretamente. Da mesma forma, a flag `:rerender` deve ser incluída na requisição. A flag `:rerender` funciona apenas em um nível de profundidade, ou seja, ela não se aplica a tags de Conteúdo conectado aninhadas.

## Modelos Liquid em chamadas de Conteúdo conectado

Para personalização, a Braze obtém os campos do perfil de usuário antes de passá-los para o Liquid. Portanto, se a resposta do Conteúdo conectado contiver campos do perfil de usuário, eles devem ser definidos previamente.

Por exemplo, se esta fosse a chamada de Conteúdo conectado:
{% raw %}
```liquid
Hi ${first_name},
{% connected_content https://examplewebsite.com :rerender %}
```
{% endraw %}

A resposta do Conteúdo conectado é {% raw %}`Your language is ${language}`{% endraw %}. O conteúdo exibido neste exemplo é `Hi Jon, your language is`.

O idioma em si não será processado pelo modelo. Isso acontece porque a Braze precisa saber quais campos recuperar do usuário antes de fazer a chamada de Conteúdo conectado.

Para renderizar o retorno do Liquid corretamente, você deve incluir a tag {% raw %}`${language}`{% endraw %} em qualquer lugar da requisição, conforme mostrado no trecho de código a seguir. O pré-processador Liquid saberá que deve buscar o atributo "language" do usuário para tê-lo pronto para o processamento do modelo na resposta.

{%raw%}
```liquid
Hi ${first_name}, {% connected_content https://examplewebsite.com?language=${language} :rerender %}
```
{% endraw %}

{% alert important %}
Lembre-se de que a opção da flag `:rerender` funciona apenas em um nível de profundidade. Se a resposta do Conteúdo conectado contiver mais tags de Conteúdo conectado ou tags de Catálogo, a Braze não renderizará novamente essas tags adicionais.
{% endalert %}

## Práticas recomendadas

### Use `json_escape` com tags Liquid que possam quebrar o formato JSON

Ao usar `:rerender`, adicione o filtro `json_escape` a qualquer tag Liquid que possa potencialmente quebrar o formato JSON. Se suas tags Liquid contiverem caracteres que quebram o formato JSON, toda a resposta do Conteúdo conectado será interpretada como texto e inserida na mensagem como modelo, e nenhuma das variáveis será salva.

Por exemplo, se a propriedade de evento `message` no exemplo abaixo contiver caracteres que possam quebrar o formato JSON, adicione o filtro `json_escape` como neste exemplo:

{% raw %}
```liquid
[{
"message":"{{event_properties.${message} | json_escape}}"
}]
```
{% endraw %}