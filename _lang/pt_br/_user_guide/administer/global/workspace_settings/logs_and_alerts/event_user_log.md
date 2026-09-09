---
nav_title: Registro de usuários de eventos
article_title: Registro de usuários de eventos
page_order: 1
page_type: reference
description: "Este artigo de referência aborda o registro de usuários de eventos, que pode ajudar você a depurar ou solucionar problemas na sua integração com a Braze."

---

# Registro de usuários de eventos {#event-user-log}

> O registro de usuários de eventos pode ajudar você a detalhar, depurar ou solucionar problemas na sua integração com a Braze. Essa guia fornece um registro de erros que detalha o tipo de erro, a qual app ele está associado, quando aconteceu e, frequentemente, a oportunidade de visualizar os dados brutos associados.

{% alert tip %}
Além deste artigo, também recomendamos conferir nosso [curso do Braze Learning sobre ferramentas de garantia de qualidade e depuração](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), que aborda como usar o registro de usuários de eventos para conduzir sua própria solução de problemas e depuração.
{% endalert %}

Para acessar o registro, acesse **Configurações** > **Configuração e testes** > **Registro de usuários de eventos**.

Para encontrar seus registros facilmente, você pode filtrar com base em:

* SDK ou API
* Nomes de apps
* Período
* Usuário

Cada registro é dividido em várias seções, que podem incluir:

* Atributos do dispositivo
* Atributos do usuário
* Eventos
* Eventos de Campaign
* Dados de resposta

Selecione o ícone **Expandir dados** para exibir os dados JSON brutos daquele registro específico.

![O ícone "Expandir dados" ao lado de um registro específico.]({% image_buster /assets/img_archive/expand_data.png %})

Os registros de usuários de eventos permanecerão no dashboard por 30 dias após serem registrados.

![Registros brutos de eventos]({% image_buster /assets/img_archive/rawlogs.png %}){: style="max-width:60%;"}

## Solução de problemas {#troubleshooting}

### Registros do SDK ausentes para usuários teste {#missing-sdk-logs-for-test-users}

Se você adicionou um usuário a um grupo interno, mas ele não está exibindo nenhum registro do SDK no registro de usuários de eventos, isso pode ser resultado de uma opção de configuração ausente. Para capturar registros do SDK, selecione **Record User Events for group members** em **Internal Group Settings** para esse [grupo interno]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups).

### Atraso na atualização dos registros {#delay-in-logs-updates}

Esse atraso geralmente é causado pela carga normal de processamento da API.

Quando você chama métodos do SDK, geralmente o SDK armazena esses eventos em cache localmente e os envia ao servidor a cada 10 segundos. Pode levar de um segundo a alguns minutos para que nossa fila de processamento de tarefas processe os eventos, dependendo da carga geral no momento.

Se você deseja que os eventos cheguem o mais rápido possível, tente chamar a função `requestImmediateDataFlush()`.

### Falhas de impressão de mensagens no app {#in-app-message-impression-failures}

Se uma mensagem no app não for exibida, você pode encontrar o motivo no registro de usuários de eventos expandindo os dados JSON brutos da solicitação relevante do SDK e procurando o campo `error_code` na resposta. O `error_code` identifica o motivo específico pelo qual a impressão falhou (por exemplo, um valor de cor inválido ou um problema de renderização). Compartilhe esse código de erro com o [suporte da Braze]({{site.baseurl}}/user_guide/administer/personal/braze_support) se uma investigação mais detalhada for necessária.

### Fim de sessão e início de sessão com timestamps semelhantes (iOS) {#session-end-and-session-start-have-similar-timestamps-ios}

O registro de usuários de eventos mostra o timestamp de quando a Braze foi notificada de que a sessão terminou, o que ocorre milissegundos antes do início da próxima sessão. A Braze não consegue saber que a sessão terminou antes de o app ser reaberto, porque o iOS é agressivo ao interromper a execução de threads quando o app está em segundo plano — então nenhum dado pode ser enviado à Braze até que o app seja reaberto.

Embora o horário de fim de sessão apareça como segundos antes do início da sessão, quando o evento é enviado, a duração da sessão é enviada separadamente e está correta — refletindo o tempo em que o app esteve aberto. Portanto, esse comportamento não impacta o filtro `Median Session Duration`.

Em relação às sessões de usuários, você pode usar a Braze para monitorar dados como:

- Quantas sessões um usuário teve
- Quando um usuário iniciou uma sessão pela última vez
- Se o usuário inicia uma sessão após receber uma Campaign
- Qual é a duração mediana de sessão do usuário

Esses comportamentos não são impactados pelo evento de fim de sessão ser enviado na sessão seguinte.