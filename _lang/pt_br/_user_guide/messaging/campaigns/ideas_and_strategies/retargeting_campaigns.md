---
nav_title: Redirecionamento de campanhas
article_title: Redirecionar campanhas
page_order: 2
page_type: reference
description: "Este artigo de referência explica como e por que você deve considerar o redirecionamento de campanhas com base nas mensagens que seus usuários recebem."
tool:
  - Campaigns

---

# Redirecionar campanhas {#retarget-campaigns}

> Ao redirecionar campanhas com base nas ações anteriores do usuário, como se ele abriu ou não um e-mail, você pode ajudar a reclassificar seus usuários, abrindo caminho para uma abordagem eficaz de marketing baseado em dados.

A Braze oferece suporte para redirecionar usuários com base nas mensagens que eles receberam. Você pode redirecionar usuários com base nas interações deles com suas Campaigns e Canvas.

Cada um desses filtros de redirecionamento oferece várias opções após ser adicionado. Para saber mais sobre o direcionamento de usuários, confira nosso [curso do Braze Learning](https://learning.braze.com/campaign-setup-delivery-targeting-conversions) sobre configuração de campanhas!

![Seção de informações do Segment com o menu suspenso dos filtros disponíveis.]({% image_buster /assets/img_archive/retarget.png %}){: style="max-width:80%;"}

## Filtros de redirecionamento {#retargeting-filters}

Você pode usar os filtros de redirecionamento desta seção para seus usuários dentro de suas Campaigns e Canvas.

### Clicou/Abriu Campaign {#clickedopened-campaign}

Use este filtro para encontrar usuários que fizeram ou não as seguintes ações:

- Clicaram em um e-mail
- Clicaram em uma mensagem no app
- Abriram diretamente uma notificação por push
- Abriram um e-mail
- Visualizaram uma mensagem no app

![Filtro Clicou/Abriu Campaign com opções de interação por canal.]({% image_buster /assets/img_archive/clickedopened.png %})

Isso pode ser especificado ainda mais selecionando qual Campaign você deseja redirecionar.

### Clicou ou abriu Campaign ou Canvas com tag {#clicked-or-opened-campaign-or-canvas-with-tag}

Use este filtro para encontrar usuários que interagiram ou não com Campaigns ou Canvas com uma determinada tag:

- Clicaram em um e-mail
- Clicaram em uma mensagem no app
- Abriram diretamente uma notificação por push
- Abriram um e-mail
- Visualizaram uma mensagem no app

![Filtro Clicou ou abriu Campaign ou Canvas com tag.]({% image_buster /assets/img_archive/retarget_tag_filter.png %})

### Converteu a partir da Campaign {#converted-from-campaign}

Use este filtro para encontrar usuários que converteram ou não (com base na conversão primária) na sua Campaign alvo.

Para Campaigns recorrentes, este filtro se refere a se os usuários converteram na mensagem mais recente da Campaign.

![Filtro Converteu a partir da Campaign com seleção de Campaign.]({% image_buster /assets/img_archive/converted_from_campaign.png %})

### Converteu a partir do Canvas {#converted-from-canvas}

Use este filtro para encontrar usuários que converteram ou não (com base na conversão primária) no seu Canvas alvo.

Para Canvas recorrentes, este filtro se refere a se os usuários converteram em algum momento ao longo de suas passagens pelo Canvas.

![Filtro Converteu a partir do Canvas com seleção de Canvas.]({% image_buster /assets/img_archive/converted_from_canvas.png %})

### No grupo de controle da Campaign {#in-campaign-control-group}

Use este filtro para encontrar usuários que estão ou não no grupo de controle da sua Campaign alvo.

![Filtro No grupo de controle da Campaign com seleção de Campaign.]({% image_buster /assets/img_archive/campaign_control_group.png %})

### No grupo de controle do Canvas {#in-canvas-control-group}

Use este filtro para encontrar usuários que estão ou não no grupo de controle do seu Canvas alvo, que pode ser selecionado no menu suspenso.

![Filtro No grupo de controle do Canvas com seleção de Canvas.]({% image_buster /assets/img_archive/canvas_control_group.png %})

### Última mensagem recebida de uma Campaign específica {#last-received-message-from-specific-campaign}

Use este filtro para encontrar usuários que receberam pela última vez uma Campaign específica antes ou depois de uma data ou número de dias especificado. Este filtro não considera quando os usuários receberam outras Campaigns.

{% multi_lang_include audience/segments.md section='same channel identifier' %}

![Filtro Última mensagem recebida de uma Campaign específica com opções de data.]({% image_buster /assets/img_archive/last_received_specific_campaign.png %})

### Última mensagem recebida de Campaign ou Canvas com tag {#last-received-message-from-campaign-or-canvas-with-tag}

Use este filtro para encontrar usuários que receberam pela última vez uma Campaign ou Canvas com uma determinada tag antes ou depois de uma data ou número de dias especificado. Este filtro não considera quando os usuários receberam outras Campaigns ou Canvas.

![Filtro Última mensagem recebida de Campaign ou Canvas com tag.]({% image_buster /assets/img_archive/last_received_campaign_with_tag.png %})

### Recebeu mensagem da Campaign {#received-message-from-campaign}

Use este filtro para encontrar usuários que receberam ou não a sua Campaign alvo.

{% multi_lang_include audience/segments.md section='same channel identifier' %}

![Filtro Recebeu mensagem da Campaign com seleção de Campaign.]({% image_buster /assets/img_archive/receivedcamp.png %})

### Recebeu mensagem de Campaign ou Canvas com tag {#received-message-from-campaign-or-canvas-with-tag}

Use este filtro para encontrar usuários que receberam ou não uma Campaign ou Canvas que possui a sua tag alvo.

![Filtro Recebeu mensagem de Campaign ou Canvas com tag.]({% image_buster /assets/img_archive/received_campaign_with_tag.png %})

## Vantagens do redirecionamento de campanhas {#advantages-with-retargeting-campaigns}

O redirecionamento é particularmente eficaz quando o Segment original também incluiu uma ação específica que você deseja que os usuários realizem. Por exemplo, digamos que você tenha um cartão direcionado a usuários que nunca fizeram uma compra. O cartão anuncia uma promoção de compra no app com desconto. O Segment inicial é o seguinte:

- Dinheiro gasto no app é exatamente 0
- Último uso do app há menos de 14 dias

O número total de usuários no Segment é 100.000 e você sabe pelas estatísticas do cartão de conteúdo que 60.000 usuários únicos visualizaram o cartão e 20.000 usuários únicos clicaram no cartão. Através do segmentador, podemos ver quantos desses usuários que clicaram no cartão realmente fizeram uma compra:

- Dinheiro gasto no app é maior que 0
- Clicou no cartão é Nome do Cartão

Após examinar essas estatísticas, podemos criar um Segment de usuários que clicaram no cartão, mas não fizeram uma compra:

- Dinheiro gasto no app é exatamente 0
- Clicou no cartão é Nome do Cartão

Podemos redirecionar esse Segment com mensagens adicionais sobre a promoção ou outra compra no app. O redirecionamento pode ser feito com uma campanha de mensagens. Uma abordagem multicanal permite que você alcance os usuários onde eles têm mais probabilidade de responder, aumentando assim a eficácia das suas campanhas.