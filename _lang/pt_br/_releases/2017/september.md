---
nav_title: Setembro
page_order: 4
noindex: true
page_type: update
description: "Este artigo contém notas de versão de setembro de 2017."
---

# Setembro de 2017 {#september-2017}

## Nova funcionalidade para relatórios de engajamento {#new-functionality-for-engagement-reports}

Agora você pode usar [os relatórios de engajamento]({{site.baseurl}}/user_guide/data_and_analytics/reporting/engagement_reports#engagement-reports) para agregar métricas de uma Campaign em períodos específicos. Por exemplo, você pode exportar o número total de aberturas de um trimestre ou o número total de cliques de toda a vida útil de uma Campaign ou de um Canvas. Tudo o que você precisa fazer é:
- Selecionar um período a partir do qual os dados serão exportados,
- Agendar um relatório de engajamento que será enviado a um ou mais destinatários regularmente, e
- Adicionar Campaigns e Canvas ao seu relatório com base em suas tags.

## Atualizações na página de perfil do usuário {#updates-to-user-profile-page}

A [página de perfil do usuário]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles#access-profiles) foi atualizada.

## Notificações por push da web que exigem ação do usuário para serem descartadas {#web-push-notifications-that-require-user-action-to-dismiss}

Agora você pode configurar o comportamento de fechamento de mensagens para os web pushes do Chrome que exigem que o destinatário interaja com a mensagem para que ela seja descartada. Esse recurso requer o Web SDK or kit de desenvolvimento de software versão 1.6.13 ou superior.

## Pré-cabeçalhos de e-mail {#email-preheaders}

Ao criar uma mensagem de e-mail na Braze, agora é possível inserir facilmente um pré-cabeçalho na seção **Sending Info**.

## Novo endpoint de API or interface de programação do aplicativo (API) para exportação de eventos brutos {#new-api-endpoint-for-raw-event-export}

Adicionamos um novo [endpoint de API or interface de programação do aplicativo (API)]({{site.baseurl}}/developer_guide/rest_api/api_network_connectivity_issues#whitelisting-brazes-api-endpoint-ip-ranges), `/raw_data/status`, que permite consultar se um determinado dia foi carregado na exportação de eventos brutos. Você pode usá-lo para verificar se os dados brutos de um determinado dia estão disponíveis, ajudando na depuração e na automação.