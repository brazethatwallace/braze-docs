---
nav_title: Opt-in duplo
article_title: Opt-in duplo
description: "Este artigo de referência aborda o recurso de opt-in duplo e explica como ativar o recurso, selecionar palavras-chave de opt-in e mensagens de resposta, e inserir usuários no fluxo de trabalho de opt-in duplo por meio de atualizações de inscrição que ocorrem na REST API, SDK e atualizações da Central de Preferências."
page_type: reference
page_order: 1
channel:
  - SMS
  - MMS
  - RCS
---

# Opt-in duplo {#double-opt-in}

> O recurso de opt-in duplo exige que os usuários confirmem explicitamente sua intenção de opt-in antes de poderem receber mensagens SMS, MMS ou RCS. Isso concentra o envio de mensagens em usuários engajados e apoia as melhores práticas de conformidade.

Quando o opt-in duplo está ativado, os usuários recebem uma mensagem que solicita seu consentimento explícito antes de poderem receber mensagens de suas Campaigns ou Canvas.

Embora não seja um requisito explícito do Telephone Consumer Protection Act de 1991 (TCPA), a Braze recomenda que você configure o opt-in duplo para confirmar que os usuários estão cientes e consentem em fazer parte do seu programa de SMS, MMS ou RCS. Para saber mais sobre conformidade, consulte [Leis, regulamentos e prevenção de abuso para SMS, MMS e RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations).

## Fluxos de trabalho de double opt-in {#double-opt-in-workflows}

O double opt-in permite que você obtenha consentimento explícito por meio de campanhas de aceitação de entrada e saída.

### Saída {#outbound}

Quando um usuário fornece seu número de telefone, ele recebe uma mensagem solicitando seu consentimento.

![Captura de tela de uma mensagem SMS de saída em que a marca envia "Welcome to BRAND text updates! 1 msg a week for the latest offers. Reply Y to opt-in.", o usuário responde com "Y" e a marca responde com "Thanks! You're now opted-in to BRAND alerts. Here is a promo code SMS10 for 10% off your first purchase!"]({% image_buster /assets/img/double_opt_in_outbound.png %}){:style="max-width:40%;"}

### Entrada {#inbound}

Quando um usuário envia uma mensagem contendo uma palavra-chave de aceitação, ele recebe uma mensagem solicitando seu consentimento.

![Captura de tela de uma mensagem SMS de entrada em que um usuário envia "JOIN" e recebe a resposta "Reply Y to confirm you want to JOIN our SMS program. 3msg/week, text STOP at any time to STOP", e então responde "Y".]({% image_buster /assets/img/double_opt_in_inbound.png %}){:style="max-width:40%;"}

## Ativação da aceitação dupla (double opt-in) {#enabling-double-opt-in}

Para ativar a aceitação dupla, acesse a tabela **Global Keywords** no grupo de inscrições aplicável e selecione **Edit** na **Opt-In Keyword Category**. Em seguida, selecione o método de aceitação (**Opt-In** ou **Double Opt-In**). Ao selecionar **Double Opt-In**, a página se expande para mostrar [campos configuráveis](#configurable-fields) adicionais.

![A seção Opt-In Method tem dois métodos de aceitação para escolha: Opt-In e Double Opt-In.]({% image_buster /assets/img/double_opt_in_method.png %}){:style="max-width:50%;"}

### Campos configuráveis {#configurable-fields}

| Categoria   |    Campos    | Descrição
| ----------- |----------- |----------------
| Pedido de aceitação (Opt-In Prompt) | Keywords | São as palavras-chave que um usuário pode enviar por mensagem de texto para indicar a intenção de aceitação. `START` é uma palavra-chave obrigatória. Esse pedido de aceitação também é enviado ao usuário quando o status da inscrição é atualizado pelas fontes listadas na seção [Fontes de inscrição](#subscription-sources).
| | Reply Message | É a resposta inicial que o usuário recebe após enviar uma palavra-chave de aceitação (por exemplo, "Responda Y para confirmar que deseja receber mensagens deste número. Taxas de Msg e Dados podem ser aplicadas.")
| Confirmação de aceitação dupla (Double Opt-In Confirmation) | Keywords | São as palavras-chave com as quais o usuário pode responder para confirmar a intenção de aceitação. É necessário informar pelo menos uma palavra-chave. Essas palavras-chave devem ser especificadas no campo **Opt-In Prompt Reply Message**.
| | Reply Message | É a resposta de confirmação que o usuário recebe após confirmar explicitamente a aceitação, passando a poder receber mensagens. O status do grupo de inscrições do usuário é definido como `Subscribed`.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Campos configuráveis" }

Quando um usuário recebe um pedido de aceitação, ele tem 30 dias para confirmar a intenção de aceitação. Se o usuário quiser se inscrever após esse período de 30 dias, será necessário enviar uma palavra-chave de aceitação para iniciar o fluxo de aceitação dupla novamente.

![Os campos configuráveis têm duas seções, Opt-In Prompt e Double Opt-In Confirmation, cada uma com os campos Keywords e Reply Message.]({% image_buster /assets/img/double_opt_in_fields.png %})

## Status do grupo de inscrições {#subscription-group-status}

Somente após o usuário concluir o fluxo de trabalho de double opt-in, o [status do grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups) é atualizado para `Subscribed`. Se o usuário iniciar o fluxo de trabalho, mas não concluí-lo, ele permanecerá como `Unsubscribed` e não poderá receber mensagens desse grupo de inscrições.

Os usuários também podem ser inseridos no fluxo de trabalho de double opt-in se forem [inscritos por outras fontes]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups) (por exemplo, REST API, SDK).

## Fontes de inscrição {#subscription-sources}

Os usuários também podem entrar no fluxo de trabalho de opt-in duplo por meio de atualizações de inscrição que ocorrem fora de mensagens de entrada. Essas fontes incluem atualizações da REST API, SDK e Central de Preferências. Quando um usuário entra no fluxo de trabalho de opt-in duplo por essas fontes, ele recebe a **Opt-In Prompt Reply Message**.

{% alert important %}
Quando os usuários são inseridos no fluxo de trabalho de opt-in duplo por fontes diferentes de mensagens de entrada, eles recebem no máximo uma mensagem de resposta de pedido de aceitação em um período contínuo de 24 horas, independentemente do número de vezes que são inseridos nesse fluxo de trabalho.
{% endalert %}

Cada fonte de inscrição tem um comportamento de inscrição diferente, conforme descrito na tabela a seguir.

| Origem | Comportamento de inscrição no opt-in duplo |
| ----------- | ----------- |
| SDK | Os usuários entram automaticamente no fluxo de trabalho de opt-in duplo quando inscritos por meio do SDK da Braze. |
| REST API | Os usuários podem ser inseridos no fluxo de trabalho quando o status de inscrição é definido por meio de `/subscription/status/set`, `/v2/subscription/status/set` ou `/users/track` e o parâmetro opcional `use_double_opt_in_logic` é passado como `true` (por exemplo, [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed", "use_double_opt_in_logic": true}]). Se esse parâmetro for omitido, os usuários não serão inseridos no fluxo de trabalho de opt-in duplo. <br><br>Ao usar `use_double_opt_in_logic` com a REST API, se nenhum perfil de usuário estiver associado ao número de telefone fornecido, o status de inscrição não será atualizado e o usuário não poderá entrar no fluxo de trabalho de opt-in duplo. |
| Shopify | Os usuários não são inseridos no fluxo de trabalho de opt-in duplo quando o status de inscrição é definido pela nossa integração com o Shopify. |
| Importação de usuários | Os usuários não são inseridos no fluxo de trabalho de opt-in duplo quando o status de inscrição é definido pela importação de usuários. |
| [Central de Preferências]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center) | Os usuários entram automaticamente no fluxo de trabalho de opt-in duplo quando inscritos por meio de uma Central de Preferências. |
| Etapa de atualização de usuário | Os usuários podem ser inseridos no fluxo de trabalho de opt-in duplo quando o status de inscrição é definido por meio da etapa de atualização de usuário e o parâmetro opcional `use_double_opt_in_logic` é passado como `true`. Se esse parâmetro for omitido, os usuários não serão inseridos no fluxo de trabalho de opt-in duplo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Fontes de inscrição" }

## Suporte a vários idiomas {#multi-language-support}
Para mensagens de entrada, a aceitação dupla é compatível com todos os idiomas definidos no grupo de inscrições. Isso significa que você pode definir suas respostas automáticas em diferentes idiomas, e a Braze enviará a resposta automática associada a um idioma específico quando uma palavra-chave correspondente for recebida.

Os usuários que entram no fluxo de aceitação dupla por meio de atualizações de inscrição que ocorrem fora das mensagens de entrada (por exemplo, SDK, REST API, Shopify) receberão apenas as palavras-chave em inglês.