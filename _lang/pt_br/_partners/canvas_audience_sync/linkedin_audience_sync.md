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

Usando o Braze Audience Sync com o LinkedIn, as marcas podem adicionar dados de usuários de sua integração com a Braze às listas de clientes do LinkedIn para veicular anúncios com base em gatilhos comportamentais, segmentação e muito mais. Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS, webhook etc.) em um Braze Canvas com base nos dados de seus usuários agora pode disparar um anúncio para esse usuário em suas listas de clientes do LinkedIn.

**Os casos de uso comuns para a sincronização de público incluem**:

- Direcionamento a usuários de alto valor por meio de vários canais para impulsionar compras ou engajamento
- Redirecionamento de usuários que são menos responsivos a outros canais de marketing
- Criação de públicos de supressão para evitar que os usuários recebam anúncios quando já são consumidores fiéis da sua marca

Esse recurso permite que as marcas controlem quais dados primários específicos são compartilhados com o LinkedIn. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

{% multi_lang_include alerts/early_access_beta_alert.md feature='Audience Sync to LinkedIn' type='beta' %}

## Pré-requisitos {#prerequisites}

Certifique-se de que os seguintes itens tenham sido criados, concluídos ou aceitos antes de configurar a etapa do LinkedIn Audience Sync no Canvas.

| Requisito | Origem | Descrição |
| --- | --- | --- |
| Conta de anúncios do LinkedIn | [LinkedIn](https://www.linkedin.com/campaignmanager) | Uma conta ativa de anúncios do LinkedIn vinculada à sua marca.<br><br>Certifique-se de que aceitou todos os termos e condições relevantes do LinkedIn para acessar e usar essa conta e que seu administrador do LinkedIn lhe concedeu as permissões apropriadas para gerenciar públicos. |
| Termos e políticas do LinkedIn | LinkedIn | Concorde em cumprir todos os termos, políticas, diretrizes e documentação exigidos pelo LinkedIn relacionados ao seu uso do LinkedIn Audience Sync, incluindo quaisquer termos, políticas, diretrizes e documentação incorporados por referência, que podem incluir os do LinkedIn: Termos de Serviços, Contrato de Anúncios, Contrato de Processamento de Dados e Diretrizes da Comunidade Profissional. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Conecte-se ao LinkedIn {#step-1-connect-to-linkedin}

{% alert important %}
Você deve ter a [permissão "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) para conectar o LinkedIn à sua conta da Braze.
{% endalert %}

No dashboard da Braze, acesse **Parceiros de tecnologia** e selecione **LinkedIn**. Na seção **LinkedIn Audience Sync**, selecione **Connect LinkedIn**.

![Página de tecnologia do LinkedIn na Braze com uma seção de Visão Geral e uma seção de LinkedIn Audience Sync com o botão Connected LinkedIn.]({% image_buster /assets/img/linkedin/linkedin3.png %}){: style="max-width:75%;"}

Em seguida, você será redirecionado para a página do LinkedIn OAuth para autorizar a Braze a obter as permissões relacionadas à integração do Audience Sync. Depois de selecionar **Confirm**, você será redirecionado de volta à Braze para selecionar com quais contas de anúncios do LinkedIn você deseja sincronizar.

!["Braze Self Service" selecionado como a conta de anúncio para conectar.]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

Após a conexão bem-sucedida, você retornará à página do parceiro, onde poderá ver quais contas estão conectadas e desconectar contas existentes.

![Uma conta do LinkedIn conectada com sucesso.]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

Sua conexão com o LinkedIn será aplicada no nível do espaço de trabalho da Braze. Se o administrador do LinkedIn remover você da sua conta de anúncios do LinkedIn, a Braze detectará um token inválido. Como resultado, seus Canvas ativos usando o LinkedIn mostrarão erros e a Braze não poderá sincronizar os usuários.

### Etapa 2: Configure seus critérios de entrada no Canvas {#step-2-configure-your-canvas-entry-criteria}

Ao criar públicos para rastreamento de anúncios, talvez seja necessário incluir ou excluir determinados usuários com base em suas preferências e para cumprir as leis de privacidade, como o direito de "Não vender ou compartilhar" de acordo com a [CCPA](https://oag.ca.gov/privacy/ccpa). Os profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários em seus critérios de entrada no Canvas. Abaixo, listamos algumas opções.

Se você coletou o [IDFA do iOS por meio do SDK da Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/overviewother_sdk_customizations/#optional-idfa-collection), poderá usar o filtro **Ads Tracking Enabled**. Selecione o valor como `true` para enviar os usuários apenas para destinos do Audience Sync nos quais eles aceitaram participar.

![Um público de entrada com o filtro "Ad Tracking Enabled is true".]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

Se você estiver coletando `opt-ins`, `opt-outs`, `Do Not Sell Or Share` ou quaisquer outros atributos personalizados relevantes, deve incluí-los nos seus critérios de entrada do Canvas como um filtro:

![Um Canvas com um público de entrada de "opted_in_marketing" igual a "true".]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Para saber mais sobre como cumprir essas leis de proteção de dados na plataforma Braze, consulte a [Assistência técnica de proteção de dados]({{site.baseurl}}/dp-technical-assistance/).

### Etapa 3: Adicione uma etapa de Audience Sync com o LinkedIn {#step-3-add-an-audience-sync-step-with-linkedin}

Adicione um componente em seu Canvas e selecione Audience Sync. Clique no botão **Custom Audience** para abrir o editor de componentes.

![O editor de Canvas com a lista de componentes disponíveis.]({% image_buster /assets/img/linkedin/linkedin2.png %}){: style="max-width:35%;"} ![O componente de Audience Sync selecionado.]({% image_buster /assets/img/linkedin/linkedin1.png %}){: style="max-width:29%;"}

### Etapa 4: Configuração de sincronização {#step-4-sync-setup}

Selecione **LinkedIn** como o parceiro desejado do Audience Sync.

![Os detalhes de "Set up Audience Sync" com os vários parceiros para escolher.]({% image_buster /assets/img/linkedin/linkedin.png %}){: style="max-width:70%;"}

Em seguida, selecione a conta de anúncios do LinkedIn desejada. No menu suspenso **Choose a New or Existing Audience**, digite o nome de um público novo ou existente.

![Audience Sync com LinkedIn com Braze selecionado como a conta de anúncio.]({% image_buster /assets/img/linkedin/linkedin20.png %})

{% tabs %}
{% tab Criar um novo público %}

**Criar um novo público**<br>
Digite um nome para o novo público, selecione **Add Users to Audience** e selecione os campos que deseja sincronizar com o LinkedIn. Para essa integração, no momento oferecemos suporte aos seguintes itens:
- E-mail
- Nome e sobrenome
- GAID para Android

Em seguida, salve seu público clicando no botão **Create Audience** na parte inferior do editor de etapas.

![Um exemplo de público "leads" com a conta de anúncios da Braze selecionada, o público "leads", a ação para adicionar usuários ao público e e-mail, Android GAID e nome e sobrenome como campos para correspondência.]({% image_buster /assets/img/linkedin/linkedin10.png %})

A Braze exibe uma notificação na parte superior do editor de etapas se o público for criado com êxito ou se ocorrerem erros. Os usuários podem referenciar esse público para remoção de usuários mais tarde na jornada do Canvas, pois o público foi criado no modo de rascunho.

![Confirmação de que o público "leads" foi criado.]({% image_buster /assets/img/linkedin/linkedin9.png %})

Ao lançar um Canvas com um novo público, a Braze sincroniza os usuários quase em tempo real quando eles entram no componente do Audience Sync.

{% endtab %}
{% tab Sincronizar com um público existente %}

**Sincronizar com um público existente**<br>
A Braze também oferece a capacidade de adicionar usuários a públicos existentes no LinkedIn para confirmar que esses públicos estão atualizados. Para sincronizar com um público existente, digite o nome do público existente no menu suspenso e selecione **Add to the Audience**. A Braze adicionará usuários quase em tempo real quando eles entrarem no componente do Audience Sync.

![Visualização expandida da etapa de Canvas de Custom Audience. Aqui, a conta de anúncios desejada e o público existente são selecionados.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### Etapa 5: Lançar o Canvas {#step-5-launch-canvas}

Depois de configurar o Audience Sync com o LinkedIn, basta lançar o Canvas! O novo público será criado, e os usuários que passarem pela etapa de Audience Sync serão transferidos para esse público no LinkedIn. Se o seu Canvas contiver componentes subsequentes, seus usuários avançarão para a próxima etapa da jornada do usuário.

É possível visualizar o público no LinkedIn acessando sua conta de anúncios e selecionando **Audiences** na seção **Assets** da navegação. Na página **Audiences**, você pode ver o tamanho de cada público após atingir mais de 300 membros.

![Página do LinkedIn listando as métricas a seguir para o público em questão.]({% image_buster /assets/img/linkedin/linkedin8.png %})

## Considerações sobre sincronização de usuários e limite de taxa {#user-syncing-and-rate-limit-considerations}

Quando os usuários atingem a etapa de Audience Sync, a Braze os sincroniza quase em tempo real, respeitando os limites de taxa da API do LinkedIn. A Braze agrupa e processa o maior número possível de usuários a cada 5 segundos antes de enviá-los ao LinkedIn.

O limite de taxa da API do LinkedIn não permite mais do que dez consultas por segundo e 100.000 usuários por solicitação. Se um cliente atingir esse limite, a Braze tentará novamente a sincronização por até 13 horas. Se a sincronização ainda não for possível, a Braze listará esses usuários na métrica Usuários com erro.

## Entendendo a análise de dados {#understanding-analytics}

A tabela a seguir inclui métricas e descrições para ajudá-lo a entender melhor a análise de dados do seu componente Audience Sync.

| Métrica | Descrição |
| ------ | ----------- |
| Entraram | Número de usuários que entraram nesse componente para serem sincronizados com o LinkedIn. |
| Avançaram para a próxima etapa | Quantos usuários avançaram para o próximo componente, se houver um? Todos os usuários avançarão automaticamente se essa for a última etapa da ramificação do Canvas. |
| Usuários sincronizados | Número de usuários que foram sincronizados com sucesso com o LinkedIn. |
| Usuários não sincronizados | Número de usuários que não foram sincronizados devido à falta de campos para correspondência. |
| Usuários pendentes | Número de usuários atualmente sendo processados pela Braze para sincronização no LinkedIn. |
| Usuários com erro | Número de usuários que não foram sincronizados com o LinkedIn devido a um erro de API após cerca de 13 horas de tentativas. As possíveis causas de erros podem incluir um token inválido do LinkedIn ou se o público foi excluído no LinkedIn. |
| Saíram do Canvas | Número de usuários que saíram do Canvas. Isso ocorre quando a última etapa de um Canvas é um componente de Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Entendendo a análise de dados" }

{% alert important %}
Lembre-se de que haverá um atraso nos relatórios das métricas de usuários sincronizados e usuários com erro devido ao envio em massa e à nova tentativa de 13 horas, respectivamente.
{% endalert %}

{% alert important %}
O LinkedIn fornece métricas adicionais sobre as taxas de correspondência em sua plataforma. Para revisar a correspondência do seu Audience Sync específico, selecione as métricas da etapa de Audience Sync para acessar a página **Canvas Step Details**.
<br><br>
Selecione o parceiro como **LinkedIn**, sua conta de anúncios e o público para ver o tamanho do público e a taxa de correspondência do LinkedIn.

![Um exemplo de métricas da etapa de Audience Sync com 10.000 usuários inseridos.]({% image_buster /assets/img/linkedin/linkedin11.png %})
{% endalert %}

## Perguntas frequentes {#frequently-asked-questions}

### Quanto tempo levará para que os tamanhos do público sejam preenchidos no LinkedIn? {#how-long-will-it-take-for-the-audience-sizes-to-populate-in-linkedin}

Pode haver um atraso de até 48 horas para visualizar os públicos em sua conta do LinkedIn.

### Qual é o tamanho mínimo do público para o LinkedIn preencher na sua conta de anúncios? {#what-is-the-minimum-audience-size-for-linkedin-to-populate-within-your-ad-account}

O público deve incluir pelo menos 300 membros para preencher o tamanho do público em sua conta do LinkedIn.

### O que devo fazer se receber um erro de token inválido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Você pode desconectar e reconectar sua conta do LinkedIn na página de parceiros do LinkedIn. Confirme com seu administrador do LinkedIn que você tem as permissões apropriadas para a conta de anúncios com a qual deseja sincronizar.

### Por que meu Canvas não pode ser lançado? {#why-is-my-canvas-not-allowed-to-launch}

Confirme se sua conta de anúncios do LinkedIn foi conectada com sucesso à Braze na página de parceiros do LinkedIn. Em seguida, verifique se você selecionou uma conta de anúncios, inseriu um nome para o novo público e selecionou os campos para correspondência.

### Como posso saber se houve correspondência entre os usuários depois de passá-los para o LinkedIn? {#how-do-i-know-if-users-have-matched-after-passing-users-to-linkedin}

O LinkedIn fornece informações sobre as taxas de correspondência em seu dashboard. Você pode revisá-las no LinkedIn na seção **Audiences**. Você pode revisar a taxa de correspondência do seu público do LinkedIn nos detalhes da etapa do Canvas da etapa de Audience Sync.

### Quantos públicos o LinkedIn pode suportar? {#how-many-audiences-can-linkedin-support}

Atualmente, não há limite para o número de públicos em sua conta de anúncios do LinkedIn.

### Por que um segmento está preso no status BUILDING e não é atualizado? {#why-is-a-segment-stuck-in-building-status-and-not-updated}

Um segmento é considerado não utilizado e definido como ARCHIVED depois de não ser usado continuamente por 30 dias em um rascunho ou em uma Campaign ativa. Por esse motivo, um segmento pode parecer "preso" em BUILDING quando as atualizações são transmitidas para um segmento ARCHIVED, empurrando-o para o estado BUILDING e, logo antes de ser arquivado novamente, novas atualizações são transmitidas para o segmento não utilizado.