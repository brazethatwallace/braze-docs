---
nav_title: Criteo
article_title: Sincronização de público do Canvas com a Criteo
description: "Este artigo de referência aborda como usar o Braze Audience Sync com a Criteo para veicular anúncios com base em gatilhos comportamentais, segmentação e muito mais."
page_order: 1
alias: /audience_sync_criteo/

tool:
  - Canvas
---

# Sincronização de público com a Criteo {#audience-sync-to-criteo}

Usando o Braze Audience Sync com a Criteo, as marcas podem optar por adicionar dados de usuários de sua própria integração da Braze às listas de clientes da Criteo para veicular anúncios com base em gatilhos comportamentais, segmentação e muito mais. Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS, webhook, etc.) em um BRAZE CANVAS com base nos dados de seu usuário agora pode ser usado para disparar um anúncio para esse usuário em suas listas de clientes da Criteo.

**Os casos de uso comuns para sincronização de público incluem:**

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md lookalike=true %}

Este recurso oferece às marcas a opção de controlar quais dados primários específicos são compartilhados com a Criteo. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

{% alert important %}
**Isenção de responsabilidade do Audience Sync Pro**<br>
O Braze Audience Sync com a Criteo é uma integração do Audience Sync Pro. Para saber mais sobre essa integração, entre em contato com seu gerente de conta Braze. <br>
{% endalert %}

## Pré-requisitos {#prerequisites}

Você deve garantir que os itens a seguir foram criados e/ou concluídos antes de configurar a sincronização de público com o Criteo.

| Requisito | Origin | Descrição |
| --- | --- | --- |
| Conta de anúncios do Criteo | [Criteo](https://marketing.criteo.com/) | Uma conta de anúncios ativa do Criteo vinculada à sua marca.<br><br>Certifique-se de que o administrador do Criteo concedeu a você as permissões apropriadas para acessar públicos. |
| [Diretrizes de publicidade do Criteo](https://www.criteo.com/advertising-guidelines/)<br>e<br>[Diretrizes de segurança de marca do Criteo](https://www.criteo.com/wp-content/uploads/2017/11/Criteo-Brand-Safety-Guidelines-UK-March-2016.pdf) | Criteo | Como cliente ativo do Criteo, você deve garantir que está em conformidade com as Diretrizes de Publicidade e de Segurança de Marca do Criteo antes de lançar qualquer campanha no Criteo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Conectar ao Criteo {#step-1-connect-to-criteo}

{% alert important %}
Você precisa ter a [permissão "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar o Criteo à sua conta da Braze.
{% endalert %}

No dashboard da Braze, acesse **Integrações com Parceiros** > **Parceiros de Tecnologia** e selecione **Criteo**. Em Criteo Audience Export, selecione **Connect Criteo**.

![Página de tecnologia do Criteo na Braze que inclui uma seção de Visão Geral e uma seção do Criteo com o botão Connected Criteo.]({% image_buster /assets/img/criteo/criteo5.png %}){: style="max-width:80%;"}

Uma página de oAuth do Criteo será exibida para autorizar a Braze a obter as permissões relacionadas à sua integração de Audience Sync.

Depois de selecionar confirmar, você será redirecionado de volta para a Braze para selecionar quais contas de anúncios do Criteo deseja sincronizar.

![Uma lista de contas de anúncios disponíveis que você pode conectar ao Criteo.]({% image_buster /assets/img/criteo/criteo7.png %}){: style="max-width:80%;"}

Após a conexão bem-sucedida, você será levado de volta à página do parceiro, onde poderá ver quais contas estão conectadas e desconectar contas existentes.

![Uma versão atualizada da página de parceiros de tecnologia do Criteo mostrando as contas de anúncios conectadas com sucesso.]({% image_buster /assets/img/criteo/criteo4.png %}){: style="max-width:80%;"}

Sua conexão com o Criteo será aplicada no nível do espaço de trabalho da Braze. Se o administrador do Criteo remover você da sua conta de anúncios do Criteo, a Braze detectará um token inválido. Como resultado, seus Canvas ativos que usam o Criteo mostrarão erros, e a Braze não conseguirá sincronizar os usuários.

### Etapa 2: Configurar os critérios de entrada do Canvas {#step-2-configure-your-canvas-entry-criteria}

Ao criar públicos para rastreamento de anúncios, você pode querer incluir ou excluir determinados usuários com base em suas preferências e para cumprir as leis de privacidade, como o direito de "Não Vender ou Compartilhar" previsto na [CCPA](https://oag.ca.gov/privacy/ccpa). Os profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários nos critérios de entrada do Canvas. As opções a seguir podem ajudar.

Se você coletou o [IDFA do iOS por meio do SDK da Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection), poderá usar o filtro Ads Tracking Enabled. Selecione o valor como verdadeiro para enviar apenas os usuários para destinos de Audience Sync nos quais eles aceitaram participar.

![Filtro de entrada do Canvas mostrando Ads Tracking Enabled definido como verdadeiro.]({% image_buster /assets/img/criteo/criteo11.png %})

Se você estiver coletando `opt-ins`, `opt-outs`, `Do Not Sell Or Share` ou quaisquer outros atributos personalizados relevantes, deverá incluí-los nos critérios de entrada do Canvas como filtro:

![Filtro de entrada do Canvas usando atributos personalizados de aceitação para elegibilidade do público.]({% image_buster /assets/img/criteo/criteo12.png %})

Para saber mais sobre como cumprir essas leis de proteção de dados na plataforma da Braze, consulte [Assistência técnica para proteção de dados]({{site.baseurl}}/dp-technical-assistance).

### Etapa 3: Adicionar uma etapa de Audience Sync com o Criteo {#step-3-add-an-audience-sync-step-with-criteo}

Adicione um componente ao seu Canvas e selecione **Audience Sync**.

![Fluxo de trabalho das etapas anteriores para adicionar um componente de Audience do Criteo no Canvas.]({% image_buster /assets/img/criteo/criteo9.png %}){: style="max-width:35%;"} ![Fluxo de trabalho das etapas anteriores para adicionar um componente de Audience do Criteo no Canvas.]({% image_buster /assets/img/criteo/criteo10.png %}){: style="max-width:28%;"}

### Etapa 4: Configuração da sincronização {#step-4-sync-setup}

Clique no botão **Custom Audience** para abrir o editor do componente.

Selecione **Criteo** como o parceiro de Audience Sync desejado.

![Editor da etapa de Audience Sync com o Criteo selecionado como parceiro.]({% image_buster /assets/img/criteo/criteo6.png %})

Em seguida, selecione a conta de anúncios do Criteo desejada. No menu suspenso **Choose a New or Existing Audience**, digite o nome de um público novo ou existente.

{% tabs %}
{% tab Criar um novo público %}
**Criar um novo público**<br>
Insira um nome para o novo público, selecione **Add Users to Audience** e escolha quais campos deseja sincronizar com o Criteo. Em seguida, salve seu público clicando no botão **Create Audience** na parte inferior do editor da etapa.

![Visualização expandida da etapa Custom Audience do Canvas. Aqui, a conta de anúncios desejada está selecionada e um novo público é criado.]({% image_buster /assets/img/criteo/criteo3.png %})

A Braze exibe uma notificação na parte superior do editor da etapa se o público for criado com sucesso ou se ocorrerem erros. Os usuários podem fazer referência a esse público para remoção de usuários posteriormente na jornada do Canvas, pois o público foi criado no modo rascunho.

![Um alerta que aparece após a criação de um novo público no componente do Canvas.]({% image_buster /assets/img/criteo/criteo1.png %})

Quando você lança um Canvas com um novo público, a Braze sincroniza os usuários quase em tempo real à medida que eles entram no componente de Audience Sync.
{% endtab %}
{% tab Sincronizar com um público existente %}
**Sincronizar com um público existente**<br>
A Braze também oferece a capacidade de adicionar usuários a públicos existentes do Criteo para garantir que esses públicos estejam atualizados. Para sincronizar com um público existente, digite o nome do público existente no menu suspenso e selecione **Add to the Audience**. A Braze adicionará os usuários quase em tempo real à medida que eles entrarem no componente de Audience Sync.

![Visualização expandida da etapa Custom Audience do Canvas. Aqui, a conta de anúncios desejada e o público existente estão selecionados.]({% image_buster /assets/img/criteo/criteo8.png %})

{% endtab %}
{% endtabs %}

### Etapa 5: Lançar o Canvas {#step-5-launch-canvas}

Após configurar seu Audience Sync para o Criteo, lance o Canvas! O novo público será criado, e os usuários que passarem pela etapa de Audience Sync serão incluídos nesse público no Criteo. Se o seu Canvas contiver componentes subsequentes, os usuários avançarão para a próxima etapa em sua jornada.

Você pode visualizar o público no Criteo acessando sua conta do gerenciador de anúncios e selecionando Segments na **Audience Library** da navegação. Na página **Segments**, você pode ver o tamanho de cada público depois que ele atingir aproximadamente 1.000.

![A biblioteca de públicos mostrando o segmento, id, origem, tipo, tamanho, uso atual e última atualização.]({% image_buster /assets/img/criteo/criteo.png %})

## Considerações sobre sincronização de usuários e limite de frequência {#user-syncing-and-rate-limit-considerations}

À medida que os usuários chegam à etapa de Audience Sync, a Braze os sincroniza em tempo quase real, respeitando os limites de frequência da API da Criteo. A Braze agrupa e processa o maior número possível de usuários a cada cinco segundos antes de enviá-los à Criteo.

O limite de frequência da API da Criteo permite no máximo 250 solicitações por minuto. Se um cliente atingir esse limite, a Braze tenta novamente a sincronização por aproximadamente 13 horas. Se a sincronização ainda não for possível, a Braze lista esses usuários na métrica Users Errored.

## Entendendo a análise de dados {#understanding-analytics}

A tabela a seguir inclui métricas e descrições para ajudar você a entender melhor a análise de dados do seu componente de Audience Sync.

| Métrica | Descrição |
| --- | --- |
| Entered | Número de usuários que entraram neste componente para serem sincronizados com o Criteo. |
| Proceeded to Next Step | Quantos usuários avançaram para o próximo componente, se houver um. Todos os usuários avançarão automaticamente se esta for a última etapa na Branch do Canvas. |
| Users Synced | Número de usuários que foram sincronizados com sucesso com o Criteo. |
| Users Not Synced | Número de usuários que não foram sincronizados devido à falta de campos para correspondência. |
| Users Pending | Número de usuários que estão sendo processados pela Braze para sincronização com o Criteo. |
| Users Errored | Número de usuários que não foram sincronizados com o Criteo devido a um erro de API após cerca de 13 horas de tentativas. Possíveis causas de erros podem incluir um token do Criteo inválido ou se o público foi excluído no Criteo. |
| Exited Canvas | Número de usuários que saíram do Canvas. Isso ocorre quando a última etapa em um Canvas é um componente de Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Entendendo a análise de dados" }

{% alert important %}
Lembre-se de que haverá um atraso no relatório das métricas de usuários sincronizados e usuários com erro devido ao envio em massa e à tentativa de 13 horas, respectivamente.
{% endalert %}

## Perguntas frequentes {#frequently-asked-questions}

### O que devo fazer se receber um erro de token inválido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}
Você pode simplesmente desconectar e reconectar sua conta Criteo na página de parceiro da Criteo. Confirme com o administrador da Criteo que você tem as permissões apropriadas para a conta de anúncios com a qual deseja sincronizar.

### Por que meu Canvas não pode ser lançado? {#why-is-my-canvas-not-allowed-to-launch}

Confirme que sua conta de anúncios da Criteo foi conectada com sucesso à Braze na página de parceiro da Criteo. Em seguida, verifique se você selecionou uma conta de anúncios, inseriu um nome para o novo público e selecionou campos para correspondência.

### Como sei se os usuários foram correspondidos após enviar usuários para a Criteo? {#how-do-i-know-if-users-have-matched-after-passing-users-to-criteo}

A Criteo não fornece essa informação devido às suas próprias políticas de privacidade de dados.

### Quantos públicos a Criteo suporta? {#how-many-audiences-can-criteo-support}

No momento, você pode ter apenas 1.000 públicos na sua conta Criteo. Se você exceder esse limite, a Braze notificará que não é possível criar novos públicos. Você precisará remover os públicos que não está mais usando na sua conta de anúncios da Criteo.