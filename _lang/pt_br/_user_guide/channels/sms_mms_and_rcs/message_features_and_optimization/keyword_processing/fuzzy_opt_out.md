---
nav_title: Descadastramento fuzzy
article_title: Descadastramento fuzzy
description: "Este artigo de referência aborda como configurar o descadastramento fuzzy, uma configuração que tenta reconhecer quando uma mensagem recebida não corresponde a uma palavra-chave de descadastramento."
page_type: reference
channel:
  - SMS
  - MMS
  - RCS
page_order: 4

---

# Descadastramento fuzzy {#fuzzy-opt-out}

![Conversa de mensagens no iOS mostrando mensagens de descadastramento enviadas em resposta ao descadastramento fuzzy recebido "Please stopppp".]({% image_buster /assets/img/sms/fuzzy1.jpg %}){: style="float:right;max-width:30%;margin-left:15px;"}

> Usuários que enviam SMS, MMS e RCS com a Braze devem seguir as leis, regulamentações e padrões do setor aplicáveis. Para o descadastramento, leis como o TCPA determinam que, quando um usuário envia qualquer mensagem que constitua uma revogação razoável de consentimento (incluindo palavras-chave de descadastramento reconhecidas como "STOP", "STOPALL", "UNSUBSCRIBE", "CANCEL", "END" ou "QUIT"), todas as mensagens subsequentes relacionadas àquele programa de envio de mensagens devem ser interrompidas. A Braze processa automaticamente as palavras-chave de descadastramento reconhecidas e cancela a inscrição do usuário.<br><br> O descadastramento fuzzy estende essa capacidade ao tentar reconhecer mensagens recebidas que não correspondem a nenhuma **palavra-chave de descadastramento** configurada para a categoria **Descadastramento** do grupo de inscrições (ou seja, qualquer [palavra-chave de descadastramento padrão]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/optin_optout/) ou [palavra-chave de descadastramento personalizada]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling/), mas que ainda indicam intenção de descadastramento — por exemplo, uma mensagem como "goodbye" ou "leave me alone".

O descadastramento fuzzy está desativado por padrão. Se o descadastramento fuzzy estiver ativado e uma mensagem recebida for considerada "fuzzy", você pode configurar a Braze para cancelar automaticamente a inscrição do usuário ou enviar uma mensagem instruindo como se descadastrar manualmente. Para marcas dos EUA, cancelar automaticamente a inscrição do usuário é fortemente recomendado para estar em conformidade com os requisitos do TCPA.

{% alert note %}
Atualmente, apenas palavras-chave de descadastramento (padrão e personalizadas) criadas usando inglês como [idioma local]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/message_features_and_optimization/keyword_processing/keyword_handling/#multi-language-support) são suportadas.
{% endalert %}

## O que é considerado fuzzy? {#what-is-deemed-as-fuzzy}

Os critérios para uma resposta recebida ser considerada "fuzzy" são os seguintes (as comparações usam todas as palavras-chave na categoria **Descadastramento**, incluindo padrão e personalizadas):
- Se trocar uma letra pela letra imediatamente à esquerda ou à direita dela em um teclado QWERTY resultar em uma palavra-chave de descadastramento correspondente.
- Uma substring da mensagem corresponde a uma palavra-chave de descadastramento.

Por exemplo, "Stpo" ou "Please stopppp" serão considerados fuzzy, e uma resposta de descadastramento fuzzy será enviada. Se o usuário então responder com uma palavra-chave de descadastramento, um evento de cancelamento de inscrição será acionado.

## Configurar o descadastramento fuzzy {#configure-fuzzy-opt-out}

Para configurar o descadastramento fuzzy, navegue até a página de gerenciamento de palavras-chave do grupo de inscrições.

1. Acesse **Audience** > **Subscription Group Management** e selecione um grupo de inscrições **SMS/MMS/RCS**.
2. Em **Global Keywords**, encontre a categoria **Opt-out** e selecione o ícone de lápis.
3. Alterne **Fuzzy Opt-Out** para **On**.
4. Selecione sua opção preferida de **Fuzzy Opt-Out Logic**:
   - **Automatically unsubscribe:** Quando um usuário envia uma mensagem semelhante a uma palavra-chave de descadastramento, a inscrição é cancelada imediatamente sem solicitação. A mensagem padrão de confirmação de descadastramento é então enviada.
   - **Send opt-out instructions:** Quando um usuário envia uma mensagem semelhante a uma palavra-chave de descadastramento, a Braze envia uma resposta personalizada (a **Opt-out instruction message**) explicando como cancelar a inscrição.
5. Se você selecionou **Send opt-out instructions**, insira seu texto personalizado no campo **Opt-out instruction message**. Este campo é obrigatório para esta configuração.
6. Selecione **Save**.

![Seção para editar palavras-chave de descadastramento e fornecer uma mensagem de instrução de descadastramento.]({% image_buster /assets/img/sms/fuzzy2.png %})

## Práticas recomendadas para mensagens de descadastramento fuzzy {#best-practices-for-fuzzy-opt-out-messages}

Para garantir uma experiência clara, em conformidade e positiva para seus inscritos, é fundamental configurar sua mensagem de descadastramento fuzzy com cuidado. O principal objetivo da mensagem de descadastramento fuzzy é **orientar usuários que enviam uma mensagem semelhante, mas não exatamente igual, à sua palavra-chave de descadastramento designada**. A mensagem orienta os usuários sobre como cancelar a inscrição com sucesso.

### Considerações críticas {#critical-considerations}

{% alert warning %}
Se você selecionou **Send opt-out instructions**, **não** configure sua mensagem de descadastramento fuzzy para confirmar um cancelamento de inscrição. Sua mensagem de descadastramento fuzzy não deve conter linguagem que implique que o usuário já cancelou a inscrição com sucesso. Por exemplo, **não** use "Sua inscrição foi cancelada", "Você não receberá mais mensagens deste número" ou "Você agora está descadastrado".
{% endalert %}

A mensagem de descadastramento fuzzy é enviada antes de o usuário ter cancelado a inscrição com sucesso. Usar linguagem de confirmação (como "Sua inscrição foi cancelada") induz o inscrito a acreditar que está descadastrado quando não está, levando a mensagens indesejadas contínuas, frustração do inscrito e riscos significativos de conformidade.

Para cancelar a inscrição dos usuários imediatamente após uma correspondência fuzzy, use a configuração **Automatically unsubscribe**.

{% alert warning %}
**NÃO** configure sua mensagem de descadastramento fuzzy para ser idêntica ou semelhante à sua palavra-chave exata de descadastramento.
{% endalert %}

Se sua mensagem fuzzy for igual ou muito parecida com sua palavra-chave exata de descadastramento (por exemplo, se "STOP" é sua palavra-chave exata e sua mensagem fuzzy é "Envie STOP para cancelar a inscrição"), isso pode gerar confusão sobre se a mensagem inicial do usuário realmente resultou em um cancelamento de inscrição ou se ele precisa tomar outra ação. A mensagem fuzzy deve sempre esclarecer qual ação o usuário precisa tomar.

### Exemplos de mensagens de descadastramento fuzzy {#examples-of-fuzzy-opt-out-messages}

Se você escolher **Send opt-out instructions**, concentre sua mensagem em orientar o usuário. Por exemplo, se sua palavra-chave de descadastramento é "STOP", estes são bons e maus exemplos de mensagens de descadastramento fuzzy que você poderia criar:

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Maus exemplos <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Para cancelar a inscrição de todas as mensagens, responda com a palavra STOP."</td>
      <td>"Sua inscrição foi cancelada com sucesso. Você não receberá mais mensagens deste número. Responda START para se reinscrever." (Esta é uma confirmação direta de cancelamento de inscrição, o que é enganoso em um cenário de descadastramento fuzzy.)</td>
    </tr>
    <tr>
      <td>"Recebemos sua mensagem. Se você deseja parar de receber mensagens de texto, envie STOP."</td>
      <td>"STOP." (Esta é apenas a palavra-chave exata, o que não orienta o usuário.)</td>
    </tr>
    <tr>
      <td>"Você quis cancelar a inscrição? Responda STOP para sair de todas as mensagens futuras."</td>
      <td>"Envie STOP para cancelar a inscrição." (Se "STOP" também é sua palavra-chave exata, isso é redundante e não esclarece a ação se a mensagem inicial foi fuzzy.)</td>
    </tr>
  </tbody>
</table>