---
nav_title: Snapchat
article_title: Sincronização de público do Canvas com o Snapchat
description: "Este artigo de referência aborda como usar o Braze Audience Sync com o Snapchat para entregar anúncios com base em disparadores comportamentais, segmentação e muito mais."
page_order: 6
alias: "/audience_sync_snapchat/"

tool:
  - Canvas

---

# Sincronização de público com o Snapchat {#audience-sync-to-snapchat}

Usando o Braze Audience Sync to Snapchat, as marcas podem adicionar dados de usuários de sua integração Braze às listas de clientes do Snapchat para entregar anúncios com base em disparadores comportamentais, segmentação e muito mais. Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS, webhook etc.) em um Canvas da Braze com base nos dados do seu usuário agora pode ser usado para disparar um anúncio para esse usuário em suas listas de clientes do Snapchat.

**Os casos de uso comuns para sincronização de público incluem:**

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md lookalike=true %}

Esse recurso permite que os usuários controlem quais dados primários específicos são compartilhados com o Snapchat. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

{% alert important %}
**Isenção de responsabilidade do Audience Sync Pro**<br>
O Braze Audience Sync com o Snapchat é uma integração do Audience Sync Pro. Para saber mais sobre essa integração, entre em contato com seu gerente de conta Braze.
{% endalert %}

## Pré-requisitos {#prerequisites}

Você deve garantir que os itens a seguir sejam criados, concluídos e/ou aceitos antes de configurar sua etapa de Audience Sync com Snapchat no Canvas.

| Requisito | Origin | Descrição |
| --- | --- | --- |
| Snapchat Business Manager | Snapchat | Uma ferramenta centralizada para gerenciar os ativos da sua marca no Snapchat (como contas de anúncios, páginas e apps). |
| Conta de anúncios do Snapchat | Snapchat | Uma conta de anúncios ativa do Snapchat vinculada ao Snapchat Business Manager da sua marca.<br><br>Certifique-se de que o administrador do seu Snapchat Business Manager concedeu a você permissões de administrador para as contas de anúncios do Snapchat que você planeja usar com a Braze. |
| Termos e políticas do Snapchat | [Snapchat](https://www.snap.com/en-US/policies) | Concorde em cumprir todos os termos, políticas, diretrizes e documentação exigidos pelo Snapchat relacionados ao seu uso do Snapchat Audience Sync, incluindo quaisquer termos, políticas, diretrizes e documentação incorporados por referência, que podem incluir: os Termos de Serviço, Termos de Serviço Comerciais, Termos para Desenvolvedores, Audience Match, Políticas de Publicidade, Política de Conteúdo Comercial, Diretrizes da Comunidade e Responsabilidade do Fornecedor. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Conectar ao Snapchat {#step-1-connect-to-snapchat}

{% alert important %}
Você precisa ter a [permissão "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar o Snapchat à sua conta da Braze.
{% endalert %}

No dashboard da Braze, acesse **Integrações com Parceiros** > **Parceiros de Tecnologia** e selecione **Snapchat**. Em Snapchat Audience Sync, selecione **Conectar Snapchat**.

![Página de tecnologia do Snapchat na Braze que inclui uma seção de visão geral e uma seção de Snapchat Audience Sync com o botão Conectar Snapchat.]({% image_buster /assets/img/snapchat/snapchat1.png %}){: style="max-width:80%;"}

Você será redirecionado para a página OAuth do Snapchat para autorizar a Braze a obter as permissões relacionadas à sua integração de Audience Sync.

Depois de confirmar, você será redirecionado de volta para a Braze para selecionar quais contas de anúncios do Snapchat deseja sincronizar.

![Uma lista de contas de anúncios disponíveis que você pode conectar ao Snapchat.]({% image_buster /assets/img/snapchat/snapchat2.png %}){: style="max-width:80%;"}

Após a conexão ser realizada com sucesso, você retornará à página de parceiros, onde poderá visualizar quais contas estão conectadas e desconectar contas existentes.

![Uma versão atualizada da página de parceiros de tecnologia do Snapchat mostrando as contas de anúncios conectadas com sucesso.]({% image_buster /assets/img/snapchat/snapchat3.png %}){: style="max-width:80%;"}

Sua conexão com o Snapchat será aplicada no nível do espaço de trabalho da Braze. Se o administrador do Snapchat remover você do Snapchat Business Manager ou do acesso às contas de anúncios conectadas do Snapchat, a Braze detectará um token inválido. Como resultado, seus Canvas ativos que usam o Snapchat exibirão erros, e a Braze não conseguirá sincronizar os usuários.

### Etapa 2: Adicionar uma etapa de Audience Sync com o Snapchat {#step-2-add-an-audience-sync-step-with-snapchat}

Adicione um componente ao seu Canvas e selecione **Audience Sync**.

![Seletor de etapas do Canvas com a opção do componente Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Cartão do componente Audience Sync adicionado a uma jornada do Canvas.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Etapa 3: Configuração da sincronização {#step-3-sync-setup}

Clique no botão **Custom Audience** para abrir o editor do componente.

Selecione **Snapchat** como o parceiro de Audience Sync desejado.

![Editor do componente Audience Sync com o Snapchat selecionado como parceiro de sincronização.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Em seguida, selecione a conta de anúncios do Snapchat desejada. No menu suspenso **Choose a New or Existing Audience**, digite o nome de um público novo ou existente.

{% tabs %}
{% tab Criar um novo público %}

**Criar um novo público**<br>
Insira um nome para o novo público, selecione **Add Users to Audience** e escolha quais campos você deseja sincronizar com o Snapchat. Em seguida, salve seu público clicando no botão **Create Audience** na parte inferior do editor de etapas.

![Visualização expandida da etapa Custom Audience do Canvas. Aqui, a conta de anúncios desejada está selecionada e um novo público é criado.]({% image_buster /assets/img/audience_sync/snapchat3.png %})

A Braze exibe uma notificação na parte superior do editor de etapas se o público for criado com sucesso ou se ocorrerem erros. Os usuários podem referenciar esse público para remoção de usuários posteriormente na jornada do Canvas, pois o público foi criado em modo de rascunho.

![Um alerta que aparece após a criação de um novo público no componente do Canvas.]({% image_buster /assets/img/audience_sync/snapchat2.png %})

Quando você lança um Canvas com um novo público, a Braze sincroniza os usuários em tempo quase real à medida que eles entram no componente Audience Sync.

{% endtab %}
{% tab Sincronizar com um público existente %}
**Sincronizar com um público existente**<br>
A Braze também oferece a possibilidade de adicionar usuários a públicos existentes do Snapchat para garantir que esses públicos estejam atualizados. Para sincronizar com um público existente, digite o nome do público existente no menu suspenso e selecione **Add to the Audience**. A Braze adicionará os usuários em tempo quase real à medida que eles entrarem no componente Audience Sync.

![Visualização expandida da etapa Custom Audience do Canvas. Aqui, a conta de anúncios desejada e o público existente estão selecionados.]({% image_buster /assets/img/audience_sync/snapchat.png %})

{% endtab %}
{% endtabs %}

### Etapa 4: Lançar o Canvas {#step-4-launch-canvas}

Após configurar seu Audience Sync com o Snapchat, lance o Canvas! Um novo público será criado, e os usuários que passarem pela etapa de Audience Sync serão adicionados a esse público no Snapchat. Se o seu Canvas contiver componentes subsequentes, os usuários avançarão para a próxima etapa da jornada.

Você pode visualizar o público no Snapchat acessando sua conta do gerenciador de anúncios e selecionando **Audiences** na seção Assets da navegação. Na página **Audiences**, você pode ver o tamanho de cada público depois que ele atingir aproximadamente 1.000.

![Detalhes do público para um determinado público do Snapchat, incluindo nome do público, tipo de público, tamanho do público e retenção do público em dias.]({% image_buster /assets/img/snapchat/snapchat7.png %})

## Sincronização de usuários e considerações sobre limite de frequência {#user-syncing-and-rate-limit-considerations}

Quando os usuários chegam à etapa de Audience Sync, a Braze os sincroniza em tempo quase real, respeitando os limites de frequência da API or interface de programação do aplicativo (API) do Snapchat. A Braze agrupa e processa o maior número possível de usuários a cada 5 segundos antes de enviá-los ao Snapchat.

O limite de frequência da API or interface de programação do aplicativo (API) do Snapchat permite no máximo dez consultas por segundo e 100.000 usuários por solicitação. Se um cliente atingir esse limite, a Braze tenta novamente a sincronização por até ~13 horas. Se a sincronização ainda não for possível, a Braze lista esses usuários na métrica Users Errored.

### Entendendo a análise de dados {#understanding-analytics}

A tabela a seguir inclui métricas e descrições para ajudar você a entender melhor a análise de dados do seu componente de Audience Sync.

| Métrica | Descrição |
| --- | --- |
| Entered | Número de usuários que entraram neste componente para serem sincronizados com o Snapchat. |
| Proceeded to Next Step | Quantos usuários avançaram para o próximo componente, se houver um? Todos os usuários avançam automaticamente se esta for a última etapa na Branch or ramificação or ramificação do Canvas. |
| Users Synced | Número de usuários que foram sincronizados com sucesso com o Snapchat. |
| Users Not Synced | Número de usuários que não foram sincronizados devido à falta de campos para correspondência. |
| Users Pending | Número de usuários que estão sendo processados pela Braze para sincronização com o Snapchat. |
| Users Errored | Número de usuários que não foram sincronizados com o Snapchat devido a um erro de API or interface de programação do aplicativo (API) após cerca de 13 horas de tentativas. Possíveis causas de erros podem incluir um token inválido do Snapchat ou se o público foi excluído no Snapchat. |
| Exited Canvas | Número de usuários que saíram do Canvas. Isso ocorre quando a última etapa em um Canvas é um componente de Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Entendendo a análise de dados" }

{% alert important %}
Lembre-se de que haverá um atraso no relatório de usuários sincronizados e métricas de erro devido ao envio em massa e à tentativa de 13 horas, respectivamente.
{% endalert %}

## Perguntas frequentes {#frequently-asked-questions}

### Quantos públicos o Snapchat suporta? {#how-many-audiences-can-snapchat-support}

No momento, você pode ter apenas 1.000 públicos na sua conta do Snapchat.

Se você exceder esse limite, a Braze notificará que não é possível criar novos públicos. Você precisará remover os públicos que não está mais usando na sua conta de anúncios do Snapchat.

### Como sei se os usuários foram correspondidos após enviá-los ao Snapchat? {#how-do-i-know-if-users-have-matched-after-passing-users-to-snapchat}

O Snapchat não fornece essa informação devido às suas políticas de privacidade de dados.

### O que devo fazer se receber um erro de token inválido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Você pode desconectar e reconectar sua conta do Snapchat na página de parceiro do Snapchat. Confirme com o administrador do seu Snapchat Business Manager que você tem as permissões apropriadas para a conta de anúncios com a qual deseja sincronizar.

### Por que meu Canvas não pode ser lançado? {#why-is-my-canvas-not-allowed-to-launch}

Verifique se sua conta de anúncios do Snapchat está conectada com sucesso à Braze na página de parceiro do Snapchat. Confirme que você selecionou uma conta de anúncios, inseriu um nome para o novo público e selecionou os campos para correspondência.