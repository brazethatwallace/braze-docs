---
nav_title: Registro de usuários de eventos
article_title: Registro de usuários de eventos
page_order: 1
page_type: reference
description: "Este artigo de referência aborda o Registro de usuários de eventos, que pode ajudar você a depurar ou solucionar problemas na sua integração com a Braze."

---

# Registro de usuários de eventos

> O Registro de usuários de eventos pode ajudar você a detalhar, depurar ou solucionar problemas na sua integração com a Braze. Essa guia fornece um registro de erros que detalha o tipo de erro, a qual app ele está associado, quando aconteceu e, frequentemente, a oportunidade de visualizar os dados brutos associados.

{% alert tip %}
Além deste artigo, também recomendamos conferir nosso [curso do Braze Learning sobre ferramentas de garantia de qualidade e debug](https://learning.braze.com/quality-assurance-and-debugging-tools-in-the-dashboard/), que aborda como usar o Registro de usuários de eventos para conduzir sua própria solução de problemas e depuração.
{% endalert %}

Para acessar o registro, acesse **Configurações** > **Registro de usuários de eventos**.

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

## Solução de problemas

### Registros de SDK ausentes para usuários teste

Se você adicionou um usuário a um grupo interno, mas ele não está exibindo nenhum registro de SDK no Registro de usuários de eventos, isso pode ser resultado de uma opção de configuração ausente. Para capturar registros de SDK, certifique-se de selecionar **Registrar eventos de usuário para membros do grupo** nas **Configurações do grupo interno** daquele [grupo interno]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/).

### Postergação nas atualizações de registros

Isso é potencialmente uma lentidão normal por parte da nossa API.

Quando você chama métodos do SDK, geralmente o SDK armazena esses eventos localmente em cache e os envia ao servidor a cada 10 segundos. Pode levar de um segundo a alguns minutos para que nossa fila de processamento de tarefas ingira os eventos, dependendo da carga geral no momento.

Se você deseja que os eventos cheguem o mais rápido possível, tente chamar a função `requestImmediateDataFlush()`.

### Falhas de impressão de mensagens no app

Se uma mensagem no app não for exibida, você pode encontrar o motivo no Registro de usuários de eventos expandindo os dados JSON brutos da solicitação de SDK relevante e procurando o campo `error_code` na resposta. O `error_code` identifica o motivo específico pelo qual a impressão falhou (por exemplo, um valor de cor inválido ou um problema de renderização). Compartilhe esse código de erro com o [suporte da Braze]({{site.baseurl}}/braze_support/) se uma investigação mais aprofundada for necessária.

### Fim de sessão e início de sessão com timestamps semelhantes (iOS)

O Registro de usuários de eventos mostra o timestamp de quando a Braze foi notificada de que a sessão terminou, que será milissegundos antes do início da próxima sessão. A Braze não consegue saber que a sessão terminou antes que o app seja reaberto, porque o iOS é agressivo ao interromper a execução de threads quando o app está em segundo plano — portanto, nenhum dado pode ser enviado para a Braze até que o app seja reaberto.

Embora o horário de fim de sessão seja especificado como segundos antes do início da sessão, quando o evento é enviado, a Duração da Sessão é enviada separadamente e está correta — refletindo o tempo em que o app esteve aberto. Portanto, esse comportamento não impacta o filtro `Median Session Duration`.

Em relação às sessões de usuário, você pode usar a Braze para monitorar dados como:

- Quantas sessões um usuário teve
- Quando um usuário iniciou uma sessão pela última vez
- Se o usuário inicia uma sessão após receber uma Campaign
- Qual é a duração mediana de sessão do usuário

Esses comportamentos não são impactados pelo evento de fim de sessão ser enviado na próxima sessão.