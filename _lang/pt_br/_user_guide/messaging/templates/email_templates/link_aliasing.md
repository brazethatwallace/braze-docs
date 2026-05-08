---
nav_title: Alias de link
article_title: Alias de link
alias: /link_aliasing/
page_order: 3
description: "Este artigo descreve como o alias de link funciona e fornece exemplos de como seus links ficarão."
channel:
  - email

---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"}Alias de link {#braze-learning-course-imagebuster-assetsimgblicon3png-httpslearningbrazecomlink-aliasing-stylefloatrightwidth120pxborder0-classnoimgborderlink-aliasing}

> Use o alias de link para criar nomes reconhecíveis e gerados pelo usuário para identificar links enviados em mensagens de e-mail da Braze. Esses links ficam disponíveis para redirecionamento de segmentação, disparo baseado em ação e análise de dados de links.

## Sobre o alias de link {#about-link-aliasing}

Com o alias de link, você pode criar nomes gerados pelo usuário para identificar e rastrear links enviados em e-mails. Dessa forma, você pode usar esses aliases de link reconhecíveis nos seus e-mails para rastrear o engajamento e analisar a performance de campanhas, sem precisar referenciar o link completo.

Com o alias de link, você pode:

- **Redirecionar usuários que clicaram em links específicos:** Identificar e direcionar usuários que clicaram em um link.
- **Criar gatilhos baseados em ação:** Enviar um e-mail quando um usuário clicar em um link.
- **Analisar métricas:** Comparar quantos usuários clicaram no Link A versus o Link B.

### Como funciona {#how-it-works}

A Braze identifica links de forma única dentro dos e-mails, adicionando um parâmetro extra chamado `lid` (também conhecido como identificador de link) a cada URL de link. Esse valor `lid` permite que a Braze rastreie, monitore e agregue as interações dos usuários com o link, mesmo que os demais parâmetros da URL sejam diferentes. Isso ajuda a fornecer insights sobre como os usuários interagem com o conteúdo das suas campanhas de e-mail.

Os identificadores de link também serão atualizados se uma campanha de e-mail, um Canvas com mensagem de e-mail ou um Content Block for duplicado.

## Criando um alias de link {#creating-a-link-alias}

Para criar um alias de link, siga estas etapas:

1. Na sua campanha ou componente do Canvas, acesse o corpo do e-mail.
2. Selecione a guia **Link Management**.
3. A Braze gera automaticamente aliases de link padrão exclusivos para cada um dos seus links.
4. Dê um nome ao alias. Os aliases devem ter nomes exclusivos por variante de campanha de e-mail ou componente do Canvas.

Você também pode definir um alias que será usado para referenciar um link específico ao lidar com relatórios ou segmentação.

![Página de Link Management com quatro aliases de link.]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
O alias de link é suportado apenas em atributos `href` dentro de tags de âncora HTML onde é seguro adicionar um parâmetro de consulta. É uma boa prática incluir um ponto de interrogação (?) no final do seu link para que a Braze possa facilmente adicionar o valor `lid`. Sem a adição do valor `lid`, a Braze não reconhecerá a URL para alias de link.
{% endalert %}

## Gerenciando aliases de link {#managing-link-aliases}

Para visualizar todos os seus aliases de link rastreados, faça o seguinte:

1. Acesse **Settings** > **Email Preferences** em **Workspace Settings**.
2. Selecione a guia **Link Aliasing Settings**.

{% alert important %}
Se você estiver usando a [navegação antiga]({{site.baseurl}}/user_guide/administer/personal/the_braze_dashboard/), essas configurações estão em **Manage Settings**.
{% endalert %}

Aqui, você pode classificar, pesquisar e desativar o rastreamento de aliases de link.

![Página de Tracked Link Aliases mostrando aliases de link ativos e inativos associados a várias campanhas.]({% image_buster /assets/img/tracked_aliases.png %})

{% alert tip %}
Use os endpoints [List link alias for campaign]({{site.baseurl}}/get_campaign_link_alias/) e [List link alias for Canvas]({{site.baseurl}}/get_canvas_link_alias/) para extrair o `alias` definido em cada variante de mensagem em uma campanha ou em um componente do Canvas específico de e-mail.
{% endalert %}

A Braze recomenda avaliar os links dentro do e-mail, adicionar modelos de link e fornecer uma convenção de nomenclatura que funcione para fins de segmentação e relatórios. Isso ajuda você a manter o controle de todos os links.

Quando o alias de link está ativado, as mensagens, Content Blocks e modelos de link não são modificados. Quaisquer mensagens existentes que usem modelos de link ou Content Blocks permanecerão iguais. No entanto, quando você atualizar uma mensagem, a marcação de alias de link será aplicada a todos os links, então você precisará reaplicar os modelos de link para que os links fiquem visíveis.

## Como os links são atualizados com o alias de link {#how-links-are-updated-with-link-aliasing}

As tabelas a seguir fornecem exemplos de links no corpo de um e-mail, resultados do alias de link e explicações de como o link original é atualizado com o alias de link.

### Permalink

**Lógica:** A Braze insere um ponto de interrogação (?) e adiciona o primeiro parâmetro de consulta na URL.

| Link no corpo do e-mail    | Link com alias                     |
|-----------------------|----------------------------------------|
| `https://www.braze.com` | `https://www.braze.com?lid=slfdldtqdhdk` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link com mais parâmetros de consulta {#link-with-more-query-parameters}

**Lógica:** A Braze detecta outros parâmetros de consulta e adiciona `lid=` ao final da URL.

| Link no corpo do e-mail                                            | Link com alias                                                             |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| `https://www.braze.com?utm_campaign=retention&utm_source=email` | `https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link HTML {#html-link}

**Lógica:** A Braze reconhece que o link é uma URL e já possui um ponto de interrogação (?) presente, então o parâmetro de consulta `lid` é adicionado após o ponto de interrogação.

| Link no corpo do e-mail                                                | Link com alias                                                                |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link com âncora {#link-with-anchor}

**Lógica:** A Braze espera que a URL use uma estrutura padrão onde as âncoras (#) estão presentes após um ponto de interrogação (?). Como a Braze lê da esquerda para a direita, o ponto de interrogação e o valor `lid` são adicionados antes da âncora.

| Link no corpo do e-mail                               | Link com alias                                                |
|--------------------------------------------------|-------------------------------------------------------------------|
| `https://www.braze.com#bookmark1?utm_source=email` | `https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email` |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

### Link com âncora e tag de captura {#link-with-anchor-and-capture-tag}

**Lógica:** Ao usar o alias de link com URLs que contêm âncoras (#), a Braze espera que a âncora seja colocada após os parâmetros de consulta. Isso significa que o valor `lid` deve ser adicionado **antes** da âncora para o rastreamento adequado, e como a Braze lê a URL da esquerda para a direita, o ponto de interrogação (?) e o `lid` devem vir antes da âncora.

| Link no corpo do e-mail                                                                        | Link com alias                                                                                           |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%}  | {%raw%}`<a href="https://www.braze.com/promotions?lid={{link_alias}}#special-offer">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Rastreando aliases de link {#tracking-link-aliases}

Na guia **Link Management**, selecione quais aliases você deseja que sejam "rastreados" para fins de segmentação e que estejam presentes nos filtros de segmentação. Observe que os aliases rastreados são apenas para fins de segmentação e não terão impacto no rastreamento do seu link para fins de relatórios.

{% alert tip %}
Para rastrear métricas de engajamento de link, certifique-se de que seu link comece com HTTP ou HTTPS. Para desativar o rastreamento de cliques em links específicos, consulte [Links universais e App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/#turning-off-click-tracking-on-a-link-to-link-basis).
{% endalert %}

A Braze permite que você selecione links ilimitados para rastrear, embora você só possa redirecionar usuários com base nos links mais recentes que eles abriram. Os perfis de usuário incluem os 100 links clicados mais recentemente. Por exemplo, se você rastrear 500 links e um usuário clicar em todos os 500, você pode redirecionar ou criar segmentos com base nos 100 links clicados mais recentemente.

![A guia Link Management com dois links selecionados.]({% image_buster /assets/img/link_management_dnd.png %})

{% alert note %}
A Braze rastreia apenas os últimos 100 aliases de link clicados no nível do perfil.
{% endalert %}

### Filtros baseados em ação {#action-based-filters}

Você pode criar mensagens baseadas em ação direcionando qualquer link (rastreado ou não rastreado) ou redirecionar usuários com base em se eles clicaram em um alias em qualquer campanha de e-mail ou componente do Canvas.

![Opções baseadas em ação para direcionar usuários que clicaram em um alias em um componente do Canvas ou interagiram com uma Campaign.]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

### Filtros de segmentação {#segmentation-filters}

Na Braze, se você tiver um alias de link no seu e-mail e um usuário clicar nele, o evento é registrado no perfil do usuário com o alias.

Se você usar o filtro de segmentação "Clicked Alias in Any Campaign or Canvas Step" e depois decidir renomear esse alias de link, os dados de cliques anteriores no perfil do usuário **não** serão atualizados, ou seja, eles ainda mostrarão o alias de link anterior. Portanto, se você direcionar usuários com base no novo alias de link, isso não incluirá os dados do alias de link anterior.

Se você usar o filtro de segmentação "Clicked Alias in Campaign" ou "Clicked Alias in Canvas", ele filtra seus usuários com base em se eles clicaram em um alias específico em uma campanha ou Canvas específico. Se vários usuários compartilharem o mesmo endereço de e-mail e o alias de link for clicado, todos os outros usuários que compartilham o endereço de e-mail terão seus perfis de usuário atualizados. Esses perfis também são atualizados por eventos de entrega e abertura, não apenas por eventos de clique.

Os filtros de segmentação a seguir se aplicam a eventos de clique que são rastreados no momento em que o evento é processado. Isso significa que links não rastreados não removerão dados existentes e rastrear um link não preencherá retroativamente os dados. Para mais detalhes, consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters/).

#### Desrastreando links {#untracking-links}

Desrastrear um link não realocará segmentos existentes com o filtro para o alias não rastreado. Os dados antigos permanecerão nos perfis de usuário até serem substituídos por dados mais recentes.

Links em mensagens arquivadas são automaticamente desrastreados. No entanto, se mensagens arquivadas forem desarquivadas, os links precisarão ser rastreados novamente. Quando aliases de link são rastreados, os relatórios de link são indexados pelo alias em vez de domínios de nível superior ou URLs completas.

Para visualizar todos os links na sua campanha de e-mail e seus respectivos cliques totais, acesse **Message Analytics** > **Email Performance** > **Preview & Heatmap** e selecione o botão **Show Heatmap**.

![Painel de tabela de links por cliques totais com aliases de link e seus cliques totais.]({% image_buster /assets/img/link_alias_total_clicks.png %}){: style="max-width:60%;"}

### Evento de cliques de e-mail {#email-clicks-event}

Se você exportar seus dados de engajamento com Currents, um evento de clique de e-mail será ligeiramente diferente se você tiver o alias de link ativado. Ele terá dois campos adicionais para o [evento de cliques de e-mail]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-clicks-events/) quando o alias de link estiver ativado: `link_id` e `link_alias`.

```json
// Email Click: users.messages.email.Click
{
  "id": (string) unique ID of this event,
  "user_id": (string) Braze user ID of the user,
  "external_user_id": (string) External ID of the user,
  "time": (int) 10-digit UTC time of the event in seconds since the epoch,
  "timezone": (string) IANA time zone of the user at the time of the event,
  "campaign_id": (string) ID of the campaign if from a campaign,
  "campaign_name": (string) name of the campaign,
  "message_variation_id": (string) ID of the message variation if from a campaign,
  "message_variation_name": (string) the name of the message variation if from a campaign,
  "canvas_id": (string) ID of the Canvas if from a Canvas,
  "canvas_name": (string) name of the Canvas,
  "canvas_variation_id": (string) ID of the Canvas variation the user is in if from a Canvas,
  "canvas_variation_name": (string) name of the Canvas variation the user is in if from a Canvas,
  "canvas_step_id": (string) ID of the step for this message if from a Canvas,
  "canvas_step_name": (string) name of the step for this message if from a Canvas,
  "send_id": (string) ID of the message if specified for the campaign (See Send Identifier under API Identifier Types),
  "dispatch_id": (string) ID of the message dispatch (unique ID for each 'transmission' sent from the Braze platform). Users who are sent a schedule message get the same dispatch_id. Action-based or API-triggered messages get a unique dispatch_id per user.,
  "email_address": (string) email address for this event,
  "url": (string) the URL that was clicked (Email Click events only),
  "user_agent": (string) description of the user's system and browser for the event (Email Click and Open events only),
  "ip_pool": (string) IP pool used for message sending,
  "link_id": (string) unique value generated by Braze for the URL,
  "link_alias": (string) alias name set when the message was sent
}
```

{% alert update %}
O comportamento do `dispatch_id` difere entre Canvas e Campaigns porque a Braze trata as etapas do Canvas (exceto as etapas de entrada, que podem ser agendadas) como eventos disparados, mesmo quando são "agendadas". Saiba mais sobre o [comportamento do `dispatch_id`]({{site.baseurl}}/help/help_articles/data/dispatch_id/) em Canvas e Campaigns.

_Atualização registrada em agosto de 2019._
{% endalert %}

## Alias de link em Content Blocks {#link-aliasing-in-content-blocks}

Novos Content Blocks terão seus links modificados, onde a Braze adicionará um `lid={{placeholder}}` a cada link quando aplicável. Esse valor de placeholder é resolvido quando inserido em uma variante de mensagem de e-mail.

Para modificar os links dentro de Content Blocks existentes que foram criados antes da Braze ativar o alias de link, duplique os Content Blocks existentes e depois modifique os links dentro dos Content Blocks duplicados.

Quando um Content Block sem um valor `lid` é inserido em uma nova mensagem, os links desse Content Block não são rastreados com um alias. Quando um novo Content Block é inserido em uma variante de mensagem "antiga", os links dessa variante de mensagem serão reconhecidos pelo alias de link. Os links do Content Block também são reconhecidos. No entanto, Content Blocks "antigos" não podem aninhar Content Blocks "novos".

{% alert tip %}
Para Content Blocks, a Braze recomenda criar cópias dos Content Blocks existentes para usar em novas mensagens. Isso pode ser feito por duplicação em massa para evitar cenários em que você possa referenciar um Content Block que não foi habilitado para alias de link em uma nova mensagem.
{% endalert %}

## Alias de link para URLs geradas por Liquid {#link-aliasing-for-urls-generated-by-liquid}

Para URLs geradas por Liquid, como instruções `assign` no HTML ou de um Content Block, você deve adicionar um ponto de interrogação (`?`) à tag Liquid. Isso permite que a Braze adicione parâmetros de consulta (`lid=somevalue`) para que o alias de link funcione corretamente.

Sem identificar onde adicionar os parâmetros de consulta, o alias de link não reconhece essas URLs e os modelos de link não são aplicados.

### Exemplo {#example}

Confira este exemplo de alias de link para a formatação recomendada do link:

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Click Here</a>
```
{% endraw %}

Se o link tiver parâmetros que contenham um ponto de interrogação (`?`), você pode substituí-lo na tag de âncora por um e comercial (`&`), como neste exemplo:

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?param_1&param_2" %}

<a href="{{link_with_params}}&">Click Here</a>
```
{% endraw %}

### URLs com Liquid condicional {#urls-with-conditional-liquid}

Quando tags Liquid condicionais são usadas dentro de um `href` (por exemplo, para definir condicionalmente uma URL usando {% raw %}`{% if %}`, `{% unless %}`{% endraw %}), o alias de link não se aplica a esses links. Isso significa que esses links não aparecem em **Link Management** e não recebem um `lid` para rastreamento de cliques.

Você pode usar o bloco {% raw %}`{% capture %}`{% endraw %} para construir a URL fora do `href` e depois referenciá-la como uma variável, como no exemplo a seguir:

{% raw %}
```liquid
  {%- if condition -%}
    https://example.com/url1
  {%- else -%}
    https://example.com/url2
  {%- endif -%}
{%- endcapture -%}

<a href="{{ url }}?">Click here</a>
```
{% endraw %}