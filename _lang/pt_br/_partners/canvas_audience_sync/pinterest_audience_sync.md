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

Usando o Braze Audience Sync com o Pinterest, as marcas podem optar por adicionar dados de usuários da sua própria integração da Braze ao Pinterest Audiences para entregar anúncios com base em disparadores comportamentais, segmentação e muito mais. Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS, webhook etc.) em um BRAZE CANVAS com base nos dados de seus usuários agora pode ser usado para disparar um anúncio para esse usuário em seus públicos do Pinterest.

**Os casos de uso comuns para sincronização de público incluem:**

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md lookalike=true %}

Este recurso permite que as marcas controlem quais dados primários específicos são compartilhados com o Pinterest. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

{% alert important %}
**Isenção de responsabilidade do Audience Sync Pro**<br>
O Braze Audience Sync com o Pinterest é uma integração do Audience Sync Pro. Para saber mais sobre essa integração, entre em contato com seu gerente de conta Braze.
{% endalert %}

## Pré-requisitos {#prerequisites}
Você deve garantir que os itens a seguir sejam criados, concluídos e/ou aceitos antes de configurar sua etapa de Sincronização de Público do Pinterest no Canvas.

| Requisito | Origin | Descrição |
| --- | --- | --- |
| Pinterest Business Hub | [Pinterest](https://www.pinterest.com/business/hub/) | Uma ferramenta centralizada para gerenciar os ativos da sua marca no Pinterest (como contas de anúncios, páginas e apps). |
| Conta de anúncios do Pinterest | [Pinterest](https://ads.pinterest.com/) | Uma conta de anúncios ativa do Pinterest vinculada ao Pinterest Business Hub da sua marca.<br><br>Certifique-se de que o administrador do seu Pinterest Business Hub concedeu a você permissões de administrador para as contas de anúncios do Pinterest que você pretende usar com a Braze. |
| Termos e políticas do Pinterest | Pinterest | Concorde em cumprir todos os termos, políticas, diretrizes e documentação exigidos pelo Pinterest relacionados ao uso da Sincronização de Público do Pinterest, incluindo quaisquer termos, políticas, diretrizes e documentação incorporados por referência, que podem incluir: os Termos de Serviço, Termos de Serviço Comerciais, Política de Privacidade, Termos de Serviço para Desenvolvedores e API, Termos de Dados de Anúncios, Diretrizes de Publicidade, Contrato de Serviços de Publicidade, Diretrizes da Comunidade e Diretrizes da Marca. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Conectar ao Pinterest {#step-1-connect-to-pinterest}

{% alert important %}
Você precisa ter a [permissão "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar o Pinterest à sua conta da Braze.
{% endalert %}

No dashboard da Braze, acesse **Integrações com Parceiros** > **Parceiros de Tecnologia** e selecione **Pinterest**. Em Pinterest Audience Sync, selecione **Conectar Pinterest**.

![Página de tecnologia do Pinterest na Braze que inclui uma seção de Visão Geral e uma seção Pinterest Audience Sync com o botão Conectar Pinterest.]({% image_buster /assets/img/pinterest/pinterest1.png %}){: style="max-width:80%;"}

Você será redirecionado para a página OAuth do Pinterest para autorizar a Braze a gerenciar contas de anúncios e públicos.

Após selecionar **Confirmar**, você será redirecionado de volta para a Braze para selecionar quais contas de anúncios do Pinterest deseja sincronizar.

![Uma lista de contas de anúncios disponíveis que você pode conectar ao Pinterest.]({% image_buster /assets/img/pinterest/pinterest2.png %}){: style="max-width:80%;"}

Quando a conexão for bem-sucedida, você retornará à página de parceiros, onde poderá visualizar quais contas estão conectadas e desconectar contas existentes.

![Uma versão atualizada da página de parceiros de tecnologia do Pinterest mostrando as contas de anúncios conectadas com sucesso.]({% image_buster /assets/img/pinterest/pinterest3.png %}){: style="max-width:80%;"}

Sua conexão com o Pinterest será aplicada no nível do espaço de trabalho da Braze. Se o administrador do Pinterest remover você do Pinterest Business Hub ou o acesso às contas conectadas do Pinterest, a Braze detectará um token inválido. Como resultado, seus Canvas ativos que usam componentes de Pinterest Audience apresentarão erros, e a Braze não conseguirá sincronizar usuários.

### Etapa 2: Adicionar uma etapa de Audience Sync com o Pinterest {#step-2-add-an-audience-sync-step-with-pinterest}

Adicione um componente ao seu Canvas e selecione **Audience Sync**.

![Seletor de etapas do Canvas com a opção do componente Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Cartão do componente Audience Sync adicionado a uma jornada do Canvas.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Etapa 3: Configuração da sincronização {#step-3-sync-setup}

Clique no botão **Custom Audience** para abrir o editor do componente.

Selecione **Pinterest** como o parceiro de Audience Sync desejado.

![Editor do componente Audience Sync com o Pinterest selecionado como parceiro de sincronização.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Em seguida, selecione a conta de anúncios do Pinterest desejada. No menu suspenso **Choose a New or Existing Audience**, digite o nome de um público novo ou existente.

{% tabs %}
{% tab Criar um novo público %}

**Criar um novo público**<br>
Insira um nome para o novo público, selecione **Add Users to Audience** e escolha quais campos deseja sincronizar com o Pinterest. Em seguida, salve seu público clicando no botão **Create Audience** na parte inferior do editor de etapas.

![Visualização expandida da etapa Custom Audience do Canvas. Aqui, a conta de anúncios desejada está selecionada e um novo público é criado.]({% image_buster /assets/img/audience_sync/pinterest_sync.png %})

A Braze exibe uma notificação na parte superior do editor de etapas se o público for criado com sucesso ou se ocorrerem erros. Os usuários podem referenciar esse público para remoção de usuários posteriormente na jornada do Canvas, pois o público foi criado em modo de rascunho.

![Um alerta que aparece após a criação de um novo público no componente do Canvas.]({% image_buster /assets/img/audience_sync/pinterest_sync3.png %})

Quando você lança um Canvas com um novo público, a Braze sincroniza os usuários em tempo quase real à medida que eles entram na etapa de Audience Sync.
{% endtab %}
{% tab Sincronizar com um público existente %}
**Sincronizar com um público existente**<br>
A Braze também oferece a possibilidade de adicionar usuários a públicos existentes do Pinterest para garantir que esses públicos estejam atualizados. Para sincronizar com um público existente, digite o nome do público existente no menu suspenso e adicione-o ao público. A Braze adicionará os usuários em tempo quase real à medida que eles entrarem na etapa de Audience Sync.

![Visualização expandida da etapa Custom Audience do Canvas. Aqui, a conta de anúncios desejada e o público existente estão selecionados.]({% image_buster /assets/img/audience_sync/pinterest_sync2.png %})

{% endtab %}
{% endtabs %}

### Etapa 4: Lançar o Canvas {#step-4-launch-canvas}

Após configurar seu Audience Sync com o Pinterest, lance o Canvas! O novo público é criado, e os usuários que passam pela etapa de Audience Sync são adicionados a esse público no Pinterest. Se o seu Canvas contiver componentes subsequentes, seus usuários avançarão para a próxima etapa em sua jornada de usuário.

Você pode visualizar o público no Pinterest acessando sua conta do gerenciador de anúncios e selecionando Audiences no menu suspenso Ads. Na página de Audience, você pode ver o tamanho de cada público após ele atingir aproximadamente 100.

![Detalhes do público para um determinado público do Pinterest que inclui nome do público, ID do público, tipo de público e tamanho do público.]({% image_buster /assets/img/pinterest/pinterest11.png %})

## Sincronização de usuários e considerações sobre limite de frequência {#user-syncing-and-rate-limit-considerations}

À medida que os usuários chegam à etapa de Audience Sync, a Braze os sincroniza em tempo quase real, respeitando os limites de frequência da API de marketing do Pinterest. A Braze agrupa e processa o maior número possível de usuários a cada 5 segundos antes de enviá-los ao Pinterest.

O limite de frequência da API de Segment do Pinterest permite no máximo sete consultas por segundo por usuário e 1.900 usuários por solicitação. Se um cliente atingir esse limite, a Braze tentará novamente a sincronização por aproximadamente 13 horas. Se a sincronização ainda não for possível, a Braze listará esses usuários na métrica Users Errored.

## Entendendo a análise de dados {#understanding-analytics}

A tabela a seguir inclui métricas e descrições para ajudar você a entender melhor a análise de dados do seu componente de Audience Sync.

| Métrica | Descrição |
| --- | --- |
| Entered | Número de usuários que entraram neste componente para serem sincronizados com o Pinterest. |
| Proceeded to Next Step | Quantos usuários avançaram para o próximo componente, se houver um? Todos os usuários avançarão automaticamente se esta for a última etapa na Branch do Canvas. |
| Users Synced | Número de usuários que foram sincronizados com sucesso com o Pinterest. |
| Users Not Synced | Número de usuários que não foram sincronizados devido à falta de campos para correspondência. |
| Users Pending | Número de usuários que estão sendo processados pela Braze para sincronização com o Pinterest. |
| Users Errored | Número de usuários que não foram sincronizados com o Pinterest devido a um erro de API após cerca de 13 horas de tentativas. Possíveis causas de erros podem incluir um token inválido do Pinterest ou se o público foi excluído no Pinterest. |
| Exited Canvas | Número de usuários que saíram do Canvas. Isso ocorre quando a última etapa em um Canvas é um componente de Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Entendendo a análise de dados" }

{% alert important %}
Lembre-se de que haverá um atraso nos relatórios de usuários sincronizados e métricas de erro devido ao envio em massa e às 13 horas de tentativas, respectivamente.
{% endalert %}

## Perguntas frequentes {#frequently-asked-questions}

### Quanto tempo levará para meus públicos serem preenchidos no Pinterest? {#how-long-will-it-take-for-my-audiences-to-populate-in-pinterest}

O tamanho do público será atualizado em 24 a 48 horas na página **Audiences** no Ads Manager do Pinterest.

### Como posso saber se os usuários foram correspondidos após enviá-los ao Pinterest? {#how-do-i-know-if-users-have-matched-after-passing-users-to-pinterest}

O Pinterest não fornece essa informação devido às suas próprias políticas de privacidade de dados.

### O que devo fazer se receber um erro de token inválido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Confirme com o administrador do seu Pinterest Business Hub que você tem as permissões apropriadas para a conta de anúncios que deseja sincronizar. Você também pode desconectar e reconectar sua conta do Pinterest na página de parceiro do Pinterest.

### Por que meu Canvas não pode ser lançado? {#why-is-my-canvas-not-allowed-to-launch}

Verifique se sua conta do Pinterest está conectada com sucesso à Braze na página de parceiro do Pinterest. Certifique-se de que você selecionou uma conta de anúncios, inseriu um nome para o novo público e selecionou campos para correspondência.

### Por que não consigo selecionar minha conta de anúncios na etapa do Audience Sync? {#why-cant-i-select-my-ad-account-for-my-audience-sync-step}

Verifique se o seu token foi gerado com as permissões de conta corretas. Observe que, se você tiver muitos públicos na sua conta de anúncios do Pinterest, o menu suspenso para selecionar sua conta de anúncios pode expirar. Nesse caso, recomendamos reduzir a quantidade de públicos na sua conta de anúncios.