---
nav_title: TikTok
article_title: Sincronização do público do Canvas com o TikTok
alias: /tiktok_audience_sync/
description: "Este artigo de referência aborda como usar o Braze Audience Sync com o TikTok para veicular anúncios com base em disparadores comportamentais, segmentação e muito mais."
tool:
  - Canvas
page_order: 8

---

# Sincronização do público com o TikTok {#audience-sync-to-tiktok}

Usando o Braze Audience Sync com o TikTok, as marcas podem optar por adicionar dados de usuários de sua própria integração Braze ao TikTok Audiences para veicular anúncios com base em disparadores comportamentais, segmentação e muito mais. Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS, webhook, etc.) em um Canvas da Braze.

**Os casos de uso comuns para a sincronização do público incluem**:

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md lookalike=true %}

Esse recurso permite que as marcas controlem quais dados primários específicos são compartilhados com o TikTok. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

{% alert important %}
**Isenção de responsabilidade do Audience Sync Pro**<br>
O Braze Audience Sync com o TikTok é uma integração do Audience Sync Pro. Para saber mais sobre essa integração, entre em contato com seu gerente de conta da Braze.
{% endalert %}

## Pré-requisitos {#prerequisites}

Você deve garantir que os itens a seguir sejam criados, concluídos e/ou aceitos antes de configurar sua etapa de Público do TikTok no Canvas.

| Requisito | Origin | Descrição |
| ----------- | ------ | ----------- |
| Conta do TikTok for Business Center | [TikTok](https://business.tiktok.com/) | Uma ferramenta centralizada para gerenciar os ativos da sua marca no TikTok (como contas de anúncios, páginas e apps). |
| Conta de anúncios do TikTok | [TikTok](https://ads.tiktok.com/) | Uma conta de anúncios ativa do TikTok vinculada à conta do Business Center da sua marca.<br><br>Certifique-se de que o administrador do TikTok Business Center tenha concedido a você permissões de administrador para as contas de anúncios do TikTok que você planeja usar com a Braze. |
| Termos e políticas do TikTok | [TikTok](https://ads.tiktok.com/i18n/official/policy/terms) | Concorde em cumprir todos os termos, políticas, diretrizes e documentação exigidos pelo TikTok relacionados ao seu uso do TikTok Audience Sync, incluindo quaisquer termos, políticas, diretrizes e documentação incorporados por referência, que podem incluir: os Termos Comerciais de Serviço, Termos de Publicidade, Política de Privacidade, Termos de Público Personalizado, Termos de Serviço para Desenvolvedores, Acordo de Compartilhamento de Dados para Desenvolvedores, Políticas de Publicidade, Diretrizes da Marca e Diretrizes da Comunidade. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Conectar ao TikTok {#step-1-connect-to-tiktok}

{% alert important %}
Você precisa ter a [permissão "Admin"]({{site.baseurl}}/user_guide/administer/global/user_management/permissions#admin) para conectar o TikTok à sua conta da Braze.
{% endalert %}

No dashboard da Braze, acesse **Integrações com Parceiros** > **Parceiros de Tecnologia** e selecione **TikTok**. Em TikTok Audience Sync, selecione **Connect TikTok**.

![Página de tecnologia do TikTok na Braze com uma seção de visão geral e uma seção TikTok Audience Sync com o botão Connected TikTok.]({% image_buster /assets/img/tiktok/tiktok1.png %}){: style="max-width:75%;"}

Você será redirecionado para a página OAuth do TikTok para autorizar a Braze a gerenciar contas de anúncios e públicos. Após selecionar **Confirm**, você será redirecionado de volta para a Braze para selecionar quais contas de anúncios do TikTok deseja sincronizar.

![Página de autorização OAuth do TikTok solicitando acesso para gerenciamento de público pela Braze.]({% image_buster /assets/img/tiktok/tiktok2.png %}){: style="max-width:75%;"}

Após a conexão bem-sucedida, você retornará à página de parceiro. Aqui, é possível visualizar quais contas estão conectadas e desconectar contas existentes.

![Página de parceiro TikTok na Braze mostrando contas de anúncios do TikTok conectadas.]({% image_buster /assets/img/tiktok/tiktok3.png %}){: style="max-width:75%;"}

Sua conexão com o TikTok será aplicada no nível do espaço de trabalho da Braze. Se o administrador do TikTok remover você do TikTok Business Center ou revogar o acesso às contas conectadas do TikTok, a Braze detectará um token inválido. Como resultado, seus Canvas ativos que utilizam componentes de TikTok Audience exibirão erros, e a Braze não conseguirá sincronizar os usuários.

### Etapa 2: Adicionar um componente TikTok Audience no Canvas {#step-2-add-a-tiktok-audience-component-in-canvas}

Adicione um componente ao seu Canvas e selecione **Audience Sync**.

![Seletor de etapas do Canvas com a opção do componente Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![Cartão do componente Audience Sync adicionado a uma jornada do Canvas.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Etapa 3: Configuração da sincronização {#step-3-sync-setup}

Clique no botão **Custom Audience** para abrir o editor do componente.

Selecione **TikTok** como o parceiro de Audience Sync desejado.

![Editor do componente Audience Sync com TikTok selecionado como parceiro de sincronização.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Em seguida, selecione a conta de anúncios do TikTok desejada. No menu suspenso **Choose a New or Existing Audience**, digite o nome de um público novo ou existente.

![Editor do TikTok Audience Sync mostrando a seleção de conta de anúncios e o menu suspenso de público.]({% image_buster /assets/img/tiktok/tiktok11.png %})

{% tabs %}
{% tab Criar um novo público %}

**Criar um novo público**<br>
Insira um nome para o novo público, selecione **Add Users to Audience** e escolha quais campos deseja sincronizar com o TikTok. Em seguida, salve seu público clicando no botão **Create Audience** na parte inferior do editor de etapas.

![Formulário de criação de novo público na etapa TikTok Audience Sync com campos de correspondência selecionados.]({% image_buster /assets/img/audience_sync/tiktok3.png %})

A Braze exibe uma notificação na parte superior do editor de etapas se o público for criado com sucesso ou se ocorrerem erros. Os usuários podem referenciar esse público para remoção de usuários posteriormente na jornada do Canvas, pois o público foi criado em modo de rascunho.

![Notificação de sucesso na etapa Audience Sync após a criação de um novo público do TikTok.]({% image_buster /assets/img/audience_sync/tiktok2.png %})

Quando você lança um Canvas com um novo público, a Braze sincroniza os usuários quase em tempo real à medida que eles entram na etapa de público.

{% endtab %}
{% tab Sincronizar com um público existente %}

**Sincronizar com um público existente**<br>
A Braze também oferece a possibilidade de adicionar usuários a públicos existentes do TikTok para garantir que esses públicos estejam atualizados. Para sincronizar com um público existente, digite o nome do público existente no menu suspenso e selecione **Add to the Audience**. A Braze adicionará os usuários quase em tempo real à medida que eles entrarem na etapa TikTok Audience.

![Visualização expandida da etapa Custom Audience do Canvas. Aqui, a conta de anúncios desejada e o público existente estão selecionados.]({% image_buster /assets/img/audience_sync/tiktok.png %})

{% endtab %}
{% endtabs %}

### Etapa 4: Lançar o Canvas {#step-4-launch-canvas}
Após configurar seu componente TikTok Audience, lance o Canvas! Um novo público será criado, e os usuários que passarem pelo componente TikTok Audience serão adicionados a esse público no TikTok. Se o seu Canvas contiver componentes subsequentes, os usuários avançarão para a próxima etapa em sua jornada.

Você pode visualizar o público no TikTok acessando sua conta do **Ads Manager** e selecionando **Audiences** no menu suspenso **Assets**. Na página **Audience**, é possível ver o tamanho de cada público após ele atingir &#126;1.000.

![Página do TikTok listando as seguintes métricas para o público especificado.]({% image_buster /assets/img/tiktok/tiktok5.png %})

## Sincronização de usuários e considerações sobre limite de frequência {#user-syncing-and-rate-limit-considerations}

Quando os usuários chegam à etapa de Audience Sync, a Braze os sincroniza quase em tempo real, respeitando os limites de frequência da API de Marketing do TikTok. A Braze agrupa e processa o maior número possível de usuários a cada 5 segundos antes de enviá-los ao TikTok.

O limite de frequência da API de Segment do TikTok permite no máximo 50 consultas por segundo e 10 mil usuários por solicitação. Se um cliente atingir esse limite, a Braze tenta novamente a sincronização por até &#126;13 horas. Se a sincronização ainda não for possível, a Braze lista esses usuários na métrica Users Errored.

## Entendendo a análise de dados {#understanding-analytics}

A tabela a seguir inclui métricas e descrições para ajudar você a entender melhor a análise de dados do seu componente de Audience Sync.

| Métrica | Descrição |
| ------ | ----------- |
| Entered | Número de usuários que entraram neste componente para serem sincronizados com o TikTok. |
| Proceeded to Next Step | Número de usuários que avançaram para o próximo componente, se houver. Todos os usuários avançarão automaticamente se esta for a última etapa na ramificação do Canvas. |
| Users Synced | Número de usuários que foram sincronizados com sucesso com o TikTok. Observe que isso não equivale a usuários correspondidos no TikTok. |
| Users Not Synced | Número de usuários que não foram sincronizados devido à falta de campos para correspondência. |
| Users Pending | Número de usuários que estão sendo processados pela Braze para sincronização com o TikTok. |
| Users Errored | Número de usuários que não foram sincronizados com o TikTok devido a um erro de API após cerca de 13 horas de tentativas. As possíveis causas de erros podem incluir um token do TikTok inválido ou se o público foi excluído no TikTok. |
| Exited Canvas | Número de usuários que saíram do Canvas. Isso ocorre quando a última etapa em um Canvas é um componente de Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Entendendo a análise de dados" }

{% alert important %}
Lembre-se de que haverá um atraso no relatório das métricas de usuários sincronizados e usuários com erro devido ao envio em massa e à tentativa de 13 horas, respectivamente.
{% endalert %}

## Perguntas frequentes {#frequently-asked-questions}

### O que devo fazer se receber um erro de token inválido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Você pode desconectar e reconectar sua conta do TikTok na página de parceiro do TikTok. Confirme com o administrador do TikTok Business Center que você tem as permissões apropriadas para a conta de anúncios que deseja sincronizar.

### Por que meu Canvas não pode ser lançado? {#why-is-my-canvas-not-allowed-to-launch}

Confirme que sua conta do TikTok está conectada com sucesso à Braze na página de parceiro do TikTok. Em seguida, verifique se você selecionou uma conta de anúncios, inseriu um nome para o novo público e selecionou os campos para correspondência.

### Como sei se os usuários foram correspondidos após enviar os usuários para o TikTok? {#how-do-i-know-if-users-have-matched-after-passing-users-to-tiktok}

O TikTok não fornece essa informação devido às suas políticas de privacidade de dados.

### Quanto tempo levará para meus públicos serem preenchidos no TikTok? {#how-long-will-it-take-for-my-audiences-to-populate-in-tiktok}

O tamanho do público será atualizado dentro de 24 a 48 horas na página de públicos no Gerenciador de Anúncios do TikTok.

### Qual é o número máximo de públicos que posso ter na minha conta de anúncios do TikTok? {#what-is-the-maximum-number-of-audiences-i-can-have-in-my-tiktok-ad-account}

Você pode ter até 400 públicos por conta de anúncios do TikTok.

### Por que o tamanho do meu público ou a taxa de correspondência no TikTok é maior do que os usuários sincronizados na Braze com o Audience Sync? {#why-is-my-audience-size-or-match-rate-in-tiktok-higher-than-the-users-synced-in-braze-with-audience-sync}

Isso acontece porque, no TikTok, um ID pode estar associado a vários usuários do TikTok. Isso ocorre com mais frequência quando os clientes usam IDs de anúncios móveis (iOS IDFA e Android GAID), pois um dispositivo pode ter vários usuários do TikTok conectados.

Além disso, o TikTok também conta os usuários do Pangle como usuários correspondidos, o que em alguns casos pode resultar em uma taxa de correspondência elevada. No entanto, quando você usa o público para veiculação de anúncios, o tamanho real do público alcançável pode não ser tão alto quanto o tamanho de usuários correspondidos, pois depende do posicionamento e de outros fatores de influência.

### Por que estou recebendo um e-mail com o assunto "Audience Does Not Exist For Canvas"? {#why-am-i-receiving-an-email-with-the-subject-audience-does-not-exist-for-canvas}

Isso pode ocorrer se o público que você escolheu para sincronizar não for um público de streaming (por exemplo, se for um público semelhante ou um público de arquivo de usuários). Tente criar um novo público por meio da etapa do Canvas de Audience Sync da Braze.