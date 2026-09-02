---
nav_title: Aprovações
article_title: Aprovações
page_order: 1
page_type: reference
description: "Este artigo de referência oferece uma visão geral dos diversos status que uma Campaign e um Canvas podem ter e o que eles significam."
tool:
    - Campaigns
    - Canvas
---

# Aprovações para Campaigns e Canvas {#approvals-for-campaigns-and-canvases}

> Use aprovações para adicionar um checkpoint final às suas Campaigns e Canvas antes do lançamento. Com esse fluxo de trabalho, você pode verificar e aprovar o conteúdo em todas as seções obrigatórias da sua mensagem.

## Como funciona {#how-it-works}

Você pode revisar os detalhes da sua Campaign ou Canvas na etapa final de edição.

Tanto para Canvas quanto para Campaigns, você deve salvar todas as alterações antes de aprovar, mesmo que sejam suas próprias alterações. Um usuário com as permissões apropriadas deve aprovar cada seção do resumo antes que a mensagem possa ser lançada. O status padrão de cada seção é **Pending Approval**.

{% tabs %}
{% tab campaign %}
Para lançar uma Campaign, você deve aprovar estes componentes:

- **Messages:** Esta é a mensagem da Campaign.
- **Delivery:** Este é o tipo de entrega e determina quando os usuários recebem a Campaign.
- **Target Audience:** Determina quem receberá a Campaign.
- **Conversion Events:** Esta é a métrica que você está rastreando para fins de engajamento e relatórios.
{% endtab %}

{% tab canvas %}
Para lançar um Canvas, você deve aprovar estes componentes principais:

- **Conversion Events:** Esta é a métrica que você está rastreando para fins de engajamento e relatórios.
- **Entry agendar/cronograma:** Inclui o tipo de cronograma de entrada e quando os usuários entram no Canvas.
- **Target Audience:** Determina quem entrará neste Canvas.
- **Send Settings:** São as opções de envio para todas as etapas do Canvas.
- **Build Canvas:** Esta é a jornada do usuário no Canvas.
{% endtab %}
{% endtabs %}

## Ativando o fluxo de aprovação {#turning-on-the-approval-workflow}

Por padrão, a configuração do fluxo de aprovação está desativada para Campaigns e Canvas. Para ativar esse recurso, acesse **Configurações** > **Fluxo de aprovação** e selecione o botão de alternância aplicável:

- **Use approval workflow for all Campaigns in [seu espaço de trabalho]**
- **Use approval workflow for all Canvases in [seu espaço de trabalho]**

{% alert important %}
A aprovação de Campaigns não é compatível com [Campaigns da API or interface de programação do aplicativo (API)]({{site.baseurl}}/api/api_campaigns) e [Campaigns de e-mail de transação]({{site.baseurl}}/user_guide/channels/transactional_email/create_a_transactional_email).
{% endalert %}

## Definindo permissões de usuário {#setting-user-permissions}

Depois de ativar o fluxo de aprovação, você deve definir as permissões de usuário para que os usuários da sua empresa possam aprovar ou rejeitar Campaigns e Canvas. Ambas as permissões também podem ser aplicadas a espaços de trabalho ou [equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) ou adicionadas a um [conjunto de permissões]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#create-a-permission-set).

{% tabs %}
{% tab campaign %}
Você deve ter a [permissão "Approve and Deny Campaigns"]({{site.baseurl}}/user_guide/administer/global/user_management/permissions). Essa permissão controla quem pode atualizar o status de aprovação de uma Campaign. Com essa permissão, você pode fazer o seguinte:

- Autoaprovar a Campaign
- Aprovar e lançar a Campaign
- Aprovar, mas não lançar a Campaign (um usuário diferente com a permissão "Send Campaigns, Canvases" pode lançar a Campaign)
- Não aprovar nem lançar a Campaign

Depois que os status de aprovação são definidos na etapa **Summary**, quaisquer alterações subsequentes feitas na Campaign redefinem todos os status de aprovação ao salvar. Isso se aplica a quaisquer alterações feitas em uma Campaign em rascunho ou em uma campanha ativa após o lançamento. Por exemplo, se você fizer alterações apenas no público-alvo, a etapa **Summary** reverte os status de aprovação de todas as seções para o estado padrão, **Pending Approval**.

{% endtab %}

{% tab canvas %}
Você deve ter a [permissão "Approve and Deny Canvases"]({{site.baseurl}}/user_guide/administer/global/user_management/permissions). Essa permissão controla quem pode atualizar o status de aprovação de um Canvas. Com essa permissão, você pode fazer o seguinte:

- Autoaprovar o Canvas
- Aprovar e lançar o Canvas
- Aprovar, mas não lançar o Canvas (um usuário diferente com a permissão "Send Campaigns, Canvases" pode lançar o Canvas)
- Não aprovar nem lançar o Canvas

Depois que os status de aprovação são definidos na etapa **Summary**, quaisquer alterações subsequentes feitas no Canvas redefinem todos os status de aprovação ao salvar. Isso se aplica a quaisquer alterações feitas em um Canvas em rascunho ou em um Canvas após o lançamento. Por exemplo, se você fizer alterações apenas no público-alvo, a etapa **Summary** reverte os status de aprovação de todas as seções para o estado padrão, **Pending Approval**.

{% alert note %}
**Status de aprovação e salvamento**

- Quando você clica em **Approve** para uma seção na etapa **Summary**, essa aprovação é salva imediatamente.
- O botão **Save** salva as alterações no conteúdo e nas configurações do Canvas, não o status de aprovação.

Para evitar a perda de aprovações:

1. Faça as edições necessárias no Canvas e clique em **Save**.
2. Depois que o Canvas terminar de salvar, aprove as seções relevantes na etapa **Summary**.
3. Clique em **Save** novamente apenas se fizer alterações adicionais no Canvas após a aprovação. Se você alterar o Canvas e salvar, todos os status de aprovação serão redefinidos para **Pending Approval**.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert important %}
Para editar uma campanha ativa, você precisa da permissão "Approve and Deny Campaigns". O usuário deve aprovar suas alterações porque uma versão em rascunho de Campaigns ainda não está disponível. Esse não é o caso para Canvas, pois um usuário pode fazer alterações e salvar como rascunho, e outro usuário pode aprovar e lançar o Canvas.
{% endalert %}