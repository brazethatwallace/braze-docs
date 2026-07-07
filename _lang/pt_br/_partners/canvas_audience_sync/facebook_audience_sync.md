---
nav_title: Facebook
article_title: Sincronização de público do Canvas com o Facebook
description: "Este artigo de referência aborda como usar o Braze Audience Sync para o Facebook para veicular anúncios com base em disparadores comportamentais, segmentação e muito mais."
page_order: 2
alias: /audience_sync_facebook/

tool:
  - Canvas

---

# Sincronização de público com o Facebook {#audience-sync-to-facebook}

> Usando o Braze Audience Sync to Facebook, você pode optar por adicionar os dados de seus próprios usuários da integração da Braze aos públicos personalizados do Facebook para veicular anúncios com base em disparadores comportamentais, segmentação e muito mais.

Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS ou webhook) em um Braze Canvas com base nos dados do seu usuário agora pode ser usado para disparar um anúncio para esse usuário no Facebook usando públicos personalizados. Por exemplo, ao configurar uma sincronização de público com o Facebook, é possível usar uma ampla variedade de campos primários, como e-mail, telefone, nome e sobrenome.

**Os casos de uso comuns para a sincronização de públicos personalizados incluem**:

- Direcionamento de usuários de alto valor com vários canais para impulsionar compras ou engajamento.
- Redirecionamento de usuários que são menos responsivos a outros canais de marketing.
- Criação de públicos de supressão para evitar que os usuários recebam anúncios quando já são consumidores fiéis da sua marca.
- Criação de públicos semelhantes para adquirir novos usuários com mais eficiência.

Esse recurso permite que as marcas controlem quais dados primários específicos são compartilhados com o Facebook. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

## Considerações sobre sincronização de usuários e limite de taxa {#user-syncing-and-rate-limit-considerations}

À medida que os usuários atingem a etapa de sincronização de público, a Braze os sincroniza quase em tempo real, respeitando os limites de taxa da API de marketing do Facebook. A Braze agrupa e processa o maior número possível de usuários a cada 5 segundos antes de enviá-los ao Facebook.

O limite de taxa da API de marketing do Facebook não permite mais do que &#126;190.000 solicitações de API por conta de anúncio em um período de uma hora. Se um cliente atingir esse limite, a Braze tentará novamente a sincronização por até &#126;13 horas. Se a sincronização ainda não for possível, a Braze listará esses usuários na métrica Usuários com erro.

## Pré-requisitos {#prerequisites}

Você precisará confirmar que os itens a seguir foram criados e concluídos antes de configurar a etapa do Facebook Audience no Canvas.

| Requisito | Origin | Descrição |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook](https://www.facebook.com/business/help/113163272211510) | Uma ferramenta centralizada para gerenciar os ativos do Facebook da sua marca (por exemplo, contas de anúncios, páginas e apps). |
| Conta de anúncio do Facebook | [Facebook](https://www.facebook.com/business/help/910137316041095) | Uma conta de anúncio ativa do Facebook vinculada ao gerente de negócios da sua marca.<br><br>Certifique-se de que o administrador do Facebook Business Manager tenha concedido permissões de "Manage Campaigns" ou "Manage ad accounts" para as contas de anúncios do Facebook que você planeja usar com a Braze. Além disso, verifique se você aceitou os termos e condições da sua conta de anúncios. |
| Termos de públicos personalizados do Facebook | [Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Aceite os Termos de Públicos Personalizados do Facebook para as contas de anúncios do Facebook que você planeja usar com a Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Prerequisites" }

## Integração {#integration}

### Etapa 1: Conecte-se ao Facebook {#step-1-connect-to-facebook}

{% alert important %}
Você deve ter a [permissão "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions/#admin) para conectar o Facebook à sua conta da Braze.
{% endalert %}

No dashboard da Braze, acesse **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Facebook**. Em Facebook Audience Export, selecione **Connect Facebook**.

![Página de tecnologia do Facebook na Braze que inclui uma seção de Visão geral e uma seção de Exportação de público do Facebook com o botão Connect Facebook.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:85%;"}

Uma janela de diálogo do Facebook oAuth é exibida para autorizar a Braze a criar públicos personalizados em suas contas de anúncios do Facebook.

![A primeira caixa de diálogo do Facebook solicitando "Conectar como X", em que X é seu nome de usuário do Facebook.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![A segunda caixa de diálogo do Facebook solicitando permissão para gerenciar anúncios para suas contas de anúncios.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

Depois de vincular a Braze à sua conta do Facebook, selecione as contas de anúncios que deseja sincronizar no seu espaço de trabalho da Braze. Quando estiver conectado, você será levado de volta à página do parceiro, onde poderá ver quais contas estão conectadas e desconectar contas existentes.

![Uma versão atualizada da página de parceiros de tecnologia do Facebook mostrando as contas de anúncios conectadas com sucesso.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:85%;"}

Sua conexão com o Facebook é aplicada no nível do espaço de trabalho da Braze. Se o administrador do Facebook remover você do seu Facebook Business Manager ou o acesso às contas do Facebook conectadas, a Braze detectará um token inválido. Como resultado, seus Canvas ativos usando componentes do público do Facebook mostrarão erros, e a Braze não poderá sincronizar usuários.

{% alert important %}
Para clientes que já passaram pelo processo de Revisão de App do Facebook para [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) e [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard), seu Token de Usuário do Sistema ainda será válido para o componente de público do Facebook. Não será possível editar ou revogar o Token de Usuário do Sistema do Facebook por meio da página de parceiro do Facebook. Em vez disso, você pode conectar sua conta do Facebook para substituir seu Token de Usuário do Sistema do Facebook dentro do seu espaço de trabalho da Braze.

<br><br>A configuração do Facebook oAuth também se aplicará às [exportações do Facebook usando Segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites).
{% endalert %}

### Etapa 2: Aceitar os termos de serviço de públicos personalizados {#step-2-accept-custom-audiences-terms-of-service}

Antes de criar seu Canvas, você deve aceitar os seguintes termos de serviço do Facebook nos links a seguir:

- **Termos de públicos personalizados de lista de clientes para sua conta pessoal:** `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- **Termos das ferramentas comerciais do Facebook para sua conta comercial:** `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

![Um exemplo dos termos a serem aceitos para públicos personalizados de lista de clientes.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}){: style="max-width:85%;"}
![Um exemplo dos termos a serem aceitos para as ferramentas de negócios do Facebook.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}){: style="max-width:85%;"}

Consulte a [seção de perguntas frequentes](#terms) para obter mais detalhes sobre a auditoria da sua conta do Facebook durante a integração.

### Etapa 3: Adicionar um componente do público do Facebook no Canvas {#step-3-add-a-facebook-audience-component-in-canvas}

Adicione um componente no seu Canvas e selecione **Facebook Audience**.

![Uma lista de componentes a serem adicionados ao Canvas.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![O componente Audience Sync.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Etapa 4: Configuração de sincronização {#step-4-sync-setup}

Selecione o botão **Custom Audience** para abrir o editor de componentes. Em seguida, selecione **Facebook** como parceiro do Audience Sync.

!["Set up Audience Sync" com opções para escolher um parceiro.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Selecione a conta de anúncio do Facebook desejada. No menu suspenso **Choose a New or Existing Audience**, digite o nome de um público novo ou existente.

{% tabs %}
{% tab Create a New Audience %}

1. Digite um nome para o novo público personalizado.
2. Selecione **Add Users to Audience** e escolha os campos que deseja sincronizar com o Facebook.
3. Em seguida, selecione **Create Audience** para salvar seu público.

![Configuração de sincronização de público para um público com as informações de e-mail, telefone, nome e sobrenome correspondentes.]({% image_buster /assets/img/audience_sync/fb_sync.png %})

Você será notificado na parte superior do editor de etapas se o público for criado com êxito ou se ocorrer um erro durante esse processo. Também é possível fazer referência a esse público para remoção de usuários posteriormente na jornada do Canvas, pois o público foi criado no modo de rascunho.

Ao lançar um Canvas com um novo público, a Braze criará o novo público personalizado ao lançar o Canvas e, posteriormente, sincronizará os usuários quase em tempo real quando eles entrarem na etapa do Audience Sync.

{% endtab %}
{% tab Sync with an Existing Audience %}

A Braze oferece a capacidade de adicionar ou remover usuários de públicos personalizados existentes do Facebook para confirmar que esses públicos estão atualizados. Para sincronizar com um público existente, faça o seguinte:

1. Digite o nome do público existente no menu suspenso.
2. Escolha se você deseja **Add to the Audience** ou **Remove from the Audience**.
3. A Braze adicionará ou removerá usuários quase em tempo real quando eles entrarem na etapa de público do Facebook.

![Configuração da sincronização do público para remover as informações de e-mail, telefone, nome e sobrenome.]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
O Facebook proíbe a remoção de usuários de públicos personalizados quando o tamanho do público é muito baixo (normalmente, menos de 1.000 usuários). Como resultado, a Braze não consegue sincronizar usuários para uma remoção da etapa de sincronização de público até que o público atinja o tamanho apropriado.
{% endalert %}

{% endtab %}
{% endtabs %}

### Etapa 5: Lançar Canvas {#step-5-launch-canvas}

Depois de configurar seu componente do público do Facebook, é hora de lançar o Canvas! O novo público personalizado é criado, e os usuários que passam pela etapa do Facebook Audience são transferidos para esse público personalizado no Facebook. Se o seu Canvas contiver etapas subsequentes, seus usuários avançarão para a próxima etapa da jornada do usuário.

A guia **History** do público personalizado no Facebook Audience Manager refletirá o número de usuários enviados para o público pela Braze. Se um usuário entrar novamente na etapa, ele será enviado ao Facebook novamente.

![Detalhes do público e a guia History para um determinado público do Facebook, com uma tabela de histórico do público com colunas de atividade, detalhes da atividade, itens alterados e data e hora.]({% image_buster /assets/img/fb_audience_sync/audience_history.png %}){: style="max-width:80%;"}

## Compreensão da análise de dados {#understanding-analytics}

A tabela a seguir inclui métricas e descrições para ajudá-lo a entender melhor a análise de dados do seu componente Audience Sync.

| Métrica | Descrição |
| --- | --- |
| Entraram | Número de usuários que entraram neste componente para serem sincronizados com o Facebook. |
| Avançaram para a etapa seguinte | Quantos usuários avançaram para o próximo componente, se houver um. Todos os usuários avançarão automaticamente se essa for a última etapa da ramificação do Canvas. |
| Usuários sincronizados | Número de usuários que foram sincronizados com sucesso com o Facebook. |
| Usuários não sincronizados | Número de usuários que não foram sincronizados devido à falta de campos para correspondência. Os campos são correspondidos usando um operador "OR", o que significa que, desde que um usuário tenha um dos campos no Facebook, o Facebook corresponderá o usuário mesmo que não haja correspondência em todos os outros campos. |
| Usuários pendentes | Número de usuários atualmente sendo processados pela Braze para sincronizar com o Facebook. |
| Usuários com erro | Número de usuários que não foram sincronizados com o Facebook devido a um erro de API após cerca de 13 horas de tentativas. As possíveis causas de erros podem incluir um token inválido do Facebook ou a exclusão do público personalizado no Facebook. |
| Saíram do Canvas | Número de usuários que saíram do Canvas. Isso ocorre quando a última etapa de um Canvas é uma etapa do Facebook. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Understanding analytics" }

{% alert important %}
Há um atraso nos relatórios de métricas de usuários sincronizados e usuários com erro devido ao processamento interno.
{% endalert %}

## Perguntas frequentes {#frequently-asked-questions}

### Quanto tempo leva para que meus públicos sejam preenchidos no dashboard de parceiro do Audience Sync? {#how-long-does-it-take-for-my-audiences-to-populate-in-my-audience-sync-partner-dashboard}

O tempo necessário para preencher um público depende do parceiro específico. Todas as redes processarão as solicitações da Braze e tentarão combinar os usuários. Pode levar até 24 horas para que os públicos personalizados sejam atualizados.

### O que devo fazer em seguida se receber um erro de token inválido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Você pode simplesmente desconectar e reconectar sua conta do Facebook na página de parceiros do Facebook. Confirme com seu administrador do Facebook Business Manager que você tem as permissões apropriadas para a conta de anúncios com a qual deseja sincronizar.

### Por que meu Canvas não pode ser iniciado? {#why-is-my-canvas-not-allowed-to-launch}

- Certifique-se de que o token de usuário do sistema esteja autenticado e tenha acesso às contas de anúncios desejadas no Facebook Business Manager.
- Certifique-se de ter selecionado uma conta de anúncios, inserido um nome para o novo público personalizado e selecionado os campos correspondentes.
- Você pode ter atingido o limite de 500 públicos personalizados no Facebook. Acesse o Facebook Audience Manager para excluir alguns públicos desnecessários antes de criar novos públicos personalizados usando o Canvas.

### Como posso saber se os usuários foram correspondidos depois de passá-los para o Facebook? {#how-do-i-know-if-users-have-matched-after-passing-users-to-facebook}

O Facebook não fornece essas informações por motivos de privacidade.

### A Braze oferece suporte a públicos personalizados baseados em valor? {#does-braze-support-value-based-custom-audiences}

No momento, os públicos personalizados baseados em valor não são suportados pela Braze. Se você estiver interessado em sincronizar esses tipos de públicos personalizados, envie [feedback de produto]({{site.baseurl}}/user_guide/administer/personal/product_portal/).

### A Braze faz hash dos dados antes de enviá-los aos parceiros do Audience Sync? {#does-braze-hash-data-before-sending-it-to-audience-sync-partners}

Depois que os dados de e-mail são normalizados, a Braze faz o hash com SHA256.

**IDFA/AAID/telefone:** A Braze faz o hash com SHA256. Os tipos de público com os quais sincronizamos são sempre um dos seguintes:

- IDFA_SHA256
- AAID_SHA256
- EMAIL_SHA256
- PHONE_SHA256.

Em termos de frequência, a Braze só fará o hash das informações de identificação pessoal (IPI) do usuário quando os usuários entrarem na etapa de sincronização de público na jornada do usuário em preparação para a sincronização.

### Como faço para resolver um problema com a sincronização de um público personalizado semelhante baseado em valor? {#how-do-i-resolve-an-issue-with-syncing-a-value-based-lookalike-custom-audience}

No momento, os públicos personalizados semelhantes baseados em valor não são suportados pela Braze. Se você tentar sincronizar com esse público, isso pode causar erros na sua etapa de Audience Sync. Para resolver isso, siga estas etapas:

1. Acesse seu dashboard do Facebook Ad Manager e selecione **Audiences**.
2. Selecione **Create audience** > **Custom audience**.
3. Selecione **Customer list**.
4. Faça upload do seu CSV ou lista sem a coluna **Value**. Selecione **No, continue with a customer list that doesn't include customer value**.
5. Conclua a criação do seu público personalizado.
6. Na Braze, atualize a etapa Facebook Audience Sync com o público personalizado que você criou.

### Recebi um e-mail relacionado aos termos de serviço do público personalizado do Facebook. O que devo fazer para resolver isso? {#ive-received-an-email-related-to-facebook-custom-audience-terms-of-service-what-should-i-do-to-resolve-this}

Para usar o Audience Sync com o Facebook, você deve aceitar estes termos do contrato de serviço.

- Se a sua conta de anúncios estiver diretamente associada à sua conta pessoal do Facebook, você poderá aceitar os termos de serviço da sua conta pessoal aqui: `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- Se a sua conta de anúncios estiver vinculada à conta do Business Manager da sua empresa, você deverá aceitar os termos de serviço na sua conta do Facebook Business Manager aqui: `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

Depois de aceitar os termos de serviço do público personalizado do Facebook, faça o seguinte:

1. Atualize seu token de acesso do Facebook com a Braze desconectando e reconectando sua conta do Facebook.
2. Reative sua etapa de sincronização do público do Facebook editando e atualizando seu Canvas.

A partir daí, a Braze poderá sincronizar os usuários assim que eles chegarem à etapa de sincronização de público do Facebook.

### O que aconteceu com os filtros **Connected Facebook** e **Number of Facebook Friends Using App**? {#what-happened-to-the-connected-facebook-and-number-of-facebook-friends-using-app-filters}

Os filtros de segmentação da Braze **Number of Facebook Friends Using App** e **Connected Facebook** foram descontinuados. O Facebook e os SDKs da Braze não coletam mais os dados subjacentes nos quais esses filtros se baseavam.

Substitua os filtros descontinuados por atributos personalizados, eventos personalizados ou segmentos baseados em engajamento — por exemplo, login do Facebook ou vinculação social em vez de **Connected Facebook**, ou indicações, convites e compartilhamentos em vez de **Number of Facebook Friends Using App**.

Para redirecionamento no Canvas, combine os usuários com e-mail, telefone, nome e sobrenome, conforme demonstrado na [Etapa 4: Configuração de sincronização](#step-4-sync-setup). Para ampliar o alcance, sincronize um segmento de alto valor com o Facebook e crie um público semelhante no Meta Ads Manager.

## Solução de problemas {#troubleshooting}

<style>
table th:nth-child(1) {
    width: 20%;
}
table th:nth-child(2) {
    width: 40%;
}
table th:nth-child(2) {
    width: 40%;
}
table td {
    word-break: break-word;
}
</style>

<table aria-label="Solução de problemas">
  <thead>
    <tr>
      <th>Erro</th>
      <th>Descrição</th>
      <th>Etapas para resolver</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><b>Token inválido</b></td>
      <td>As causas típicas incluem o usuário que conectou a integração alterar sua senha, as credenciais expirarem e outros.</td>
      <td>Acesse <b>Integrações de parceiros</b> > <b>Facebook</b> e desconecte e reconecte sua conta. Consulte <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>esta seção de solução de problemas</a> para obter etapas adicionais para auditar sua conta do Facebook.</td>
    </tr>
    <tr>
      <td><b>Tamanho do público muito baixo</b></td>
      <td>Esse erro pode ocorrer se você tiver criado uma etapa de Audience Sync que remove usuários de seus públicos. Se o tamanho do seu público se aproximar de zero, a rede poderá sinalizar que o tamanho do público é muito pequeno para ser atendido.</td>
      <td>Use uma estratégia de sincronização de público que adicione e remova usuários regularmente, de modo a não esgotar totalmente o tamanho do público.</td>
    </tr>
    <tr>
      <td><b>O público não existe</b></td>
      <td>A etapa Audience Sync usa um público que não existe ou foi excluído. Isso também pode ser disparado se você não tiver mais a permissão necessária para acessar o público.</td>
      <td>Peça a um administrador para verificar na plataforma do parceiro se o público ainda existe. <br><br>Se existir, confirme se o usuário que conectou a integração tem permissão para o público. Caso contrário, o usuário deve receber acesso a esse público. <br><br>Se o público tiver sido removido intencionalmente, adicione um público ativo e crie um novo público na etapa.</td>
    </tr>
    <tr>
      <td><b>Tentativa de acesso à conta de anúncios</b></td>
      <td>Você não tem permissões para a conta de anúncios ou o público selecionado.</td>
      <td>Trabalhe com os administradores da sua conta de anúncios para obter acesso e permissões adequados.</td>
    </tr>
    <tr>
      <td><b>Termos de serviço não aceitos</b></td>
      <td>Para alguns destinos do Audience Sync, como o Facebook, a rede de anúncios exige que você aceite termos de serviço específicos para usar o recurso Audience Sync. Esse erro será disparado se você não tiver aceitado os termos apropriados. Como resultado, você também pode ter recebido um e-mail da Braze com o assunto: "Suas credenciais de autorização para o Facebook são inválidas."</td>
      <td>Verifique se você aceitou os termos exigidos pelo Facebook.</td>
    </tr>
    <tr>
      <td><b>Todos os usuários estão apresentando erros</b></td>
      <td>Se todos os usuários apresentarem erros em uma etapa, apesar de confirmar que esses usuários têm valores para os campos selecionados na etapa, isso pode indicar um problema com a sua conta do Facebook.</td>
      <td>Siga as etapas <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>desta seção de solução de problemas</a> para verificar se há algum problema na sua conta.
      </td>
    </tr>
    <tr>
      <td><b>Falha ao criar público</b></td>
      <td>Na página Parceiro de tecnologia do Facebook, você está vendo "Conectado", mas há um erro na etapa Sincronização de público do Facebook ao sincronizar um público: "Falha ao criar o público 'nome do público'". A autorização da sua conta do Facebook falhou. Visite a página Parceiros de tecnologia para reconectar sua conta.</td>
      <td>Siga as etapas <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-facebook-account'>desta seção de solução de problemas</a> para verificar se há algum problema na sua conta.
      </td>
    </tr>
    <tr>
      <td><b>Conta de anúncios ausente no menu suspenso</b></td>
      <td>Ao configurar a etapa Facebook Audience, uma conta de anúncios esperada não aparece no seletor de contas de anúncios.</td>
      <td>Confirme se o seu app do Facebook concluiu a <a href="https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management">Revisão de App</a> para <code>ads_management</code> com o nível de acesso que o Facebook exige para uso da API de marketing. No <a href="https://business.facebook.com/">Facebook Business Manager</a>, confirme se o token de usuário do sistema tem as permissões corretas e está associado às contas de anúncios que você usa na Braze, e se os termos da conta de anúncios foram aceitos. <br><br>Se o menu suspenso funcionar em um novo Canvas, mas não em um Canvas que você já editou, tente atualizar o navegador (ou limpar o cache) e confirme se você está conectado como um usuário que ainda tem acesso a essas contas de anúncios.</td>
    </tr>
    <tr>
      <td><b>Erro ao validar o token de acesso</b></td>
      <td>Você vê um erro sobre a validação do token de acesso do Facebook ao conectar a Braze ao Facebook ou ao sincronizar públicos.</td>
      <td>Saia do Facebook no seu navegador. Na Braze, acesse <b>Integrações de parceiros</b> &gt; <b>Facebook</b>, remova as credenciais salvas do Facebook e conecte o Facebook novamente. Na página de Parceiros de tecnologia do Facebook para a Braze, desconecte e reconecte a integração, se a opção estiver disponível. <br><br>Se os problemas continuarem, siga <a href="#audit-your-facebook-account">Audite sua conta do Facebook</a>.</td>
    </tr>
    <tr>
      <td><b>Erros de permissão de exportação ou sincronização de público</b></td>
      <td>A exportação ou sincronização de um público do Facebook falha com erros de autorização, administrador ou conta de anúncios.</td>
      <td>No <a href="https://developers.facebook.com/">Meta for Developers</a>, abra seu app e confirme se o seu usuário tem uma função de <b>Admin</b> em <b>App roles</b>. Em <b>App settings</b> &gt; <b>Advanced</b>, confirme se <b>Advertising accounts</b> inclui as contas que você usa com a Braze. Em <a href="https://business.facebook.com/latest/settings">Business settings</a>, confirme se o usuário que está conectando ou o usuário do sistema tem acesso à conta de anúncios correta.</td>
    </tr>
  </tbody>
</table>

### Audite sua conta do Facebook {#audit-your-facebook-account}

Se tiver problemas adicionais com a integração, consulte as seções e etapas a seguir para auditar sua conta do Facebook.

#### Revisar as permissões da conta {#review-account-permissions}

1. Consulte [a documentação do Facebook](https://www.facebook.com/business/help/186007118118684?id=829106167281625) sobre como gerenciar essas permissões na plataforma. Para o Facebook Business Manager, você precisa, no mínimo, de uma função de **Admin** ou **Employee** no Business Manager com acesso às contas de anúncios necessárias.
2. Como **Employee**, confirme se o administrador concede a você permissões completas de **Manage Ad Account** para cada conta de anúncios para criar um público ou sincronizar usuários com o público.
3. Depois que isso for concedido, você deverá desconectar e reconectar sua conta.

#### Aceitar os termos de serviço {#terms}

Aceite quaisquer Termos de Serviço (TOS) pendentes do Facebook. O Facebook solicitará periodicamente que você (o usuário) e o gerente de negócios aprovem novamente os termos de serviço.

1. O usuário conectado precisa aceitar todos os termos de serviço de cada uma de suas contas de anúncios:
- Termos de serviço do público personalizado para sua conta pessoal do Facebook:
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`

![Uma conta com permissões de controle total para gerenciar uma conta de anúncios.]({% image_buster /assets/img/fb_audience_sync/ad_account_permission.png %}){: style="max-width:70%;"}

Para encontrar sua conta e ID comercial, siga estas etapas:

1. Acesse sua [conta do Facebook Ads Manager](https://adsmanager.facebook.com/).
2. Confirme que está usando a conta de anúncios correta verificando-a no menu suspenso.
3. No URL, localize o ID da conta após `act=` e o ID da empresa após `business_id=`

![O URL com o ID da conta e o ID da empresa destacados.]({% image_buster /assets/img/fb_audience_sync/fb_businessid_url.png %}){: style="max-width:90%;"}

{:start="4"}

4. Leia e selecione **Accept** para os Termos do público personalizado. Recomendamos confirmar para qual conta os termos de serviço estão sendo assinados usando o menu suspenso na parte superior dos termos.

![O menu suspenso que mostra a conta que está assinando os termos de serviço.]({% image_buster /assets/img/fb_audience_sync/confirm_accept_tos.png %}){: style="max-width:90%;"}

{:start="5"}
5. Você deve selecionar **Accept** para os termos de serviço. Depois, você verá esta mensagem: "You have accepted these terms of service on behalf of Braze".
6. Atualize seu token de acesso do Facebook com a Braze desconectando e reconectando sua conta do Facebook.
7. Reative sua etapa de sincronização do público do Facebook editando e atualizando seu Canvas. A partir daí, a Braze poderá sincronizar os usuários assim que eles chegarem à etapa de público do Facebook.
8. Se o problema persistir, tente usar um usuário separado com permissões de administrador para aceitar manualmente os termos por meio do Ads Manager.

#### Concluir todas as tarefas pendentes {#complete-any-pending-tasks}

Verifique se você tem alguma tarefa pendente com o Facebook que possa estar bloqueando o uso dos serviços do Facebook Ads:

1. [Faça login no Facebook Ads Manager](https://adsmanager.facebook.com/).
2. Selecione a conta de anúncios com a qual você está tendo problemas.
3. Na navegação, selecione **Account Overview**. <br> ![A navegação com Account Overview selecionada.]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %})
4. Verifique se há algum alerta que precise ser resolvido. <br> ![Uma conta com um cartão de crédito expirado.]({% image_buster /assets/img/fb_audience_sync/resolve_alerts.png %})

{:start="5"}

5. Verifique se há alguma tarefa de configuração que precise ser concluída. <br> ![Uma conta com uma configuração de conta parcialmente concluída.]({% image_buster /assets/img/fb_audience_sync/confirm_tasks.png %})

#### Conecte-se com um usuário diferente {#connect-with-a-different-user}

Como outra etapa de solução de problemas, recomendamos que um usuário administrador diferente tente conectar sua conta fazendo o seguinte:

1. Desconecte a integração atual.
2. Um usuário separado com permissões de administrador conecta sua conta de usuário do Facebook.