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

- [Descrições dos Créditos de Ação da Braze](#braze-action-credits-descriptions)
  - [Detalhes do canal de e-mail](#email-channel-details)
  - [Detalhes dos canais SMS, MMS e RCS](#sms-mms-and-rcs-channel-details)
    - [Segmentos de SMS](#sms-segments)
    - [Mensagens MMS](#mms-messages)
    - [Tipos de RCS](#rcs-types)
  - [Detalhes do canal WhatsApp](#whatsapp-channel-details)
    - [Detalhamento por região de cobrança](#billing-region-breakdown)
  - [Detalhes do Console do agente](#agent-console-details)
  - [Detalhes de canais adicionais](#additional-channel-details)
    - [LINE](#line)
    - [KakaoTalk](#kakaotalk)
    - [Content Cards](#content-cards)
    - [Banners](#banners)
    - [Audience Sync](#audience-sync)
    - [Arquivamento de mensagem](#message-archiving)
    - [Webhooks](#webhooks)

## Detalhes do canal de e-mail {#email-channel-details}

As proporções de créditos de e-mail são denominadas em incrementos de mil e-mails enviados (CPM) a partir da plataforma Braze.

{% alert note %}
Consulte nossa [documentação de e-mail]({{site.baseurl}}/user_guide/message_building_by_channel/email/) para saber mais sobre nosso canal de e-mail.
{% endalert %}

## Detalhes dos canais SMS, MMS e RCS {#sms-mms-and-rcs-channel-details}

As proporções de créditos de SMS e MMS são denominadas em incrementos de segmentos enviados a partir da plataforma Braze. As proporções de créditos de RCS são denominadas em incrementos de tipos Basic e Rich Media, ou tipos Single e Rich Media entregues a partir da plataforma Braze. Tanto os tipos de entrada quanto os de saída são cobrados.

{% alert note %}
Quando aplicável para esses canais, as taxas de operadora são cobradas separadamente (em atraso) e não são consideradas como parte dos Créditos de Ação.
{% endalert %}

### Segmentos de SMS {#sms-segments}

O setor de SMS conta as mensagens em segmentos de mensagem SMS. Um segmento de mensagem é um agrupamento de até um número definido de caracteres (160 para codificação GSM-7; 67 para codificação UCS-2) que será enviado em um único despacho de SMS. Se você enviar um SMS com 161 caracteres usando codificação GSM-7, dois (2) segmentos de mensagem serão enviados. O envio de múltiplos segmentos de mensagem resultará em cobranças adicionais.

### Mensagens MMS {#mms-messages}

Para MMS, o limite da mensagem é de 5 MB (isso inclui o ativo multimídia e o tamanho do corpo da mensagem). Para maior segurança, a Braze recomenda não exceder 600 KB para seu ativo multimídia, incluindo também um corpo de mensagem.

### Tipos de RCS {#rcs-types}

O RCS é a próxima geração de SMS e MMS. Ele oferece os benefícios de um canal direto e de alto engajamento como o SMS, com recursos mais ricos que os consumidores modernos esperam, como conteúdo rico (imagens, vídeos, documentos), envio verificado e com marca, recursos interativos como respostas e ações sugeridas, e muito mais.

- A cobrança do RCS é baseada em dois tipos diferentes de mensagem (com distinções para os EUA):
    - **RCS Basic:** Somente texto, até 160 caracteres
    - **RCS Single:** Mensagens contendo conteúdo rico, ou mensagens somente texto com mais de 160 caracteres
    - **RCS Rich (somente EUA):** Somente texto, pode incluir sugestões/botões limitados (quickReply, dialPhone, openURL sem webview), segmentado a cada 160 bytes UTF-8
    - **RCS Rich Media (somente EUA):** Qualquer mídia OU texto com sugestões/botões mais ricos (webview, localização, calendário, etc.), contado como uma mensagem

{% alert note %}
Consulte nossa [documentação de SMS e MMS]({{site.baseurl}}/user_guide/message_building_by_channel/sms/) para saber mais sobre nossas ofertas da família SMS.
{% endalert %}

## Detalhes do canal WhatsApp {#whatsapp-channel-details}

{% multi_lang_include whatsapp/about_credits.md content="h3" %}

### Detalhamento por região de cobrança {#billing-region-breakdown}

#### América do Norte {#north-america}

Estados Unidos, Canadá

#### Restante da África {#rest-of-africa}

Argélia, Angola, Benin, Botsuana, Burkina Faso, Burundi, Camarões, Chade, Congo, Eritreia, Etiópia, Gabão, Gâmbia, Gana, Guiné-Bissau, Costa do Marfim, Quênia, Lesoto, Libéria, Líbia, Madagascar, Malauí, Mali, Mauritânia, Marrocos, Moçambique, Namíbia, Níger, Ruanda, Senegal, Serra Leoa, Somália, Sudão do Sul, Sudão, Suazilândia, Tanzânia, Togo, Tunísia, Uganda, Zâmbia

#### Restante da Ásia-Pacífico {#rest-of-asia-pacific}

Afeganistão, Austrália, Bangladesh, Camboja, China, Hong Kong, Japão, Laos, Mongólia, Nepal, Nova Zelândia, Papua-Nova Guiné, Filipinas, Singapura, Sri Lanka, Taiwan, Tajiquistão, Tailândia, Turcomenistão, Uzbequistão, Vietnã

#### Restante da Europa Central e Oriental {#rest-of-central-eastern-europe}

Albânia, Armênia, Azerbaijão, Belarus, Bulgária, Croácia, República Tcheca, Geórgia, Grécia, Hungria, Letônia, Lituânia, Macedônia, Moldávia, Polônia, Romênia, Sérvia, Eslováquia, Eslovênia, Ucrânia

#### Restante da América Latina {#rest-of-latin-america}

Bolívia, Costa Rica, República Dominicana, Equador, El Salvador, Guatemala, Haiti, Honduras, Jamaica, Nicarágua, Panamá, Paraguai, Porto Rico, Uruguai, Venezuela

#### Restante do Oriente Médio {#rest-of-middle-east}

Bahrein, Iraque, Jordânia, Kuwait, Líbano, Omã, Catar, Iêmen

#### Restante da Europa Ocidental {#rest-of-western-europe}

Áustria, Bélgica, Dinamarca, Finlândia, Irlanda, Noruega, Portugal, Suécia, Suíça

{% alert note %}
Consulte nossa [documentação do WhatsApp]({{site.baseurl}}/user_guide/message_building_by_channel/whatsapp/) para saber mais sobre nossas ofertas de WhatsApp.
{% endalert %}

## Detalhes do Console do agente {#agent-console-details}

As proporções de créditos do Console do agente são denominadas em incrementos de mil (1.000) invocações realizadas a partir da plataforma Braze. Uma invocação é registrada quando um agente inicia uma chamada a um LLM. Por padrão, seu contrato inclui uma alocação de invocações conforme especificado pela sua Edição da Plataforma para cada Período do seu Prazo de Assinatura. Invocações adicionais serão cobradas conforme seu Formulário de Pedido.

{% alert note %}
Consulte nossa [documentação de Braze Agents]({{site.baseurl}}/user_guide/brazeai/agents/) para saber mais sobre o Console do agente.
{% endalert %}

## Detalhes de canais adicionais {#additional-channel-details}

### LINE {#line}

As proporções de créditos do LINE são denominadas em incrementos de mensagens LINE enviadas a partir da plataforma Braze.

{% alert note %}
Consulte nossa [documentação do LINE]({{site.baseurl}}/user_guide/message_building_by_channel/line/) para saber mais sobre como usar o LINE com a Braze.
{% endalert %}

### KakaoTalk {#kakaotalk}

As proporções de créditos do KakaoTalk são denominadas em incrementos de mensagens KakaoTalk enviadas a partir da plataforma Braze.

{% alert note %}
Consulte nossa [documentação do KakaoTalk]({{site.baseurl}}/kakaotalk/) para saber mais sobre como usar o KakaoTalk com a Braze.
{% endalert %}

### Content Cards {#content-cards}

As proporções de créditos de Content Cards são denominadas em incrementos de mil impressões únicas diárias.

A Braze reserva-se o direito de cobrar créditos por Content Cards com base no número de Content Cards enviados se o Cliente não configurar os Content Cards para registrar impressões únicas de acordo com as orientações da Braze. Isso será considerado aplicável se, dentro de seis (6) meses do primeiro envio de Content Cards, o Cliente tiver:
- Enviado mais de cinco milhões (5.000.000) de Content Cards, E TAMBÉM
    - Zero (0) impressões registradas
    - Proporção de envios para impressões únicas diárias maior que cem (100)

{% alert note %}
Consulte nossa [documentação de Content Cards]({{site.baseurl}}/user_guide/message_building_by_channel/content_cards/) para saber mais sobre Content Cards da Braze.
{% endalert %}

### Banners {#banners}

As proporções de créditos de Banners são denominadas em incrementos de mil impressões únicas diárias.

{% alert note %}
Consulte nossa [documentação de Banners]({{site.baseurl}}/developer_guide/banner_cards/) para saber mais sobre Banners da Braze.
{% endalert %}

### Audience Sync {#audience-sync}

As proporções de créditos de Audience Sync são denominadas em incrementos de mil sincronizações totais de usuários. Por padrão, seu contrato inclui cinco milhões de sincronizações de usuários para cada Período do seu Prazo de Assinatura. Sincronizações adicionais de usuários serão cobradas conforme seu Formulário de Pedido.

{% alert note %}
Consulte nossa [documentação de Canvas]({{site.baseurl}}/partners/canvas_steps/) para saber mais sobre Canvas Audience Sync e parceiros disponíveis.
{% endalert %}

### Arquivamento de mensagem {#message-archiving}

As proporções de créditos de Arquivamento de mensagem são denominadas em incrementos de mil mensagens arquivadas nos canais push, e-mail e SMS/MMS.

{% alert note %}
Consulte nossa [documentação de arquivamento de mensagem]({{site.baseurl}}/user_guide/data/export_braze_data/message_archiving/#message-archiving) para saber mais sobre Arquivamento de mensagem.
{% endalert %}

### Webhooks {#webhooks}

As proporções de créditos de Webhooks são denominadas em incrementos de mil webhooks enviados a partir da plataforma Braze. Por padrão, seu contrato inclui cem mil webhooks para cada Período do seu Prazo de Assinatura. Webhooks adicionais serão cobrados conforme seu Formulário de Pedido.

{% alert note %}
Consulte nossa [documentação de webhooks]({{site.baseurl}}/user_guide/message_building_by_channel/webhooks/) para saber mais sobre Webhooks da Braze.
{% endalert %}