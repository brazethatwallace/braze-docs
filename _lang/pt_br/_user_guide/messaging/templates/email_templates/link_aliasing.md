---
nav_title: Alias de link
article_title: Alias de link
alias: /link_aliasing/
page_order: 3
description: "Este artigo descreve como o alias de link funciona e fornece exemplos de como seus links ficarão."
channel:
  - email

---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/link-aliasing){: style="float:right;width:120px;border:0;" class="noimgborder"}Alias de link {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomlink-aliasing-stylefloatrightwidth120pxborder0-classnoimgborderlink-aliasing}

> Use o alias de link para criar nomes reconhecíveis e gerados pelo usuário para identificar links enviados em mensagens de e-mail da Braze. Esses links ficam disponíveis para redirecionamento de segmentação, disparo baseado em ação e análise de dados de links.

## Sobre o alias de link {#about-link-aliasing}

Com o alias de link, você pode criar nomes gerados pelo usuário para identificar e rastrear links enviados em e-mails. Dessa forma, você pode usar esses aliases de link reconhecíveis nos seus e-mails para rastrear o engajamento e analisar a performance de Campaigns, sem precisar referenciar o link completo.

Com o alias de link, você pode:

- **Redirecionar usuários que clicaram em links específicos:** Identificar e direcionar usuários que clicaram em um link.
- **Criar gatilhos baseados em ação:** Enviar um e-mail quando um usuário clicar em um link.
- **Analisar métricas:** Comparar quantos usuários clicaram no Link A versus o Link B.

### Como funciona {#how-it-works}

A Braze identifica links de forma única dentro dos e-mails, adicionando um parâmetro extra chamado `lid` (também conhecido como identificador de link) a cada URL de link. Esse valor `lid` permite que a Braze rastreie, monitore e agregue as interações dos usuários com o link, mesmo que os demais parâmetros da URL sejam diferentes. Isso ajuda a fornecer insights sobre como os usuários interagem com o conteúdo das suas campanhas de e-mail.

Os identificadores de link também serão atualizados se uma campanha de e-mail, um Canvas com mensagem de e-mail ou um Content Block for duplicado.

## Criando um alias de link {#creating-a-link-alias}

{% alert important %}
**Link Management** aparece no criador de e-mail da Campaign ou do Canvas quando a Braze ativa o gerenciamento de links para a sua conta. Para criar e editar **aliases de link**, o alias de link deve estar ativado. Se **Link Management** não estiver aparecendo, entre em contato com o seu gerente de conta para ativar o alias de link.
{% endalert %}

Para criar um alias de link, abra o corpo do e-mail na Campaign ou no componente do Canvas e, em seguida, abra **Link Management** na área **Content**. Os editores de arrastar e soltar e de HTML usam o mesmo layout de barra lateral:

### Editor de arrastar e soltar {#drag-and-drop-editor}

1. Selecione **Edit Email Body** para abrir o editor de arrastar e soltar.
2. Na barra lateral do editor, selecione **Content** (ao lado de **Sending Settings** e **Preview & Test**). Para mais informações sobre esse layout, consulte [Criar um e-mail com arrastar e soltar]({{site.baseurl}}/user_guide/channels/email/drag_and_drop).
3. No submenu **Content**, selecione **Link Management** (aparece em **Design and Build**). Se o submenu estiver recolhido, expanda-o usando o controle de seta na barra lateral.

### Editor de HTML {#html-editor}

1. Acesse o corpo do e-mail no editor.
2. Na barra lateral do editor, selecione **Content**.
3. No submenu **Content**, selecione **Link Management** em **Design and Build**.

Em **Link Management**:

1. A Braze gera automaticamente aliases de link padrão exclusivos para cada um dos seus links.
2. Dê um nome ao alias. Os aliases devem ter nomes exclusivos por variante de Campaign de e-mail ou componente do Canvas.

Você também pode definir um alias que será usado para referenciar um link específico ao lidar com relatórios ou segmentação.

![Página de Link Management com quatro aliases de link.]({% image_buster /assets/img/link_aliasing_composer.png %})

{% alert note %}
O alias de link é suportado apenas em atributos `href` dentro de tags de âncora HTML onde é seguro adicionar um parâmetro de consulta. É uma boa prática incluir um ponto de interrogação (?) no final do seu link para que a Braze possa facilmente adicionar o valor `lid`. Sem a adição do valor `lid`, a Braze não reconhecerá a URL para alias de link.
{% endalert %}

## Gerenciando aliases de link {#managing-link-aliases}

Para visualizar todos os seus aliases de link rastreados, faça o seguinte:

1. Acesse **Settings** > **Email Preferences** em **Workspace Settings**.
2. Selecione a guia **Link Aliasing Settings**.

Aqui, você pode classificar, pesquisar e desativar o rastreamento de aliases de link.

![Página de aliases de link rastreados mostrando aliases de link ativos e inativos associados a várias Campaigns.]({% image_buster /assets/img/tracked_aliases.png %})

{% alert tip %}
Use os endpoints [List link alias for campaign]({{site.baseurl}}/get_campaign_link_alias) e [List link alias for Canvas]({{site.baseurl}}/get_canvas_link_alias) para extrair o `alias` definido em cada variante de mensagem em uma Campaign ou em um componente do Canvas específico de e-mail.
{% endalert %}

A Braze recomenda avaliar os links dentro do e-mail, adicionar modelos de link e fornecer uma convenção de nomenclatura que funcione para fins de segmentação e relatórios. Isso ajuda você a manter o controle de todos os links.

Quando o alias de link está ativado, as mensagens, Content Blocks e modelos de link não são modificados. Quaisquer mensagens existentes que usem modelos de link ou Content Blocks permanecerão iguais. No entanto, quando você atualizar uma mensagem, a marcação de alias de link será aplicada a todos os links, então você precisará reaplicar os modelos de link para que os links fiquem visíveis.

## Como os links são atualizados com o alias de link {#how-links-are-updated-with-link-aliasing}

As tabelas a seguir fornecem exemplos de links no corpo de um e-mail, resultados do alias de link e explicações de como o link original é atualizado com o alias de link.

### Permalink {#permalink}

**Lógica:** A Braze insere um ponto de interrogação (?) e adiciona o primeiro parâmetro de consulta na URL.

| Link no corpo do e-mail | Link com alias |
|-----------------------|----------------------------------------|
| `https://www.braze.com` | `https://www.braze.com?lid=slfdldtqdhdk` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Permalink" }

### Link com mais parâmetros de consulta {#link-with-more-query-parameters}

**Lógica:** A Braze detecta outros parâmetros de consulta e adiciona `lid=` ao final da URL.

| Link no corpo do e-mail | Link com alias |
|---------------------------------------------------------------|--------------------------------------------------------------------------------|
| `https://www.braze.com?utm_campaign=retention&utm_source=email` | `https://www.braze.com?utm_campaign=retention&utm_source=email&lid=0goty30mviyz` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Link com mais parâmetros de consulta" }

### Link HTML {#html-link}

**Lógica:** A Braze reconhece que o link é uma URL e já possui um ponto de interrogação (?) presente, então o parâmetro de consulta `lid` é adicionado após o ponto de interrogação.

| Link no corpo do e-mail | Link com alias |
|-------------------------------------------------------------------|-----------------------------------------------------------------------------------|
| {%raw%}`<a href="{{custom_attribute.{product_url}}}?">`{%endraw%} | {%raw%}`<a href="{{custom_attribute.{product_url}}}?lid=ac7a548g5kl7">`{%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Link HTML" }

### Link com âncora {#link-with-anchor}

**Lógica:** A Braze espera que a URL use uma estrutura padrão onde as âncoras (#) estão presentes após um ponto de interrogação (?). Como a Braze lê da esquerda para a direita, o ponto de interrogação e o valor `lid` são adicionados antes da âncora.

| Link no corpo do e-mail | Link com alias |
|--------------------------------------------------|-------------------------------------------------------------------|
| `https://www.braze.com#bookmark1?utm_source=email` | `https://www.braze.com?lid=eqslgd5a9m3y#bookmark1?utm_source=email` |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Link com âncora" }

### Link com âncora e tag de captura {#link-with-anchor-and-capture-tag}

**Lógica:** Ao usar o alias de link com URLs que contêm âncoras (#), a Braze espera que a âncora seja colocada após os parâmetros de consulta. Isso significa que o valor `lid` deve ser adicionado **antes** da âncora para o rastreamento adequado, e como a Braze lê a URL da esquerda para a direita, o ponto de interrogação (?) e o `lid` devem vir antes da âncora.

| Link no corpo do e-mail | Link com alias |
|-------------------------------------------------------------------------------------------|--------------------------------------------------------------------------------------------------------------|
| {%raw%}`<a href="https://www.braze.com/promotions#special-offer">Check out our special offer!</a>`{%endraw%} | {%raw%}`<a href="https://www.braze.com/promotions?lid={{link_alias}}#special-offer">Check out our special offer!</a>` {%endraw%} |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Link com âncora e tag de captura" }

## Rastreando aliases de link {#tracking-link-aliases}

Na barra lateral do editor, selecione **Content** > **Link Management** (em **Design and Build**) e, em seguida, selecione quais aliases você deseja que sejam **rastreados**. Os aliases rastreados ficam disponíveis nos filtros de segmentação que referenciam aliases de link (consulte [Filtros de segmentação](#segmentation-filters)). Você também pode enviar mensagens baseadas em ação ou mover usuários por um Canvas quando eles clicarem em um alias de link no e-mail — consulte [Filtros baseados em ação](#action-based-filters). A configuração de **rastreado** não altera se os cliques nesse link contam nos relatórios de performance de e-mail.

{% alert tip %}
Para rastrear métricas de engajamento de link, certifique-se de que seu link comece com HTTP ou HTTPS. Para desativar o rastreamento de cliques em links específicos, consulte [Links universais e App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links#turning-off-click-tracking-on-a-link-to-link-basis).
{% endalert %}

A Braze permite que você selecione links ilimitados para rastrear, embora você só possa redirecionar usuários com base nos links mais recentes que eles abriram. Os perfis de usuário incluem os 100 links clicados mais recentemente. Por exemplo, se você rastrear 500 links e um usuário clicar em todos os 500, você pode redirecionar ou criar Segments com base nos 100 links clicados mais recentemente.

![A guia Link Management com dois links selecionados.]({% image_buster /assets/img/link_management_dnd.png %})

{% alert note %}
A Braze rastreia apenas os últimos 100 aliases de link clicados no nível do perfil.
{% endalert %}

### Filtros baseados em ação {#action-based-filters}

Você pode criar mensagens baseadas em ação direcionando qualquer link (rastreado ou não rastreado) ou redirecionar usuários com base em se eles clicaram em um alias em qualquer Campaign de e-mail ou componente do Canvas.

![Opções baseadas em ação para direcionar usuários que clicaram em um alias em um componente do Canvas ou interagiram com uma Campaign.]({% image_buster /assets/img/link_aliasing_action_based_filters.png %})

### Filtros de segmentação {#segmentation-filters}

Na Braze, se você tiver um alias de link no seu e-mail e um usuário clicar nele, o evento é registrado no perfil do usuário com o alias.

Se você usar o filtro de segmentação "Clicked Alias in Any Campaign or Canvas Step" e depois decidir renomear esse alias de link, os dados de cliques anteriores no perfil do usuário **não** serão atualizados, ou seja, eles ainda mostrarão o alias de link anterior. Portanto, se você direcionar usuários com base no novo alias de link, isso não incluirá os dados do alias de link anterior.

Se você usar o filtro de segmentação "Clicked Alias in Campaign" ou "Clicked Alias in Canvas", ele filtra seus usuários com base em se eles clicaram em um alias específico em uma Campaign ou Canvas específico. Se vários usuários compartilharem o mesmo endereço de e-mail e o alias de link for clicado, todos os outros usuários que compartilham o endereço de e-mail terão seus perfis de usuário atualizados. Esses perfis também são atualizados por eventos de entrega e abertura, não apenas por eventos de clique.

Os filtros de segmentação a seguir se aplicam a eventos de clique que são rastreados no momento em que o evento é processado. Isso significa que links não rastreados não removerão dados existentes e rastrear um link não preencherá retroativamente os dados. Para mais detalhes, consulte [Filtros de segmentação]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters).

#### Cancelando o rastreamento de links {#untracking-links}

Cancelar o rastreamento de um link não realocará Segments existentes com o filtro para o alias não rastreado. Os dados antigos permanecerão nos perfis de usuário até serem substituídos por dados mais recentes.

Links em mensagens arquivadas são automaticamente desrastreados. No entanto, se mensagens arquivadas forem desarquivadas, os links precisarão ser rastreados novamente. Quando aliases de link são rastreados, os relatórios de link são indexados pelo alias em vez de domínios de nível superior ou URLs completas.

Para visualizar todos os links na sua Campaign de e-mail e seus respectivos cliques totais, acesse **Message Analytics** > **Email Performance** > **Preview & Heatmap** e selecione o botão **Show Heatmap**.

![Painel de tabela de links por cliques totais com aliases de link e seus cliques totais.]({% image_buster /assets/img/link_alias_total_clicks.png %}){: style="max-width:60%;"}

### Evento de cliques de e-mail {#email-clicks-event}

Se você exportar seus dados de engajamento com Currents, um evento de clique de e-mail será ligeiramente diferente se você tiver o alias de link ativado. Ele terá dois campos adicionais para o [evento de cliques de e-mail]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events#email-clicks-events) quando o alias de link estiver ativado: `link_id` e `link_alias`.

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
O comportamento do `dispatch_id` difere entre Canvas e Campaigns porque a Braze trata as etapas do Canvas (exceto as etapas de entrada, que podem ser agendadas) como eventos disparados, mesmo quando são "agendadas". Saiba mais sobre o [comportamento do `dispatch_id`]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id) em Canvas e Campaigns.

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

Para URLs geradas por Liquid (por exemplo, instruções `assign` no HTML, valores extraídos de um Content Block ou Liquid em um atributo personalizado), a Braze precisa de um local claro para inserir o parâmetro de consulta `lid`. Na maioria dos casos, quando o Liquid permanece na URL, a Braze não infere se deve iniciar uma nova query string com `?` ou unir a uma query existente com `&`, a menos que você adicione esse delimitador.

Faça o seguinte:

- Se a URL **não** inclui uma query string, adicione `?` após o Liquid (por exemplo, `{{my_url}}?`).
- Se a URL **já** inclui `?` e parâmetros de consulta, adicione `&` após o Liquid (por exemplo, `{{my_url}}&`).

{% alert note %}
Quando você usa [modelos de link]({{site.baseurl}}/user_guide/messaging/templates/email_templates/link_template) com URLs geradas por Liquid, a Braze pode normalizar de forma conservadora a URL renderizada após a execução do Liquid quando ela contém exatamente dois caracteres `?` usados como separadores de consulta. O segundo `?` pode ser reescrito como `&` para que a Braze altere o mínimo possível da URL. <br><br>A Braze não tenta corrigir todos os padrões de `?` duplicados, e o tratamento de URLs mais complexas permanece intencionalmente limitado. Adicione o `?` ou `&` correto na sua marcação primeiro e trate qualquer normalização como uma proteção limitada — não como um substituto para URLs bem formadas ou para que os links sejam reconhecidos em **Link Management** quando nenhum delimitador está presente.
{% endalert %}

Sem um `?` ou `&` final (ou outro ponto de inserção suportado), o alias de link não reconhece a URL, **Link Management** não a lista e os modelos de link não são aplicados.

### Fragmentos de URL (`#`) e parâmetros de rastreamento {#url-fragments-and-tracking-parameters}

O fragmento (`#` e tudo depois dele) não é enviado ao servidor em uma requisição de link normal. A Braze insere o `lid` na query string, que deve aparecer antes do `#`. Se o seu `href` tem Liquid e um fragmento `#`, mas nenhum `?` ou `&` antes do `#`, a Braze não pode adicionar o `lid` com segurança, então o link pode não aparecer em **Link Management** ou ser rastreado como alias de link.

Isso é especialmente comum no editor de arrastar e soltar quando a URL de um botão mistura Liquid com um padrão baseado em hash (por exemplo, um caminho estático, depois `#`, depois pares chave-valor adicionais). Nesse caso, adicione `?` imediatamente antes do `#` para que a query string (incluindo o `lid`) seja analisada antes do fragmento.

{% raw %}
```text
https://example.com/campaign/to/abc123?#user_id={{${user_id}}}&source=email
```
{% endraw %}

No exemplo acima, o `?` antes do `#` fornece à Braze um segmento de consulta para adicionar o `lid`. Sem ele, o link pode não aparecer em **Link Management**.

Sem identificar onde adicionar parâmetros de consulta, o alias de link não reconhece essas URLs e os modelos de link não são aplicados. Se você encontrar erros como **Failed to be assigned an LID** para uma URL dinâmica, confirme que o `href` usa o padrão `?` ou `&` mostrado nos exemplos desta seção.

### Considerações do editor de arrastar e soltar {#drag-and-drop-editor-considerations}

No editor de arrastar e soltar, os campos que contêm um link (como a **URL** de um botão) validam o `href` subjacente antes da execução do Liquid. Espaços, quebras de linha e outros caracteres que não são seguros para URL podem causar comportamento inesperado quando a Braze adiciona modelos de link ou parâmetros de alias de link. Quando você precisa de Liquid condicional para o destino, defina a URL em um bloco HTML (consulte a seção a seguir) e referencie uma única variável no campo de **URL** do arrastar e soltar, em vez de colocar Liquid complexo diretamente nesse campo.

### Exemplo de Content Block {#content-block-example}

{% raw %}
Se um Content Block contém um link como `https://www.braze.com/{{custom_attribute.${offer_id}}}` sem um `?` ou `&` final, a Braze não sabe onde adicionar o `lid`, então o link não é capturado para **Link Management**. Adicione `?` ou `&` no final da URL no Content Block (dependendo de já existir ou não uma query string), salve o Content Block e o link poderá ser reconhecido.
{% endraw %}

### Relatórios quando a URL varia por usuário {#reporting-when-the-url-varies-per-user}

Cada `href` distinto na mensagem é mapeado para **um** ID de link e um alias de link para **Link Management** e relatórios baseados em alias. Quando aliases de link são rastreados, os relatórios de e-mail no dashboard são indexados pelo alias em vez de cada URL resolvida possível.

Use as seguintes abordagens na Braze primeiro:

- **Análise de dados de e-mail de Campaign e Canvas:** Revise os cliques agregados por link em **Message Analytics** > **Email Performance** > **Preview & Heatmap** com **Show Heatmap** ativado, conforme descrito em [Cancelando o rastreamento de links](#untracking-links).
- **Cliques por destinatário no Criador de consultas:** Execute o modelo [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder/query_templates#email-templates) **Email URLs clicked** para uma Campaign ou Canvas. O modelo exibe links despersonalizados para contagens resumidas; a exportação CSV inclui os IDs de usuário dos que clicaram, o link clicado e um timestamp. (URLs despersonalizadas removem tags Liquid para a visualização resumida; consulte a descrição do modelo para detalhes.)
- **Detalhamentos por alias no editor:** Se você precisa que cada destino (por exemplo, cada `offer_id`) apareça como sua própria linha em **Link Management** e nos relatórios baseados em alias, use valores `href` separados (e, portanto, aliases separados) — por exemplo, links distintos por ramificação — em vez de um link cujo caminho muda por usuário.

Se você também usa exportações de engajamento por streaming, os eventos de clique de e-mail incluem um campo **`url`**; consulte [Evento de cliques de e-mail](#email-clicks-event) nesta página para saber como essa carga útil se relaciona com o alias de link.

### Exemplo {#example}

Use este padrão quando a URL atribuída não tem parâmetros de consulta:

{% raw %}
```liquid
{% assign link1 = "https://www.braze1.com" %}

<a href="{{link1}}?">Visit Braze</a>
```
{% endraw %}

Se a URL atribuída já contém `?` e parâmetros de consulta, adicione `&` após o Liquid em vez de `?`:

{% raw %}
```liquid
{% assign link_with_params = "https://www.braze1.com?campaign=test" %}

<a href="{{link_with_params}}&">Visit Braze</a>
```
{% endraw %}

### URLs com Liquid condicional {#urls-with-conditional-liquid}

Quando tags Liquid condicionais são usadas dentro de um `href` (por exemplo, para definir uma URL com {% raw %}`{% if %}`, `{% elsif %}` ou `{% unless %}`{% endraw %}), o alias de link não se aplica a esses links. Isso significa que esses links não aparecem em **Link Management** e não recebem um `lid` para rastreamento de cliques.

**Recomendado:** Construa a URL final em um bloco HTML com `assign` (ou {% raw %}`{% capture %}`{% endraw %}) e depois referencie essa variável onde precisar do link. No editor de arrastar e soltar, cole a variável no campo de **URL** do botão com um `?` ou `&` final conforme apropriado — por exemplo, `{{url}}?`.

{% raw %}
```liquid
{% if {{custom_attribute.${account_tier}}} == "pro" %}
{% assign url = "https://example.com/pro/verify" %}
{% else %}
{% assign url = "https://example.com/retail/account" %}
{% endif %}
```
{% endraw %}

No campo de **URL** do botão (arrastar e soltar) ou no HTML, aponte o `href` para a variável com um delimitador:

{% raw %}
```liquid
<a href="{{ url }}?">Go to account</a>
```
{% endraw %}

Alternativamente, você pode capturar a URL em uma variável:

{% raw %}
```liquid
{% capture url %}
  {%- if condition -%}
    https://example.com/url1
  {%- else -%}
    https://example.com/url2
  {%- endif -%}
{% endcapture %}

<a href="{{ url }}?">Go to account</a>
```
{% endraw %}

## Solução de problemas {#troubleshooting}

### Destinos que não aceitam o parâmetro `lid` {#destinations-that-dont-accept-the-lid-parameter}

Quando você envia uma mensagem de teste pelo editor de e-mail, a Braze adiciona {% raw %}`lid={{placeholder}}`{% endraw %} aos seus links (o placeholder se torna um valor único no momento do envio). Se o site ou API de destino não tolerar parâmetros de consulta extras, o link pode funcionar no editor, mas falhar quando aberto a partir do e-mail.

Sem o valor `lid`, a Braze não trata a URL como alias de link para rastreamento e segmentação. Recomendamos atualizar seu backend ou site para que ele ignore o parâmetro de consulta `lid` quando presente. Isso preserva o alias de link, os relatórios e os casos de uso de segmentação descritos neste artigo.

Alternativamente, você pode desativar o alias de link no dashboard enquanto planeja uma mudança no backend. Acesse **Settings** > **Email Preferences** > **Link Aliasing Settings**.

Se você não puder alterar seus sistemas de destino, entre em contato com o [suporte da Braze]({{site.baseurl}}/braze_support) para desativar o alias de link no seu espaço de trabalho. Observe as seguintes considerações se o alias de link for desativado no seu espaço de trabalho:

- Novas mensagens de e-mail e Content Blocks normalmente não receberão nova marcação de alias de link (como o parâmetro de consulta `lid`).
- Mensagens existentes que foram criadas enquanto o alias de link estava ativado ainda podem conter marcação de alias de link no HTML. Pode ser necessário remover manualmente os parâmetros `lid` restantes onde você não os deseja mais.
- Se você editar uma Campaign existente, uma etapa de e-mail do Canvas ou um Content Block, pode ser necessário adicionar modelos de link novamente para que os links com modelo sejam exibidos corretamente.
- Os relatórios de cliques para envios realizados enquanto o alias de link estava ativado podem não se alinhar perfeitamente com os relatórios após a desativação do recurso.
- Segments que usam filtros baseados em alias de link (por exemplo, filtros **Clicked Alias**) podem parar de retornar os públicos esperados.