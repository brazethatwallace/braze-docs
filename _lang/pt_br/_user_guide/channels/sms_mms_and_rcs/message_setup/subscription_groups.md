---
nav_title: "Grupos de inscrições"
article_title: Grupos de inscrições de SMS e RCS
page_order: 4
description: "Este artigo de referência aborda grupos de inscrições, estados de inscrição e o processo de configuração de grupos de inscrições para os canais SMS, MMS e RCS."
page_type: reference
alias: /sms_rcs_subscription_groups/
channel:
  - SMS
  - MMS
  - RCS

---

# Grupos de inscrições de SMS, MMS e RCS {#sms-mms-and-rcs-subscription-groups}

> Os grupos de inscrições são a base para o envio de mensagens SMS, MMS e RCS pela Braze. Um grupo de inscrições é uma coleção de [entidades de envio]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/sender_setup) (como remetentes verificados por RCS, códigos curtos de SMS, códigos longos de SMS ou IDs de remetente alfanuméricos de SMS) usadas para um tipo específico de envio de mensagens. Por exemplo, se uma marca planeja enviar mensagens SMS transacionais e promocionais, será necessário configurar dois grupos de inscrições com pools separados de números de telefone de envio no dashboard da Braze.

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## Estados do grupo de inscrições {#subscription-group-states}

Existem dois estados de inscrição para usuários de SMS e RCS: `subscribed` e `unsubscribed`. O estado de inscrição de um usuário reside no nível do grupo de inscrições e não é compartilhado entre grupos de inscrições, o que significa que um usuário pode estar `subscribed` em um grupo de inscrições transacional, mas `unsubscribed` em um grupo promocional. Para as marcas, essa separação de estados garante que elas possam continuar enviando mensagens SMS e RCS relevantes para seus usuários.

| Estado | Definição |
| --------- | ---------- |
| Inscrito | O usuário está inscrito para receber SMS e RCS de um grupo de inscrições específico. Um usuário pode ser inscrito ao ter seu estado de inscrição atualizado pela API de inscrições da Braze ou ao enviar uma resposta com palavra-chave de opt-in. Um usuário deve estar inscrito em um grupo de inscrições de SMS ou RCS para receber SMS, RCS ou ambos. Quando o [double opt-in]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/double_opt_in) está ativado, os usuários devem confirmar sua intenção de opt-in antes que o status de inscrição seja atualizado para `Subscribed`. |
| Cancelou inscrição | O usuário optou explicitamente por não receber mensagens do seu grupo de inscrições de SMS e RCS e dos números de telefone de envio dentro do grupo de inscrições. Eles podem cancelar a inscrição enviando uma resposta com palavra-chave de descadastramento, ou você pode cancelar a inscrição dos usuários pela [API de inscrições da Braze]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status). Usuários que cancelaram a inscrição de um grupo de inscrições de SMS e RCS não receberão mais nenhum SMS ou RCS dos números de telefone de envio que pertencem ao grupo de inscrições.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados do grupo de inscrições" }

### Definir o estado de um usuário {#set-a-users-state}

Quando um número de telefone é atualizado em um perfil de usuário, o novo número de telefone herda o status do grupo de inscrições do usuário. Se o número de telefone for atualizado para um número que já existe na Braze, o status de inscrição desse número de telefone existente será herdado.

Por exemplo, se o Usuário A tem um número de telefone inscrito em vários grupos de inscrições e esse número é adicionado ao Usuário B, o Usuário B será inscrito nos mesmos grupos de inscrições. Para evitar que um usuário herde as inscrições existentes, você pode redefinir os grupos de inscrições do número antigo pela REST API da Braze sempre que um usuário alterar seu número. Se vários usuários compartilharem esse número de telefone, todos serão desinscritos.

Para definir o estado do grupo de inscrições de um usuário, use um dos seguintes métodos:

- **REST API:** Os perfis de usuário podem ser definidos programaticamente pelo [endpoint `/subscription/status/set`]({{ site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status/) usando a REST API da Braze.
- **Integração de SDK:** Os usuários podem ser adicionados a um grupo de inscrições de e-mail ou SMS e RCS usando o método `addToSubscriptionGroup` para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) ou [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup).
- **Formulário IAM de captura de número de telefone:** Os números de telefone dos usuários podem ser coletados pelo modelo de captura de número de telefone no editor de arrastar e soltar de mensagens no app.
- **Tratamento automático ao opt-in/descadastramento do usuário:** Quando os usuários enviam uma [palavra-chave]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout) padrão de opt-in ou descadastramento, a Braze define e atualiza automaticamente o estado de inscrição dos usuários.
- **Importação de usuários:** Os usuários podem ser adicionados a grupos de inscrições de e-mail ou SMS e RCS por meio de **Importar usuários**. Ao atualizar o status do grupo de inscrições, você deve ter estas duas colunas no seu CSV: `subscription_group_id` e `subscription_state`. Consulte [Importação de usuários]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) para saber mais.

#### Atualizar o estado de um usuário em um Canvas {#update-a-users-state-in-a-canvas}

Ao atualizar o status do grupo de inscrições de um usuário como parte de um fluxo do Canvas, use uma etapa de [Atualização de usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) em vez de um webhook. A etapa de Atualização de usuário aguarda a conclusão do processamento antes de avançar o usuário para a próxima etapa, para que as etapas de envio de mensagens subsequentes usem o status de inscrição atualizado.

Se você usar um webhook para atualizar grupos de inscrições, o usuário avança assim que o webhook é enviado — e não quando a alteração de inscrição termina de ser processada. Isso pode criar uma condição de corrida em que uma etapa de SMS subsequente é executada antes que o usuário esteja inscrito, fazendo com que a mensagem falhe para uma parte dos usuários. Se você precisar usar um webhook, adicione uma etapa de postergação de pelo menos 1 minuto antes da próxima etapa de envio de mensagens.

#{% multi_lang_include api/orphaned_subscription_states.md %}

### Verificar o grupo de um usuário {#check-a-users-group}

Para verificar o grupo de inscrições de um usuário, use um dos seguintes métodos:

- **Perfil de usuário:** Os perfis de usuário individuais podem ser acessados pelo dashboard da Braze selecionando **Pesquisa de usuários** na barra lateral. Nessa tela, você pode pesquisar perfis de usuário por endereço de e-mail, número de telefone ou ID de usuário externo. Dentro de um perfil de usuário, na guia Engajamento, você pode visualizar os grupos de inscrições de SMS e RCS de um usuário.
- **REST API:** O grupo de inscrições de perfis de usuário individuais pode ser visualizado pelo [endpoint Listar grupos de inscrições do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) ou pelo [endpoint Listar status do grupo de inscrições do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) usando a REST API da Braze.

## Enviar mensagens com um grupo de inscrições {#send-messages-with-a-subscription-group}

Para lançar uma Campaign de SMS ou RCS pela Braze, selecione um grupo de inscrições no menu suspenso **SMS/MMS/RCS Variants**. Após a seleção, um filtro de público será adicionado automaticamente à sua Campaign ou Canvas, garantindo que apenas os usuários `subscribed` no grupo de inscrições selecionado estejam no público-alvo.

{% alert important %}
Em conformidade com as [diretrizes e regulamentações internacionais de telecomunicações]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations), a Braze nunca enviará SMS ou RCS para usuários que não estejam inscritos no grupo de inscrições selecionado.
{% endalert %}

![Criador de SMS com o menu suspenso do grupo de inscrições aberto e "Messaging Service A for SMS" destacado pelo usuário.]({% image_buster /assets/img/sms/sms_subgroup_select.png %})

## Práticas recomendadas para grupos de inscrições de SMS {#sms-subscription-group-best-practices}

Crie grupos de inscrições de SMS separados para cada finalidade de envio de mensagens (por exemplo, transacional versus marketing) e para cada espaço de trabalho. Quando você opera em vários países, considere grupos separados por região para atender às regras de conformidade locais — por exemplo, as restrições do Brasil sobre janelas de envio promocional.

## Ativar grupos de inscrições {#enable-subscription-groups}

Para ativar grupos de inscrições para SMS, MMS ou RCS, consulte o seguinte:

{% tabs local %}
{% tab SMS %}
Durante o processo de integração de SMS, um gerente de integração da Braze configurará os grupos de inscrições para a conta do seu dashboard. Ele trabalhará com você para determinar quantos grupos de inscrições são necessários e adicionará os números de telefone de envio apropriados aos seus grupos de inscrições. Os prazos para configurar um grupo de inscrições dependerão do tipo de números de telefone que você está adicionando. Por exemplo, solicitações de códigos curtos podem levar de 8 a 12 semanas, enquanto códigos longos podem ser configurados em um dia. Se você tiver dúvidas sobre a configuração do seu dashboard da Braze, entre em contato com seu representante da Braze para obter suporte.
{% endtab %}

{% tab MMS %}
Para enviar uma mensagem MMS, pelo menos um número dentro do seu grupo de inscrições deve estar habilitado para enviar MMS. Isso é indicado por uma tag localizada ao lado do grupo de inscrições.

![Menu suspenso do grupo de inscrições com "Messaging Service A for SMS" destacado. A entrada é prefixada com a tag "MMS".]({% image_buster /assets/img/sms/mms_sub_group_tag.png %}){: style="max-width:40%"}
{% endtab %}

{% tab RCS %}
Um remetente verificado por RCS deve estar presente no seu grupo de inscrições antes que você possa enviar uma mensagem RCS.

Existem duas maneiras de adicionar um remetente verificado por RCS:
- Adicioná-lo a um grupo de inscrições existente
- Criar um novo grupo de inscrições RCS
A escolha depende em grande parte dos casos de uso de RCS nos quais você está interessado.

Dependendo da sua integração, a Braze pode adicionar remetentes verificados por RCS aos seus grupos de inscrições de SMS existentes ou configurar novos grupos de inscrições para você. Em ambos os casos, seu gerente de sucesso do cliente guiará você por uma atualização de tráfego SMS eficiente e sem complicações.
{% endtab %}
{% endtabs %}

## Gerenciar descadastramentos em linguagem natural no Console do agente {#handle-natural-language-opt-outs-in-the-agent-console}

Para um gerenciamento abrangente de inscrições, você pode capturar intenções de descadastramento que fogem das palavras-chave padrão ou personalizadas (como "Por favor, não me mande mais mensagens"). Ao criar um agente de IA, você pode usar análise de sentimento para ajudar a identificar e agir sobre essas solicitações automaticamente.

### Configuração {#setup}

1. No [Console do agente]({{site.baseurl}}/user_guide/brazeai/agents), crie um "Agente de Análise de Sentimento de SMS".

{% alert tip %}
Use o [Operator]({{site.baseurl}}/user_guide/brazeai/agents/creating_agents#agent-templates-built-with-operator) para auxiliar na configuração inicial do agente.
{% endalert %}

{: start="2"}
2. Crie um Canvas baseado em ação disparado por **Send an SMS inbound message**, dentro da categoria de palavra-chave **Other**.
3. Adicione a [etapa de Agente]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/agent_step) ao Canvas para identificar a intenção de descadastramento.
4. Adicione uma [etapa de Mensagem]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step) de SMS subsequente para confirmar a solicitação: "Parece que você está tentando cancelar a inscrição de SMS, então vamos cancelar sua inscrição. Se isso foi um engano, envie START para se inscrever novamente."
5. Adicione uma [etapa de Atualização de usuário]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/user_update) para alterar o status do usuário no grupo de inscrições de SMS específico para "Cancelou inscrição".

{% alert note %}
O uso do Console do agente consome créditos de mensagem ou de ação.
{% endalert %}

## Migrar tráfego de SMS para RCS {#migrate-sms-traffic-to-rcs}

Se você tiver grupos de inscrições de SMS e RCS separados, poderá migrar usuários de SMS para RCS usando um Canvas de uma única etapa.

A Braze recomenda que você teste o envio de RCS para volumes menores de usuários inicialmente e migre mais usuários para o grupo de inscrições RCS ao longo do tempo. Por exemplo, se você tiver 1.000.000 de usuários inscritos em um grupo de inscrições de SMS, isso poderia significar primeiro migrar todos os usuários para o novo grupo de inscrições e depois segmentar um público menor de 50.000 a 100.000 (5-10%) para testar as mensagens RCS.

### Etapa 1: Criar um Canvas e preencher o cronograma de entrada {#step-1-create-a-canvas-and-fill-out-the-entry-schedule}

Crie um Canvas e dê a ele um nome facilmente identificável (como "Transferência de Usuários do Grupo de Inscrições SMS-RCS"). Em seguida, agende a campanha para quando for conveniente para você.

### Etapa 2: Definir seu público {#step-2-define-your-audience}
{: #step-2-define-your-audience}

Defina seu público usando um dos seguintes métodos. Em seguida, vá para a etapa **Configurações de envio** e selecione **Usuários que estão inscritos ou optaram por receber**.

| Método | Descrição |
|------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| **Criar um segmento** | Crie um segmento que inclua todos os usuários em um grupo de inscrições ou um subconjunto usando filtros de segmentação (como 5-10% aleatórios). Os segmentos são atualizados antes de cada envio para refletir sua base de usuários atual. |
| **Aplicar filtros de Campaign ou Canvas** | Refine o público na etapa **Público-alvo** da sua Campaign ou Canvas. Ajuste as opções de direcionamento sem sair da página para maior flexibilidade. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 2: Definir seu público" }

### Etapa 3: Configurar uma etapa de Atualização de usuário {#step-3-configure-a-user-update-step}

Adicione uma etapa de Atualização de usuário ao seu Canvas. Na etapa, abra o **Editor JSON avançado** e insira o seguinte (para o campo de identificador único do usuário, recomendamos usar o campo `braze_id`):

{% raw %}
```json
{
  "attributes": [
    {
      "braze_id": "{{${braze_id}}}",
      "subscription_groups": [
        {
          "subscription_group_id": "xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxx",
          "subscription_state": "subscribed",
          "use_double_opt_in_logic": true
        }
      ]
    }
  ]
}
```
{% endraw %}

![Objeto de Atualização de Usuário que contém o código JSON mencionado anteriormente.]({% image_buster /assets/img/sms/user_update_object.png %})

### Etapa 4: Testar o Canvas {#step-4-test-the-canvas}

Recomendamos fortemente [testar seu Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/sending_test_canvases) para confirmar que ele funciona conforme o esperado antes de enviá-lo para seu público mais amplo.

### Etapa 5: Lançar seu Canvas {#step-5-launch-your-canvas}

Após testar seu Canvas com sucesso, lance-o para seu subconjunto de usuários!

Para confirmar que seus usuários foram migrados com sucesso, recomendamos verificar alguns perfis de usuário individuais que foram atualizados. Na guia **Engajamento**, procure por **Configurações de contato** e role para visualizar os grupos de inscrições nos quais o usuário está inscrito. O toggle do grupo de inscrições RCS agora deve estar ativado.

Para a configuração de remetente e grupo de inscrições RCS, consulte também [Configurar RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/rcs_setup).

## Práticas recomendadas {#best-practices}

### Designar grupos de inscrições separados {#designate-separate-subscription-groups}

- **Tipo de envio de mensagens:** Crie grupos de inscrições distintos para cada tipo de envio de mensagens, como transacional e marketing.
- **Espaço de trabalho:** Crie grupos de inscrições distintos para cada espaço de trabalho para manter clareza e organização.

Considere o seguinte exemplo com quatro grupos de inscrições em dois espaços de trabalho:

- **Espaço de trabalho de produção**
  - Marketing - PROD para SMS
  - Transacional - PROD para SMS
- **Espaço de trabalho de desenvolvimento (para testes)**
  - Marketing - DEV para SMS
  - Transacional - DEV para SMS

### Usar convenções de nomenclatura claras {#use-clear-naming-conventions}

Escolha nomes de grupos de inscrições descritivos e claros para que o grupo correto seja selecionado ao criar Campaigns de SMS.

### Separar grupos por país {#separate-groups-by-country}

As regulamentações de SMS variam por país. Sugerimos separar os grupos de inscrições de SMS por país. Isso ajuda você a atender aos padrões de conformidade em todas as regiões onde envia mensagens.

Para cada grupo de inscrições, você também pode configurar uma lista de permissões de países em **Permissões geográficas** para que SMS, MMS e RCS sejam enviados apenas para regiões aprovadas. Para saber mais, consulte [Permissões geográficas]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/geographic_permissions).

Por exemplo, no Brasil, o envio de mensagens de marketing fora do horário das 9h às 21h no horário local é proibido, e o país abrange três fusos horários. Para cumprir essas regulamentações, você pode configurar grupos separados para enviar mensagens ao Brasil e aos Estados Unidos. Isso evita que usuários no Brasil recebam mensagens de marketing durante horários proibidos.