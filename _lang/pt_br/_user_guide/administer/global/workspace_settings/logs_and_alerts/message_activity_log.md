---
nav_title: Registro de atividades de envio de mensagem
article_title: Registro de atividades de envio de mensagem
page_order: 3
page_type: reference
description: "Este artigo de referência descreve o Registro de atividades de envio de mensagem, que mostra as mensagens associadas às suas campanhas e envios. Aqui, você também encontra informações sobre como entender as mensagens do registro."

---

# Registro de atividades de envio de mensagem {#dev-console-troubleshooting}

> O **Registro de atividades de envio de mensagem** permite que você veja todas as mensagens (especialmente mensagens de erro) associadas às suas campanhas e envios.

Você pode ver transações de campanhas da API, solucionar problemas com detalhes sobre mensagens com falha e obter insights sobre como melhorar a entrega de notificações ou resolver problemas técnicos existentes.

Para acessar o registro, acesse **Configurações** > **Registro de atividades de envio de mensagem**.

![Registro de atividades de envio de mensagem]({% image_buster /assets/img_archive/message_activity_log.png %})

{% alert tip %}
Além deste artigo, também recomendamos conferir nosso curso do Braze Learning [Ferramentas de garantia de qualidade e debug](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), que aborda como usar o Registro de atividades de envio de mensagem para conduzir sua própria solução de problemas e debug.
{% endalert %}

Você pode filtrar pelo seguinte conteúdo registrado no **Registro de atividades de envio de mensagem**:

- Erros de notificação por push
- Erros de mensagens no app com modelo abortado
- Erros de webhook
- Erros de e-mail
- Registros de mensagens da API
- Erros de Conteúdo conectado
- Erros de público conectado da REST API
- Erros de aliasing de usuário
- Erros de Testes A/B
- Erros de SMS/MMS
- Erros de WhatsApp
- Erros de Live Activity
- Erros de gatilho de usuário inválido
- Erros de [limite diário de invocações]({{site.baseurl}}/user_guide/brazeai/agents/deploying_agents/#monitor-your-agent) do Braze Agents
- Erros de [modelo]({{site.baseurl}}/user_guide/brazeai/agents/reference/#models) indisponível do Braze Agents

Essas mensagens podem vir do nosso próprio sistema, dos seus apps ou plataformas, ou dos nossos parceiros terceiros. Isso pode resultar em um número infinito de mensagens que podem aparecer neste registro.

## Entendendo as mensagens do registro {#understanding-log-messages}

Para determinar o que suas mensagens significam, preste atenção ao texto de cada mensagem e às colunas correspondentes, pois isso pode ajudar na solução de problemas usando pistas de contexto.

Por exemplo, se você tem uma entrada no registro cuja mensagem diz "empty-cart_app" e não tem certeza do que isso significa, olhe para a coluna **Tipo** à esquerda. Se você vir "Erro de mensagem abortada", pode assumir com segurança que a mensagem foi o que foi escrito como [mensagem de aborto]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/#abort-messages) usando Liquid, e que a mensagem foi abortada porque o destinatário pretendido tinha um carrinho vazio no seu app.

### Mensagens comuns {#common-messages}

Existem alguns tipos de mensagens comuns que você pode ver, e alguns podem até fornecer links de solução de problemas para ajudar a diagnosticar e corrigir problemas.

As mensagens listadas a seguir são apenas para fins de exemplo e podem não corresponder exatamente ao que é exibido na coluna **Mensagem** do seu registro.

| Tipo de mensagem | Mensagem potencial | Descrição |
|---|---|---|
| Soft Bounce | O endereço de e-mail same@example.com teve um soft bounce. | O endereço de e-mail era válido e a mensagem de e-mail chegou ao servidor de e-mail do destinatário, mas foi rejeitada por um problema "temporário". <br><br>Motivos comuns de soft bounce incluem: {::nomarkdown} <ul> <li> A caixa de entrada estava cheia (o usuário excedeu sua cota) </li> <li> O servidor estava fora do ar </li> <li> A mensagem era grande demais para a caixa de entrada do destinatário </li>  </ul> {:/} Se um e-mail recebeu um soft bounce, geralmente tentamos novamente dentro de um período de 72 horas, mas o número de tentativas varia de destinatário para destinatário. |
| Hard Bounce | A conta de e-mail que você tentou alcançar não existe. Tente verificar novamente o endereço de e-mail do destinatário em busca de erros de digitação ou espaços desnecessários. | Sua mensagem nunca chegou à caixa de entrada dessa pessoa porque não havia caixa de entrada para alcançar. Se quiser investigar mais, mensagens como essa às vezes podem ter links na coluna **Ver informações** que permitem visualizar o perfil do destinatário pretendido.|
| Bloqueio | A mensagem de spam foi rejeitada por causa da política anti-spam. | Sua mensagem foi categorizada como spam. Esse erro de e-mail é registrado para um usuário se recebermos um evento do ESP indicando que o e-mail foi descartado. Pode ser apenas para aquele destinatário específico, mas se você está vendo essa mensagem com frequência, talvez queira reavaliar seus hábitos de envio ou o conteúdo da sua mensagem. Além disso, pense: você [aqueceu seu IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/)? Se não, fale com a Braze para obter orientações sobre como fazer isso.|
| Erro de mensagem abortada | empty-cart_web | Se você tem um app com carrinho ou cria um envio com uma mensagem de aborto no Liquid, pode personalizar qual mensagem é retornada se o envio for abortado. Neste caso, a mensagem retornada é empty-cart_web.|
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Mensagens comuns" }

### Por que minha mensagem não está listada aqui? {#why-isnt-my-message-listed-here}

As mensagens no Registro de atividades de envio de mensagem podem vir de diversas fontes: da Braze, dos seus apps ou plataformas, ou dos nossos parceiros terceiros. Isso significa que há um número infinito de mensagens que podem aparecer neste registro — como você pode imaginar, não é possível listar todas!

Por exemplo, algumas possíveis mensagens de "Bloqueio", além da listada na tabela anterior, podem ser:

- Infelizmente, as mensagens de [_IP_ADDRESS_] não foram enviadas. Entre em contato com seu provedor de acesso à internet, pois parte da rede dele está na nossa lista de bloqueio.
- Mensagem rejeitada devido à política local.
- A mensagem foi bloqueada pelo destinatário como spam.
- Serviço indisponível, host do cliente [_IP_ADDRESS_] bloqueado usando Spamhaus.

## Período de retenção de armazenamento {#storage-retention-period}

Erros das últimas 60 horas estão disponíveis no Registro de atividades de envio de mensagem. Registros com mais de 60 horas são limpos e não estão mais acessíveis.

### Número de registros de erro armazenados {#number-of-error-logs-stored}

O número de registros salvos é influenciado por diversas condições. Por exemplo, se uma campanha agendada é enviada para milhares de usuários, potencialmente veríamos uma amostra dos erros no Registro de atividades de envio de mensagem em vez de todos os erros. A seguir, uma visão geral das condições que afetam quantos registros são salvos:
- Até 20 registros de erro do mesmo tipo são salvos para a mesma Campaign ou etapa do Canvas dentro de uma hora fixa de relógio para os seguintes tipos de erro:
    - Erros de Conteúdo conectado
    - Erros de mensagem abortada
    - Erros de webhook
    - Erros de rejeição de SMS
    - Erros de falha de entrega de SMS
    - Erros de falha de WhatsApp
    - Erros de Testes A/B
- Até 20 registros de erro de notificação por push do mesmo tipo são salvos para a mesma Campaign ou etapa do Canvas e combinação de app para os seguintes tipos de erro:
    - Credencial de push inválida
    - Token por push inválido
    - Sem credencial de push
    - Erros de token
    - Cota excedida
    - Tempo limite de tentativas esgotado
    - Carga útil inválida
    - Erro inesperado
- Até 100 registros de erro do mesmo tipo são salvos para o mesmo app dentro de uma hora fixa de relógio para os seguintes tipos de erro:
    - Erro de Live Activity (sem credencial de push)
    - Erro de Live Activity (credencial de push inválida)
    - Outros erros de Live Activity
    - Erros de token removido por feedback do APNs
- Até 100 registros de erro do mesmo tipo são salvos para a mesma Campaign ou etapa do Canvas dentro de uma hora fixa de relógio para os seguintes tipos de erro:
    - Erros de soft bounce de e-mail
    - Erros de hard bounce de e-mail
    - Erros de bloqueio de e-mail
- Até 100 registros de erro de aliasing de usuário são salvos para o mesmo espaço de trabalho dentro de uma hora fixa de relógio.

## Envios de teste {#test-sends}

O **Registro de atividades de envio de mensagem** mostra registros de teste para estes canais de envio de mensagens:

- SMS
- WhatsApp
- LINE
- KakaoTalk
- Webhook

Registros de envio de teste não estão disponíveis para os seguintes canais: e-mail, Content Cards, mensagens no app e push.

Os registros de envio de teste são prefixados com "[TEST SEND]", mas não é garantido que todos os registros de envio de teste tenham o prefixo (por exemplo, erros de Conteúdo conectado não têm o prefixo).