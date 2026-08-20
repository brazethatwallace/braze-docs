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

## Sumário {#table-of-contents}

- [Detalhes do canal de e-mail](#email-channel-details)
- [Detalhes dos canais SMS, MMS e RCS](#sms-mms-and-rcs-channel-details)
  - [Segmentos de SMS](#sms-segments)
  - [Mensagens MMS](#mms-messages)
  - [Tipos de RCS](#rcs-types)
- [Detalhes do canal WhatsApp](#whatsapp-channel-details)
  - [Detalhamento por região de cobrança](#billing-region-breakdown)
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
Consulte nossa [documentação de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email) para saber mais sobre nosso canal de e-mail.
{% endalert %}

## Detalhes dos canais SMS, MMS e RCS {#sms-mms-and-rcs-channel-details}

As proporções de créditos de SMS e MMS são calculadas em incrementos de segmentos enviados pela plataforma da Braze. As proporções de créditos de RCS são calculadas em incrementos de tipos Básico e Mídia Rica, ou tipos Simples e Mídia Rica entregues pela plataforma da Braze. Tanto os tipos de entrada quanto os de saída são cobrados.

{% alert note %}
Quando aplicável para esses canais, as taxas de operadora são cobradas separadamente (após o uso) e não são consideradas como parte dos Créditos de Ação.
{% endalert %}

### Segmentos de SMS {#sms-segments}

O setor de SMS conta as mensagens em segmentos de mensagem SMS. Um segmento de mensagem é um agrupamento de até um número definido de caracteres (160 para codificação GSM-7; 67 para codificação UCS-2) que será enviado em um único despacho de SMS. Se você enviar um SMS com 161 caracteres usando codificação GSM-7, dois (2) segmentos de mensagem serão enviados. O envio de múltiplos segmentos de mensagem resultará em cobranças adicionais.

### Mensagens MMS {#mms-messages}

Para MMS, o limite da mensagem é de 5 MB (isso inclui o ativo multimídia e o tamanho do corpo da mensagem). Para maior segurança, a Braze recomenda não exceder 600 KB para o seu ativo multimídia, incluindo também um corpo de mensagem.

### Tipos de RCS {#rcs-types}

O RCS é a próxima geração de SMS e MMS. Ele oferece os benefícios de um canal direto e de alto engajamento como o SMS, com recursos mais ricos que os consumidores modernos esperam, como conteúdo rico (imagens, vídeos, documentos), envio verificado e com marca, recursos interativos como respostas e ações sugeridas, e muito mais.

{% multi_lang_include pricing/rcs_billing_message_types.md %}

{% alert note %}
Consulte nossa [documentação de SMS e MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms) para saber mais sobre nossas ofertas da família SMS.
{% endalert %}

## Detalhes do canal WhatsApp {#whatsapp-channel-details}

{% multi_lang_include whatsapp/about_credits.md content="h3" %}

## Detalhamento por região de cobrança {#billing-region-breakdown}

### América do Norte {#north-america}

Estados Unidos, Canadá

### Restante da África {#rest-of-africa}

Argélia, Angola, Benin, Botsuana, Burkina Faso, Burundi, Camarões, Chade, Congo, Eritreia, Etiópia, Gabão, Gâmbia, Gana, Guiné-Bissau, Costa do Marfim, Quênia, Lesoto, Libéria, Líbia, Madagascar, Malawi, Mali, Mauritânia, Marrocos, Moçambique, Namíbia, Níger, Ruanda, Senegal, Serra Leoa, Somália, Sudão do Sul, Sudão, Essuatíni, Tanzânia, Togo, Tunísia, Uganda, Zâmbia

### Restante da Ásia-Pacífico {#rest-of-asia-pacific}

Afeganistão, Austrália, Bangladesh, Camboja, China, Japão, Laos, Mongólia, Nepal, Nova Zelândia, Papua-Nova Guiné, Filipinas, Sri Lanka, Taiwan, Tajiquistão, Tailândia, Turcomenistão, Uzbequistão, Vietnã

### Restante da Europa Central e Oriental {#rest-of-central-eastern-europe}

Albânia, Armênia, Azerbaijão, Belarus, Bulgária, Croácia, República Tcheca, Geórgia, Grécia, Letônia, Lituânia, Macedônia, Moldávia, Sérvia, Eslováquia, Eslovênia, Ucrânia

### Restante da América Latina {#rest-of-latin-america}

Bolívia, Costa Rica, República Dominicana, Equador, El Salvador, Guatemala, Haiti, Honduras, Jamaica, Nicarágua, Panamá, Paraguai, Porto Rico, Uruguai, Venezuela

### Restante do Oriente Médio {#rest-of-middle-east}

Bahrein, Iraque, Jordânia, Kuwait, Líbano, Omã, Iêmen

### Restante da Europa Ocidental {#rest-of-western-europe}

Áustria, Bélgica, Dinamarca, Finlândia, Irlanda, Noruega, Portugal, Suécia, Suíça

{% alert note %}
Consulte nossa [documentação do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp) para saber mais sobre nossas ofertas de WhatsApp.
{% endalert %}

## Detalhes do Agent Console {#agent-console-details}

As taxas de crédito do Agent Console são calculadas em incrementos de mil (1.000) invocações realizadas a partir da plataforma Braze. Uma invocação é registrada quando um agente inicia uma chamada a um LLM. Por padrão, seu contrato inclui uma quantidade de invocações conforme especificado pela sua edição da plataforma para cada período do seu prazo de inscrição. Invocações adicionais serão cobradas conforme seu formulário de pedido.

{% alert note %}
Consulte nossa [documentação de Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents) para saber mais sobre o Agent Console.
{% endalert %}

## Detalhes adicionais por canal {#additional-channel-details}

### LINE {#line}

As taxas de crédito do LINE são calculadas em incrementos de mensagens LINE enviadas a partir da plataforma Braze.

{% alert note %}
Consulte nossa [documentação do LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line) para saber mais sobre como usar o LINE com a Braze.
{% endalert %}

### KakaoTalk {#kakaotalk}

As taxas de crédito do KakaoTalk são calculadas em incrementos de mensagens KakaoTalk enviadas a partir da plataforma Braze.

{% alert note %}
Consulte nossa [documentação do KakaoTalk]({{site.baseurl}}/kakaotalk) para saber mais sobre como usar o KakaoTalk com a Braze.
{% endalert %}

### Content Cards {#content-cards}

As taxas de crédito de Content Cards são calculadas em incrementos de mil impressões únicas diárias.

A Braze reserva-se o direito de cobrar créditos por Content Cards com base no número de Content Cards enviados se o cliente não configurar os Content Cards para registrar impressões únicas de acordo com as orientações da Braze. Isso será considerado aplicável se, dentro de seis (6) meses após o primeiro envio de Content Cards, o cliente tiver:
- Enviado mais de cinco milhões (5.000.000) de Content Cards, E TAMBÉM
    - Zero (0) impressões registradas
    - Proporção de envios para impressões únicas diárias superior a cem (100)

{% alert note %}
Consulte nossa [documentação de Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards) para saber mais sobre Content Cards da Braze.
{% endalert %}

### Banners {#banners}

As taxas de crédito de Banners são calculadas em incrementos de mil impressões únicas diárias.

{% alert note %}
Consulte nossa [documentação de Banners]({{site.baseurl}}/developer_guide/banner_cards) para saber mais sobre Banners da Braze.
{% endalert %}

### Audience Sync {#audience-sync}

As taxas de crédito do Audience Sync são calculadas em incrementos de mil sincronizações totais de usuários. Por padrão, seu contrato inclui cinco milhões de sincronizações de usuários por cada período do seu prazo de assinatura. Sincronizações adicionais de usuários serão cobradas conforme seu formulário de pedido.

{% alert note %}
Consulte nossa [documentação de Canvas]({{site.baseurl}}/partners/canvas_steps) para saber mais sobre o Canvas Audience Sync e os parceiros disponíveis.
{% endalert %}

### Arquivamento de mensagens {#message-archiving}

As taxas de crédito do arquivamento de mensagens são calculadas em incrementos de mil mensagens arquivadas nos canais de push, e-mail e SMS/MMS.

{% alert note %}
Consulte nossa [documentação de arquivamento de mensagens]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving#message-archiving) para saber mais sobre o arquivamento de mensagens.
{% endalert %}

### Webhooks {#webhooks}

As taxas de crédito de webhooks são calculadas em incrementos de mil webhooks enviados com sucesso a partir da plataforma Braze. Por padrão, seu contrato inclui cem mil webhooks por cada período do seu prazo de assinatura. Webhooks adicionais serão cobrados conforme seu formulário de pedido.

{% multi_lang_include pricing/webhook_failed_requests_billing.md credit_name='Action Credits' %}

{% alert note %}
Consulte nossa [documentação de webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks) para saber mais sobre webhooks da Braze.
{% endalert %}