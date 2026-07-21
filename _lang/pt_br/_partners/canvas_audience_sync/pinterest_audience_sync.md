---
nav_title: Pinterest
article_title: Sincronização de público do Canvas com o Pinterest
description: "Este artigo de referência aborda como usar o Braze Audience Sync com o Pinterest para entregar anúncios com base em disparadores comportamentais, segmentação e muito mais."
page_order: 5
alias: "/audience_sync_pinterest/"

tool:
  - Canvas

---

# Sincronização de público com o Pinterest {#audience-sync-to-pinterest}

Usando o Braze Audience Sync com o Pinterest, as marcas podem optar por adicionar dados de usuários da sua própria integração da Braze ao Pinterest Audiences para entregar anúncios com base em disparadores comportamentais, segmentação e muito mais. Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS, webhook etc.) em um Braze Canvas com base nos dados de seus usuários agora pode ser usado para disparar um anúncio para esse usuário em seus públicos do Pinterest.

**Os casos de uso comuns para sincronização de público incluem:**

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md %}

Este recurso permite que as marcas controlem quais dados primários específicos são compartilhados com o Pinterest. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

{% alert important %}
**Isenção de responsabilidade do Audience Sync Pro**<br>
O Braze Audience Sync com o Pinterest é uma integração do Audience Sync Pro. Para saber mais sobre essa integração, entre em contato com seu gerente de conta Braze.
{% endalert %}

## Pré-requisitos {#prerequisites}
É necessário garantir que os itens a seguir sejam criados, concluídos e/ou aceitos antes de configurar a etapa do público do Pinterest no Canvas.

| Requisito | Origem | Descrição |
| --- | --- | --- |
| Pinterest Business Hub | [Pinterest](https://www.pinterest.com/business/hub/) | Uma ferramenta centralizada para gerenciar os ativos do Pinterest da sua marca (como contas de anúncios, páginas, apps). |
| Conta de anúncios do Pinterest | [Pinterest](https://ads.pinterest.com/) | Uma conta ativa de anúncios do Pinterest vinculada ao Pinterest Business Hub da sua marca.<br><br>Certifique-se de que o administrador do Pinterest Business Hub lhe concedeu permissões de administrador para as contas de anúncios do Pinterest que você planeja usar com a Braze. |
| Termos e políticas do Pinterest | Pinterest | Concordar em cumprir todos os termos, políticas, diretrizes e documentação exigidos pelo Pinterest relacionados ao seu uso do Pinterest Audience Sync, incluindo quaisquer termos, políticas, diretrizes e documentação incorporados por referência, que podem incluir: os Termos de Serviço, os Termos de Serviço para Empresas, a Política de Privacidade, os Termos de Serviço para Desenvolvedores e API, os Termos de Dados de Anúncios, as Diretrizes de Publicidade, o Contrato de Serviços de Publicidade, as Diretrizes da Comunidade e as Diretrizes da Marca. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Conectar-se ao Pinterest {#step-1-connect-to-pinterest}

{% alert important %}
Você deve ter a [permissão "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar o Pinterest à sua conta Braze.
{% endalert %}

No dashboard da Braze, acesse **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Pinterest**. Em Pinterest Audience Sync, selecione **Connect Pinterest**.

![Página de tecnologia do Pinterest na Braze que inclui uma seção de Visão geral e uma seção de Pinterest Audience Sync com o botão Connect Pinterest.]({% image_buster /assets/img/pinterest/pinterest1.png %}){: style="max-width:80%;"}

Em seguida, você será redirecionado para a página de OAuth do Pinterest para autorizar a Braze a executar o gerenciamento de contas de anúncios e o gerenciamento de público.

Depois de selecionar **Confirm**, você será redirecionado de volta à Braze para selecionar quais contas de anúncios do Pinterest deseja sincronizar.

![Uma lista de contas de anúncios disponíveis que você pode conectar ao Pinterest.]({% image_buster /assets/img/pinterest/pinterest2.png %}){: style="max-width:80%;"}

Quando a conexão for bem-sucedida, você retornará à página do parceiro, onde poderá ver quais contas estão conectadas e desconectar contas existentes.

![Uma versão atualizada da página de parceiros de tecnologia do Pinterest mostrando as contas de anúncios conectadas com sucesso.]({% image_buster /assets/img/pinterest/pinterest3.png %}){: style="max-width:80%;"}

Sua conexão com o Pinterest será aplicada no nível do espaço de trabalho da Braze. Se o administrador do Pinterest remover você do seu Pinterest Business Hub ou do acesso às contas do Pinterest conectadas, a Braze detectará um token inválido. Como resultado, seus Canvas ativos que usam componentes de público do Pinterest mostrarão erros, e a Braze não conseguirá sincronizar os usuários.

### Etapa 2: Adicionar uma etapa de sincronização de público com o Pinterest {#step-2-add-an-audience-sync-step-with-pinterest}

Adicione um componente ao seu Canvas e selecione **Audience Sync**.

![Seletor de etapas do Canvas com a opção do componente Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Cartão do componente Audience Sync adicionado a uma jornada do Canvas.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Etapa 3: Configuração de sincronização {#step-3-sync-setup}

Clique no botão **Custom Audience** para abrir o editor de componentes.

Selecione **Pinterest** como parceiro desejado do Audience Sync.

![Editor do componente Audience Sync com o Pinterest selecionado como parceiro de sincronização.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Em seguida, selecione sua conta de anúncios do Pinterest desejada. No menu suspenso **Choose a New or Existing Audience**, digite o nome de um público novo ou existente.

{% tabs %}
{% tab Criar um novo público %}

**Criar um novo público**<br>
Digite um nome para o novo público, selecione **Add Users to Audience** e selecione os campos que deseja sincronizar com o Pinterest. Em seguida, salve seu público clicando no botão **Create Audience** na parte inferior do editor de etapas.

![Visualização expandida da etapa do Canvas de público personalizado. Aqui, a conta de anúncios desejada é selecionada e um novo público é criado.]({% image_buster /assets/img/audience_sync/pinterest_sync.png %})

A Braze exibe uma notificação na parte superior do editor de etapas se o público for criado com êxito ou se ocorrerem erros. Os usuários podem referenciar este público para remoção de usuários mais tarde na jornada do Canvas porque o público foi criado no modo de rascunho.

![Um alerta que aparece depois que um novo público é criado no componente Canvas.]({% image_buster /assets/img/audience_sync/pinterest_sync3.png %})

Ao lançar um Canvas com um novo público, a Braze sincroniza os usuários quase em tempo real quando eles entram na etapa do Audience Sync.
{% endtab %}
{% tab Sincronizar com um público existente %}
**Sincronizar com um público existente**<br>
A Braze também oferece a capacidade de adicionar usuários a públicos existentes no Pinterest para garantir que esses públicos estejam atualizados. Para sincronizar com um público existente, digite o nome do público existente no menu suspenso e adicione-o ao público. A Braze adicionará usuários quase em tempo real quando eles entrarem na etapa do Audience Sync.

![Visualização expandida da etapa do Canvas de público personalizado. Aqui, a conta de anúncios desejada e o público existente são selecionados.]({% image_buster /assets/img/audience_sync/pinterest_sync2.png %})

{% endtab %}
{% endtabs %}

### Etapa 4: Lançar o Canvas {#step-4-launch-canvas}

Depois de configurar a sincronização do público com o Pinterest, lance o Canvas! O novo público será criado, e os usuários que passarem pela etapa do Audience Sync serão transferidos para esse público no Pinterest. Se o seu Canvas contiver componentes subsequentes, seus usuários avançarão para a próxima etapa da jornada do usuário.

Você pode visualizar o público no Pinterest entrando em sua conta do gerenciador de anúncios e selecionando Audiences no menu suspenso Ads. Na página Audience, você pode ver o tamanho de cada público depois que ele atinge ~100.

![Detalhes de um determinado público do Pinterest, incluindo nome, ID, tipo e tamanho do público.]({% image_buster /assets/img/pinterest/pinterest11.png %})

## Considerações sobre sincronização de usuários e limite de frequência {#user-syncing-and-rate-limit-considerations}

Quando os usuários atingem a etapa de sincronização do público, a Braze os sincroniza quase em tempo real, respeitando os limites de frequência da API de marketing do Pinterest. A Braze agrupa e processa o maior número possível de usuários a cada 5 segundos antes de enviá-los ao Pinterest.

O limite de frequência da API de segmentos do Pinterest não permite mais do que sete consultas por segundo por usuário e 1.900 usuários por solicitação. Se um cliente atingir esse limite, a Braze tentará novamente a sincronização por até ~13 horas. Se a sincronização ainda não for possível, a Braze listará esses usuários na métrica Usuários com erro.

## Compreensão da análise de dados {#understanding-analytics}

A tabela a seguir inclui métricas e descrições para ajudá-lo a entender melhor a análise de dados do seu componente Audience Sync.

| Métrica | Descrição |
| --- | --- |
| Entraram | Número de usuários que entraram nesse componente para serem sincronizados com o Pinterest. |
| Avançaram para a etapa seguinte | Quantos usuários avançaram para o próximo componente, se houver um? Todos os usuários avançarão automaticamente se essa for a última etapa da ramificação do Canvas. |
| Usuários sincronizados | Número de usuários que foram sincronizados com sucesso com o Pinterest. |
| Usuários não sincronizados | Número de usuários que não foram sincronizados devido à falta de campos para correspondência. |
| Usuários pendentes | Número de usuários que estão sendo processados pela Braze para sincronização com o Pinterest. |
| Usuários com erro | Número de usuários que não foram sincronizados com o Pinterest devido a um erro de API após cerca de 13 horas de tentativas. As possíveis causas de erros podem incluir um token inválido do Pinterest ou a exclusão do público no Pinterest. |
| Saíram do Canvas | Número de usuários que saíram do Canvas. Isso ocorre quando a última etapa de um Canvas é um componente de Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Compreensão da análise de dados" }

{% alert important %}
Lembre-se de que haverá um atraso nos relatórios de usuários sincronizados e métricas com erro devido ao envio em massa e à nova tentativa de 13 horas, respectivamente.
{% endalert %}

## Perguntas frequentes {#frequently-asked-questions}

### Quanto tempo levará para que meus públicos sejam preenchidos no Pinterest? {#how-long-will-it-take-for-my-audiences-to-populate-in-pinterest}

O tamanho do público será atualizado dentro de 24 a 48 horas na página **Audiences** no gerenciador de anúncios do Pinterest.

### Como posso saber se os usuários corresponderam depois de passá-los para o Pinterest? {#how-do-i-know-if-users-have-matched-after-passing-users-to-pinterest}

O Pinterest não fornece essas informações devido às suas próprias políticas de privacidade de dados.

### O que devo fazer se receber um erro de token inválido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Confirme com o administrador do Pinterest Business Hub que você tem as permissões apropriadas para a conta de anúncios que deseja sincronizar. Você também pode desconectar e reconectar sua conta do Pinterest na página de parceiros do Pinterest.

### Por que meu Canvas não pode ser lançado? {#why-is-my-canvas-not-allowed-to-launch}

Certifique-se de que sua conta do Pinterest se conecte com sucesso à Braze na página de parceiros do Pinterest. Certifique-se de ter selecionado uma conta de anúncios, inserido um nome para o novo público e selecionado os campos para correspondência.

### Por que não consigo selecionar minha conta de anúncios para a etapa Audience Sync? {#why-cant-i-select-my-ad-account-for-my-audience-sync-step}

Verifique se o token foi gerado com as permissões de conta corretas. Observe que, se houver muitos públicos em sua conta de anúncios do Pinterest, o menu suspenso para selecionar sua conta de anúncios poderá expirar. Nesse caso, recomendamos reduzir o número de públicos em sua conta de anúncios.