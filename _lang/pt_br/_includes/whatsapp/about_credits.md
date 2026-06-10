A partir de 1º de julho de 2025, o WhatsApp passou a cobrar por mensagem. As taxas de mensagem são baseadas tanto no código do país do número de telefone do destinatário quanto no tipo de mensagem que você está enviando. O tipo de mensagem é determinado pelo [modelo de mensagem](https://developers.facebook.com/docs/whatsapp/message-templates/guidelines/) que você envia para aprovação no WhatsApp Manager.

{% alert note %}
Todas as conversas iniciadas pela empresa na plataforma devem começar com um modelo de mensagem aprovado.
{% endalert %}

{% if include.content == "h2" %}##{% else include.content == "h3" %}###{% endif %} Definições de modelos de mensagem

Estes são os modelos de mensagem que você pode enviar para aprovação no WhatsApp Manager:

| Modelo | Definição |
|----------|------------|
| **Modelo de marketing**     | Este modelo permite que você alcance uma ampla variedade de objetivos, desde gerar reconhecimento até impulsionar vendas e redirecionar clientes. Exemplos incluem anúncios de novos produtos, serviços ou recursos, promoções ou ofertas direcionadas e lembretes de abandono de carrinho. |
| **Modelo de utilidade**       | Este modelo permite que você faça o acompanhamento de ações ou solicitações dos usuários, já que essas mensagens são normalmente disparadas por ações dos usuários. Exemplos incluem confirmação de opt-in, gerenciamento de pedidos ou entregas (como atualizações de entrega), atualizações ou alertas de conta (como lembretes de pagamento) ou pesquisas de feedback.<br><br>A partir de 1º de julho de 2025:<br>• Os modelos de utilidade devem ser não promocionais, sem qualquer intenção persuasiva.<br>• Os modelos de utilidade devem ser (1) específicos para ou solicitados pelo usuário ou (2) essenciais ou críticos para o usuário. |
| **Modelo de autenticação** | Este modelo permite que você verifique a identidade de um usuário, potencialmente em várias etapas da jornada do cliente (como verificação de conta, recuperação de conta e desafios de integridade).<br><br>Conversas de autenticação serão suportadas apenas caso a caso, e a Braze não pode garantir SLAs específicos. Além disso, a Braze não oferece suporte à geração de PIN. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}

{% if include.content == "h2" %}##{% else include.content == "h3" %}###{% endif %} Tipos de mensagens gratuitas

Veja alguns cenários em que sua mensagem do WhatsApp será gratuita:

| Mensagem | Informações |
|-------|-------|
| Todas as conversas de atendimento | _A partir de 1º de novembro de 2024_<br><br>Quando um usuário envia uma mensagem para sua marca (iniciando a janela de atendimento ao cliente de 24 horas), as mensagens de resposta sem modelo não são cobradas. Nota: se sua marca responder ao usuário com um modelo, você ainda será cobrado com base no tipo de modelo. |
| Modelos de utilidade enviados durante uma janela de atendimento ao cliente de 24 horas | _A partir de 1º de julho de 2025_<br><br>Uma janela de atendimento ao cliente de 24 horas é criada quando um usuário final envia uma mensagem para sua marca. Se sua marca responder com um modelo de utilidade, será gratuito. Modelos de utilidade enviados fora da janela de atendimento ao cliente de 24 horas (por exemplo, modelos de utilidade enviados proativamente pela sua marca para lembretes de conta e atualizações de status de pedido) ainda serão cobrados. |
| Conversas de ponto de entrada gratuitas | Uma conversa de ponto de entrada gratuita é aberta se 1) um usuário enviar uma mensagem para sua marca por meio de um anúncio Click to WhatsApp ou botão de chamada para ação da página do Facebook e 2) sua marca responder dentro de 24 horas. A conversa de ponto de entrada gratuita é aberta assim que sua marca responde e dura 72 horas. Dentro da janela de 72 horas, sua marca pode enviar modelos de mensagem para os usuários gratuitamente. No entanto, sua marca só pode enviar mensagens sem modelo se houver uma janela de atendimento ao cliente de 24 horas aberta. |
| Mensagens de resposta | As mensagens de resposta permitem que sua marca envie mensagens sem modelo em resposta às mensagens dos usuários. As mensagens de resposta podem ser enviadas quando há uma janela de atendimento ao cliente de 24 horas aberta, como quando um usuário envia uma mensagem para sua marca no WhatsApp.<br><br>Lembre-se de que o modelo de mensagem que inicia a conversa ainda será cobrado, mas as mensagens de resposta subsequentes serão gratuitas. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation"}