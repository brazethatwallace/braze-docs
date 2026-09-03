---
nav_title: Descrições dos Créditos de Ação da Braze
permalink: "/message_credits_descriptions/"
hidden: true
noindex: true
hide_toc: true
---

# Descrições dos Créditos de Ação da Braze {#braze-action-credits-descriptions}

> Os Créditos de Ação oferecem uma estrutura flexível que permite acessar facilmente o envio de mensagens multicanal e produtos avançados de IA, maximizando seu orçamento de marketing. Comece engajando em um único canal ou região e expanda facilmente seu mix para incluir agentes de IA à medida que seu modelo de negócios, base de clientes e estratégias de engajamento evoluem.

Os Créditos de Ação podem ser aplicados em qualquer um dos canais e recursos apresentados nesta página.

Observe que a "Proporção de Créditos" referenciada nesta página é definida como o número exato de Créditos de Ação necessários para realizar a ação especificada.

## Índice {#table-of-contents}

- [Detalhes do canal de e-mail](#email-channel-details)
- [Detalhes dos canais SMS, MMS e RCS](#sms-mms-and-rcs-channel-details)
  - [Segmentos de SMS](#sms-segments)
  - [Mensagens MMS](#mms-messages)
  - [Tipos de RCS](#rcs-types)
- [Detalhes do canal WhatsApp](#whatsapp-channel-details)
  - [Detalhamento por região de faturamento](#billing-region-breakdown)
- [Detalhes do Agent Console](#agent-console-details)
- [Detalhes de canais adicionais](#additional-channel-details)
  - [LINE](#line)
  - [KakaoTalk](#kakaotalk)
  - [Content Cards](#content-cards)
  - [Banners](#banners)
  - [Audience Sync](#audience-sync)
  - [Arquivamento de mensagens](#message-archiving)
  - [Webhooks](#webhooks)

## Detalhes do canal de e-mail {#email-channel-details}

As taxas de crédito de e-mail são calculadas em incrementos de mil e-mails enviados (CPM) a partir da plataforma Braze.

{% alert note %}
Consulte nossa [documentação de e-mail]({{site.baseurl}}/user_guide/channels/email) para saber mais sobre nosso canal de e-mail.
{% endalert %}

## Detalhes do canal SMS, MMS e RCS {#sms-mms-and-rcs-channel-details}

As proporções de crédito de SMS e MMS são calculadas em incrementos de segmentos enviados pela plataforma da Braze. As proporções de crédito de RCS são calculadas em incrementos de tipos Basic e Rich Media, ou tipos Single e Rich Media entregues pela plataforma da Braze. Tanto os tipos de entrada quanto os de saída são cobrados.

{% alert note %}
Quando aplicável para esses canais, as taxas de operadora são cobradas separadamente (após o uso) e não são consideradas como parte dos Action Credits.
{% endalert %}

### Segmentos de SMS {#sms-segments}

O setor de SMS conta as mensagens em segmentos de mensagem SMS. Um segmento de mensagem é um agrupamento de até um número definido de caracteres (160 para codificação GSM-7; 67 para codificação UCS-2) que será enviado em um único despacho de SMS. Se você enviar um SMS com 161 caracteres usando codificação GSM-7, dois (2) segmentos de mensagem serão enviados. O envio de múltiplos segmentos de mensagem resultará em cobranças adicionais.

### Mensagens MMS {#mms-messages}

Para MMS, o limite da mensagem é de 5 MB (isso inclui o ativo multimídia e o tamanho do corpo da mensagem). Para maior segurança, a Braze recomenda não exceder 600 KB para o seu ativo multimídia e também incluir um corpo de mensagem.

### Tipos de RCS {#rcs-types}

O RCS é a próxima geração do SMS e MMS. Ele oferece os benefícios de um canal direto e de alto engajamento como o SMS, com recursos mais ricos que os consumidores modernos passaram a esperar, como conteúdo rich (imagens, vídeos, documentos), envio verificado e com identidade de marca, recursos interativos como respostas e ações sugeridas, e muito mais.

{% multi_lang_include pricing/rcs_billing_message_types.md %}

{% alert note %}
Consulte nossa [documentação de SMS e MMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs) para saber mais sobre nossas ofertas da família SMS.
{% endalert %}

## Detalhes do canal WhatsApp {#whatsapp-channel-details}

{% multi_lang_include whatsapp/about_credits.md content="h3" %}

## Detalhamento por região de faturamento {#billing-region-breakdown}

### América do Norte {#north-america}

Estados Unidos, Canadá

### Restante da África {#rest-of-africa}

Argélia, Angola, Benin, Botsuana, Burkina Faso, Burundi, Camarões, Chade, Congo, Eritreia, Etiópia, Gabão, Gâmbia, Gana, Guiné-Bissau, Costa do Marfim, Quênia, Lesoto, Libéria, Líbia, Madagascar, Malaui, Mali, Mauritânia, Marrocos, Moçambique, Namíbia, Níger, Ruanda, Senegal, Serra Leoa, Somália, Sudão do Sul, Sudão, Essuatíni, Tanzânia, Togo, Tunísia, Uganda, Zâmbia

### Restante da Ásia-Pacífico {#rest-of-asia-pacific}

Afeganistão, Austrália, Bangladesh, Camboja, China, Japão, Laos, Mongólia, Nepal, Nova Zelândia, Papua-Nova Guiné, Filipinas, Sri Lanka, Taiwan, Tajiquistão, Tailândia, Turcomenistão, Uzbequistão, Vietnã

### Restante da Europa Central e Oriental {#rest-of-central-eastern-europe}

Albânia, Armênia, Azerbaijão, Belarus, Bulgária, Croácia, República Tcheca, Geórgia, Grécia, Letônia, Lituânia, Macedônia, Moldávia, Sérvia, Eslováquia, Eslovênia, Ucrânia

### Restante da América Latina {#rest-of-latin-america}

Bolívia, Costa Rica, República Dominicana, Equador, El Salvador, Guatemala, Haiti, Honduras, Jamaica, Nicarágua, Panamá, Paraguai, Porto Rico, Uruguai, Venezuela

### Restante do Oriente Médio {#rest-of-middle-east}

Barein, Iraque, Jordânia, Kuwait, Líbano, Omã, Iêmen

### Restante da Europa Ocidental {#rest-of-western-europe}

Áustria, Bélgica, Dinamarca, Finlândia, Irlanda, Noruega, Portugal, Suécia, Suíça

{% alert note %}
Consulte nossa [documentação sobre WhatsApp]({{site.baseurl}}/user_guide/channels/whatsapp) para saber mais sobre nossas ofertas de WhatsApp.
{% endalert %}

## Detalhes do Agent Console {#agent-console-details}

As taxas de crédito do Agent Console são denominadas em incrementos de mil (1.000) Invocações realizadas a partir da plataforma Braze. Uma Invocação é registrada quando um Agent inicia uma chamada a um LLM. Por padrão, seu contrato inclui uma quantidade de invocações conforme especificado pela sua Edição da Plataforma para cada Período do seu Prazo de Assinatura. Invocações adicionais serão cobradas conforme seu Formulário de Pedido.

{% alert note %}
Consulte nossa [documentação do Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents) para saber mais sobre o Agent Console.
{% endalert %}

## Detalhes adicionais dos canais {#additional-channel-details}

### LINE {#line}

As proporções de crédito do LINE são calculadas em incrementos de mensagens LINE enviadas pela plataforma da Braze.

{% alert note %}
Consulte nossa [documentação do LINE]({{site.baseurl}}/user_guide/channels/line) para saber mais sobre como usar o LINE com a Braze.
{% endalert %}

### KakaoTalk {#kakaotalk}

As proporções de crédito do KakaoTalk são calculadas em incrementos de mensagens KakaoTalk enviadas pela plataforma da Braze.

{% alert note %}
Consulte nossa [documentação do KakaoTalk]({{site.baseurl}}/kakaotalk) para saber mais sobre como usar o KakaoTalk com a Braze.
{% endalert %}

### Content Cards {#content-cards}

As proporções de crédito de Content Cards são calculadas em incrementos de mil impressões únicas diárias.

A Braze reserva o direito de cobrar créditos por Content Cards com base no número de Content Cards enviados caso o cliente não configure os Content Cards para registrar impressões únicas de acordo com as orientações da Braze. Isso será considerado aplicável se, dentro de seis (6) meses após o primeiro envio de Content Cards, o cliente tiver:
- Enviado mais de cinco milhões (5.000.000) de Content Cards, E TAMBÉM
    - Zero (0) impressões registradas
    - Proporção de envios para impressões únicas diárias maior que cem (100)

{% alert note %}
Consulte nossa [documentação de Content Cards]({{site.baseurl}}/user_guide/channels/content_cards) para saber mais sobre Content Cards da Braze.
{% endalert %}

### Banners {#banners}

As proporções de crédito de Banners são calculadas em incrementos de mil impressões únicas diárias.

{% alert note %}
Consulte nossa [documentação de Banners]({{site.baseurl}}/developer_guide/banners) para saber mais sobre Banners da Braze.
{% endalert %}

### Audience Sync {#audience-sync}

As proporções de crédito do Audience Sync são calculadas em incrementos de mil sincronizações totais de usuários. Por padrão, seu contrato inclui cinco milhões de sincronizações de usuários por cada período do seu prazo de assinatura. Sincronizações adicionais serão cobradas conforme seu formulário de pedido.

{% alert note %}
Consulte nossa [documentação de Canvas]({{site.baseurl}}/partners/canvas_audience_sync) para saber mais sobre Canvas Audience Sync e parceiros disponíveis.
{% endalert %}

### Arquivamento de mensagens {#message-archiving}

As proporções de crédito do arquivamento de mensagens são calculadas em incrementos de mil mensagens arquivadas com sucesso nos canais push, e-mail, SMS/MMS e mensagens no app.

{% alert note %}
A partir de 2 de setembro de 2026, as tentativas de arquivamento com falha são excluídas da cobrança de uso; apenas os arquivamentos bem-sucedidos consomem Action Credits. Essa alteração não afeta o uso cobrado antes de 2 de setembro de 2026.
{% endalert %}

{% alert note %}
Consulte nossa [documentação de arquivamento de mensagens]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/message_archiving) para saber mais sobre o arquivamento de mensagens.
{% endalert %}

### Webhooks {#webhooks}

As proporções de crédito de webhooks são calculadas em incrementos de mil webhooks enviados com sucesso pela plataforma da Braze. Por padrão, seu contrato inclui cem mil webhooks por cada período do seu prazo de assinatura. Webhooks adicionais serão cobrados conforme seu formulário de pedido.

{% multi_lang_include pricing/webhook_failed_requests_billing.md credit_name='Action Credits' %}

{% alert note %}
Consulte nossa [documentação de webhooks]({{site.baseurl}}/user_guide/channels/webhooks) para saber mais sobre webhooks da Braze.
{% endalert %}