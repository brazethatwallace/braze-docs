---
nav_title: Visão geral
page_order: 0
noindex: true
---

# Exemplo de layout: Visão geral {#example-layout-overview}

> O layout de visão geral é ideal para criar uma opção de navegação específica na parte superior de uma página, permitindo que os usuários cliquem em um botão para ir a uma parte específica da página ou a uma página completamente diferente.

Exemplos clássicos do layout de seletor são a página de [changelogs do SDK]({{site.baseurl}}/developer_guide/changelogs/) ou a página de [detalhes de criativos da mensagem no app]({{site.baseurl}}/user_guide/message_building_by_channel/in-app_messages/creative_details/).

## Componentes necessários {#required-components}

1. Notação de abertura e fechamento do YAML. Em outras palavras, --- antes do conteúdo e --- depois.
2. Aspas em torno de determinados conteúdos de parâmetros. (Parâmetros de cabeçalho, parâmetros de texto, conteúdo com hífens ou outros caracteres especiais.)
3. Notação das tags do glossário (essas são tags de filtro)

## Parâmetros necessários {#required-parameters}

| Parâmetro | Tipo de conteúdo | Informações |
|---|---|---|
| `page_order` | Numérico | Ordene a página dentro da seção. Essa ordem será refletida na navegação à esquerda. |
| `nav-title` | Alfanumérico | Título que aparecerá na navegação à esquerda. |
| `layout` | Alfanumérico - Sem espaços | Selecione um layout na [seção de layout](https://github.com/Appboy/braze-docs/tree/develop/_layouts) da documentação. |
| `guide_top_header` | Alfanumérico | Dê um título à sua página. |
| `guide_top_text` | Alfanumérico | Descreva sua página; isso será exibido diretamente acima dos botões e de seu título. São necessárias aspas em torno do conteúdo. |
| `guide_featured_title` | Alfanumérico | Dê um título aos seus cartões. Ele ficará diretamente acima dos botões.
| `guide_featured_list` | Mais YAML, alfanumérico | Consulte o [formato de listagem do guia](#guide-listing-format) abaixo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Parâmetros necessários" }

### Formato de listagem do guia {#guide-listing-format}

| Parâmetro | Tipo de conteúdo | Informações |
|---|---|---|
| `name` | Alfanumérico | Dê um nome à caixa. |
| `link` | URL ou caminho | Link de destino da caixa. Deve conter o URL completo ou (se for um link interno) `/docs...` |
| `image` | Caminho | Link do local da imagem. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Formato de listagem do guia" }

Exemplo de formato:

```yaml
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
```

## Exemplo {#example}

```yaml
---
nav_title: Creative Details
page_order: 4
layout: featured
guide_top_header: "Creative Details"
guide_top_text: "Get creative with our in-app messages! But you should know some of the guidelines, first! After all, you have to know those rules to break them! Check out the individual message type's Creative Specs or the global Creative Details below."

guide_featured_title: "Message Type Creative Specs"
guide_featured_list:
- name: Modal
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: Slideup
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#slideup
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: Full-Screen
  link: /docs/user_guide/message_building_by_channel/in-app_messages/creative_details/#full-screen
  image: /assets/img/braze_icons/expand-05.svg
---

# Creative Details {#general}

Braze in-app messages have both global and individual creative specifications. For more information on our more customizable in-app message types, go to our [Customize]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/) page.

{% alert important %}
  These details only apply to our most recent in-app message generation (Generation 3). If you are not using our newest generation of in-app messages, check out our [previous in-app message generations]({{ site.baseurl }}/help/best_practices/in-app_messages/previous_in-app_message_generations/) documentation.
{% endalert %}
```
