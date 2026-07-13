---
nav_title: "Grupos de inscrições"
article_title: "Grupos de inscrições"
page_order: 4
description: "Este artigo descreve os grupos de inscrições do WhatsApp, quais estados de inscrição são oferecidos e como os grupos de inscrições são configurados."
page_type: reference
alias: /whatsapp_subscription_groups/
channel:
  - WhatsApp

---

# Grupos de inscrições do WhatsApp {#whatsapp-subscription-groups}

> Os grupos de inscrições do WhatsApp são criados ao integrar o WhatsApp com seu app por meio do **Technology Partner Portal**.

{% multi_lang_include alerts/note_alerts.md alert='subscription group limit' %}

## Estados de inscrição do WhatsApp {#whatsapp-subscription-states}

Existem dois estados de inscrição para usuários do WhatsApp: `subscribed` e `unsubscribed`.

| Estado | Definição |
| --- | --- |
| Inscrito | O usuário confirmou explicitamente que deseja receber mensagens do WhatsApp de uma empresa específica. Os usuários podem ser inscritos tendo seu estado de inscrição atualizado por meio da API de inscrição da Braze ou implantando uma estratégia de opt-in, conforme as diretrizes do WhatsApp. |
| Cancelou inscrição | O usuário não deu consentimento explícito para opt-in ou seu status de opt-in foi explicitamente removido. <br><br> Usuários que cancelaram a inscrição de um grupo de inscrições do WhatsApp não receberão mais nenhuma mensagem do WhatsApp dos números de telefone de envio que pertencem ao grupo de inscrições. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Estados de inscrição do WhatsApp" }

### Configurando os grupos de inscrições do WhatsApp dos usuários {#setting-users-whatsapp-subscription-groups}

- **REST API:** os perfis de usuário podem ser definidos programaticamente pelo [endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) usando a REST API da Braze.
- **SDK Web:** os usuários podem ser adicionados a um grupo de inscrições de e-mail, SMS ou WhatsApp usando o método `addToSubscriptionGroup` para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) ou [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup).
- **Importação de usuários**: os usuários podem ser adicionados a grupos de inscrições de e-mail ou SMS por meio de **Importar usuários**. Ao atualizar o status do grupo de inscrições, você deve ter estas duas colunas no seu CSV: `subscription_group_id` e `subscription_state`. Consulte [Importação de usuários]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#updating-subscription-group-status) para saber mais.

### Verificando o grupo de inscrições do WhatsApp de um usuário {#checking-a-users-whatsapp-subscription-group}

- **Perfil de usuário:** perfis de usuário individuais podem ser acessados pelo dashboard da Braze em **Audience** > **Search Users**. Aqui, você pode pesquisar perfis de usuário por endereço de e-mail, número de telefone ou ID de usuário externo. Dentro de um perfil de usuário, na guia **Engagement**, você pode visualizar o grupo de inscrições do WhatsApp de um usuário e seu status.

- **REST API:** o grupo de inscrições de perfis de usuário individuais pode ser visualizado pelo [endpoint Listar grupos de inscrições do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) ou pelo [endpoint Listar status do grupo de inscrições do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) usando a REST API da Braze.

## Arquivar grupos de inscrições {#archive-subscription-groups}

Se você precisar parar de usar um grupo de inscrições do WhatsApp, pode arquivá-lo para marcá-lo como inativo.

Arquivar um grupo de inscrições o marca como inativo, mas não o exclui do seu espaço de trabalho. Se você precisar remover completamente um número de telefone do WhatsApp ou um grupo de inscrições, primeiro é necessário arquivar o grupo de inscrições no Gerenciamento de grupos de inscrições antes de solicitar a exclusão ao suporte da Braze.

Para arquivar um grupo de inscrições:

1. Acesse **Audience** > **Subscription Group Management**.
2. Encontre o grupo de inscrições do WhatsApp que deseja arquivar.
3. Passe o cursor sobre o status do grupo de inscrições e selecione <i class="fa-solid fa-box-archive" aria-label="Arquivar"></i> **Arquivar**.

## Processo de opt-in e descadastramento do WhatsApp {#whatsapp-opt-in-and-opt-out-process}

Atualmente, os usuários podem se inscrever e fazer [opt-in e descadastramento]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs) do envio de mensagens do WhatsApp de várias maneiras, incluindo [SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal), por meio de um site, uma conversa no WhatsApp, telefone ou pessoalmente. Observe que os opt-ins são obrigatórios.

Palavras-chave de opt-in não são suportadas atualmente para o canal do WhatsApp, então caberá a você manter uma lista de usuários. O WhatsApp tem uma abordagem retrospectiva para opt-ins e limites de taxa. Se os usuários começarem a denunciar ou bloquear você, seu limite de taxa será reduzido.

## Atualizando o status de inscrição de um usuário para um Canvas do WhatsApp {#update-subscription-status}

Independentemente dos métodos de opt-in e descadastramento que você utiliza, é possível atualizar o status de inscrição dos perfis de usuário com um dos seguintes métodos de atualização:

- Crie um [webhook Braze-to-Braze]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook#things-to-know) que atualize o status de inscrição via REST API, como no exemplo a seguir:

![Criador de webhook com uma mensagem usando o método POST.]({% image_buster /assets/img/whatsapp/whatsapp118.png %}){: style="max-width:90%;"}

Para evitar condições de corrida, qualquer envio de mensagens subsequente após o webhook deve estar contido em um segundo Canvas que seja disparado por resultados do primeiro Canvas (como um usuário ter entrado em uma variação do Canvas e estar em um grupo de inscrições do WhatsApp).

- Use o editor JSON avançado para atualizar o perfil de usuário com o seguinte modelo:

	```json
	{
	  "attributes": [
	  {
	  	"subscription_groups": [{
	  	  "subscription_group_id": "subscription_group_identifier_1",
	  	  "subscription_state": "unsubscribed"
	  	   },
	  	   {
	  	     "subscription_group_id": "subscription_group_identifier_2",
	  	     "subscription_state": "subscribed"
	  	     },
	  	     {
	  	       "subscription_group_id": "subscription_group_identifier_3",
	  	       "subscription_state": "subscribed"
	  	    }
	  	  ]
	  	}
	  ]
	}
	```

![Etapa de Atualização de usuário com uma etapa do Editor JSON Avançado.]({% image_buster /assets/img/whatsapp/whatsapp_json_editor.png %}){: style="max-width:90%;"}

{% alert note %}
As atualizações no status de inscrição de um usuário podem levar até 60 segundos.
{% endalert %}