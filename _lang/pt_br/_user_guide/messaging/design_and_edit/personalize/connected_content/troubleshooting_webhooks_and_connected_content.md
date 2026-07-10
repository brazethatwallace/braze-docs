---
nav_title: Solucionar problemas de webhooks e Conteúdo conectado
article_title: Solucionar problemas de solicitações de webhook e Conteúdo conectado
page_order: 4
description: "Este artigo aborda como solucionar problemas de códigos de erro de webhook e Conteúdo conectado, incluindo o que são os erros e as etapas para resolvê-los."
---

# Solucionar problemas de solicitações de webhook e Conteúdo conectado {#troubleshoot-webhook-and-connected-content-requests}

> Este artigo aborda como solucionar problemas de códigos de erro comuns para webhooks e Conteúdo conectado, além de fornecer explicações adicionais sobre como esses erros podem ocorrer nas suas solicitações.

## Erros 4XX {#4xx-errors}

Erros `4XX` indicam que há um problema com a solicitação enviada ao endpoint. Esses erros geralmente são causados por solicitações incorretas, incluindo parâmetros malformados, cabeçalhos de autenticação ausentes ou URLs incorretas. Esses erros também se aplicam ao [Criador de relatórios]({{site.baseurl}}/user_guide/analytics/reports/report_builder).

Consulte a tabela a seguir para detalhes dos códigos de erro e etapas para resolução:

<style>
table td {
    word-break: break-word;
}
</style>

<table aria-label="Erros 4XX">
  <caption>Erros 4XX</caption>
  <thead>
    <tr>
      <th>Código de erro</th>
      <th>O que significa</th>
      <th>Etapas para resolução</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>400 Bad Request</b></td>
      <td>Há uma sintaxe inválida na solicitação.</td>
      <td>
        <ul>
          <li>Verifique a carga útil da solicitação em busca de erros de sintaxe.</li>
          <li>Confirme que todos os campos obrigatórios estão incluídos e formatados corretamente.</li>
          <li>Se você estiver enviando uma carga útil JSON, valide a estrutura do JSON.</li>
          <li>Se você estiver usando Liquid para incluir tags de personalização na solicitação de webhook, verifique se o Liquid não resolve para um valor em branco ou produz caracteres que quebram o JSON (como aspas sem escape). Pré-visualize a mensagem para um usuário teste para confirmar que a saída renderizada é válida.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>401 Unauthorized</b></td>
      <td>A solicitação requer autenticação do usuário.</td>
      <td>
        <ul>
          <li>Verifique se as credenciais de autenticação corretas (como chaves de API ou tokens) estão incluídas nos cabeçalhos da solicitação.</li>
          <li>Confirme que você tem as permissões de usuário para acessar o endpoint.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>403 Forbidden</b></td>
      <td>O endpoint entende a solicitação, mas se recusa a autorizá-la.</td>
      <td>
        <ul>
          <li>Verifique se a chave de API ou o token tem as permissões necessárias.</li>
          <li>Confirme que você tem as permissões de usuário para acessar o endpoint.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>404 Not Found</b></td>
      <td>O endpoint não consegue encontrar o recurso solicitado.</td>
      <td>
        <ul>
          <li>Verifique a URL do endpoint em busca de erros de digitação ou caminhos incorretos.</li>
          <li>Confirme que o recurso que você está tentando acessar existe.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>405 Method Not Allowed</b></td>
      <td>O método da solicitação é conhecido pelo endpoint, mas não é suportado pelo recurso de destino.</td>
      <td>
        <ul>
          <li>Verifique o método HTTP (DELETE, GET, POST, PUT) usado na solicitação.</li>
          <li>Confirme que o endpoint suporta o método que você está usando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>408 Request Timeout</b></td>
      <td>O endpoint atingiu o tempo limite ao processar a solicitação.</td>
      <td>
        <ul>
          <li>Verifique o método HTTP (DELETE, GET, POST, PUT) usado na solicitação.</li>
          <li>Confirme que o endpoint suporta o método que você está usando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>409 Conflict</b></td>
      <td>A solicitação está incompleta devido a um conflito com o estado atual do recurso.</td>
      <td>
        <ul>
          <li>Verifique o método HTTP (DELETE, GET, POST, PUT) usado na solicitação.</li>
          <li>Confirme que o endpoint suporta o método que você está usando.</li>
        </ul>
      </td>
    </tr>
    <tr>
      <td><b>429 Too Many Requests</b></td>
      <td>Muitas solicitações foram enviadas em um determinado período de tempo.</td>
      <td>
        <ul>
          <li>Reduza o limite de frequência na sua Campaign ou etapa do Canvas.</li>
        </ul>
      </td>
    </tr>
  </tbody>
</table>

## Erros 5XX {#5xx-errors}

Erros `5XX` indicam que há um problema com o endpoint. Esses erros geralmente são causados por problemas no lado do servidor.

| Código de erro | O que significa |
|-------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------------------|
| **500 Internal Server Error** | O endpoint encontrou uma condição inesperada que o impediu de concluir a solicitação. |
| **502 Bad Gateway** | O endpoint recebeu uma resposta inválida do servidor upstream. |
| **503 Service Unavailable** | O endpoint está temporariamente incapaz de processar a solicitação devido a uma sobrecarga temporária ou manutenção. |
| **504 Gateway Timeout** | O endpoint não recebeu uma resposta em tempo hábil do servidor upstream. |
| **529 Host Overloaded** | O host do endpoint está sobrecarregado e não conseguiu responder. |
| **598 Host Unhealthy** | A Braze simulou a resposta porque o host do endpoint está temporariamente marcado como não íntegro. Para saber mais, consulte [Detecção de host não íntegro](#unhealthy-host-detection). |
| **599 Connection Error** | A Braze encontrou um erro de tempo limite de conexão de rede ao tentar estabelecer uma conexão com o endpoint, o que significa que o endpoint pode estar instável ou fora do ar. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Erros 5XX" }

### Resolvendo erros 5XX {#resolving-5xx-errors}

Aqui estão dicas para solucionar erros `5XX` comuns:

- Revise a mensagem de erro para obter detalhes específicos disponíveis no **Registro de atividades de envio de mensagem**. Para webhooks, acesse a seção **Performance Over Time** na página inicial da Braze e selecione as estatísticas de webhooks. A partir daí, você pode encontrar o timestamp que indica quando os erros ocorreram.
- Certifique-se de que você não está enviando muitas solicitações que sobrecarregam o endpoint. Você pode enviar em lotes ou ajustar o limite de frequência para verificar se isso reduz os erros.

## Detecção de host não íntegro {#unhealthy-host-detection}

Os webhooks e o Conteúdo conectado da Braze utilizam um mecanismo de detecção de host não íntegro para detectar quando o host de destino apresenta uma alta taxa de lentidão significativa ou sobrecarga, resultando em tempos limite, muitas solicitações ou outros resultados que impedem a Braze de se comunicar com sucesso com o endpoint de destino. Ele atua como uma proteção para reduzir a carga desnecessária que pode estar causando dificuldades ao host de destino. Também serve para estabilizar a infraestrutura da Braze e manter velocidades rápidas de envio de mensagens.

Os limites de detecção diferem entre webhooks e Conteúdo conectado:
- **Para webhooks**: Se o número de **falhas exceder 3.000 em qualquer janela de tempo móvel de um minuto** (por combinação única de nome de host e grupo de apps&#8212;**não** por caminho de endpoint), a Braze interrompe temporariamente as solicitações ao host de destino por um minuto.
- **Para Conteúdo conectado**: Se o número de **falhas exceder 3.000 E a taxa de erro exceder 90% em qualquer janela de tempo móvel de um minuto** (por combinação única de nome de host e grupo de apps&#8212;**não** por caminho de endpoint), a Braze interrompe temporariamente as solicitações ao host de destino por um minuto.

Quando as solicitações são interrompidas, a Braze simula respostas com um código de erro `598` para indicar a integridade comprometida. Após um minuto, a Braze retoma as solicitações em velocidade total se o host for considerado íntegro. Se o host ainda estiver não íntegro, a Braze aguarda mais um minuto antes de tentar novamente.

Os seguintes códigos de erro contribuem para a contagem de falhas do detector de host não íntegro: `408`, `429`, `502`, `503`, `504`, `529`.

Para webhooks, a Braze tenta automaticamente reenviar solicitações HTTP que foram interrompidas pelo detector de host não íntegro. Essa tentativa automática usa backoff exponencial e tenta apenas algumas vezes antes de falhar. Para saber mais sobre erros de webhook, consulte [Erros, lógica de nova tentativa e tempos limite]({{site.baseurl}}/user_guide/channels/webhooks/create_a_webhook#errors-retry-logic-and-timeouts).

Para Conteúdo conectado, se as solicitações ao host de destino forem interrompidas pelo detector de host não íntegro, a Braze continua a renderizar mensagens e seguir sua lógica Liquid como se tivesse recebido um código de resposta de erro. Se você quiser garantir que essas solicitações de Conteúdo conectado sejam reenviadas quando interrompidas pelo detector de host não íntegro, use a opção `:retry`. Para saber mais sobre a opção `:retry`, consulte [Novas tentativas de Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/connected_content_retries).

Se você acredita que a detecção de host não íntegro pode estar causando problemas, entre em contato com o [suporte da Braze]({{site.baseurl}}/support_contact).

### Conteúdo conectado não retorna corpo de resposta {#connected-content-returns-no-response-body}

Se uma chamada de Conteúdo conectado aparece em branco na pré-visualização ou no envio da mensagem, verifique:

- **Espaços não separáveis na URL:** A Braze remove espaços não separáveis (`&nbsp;` ou Unicode `U+00A0`) das URLs de Conteúdo conectado antes de fazer a solicitação. Se a URL foi copiada de um documento ou campo do dashboard que inseriu espaços não separáveis entre os caracteres, a solicitação pode falhar ou não retornar um corpo utilizável. Redigite a URL em texto simples ou remova os espaços ocultos e pré-visualize novamente.
- **Erros HTTP e corpos vazios:** Para códigos de status anteriores nesta seção a partir de 300 ou hosts bloqueados, o Conteúdo conectado pode renderizar uma string vazia. Consulte [Fazendo uma chamada de API]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call) e revise as falhas no **Registro de atividades de envio de mensagem**.

## E-mails automatizados e entradas no Registro de atividades de envio de mensagem {#automated-emails-and-message-activity-log-entries}

### Configurando e-mails automatizados {#setting-up-automated-emails}

Se você tiver mais de 100.000 erros de endpoint de webhook ou Conteúdo conectado (incluindo novas tentativas) em um espaço de trabalho em um período de 24 horas, a Braze envia um e-mail com as seguintes informações sobre como resolver os erros.

- Nome do espaço de trabalho
- Um link para o Canvas ou Campaign
- URL do endpoint
- Código de erro
- Hora em que o erro foi observado pela última vez
- Links para o Registro de atividades de envio de mensagem e documentação relacionada

{% alert note %}
Você pode configurar o limite de erros por espaço de trabalho. Para ajustar esse limite, entre em contato com o [suporte da Braze]({{site.baseurl}}/support_contact).
{% endalert %}

Os erros de endpoint são:

- **`4XX`:** `400`, `401`, `403`, `404`, `405`, `408`, `409`, `429`
- **`5XX`:** `500`, `502`, `503`, `504`, `598`, `599`

Esses e-mails são enviados apenas uma vez por dia no nível do espaço de trabalho. Se nenhum usuário se inscrever para receber esses e-mails, a Braze notifica todos os administradores da empresa.

Para se inscrever e receber esses e-mails, faça o seguinte:

1. Acesse **Configurações** > **Configurações de administrador** > **Preferências de notificação**.
2. Selecione **Connected Content Errors** e **Webhook Errors** na seção **Canvas & Campaigns**.

### Entradas no Registro de atividades de envio de mensagem {#message-activity-log-entries}

Se ocorrer uma falha, haverá pelo menos uma entrada no [Registro de atividades de envio de mensagem]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/message_activity_log) relacionada a ela. Se a solicitação for reenviada e eventualmente tiver sucesso, esses detalhes estarão disponíveis no Currents e no Compartilhamento de dados do Snowflake. Mesmo que uma solicitação eventualmente tenha sucesso após uma nova tentativa, os erros ainda podem acionar o e-mail automatizado.

### Insights adicionais de falhas no Braze Currents {#additional-failure-insights-in-braze-currents}

Para aumentar a transparência em relação a problemas relacionados a webhooks, a Braze transmite eventos detalhados de falha de webhook para o Currents e o Compartilhamento de dados do Snowflake. Esses eventos incluem solicitações de webhook com falha (como respostas HTTP `4xx` ou `5xx`), proporcionando mais observabilidade sobre como problemas de webhook podem impactar a entrega de mensagens. Os eventos de falha incluem erros terminais, bem como erros que estão sendo reenviados.

{% alert note %}
Solicitações de Conteúdo conectado não estão incluídas nesses eventos de falha de webhook.
{% endalert %}

Para saber mais, consulte o [Glossário de eventos de engajamento com mensagem]({{site.baseurl}}/user_guide/data/distribution/braze_currents/event_glossary/message_engagement_events).