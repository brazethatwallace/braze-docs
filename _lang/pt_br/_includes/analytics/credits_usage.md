# Dashboard de uso de créditos {#credits-usage-dashboard}

> O dashboard de uso de créditos fornece insights de autoatendimento sobre o consumo de créditos, oferecendo uma visão abrangente do uso histórico e atual em comparação com as alocações contratuais. Esses insights podem reduzir suas dúvidas e ajudar você a fazer ajustes para evitar riscos de excedente.

O dashboard **Credits Usage** é dividido em duas seções:
- [Visão geral do uso de créditos](#credits-usage-overview)
- [Guias de canais](#credits-features)

Acesse o dashboard em **Configurações** > **Billing** > **Credits Usage**.

## Visão geral do uso de créditos {#credits-usage-overview}

A **Message credit usage overview** fornece uma visão geral do uso em todos os canais que consomem créditos. Você pode ver como está o ritmo de consumo em relação à sua alocação total de créditos e encontrar informações sobre seu contrato ativo e o período contratual.

Esta página é exibida se você estiver em um contrato de créditos. Os canais que consomem créditos são mostrados em **Credits usage**.

{% alert note %}
Se você adquiriu o WhatsApp, mas não está em um contrato de créditos, ainda verá o consumo de créditos para o WhatsApp, pois é assim que os contratos legados de WhatsApp são cobrados. Isso difere do SMS legado, que só consome créditos quando você está em um contrato de créditos.
{% endalert %}

Os dados da visão geral de uso de créditos são limitados ao período contratual, exibido em **Credits contract overview**. Não é possível filtrar por um intervalo de datas fora do **Credits period**.


### Uso de créditos ao longo do contrato {#credits-usage-over-contract}

O gráfico **Message credits usage over contract** mostra seu uso ao longo do período selecionado. A granularidade deste gráfico depende do período selecionado. Veja as opções de exportação selecionando o menu no menu do gráfico.

![Gráfico de uso de créditos ao longo do contrato.]({% image_buster /assets/img/app_settings/credit_usage_over_contract1.png %})

## Guia Visão geral {#overview-tab}

A guia **Overview Usage** mostra o uso de créditos nos canais aplicáveis à sua empresa. Por exemplo, se você não tem WhatsApp, a guia correspondente não aparecerá.

### Recursos de créditos {#credits-features}

Consulte as guias a seguir para ver os detalhes do que é exibido para cada recurso que consome créditos.

{% tabs %}
{% tab Banners %}

### Banners

**Banners Credits Usage** mostra o uso de créditos de Banners em todas as contas. Os blocos mostram o total de créditos consumidos e o total de impressões únicas diárias. A tabela **Usage by account** inclui **Braze workspace**, **Daily unique impressions**, **Credit ratio** e **Credits**. Quando os dados estão disponíveis, **Last updated** mostra quando a tabela foi atualizada.

#### Filtros {#filters}

Você pode filtrar seus dados por:
- Intervalo de datas (padrão: últimos 30 dias)
- Espaço de trabalho da Braze

Use **Export** para baixar os dados da tabela.

![Uso de créditos de Banners com blocos de créditos e impressões únicas e uma tabela de uso por conta.]({% image_buster /assets/img/app_settings/credits_usage_banners.png %})

{% endtab %}
{% tab Content Cards %}

### Content Cards

**Content Cards Credits Usage** mostra o uso de créditos de Content Cards em todas as contas. Os blocos mostram o total de créditos consumidos e o total de impressões únicas diárias. A tabela **Usage by account** inclui **Braze workspace**, **Card type**, **Daily Unique Impressions**, **Credit ratio** e **Credits**. Quando os dados estão disponíveis, **Last updated** mostra quando a tabela foi atualizada.

#### Filtros

Você pode filtrar seus dados por:
- Intervalo de datas (padrão: últimos 30 dias)
- Espaço de trabalho da Braze
- Tipo de cartão

Use **Export** para baixar os dados da tabela.

![Uso de créditos de Content Cards com blocos de créditos e impressões únicas e uma tabela de uso por conta.]({% image_buster /assets/img/app_settings/credits_usage_content_cards.png %})

{% endtab %}
{% tab E-mail %}

### E-mail {#email}

**Email Credits Usage** mostra o uso de créditos de e-mail em todas as contas. Os blocos mostram o total de créditos consumidos e o total de e-mails enviados. A tabela **Usage by account** inclui **Braze workspace**, **Email sent**, **Credit ratio** e **Credits**. Quando os dados estão disponíveis, **Last updated** mostra quando a tabela foi atualizada.

#### Filtros

Você pode filtrar seus dados por:
- Intervalo de datas (padrão: últimos 30 dias)
- Espaço de trabalho da Braze

Use **Export** para baixar os dados da tabela.

![Uso de créditos de e-mail com blocos de créditos e e-mails enviados e uma tabela de uso por conta.]({% image_buster /assets/img/app_settings/credits_usage_email.png %})

{% endtab %}
{% tab KakaoTalk %}

### KakaoTalk

**KakaoTalk Credits Usage** mostra o uso de créditos do KakaoTalk em todas as contas. Os blocos mostram o total de créditos consumidos e o total de envios do KakaoTalk. A tabela da seção **KakaoTalk** inclui **Braze workspace**, **Month**, **Year**, **Company**, **Sends**, **Credit Ratio** e **Credits**. Quando os dados estão disponíveis, **Last updated** mostra quando a tabela foi atualizada.

#### Filtros

Você pode filtrar seus dados por:
- Intervalo de datas (padrão: últimos 30 dias)
- Espaço de trabalho da Braze
- Mês
- Ano
- Empresa

Use **Export** para baixar os dados da tabela.

![Uso de créditos do KakaoTalk com blocos de créditos e envios do KakaoTalk e uma tabela de uso.]({% image_buster /assets/img/app_settings/credits_usage_kakaotalk.png %})

{% endtab %}
{% tab LINE %}

### LINE

**LINE Credits Usage** mostra o uso de créditos do LINE em todas as contas. Os blocos mostram o total de créditos consumidos e o total de envios faturáveis. A tabela da seção **Line** inclui **Braze workspace**, **Month**, **Year**, **Company**, **Destination**, **Billable sends**, **Credit ratio** e **Credits**. Quando os dados estão disponíveis, **Last updated** mostra quando a tabela foi atualizada.

#### Filtros

Você pode filtrar seus dados por:
- Intervalo de datas (padrão: últimos 30 dias)
- Espaço de trabalho da Braze
- Mês
- Ano
- Empresa
- Destino

Use **Export** para baixar os dados da tabela.

![Uso de créditos do LINE com blocos de créditos e envios faturáveis e uma tabela detalhada de uso.]({% image_buster /assets/img/app_settings/credits_usage_line.png %})

{% endtab %}
{% tab SMS, MMS e RCS %}

### SMS, MMS e RCS {#sms-mms-and-rcs}

**SMS/MMS/RCS Credits Usage** mostra o detalhamento de uso para os canais SMS, MMS e RCS. As colunas **Credit ratio** e **Credits** indicam a taxa do respectivo país e os créditos consumidos. Além disso, os blocos de alto nível indicam o consumo total de SMS e, quando relevante, de MMS no intervalo de datas selecionado.

Filtros estão disponíveis para filtrar por **Country** ou tipo de SMS e RCS.

![Uso de créditos de SMS/MMS/RCS com blocos de dados de alto nível e uma seção de consumo por conta.]({% image_buster /assets/img/app_settings/sms_credit_consumption2.png %})

Diferentemente da **Credits Usage Overview**, esta seção contém dados históricos de períodos contratuais anteriores.

{% alert note %}
É possível selecionar um intervalo de datas que contenha uso com e sem créditos. Nesse caso, o consumo que ocorreu fora do regime de créditos exibirá `—` (nulo) nas colunas **Credit ratio** e **Credits**.
{% endalert %}

![Tabela de uso de créditos de SMS/MMS/RCS com valores nulos.]({% image_buster /assets/img/app_settings/sms_table_null3.png %})

{% endtab %}
{% tab Webhooks %}

### Webhooks

**Webhooks Credits Usage** mostra o uso de créditos de webhooks em todas as contas. Os blocos mostram o total de créditos consumidos e o total de envios de webhook. A tabela **Usage by account** inclui **Braze workspace**, **Sends**, **Credit ratio** e **Credits**. Quando os dados estão disponíveis, **Last updated** mostra quando a tabela foi atualizada.

#### Filtros

Você pode filtrar seus dados por:
- Intervalo de datas (padrão: últimos 30 dias)
- Espaço de trabalho da Braze

Use **Export** para baixar os dados da tabela.

![Uso de créditos de webhooks com blocos de créditos e envios de webhook e uma tabela de uso por conta.]({% image_buster /assets/img/app_settings/credits_usage_webhooks.png %})

{% endtab %}
{% tab WhatsApp %}

### WhatsApp

**WhatsApp Credits Usage** mostra o detalhamento de uso para o canal WhatsApp. Os blocos exibem o total de créditos consumidos pelo WhatsApp, que pode ser detalhado na seção **Usage by account** aplicando filtros para limitar os resultados da tabela a um espaço de trabalho específico.

#### Filtros

Você pode filtrar seus dados por:
- País
- Conta WhatsApp Business
- Espaço de trabalho da Braze
- Tipo de categoria de conversa
- Região

![Uso de créditos do WhatsApp com um bloco de total de créditos consumidos e uma tabela de uso por conta.]({% image_buster /assets/img/app_settings/whatsapp_credit_consumption4.png %})

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

**Agent Console Credits Usage** mostra o uso de créditos do Agent Console em todas as contas. Os blocos mostram o total de créditos consumidos e o total de invocações. A tabela **Usage by account** inclui **Braze workspace**, **Agent name**, **Model owner**, **Total invocations**, **Credit ratio** e **Credits**. Quando os dados estão disponíveis, **Last updated** mostra quando a tabela foi atualizada.

Para planejar o gasto diário antes do lançamento, compare essas taxas com o **Daily action credit cost limit** de cada agente no Agent Console (limite diário de invocações × taxa de crédito). Consulte [Limites diários de invocação e crédito]({{site.baseurl}}/user_guide/brazeai/agents/reference#daily-invocation-and-credit-limits).

#### Filtros

Você pode filtrar seus dados por:
- Intervalo de datas (padrão: últimos 30 dias)
- Espaço de trabalho da Braze
- Nome do agente
- Proprietário do modelo

Use **Export** para baixar os dados da tabela.

![Uso de créditos do Agent Console com blocos de créditos e invocações e uma tabela de uso por conta.]({% image_buster /assets/img/app_settings/credits_usage_agent_console.png %})

{% endtab %}
{% tab Audience Sync %}

### Audience Sync

**Audience Sync Credits Usage** mostra o uso de créditos do Audience Sync em todas as contas. Os blocos mostram o total de créditos consumidos e o total de sincronizações de público. A tabela **Usage by account** inclui **Braze workspace**, **Provider**, **Total syncs**, **Credit ratio** e **Credits**. Quando os dados estão disponíveis, **Last updated** mostra quando a tabela foi atualizada.

#### Filtros

Você pode filtrar seus dados por:
- Intervalo de datas (padrão: últimos 30 dias)
- Espaço de trabalho da Braze
- Provedor

Use **Export** para baixar os dados da tabela.

![Uso de créditos do Audience Sync com blocos de créditos e sincronizações de público e uma tabela de uso por conta.]({% image_buster /assets/img/app_settings/credits_usage_audience_sync.png %})

{% endtab %}
{% tab Message Archiving %}

### Message Archiving

**Message Archiving Credits Usage** mostra o uso de créditos de Message Archiving em todas as contas. Os blocos mostram o total de créditos consumidos e o total de mensagens arquivadas. A tabela **Usage by account** inclui **Braze workspace**, **Channel**, **Messages archived**, **Credit ratio** e **Credits**. Quando os dados estão disponíveis, **Last updated** mostra quando a tabela foi atualizada.

#### Filtros

Você pode filtrar seus dados por:
- Intervalo de datas (padrão: últimos 30 dias)
- Espaço de trabalho da Braze
- Canal

Use **Export** para baixar os dados da tabela.

![Uso de créditos de Message Archiving com blocos de créditos e mensagens arquivadas e uma tabela de uso por conta.]({% image_buster /assets/img/app_settings/credits_usage_message_archiving.png %})

{% endtab %}
{% endtabs %}

## Informações importantes {#things-to-know}

{% alert important %}
Os dados exibidos no dashboard **Credits Usage** estão no nível do contrato e não são limitados a uma empresa ou espaço de trabalho individual do dashboard. Esses dados refletem o uso de todos os espaços de trabalho dentro do seu dashboard e, potencialmente, de todos os dashboards (se você tiver múltiplos).
{% endalert %}

- Os dados subjacentes são fornecidos em cadência diária, com as tabelas de dados atualizadas às 3h, 9h, 12h e 18h EST. O dashboard **Credits Usage** pode levar mais de 24 horas para ser atualizado.
- A Braze segue a metodologia padrão de arredondamento: os números são arredondados para o décimo mais próximo.

### Seleção de intervalo de datas {#date-range-selection}

O dashboard **Credits Usage** exclui a data final do intervalo selecionado dos resultados. Por exemplo, se você selecionar 1 a 31 de outubro, as estatísticas de uso de 31 de outubro serão excluídas. Para incluir o último dia do período desejado, estenda o intervalo em um dia. Por exemplo, para incluir todo o mês de outubro, selecione 1 de outubro a 1 de novembro.

### Comparação com provedores terceiros {#comparing-with-third-party-providers}

Ao comparar os dados de uso de créditos da Braze com provedores terceiros (como Infobip), tenha em mente:

- **Segmentos de mensagem versus mensagens**: a Braze conta mensagens SMS por segmentos. Uma única mensagem SMS dividida em múltiplos segmentos (por exemplo, devido ao tamanho) é contada como múltiplos segmentos na Braze. Para saber mais, consulte [Calculadoras de cobrança de SMS e RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments).
- **Mensagens baseadas em créditos versus não baseadas em créditos**: o dashboard inclui tanto mensagens baseadas em créditos quanto não baseadas em créditos. Provedores terceiros podem contar apenas mensagens baseadas em créditos, o que pode causar discrepâncias nos totais.
- **Entrada versus saída**: certifique-se de que você está comparando os mesmos tipos de mensagem. Alguns dashboards de terceiros incluem mensagens de entrada e saída em seus totais, enquanto a Braze permite filtrar por direção.
- **Alinhamento do intervalo de datas**: como o dashboard exclui a data final, comparações dia a dia podem se alinhar mais precisamente do que intervalos de datas mais longos. Se você estiver comparando dados de um período específico, estenda o intervalo de datas da Braze em um dia para incluir o último dia do período de comparação.