# Painel de uso de mensagens {#message-usage-dashboard}

> O painel de uso de mensagens fornece insights de autoatendimento sobre o uso de créditos de SMS, RCS e WhatsApp para uma visão abrangente do uso histórico e atual em comparação com as alocações contratuais. Esses insights podem reduzir suas dúvidas e ajudar você a fazer ajustes para prevenir riscos de excedente.

O painel **Message Usage** é dividido em três seções:
- [Visão geral do uso de créditos](#credit-usage-overview)
- [SMS/MMS](#smsmms)
- [WhatsApp](#whatsapp)

Acesse o dashboard indo para **Configurações** > **Faturamento** > **Message Usage**.

## Visão geral do uso de créditos {#credits-usage-overview}

A **Credits Usage Overview** fornece uma visão geral do uso em todos os canais que utilizam créditos. Você pode ver como está seu ritmo em relação à sua alocação total de créditos e encontrar detalhes sobre seu contrato ativo e seu período de contrato.

Esta página é exibida se você está em um contrato de créditos. Os canais que usam créditos são mostrados na **Credits contract overview**.

{% alert note %}
Se você comprou o WhatsApp, mas não está em um contrato de créditos, ainda verá o consumo de créditos para o WhatsApp, porque é assim que os contratos legados do WhatsApp são cobrados. Isso difere do SMS legado, que consome créditos apenas quando você está em um contrato de créditos.
{% endalert %}

Os dados da **Credits Usage Overview** são limitados ao período do contrato, que é exibido na **Credits contract overview**. Você não pode filtrar em um intervalo de datas fora do **Credits period**.

### Uso de créditos ao longo do contrato {#credits-usage-over-contract}

O gráfico **Credits Usage over Contract** mostra seu uso durante o período de tempo selecionado. A granularidade deste gráfico depende do período de tempo selecionado. Acesse as opções de exportação selecionando o menu no canto superior direito do gráfico.

![Painel de visão geral do uso de créditos com seções para uso de créditos, visão geral do contrato de créditos e consumo de créditos ao longo do contrato.]({% image_buster /assets/img/app_settings/credit_usage_over_contract1.png %}){: style="max-width:70%;"}

## SMS, MMS e RCS {#sms-mms-and-rcs}

**SMS/MMS/RCS Credits Usage** mostra o detalhamento do uso para o canal SMS, MMS e RCS. As colunas na tabela de dados geralmente exigem que você tenha comprado créditos (embora a Braze ainda suporte modelos de cobrança mais antigos temporariamente), e as colunas **Credit ratio** e **Credits** indicam a respectiva taxa do país e os créditos consumidos. Além disso, os blocos de alto nível indicarão o consumo total de SMS e, quando relevante, de MMS ao longo do intervalo de datas selecionado.

Filtros estão disponíveis permitindo que você filtre por **Country** ou tipo de SMS e RCS.

![Uso de créditos SMS/MMS/RCS com blocos para dados de alto nível e uma seção para consumo por conta.]({% image_buster /assets/img/app_settings/sms_credit_consumption2.png %}){: style="max-width:70%;"}

Ao contrário da **Credits Usage Overview**, esta seção contém dados históricos de períodos contratuais anteriores.

{% alert note %}
É possível selecionar um intervalo de datas que contenha tanto o uso sem créditos quanto o uso com créditos. Neste caso, o consumo que ocorreu fora dos créditos será exibido como `—` (nulo) nas colunas **Credit ratio** e **Credits**.
{% endalert %}

![Tabela de uso de créditos SMS/MMS/RCS com valores nulos.]({% image_buster /assets/img/app_settings/sms_table_null3.png %}){: style="max-width:70%;"}

## WhatsApp {#whatsapp}

**WhatsApp Credits Usage** mostra o detalhamento de uso para o canal do WhatsApp. Os blocos exibem o uso total de créditos do WhatsApp, que pode ser detalhado na seção **Usage by account**, aplicando filtros para limitar os resultados da tabela de dados a um espaço de trabalho específico.

### Filtros {#filters}

Você pode filtrar seus dados por:
- País
- Conta do WhatsApp Business
- Espaço de trabalho da Braze
- Tipo de categoria de conversa
- Região

![Uso de créditos do WhatsApp com um bloco para créditos totais consumidos e uma tabela de uso por conta.]({% image_buster /assets/img/app_settings/whatsapp_credit_consumption4.png %}){: style="max-width:70%;"}

## O que você precisa saber {#things-to-know}

{% alert important %}
Os dados mostrados no painel **Message Usage** estão no nível do contrato e não estão restritos a uma empresa ou espaço de trabalho individual do dashboard. Esses dados refletem o uso de todos os espaços de trabalho dentro do seu dashboard e, potencialmente, de todos os dashboards (se você tiver múltiplos).
{% endalert %}

- Os dados subjacentes são fornecidos em uma cadência diária, com as tabelas de dados atualizadas às 3h, 9h, 12h e 18h EST. O painel **Message Usage** pode levar mais de 24 horas para atualizar.
- A Braze segue a metodologia padrão de arredondamento: os números são arredondados para cima até o décimo mais próximo.

### Seleção de intervalo de datas {#date-range-selection}

O painel **Message Usage** exclui a data final do intervalo selecionado dos resultados. Por exemplo, se você selecionar de 1 a 31 de outubro, as estatísticas de uso para 31 de outubro são excluídas. Para incluir o último dia do seu período desejado, estenda o intervalo em um dia. Por exemplo, para incluir todo o mês de outubro, selecione de 1 de outubro a 1 de novembro.

### Comparando com provedores de terceiros {#comparing-with-third-party-providers}

Ao comparar os dados de uso de mensagens da Braze com provedores de terceiros (como Infobip), tenha em mente:

- **Segmentos de mensagem vs mensagens**: A Braze conta mensagens SMS por segmentos. Uma única mensagem SMS que é dividida em vários segmentos (por exemplo, devido ao comprimento) é contada como vários segmentos na Braze. Para saber mais, consulte [Calculadoras de cobrança de SMS e RCS]({{site.baseurl}}/user_guide/message_building_by_channel/sms_mms_rcs/segments/).
- **Mensagens baseadas em crédito vs sem crédito**: O dashboard inclui mensagens tanto baseadas em crédito quanto sem crédito. Provedores de terceiros podem contar apenas mensagens baseadas em crédito, o que pode causar discrepâncias nos totais.
- **Entrada vs saída**: Certifique-se de que você está comparando os mesmos tipos de mensagens. Alguns dashboards de terceiros incluem tanto mensagens de entrada quanto de saída em seus totais, enquanto a Braze permite que você filtre por direção.
- **Alinhamento de intervalo de datas**: Como o dashboard exclui a data final, comparações dia a dia podem se alinhar mais de perto do que intervalos de datas mais longos. Se você está comparando dados para um período específico, estenda seu intervalo de datas na Braze em um dia para incluir o último dia do seu período de comparação.