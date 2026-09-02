---
nav_title: "Tipos de identificadores da API or interface de programação do aplicativo (API)"
article_title: Tipos de identificadores de API or interface de programação do aplicativo (API)
page_order: 2.2
toc_headers: h2
description: "Este artigo de referência aborda os diferentes tipos de identificadores de API or interface de programação do aplicativo (API) que existem no dashboard da Braze, onde você pode encontrá-los e para que são usados."
page_type: reference
---

# Tipos de identificadores da API or interface de programação do aplicativo (API) {#api-identifier-types}

> Este guia de referência aborda os diferentes tipos de identificadores de API or interface de programação do aplicativo (API) que podem ser encontrados no dashboard da Braze, sua finalidade, onde você pode encontrá-los e como eles são normalmente usados. Para obter informações sobre as chaves da API or interface de programação do aplicativo (API) REST or transferir estado representacional ou as chaves da API or interface de programação do aplicativo (API) do espaço de trabalho, consulte a [visão geral da API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/basics).

Os seguintes identificadores podem ser usados para acessar seu modelo, Canvas, Campaign ou Segment or segmento a partir da API or interface de programação do aplicativo (API) externa da Braze. Todas as mensagens devem seguir a codificação [UTF-8](https://en.wikipedia.org/wiki/UTF-8).

## Identificador do app {#app-identifier}

O identificador do app, ou `app_id`, é um parâmetro que associa atividades a um app específico no seu espaço de trabalho. Ele designa com qual app dentro do espaço de trabalho você está interagindo. Por exemplo, você pode ter um `app_id` para o app iOS, um `app_id` para o app Android e um `app_id` para a integração web. Na Braze, você pode ter vários apps para a mesma plataforma nos diferentes tipos de plataforma que a Braze suporta.

### Onde posso encontrá-lo? {#where-can-i-find-it}

Existem duas maneiras de localizar seu `app_id`:

{% tabs local %}
{% tab App Identifiers %}
Acesse **Settings** > **APIs and Identifiers** > **App Identifiers**. Sua chave de API or interface de programação do aplicativo (API) para cada app está listada na coluna **Identifier**.
{% endtab %}

{% tab App Settings %}
Acesse **Settings** > **App Settings**. Sua chave de API or interface de programação do aplicativo (API) está listada ao lado do campo **API or interface de programação do aplicativo (API) Key** na seção de configurações.

{% endtab %}
{% endtabs %}

### Para que pode ser usado? {#what-can-it-be-used-for}

Os identificadores de app na Braze são usados ao integrar o SDK or kit de desenvolvimento de software e também para referenciar um app específico em chamadas da REST or transferir estado representacional API or interface de programação do aplicativo (API). Com o `app_id`, você pode fazer diversas coisas, como obter dados de um evento personalizado ocorrido em um app específico, recuperar estatísticas de desinstalações, estatísticas de novos usuários, estatísticas de usuários ativos diários e estatísticas de início de sessão para um app específico.

{% alert tip %}
Às vezes, você pode receber uma solicitação de `app_id`, mas não está trabalhando com um app, pois se trata de um campo legado específico de uma determinada plataforma. Nesse caso, você pode omitir esse campo incluindo qualquer string de caracteres como placeholder para esse parâmetro obrigatório.
{% endalert %}

### Múltiplos identificadores de app {#multiple-app-identifiers}

Durante a configuração do SDK or kit de desenvolvimento de software, o caso de uso mais comum para múltiplos identificadores de app é separar esses identificadores para variantes de compilação de debug e release.

Para alternar facilmente entre múltiplos identificadores de app nas suas compilações, recomendamos criar um arquivo `braze.xml` separado para cada [variante de compilação](https://developer.android.com/studio/build/build-variants.html) relevante. Uma variante de compilação é uma combinação de tipo de compilação e variação de produto. Por padrão, um novo projeto Android é configurado com os tipos de compilação `debug` e `release` e sem variações de produto.

Para cada variante de compilação relevante, crie um novo `braze.xml` em `src/<build variant name>/res/values/`:

```xml
<?xml version="1.0" encoding="utf-8"?>
<resources>
<string name="com_braze_api_key">{YOUR_BUILD_VARIANT_API_KEY}</string>
</resources>
```
Quando a variante de compilação for compilada, ela usará o novo identificador.

## Identificador de modelo {#template-identifier}

Um identificador de [modelo]({{site.baseurl}}/api/endpoints/templates) ou ID de modelo é uma chave aleatória gerada pela Braze para um determinado modelo dentro do dashboard. Os IDs de modelo são únicos para cada modelo e podem ser usados para referenciar modelos por meio da API or interface de programação do aplicativo (API).

Os modelos são ótimos quando sua empresa terceiriza os designs HTML para Campaigns. Depois que os modelos são criados, você tem um modelo que não é específico de uma Campaign, mas pode ser aplicado a uma série de Campaigns, como um boletim informativo.

### Onde posso encontrá-lo?

Você pode encontrar o ID do seu modelo de duas maneiras:

{% tabs local %}
{% tab Modelos %}
Acessar **Modelos**, selecione uma página de modelos e, em seguida, selecione um modelo pré-existente. Se o modelo desejado ainda não existe, crie um e salve. Na parte inferior da página do modelo individual, você pode encontrar o identificador do modelo.
{% endtab %}

{% tab Chaves de API or interface de programação do aplicativo (API) %}
Acessar **Configurações** > **APIs e identificadores**. Aqui, a Braze oferece uma pesquisa de **Identificadores de API or interface de programação do aplicativo (API) adicionais** onde você pode procurar identificadores específicos.

{% endtab %}
{% endtabs %}

### Para que ele pode ser usado?

- Atualizar modelos usando a API or interface de programação do aplicativo (API)
- Obter informações sobre um modelo específico

## Identificador do Canvas {#canvas-identifier}

Um identificador de [Canvas]({{site.baseurl}}/user_guide/messaging/canvas) ou Canvas ID é uma chave aleatória gerada pela Braze para um determinado Canvas no dashboard. Os Canvas IDs são exclusivos para cada Canvas e podem ser usados para referenciar Canvas por meio da API or interface de programação do aplicativo (API).

Lembre-se de que, se você tiver um Canvas com variantes, existe um Canvas ID geral, além de Canvas IDs de variantes individuais aninhados sob o Canvas principal.

### Onde posso encontrá-lo?

Você pode encontrar o Canvas ID no dashboard. Acesse **Messaging** > **Canvas** e selecione um Canvas existente. Se o Canvas desejado ainda não existir, crie um e salve-o. Na parte inferior da página de um Canvas individual, clique em **Analyze Variants**. Uma janela será exibida com o identificador de API or interface de programação do aplicativo (API) do Canvas localizado na parte inferior.

### Para que ele pode ser usado?

- Rastrear a análise de dados de uma mensagem específica
- Obter estatísticas agregadas de alto nível sobre a performance do Canvas
- Obter detalhes sobre um Canvas específico
- Com o Currents, para trazer dados em nível de usuário e ter uma visão mais ampla dos Canvas
- Com entrega disparada por API or interface de programação do aplicativo (API), para coletar estatísticas de mensagens transacionais

## Identificador de Campaign {#campaign-identifier}

Um identificador de [Campaign]({{site.baseurl}}/user_guide/messaging/campaigns) ou ID de Campaign é uma chave aleatória gerada pela Braze para uma determinada Campaign no dashboard. Os IDs de Campaign são únicos para cada Campaign e podem ser usados para referenciar Campaigns por meio da API or interface de programação do aplicativo (API).

Lembre-se de que, se você tem uma Campaign com variantes, há tanto um ID geral de Campaign quanto IDs individuais de variante de Campaign aninhados sob a Campaign principal.

### Onde posso encontrá-lo?

Você pode encontrar o ID da sua Campaign de duas maneiras:

{% tabs local %}
{% tab Campaigns %}
Acesse **Messaging** > **Campaigns** e selecione uma Campaign já existente. Se a Campaign desejada ainda não existir, crie uma e salve-a. Na parte inferior da página individual da Campaign, você encontrará o **Campaign API or interface de programação do aplicativo (API) Identifier**.

{% endtab %}

{% tab API or interface de programação do aplicativo (API) Keys %}
Acesse **Settings** > **APIs and Identifiers**. Aqui, a Braze oferece uma pesquisa de **Additional API or interface de programação do aplicativo (API) Identifiers** onde você pode buscar identificadores específicos.

{% endtab %}
{% endtabs %}

### Para que ele pode ser usado?

- Rastrear análises de dados de uma mensagem específica
- Obter estatísticas agregadas de alto nível sobre o desempenho de uma Campaign
- Obter detalhes de uma Campaign específica
- Com Currents, para trazer dados em nível de usuário para uma abordagem mais ampla de Campaigns
- Com entrega disparada por API or interface de programação do aplicativo (API), para coletar estatísticas de mensagens transacionais
- Para [pesquisar uma Campaign específica]({{site.baseurl}}/user_guide/messaging/campaigns/manage_campaigns/search_campaigns) na página de **Campaigns** usando o filtro `api_id:YOUR_API_ID`

## Identificador de Segment or segmento {#segment-identifier}

Um [Segment]({{site.baseurl}}/user_guide/audience/segments) ou ID de Segment é uma chave aleatória gerada pela Braze para um determinado Segment no dashboard. Os IDs de Segment são exclusivos para cada Segment e podem ser usados para referenciar Segments por meio da API or interface de programação do aplicativo (API).

### Onde posso encontrá-lo?

Você pode encontrar o ID do seu Segment or segmento de duas maneiras:

{% tabs local %}
{% tab Segments %}
Acessar **Público** > **Segments** e selecione um Segment or segmento pré-existente. Se o Segment or segmento que você procura ainda não existe, crie um e salve. Na parte inferior da página individual do Segment or segmento, você encontrará o identificador do Segment or segmento.

{% endtab %}

{% tab Chaves de API or interface de programação do aplicativo (API) %}
Acessar **Configurações** > **APIs e identificadores**. Lá, a Braze oferece uma pesquisa de **Identificadores de API or interface de programação do aplicativo (API) adicionais** onde você pode buscar identificadores específicos.

{% endtab %}
{% endtabs %}

### Para que pode ser usado?

- Obter detalhes sobre um Segment or segmento específico
- Recuperar análises de dados de um Segment or segmento específico
- Verificar quantas vezes um evento personalizado foi registrado para um Segment or segmento específico
- Especificar e enviar uma Campaign para membros de um Segment or segmento por meio da API or interface de programação do aplicativo (API)

## Identificador de envio {#send-identifier}

Um identificador de envio, ou send ID, é uma chave gerada pela Braze ou criada por você para um determinado envio de mensagem, sob a qual a análise de dados será rastreada. O identificador de envio permite que você recupere a análise de dados de uma instância específica de envio de uma Campaign por meio do [endpoint `/sends/data_series`]({{site.baseurl}}/api/endpoints/export/campaigns/get_send_analytics).

### Onde posso encontrá-lo?

Campaigns de API or interface de programação do aplicativo (API) e disparadas por API or interface de programação do aplicativo (API) que são enviadas como broadcast geram automaticamente um identificador de envio caso nenhum seja fornecido. Se você quiser especificar seu próprio identificador de envio, primeiro será necessário criar um por meio do [endpoint `/sends/id/create`]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_create_send_ids). O identificador deve conter apenas caracteres ASCII e ter no máximo 64 caracteres. Você pode reutilizar um identificador de envio em vários envios da mesma Campaign se quiser agrupar a análise de dados desses envios.

### Para que ele pode ser usado?
Enviar e acompanhar o desempenho de mensagens de forma programática, sem a necessidade de criar uma Campaign para cada envio.

## Identificador do grupo de inscrições {#subscription-group-identifier}

Um identificador do grupo de inscrições, ou ID do grupo de inscrições, é uma chave gerada pela Braze para um determinado grupo de inscrições. Os IDs são exclusivos para cada grupo de inscrições e podem ser usados para referenciar grupos de inscrições por meio da API or interface de programação do aplicativo (API).

### Onde posso encontrá-lo?

Acesse **Público** > **Inscrições** e copie o ID ao lado do respectivo grupo de inscrições.

### Para que ele pode ser usado?

- Listar os grupos de inscrições de um usuário
- Obter o status do grupo de inscrições de um usuário
- Atualizar o status do grupo de inscrições de um usuário