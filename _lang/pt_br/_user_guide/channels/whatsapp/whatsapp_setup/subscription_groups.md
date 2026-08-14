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

Para definições dos estados de inscrição do WhatsApp e como eles se relacionam com os requisitos de aceitação da Meta, consulte [Status de inscrição]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#whatsapp).

### Definindo os grupos de inscrições do WhatsApp dos usuários {#setting-users-whatsapp-subscription-groups}

- **REST API:** Os perfis de usuário podem ser definidos programaticamente pelo [endpoint `/subscription/status/set`]({{site.baseurl}}/api/endpoints/subscription_groups/post_update_user_subscription_group_status) usando a REST API da Braze.
- **Web SDK:** Os usuários podem ser adicionados a um grupo de inscrições de e-mail, SMS ou WhatsApp usando o método `addToSubscriptionGroup` para [Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-braze-user/add-to-subscription-group.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/user-swift.class/addtosubscriptiongroup(id:fileid:line:)) ou [Web](https://js.appboycdn.com/web-sdk/latest/doc/classes/braze.user.html#addtosubscriptiongroup).
- **Importação de usuário**: Os usuários podem ser adicionados a grupos de inscrições de e-mail ou SMS por meio de **Importar usuários**. Ao atualizar o status do grupo de inscrições, você deve ter estas duas colunas no seu CSV: `subscription_group_id` e `subscription_state`. Consulte [Importação de usuário]({{site.baseurl}}/user_guide/audience/manage_audience/import_users#constructing-your-csv) para saber mais.

### Verificando o grupo de inscrições do WhatsApp de um usuário {#checking-a-users-whatsapp-subscription-group}

- **Perfil de usuário:** Os perfis de usuário individuais podem ser acessados pelo dashboard da Braze em **Público** > **Pesquisar usuários**. Nessa página, você pode pesquisar perfis de usuário por endereço de e-mail, número de telefone ou ID de usuário externo. Dentro de um perfil de usuário, na guia **Engajamento**, você pode visualizar o grupo de inscrições do WhatsApp de um usuário e seu status.

- **REST API:** O grupo de inscrições de perfis de usuário individuais pode ser visualizado pelo [endpoint Listar os grupos de inscrições do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_groups) ou pelo [endpoint Listar o status do grupo de inscrições do usuário]({{site.baseurl}}/api/endpoints/subscription_groups/get_list_user_subscription_group_status) usando a REST API da Braze.

## Arquivar grupos de inscrições {#archive-subscription-groups}

Se você precisar parar de usar um grupo de inscrições do WhatsApp, poderá arquivá-lo para marcá-lo como inativo.

Arquivar um grupo de inscrições o marca como inativo, mas não o exclui do seu espaço de trabalho. Se você precisar remover um número de telefone do WhatsApp ou um grupo de inscrições completamente, primeiro será necessário arquivar o grupo de inscrições no Gerenciamento de grupos de inscrições antes de solicitar a exclusão ao suporte da Braze.

Para arquivar um grupo de inscrições:

1. Acesse **Público** > **Gerenciamento de grupos de inscrições**.
2. Encontre o grupo de inscrições do WhatsApp que deseja arquivar.
3. Passe o cursor sobre o status do grupo de inscrições e selecione <i class="fa-solid fa-box-archive"></i> **Arquivar**.

## Processo de aceitação e cancelamento do WhatsApp {#whatsapp-opt-in-and-opt-out-process}

Para uma visão geral do status de inscrição do WhatsApp, requisitos de aceitação e comportamento de cancelamento, consulte [Status de inscrição]({{site.baseurl}}/user_guide/audience/subscription_preferences/subscription_status#whatsapp).

Atualmente, os usuários podem se inscrever e [aceitar ou cancelar a inscrição]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs) no envio de mensagens do WhatsApp de várias formas, incluindo [SMS](https://github.com/braze-inc/in-app-message-templates/tree/master/braze-templates/4-sms-capture-modal), por meio de um website, uma conversa no WhatsApp, telefone ou pessoalmente. A aceitação é obrigatória.

Palavras-chave de aceitação não são suportadas atualmente para o canal do WhatsApp, então caberá a você manter uma lista de usuários. O WhatsApp tem uma abordagem retrospectiva para aceitações e limites de frequência: se os usuários começarem a denunciar ou bloquear você, seu limite de frequência será reduzido.

## Atualizando o status de inscrição de um usuário para um Canvas do WhatsApp {#update-subscription-status}

Independentemente dos métodos de opt-in e descadastramento que você utiliza, é possível atualizar o status de inscrição dos perfis de usuário com um dos seguintes métodos de atualização:

- Crie um [webhook Braze-to-Braze]({{site.baseurl}}/user_guide/channels/webhooks/use_case_create_a_braze_to_braze_webhook#considerations) que atualize o status de inscrição via REST API, como no exemplo a seguir:

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

![Etapa de atualização de usuário com uma etapa do editor JSON avançado.]({% image_buster /assets/img/whatsapp/whatsapp_json_editor.png %}){: style="max-width:90%;"}

{% alert note %}
As atualizações no status de inscrição de um usuário podem levar até 60 segundos.
{% endalert %}