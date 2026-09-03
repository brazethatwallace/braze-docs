# Dashboard de uso de créditos {#credits-usage-dashboard}

> O dashboard de uso de créditos fornece insights de autoatendimento sobre o consumo de créditos, oferecendo uma visão abrangente do uso histórico e atual em comparação com as alocações contratuais. Esses insights podem reduzir suas dúvidas e ajudar você a fazer ajustes para evitar riscos de excedente.

O dashboard **Credits Usage** é dividido em duas seções:
- [Visão geral do uso de créditos](#credits-usage-overview)
- [Guias de canais](#credits-features)

Acesse o dashboard em **Configurações** > **Billing** > **Credits Usage**.

## Visão geral do uso de créditos {#credits-usage-overview}

A **Visão geral do uso de créditos de mensagem** fornece uma visão geral do uso em todos os canais que utilizam créditos. Você pode ver como está o ritmo em relação à sua alocação total de créditos e encontrar detalhes sobre seu contrato ativo e o período do contrato.

Esta página é exibida se você estiver em um contrato de créditos. Os canais que utilizam créditos são mostrados em **Uso de créditos**.

{% alert note %}
Se você adquiriu o WhatsApp, mas não está em um contrato de créditos, ainda verá o consumo de créditos para o WhatsApp, pois é assim que os contratos legados do WhatsApp são cobrados. Isso difere do SMS legado, que só consome créditos quando você está em um contrato de créditos.
{% endalert %}

Os dados de visão geral do uso de créditos são limitados ao período do contrato, que é exibido na **Visão geral do contrato de créditos**. Não é possível filtrar por um intervalo de datas fora do **Período de créditos**.


### Uso de créditos ao longo do contrato {#credits-usage-over-contract}

O gráfico **Uso de créditos de mensagem ao longo do contrato** mostra seu uso durante o período selecionado. A granularidade deste gráfico depende do período selecionado. Visualize as opções de exportação selecionando o menu no menu do gráfico.

![Gráfico de uso de créditos ao longo do contrato.]({% image_buster /assets/img/app_settings/credit_usage_over_contract1.png %})

## Guia Visão geral {#overview-tab}

A guia **Visão geral de uso** mostra o uso de créditos em canais aplicáveis à sua empresa. Por exemplo, se você não tem WhatsApp, a guia correspondente não aparecerá.

### Recursos de créditos {#credits-features}

Consulte as guias a seguir para ver detalhes sobre o que é exibido para cada recurso que consome créditos.

{% tabs %}
{% tab Banners %}

### Banners

**Banners Credits Usage** mostra o uso de créditos de Banners em todas as contas. Os blocos mostram o total de créditos consumidos e o total de impressões únicas diárias. A tabela **Usage by account** inclui **Braze workspace**, **Daily unique impressions**, **Credit ratio** e **Credits**. Quando há dados disponíveis, **Last updated** mostra quando a tabela foi atualizada.

#### Filtros {#filters}

Você pode filtrar seus dados por:
- Período (padrão: últimos 30 dias)
- Espaço de trabalho da Braze

Use **Export** para baixar os dados da tabela.

![Uso de créditos de Banners com blocos para créditos e impressões únicas e uma tabela de uso por conta.]({% image_buster /assets/img/app_settings/credits_usage_banners.png %})

{% endtab %}
{% tab Content Cards %}

### Content Cards

**Content Cards Credits Usage** mostra o uso de créditos de Content Cards em todas as contas. Os blocos mostram o total de créditos consumidos e o total de impressões únicas diárias. A tabela **Usage by account** inclui **Braze workspace**, **Card type**, **Daily Unique Impressions**, **Credit ratio** e **Credits**. Quando há dados disponíveis, **Last updated** mostra quando a tabela foi atualizada.

#### Filtros

Você pode filtrar seus dados por:
- Período (padrão: últimos 30 dias)
- Espaço de trabalho da Braze
- Tipo de cartão

Use **Export** para baixar os dados da tabela.

![Uso de créditos de Content Cards com blocos para créditos e impressões únicas e uma tabela de uso por conta.]({% image_buster /assets/img/app_settings/credits_usage_content_cards.png %})

{% endtab %}
{% tab Email %}

### E-mail {#email}

**Email Credits Usage** mostra o uso de créditos de e-mail em todas as contas. Os blocos mostram o total de créditos consumidos e o total de e-mails enviados. A tabela **Usage by account** inclui **Braze workspace**, **Email sent**, **Credit ratio** e **Credits**. Quando há dados disponíveis, **Last updated** mostra quando a tabela foi atualizada.

#### Filtros

Você pode filtrar seus dados por:
- Período (padrão: últimos 30 dias)
- Espaço de trabalho da Braze

Use **Export** para baixar os dados da tabela.

![Uso de créditos de e-mail com blocos para créditos e e-mails enviados e uma tabela de uso por conta.]({% image_buster /assets/img/app_settings/credits_usage_email.png %})

{% endtab %}
{% tab KakaoTalk %}

### KakaoTalk

**KakaoTalk Credits Usage** mostra o uso de créditos de KakaoTalk em todas as contas. Os blocos mostram o total de créditos consumidos e o total de envios de KakaoTalk. A tabela da seção **KakaoTalk** inclui **Braze workspace**, **Month**, **Year**, **Company**, **Sends**, **Credit Ratio** e **Credits**. Quando há dados disponíveis, **Last updated** mostra quando a tabela foi atualizada.

#### Filtros

Você pode filtrar seus dados por:
- Período (padrão: últimos 30 dias)
- Espaço de trabalho da Braze
- Mês
- Ano
- Empresa

Use **Export** para baixar os dados da tabela.

![Uso de créditos de KakaoTalk com blocos para créditos e envios de KakaoTalk e uma tabela de uso.]({% image_buster /assets/img/app_settings/credits_usage_kakaotalk.png %})

{% endtab %}
{% tab LINE %}

### LINE

**LINE Credits Usage** mostra o uso de créditos de LINE em todas as contas. Os blocos mostram o total de créditos consumidos e o total de envios faturáveis. A tabela da seção **Line** inclui **Braze workspace**, **Month**, **Year**, **Company**, **Destination**, **Billable sends**, **Credit ratio** e **Credits**. Quando há dados disponíveis, **Last updated** mostra quando a tabela foi atualizada.

#### Filtros

Você pode filtrar seus dados por:
- Período (padrão: últimos 30 dias)
- Espaço de trabalho da Braze
- Mês
- Ano
- Empresa
- Destino

Use **Export** para baixar os dados da tabela.

![Uso de créditos de LINE com blocos para créditos e envios faturáveis e uma tabela detalhada de uso.]({% image_buster /assets/img/app_settings/credits_usage_line.png %})

{% endtab %}
{% tab SMS, MMS, and RCS %}

### SMS, MMS e RCS {#sms-mms-and-rcs}

**SMS/MMS/RCS Credits Usage** mostra o detalhamento de uso para os canais SMS, MMS e RCS. As colunas **Credit ratio** e **Credits** indicam a taxa do respectivo país e os créditos consumidos. Além disso, os blocos de alto nível indicam o consumo total de SMS e, quando aplicável, de MMS no período selecionado.

Filtros estão disponíveis para filtrar por **Country** ou tipo de SMS e RCS.

![Uso de créditos de SMS/MMS/RCS com blocos para dados de alto nível e uma seção de consumo por conta.]({% image_buster /assets/img/app_settings/sms_credit_consumption2.png %})

Diferentemente da **Visão geral de uso de créditos**, esta seção contém dados históricos de períodos contratuais anteriores.

{% alert note %}
É possível selecionar um período que contenha uso com e sem créditos. Nesse caso, o consumo que ocorreu fora do modelo de créditos exibirá `—` (nulo) nas colunas **Credit ratio** e **Credits**.
{% endalert %}

![Tabela de uso de créditos de SMS/MMS/RCS com valores nulos.]({% image_buster /assets/img/app_settings/sms_table_null3.png %})

{% endtab %}
{% tab Webhooks %}

### Webhooks

**Webhooks Credits Usage** mostra o uso de créditos de webhooks em todas as contas. Os blocos mostram o total de créditos consumidos e o total de envios de webhook. A tabela **Usage by account** inclui **Braze workspace**, **Sends**, **Credit ratio** e **Credits**. Quando há dados disponíveis, **Last updated** mostra quando a tabela foi atualizada.

#### Filtros

Você pode filtrar seus dados por:
- Período (padrão: últimos 30 dias)
- Espaço de trabalho da Braze

Use **Export** para baixar os dados da tabela.

![Uso de créditos de webhooks com blocos para créditos e envios de webhook e uma tabela de uso por conta.]({% image_buster /assets/img/app_settings/credits_usage_webhooks.png %})

{% endtab %}
{% tab WhatsApp %}

### WhatsApp

**WhatsApp Credits Usage** mostra o detalhamento de uso para o canal WhatsApp. Os blocos exibem o total de uso de créditos de WhatsApp, que pode ser detalhado na seção **Usage by account** aplicando filtros para limitar os resultados da tabela a um espaço de trabalho específico.

#### Filtros

Você pode filtrar seus dados por:
- País
- Conta WhatsApp Business
- Espaço de trabalho da Braze
- Tipo de categoria de conversa
- Região

![Uso de créditos de WhatsApp com um bloco para o total de créditos consumidos e uma tabela de uso por conta.]({% image_buster /assets/img/app_settings/whatsapp_credit_consumption4.png %})

{% endtab %}
{% tab Credit Ratios %}

### Taxas de crédito {#credit-ratios}

**Credit Ratios** mostra as taxas de crédito em diferentes canais e destinos. Não há blocos de resumo nem controle de **Date range** nesta página. A tabela **Credit ratios** inclui **Channel grouping**, **Destination** e **Credit ratio**.

#### Filtros

Você pode filtrar seus dados por:
- Agrupamento de canal
- Destino

Use **Export** para baixar os dados da tabela.

![Página de taxas de crédito com uma tabela de taxas de crédito e filtros de canal e destino.]({% image_buster /assets/img/app_settings/credits_usage_credit_ratios.png %})

{% endtab %}
{% tab Agent Console %}

### Agent Console

**Agent Console Credits Usage** mostra o uso de créditos do Agent Console em todas as contas. Os blocos mostram o total de créditos consumidos e o total de invocações. A tabela **Usage by account** inclui **Braze workspace**, **Agent name**, **Model owner**, **Total invocations**, **Credit ratio** e **Credits**. Quando há dados disponíveis, **Last updated** mostra quando a tabela foi atualizada.

Para planejar o gasto diário antes do lançamento, compare essas taxas com o **Daily action credit cost limit** de cada agente no Agent Console (limite de invocações diárias × taxa de crédito). Consulte [Limites diários de invocação e créditos]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits).

#### Filtros

Você pode filtrar seus dados por:
- Período (padrão: últimos 30 dias)
- Espaço de trabalho da Braze
- Nome do agente
- Proprietário do modelo

Use **Export** para baixar os dados da tabela.

![Uso de créditos do Agent Console com blocos para créditos e invocações e uma tabela de uso por conta.]({% image_buster /assets/img/app_settings/credits_usage_agent_console.png %})

{% endtab %}
{% tab Audience Sync %}

### Audience Sync

**Audience Sync Credits Usage** mostra o uso de créditos de Audience Sync em todas as contas. Os blocos mostram o total de créditos consumidos e o total de sincronizações de público. A tabela **Usage by account** inclui **Braze workspace**, **Provider**, **Total syncs**, **Credit ratio** e **Credits**. Quando há dados disponíveis, **Last updated** mostra quando a tabela foi atualizada.

#### Filtros

Você pode filtrar seus dados por:
- Período (padrão: últimos 30 dias)
- Espaço de trabalho da Braze
- Provedor

Use **Export** para baixar os dados da tabela.

![Uso de créditos de Audience Sync com blocos para créditos e sincronizações de público e uma tabela de uso por conta.]({% image_buster /assets/img/app_settings/credits_usage_audience_sync.png %})

{% endtab %}
{% tab Message Archiving %}

### Arquivamento de mensagens {#message-archiving}

**Message Archiving Credits Usage** mostra o uso de créditos de arquivamento de mensagens em todas as contas. Os blocos mostram o total de créditos consumidos e o total de mensagens arquivadas. A tabela **Usage by account** inclui **Braze workspace**, **Channel**, **Messages archived**, **Credit ratio** e **Credits**. Quando há dados disponíveis, **Last updated** mostra quando a tabela foi atualizada.

#### Filtros

Você pode filtrar seus dados por:
- Período (padrão: últimos 30 dias)
- Espaço de trabalho da Braze
- Canal

Use **Export** para baixar os dados da tabela.

![Uso de créditos de arquivamento de mensagens com blocos para créditos e mensagens arquivadas e uma tabela de uso por conta.]({% image_buster /assets/img/app_settings/credits_usage_message_archiving.png %})

{% endtab %}
{% endtabs %}

## Informações importantes {#things-to-know}

{% alert important %}
Os dados exibidos no dashboard de **Credits Usage** estão no nível do contrato e não são limitados a uma empresa ou espaço de trabalho individual do dashboard. Esses dados refletem o uso de todos os espaços de trabalho dentro do seu dashboard e, potencialmente, de todos os dashboards (caso você tenha mais de um).
{% endalert %}

- Os dados subjacentes são fornecidos em cadência diária, com as tabelas de dados atualizadas às 3h, 9h, 12h e 18h (horário do leste dos EUA). O dashboard de **Credits Usage** pode levar mais de 24 horas para ser atualizado.
- Quando um novo período de contrato começa, as informações atualizadas de contrato e créditos de mensagem podem levar até 24 horas para aparecer. Até que esses dados sejam carregados, o dashboard pode exibir apenas a guia **Credit Ratios** em vez da visão geral completa e dos detalhes de uso por canal.
- A Braze segue a metodologia padrão de arredondamento: os números são arredondados para o décimo mais próximo.

### Seleção de período {#date-range-selection}

O dashboard de **Credits Usage** exclui a data final do intervalo selecionado dos resultados. Por exemplo, se você selecionar 1 a 31 de outubro, as estatísticas de uso do dia 31 de outubro serão excluídas. Para incluir o último dia do período desejado, estenda o intervalo em um dia. Por exemplo, para incluir todo o mês de outubro, selecione 1 de outubro a 1 de novembro.

### Comparação com provedores terceiros {#comparing-with-third-party-providers}

Ao comparar os dados de uso de créditos da Braze com provedores terceiros (como Infobip), tenha em mente:

- **Segmentos de mensagem versus mensagens**: a Braze conta mensagens SMS por segmentos. Uma única mensagem SMS que é dividida em múltiplos segmentos (por exemplo, devido ao tamanho) é contada como múltiplos segmentos na Braze. Para saber mais, consulte [Calculadoras de faturamento de SMS e RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments).
- **Mensagens baseadas em crédito versus não baseadas em crédito**: o dashboard inclui tanto mensagens baseadas em crédito quanto não baseadas em crédito. Provedores terceiros podem contar apenas mensagens baseadas em crédito, o que pode causar discrepâncias nos totais.
- **Entrada versus saída**: certifique-se de que você está comparando os mesmos tipos de mensagem. Alguns dashboards de terceiros incluem tanto mensagens de entrada quanto de saída em seus totais, enquanto a Braze permite que você filtre por direção.
- **Alinhamento do período**: como o dashboard exclui a data final, comparações dia a dia podem ser mais precisas do que comparações de períodos mais longos. Se você estiver comparando dados de um período específico, estenda o período na Braze em um dia para incluir o último dia do seu período de comparação.