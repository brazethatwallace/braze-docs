---
nav_title: Maio
page_order: 8
noindex: true
page_type: update
description: "Este artigo contém notas de versão de maio de 2019."
---

# Maio de 2019 {#may-2019}

## Content Cards

Content Cards são conteúdos persistentes que aparecem nas experiências de app e web dos clientes.

Com Content Cards, você pode enviar um fluxo altamente segmentado e dinâmico de conteúdo rico para seus clientes diretamente nos apps que eles adoram, sem interromper a experiência. Ou você pode combinar Content Cards com outros canais, como e-mail ou notificações por push, para viabilizar estratégias de marketing coesas.

![Feed de Content Cards]({% image_buster /assets/img/cc-feed.png %}){: height="50%" width="50%"}

Além disso, Content Cards oferecem suporte a recursos mais personalizados, incluindo fixação de cartão, descarte de cartão, entrega baseada em API or interface de programação do aplicativo (API), tempos de expiração de cartão personalizados e análise de dados de cartão.

Use esse recurso para criar centrais de notificações, feeds de página inicial e feeds de promoção.

Você precisará atualizar para uma versão compatível do SDK or kit de desenvolvimento de software da Braze:
- iOS: 3.8.0 ou posterior
- Android: 2.6.0 ou posterior
- Web: 2.2.0 ou posterior

[Saiba mais sobre Content Cards aqui!]({{site.baseurl}}/user_guide/channels/content_cards)

{% alert update %}
Content Cards para Currents e nossa documentação de API or interface de programação do aplicativo (API) para Content Cards serão lançados no final desta semana. Fique de olho!
{% endalert %}

## Adição da plataforma Roku {#roku-platform-addition}

A Braze adicionou um novo canal às nossas capacidades! Ao expandir para novos canais, podemos permitir que nossos clientes enriqueçam seus dados ao entender o comportamento de visualização ou ofereçam experiências significativas aos seus consumidores em todos os canais relevantes.

Agora você pode [recuperar dados de dispositivos Roku]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=roku) para enriquecimento de dados e rastreamento de eventos personalizados.

## Preferências de notificação para atualizações de Canvas ou Campaign {#notification-preferences-for-canvas-or-campaign-updates}

Esta [nova notificação]({{site.baseurl}}/user_guide/administrative/company_settings/notification_preferences#notification-preferences) alertará você por e-mail quando uma Campaign ou Canvas for ativada, atualizada, reativada ou desativada. Ative isso em **Preferências de notificação** na sua conta Braze.

## Documentação da parceira de tecnologia Jampp {#jampp-technology-partner-documentation}

A Jampp é uma plataforma de marketing de performance para aquisição e redirecionamento de clientes móveis. Ela combina dados comportamentais com tecnologia preditiva e programática para gerar receita para os anunciantes, exibindo anúncios pessoais e relevantes que inspiram os consumidores a comprar pela primeira vez ou com mais frequência.

Os clientes da Braze podem [integrar-se com a Jampp]({{site.baseurl}}/partners/jampp) configurando o canal de webhook da Braze para transmitir eventos para a Jampp. Como resultado, os clientes conseguem adicionar conjuntos de dados mais ricos às suas iniciativas de redirecionamento com a Jampp dentro do ecossistema de publicidade móvel.

## Seletor de plataforma para mensagens no app {#platform-picker-for-in-app-messages}

Facilitamos a seleção de para onde suas mensagens no app estão indo e para quais plataformas elas são criadas com nosso seletor de plataforma, que destaca essa etapa no processo de criação da Campaign.

![Seletor de plataforma]({% image_buster /assets/img/iam_platforms.gif %})

## Campo dispatch ID do Currents para e-mail {#dispatch-id-currents-field-for-email}

{% alert update %}
O comportamento do `dispatch_id` difere entre Canvas e Campaigns porque a Braze trata as etapas do Canvas (exceto as etapas de entrada, que podem ser agendadas) como eventos disparados, mesmo quando estão "agendadas". Saiba mais sobre o [comportamento do `dispatch_id`]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id) em Canvas e Campaigns.

_Atualização registrada em agosto de 2019._
{% endalert %}

No esforço de continuar aprimorando nossas capacidades do Currents, estamos adicionando `dispatch_id` como um campo para eventos de e-mail do Currents em todos os tipos de conector.

O `dispatch_id` é o ID único gerado para cada transmissão, ou despacho, enviado pela plataforma Braze.

Embora todos os clientes que recebem uma mensagem agendada recebam o mesmo `dispatch_id`, os clientes que recebem mensagens baseadas em ações ou disparadas por API or interface de programação do aplicativo (API) receberão um `dispatch_id` único por mensagem. O campo `dispatch_id` permite que você identifique qual instância de uma Campaign recorrente é responsável pela conversão, fornecendo assim mais insights e informações sobre quais tipos de Campaigns estão ajudando a impulsionar suas metas comerciais.

## Recurso de classificação "Mostrar só os meus" para Campaigns {#only-show-mine-campaign-sorting-feature}

Quando um usuário marca a caixa de seleção `Only Show Mine` na grade de Campaigns, os resultados serão filtrados para mostrar apenas as Campaigns criadas pelo usuário conectado. Além disso, o usuário pode usar a barra de pesquisa inserindo `created_by_me:true`.

A barra lateral da grade de Campaigns agora também é redimensionável!

## Excluir usuários por alias {#delete-users-by-alias}

Agora você pode usar o endpoint `users/delete` para [excluir usuários por alias]({{site.baseurl}}/api/endpoints/user_data/post_user_delete)!

## Cálculo único para cliques e aberturas de e-mail {#unique-calculation-for-email-clicks-and-opens}

Cliques únicos e aberturas únicas para e-mail agora são capturados e exibidos em um período de 7 dias por usuário, incrementando uma contagem de 1 dentro dessa janela de 7 dias para cada `dispatch_id`.

Usar `dispatch_id` permite que mensagens recorrentes reflitam a verdadeira contagem de abertura única ou clique único de cada mensagem. Será fácil para os clientes conciliar esses dados, agora que o `dispatch_id` está disponível no Currents.

Qualquer usuário que também use o Mailjet verá um aumento nesses números, já que o período de unicidade anterior era superior a 30 dias. Você deveria ter sido informado sobre essa mudança três (3) semanas atrás. Os clientes do SendGrid não devem notar nenhuma diferença.

Você pode pesquisar esses termos atualizados em nosso [glossário de métricas de relatórios]({{site.baseurl}}/user_guide/analytics/metrics_glossary).

{% alert update %}
O comportamento do `dispatch_id` difere entre Canvas e Campaigns porque a Braze trata as etapas do Canvas (exceto as etapas de entrada, que podem ser agendadas) como eventos disparados, mesmo quando estão "agendadas". [Saiba mais sobre o comportamento do `dispatch_id`]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/dispatch_id) em Canvas e Campaigns.

_Atualização registrada em agosto de 2019._
{% endalert %}

## Canal mais engajado {#most-engaged-channel}

{% alert update %}
A partir do [lançamento do produto de novembro de 2019]({{site.baseurl}}/help/release_notes/2019/november#intelligence-suite), "Canal mais engajado" foi renomeado para ["Canal inteligente"]({{site.baseurl}}/user_guide/brazeai/intelligence_suite/intelligent_channel).
{% endalert %}

O filtro de canal mais engajado seleciona a parte do seu público para quem o canal de envio de mensagens selecionado é o "melhor" canal. Nesse caso, "melhor" significa "tem a maior probabilidade de engajamento, dado o histórico do usuário". Você pode selecionar e-mail, web push ou push móvel (que inclui qualquer sistema operacional móvel ou dispositivo disponível) como canal.

Confira esse novo filtro em nossa [biblioteca de filtros de segmentação]({{site.baseurl }}/user_guide/engagement_tools/segments/segmentation_filters/).