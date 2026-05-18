---
nav_title: Classificação de qualidade e limites de envio de mensagens
article_title: Classificação de qualidade e limites de envio de mensagens
description: "Este artigo de referência aborda como a Meta influencia sua classificação de qualidade e os limites de envio de mensagens para o canal WhatsApp."
page_type: partner
search_tag: Partner
page_order: 1
channel:
  - WhatsApp
---

# Classificação de qualidade e limites de envio de mensagens {#quality-rating-and-messaging-limits}

> A Meta influencia sua classificação de qualidade e os [limites de envio de mensagens](https://developers.facebook.com/docs/whatsapp/messaging-limits) desde o momento em que você começa a usar o canal WhatsApp, e continuará influenciando-os em resposta ao seu uso do WhatsApp.

## Definições {#definitions}

| Termo | Definição |
| --- | --- |
| Classificação de qualidade | Uma classificação baseada nas mensagens recentes que seus clientes receberam nos últimos sete dias. Essa classificação é determinada pelo feedback dos seus clientes, como o motivo para bloquear seu número de telefone e outros problemas reportados. Consulte a documentação da Meta para saber mais [sobre sua classificação de qualidade](https://www.facebook.com/business/help/896873687365001).|
| Limite de envio de mensagens | O número máximo de conversas iniciadas pela empresa que você pode começar com cada um dos seus números de telefone em um período contínuo de 24 horas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Definitions" }

## Integração {#onboarding}

Quando uma nova conta WhatsApp Business é criada, a Meta usa uma variedade de fatores para determinar o limite inicial de envio. Você pode encontrar esse limite no seu WhatsApp Business Manager, e informações adicionais na sua página de Insights do Número de Telefone.

Consulte a documentação da Meta para saber mais sobre [como verificar seu limite](https://developers.facebook.com/docs/whatsapp/messaging-limits#checking-your-limit) e [requisitos de número de telefone](https://developers.facebook.com/docs/whatsapp/cloud-api/phone-numbers).

## Taxa de transferência {#throughput}

A Meta inicia cada número de telefone comercial registrado com uma taxa de transferência de 80 mensagens por segundo. O upgrade para 1.000 mensagens por segundo pode acontecer automaticamente ou mediante solicitação.

Consulte a documentação da Meta para saber mais sobre sua [taxa de transferência](https://developers.facebook.com/docs/whatsapp/cloud-api/overview#throughput).

## Ritmo de modelos {#template-pacing}

Modelos de marketing criados recentemente e modelos de marketing pausados que são reativados estão potencialmente sujeitos a controle de ritmo. Os critérios de seleção de ritmo da Meta são principalmente baseados no histórico de qualidade dos seus modelos. Quando você usa um modelo de marketing criado recentemente ou um modelo de marketing reativado recentemente, as mensagens serão enviadas normalmente até que um limite não especificado seja atingido. Depois que esse limite for atingido, as mensagens subsequentes usando esse modelo serão retidas para permitir tempo suficiente para o feedback dos clientes.

Consulte a documentação da Meta para saber mais sobre o [ritmo de modelos](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/#template-pacing).