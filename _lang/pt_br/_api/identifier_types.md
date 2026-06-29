---
nav_title: "Tipos de identificadores da API"
article_title: Tipos de identificadores de API
page_order: 2.2
toc_headers: h2
description: "Este artigo de referência aborda os diferentes tipos de identificadores de API que existem no dashboard da Braze, onde você pode encontrá-los e para que são usados."
page_type: reference

---

# Tipos de identificadores da API {#api-identifier-types}

> Este guia de referência aborda os diferentes tipos de identificadores de API que podem ser encontrados no dashboard da Braze, sua finalidade, onde você pode encontrá-los e como eles são normalmente usados. Para obter informações sobre as chaves da API REST ou as chaves da API do espaço de trabalho, consulte a [visão geral da API]({{site.baseurl}}/api/api_key).

Os seguintes identificadores podem ser usados para acessar seu modelo, Canvas, Campaign ou Segment a partir da API externa da Braze. Todas as mensagens devem seguir a codificação [UTF-8](https://en.wikipedia.org/wiki/UTF-8).

## Identificador do app {#app-identifier}

O identificador do app ou `app_id` é um parâmetro que associa a atividade a um app específico em seu espaço de trabalho. Ele designa com qual app dentro do espaço de trabalho você está interagindo. Por exemplo, você descobre que tem um `app_id` para seu app para iOS, um `app_id` para seu app para Android e um `app_id` para sua integração na Web. Na Braze, você pode descobrir que tem vários apps para a mesma plataforma nos vários tipos de plataforma suportados pela Braze.

### Onde posso encontrá-lo? {#where-can-i-find-it}

Há duas maneiras de localizar seu `app_id`:

{% tabs local %}
{% tab App Identifiers %}
Acesse **Configurações** > **APIs e identificadores** > **Identificadores de Aplicativos**. Sua chave de API para cada app está listada na coluna **Identificador**.
{% endtab %}

{% tab App Settings %}
Acesse **Configurações** > **Configurações do app**. Sua chave de API está listada ao lado do campo **Chave de API** na seção de configurações.

{% endtab %}
{% endtabs %}

### Para que ele pode ser usado? {#what-can-it-be-used-for}

Os identificadores de app na Braze são usados na integração do SDK e também são usados para fazer referência a um app específico nas chamadas da REST API. Com o `app_id`, é possível fazer muitas coisas, como extrair dados de um evento personalizado que ocorreu em um determinado app, recuperar estatísticas de desinstalação, estatísticas de novos usuários, estatísticas de DAU e estatísticas de início de sessão de um determinado app.

{% alert tip %}
Às vezes, pode ser que seja solicitado um `app_id`, mas você não está trabalhando com um app, porque é um campo legado específico para uma plataforma específica. Você pode omitir esse campo incluindo qualquer string de caracteres como espaço reservado para esse parâmetro obrigatório.
{% endalert %}

### Vários identificadores de app {#multiple-app-identifiers}

Durante a configuração do SDK, o caso de uso mais comum para vários identificadores de app é separar esses identificadores para variantes de compilação de depuração e lançamento.

Para alternar facilmente entre vários identificadores de app em suas compilações, recomendamos a criação de um arquivo `braze.xml` separado para cada [variante de compilação](https://developer.android.com/studio/build/build-variants.html) relevante. Uma variante de compilação é uma combinação de tipo de compilação e flavor de produto. Por padrão, um novo projeto Android é configurado com os tipos de compilação `debug` e `release` e sem flavors de produto.

Para cada variante de compilação relevante, crie um novo `braze.xml` para ela em `src/<build variant name>/res/values/`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">{YOUR_BUILD_VARIANT_API_KEY}</string>
</resources>
```
Quando a variante de compilação é compilada, ela usa o novo identificador.

## Identificador do modelo {#template-identifier}

Um identificador de [modelo]({{site.baseurl}}/api/endpoints/templates) ou ID de modelo é uma chave aleatória gerada pela Braze para um determinado modelo dentro do dashboard. Os IDs de modelo são exclusivos para cada modelo e podem ser usados para fazer referência a modelos por meio da API.

Os modelos são ótimos se sua empresa terceiriza seus designs de HTML para campanhas. Depois que os modelos forem criados, você terá um modelo que não é específico para uma campanha, mas que pode ser aplicado a uma série de campanhas, como um boletim informativo.

### Onde posso encontrá-lo?

Você pode encontrar o ID do modelo de duas maneiras:

{% tabs local %}
{% tab Templates %}
Acesse **Modelos**, selecione uma página de modelo e, em seguida, selecione um modelo pré-existente. Se o modelo que você deseja ainda não existir, crie um e salve-o. Na parte inferior da página do modelo individual, você pode encontrar o identificador do modelo.
{% endtab %}

{% tab API Keys %}
Acesse **Configurações** > **APIs e identificadores**. Aqui, a Braze oferece uma pesquisa de **identificadores adicionais de API**, onde você pode procurar identificadores específicos.

{% endtab %}
{% endtabs %}

### Para que ele pode ser usado?

- Atualizar modelos usando a API
- Obter informações sobre um modelo específico

## Identificador do Canvas {#canvas-identifier}

Um identificador de [Canvas]({{site.baseurl}}/user_guide/messaging/canvas) ou ID do Canvas é uma chave aleatória gerada pela Braze para um determinado Canvas dentro do dashboard. Os IDs do Canvas são exclusivos para cada Canvas e podem ser usados para fazer referência a Canvas por meio da API.

Lembre-se de que, se você tiver um Canvas com variantes, haverá um ID geral do Canvas, bem como IDs de Canvas de variantes individuais aninhados sob o Canvas principal.

### Onde posso encontrá-lo?

Você pode encontrar seu ID do Canvas no dashboard. Acesse **Envio de mensagens** > **Canvas** e selecione um Canvas pré-existente. Se o Canvas que você deseja ainda não existir, crie um e salve-o. Na parte inferior de uma página individual do Canvas, clique em **Analyze Variants**. Uma janela é exibida com o identificador da API do Canvas localizado na parte inferior.

### Para que ele pode ser usado?

- Rastrear análise de dados em uma mensagem específica
- Obter estatísticas agregadas de alto nível sobre o desempenho do Canvas
- Obter detalhes sobre um Canvas específico
- Com o Currents para trazer dados de nível de usuário para uma abordagem "mais ampla" do Canvas
- Com entrega disparada por API para coletar estatísticas de mensagens transacionais

## Identificador de Campaign {#campaign-identifier}

Um identificador de [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) ou ID de Campaign é uma chave aleatória gerada pela Braze para uma determinada Campaign dentro do dashboard. Os IDs de Campaign são exclusivos para cada Campaign e podem ser usados para fazer referência a Campaigns por meio da API.

Tenha em mente que, se você tiver uma Campaign que possui variantes, há tanto um ID de Campaign geral quanto IDs de Campaign de variantes individuais aninhados sob a Campaign principal.

### Onde posso encontrá-lo?

Você pode encontrar seu ID de Campaign de duas maneiras:

{% tabs local %}
{% tab Campaigns %}
Acesse **Envio de mensagens** > **Campaigns** e selecione uma Campaign pré-existente. Se a Campaign que você deseja ainda não existir, crie uma e salve-a. Na parte inferior da página da Campaign individual, você pode encontrar seu **Campaign API Identifier**.

{% endtab %}

{% tab API Keys %}
Acesse **Configurações** > **APIs e identificadores**. Aqui, a Braze oferece uma pesquisa de **identificadores adicionais de API**, onde você pode procurar identificadores específicos.

{% endtab %}
{% endtabs %}

### Para que ele pode ser usado?

- Rastrear análise de dados em uma mensagem específica
- Obter estatísticas agregadas de alto nível sobre o desempenho da Campaign
- Obter detalhes sobre uma Campaign específica
- Com o Currents para trazer dados de nível de usuário para uma abordagem "mais ampla" das Campaigns
- Com entrega disparada por API para coletar estatísticas de mensagens transacionais
- Para [pesquisar uma Campaign específica]({{site.baseurl}}/user_guide/engagement_tools/campaigns/managing_campaigns/search_campaigns#search-syntax) na página **Campaigns** usando o filtro `api_id:YOUR_API_ID`

## Identificador de Segment {#segment-identifier}

Um identificador de [Segment]({{site.baseurl}}/user_guide/audience/segments) ou ID de Segment é uma chave aleatória gerada pela Braze para um determinado Segment dentro do dashboard. Os IDs de Segment são exclusivos para cada Segment e podem ser usados para fazer referência a Segments por meio da API.

### Onde posso encontrá-lo?

Você pode encontrar seu ID de Segment de duas maneiras:

{% tabs local %}
{% tab Segments %}
Acesse **Público** > **Segments** e selecione um Segment pré-existente. Se o Segment que você deseja ainda não existir, crie um e salve-o. Na parte inferior da página de Segment individual, você pode encontrar seu identificador de Segment.

{% endtab %}

{% tab API Keys %}
Acesse **Configurações** > **APIs e identificadores**. Aqui, a Braze oferece uma pesquisa de **identificadores adicionais de API**, onde você pode procurar identificadores específicos.

{% endtab %}
{% endtabs %}

### Para que ele pode ser usado?

- Obter detalhes sobre um Segment específico
- Recuperar análise de dados de um Segment específico
- Verificar quantas vezes um evento personalizado foi registrado para um Segment específico
- Especificar e enviar uma Campaign para membros de um Segment a partir da API

## Identificador de envio {#send-identifier}

Um identificador de envio, ou ID de envio, é uma chave gerada pela Braze ou criada por você para um determinado envio de mensagens sob a qual a análise de dados deve ser rastreada. O identificador de envio permite que você obtenha análise de dados para uma instância específica de um envio de Campaign por meio do [endpoint `/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics).

### Onde posso encontrá-lo?

As Campaigns disparadas por API que são enviadas como broadcast geram automaticamente um identificador de envio se um identificador de envio não for fornecido. Se quiser especificar seu próprio identificador de envio, você deve primeiro criar um por meio do [endpoint `/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids). O identificador precisa conter apenas caracteres ASCII e ter no máximo 64 caracteres. Você pode reutilizar um identificador de envio em vários envios da mesma Campaign se quiser agrupar a análise de dados desses envios.

### Para que ele pode ser usado?
Enviar e rastrear o desempenho das mensagens de forma programática, sem a criação de Campaigns para cada envio.

## Identificador do grupo de inscrições {#subscription-group-identifier}

Um identificador de grupo de inscrições, ou ID de grupo de inscrições, é uma chave gerada pela Braze para um determinado grupo de inscrições. Os IDs são exclusivos para cada grupo de inscrições e podem ser usados para fazer referência a grupos de inscrições por meio da API.

### Onde posso encontrá-lo?

Acesse **Público** > **Inscrições** e copie o ID ao lado do respectivo grupo de inscrições.

### Para que ele pode ser usado?

- Listar os grupos de inscrições de um usuário
- Obter o status do grupo de inscrições de um usuário
- Atualizar o status do grupo de inscrições de um usuário