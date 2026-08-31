---
nav_title: Envio de SMS
article_title: Envio de SMS
page_order: 4
alias: /sms_message_sending/
description: "Revise grupos de inscrições, cobrança de mensagens e fundamentos de palavras-chave para o envio de mensagens SMS."
page_type: reference
channel:
  - SMS

---

# Envio de mensagens SMS {#sms-message-sending}

> Revise os fundamentos de inscrição, cobrança e palavras-chave que se aplicam ao envio de mensagens SMS com a Braze.

## Fundamentos de envio de SMS {#sms-sending-basics}

### Selecione seu grupo de inscrições {#select-your-subscription-group}

Envie mensagens SMS a partir de um [grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups). Um grupo de inscrições contém números de telefone de envio, como short codes, long codes e IDs alfanuméricos de remetente, para uma finalidade específica de envio de mensagens. Use grupos de inscrições separados para casos de uso como envio de mensagens transacionais e promocionais.

### Componha a mensagem {#compose-the-message}

Para campos de mensagem, limites de caracteres, personalização, mídia e encurtamento de links, consulte [Criar uma mensagem SMS, MMS ou RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/create#sms-and-mms-fields-and-settings).

### Entenda os segmentos de mensagem e os limites de caracteres {#understand-message-segments-and-character-limits}

As mensagens SMS usam codificação GSM-7 ou UCS-2 e são cobradas por segmento de mensagem. Para regras de codificação, tamanhos de segmento e a calculadora de segmentos, consulte [Calculadoras de cobrança de SMS e RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/billing_calculator).

### Personalização de palavras-chave (opcional) {#keyword-customization-optional}

As regulamentações exigem respostas para palavras-chave de aceitação, cancelamento e Ajuda ou Informações. Defina palavras-chave, respostas e conjuntos de palavras-chave específicos por idioma por meio do [Processamento de palavras-chave]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing).

Para práticas recomendadas de envio, incluindo orientações sobre envio para múltiplos países e em alto volume, consulte [Práticas recomendadas para SMS, MMS e RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/best_practices).