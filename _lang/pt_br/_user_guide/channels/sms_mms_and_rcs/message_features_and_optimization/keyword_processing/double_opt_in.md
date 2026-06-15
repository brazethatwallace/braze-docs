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

Embora não seja um requisito explícito do Telephone Consumer Protection Act de 1991 (TCPA), a Braze recomenda que você configure o opt-in duplo para confirmar que os usuários estão cientes e consentem em fazer parte do seu programa de SMS, MMS ou RCS. Para saber mais sobre conformidade, consulte [Leis, regulamentos e prevenção de abuso para SMS, MMS e RCS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/compliance_and_delivery/laws_and_regulations/).

## Fluxos de trabalho de opt-in duplo {#double-opt-in-workflows}

O opt-in duplo permite que você obtenha consentimento explícito por meio de campanhas de opt-in de entrada e saída.

### Saída {#outbound}

Quando um usuário fornece seu número de telefone, ele recebe uma mensagem que solicita seu consentimento.

![Captura de tela de mensagem SMS de saída com a marca enviando "Bem-vindo às atualizações de texto da MARCA! 1 msg por semana com as últimas ofertas. Responda S para aceitar.", o usuário respondendo com "S", e a marca respondendo com "Obrigado! Agora você está inscrito nos alertas da MARCA. Aqui está um código promocional SMS10 para 10% de desconto na sua primeira compra!"]({% image_buster /assets/img/double_opt_in_outbound.png %}){:style="max-width:40%;"}

### Entrada {#inbound}

Quando um usuário envia uma mensagem contendo uma palavra-chave de opt-in, ele recebe uma mensagem que solicita seu consentimento.

![Captura de tela de mensagem SMS de entrada onde um usuário envia "ENTRAR" e recebe a resposta "Responda S para confirmar que deseja ENTRAR no nosso programa de SMS. 3 msg/semana, envie PARAR a qualquer momento para PARAR", e então responde "S".]({% image_buster /assets/img/double_opt_in_inbound.png %}){:style="max-width:40%;"}

## Ativando o opt-in duplo {#enabling-double-opt-in}

Para ativar o opt-in duplo, acesse a tabela **Global Keywords** no grupo de inscrições aplicável e clique em **Edit** na **Opt-In Keyword Category**. Em seguida, selecione seu método de opt-in (**Opt-In** ou **Double Opt-In**). Selecionar **Double Opt-In** expandirá a página para mostrar [campos configuráveis](#configurable-fields) adicionais.

![A seção Opt-In Method tem dois métodos de opt-in para escolher: Opt-In e Double Opt-In.]({% image_buster /assets/img/double_opt_in_method.png %}){:style="max-width:50%;"}

### Campos configuráveis {#configurable-fields}

| Categoria | Campos | Descrição
| ----------- | ----------- | ----------------
| Pedido de aceitação | Palavras-chave | São as palavras-chave que um usuário pode enviar para indicar a intenção de opt-in. `START` é uma palavra-chave obrigatória. Esse pedido de aceitação também será enviado ao usuário quando o status de inscrição for atualizado por fontes listadas na seção [Fontes de inscrição](#subscription-sources).
| | Mensagem de resposta | É a resposta inicial que um usuário receberá após enviar uma palavra-chave de opt-in (por exemplo, "Responda S para confirmar que deseja receber mensagens deste número. Taxas de Msg e Dados podem ser aplicadas.")
| Confirmação de opt-in duplo | Palavras-chave | São as palavras-chave com as quais um usuário pode responder para confirmar sua intenção de opt-in. Pelo menos uma palavra-chave é obrigatória. Essas palavras-chave devem ser especificadas no campo **Opt-In Prompt Reply Message**.
| | Mensagem de resposta | É a resposta de confirmação que um usuário receberá após confirmar explicitamente seu opt-in e estar apto a receber mensagens. O status do grupo de inscrições do usuário será definido como `Subscribed`.
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Configurable fields #configurable-fields" }

Quando um usuário recebe um pedido de aceitação, ele tem 30 dias para confirmar sua intenção de opt-in. Se um usuário quiser se inscrever após o período de 30 dias, ele precisará enviar uma palavra-chave de opt-in para iniciar o fluxo de trabalho de opt-in duplo novamente.

![Os campos configuráveis têm duas seções, Pedido de aceitação e Confirmação de opt-in duplo, cada uma com os campos Palavras-chave e Mensagem de resposta.]({% image_buster /assets/img/double_opt_in_fields.png %})

## Status do grupo de inscrições {#subscription-group-status}

Somente após o usuário concluir o fluxo de trabalho de opt-in duplo é que o [status do grupo de inscrições]({{site.baseurl}}/sms_rcs_subscription_groups/) é atualizado para `Subscribed`. Se o usuário iniciar o fluxo de trabalho mas não concluí-lo, ele permanecerá como `Unsubscribed` e não poderá receber mensagens desse grupo de inscrições.

Os usuários também podem ser inseridos no fluxo de trabalho de opt-in duplo se forem [inscritos por outras fontes]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_setup/subscription_groups/) (por exemplo, REST API, SDK).

## Fontes de inscrição {#subscription-sources}

Os usuários também podem entrar no fluxo de trabalho de opt-in duplo por meio de atualizações de inscrição que ocorrem fora de mensagens de entrada. Essas fontes incluem atualizações da REST API, SDK e Central de Preferências. Quando um usuário entra no fluxo de trabalho de opt-in duplo por essas fontes, ele receberá a **Opt-In Prompt Reply Message**.

{% alert important %}
Quando os usuários são inseridos no fluxo de trabalho de opt-in duplo por fontes diferentes de mensagens de entrada, eles recebem no máximo uma mensagem de resposta de pedido de aceitação em um período contínuo de 24 horas, independentemente do número de vezes que são inseridos nesse fluxo de trabalho.
{% endalert %}

Cada fonte de inscrição tem um comportamento de inscrição diferente, conforme descrito na tabela a seguir.

| Origem | Comportamento de inscrição no opt-in duplo |
| ----------- | ----------- |
| SDK | Os usuários entrarão automaticamente no fluxo de trabalho de opt-in duplo quando inscritos por meio do SDK da Braze. |
| REST API | Os usuários podem ser inseridos no fluxo de trabalho quando o status de inscrição é definido por meio de `/subscription/status/set`, `/v2/subscription/status/set` ou `/users/track` e o parâmetro opcional `use_double_opt_in_logic` é passado como `true` (por exemplo, [{"subscription_group_id" : "subscription_group_identifier", "subscription_state" : "subscribed", "use_double_opt_in_logic": true}]). Se esse parâmetro for omitido, os usuários não serão inseridos no fluxo de trabalho de opt-in duplo. |
| Shopify | Os usuários não serão inseridos no fluxo de trabalho de opt-in duplo quando o status de inscrição for definido pela nossa integração com o Shopify. |
| Importação de usuários | Os usuários não serão inseridos no fluxo de trabalho de opt-in duplo quando o status de inscrição for definido pela importação de usuários. |
| [Central de Preferências]({{site.baseurl}}/user_guide/audience/subscription_preferences/preference_center/) | Os usuários entrarão automaticamente no fluxo de trabalho de opt-in duplo quando inscritos por meio de uma Central de Preferências. |
| Etapa de Atualização de usuário | Os usuários podem ser inseridos no fluxo de trabalho de opt-in duplo quando o status de inscrição é definido por meio da etapa de Atualização de usuário e o parâmetro opcional `use_double_opt_in_logic` é passado como `true`. Se esse parâmetro for omitido, os usuários não serão inseridos no fluxo de trabalho de opt-in duplo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Subscription sources #subscription-sources" }

## Suporte multilíngue {#multi-language-support}
Para mensagens de entrada, o opt-in duplo é compatível com todos os idiomas definidos no grupo de inscrições. Isso significa que você pode definir suas respostas automáticas em diferentes idiomas e a Braze enviará a resposta automática associada a um idioma específico quando uma palavra-chave correspondente for recebida.

Os usuários que entram no fluxo de trabalho de opt-in duplo por meio de atualizações de inscrição que ocorrem fora de mensagens de entrada (por exemplo, SDK, REST API, Shopify) receberão apenas as palavras-chave em inglês.