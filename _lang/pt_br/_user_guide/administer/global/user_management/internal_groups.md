---
nav_title: Grupos internos
article_title: Grupos internos
page_order: 4
page_type: reference
description: "Este artigo de referência descreve os grupos internos, uma ótima maneira de obter insights sobre os registros do SDK ou da API do seu dispositivo de teste ao testar a integração de SDK."

---

# Grupos internos {#internal-groups}

> Grupos internos são uma ótima maneira de criar e organizar grupos de teste internos ou de terceiros. Eles fornecem insights sobre os registros do SDK ou da API e são úteis ao testar a integração de SDK. Você pode criar um número ilimitado de grupos internos personalizados com até 1.000 usuários.

{% alert tip %}
Também recomendamos conferir nosso curso do Braze Learning [Testes e solução de problemas](https://learning.braze.com/path/developer/testing-and-troubleshooting), que aborda como usar grupos internos para conduzir sua própria solução de problemas e depuração.
{% endalert %}

## Pré-requisitos {#prerequisites}

Para criar e gerenciar grupos internos, você precisa das seguintes [permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/):

- Visualizar chaves de API
- Editar chaves de API
- Visualizar grupos internos
- Editar grupos internos
- Visualizar registro de atividades de envio de mensagem
- Visualizar registro de usuários de eventos
- Visualizar identificadores de API
- Visualizar dashboard de uso da API
- Visualizar limites da API
- Visualizar alertas de uso da API
- Editar alertas de uso da API
- Editar Depurador do SDK
- Visualizar Depurador do SDK

## Criando um grupo interno {#creating-an-internal-group}

Para criar um grupo interno:

1. Acesse **Configurações** > **Grupos internos**.
2. Selecione **Criar grupo interno**.
3. Dê um nome ao seu grupo, como "Grupo de teste de e-mail".
4. Escolha um ou mais tipos de grupo, conforme listado na tabela a seguir.

| Tipo de grupo | Descrição |
|---|---|
| **Grupo de eventos de usuário** | Use para verificar eventos ou registros do seu dispositivo de teste. |
| **Grupo de teste de conteúdo** | Use em push, e-mail e mensagens no app para enviar uma cópia renderizada da mensagem. |
| **Grupo de teste** | Envia automaticamente uma cópia do e-mail para todos no grupo de teste no momento do envio. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Criando um grupo interno" }

{:start="5"}

5. Selecione **Criar grupo interno** novamente.

### Adicionando usuários teste {#adding-test-users}

Depois de criar seu grupo interno, adicione usuários teste como membros desse grupo.

1. Na página de gerenciamento do seu grupo interno, selecione **Adicionar usuários teste**.
2. Escolha entre os seguintes métodos para pesquisar e selecionar seus usuários teste.

| Método | Descrição |
|---|---|
| **Adicionar usuário identificado** | Pesquise o usuário pelo ID externo, endereço de e-mail, número de telefone ou token por push. |
| **Adicionar usuário anônimo** | Pesquise por endereço IP. Em seguida, forneça um nome para cada usuário teste adicionado. Esse é o nome ao qual todos os registros de eventos são associados na página [Registro de usuários de eventos]({{site.baseurl}}/user_guide/administer/global/workspace_settings/logs_and_alerts/event_user_log/). |
| **Adicionar usuários em massa** | Copie e cole uma lista de endereços de e-mail ou IDs externos. Você só pode adicionar usuários que já são conhecidos no dashboard. Para saber mais, consulte [Importação de usuários]({{site.baseurl}}/user_guide/audience/manage_audience/import_users/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Adicionando usuários teste" }

![Configurações de grupo interno ao criar um novo grupo interno]({% image_buster /assets/img_archive/internal_group_add_user.png %})

### Grupos de teste de conteúdo {#content-test-groups}

Semelhante ao envio de uma pré-visualização de teste de uma mensagem, o grupo de teste de conteúdo economiza tempo e permite que você lance testes para uma lista predefinida de usuários da Braze simultaneamente. Isso está disponível para push, mensagens no app, SMS, e-mail e Content Cards na Braze. Somente grupos marcados como grupos de teste de conteúdo ficam disponíveis na seção de pré-visualização de uma mensagem.

{% alert note %}
Mensagens de teste de [SMS]({{site.baseurl}}/user_guide/channels/sms_mms_and_rcs/) só podem ser enviadas para números de telefone válidos no banco de dados.
{% endalert %}

Selecione usuários individuais da Braze ou qualquer número de grupos internos para enviar a mensagem. Se sua mensagem incluir Liquid ou outra personalização dinâmica, a Braze usa os atributos disponíveis para cada usuário para personalizar o conteúdo da mensagem. Para usuários que não possuem atributos, a Braze usa o valor padrão definido.

Além disso, se você pré-visualizar a mensagem como um usuário aleatório, um usuário personalizado ou um usuário existente, poderá enviar essa versão pré-visualizada. Desmarcar a caixa de seleção permite enviar com base nos atributos de cada usuário em vez da versão pré-visualizada.

Se você usar um pool de IP para enviar um e-mail, selecione de qual pool de IP enviar o e-mail escolhendo o pool no menu suspenso disponível.

![A seção de teste do editor de mensagens no app para selecionar o grupo de teste de conteúdo.]({% image_buster /assets/img_archive/content_test_preview.png %}){: style="max-width:60%" }

### Grupos de teste {#seed-groups}

Os grupos de teste são compatíveis apenas com o canal de e-mail. Adicione usuários a um grupo de teste para enviar cópias de cada variante de mensagem de e-mail para todos os membros do grupo.

Os grupos de teste não estão disponíveis para Campaigns da API, mas você pode incluir grupos de teste usando uma entrada disparada por API na Campaign. Use isso para medir métricas de entregabilidade e manter um registro do conteúdo do seu e-mail para fins históricos e de arquivamento.

Depois de criar um grupo interno e marcá-lo para ser usado como grupo de teste, selecione-o na etapa **Público-alvo** do editor de Campaign ou na etapa **Configurações de envio** em um Canvas.

E-mails de teste têm `[SEED]` adicionado antes da linha de assunto. Observe que e-mails de teste **não**:

- Incrementam os envios na análise de dados do dashboard.
- Impactam a análise de dados de e-mail ou o redirecionamento.
- Atualizam a lista de **Campaigns recebidas** do perfil de um usuário.
- Impactam o limite de frequência.
- Contabilizam ou impactam os limites de taxa de velocidade de entrega.

#### Comportamento de inscrição {#subscription-behavior}

Os envios de teste são projetados para QA e revisão internos, então eles intencionalmente ignoram as verificações de inscrição para os usuários da empresa incluídos no grupo de teste. Isso significa que usuários com endereços de e-mail válidos que fazem parte de um grupo de teste recebem a mensagem mesmo que não estejam inscritos. No entanto, a mensagem deve estar configurada para enviar cópias de teste para esse grupo.

{% alert tip %}
Se os membros do grupo de teste não estiverem vendo a mensagem, confirme que eles estão no grupo interno, use linhas de assunto distintas para que o Gmail não agrupe as mensagens e peça que verifiquem a pasta de spam.

Se o e-mail usar [Liquid `abort_message()`]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages/), os membros do grupo de teste ainda devem satisfazer a condição de cancelamento para receber o envio.
{% endalert %}

#### Para Campaigns {#for-campaigns}

Ao compor uma Campaign de e-mail, edite seus grupos de teste na seção **Público-alvo** do editor.

{% alert important %}
Se você configurar um grupo de teste para ser anexado automaticamente a todas as Campaigns, isso se aplica apenas a novas Campaigns. Não se aplica quando você copia Campaigns existentes. Você deve aplicar manualmente os grupos de teste desejados à Campaign copiada na seção **Público-alvo**.
{% endalert %}

Os grupos de teste enviam para cada variante de e-mail uma vez e são entregues na primeira vez que seu usuário recebe aquela variante específica. Para mensagens agendadas, isso normalmente é a primeira vez que a Campaign é lançada. Para Campaigns baseadas em ação ou disparadas por API, é o momento em que o primeiro usuário recebe uma mensagem.

Se sua Campaign for multivariante e sua variante tiver uma porcentagem de envio de 0%, ela não será enviada para os grupos de teste. Além disso, se a variante já tiver sido enviada e não tiver sido atualizada para reenvio em **Editar grupos de teste** na etapa **Alvo**, ela não será enviada novamente por padrão.

{% alert note %}
Se você tiver uma Campaign recorrente e qualquer uma das variantes for atualizada, poderá escolher enviar novamente apenas para as variantes atualizadas ou todas as variantes, ou desativar o envio do grupo de teste na atualização.
{% endalert %}

![O grupo de teste "Email seed test" selecionado para receber a Campaign de e-mail da Variante 1.]({% image_buster /assets/img_archive/seed_group_campaign.png %})

#### Para Canvas {#for-canvas}

Os grupos de teste no Canvas funcionam de forma semelhante a qualquer Campaign disparada. A Braze detecta automaticamente todas as etapas que contêm uma mensagem de e-mail e envia quando seu usuário alcança pela primeira vez aquela etapa de e-mail específica.

Se uma etapa de e-mail foi atualizada depois que o grupo de teste recebeu o envio, a Braze apresenta a opção de enviar apenas para as etapas atualizadas, todas as etapas ou desativar os envios de teste.