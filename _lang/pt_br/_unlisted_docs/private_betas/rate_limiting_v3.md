---
article_title: Limite de taxa para Campaigns push e Canvas multicanal
permalink: /rate_limiting_v3/
page_type: reference
description: "Este artigo descreve os limites de taxa de velocidade de entrega para Campaigns push e Canvas multicanal."
---

# Limite de taxa para Campaigns push e Canvas multicanal {#rate-limiting-for-push-campaigns-and-multichannel-canvases}

> Esta página aborda o limite de taxa para Campaigns push e Canvas multicanal, incluindo considerações a ter em mente ao regular suas mensagens.

Ao definir os limites de taxa de velocidade de entrega para Campaigns push e Canvas multicanal, agora você pode escolher entre definir:

- Limites de taxa por canal
- Um limite de taxa geral compartilhado entre todos os canais de mensagem.

{% alert important %}
O limite de taxa para Campaigns push e Canvas multicanal está em acesso antecipado. Entre em contato com o gerente da sua conta da Braze se tiver interesse em participar deste acesso antecipado.
{% endalert %}

As seguintes funcionalidades **não estão** incluídas neste acesso antecipado:

- Definir limites de taxa por canal em Campaigns multicanal de qualquer tipo e Canvas disparados por API
- Definir um limite de taxa global
- Definir limites de taxa por etapa de Mensagem no Canvas

## Considerações {#considerations}

- Esta atualização de limite de taxa não impede que você defina um limite de taxa muito baixo. Isso significa que, sem essa prevenção, você poderia definir um limite de taxa e, dependendo do tamanho do público, suas mensagens poderiam ser enviadas a uma taxa extremamente lenta.
- Os resumos de **Configurações de envio** para Campaigns e Canvas podem conter descrições imprecisas para os limites de taxa que foram definidos: <br><br>![Configurações de envio para Campaigns onde não há limitações na taxa em que os usuários receberão mensagens.]({% image_buster /assets/unlisted_docs/img/send_settings_example.png %}){: style="max-width:65%"}<br><br>
- O limite de taxa para Campaigns multicanal (não Canvas ou Campaigns push) refletirá o [comportamento de limite de taxa de Campaigns multicanal não atualizado](https://www.braze.com/docs/user_guide/engagement_tools/campaigns/building_campaigns/rate-limiting/#delivery-speed-rate-limiting). Recomendamos evitar a criação de Campaigns multicanal com limite de taxa enquanto fizer parte desta fase de acesso antecipado.