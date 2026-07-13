---
nav_title: Calculadora de faturamento
article_title: Calculadora de faturamento
page_order: 5
description: "Este artigo de referência aborda o que é um segmento de mensagem SMS, como eles são contabilizados para faturamento, além de pontos importantes a considerar ao criar textos de mensagens SMS e RCS."
page_type: reference
alias: /sms_rcs_billing_calculators/
tool:
  - Testing Tools
channel:
  - SMS
  - MMS
  - RCS

---

# Calculadoras de faturamento de SMS e RCS {#sms-and-rcs-billing-calculators}

> Na Braze, as mensagens SMS são cobradas por segmento de mensagem, enquanto as mensagens RCS são cobradas por mensagem. Entender o que define um segmento de SMS e os diferentes tipos de faturamento de RCS ajudará você a compreender como será cobrado e a evitar excedentes acidentais.

## Texto de mensagem SMS e calculadora de segmentos {#sms-message-copy-and-segment-calculator}

As mensagens SMS são cobradas por segmento de mensagem. Entender como as mensagens SMS são divididas é fundamental para compreender seu faturamento.

### O que é um segmento de SMS? {#what-is-an-sms-segment}

O Serviço de Mensagens Curtas (SMS) é um protocolo de comunicação padronizado que permite que dispositivos enviem e recebam mensagens de texto breves. Ele foi projetado para "se encaixar entre" outros protocolos de sinalização, e é por isso que o comprimento das mensagens SMS é limitado a 160 caracteres de 7 bits, ou seja, 1120 bits, ou 140 bytes. Os segmentos de mensagem SMS são os lotes de caracteres que as operadoras de telefonia usam para medir as mensagens de texto. As mensagens são cobradas por segmento de mensagem, então os clientes que utilizam SMS se beneficiam muito ao entender as nuances de como as mensagens serão divididas.

Ao criar uma Campaign ou Canvas de SMS usando a Braze, as mensagens que você cria no criador são representativas do que seus usuários podem ver quando a mensagem for entregue em seus telefones, mas **não indicam como sua mensagem será dividida em segmentos e, em última análise, como você será cobrado**. Entender quantos segmentos serão enviados e estar ciente dos possíveis excedentes que podem ocorrer é sua responsabilidade, mas fornecemos alguns recursos para facilitar isso. Confira nossa [calculadora de segmentos](#segment-calculator) integrada.

![Ao criar uma Campaign ou Canvas de SMS usando a Braze, as mensagens que você cria no criador são representativas do que seus usuários podem ver quando a mensagem for entregue, mas não indicam como sua mensagem será dividida em segmentos e como você será cobrado. Entender quantos segmentos serão enviados e estar ciente dos possíveis excedentes é sua responsabilidade, mas fornecemos recursos para facilitar isso. Confira nossa calculadora de segmentos integrada.]({% image_buster /assets/img/sms_segment_pic.png %}){: style="border:0;"}

#### Detalhamento de segmentos {#segment-breakdown}

O limite de caracteres para **um segmento de SMS independente** é de 160 caracteres (codificação [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38)) ou 70 caracteres (codificação [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set)), dependendo do tipo de codificação. No entanto, a maioria dos telefones e redes suporta concatenação, oferecendo mensagens SMS mais longas de até 1530 caracteres (GSM-7) ou 670 caracteres (UCS-2). Então, embora uma mensagem possa incluir vários segmentos, se não exceder esses limites de concatenação, ela será visualizada como uma única mensagem e reportada como tal.

É importante observar que **ao ultrapassar o limite de caracteres do seu primeiro segmento, os caracteres adicionais farão com que toda a sua mensagem seja dividida e segmentada com base em novos limites de caracteres**:
- **Codificação GSM-7**
    - Mensagens que excedem o limite de 160 caracteres serão segmentadas em segmentos de 153 caracteres e enviadas individualmente, sendo reconstruídas pelo dispositivo do destinatário. Por exemplo, uma mensagem de 161 caracteres será enviada como duas mensagens, uma com 153 caracteres e a segunda com 8 caracteres.
- **Codificação UCS-2**
    - Se você incluir caracteres não GSM, como emojis, caracteres chineses, coreanos ou japoneses em mensagens SMS, essas mensagens precisarão ser enviadas via codificação UCS-2. Mensagens que excedem o limite inicial de 70 caracteres farão com que toda a mensagem seja concatenada em segmentos de 67 caracteres. Por exemplo, uma mensagem de 71 caracteres será enviada como duas mensagens, uma com 67 caracteres e a segunda com 4 caracteres.

Independentemente do tipo de codificação, cada mensagem SMS enviada pela Braze tem um limite de até 10 segmentos e é compatível com [modelos Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/using_liquid), [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content), emojis e links.

{% tabs %}
{% tab Codificação GSM-7 %}
| Número de caracteres | Quantos segmentos? |
| -------------------- | ----------------- |
| 0 - 160 caracteres | 1 segmento |
| 161 - 306 caracteres | 2 segmentos |
| 307 - 459 caracteres | 3 segmentos |
| 460 - 612 caracteres | 4 segmentos |
| 613 - 765 caracteres | 5 segmentos |
| 766 - 918 caracteres | 6 segmentos |
| 919 - 1071 caracteres | 7 segmentos |
| 1072 - 1224 caracteres | 8 segmentos |
| 1225 - 1377 caracteres | 9 segmentos |
| 1378 - 1530 caracteres | 10 segmentos |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Detalhamento de segmentos" }
{% endtab %}
{% tab Codificação UCS-2 %}
| Número de caracteres | Quantos segmentos? |
| -------------------- | ----------------- |
| 0 - 70 caracteres | 1 segmento |
| 71 - 134 caracteres | 2 segmentos |
| 135 - 201 caracteres | 3 segmentos |
| 202 - 268 caracteres | 4 segmentos |
| 269 - 335 caracteres | 5 segmentos |
| 336 - 402 caracteres | 6 segmentos |
| 403 - 469 caracteres | 7 segmentos |
| 470 - 536 caracteres | 8 segmentos |
| 537 - 603 caracteres | 9 segmentos |
| 604 - 670 caracteres | 10 segmentos |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Detalhamento de segmentos" }
{% endtab %}
{% endtabs %}

### Pontos importantes ao criar seu texto {#things-to-keep-in-mind-as-you-create-your-copy}

- **Limite de caracteres por segmento**
    - [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) tem um limite de 160 caracteres para um único segmento de SMS. Para mensagens com mais de 160 caracteres, todas as mensagens serão segmentadas com um limite de 153 caracteres.
    - [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set) tem um limite de 70 caracteres por segmento de mensagem. Para mensagens com mais de 70 caracteres, todas as mensagens serão segmentadas com um limite de 67 caracteres.<br><br>
- **Limite de segmentos por mensagem**
    - Existe uma quantidade máxima de segmentos que você pode enviar devido às limitações do meio. Não mais do que **10 segmentos** de mensagens podem ser enviados em uma única mensagem SMS da Braze.
    - Esses 10 segmentos serão limitados a 1530 caracteres (codificação GSM-7) ou 670 caracteres (codificação UCS-2).<br><br>
- **Compatível com modelos Liquid, Conteúdo conectado, emojis e links**
    - Modelos Liquid e Conteúdo conectado podem fazer com que sua mensagem ultrapasse o limite de caracteres para o seu tipo de codificação. Você pode usar o [filtro truncate words](https://help.shopify.com/en/themes/liquid/filters/string-filters#truncatewords) para limitar o número de palavras que o Liquid pode adicionar à mensagem.
    - Emojis não têm uma contagem de caracteres padrão entre todos os emojis, então certifique-se de testar se suas mensagens estão sendo segmentadas e exibidas corretamente.
    - Links podem usar muitos caracteres, resultando em mais segmentos de mensagem do que o pretendido. Embora o uso de encurtadores de links seja possível, eles funcionam melhor com códigos curtos. Visite nosso [FAQ de SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/faqs) para mais informações.<br><br>
- **Testes**
    - Sempre teste suas mensagens SMS antes do lançamento, especialmente ao usar Liquid e Conteúdo conectado, pois ultrapassar os limites de mensagem ou texto pode resultar em cobranças adicionais. Observe que as mensagens de teste contam para seus limites de mensagem.

### Calculadora de segmentos de SMS {#segment-calculator}
---

{% multi_lang_include alerts/tip_alerts.md alert='SMS segment calculator' %}

## Faturamento de mensagens RCS {#rcs-message-billing}

As mensagens RCS são cobradas com base em seu conteúdo e no país em que a mensagem é entregue. Para estimar os custos com precisão, é essencial entender os diferentes tipos de mensagem e como eles são cobrados.

### Tipos de faturamento RCS {#rcs-billing-types}

Nossa plataforma suporta dois modelos principais de faturamento: um modelo global e um modelo para os Estados Unidos.

#### Modelo global (mercados fora dos EUA) {#global-model-non-us-markets}

As mensagens são cobradas por mensagem e classificadas como Básica ou Individual.

{% tabs local %}
{% tab Básica %}

As mensagens RCS básicas são mensagens somente de texto com até 160 caracteres e são cobradas como uma única mensagem.

{% alert note %}
Adicionar botões ou qualquer elemento rico mudará o tipo de mensagem para uma mensagem RCS Individual.
{% endalert %}

{% endtab %}
{% tab Individual %}

As mensagens RCS individuais são mensagens com mais de 160 caracteres OU que incluem qualquer elemento rico, como botões ou mídia. Elas são cobradas como uma única mensagem, independentemente do comprimento da mensagem.

{% alert note %}
Enviar uma mensagem de texto e um arquivo de mídia separado ainda é cobrado como duas mensagens distintas.
{% endalert %}

{% endtab %}
{% endtabs %}

#### Modelo dos Estados Unidos {#united-states-model}

As mensagens são categorizadas como Rich ou Rich Media.

{% tabs local %}
{% tab Mensagens Rich %}

As mensagens Rich são mensagens somente de texto com ou sem botões. Elas são cobradas por segmento, com cada segmento limitado a 160 bytes UTF-8, o que significa que **o número de caracteres por segmento não é fixo**. Uma mensagem com apenas 160 caracteres em inglês simples é um segmento, mas uma mensagem com texto mais longo e emojis pode ter múltiplos segmentos.

{% endtab %}
{% tab Mensagens Rich Media %}

As mensagens Rich Media incluem um arquivo de mídia (imagem, vídeo) ou um Rich Card e são cobradas como uma única mensagem.

{% endtab %}
{% endtabs %}

### Criador de mensagens e dashboard de uso de créditos {#message-composer-and-credits-usage-dashboard}

Ao criar sua mensagem, o criador de mensagens exibirá o tipo de faturamento em tempo real por meio de um rótulo (Basic RCS, Single RCS, Rich ou Rich Media), ajudando você a acompanhar os custos antes de enviar.

Seu [dashboard de uso de créditos]({{site.baseurl}}/credits_usage_dashboard) refletirá esses tipos de faturamento e fornecerá o número de segmentos usados para mensagens dos EUA, oferecendo uma visão transparente do consumo de créditos de mensagem.