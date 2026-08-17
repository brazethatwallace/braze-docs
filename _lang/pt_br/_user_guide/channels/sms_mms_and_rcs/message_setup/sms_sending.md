---
nav_title: Envio de SMS
article_title: Envio de SMS
page_order: 4
alias: /sms_message_sending/
description: "Este artigo de referência aborda os fundamentos e as melhores práticas do envio de SMS."
page_type: reference
channel:
  - SMS


---

# Envio de mensagens SMS {#sms-message-sending}

> O envio de mensagens pode ser complicado, mas não precisa ser. As seções a seguir apresentam os fundamentos do envio de mensagens SMS na Braze, incluindo a importância dos grupos de inscrições, os requisitos para segmentos de mensagem e corpos de mensagem, além das opções avançadas de personalização disponíveis.

## Conceitos básicos de envio de SMS {#sms-sending-basics}

### Selecione seu grupo de inscrições {#select-your-subscription-group}

As mensagens SMS devem ser enviadas a partir de um [grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups). Um grupo de inscrições é uma coleção de números de telefone de envio (como códigos curtos, códigos longos e/ou IDs de remetente alfanuméricos) usados para um tipo específico de finalidade de envio de mensagens. Você deve designar um grupo de inscrições para garantir que apenas usuários inscritos sejam direcionados. Alguns clientes podem ter vários grupos de inscrições para diferentes casos de uso, como envio de mensagens SMS transacionais e envio de mensagens SMS promocionais.<br><br>

### Insira o corpo da mensagem {#input-message-body}

O corpo de uma mensagem SMS aceita até 1.600 caracteres, incluindo emojis, Liquid e Connected Content. Um único envio de Campaign pode resultar no envio de vários segmentos de mensagem. Os corpos de mensagens SMS da Braze podem ser compostos usando os padrões de codificação [GSM-7](https://en.wikipedia.org/wiki/GSM_03.38) ou [UCS-2](https://en.wikipedia.org/wiki/Universal_Coded_Character_Set). Caso um caractere UCS-2 (por exemplo, um emoji) seja usado, o corpo da mensagem será formatado automaticamente para esse padrão de codificação.<br><br>

### Entenda os segmentos de mensagem e os limites de caracteres {#understand-message-segments-and-character-limits}

Os segmentos de mensagem SMS são a forma como o setor de SMS contabiliza as mensagens. Um segmento de mensagem é um agrupamento de até um número definido de caracteres (160 para codificação GSM-7; 67 para codificação UCS-2) enviado em um único despacho de SMS. Se sua mensagem usar caracteres da tabela de extensão GSM-7 (como `{`, `}` ou `~`), cada segmento poderá conter menos caracteres. Se você enviar um SMS com 161 caracteres usando codificação GSM-7, dois segmentos de mensagem serão enviados. O envio de vários segmentos de mensagem pode resultar em cobranças adicionais.<br><br>

### Personalização de palavras-chave (opcional) {#keyword-customization-optional}

As regulamentações exigem que haja respostas para todas as respostas de palavras-chave de SMS de aceitação, cancelamento e ajuda/informações. Com a Braze, você pode definir suas próprias palavras-chave para disparar respostas de aceitação, cancelamento e ajuda, gerenciar suas próprias respostas enviadas aos usuários e definir conjuntos de palavras-chave para diferentes idiomas. Para saber mais, consulte nossa coleção sobre [Processamento de palavras-chave]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing).

{% alert tip %}
Quer aprender a criar uma campanha de SMS? Confira nosso guia passo a passo sobre [Criação de uma mensagem SMS, MMS ou RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create).
{% endalert %}

Para práticas recomendadas de envio, incluindo orientações sobre envio para vários países e em alto volume, consulte [Práticas recomendadas para SMS, MMS e RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/best_practices).