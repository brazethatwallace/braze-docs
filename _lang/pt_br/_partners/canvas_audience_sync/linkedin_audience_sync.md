---
nav_title: LinkedIn
article_title: Sincronização de público do Canvas com o LinkedIn
alias: /linkedin_audience_sync/
description: "Este artigo de referência aborda como usar o Braze Audience Sync com o LinkedIn para veicular anúncios com base em gatilhos comportamentais, segmentação e muito mais."
tool:
  - Canvas
page_order: 4

---

# Audience Sync com o LinkedIn {#audience-sync-to-linkedin}

Usando o Braze Audience Sync com o LinkedIn, as marcas podem adicionar dados de usuários de sua integração com a Braze às listas de clientes do LinkedIn para veicular anúncios com base em gatilhos comportamentais, segmentação e muito mais. Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS, webhook etc.) em um BRAZE CANVAS com base nos dados de seus usuários agora pode disparar um anúncio para esse usuário em suas listas de clientes do LinkedIn.

**Os casos de uso comuns para a sincronização de público incluem**:

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md %}

Esse recurso permite que as marcas controlem quais dados primários específicos são compartilhados com o LinkedIn. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

{% multi_lang_include alerts/early_access_beta_alert.md feature='Audience Sync to LinkedIn' type='beta' %}

## Pré-requisitos {#prerequisites}

Você deve garantir que os seguintes itens foram criados, concluídos ou aceitos antes de configurar sua etapa de Audience Sync com o LinkedIn no Canvas.

| Requisito | Origin | Descrição |
| --- | --- | --- |
| Conta de anúncios do LinkedIn | [LinkedIn](https://www.linkedin.com/campaignmanager) | Uma conta de anúncios ativa do LinkedIn vinculada à sua marca.<br><br>Certifique-se de que você aceitou todos os termos e condições relevantes do LinkedIn para acessar e usar essa conta e que o administrador do LinkedIn concedeu a você as permissões apropriadas para gerenciar públicos. |
| Termos e políticas do LinkedIn | LinkedIn | Concorde em cumprir todos os termos, políticas, diretrizes e documentação exigidos pelo LinkedIn relacionados ao seu uso do LinkedIn Audience Sync, incluindo quaisquer termos, políticas, diretrizes e documentação incorporados por referência, que podem incluir: Termos de Serviço, Contrato de Anúncios, Acordo de Processamento de Dados e Diretrizes da Comunidade Profissional do LinkedIn. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Conectar ao LinkedIn {#step-1-connect-to-linkedin}

{% alert important %}
Você deve ter a [permissão "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar o LinkedIn à sua conta da Braze.
{% endalert %}

No dashboard da Braze, acesse **Technology Partners** e selecione **LinkedIn**. Na seção **LinkedIn Audience Sync**, selecione **Connect LinkedIn**.

![Página de tecnologia do LinkedIn na Braze com uma seção de visão geral e uma seção LinkedIn Audience Sync com o botão Connected LinkedIn.]({% image_buster /assets/img/linkedin/linkedin3.png %}){: style="max-width:75%;"}

Você será redirecionado para a página OAuth do LinkedIn para autorizar a Braze nas permissões relacionadas à sua integração de Audience Sync. Após selecionar **Confirm**, você será redirecionado de volta para a Braze para selecionar quais contas de anúncios do LinkedIn deseja sincronizar.

!["Braze Self Service" selecionado como a conta de anúncios a ser conectada.]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

Após a conexão bem-sucedida, você retornará à página de parceiro, onde poderá visualizar quais contas estão conectadas e desconectar contas existentes.

![Uma conta do LinkedIn conectada com sucesso.]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

Sua conexão com o LinkedIn será aplicada no nível do espaço de trabalho da Braze. Se o administrador do LinkedIn remover você da sua conta de anúncios do LinkedIn, a Braze detectará um token inválido. Como resultado, seus Canvas ativos que usam o LinkedIn exibirão erros, e a Braze não conseguirá sincronizar usuários.

### Etapa 2: Configurar os critérios de entrada do Canvas {#step-2-configure-your-canvas-entry-criteria}

Ao criar públicos para rastreamento de anúncios, você pode querer incluir ou excluir determinados usuários com base em suas preferências e para cumprir leis de privacidade, como o direito de "Não Vender ou Compartilhar" previsto na [CCPA](https://oag.ca.gov/privacy/ccpa). Os profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários nos critérios de entrada do Canvas. As opções a seguir podem ajudar.

Se você coletou o [IDFA do iOS por meio do SDK da Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection), poderá usar o filtro **Ads Tracking Enabled**. Selecione o valor como `true` para enviar apenas usuários para destinos de Audience Sync nos quais eles optaram por participar.

![Um público de entrada com o filtro "Ad Tracking Enabled is true".]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

Se você estiver coletando `opt-ins`, `opt-outs`, `Do Not Sell Or Share` ou quaisquer outros atributos personalizados relevantes, inclua-os nos critérios de entrada do Canvas como filtro:

![Um Canvas com público de entrada "opted_in_marketing" igual a "true".]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Para saber mais sobre como cumprir essas leis de proteção de dados na plataforma da Braze, consulte [Assistência técnica para proteção de dados]({{site.baseurl}}/dp-technical-assistance).

### Etapa 3: Adicionar uma etapa de Audience Sync com o LinkedIn {#step-3-add-an-audience-sync-step-with-linkedin}

Adicione um componente ao seu Canvas e selecione Audience Sync. Clique no botão **Custom Audience** para abrir o editor de componentes.

![O editor de Canvas com a lista de componentes disponíveis.]({% image_buster /assets/img/linkedin/linkedin2.png %}){: style="max-width:35%;"} ![O componente Audience Sync selecionado.]({% image_buster /assets/img/linkedin/linkedin1.png %}){: style="max-width:29%;"}

### Etapa 4: Configuração da sincronização {#step-4-sync-setup}

Selecione **LinkedIn** como o parceiro de Audience Sync desejado.

![Os detalhes de "Set up Audience Sync" com os vários parceiros disponíveis para escolha.]({% image_buster /assets/img/linkedin/linkedin.png %}){: style="max-width:70%;"}

Em seguida, selecione a conta de anúncios do LinkedIn desejada. No menu suspenso **Choose a New or Existing Audience**, digite o nome de um público novo ou existente.

![Audience Sync para LinkedIn com Braze selecionado como a conta de anúncios.]({% image_buster /assets/img/linkedin/linkedin20.png %})

{% tabs %}
{% tab Criar um novo público %}

**Criar um novo público**<br>
Insira um nome para o novo público, selecione **Add Users to Audience** e escolha quais campos deseja sincronizar com o LinkedIn. Para essa integração, atualmente oferecemos suporte aos seguintes campos:
- E-mail
- Nome e sobrenome
- Android GAID

Em seguida, salve seu público clicando no botão **Create Audience** na parte inferior do editor de etapas.

![Um exemplo de público "leads" com a conta de anúncios Braze selecionada, público "leads", a ação de adicionar usuários ao público e e-mail, Android GAID e nome e sobrenome como campos de correspondência.]({% image_buster /assets/img/linkedin/linkedin10.png %})

A Braze exibe uma notificação na parte superior do editor de etapas se o público for criado com sucesso ou se ocorrerem erros. Os usuários podem referenciar esse público para remoção de usuários posteriormente na jornada do Canvas, pois o público foi criado no modo rascunho.

![Confirmação de que o público "leads" foi criado.]({% image_buster /assets/img/linkedin/linkedin9.png %})

Ao lançar um Canvas com um novo público, a Braze sincroniza os usuários quase em tempo real à medida que eles entram no componente Audience Sync.

{% endtab %}
{% tab Sincronizar com um público existente %}

**Sincronizar com um público existente**<br>
A Braze também oferece a capacidade de adicionar usuários a públicos existentes do LinkedIn para garantir que esses públicos estejam atualizados. Para sincronizar com um público existente, digite o nome do público existente no menu suspenso e selecione **Add to the Audience**. A Braze adicionará os usuários quase em tempo real à medida que eles entrarem no componente Audience Sync.

![Visualização expandida da etapa Custom Audience do Canvas. Aqui, a conta de anúncios desejada e o público existente estão selecionados.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### Etapa 5: Lançar o Canvas {#step-5-launch-canvas}

Após configurar seu Audience Sync para o LinkedIn, lance o Canvas! O novo público será criado, e os usuários que passarem pela etapa de Audience Sync serão adicionados a esse público no LinkedIn. Se o seu Canvas contiver componentes subsequentes, os usuários avançarão para a próxima etapa em sua jornada.

Você pode visualizar o público no LinkedIn acessando sua conta de anúncios e selecionando **Audiences** na seção **Assets** da navegação. Na página **Audiences**, você pode ver o tamanho de cada público após atingir mais de 300 membros.

![Página do LinkedIn listando as métricas a seguir para o público especificado.]({% image_buster /assets/img/linkedin/linkedin8.png %})

## Sincronização de usuários e considerações sobre limite de frequência {#user-syncing-and-rate-limit-considerations}

À medida que os usuários chegam à etapa de Audience Sync, a Braze os sincroniza em tempo quase real, respeitando os limites de frequência da API do LinkedIn. A Braze agrupa e processa o maior número possível de usuários a cada 5 segundos antes de enviá-los ao LinkedIn.

O limite de frequência da API do LinkedIn permite no máximo dez consultas por segundo e 100.000 usuários por solicitação. Se um cliente atingir esse limite, a Braze tentará novamente a sincronização por aproximadamente 13 horas. Se a sincronização ainda não for possível, a Braze listará esses usuários na métrica Users Errored.

## Entendendo a análise de dados {#understanding-analytics}

A tabela a seguir inclui métricas e descrições para ajudar você a entender melhor a análise de dados do seu componente de Audience Sync.

| MÉTRICA | DESCRIÇÃO |
| ------ | ----------- |
| Entered | Número de usuários que entraram neste componente para serem sincronizados com o LinkedIn. |
| Proceeded to Next Step | Quantos usuários avançaram para o próximo componente, se houver um? Todos os usuários avançarão automaticamente se esta for a última etapa na Branch do Canvas. |
| Users Synced | Número de usuários que foram sincronizados com sucesso com o LinkedIn. |
| Users Not Synced | Número de usuários que não foram sincronizados devido à falta de campos para correspondência. |
| Users Pending | Número de usuários que estão sendo processados pela Braze para sincronização com o LinkedIn. |
| Users Errored | Número de usuários que não foram sincronizados com o LinkedIn devido a um erro de API após cerca de 13 horas de tentativas. Possíveis causas de erros podem incluir um token inválido do LinkedIn ou se o público foi excluído no LinkedIn. |
| Exited Canvas | Número de usuários que saíram do Canvas. Isso ocorre quando a última etapa em um Canvas é um componente de Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Entendendo a análise de dados" }

{% alert important %}
Lembre-se de que haverá um atraso no relatório das métricas de usuários sincronizados e usuários com erro devido ao envio em massa e às 13 horas de tentativas, respectivamente.
{% endalert %}

{% alert important %}
O LinkedIn fornece métricas adicionais sobre taxas de correspondência dentro da plataforma. Para revisar a correspondência do seu Audience Sync específico, selecione as métricas da etapa de Audience Sync para acessar a página **Canvas Step Details**.
<br><br>
Selecione o parceiro como **LinkedIn**, sua conta de anúncios e o público para ver o tamanho do público e a taxa de correspondência do LinkedIn.

![Um exemplo de métricas da etapa de Audience Sync com 10.000 usuários que entraram.]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## Perguntas frequentes {#frequently-asked-questions}

### Quanto tempo leva para os tamanhos de público serem preenchidos no LinkedIn? {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-linkedin}

Há um atraso de até 48 horas para visualizar os públicos na sua conta do LinkedIn.

### Qual é o tamanho mínimo de público para que o LinkedIn preencha os dados na sua conta de anúncios? {#what-is-the-minimum-audience-size-for-linkedin-to-populate-within-your-ad-account}

O público deve incluir pelo menos 300 membros para que o tamanho do público seja preenchido na sua conta do LinkedIn.

### O que devo fazer se receber um erro de token inválido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Você pode desconectar e reconectar sua conta do LinkedIn na página de parceiro do LinkedIn. Confirme com o administrador do LinkedIn que você tem as permissões apropriadas para a conta de anúncios com a qual deseja sincronizar.

### Por que meu Canvas não pode ser lançado? {#why-is-my-canvas-not-allowed-to-launch}

Confirme que sua conta de anúncios do LinkedIn foi conectada com sucesso à Braze na página de parceiro do LinkedIn. Em seguida, verifique se você selecionou uma conta de anúncios, inseriu um nome para o novo público e selecionou os campos para correspondência.

### Como sei se os usuários foram correspondidos após enviar usuários para o LinkedIn? {#how-do-i-know-if-users-have-matched-after-passing-users-to-linkedin}

O LinkedIn fornece informações sobre taxas de correspondência no dashboard deles. Você pode verificar isso no LinkedIn na seção **Audiences**. Você pode verificar a taxa de correspondência do seu público do LinkedIn nos detalhes da etapa do Canvas da sua etapa de Audience Sync.

### Quantos públicos o LinkedIn suporta? {#how-many-audiences-can-linkedin-support}

Atualmente, não há limite para o número de públicos na sua conta de anúncios do LinkedIn.

### Por que um Segment está preso no status BUILDING e não é atualizado? {#why-is-a-segment-stuck-in-building-status-and-not-updated}

Um Segment é considerado não utilizado e definido como ARCHIVED depois de não ser usado continuamente por 30 dias em uma Campaign de rascunho ou ativa. Por causa disso, um Segment pode parecer "preso" em BUILDING quando atualizações são transmitidas para um Segment ARCHIVED, empurrando-o para o estado BUILDING, e logo antes de ser arquivado novamente, novas atualizações são transmitidas para o Segment não utilizado.