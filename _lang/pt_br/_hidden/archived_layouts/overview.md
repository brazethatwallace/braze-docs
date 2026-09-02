---
nav_title: Visão geral
page_order: 0
noindex: true
---

# Exemplo de layout: visão geral

> O layout de visão geral é ideal para criar uma opção de navegação específica na parte superior de uma página, permitindo que os usuários cliquem em um botão para ir a uma parte específica da página ou a uma página completamente diferente.

Exemplos clássicos do layout de seletor são a página de [changelogs do SDK]({{site.baseurl}}/developer_guide/changelogs) ou a página de [detalhes de criativos de In-App Messages]({{site.baseurl}}/user_guide/channels/in_app_messages/message_types).

## Componentes obrigatórios

1. Notação de abertura e fechamento YAML. Em outras palavras, --- antes do conteúdo e --- depois.
2. Aspas ao redor de determinados conteúdos de parâmetro. (Parâmetros de cabeçalho, parâmetros de texto, conteúdo com hifens ou outros caracteres especiais.)
3. Notação de tags de glossário (são tags de filtro)

## Parâmetros obrigatórios

| Parâmetro | Tipo de conteúdo | Detalhes |
|---|---|---|
| `page_order` | numérico | Ordena a página dentro da seção. Essa ordem será refletida na navegação à esquerda. |
| `nav-title` | Alfanumérico | Título que aparecerá na navegação à esquerda. |
| `layout` | Alfanumérico - Sem espaços | Selecione um layout na [seção de layouts](https://github.com/Appboy/braze-docs/tree/develop/_layouts) da documentação. |
| `guide_top_header` | Alfanumérico | Dê um título à sua página. |
| `guide_top_text` | Alfanumérico | Descreva sua página. Esse texto aparecerá logo acima dos botões e de seus títulos. É necessário usar aspas ao redor do conteúdo. |
| `guide_featured_title` | Alfanumérico | Dê um título aos seus cartões. Ele aparecerá logo acima dos botões. |
| `guide_featured_list` | YAML adicional, Alfanumérico | Consulte [Formato de listagem do guia](#guide-listing-format) abaixo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Parâmetros obrigatórios" }

### Formato de listagem do guia {#guide-listing-format}

| Parâmetro | Tipo de conteúdo | Detalhes |
|---|---|---|
| `name` | Alfanumérico | Dê um nome à caixa. |
| `link` | URL ou caminho | Link para onde a caixa direcionará. Deve conter a URL completa ou (se for um link interno) `/docs...` |
| `image` | Caminho | Link para a localização da imagem. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Formato de listagem do guia" }

Exemplo de formato:

```yaml
- name: Modal
  link: /docs/user_guide/channels/in_app_messages/message_types/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
```

```yaml
---
nav_title: Detalhes criativos
page_order: 4
layout: featured
guide_top_header: "Detalhes criativos"
guide_top_text: "Seja criativo com suas mensagens no app! Mas primeiro, conheça algumas diretrizes! Afinal, você precisa conhecer as regras para poder quebrá-las! Confira as especificações criativas de cada tipo de mensagem ou os detalhes criativos gerais abaixo."

guide_featured_title: "Especificações criativas por tipo de mensagem"
guide_featured_list:
- name: Modal
  link: /docs/user_guide/channels/in_app_messages/message_types/#modal
  image: /assets/img/braze_icons/layout-alt-01.svg
- name: Slideup
  link: /docs/user_guide/channels/in_app_messages/message_types/#slideup
  image: /assets/img/braze_icons/arrow-circle-broken-up.svg
- name: Tela inteira
  link: /docs/user_guide/channels/in_app_messages/message_types/#full-screen
  image: /assets/img/braze_icons/expand-05.svg
---

# Detalhes criativos {#general}

As mensagens no app da Braze possuem especificações criativas globais e individuais. Para saber mais sobre nossos tipos de mensagens no app mais personalizáveis, acesse nossa página [Personalizar]({{ site.baseurl }}/user_guide/message_building_by_channel/in-app_messages/customize/).

{% alert important %}
  Esses detalhes se aplicam apenas à nossa geração mais recente de mensagens no app (Geração 3). Se você não está usando a geração mais recente de mensagens no app, confira nossa documentação sobre [gerações anteriores de mensagens no app]({{ site.baseurl }}/help/best_practices/in-app_messages/previous_in-app_message_generations/).
{% endalert %}