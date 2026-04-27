---
nav_title: Setembro
page_order: 4
noindex: true
page_type: update
description: "Este artigo contém notas de versão de setembro de 2020."
---

# Setembro {#september}

## Relatórios de funil {#funnel-reporting}

O Funnel Reporting oferece um relatório visual que permite analisar as jornadas que seus clientes percorrem após receberem uma [Campaign]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/) ou um [Canvas]({{site.baseurl}}/user_guide/analytics/reports/funnel_reports/).

## Guia para fazer upgrade do iOS 14 {#ios-14-upgrade-guide}

De acordo com as alterações anunciadas no novo iOS 14 da Apple, há algumas alterações relacionadas à Braze e itens de ação necessários para as integrações do SDK da Braze para iOS. Para saber mais, dê uma olhada neste [guia de upgrade]({{site.baseurl}}/ios_14/).

## Alterações no IDFA e no IDFV para iOS 14 {#changes-to-idfa-and-idfv-for-ios-14}

No iOS 14, os usuários devem decidir se querem aceitar o rastreamento de anúncios e permitir que apps e redes de anúncios leiam seu IDFA ao visitar um app. Como resultado, a estratégia da Braze é usar o "identificador para fornecedores" (como o IDFV) para que você possa continuar a rastrear usuários em diferentes dispositivos. Para saber mais, dê uma olhada no [guia de upgrade do iOS 14]({{site.baseurl}}/ios_14/).

## Validação de e-mail {#email-validation}

Esse novo processo de validação da sintaxe de e-mail é um upgrade do processo existente da Braze. Essa é uma verificação para confirmar se os e-mails atualizados ou importados para a Braze estão corretos. Para saber mais, dê uma olhada [nestas diretrizes e notas]({{site.baseurl}}/user_guide/channels/email/email_setup/email_validation/).

## Evento de usuário de bucket aleatório no Currents {#random-bucket-user-event-in-currents}

O número de bucket aleatório (como RBN) ocorre sempre que um novo usuário é criado em seu espaço de trabalho. Durante esse evento, é atribuído a cada novo usuário um número de bucket aleatório que pode ser usado para criar segmentos uniformemente distribuídos de usuários aleatórios. Use isso para agrupar uma faixa de valores de números de bucket aleatórios e comparar o desempenho entre suas Campaigns e variantes de campanha. Para ver se esse evento está disponível para você, dê uma olhada no [glossário de eventos de comportamento do cliente]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/customer_behavior_events/) do Currents.

## Componentes do Canvas - Em breve! {#canvas-components-coming-soon}

A Braze adicionou quatro novos componentes do Canvas para ajudar a aumentar a flexibilidade e a funcionalidade dos seus Canvas. Esses novos componentes incluem: [Etapa de divisão de decisão]({{site.baseurl}}/decision_split/), [Etapa de postergação]({{site.baseurl}}/delay_step/), [Etapas de envio de mensagens]({{site.baseurl}}/message_step/) e [Audience Sync to Facebook]({{site.baseurl}}/audience_sync_facebook/).
- **Etapas de divisão de decisão, postergação e envio de mensagens do Canvas**<br>As divisões de decisão podem ser usadas para criar ramificações do Canvas dependendo de um usuário corresponder ou não a uma consulta definida. As etapas de postergação permitem adicionar uma postergação independente ao seu Canvas sem a necessidade de uma mensagem correspondente. As etapas de envio de mensagens permitem que você adicione uma mensagem independente onde quiser no fluxo do Canvas.
- **Audience Sync to Facebook**<br>Usando o Audience Sync to Facebook da Braze, as marcas podem optar por adicionar os dados de seus próprios usuários da sua integração com a Braze aos públicos personalizados do Facebook para veicular anúncios com base em gatilhos comportamentais, segmentação e muito mais. Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS, webhook etc.) em um Canvas da Braze com base nos dados do seu usuário agora pode ser usado para disparar um anúncio para esse usuário no Facebook por meio de públicos personalizados.

## Eventos de entrada de SMS recebidos {#sms-inbound-received-events}

Um novo evento de engajamento com mensagens foi adicionado ao Currents. Esse evento ocorre quando um dos seus usuários envia um SMS para um número de telefone em um dos seus grupos de inscrições de SMS da Braze. Para saber mais, consulte nosso [glossário de eventos de engajamento e envio de mensagens]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events/) do Currents.