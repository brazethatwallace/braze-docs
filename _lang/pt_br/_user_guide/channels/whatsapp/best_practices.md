---
nav_title: Melhores práticas
article_title: Melhores práticas
page_order: 22
description: "Este artigo descreve as melhores práticas sugeridas ao usar o canal de envio de mensagens do WhatsApp, incluindo como manter uma classificação de qualidade do telefone alta e evitar uma taxa elevada de bloqueios e denúncias."
page_type: reference
channel:
  - WhatsApp

---
# Melhores práticas para o WhatsApp {#whatsapp-best-practices}

> Antes de enviar suas mensagens pelo WhatsApp, consulte estas melhores práticas sugeridas para manter uma classificação de qualidade do telefone alta, evitar bloqueios e denúncias, e gerenciar o opt-in e o descadastramento de usuários.

## Manter uma classificação de qualidade do telefone alta {#maintain-a-high-phone-quality-rating}

O WhatsApp baseia sua [classificação de qualidade do telefone](https://www.facebook.com/business/help/896873687365001) nas ações realizadas pelos usuários que recebem suas mensagens, como bloquear ou denunciar sua empresa. É importante manter uma classificação de qualidade alta, pois se ela estiver baixa e não melhorar dentro de um determinado período, seu limite de envio de mensagens pode diminuir.

Na primeira vez que você envia uma mensagem a um usuário no WhatsApp, essas opções são exibidas dentro da conversa.

![Conversa do WhatsApp com opções para bloquear ou denunciar uma empresa]({% image_buster /assets/img/whatsapp/whatsapp_block_report.png %}){: style="max-width:30%;"}

{% alert note %}
Para métricas sobre seus bloqueios e denúncias, certifique-se de que a [guia Insights](https://www.facebook.com/business/help/683499390267496) esteja ativada no seu WhatsApp Manager.
{% endalert %}

Para evitar altas taxas de bloqueios e denúncias, a Braze sugere as seguintes melhores práticas para manter uma classificação de qualidade do telefone alta e limites de envio de mensagens estáveis.

### Siga os requisitos e diretrizes de opt-in do WhatsApp {#follow-whatsapp-opt-in-requirements-and-guidelines}

Certifique-se de que todos os usuários tenham consentido ativamente em receber mensagens do WhatsApp antes de começar a se comunicar com eles por esse canal. Ao solicitar o opt-in dos usuários, eles devem ser informados de que estão concordando especificamente em receber mensagens da sua empresa pelo WhatsApp.

{% alert note %}
Para informações sobre requisitos de opt-in e dicas úteis, consulte [Get Opt-in for WhatsApp](https://developers.facebook.com/docs/whatsapp/overview/getting-opt-in/).
{% endalert %}

### Siga as melhores práticas de envio de mensagens {#follow-messaging-best-practices}

- Faça com que o nome do seu canal reflita sua marca para que os usuários reconheçam que a mensagem é sua, e não SPAM.
- Envie uma mensagem de confirmação aos usuários após coletar o consentimento de opt-in.
- Envie mensagens em horários apropriados.

### Dê aos clientes a opção de descadastramento {#give-customers-the-option-to-opt-out}

Os descadastramentos não afetam sua classificação de qualidade do telefone, então é melhor que um usuário cancele o recebimento de comunicações do WhatsApp do que bloqueie ou denuncie você.

Uma melhor prática sugerida é fornecer instruções sobre como cancelar a inscrição no rodapé da primeira mensagem que você enviar aos usuários. Por exemplo, você pode informar que os usuários podem cancelar a inscrição do seu canal do WhatsApp respondendo com sua palavra-gatilho de descadastramento. Você também pode incluir regularmente o rodapé de descadastramento em campanhas futuras. Para saber como configurar isso, consulte [Opt-in e descadastramento]({{site.baseurl}}/user_guide/channels/whatsapp/message_processing/opt_ins_and_opt_outs).

![Mensagem do WhatsApp com um rodapé informando para responder STOP para cancelar a inscrição do canal]({% image_buster /assets/img/whatsapp/whatsapp_unsubscribe.png %}){: style="max-width:35%;"}

### Minimize a latência de resposta em fluxos bidirecionais {#minimize-response-latency-for-two-way-flows}

Para fluxos interativos de Canvas que respondem com [mensagens de resposta]({{site.baseurl}}/user_guide/channels/whatsapp/create_a_whatsapp_message/message_and_image_formats#response-messages):

- Posicione a etapa de mensagem de resposta imediatamente após o disparador de entrada ou a avaliação do Action Path.
- Use [webhooks]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook) em vez de etapas de atualização de usuário quando não forem necessárias alterações de inscrição antes da resposta.
- Evite postergações longas ou esperas de vários dias entre mensagens recebidas e envios de resposta; a janela de atendimento ao cliente do WhatsApp é de 24 horas por mensagem recebida.