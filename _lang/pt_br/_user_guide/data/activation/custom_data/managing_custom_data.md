---
nav_title: Gerenciar dados personalizados
article_title: Gerenciar dados personalizados
page_order: 2
page_type: reference
description: "Este artigo de referência aborda como gerenciar eventos e atributos personalizados — preencher previamente, adicionar descrições e tags, gerenciar propriedades de eventos, forçar tipos de dados e marcar atributos como IPI."
---

# Gerenciar dados personalizados {#manage-custom-data}

> Esta página aborda como preencher previamente dados personalizados em suas campanhas e segmentos, gerenciar eventos e atributos personalizados e suas propriedades, e configurar tipos de dados. Para colocar na lista de bloqueio e excluir dados personalizados, consulte [Lista de bloqueio de dados personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).

Para saber como gerenciar atributos personalizados em particular (incluindo adicionar descrições, adicionar tags e marcar atributos como IPI), consulte [Gerenciar atributos personalizados]({{site.baseurl}}/user_guide/data/activation/attributes/custom_attributes/#managing-custom-attributes).

## Preenchimento prévio de dados personalizados {#pre-populate-custom-data}

Pode haver ocasiões em que você queira configurar Campaigns e Segments usando dados personalizados antes que sua equipe de desenvolvimento tenha integrado esses dados. A Braze permite que você preencha previamente eventos e atributos personalizados no dashboard antes que esses dados comecem a ser rastreados, de modo que esses eventos e atributos estejam disponíveis para uso em menus suspensos e como parte do processo de criação de Campaigns.

Para preencher previamente eventos e atributos personalizados, faça o seguinte:

1. Acesse **Configurações de dados** > **Eventos personalizados** ou **Atributos personalizados** ou **Produtos**.

![Navegue até Atributos personalizados, Eventos personalizados ou Produtos.]({% image_buster /assets/img_archive/prepopulate_page.png %}){: style="max-width:90%;" }

{: start="2"}
2. Para adicionar um atributo personalizado, evento ou produto, acesse a respectiva página e selecione **Add Custom Attributes**, **Add Custom Events** ou **Add Products**.<br><br>Para atributos personalizados, selecione um [tipo de dado]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#custom-attribute-data-types) para esse atributo (por exemplo, booleano ou string). O tipo de dados de um atributo determina os filtros de segmentação disponíveis para esse atributo. <br><br>![Adicionar novo atributo ou evento]({% image_buster /assets/img_archive/prepopulate_add.png %}){: style="max-width:80%;" }
3. Selecione **Save**.

### Nomeação de eventos personalizados e atributos personalizados {#naming-custom-events-and-custom-attributes}

Os eventos personalizados e os atributos personalizados diferenciam maiúsculas de minúsculas. Tenha isso em mente quando sua equipe de desenvolvimento integrar esses eventos ou atributos personalizados posteriormente. Eles devem nomear os eventos ou atributos personalizados exatamente como você os nomeou aqui, caso contrário a Braze gerará um evento ou atributo personalizado diferente.

## Gerenciamento de propriedades {#managing-properties}

Depois de criar um evento personalizado ou produto, selecione **Manage Properties** desse evento ou produto para adicionar novas propriedades, colocar na lista de bloqueio as propriedades existentes e visualizar quais Campaigns ou Canvas usam essa propriedade em um [evento de gatilho]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign/triggered_delivery/).

![Propriedades personalizadas para um evento personalizado.]({% image_buster /assets/img_archive/manageproperties1.png %}){: style="max-width:80%"}

Para colocar propriedades de eventos ou produtos na lista de bloqueio, use o menu de ações na página de propriedades. Para colocar atributos personalizados, eventos ou produtos inteiros na lista de bloqueio, consulte [Lista de bloqueio de dados personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).

Para tornar rastreáveis esses atributos personalizados, eventos, produtos ou propriedades de eventos adicionados, é necessário pedir à equipe de desenvolvimento que os crie no SDK usando o nome exato que você usou para adicioná-los anteriormente. Ou você pode usar a [API]({{site.baseurl}}/api/basics/) da Braze para importar dados sobre esse atributo. Depois disso, o atributo personalizado, evento ou outro será acionável e se aplicará aos seus usuários.

{% include alerts/note_alerts.md alert='Manage custom data storage' %}

## Detecção de tipo de dados entre ambientes {#data-type-detection-across-environments}

A Braze detecta automaticamente o tipo de dados de um atributo personalizado com base no primeiro valor recebido. Se o seu ambiente de desenvolvimento enviar primeiro um valor numérico como `100`, o atributo será armazenado como número. Se o primeiro valor do seu ambiente de produção chegar como string (como `"100"` entre aspas), o atributo será armazenado como string.

Para evitar isso, garanta que sua integração envie tipos de dados consistentes em todos os ambientes. Se o tipo errado já estiver definido, você pode forçar o tipo de dados correto em **Configurações de dados** > **Atributos personalizados** usando o [menu suspenso de tipo de dados](#forcing-data-type-comparisons).

## Forçar comparações de tipos de dados {#forcing-data-type-comparisons}

A Braze reconhece automaticamente os tipos de dados para os dados de atributos enviados a ela. No entanto, caso vários tipos de dados sejam aplicados a um único atributo, é possível forçar o tipo de dados de qualquer atributo para que a Braze saiba o que ele é. Selecione na lista suspensa da coluna **Data Type**.

{% alert note %}
A partir de 30 de março de 2026, a detecção automática só define um tipo de dados na ingestão inicial. Para alterar o tipo de dados após a ingestão inicial, atualize-o manualmente seguindo as etapas abaixo.
{% endalert %}

{% alert note %}
Forçar tipos de dados não se aplica a propriedades de eventos ou propriedades de compra.
{% endalert %}

![Menu suspenso de tipo de dados de atributos personalizados]({% image_buster /assets/img_archive/custom_events_view_data_type_dropdown.png %})

{% alert warning %}
Se você optar por forçar o tipo de dados de um atributo, todos os dados recebidos que não forem do tipo especificado serão convertidos para esse tipo. Se essa conversão for impossível (por exemplo, uma string contendo letras sendo convertida em um número), os dados serão ignorados. Todos os dados ingeridos antes da alteração do tipo continuarão armazenados como o tipo antigo (e, portanto, podem não ser segmentáveis), e um aviso aparecerá ao lado do atributo nos perfis dos usuários afetados.
{% endalert %}

### Dados existentes após uma alteração de tipo {#existing-data-after-a-type-change}

Forçar uma alteração de tipo de dados afeta apenas os novos dados que chegam à Braze. Todos os dados ingeridos antes da alteração de tipo continuam armazenados como o tipo antigo e podem não ser segmentáveis com os filtros do novo tipo. Um aviso aparece nos perfis dos usuários afetados. Para novos dados recebidos, se um valor não corresponder ao tipo forçado, a Braze pode convertê-lo para o tipo forçado (por exemplo, a string `"100"` para o número `100`). Valores que não podem ser convertidos são ignorados e não atualizam o atributo.

Se você precisar que todos os dados de usuários existentes correspondam ao novo tipo, será necessário reenviar os valores do atributo para esses usuários por meio do SDK, da API ou de uma importação CSV. Não há conversão em massa automática para dados existentes.

### Coerção de tipos de dados {#data-type-coercion}

| Tipo de dados forçado | Descrição |
|------------------|-------------|
| Booleano | As entradas `1`, `true`, `t` (não diferenciam maiúsculas de minúsculas) são armazenadas como `true` |
| Booleano | As entradas `0`, `false`, `f` (não diferenciam maiúsculas de minúsculas) são armazenadas como `false` |
| Número | Números inteiros ou de ponto flutuante (como `1`, `1.5`) são armazenados como números |
| Número | Strings numéricas (como `"100"` ou `"3.14"`) podem ser convertidas em números quando o atributo é forçado para **Número** |
| String | Valores numéricos podem ser convertidos para sua forma de string quando o atributo é forçado para **String** |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Coerção de tipos de dados" }

Para saber mais sobre opções de filtro específicas expostas por diferentes comparações de tipos de dados, confira [Configurando relatórios]({{site.baseurl}}/user_guide/analytics/reports/configure_reporting/). Para saber mais sobre os diferentes tipos de dados disponíveis, consulte [Tipos de dados]({{site.baseurl}}/user_guide/data/activation/custom_data/data_types/#custom-attribute-data-types).

{% alert note %}
Os dados enviados à Braze são imutáveis e não podem ser excluídos ou modificados depois que a Braze os recebe. No entanto, é possível usar qualquer uma das etapas listadas nas seções anteriores para exercer controle sobre o que está sendo rastreado no dashboard. Para colocar na lista de bloqueio ou excluir dados personalizados, consulte [Lista de bloqueio de dados personalizados]({{site.baseurl}}/user_guide/data/activation/custom_data/blocklist_custom_data/).
{% endalert %}