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

Usando o Braze Audience Sync com o LinkedIn, as marcas podem adicionar dados de usuários de sua integração com a Braze às listas de clientes do LinkedIn para veicular anúncios com base em gatilhos comportamentais, segmentação e muito mais. Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS, webhook etc.) em um Canvas da Braze com base nos dados de seus usuários agora pode disparar um anúncio para esse usuário em suas listas de clientes do LinkedIn.

**Os casos de uso comuns para a sincronização de público incluem**:

{% multi_lang_include partners/canvas_audience_sync/common_use_cases.md %}

Esse recurso permite que as marcas controlem quais dados primários específicos são compartilhados com o LinkedIn. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

## Pré-requisitos {#prerequisites}

Você precisa ter os seguintes itens criados, concluídos ou aceitos antes de configurar sua etapa de Audience Sync com o LinkedIn no Canvas.

| Requisito | Origin | Descrição |
| --- | --- | --- |
| Audience Sync Pro | Braze | O LinkedIn é um parceiro do [Audience Sync Pro]({{site.baseurl}}/partners/canvas_audience_sync/overview#audience-sync-pro). Selecione o LinkedIn nas suas alocações do Audience Sync Pro na página **Technology Partners** antes de conectar uma conta de anúncios. Entre em contato com o gerente de conta da Braze para obter detalhes sobre a compra. |
| Conta de anúncios do LinkedIn | [LinkedIn](https://www.linkedin.com/campaignmanager) | Uma conta de anúncios do LinkedIn ativa vinculada à sua marca.<br><br>Verifique se você aceitou todos os termos e condições relevantes do LinkedIn para acessar e usar essa conta. Seu administrador do LinkedIn precisa conceder a você uma destas funções de conta de anúncios: Account Billing Admin, Account Manager, Campaign Manager ou Creative Manager. |
| Termos e políticas do LinkedIn | LinkedIn | Concorde em cumprir todos os termos, políticas, diretrizes e documentações exigidos pelo LinkedIn relacionados ao uso do LinkedIn Audience Sync, incluindo quaisquer termos, políticas, diretrizes e documentações incorporados por referência, que podem incluir: Termos de Serviço, Contrato de Anúncios, Acordo de Processamento de Dados e Diretrizes da Comunidade Profissional do LinkedIn. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Conectar ao LinkedIn {#step-1-connect-to-linkedin}

{% alert important %}
Você deve ter a [permissão "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar o LinkedIn à sua conta da Braze.
{% endalert %}

No dashboard da Braze, acesse **Parceiros de tecnologia** e selecione **LinkedIn**. Na seção **LinkedIn Audience Sync**, selecione **Connect LinkedIn**.

Você será redirecionado para a página OAuth do LinkedIn para autorizar a Braze nas permissões relacionadas à sua integração de Audience Sync. Depois de selecionar **Confirm**, você será redirecionado de volta à Braze para selecionar quais contas de anúncios do LinkedIn deseja sincronizar.

!["Braze Self Service" está selecionada como a conta de anúncios a ser conectada.]({% image_buster /assets/img/linkedin/linkedin7.png %}){: style="max-width:75%;"}

Quando a conexão é realizada com sucesso, você retorna à página de parceiro, onde pode visualizar quais contas estão conectadas e desconectar contas existentes.

![Uma conta do LinkedIn conectada com sucesso.]({% image_buster /assets/img/linkedin/linkedin6.png %}){: style="max-width:75%;"}

Sua conexão com o LinkedIn é aplicada no nível do espaço de trabalho da Braze. Se o administrador do LinkedIn remover você da conta de anúncios do LinkedIn, a Braze detectará um token inválido. Como resultado, seus Canvas ativos que usam o LinkedIn exibirão erros, e a Braze não conseguirá sincronizar os usuários.

### Etapa 2: Configurar os critérios de entrada do Canvas {#step-2-configure-your-canvas-entry-criteria}

Ao criar públicos para rastreamento de anúncios, pode ser útil incluir ou excluir determinados usuários com base em suas preferências e para cumprir leis de privacidade, como o direito de "Não vender ou compartilhar" previsto na [CCPA](https://oag.ca.gov/privacy/ccpa). Os profissionais de marketing devem implementar os filtros relevantes de elegibilidade dos usuários dentro dos critérios de entrada do Canvas. As opções a seguir podem ajudar.

Se você coletou o [IDFA do iOS pelo SDK da Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection), é possível usar o filtro **Ads Tracking Enabled**. Selecione o valor como `true` para enviar apenas usuários que aceitaram o rastreamento para os destinos de Audience Sync. IDs de publicidade do iOS não são compatíveis como campos de correspondência para o LinkedIn Audience Sync.

![Um público de entrada com o filtro "Ad Tracking Enabled is true".]({% image_buster /assets/img/linkedin/linkedin5.png %}){: style="max-width:75%;"}

Se você estiver coletando `opt-ins`, `opt-outs`, `Do Not Sell Or Share` ou quaisquer outros atributos personalizados relevantes, inclua-os nos critérios de entrada do Canvas como filtro:

![Um Canvas com público de entrada "opted_in_marketing" igual a "true".]({% image_buster /assets/img/linkedin/linkedin4.png %}){: style="max-width:75%;"}

Para saber mais sobre como cumprir essas leis de proteção de dados na plataforma Braze, consulte [Assistência técnica de proteção de dados]({{site.baseurl}}/dp-technical-assistance).

### Etapa 3: Adicionar uma etapa de Audience Sync com o LinkedIn {#step-3-add-an-audience-sync-step-with-linkedin}

Adicione um componente ao seu Canvas e selecione Audience Sync. Clique no botão **Custom Audience** para abrir o editor do componente.

### Etapa 4: Configuração da sincronização {#step-4-sync-setup}

1. Selecione **LinkedIn** como o parceiro de Audience Sync desejado.
2. Selecione a conta de anúncios do LinkedIn desejada.
3. No menu suspenso **Choose a New or Existing Audience**, digite o nome de um público novo ou existente.

{% tabs %}
{% tab Criar um novo público %}

#### Criar um novo público {#create-a-new-audience}

Insira um nome para o novo público, selecione **Add Users to Audience** e escolha quais campos você deseja sincronizar com o LinkedIn. Para esta integração, a Braze atualmente oferece suporte ao seguinte:
- E-mail
- Nome e sobrenome (ambos são obrigatórios quando você usa correspondência por nome)
- Android GAID

IDs de publicidade do iOS não são compatíveis como campos de correspondência para o LinkedIn.

Em seguida, salve seu público clicando no botão **Create Audience** na parte inferior do editor de etapas.

![Um exemplo de público "leads" com a conta de anúncios da Braze selecionada, o público "leads", a ação de adicionar usuários ao público e e-mail, Android GAID e nome e sobrenome como campos de correspondência.]({% image_buster /assets/img/linkedin/linkedin10.png %})

A Braze exibe uma notificação no topo do editor de etapas caso o público seja criado com sucesso ou se ocorrerem erros. Você pode referenciar esse público para remoção de usuários posteriormente na jornada do Canvas, depois de salvá-lo no editor de etapas.

![Confirmação de que o público "leads" foi criado.]({% image_buster /assets/img/linkedin/linkedin9.png %})

Quando você inicia um Canvas com um novo público, a Braze sincroniza os usuários à medida que eles entram na etapa de Audience Sync, sujeito ao [processamento em lote e latência]({{site.baseurl}}/partners/canvas_audience_sync/overview#batching-and-latency).

{% endtab %}
{% tab Sincronizar com um público existente %}

#### Sincronizar com um público existente {#sync-with-an-existing-audience}

A Braze também oferece a possibilidade de adicionar ou remover usuários de públicos existentes do LinkedIn para garantir que esses públicos estejam atualizados. Para sincronizar com um público existente, digite o nome do público existente no menu suspenso e escolha **Add to the Audience** ou **Remove from the Audience**. A Braze sincroniza os usuários à medida que eles entram na etapa de Audience Sync, sujeito ao [processamento em lote e latência]({{site.baseurl}}/partners/canvas_audience_sync/overview#batching-and-latency).

![Visualização expandida da etapa Custom Audience do Canvas. Aqui, a conta de anúncios desejada e o público existente estão selecionados.]({% image_buster /assets/img/linkedin/linkedin17.png %})

{% endtab %}
{% endtabs %}

### Etapa 5: Iniciar o Canvas {#step-5-launch-canvas}

Depois de configurar o Audience Sync com o LinkedIn, inicie o Canvas! O novo público será criado, e os usuários que passarem pela etapa de Audience Sync serão adicionados a esse público no LinkedIn. Se o seu Canvas contiver componentes subsequentes, os usuários avançarão para a próxima etapa da jornada.

Você pode visualizar o público no LinkedIn acessando sua conta de anúncios e selecionando **Audiences** na seção **Assets** da navegação. Na página **Audiences**, é possível ver o tamanho de cada público após atingir mais de 300 membros.

![Página do LinkedIn listando as métricas a seguir para o público em questão.]({% image_buster /assets/img/linkedin/linkedin8.png %})

## Considerações sobre sincronização de usuários e limite de frequência {#user-syncing-and-rate-limit-considerations}

À medida que os usuários chegam à etapa de Audience Sync, a Braze os enfileira para agrupamento antes de enviá-los ao LinkedIn. Consulte [Agrupamento e latência]({{site.baseurl}}/partners/canvas_audience_sync/overview#batching-and-latency) para saber como a Braze despacha os lotes.

A Braze envia até 2.000 usuários por solicitação ao LinkedIn. Se os limites de frequência da API do LinkedIn forem aplicados à sua conta, a Braze tenta novamente a sincronização por aproximadamente 13 horas. Se a sincronização ainda não for possível, a Braze lista esses usuários na métrica Users Errored.

## Entendendo a análise de dados {#understanding-analytics}

A tabela a seguir inclui métricas e descrições para ajudar você a entender melhor a análise de dados do seu componente de Audience Sync.

| MÉTRICA | DESCRIÇÃO |
| ------ | ----------- |
| Entered | Número de usuários que entraram neste componente para serem sincronizados com o LinkedIn. |
| Proceeded to Next Step | Quantos usuários avançaram para o próximo componente, se houver algum? Todos os usuários avançam automaticamente se esta for a última etapa da ramificação do Canvas. |
| Users Synced | Número de usuários que foram sincronizados com sucesso com o LinkedIn. |
| Users Not Synced | Número de usuários que não foram sincronizados devido à falta de campos para correspondência. |
| Users Pending | Número de usuários que estão sendo processados pela Braze para sincronização com o LinkedIn. |
| Users Errored | Número de usuários que não foram sincronizados com o LinkedIn devido a um erro de API após aproximadamente 13 horas de tentativas. Possíveis causas de erros podem incluir um token inválido do LinkedIn ou se o público foi excluído no LinkedIn. |
| Exited Canvas | Número de usuários que saíram do Canvas. Isso ocorre quando a última etapa de um Canvas é um componente de Audience Sync. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Entendendo a análise de dados" }

{% alert important %}
Lembre-se de que há um atraso no relatório das métricas de usuários sincronizados e usuários com erro devido ao agrupamento em lotes e às 13 horas de tentativas, respectivamente.
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

Confirme se sua conta de anúncios do LinkedIn foi conectada com sucesso à Braze na página de parceiro do LinkedIn. Em seguida, verifique se você selecionou uma conta de anúncios, inseriu um nome para o novo público e selecionou os campos para correspondência.

### Como sei se os usuários foram correspondidos após enviá-los ao LinkedIn? {#how-do-i-know-if-users-have-matched-after-passing-users-to-linkedin}

O LinkedIn fornece informações sobre taxas de correspondência no dashboard dele. Você pode verificar isso no LinkedIn na seção **Audiences**. Também é possível verificar a taxa de correspondência do seu público do LinkedIn nos detalhes da etapa do Canvas referente à etapa de Audience Sync.

### Quantos públicos o LinkedIn suporta? {#how-many-audiences-can-linkedin-support}

Atualmente, não há limite para o número de públicos na sua conta de anúncios do LinkedIn.

### Por que um segmento está preso no status BUILDING e não é atualizado? {#why-is-a-segment-stuck-in-building-status-and-not-updated}

Um segmento é considerado não utilizado e definido como ARCHIVED quando não é usado continuamente por 30 dias em uma campanha ativa ou em rascunho. Por causa disso, um segmento pode parecer "preso" em BUILDING quando atualizações são transmitidas para um segmento ARCHIVED, empurrando-o para o estado BUILDING, e logo antes de ser arquivado novamente, novas atualizações são transmitidas para o segmento não utilizado.