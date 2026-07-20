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

Usando o Braze Audience Sync com a Criteo, as marcas podem optar por adicionar dados de usuários de sua própria integração da Braze às listas de clientes da Criteo para veicular anúncios com base em gatilhos comportamentais, segmentação e muito mais. Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS, webhook, etc.) em um Braze Canvas com base nos dados de seu usuário agora pode ser usado para disparar um anúncio para esse usuário em suas listas de clientes da Criteo.

**Os casos de uso comuns para sincronização de público incluem:**

- Direcionamento a usuários de alto valor por meio de vários canais para impulsionar compras ou engajamento
- Redirecionamento de usuários que são menos responsivos a outros canais de marketing
- Criação de públicos de supressão para evitar que os usuários recebam anúncios quando já são consumidores fiéis da sua marca
- Criação de públicos semelhantes para adquirir novos usuários com mais eficiência

Este recurso oferece às marcas a opção de controlar quais dados primários específicos são compartilhados com a Criteo. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

{% alert important %}
**Isenção de responsabilidade do Audience Sync Pro**<br>
O Braze Audience Sync com a Criteo é uma integração do Audience Sync Pro. Para saber mais sobre essa integração, entre em contato com seu gerente de conta Braze. <br>
{% endalert %}

## Pré-requisitos {#prerequisites}

Você deve garantir que os seguintes itens tenham sido criados e/ou concluídos antes de configurar a sincronização de público com a Criteo.

| Requisito | Origem | Descrição |
| --- | --- | --- |
| Conta de anúncios da Criteo | [Criteo](https://marketing.criteo.com/) | Uma conta ativa de anúncios da Criteo vinculada à sua marca.<br><br>Certifique-se de que o administrador da Criteo lhe concedeu as permissões apropriadas para acessar públicos. |
| [Diretrizes de publicidade da Criteo](https://www.criteo.com/advertising-guidelines/)<br>e<br>[Diretrizes de segurança da marca Criteo](https://www.criteo.com/wp-content/uploads/2017/11/Criteo-Brand-Safety-Guidelines-UK-March-2016.pdf) | Criteo | Como cliente ativo da Criteo, você precisa confirmar que está em conformidade com as diretrizes de publicidade e segurança de marca da Criteo antes de lançar qualquer campanha na Criteo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: conecte-se à Criteo {#step-1-connect-to-criteo}

{% alert important %}
Você deve ter a [permissão "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar a Criteo à sua conta da Braze.
{% endalert %}

No dashboard da Braze, acesse **Partner Integrations** > **Technology Partners** e selecione **Criteo**. Em Criteo Audience Export, selecione **Connect Criteo**.

![Página da tecnologia Criteo na Braze que inclui uma seção Visão geral e uma seção Criteo com o botão Connect Criteo.]({% image_buster /assets/img/criteo/criteo5.png %}){: style="max-width:80%;"}

Uma página oAuth da Criteo será exibida para autorizar a Braze nas permissões relacionadas à sua integração do Audience Sync.

Depois de confirmar, você será redirecionado de volta à Braze para selecionar as contas de anúncios da Criteo que deseja sincronizar.

![Uma lista de contas de anúncios disponíveis que você pode conectar à Criteo.]({% image_buster /assets/img/criteo/criteo7.png %}){: style="max-width:80%;"}

Depois de se conectar com sucesso, você será levado de volta à página do parceiro, onde poderá ver quais contas estão conectadas e desconectar contas existentes.

![Uma versão atualizada da página de parceiros de tecnologia da Criteo mostrando as contas de anúncios conectadas com sucesso.]({% image_buster /assets/img/criteo/criteo4.png %}){: style="max-width:80%;"}

Sua conexão com a Criteo será aplicada no nível do espaço de trabalho da Braze. Se o administrador da Criteo remover você da sua conta de anúncios da Criteo, a Braze detectará um token inválido. Como resultado, seus Canvas ativos que usam a Criteo mostrarão erros, e a Braze não poderá sincronizar os usuários.

### Etapa 2: configure seus critérios de entrada no Canvas {#step-2-configure-your-canvas-entry-criteria}

Ao criar públicos para rastreamento de anúncios, talvez seja necessário incluir ou excluir determinados usuários com base em suas preferências e para cumprir as leis de privacidade, como o direito de "Não vender ou compartilhar" de acordo com a [CCPA](https://oag.ca.gov/privacy/ccpa). Os profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários em seus critérios de entrada no Canvas. Abaixo, listamos algumas opções.

Se você tiver coletado o [IDFA do iOS por meio do SDK da Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection), poderá usar o filtro Ads Tracking Enabled. Selecione o valor como true para enviar apenas usuários para destinos do Audience Sync nos quais eles fizeram opt-in.

![Filtro de entrada do Canvas mostrando Ads Tracking Enabled definido como true.]({% image_buster /assets/img/criteo/criteo11.png %})

Se você estiver coletando `opt-ins`, `opt-outs`, `Do Not Sell Or Share` ou quaisquer outros atributos personalizados relevantes, deve incluí-los nos seus critérios de entrada do Canvas como um filtro:

![Filtro de entrada do Canvas usando atributos personalizados de opt-in para elegibilidade de público.]({% image_buster /assets/img/criteo/criteo12.png %})

Para saber mais sobre como cumprir essas leis de proteção de dados na plataforma Braze, consulte a [Assistência técnica de proteção de dados]({{site.baseurl}}/dp-technical-assistance).

### Etapa 3: adicione uma etapa de sincronização de público com a Criteo {#step-3-add-an-audience-sync-step-with-criteo}

Adicione um componente ao seu Canvas e selecione **Audience Sync**.

![Fluxo de trabalho das etapas anteriores para adicionar um componente do Criteo Audience no Canvas.]({% image_buster /assets/img/criteo/criteo9.png %}){: style="max-width:35%;"} ![Fluxo de trabalho das etapas anteriores para adicionar um componente do Criteo Audience no Canvas.]({% image_buster /assets/img/criteo/criteo10.png %}){: style="max-width:28%;"}

### Etapa 4: configuração de sincronização {#step-4-sync-setup}

Clique no botão **Custom Audience** para abrir o editor de componentes.

Selecione **Criteo** como parceiro desejado do Audience Sync.

![Editor da etapa de Audience Sync com a Criteo selecionada como parceira.]({% image_buster /assets/img/criteo/criteo6.png %})

Em seguida, selecione a conta de anúncios da Criteo desejada. No menu suspenso **Choose a New or Existing Audience**, digite o nome de um público novo ou existente.

{% tabs %}
{% tab Criar um novo público %}
**Criar um novo público**<br>
Digite um nome para o novo público, selecione **Add Users to Audience** e selecione os campos que deseja sincronizar com a Criteo. Em seguida, salve seu público clicando no botão **Create Audience** na parte inferior do editor de etapas.

![Visualização expandida da etapa do Canvas de público personalizado. Aqui, a conta de anúncios desejada é selecionada e um novo público é criado.]({% image_buster /assets/img/criteo/criteo3.png %})

A Braze exibe uma notificação na parte superior do editor de etapas se o público for criado com êxito ou se ocorrerem erros. Os usuários podem referenciar este público para remoção de usuários mais tarde na jornada do Canvas, porque o público foi criado no modo de rascunho.

![Um alerta que aparece depois que um novo público é criado no componente do Canvas.]({% image_buster /assets/img/criteo/criteo1.png %})

Ao lançar um Canvas com um novo público, a Braze sincroniza os usuários quase em tempo real quando eles entram no componente do Audience Sync.
{% endtab %}
{% tab Sincronizar com um público existente %}
**Sincronização com um público existente**<br>
A Braze também oferece a capacidade de adicionar usuários aos públicos existentes da Criteo para garantir que esses públicos estejam atualizados. Para sincronizar com um público existente, digite o nome do público existente no menu suspenso e selecione **Add to the Audience**. A Braze adicionará usuários quase em tempo real quando eles entrarem no componente do Audience Sync.

![Visualização expandida da etapa do Canvas de público personalizado. Aqui, a conta de anúncios desejada e o público existente são selecionados.]({% image_buster /assets/img/criteo/criteo8.png %})

{% endtab %}
{% endtabs %}

### Etapa 5: lance o Canvas {#step-5-launch-canvas}

Depois de configurar o Audience Sync com a Criteo, basta lançar o Canvas! O novo público será criado, e os usuários que passarem pela etapa Audience Sync serão transferidos para esse público na Criteo. Se o seu Canvas contiver componentes subsequentes, os usuários avançarão para a próxima etapa da jornada do usuário.

Você pode visualizar o público na Criteo acessando sua conta do gerenciador de anúncios e selecionando Segments na **Audience Library** da navegação. Na página **Segments**, você pode ver o tamanho de cada público depois que ele atinge ~1.000.

![A biblioteca de público mostrando o segmento, o ID, a origem, o tipo, o tamanho, o uso atual e a última atualização.]({% image_buster /assets/img/criteo/criteo.png %})

## Considerações sobre sincronização de usuários e limite de frequência {#user-syncing-and-rate-limit-considerations}

Quando os usuários atingem a etapa de sincronização de público, a Braze os sincroniza quase em tempo real, respeitando os limites de frequência da API da Criteo. A Braze agrupa e processa o maior número possível de usuários a cada cinco segundos antes de enviá-los para a Criteo.

O limite de frequência da API da Criteo não permite mais do que 250 solicitações por minuto. Se um cliente atingir esse limite, a Braze tentará novamente a sincronização por até ~13 horas. Se a sincronização ainda não for possível, a Braze listará esses usuários na métrica Usuários com erro.

## Entendendo a análise de dados {#understanding-analytics}

A tabela a seguir inclui métricas e descrições para ajudá-lo a entender melhor a análise de dados do seu componente Audience Sync.

| Métrica | Descrição |
| --- | --- |
| Entraram | Número de usuários que entraram nesse componente para serem sincronizados com a Criteo. |
| Avançaram para a próxima etapa | Quantos usuários avançaram para o próximo componente, se houver um. Todos os usuários avançarão automaticamente se essa for a última etapa da ramificação do Canvas. |
| Usuários sincronizados | Número de usuários que foram sincronizados com sucesso com a Criteo. |
| Usuários não sincronizados | Número de usuários que não foram sincronizados devido à falta de campos para correspondência. |
| Usuários pendentes | Número de usuários atualmente sendo processados pela Braze para sincronização com a Criteo. |
| Usuários com erro | Número de usuários que não foram sincronizados com a Criteo devido a um erro de API após cerca de 13 horas de tentativas. As possíveis causas de erros podem incluir um token inválido da Criteo ou se o público foi excluído na Criteo. |
| Saíram do Canvas | Número de usuários que saíram do Canvas. Isso ocorre quando a última etapa de um Canvas é um componente de Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Entendendo a análise de dados" }

{% alert important %}
Lembre-se de que haverá um atraso nos relatórios das métricas de usuários sincronizados e usuários com erro devido ao envio em massa e à nova tentativa de 13 horas, respectivamente.
{% endalert %}

## Perguntas frequentes {#frequently-asked-questions}

### O que devo fazer se receber um erro de token inválido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}
Você pode simplesmente desconectar e reconectar sua conta da Criteo na página de parceiros da Criteo. Verifique com seu administrador da Criteo se você tem as permissões apropriadas para a conta de anúncios com a qual deseja sincronizar.

### Por que meu Canvas não pode ser lançado? {#why-is-my-canvas-not-allowed-to-launch}

Confirme que sua conta de anúncios da Criteo foi conectada com sucesso à Braze na página de parceiros da Criteo. Em seguida, verifique se você selecionou uma conta de anúncios, inseriu um nome para o novo público e selecionou os campos para correspondência.

### Como posso saber se houve correspondência entre os usuários depois de passá-los para a Criteo? {#how-do-i-know-if-users-have-matched-after-passing-users-to-criteo}

A Criteo não fornece essas informações devido às suas políticas internas de privacidade de dados.

### Quantos públicos a Criteo pode suportar? {#how-many-audiences-can-criteo-support}

No momento, você só pode ter 1.000 públicos na sua conta da Criteo. Se você exceder esse limite, a Braze o notificará de que não é possível criar novos públicos. Você precisará remover os públicos que não está mais usando na sua conta de anúncios da Criteo.