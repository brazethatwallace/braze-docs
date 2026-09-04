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

Qualquer critério que você normalmente usaria para disparar uma mensagem (push, e-mail, SMS ou webhook) em um BRAZE CANVAS com base nos dados do seu usuário agora pode ser usado para disparar um anúncio para esse usuário no Facebook usando públicos personalizados. Por exemplo, ao configurar uma sincronização de público com o Facebook, é possível usar uma ampla variedade de campos primários, como e-mail, telefone, nome e sobrenome.

**Os casos de uso comuns para a sincronização de públicos personalizados incluem**:

- Direcionamento de usuários de alto valor com vários canais para impulsionar compras ou engajamento.
- Redirecionamento de usuários que são menos responsivos a outros canais de marketing.
- Criação de públicos de supressão para evitar que os usuários recebam anúncios quando já são consumidores fiéis da sua marca.
- Criação de públicos semelhantes para adquirir novos usuários com mais eficiência.

Esse recurso permite que as marcas controlem quais dados primários específicos são compartilhados com o Facebook. Na Braze, as integrações com as quais você pode e não pode compartilhar seus dados primários recebem a máxima consideração. Para saber mais, consulte nossa [política de privacidade](https://www.braze.com/privacy).

## Sincronização de usuários e considerações sobre limite de frequência {#user-syncing-and-rate-limit-considerations}

À medida que os usuários chegam à etapa de Audience Sync, a Braze os sincroniza em tempo quase real, respeitando os limites de frequência da API de Marketing do Facebook. A Braze agrupa e processa o maior número possível de usuários a cada 5 segundos antes de enviá-los ao Facebook.

O limite de frequência da API de Marketing do Facebook permite no máximo &#126;190.000 solicitações de API por conta de anúncio em um período de uma hora. Se um cliente atingir esse limite, a Braze tentará novamente a sincronização por até &#126;13 horas. Se a sincronização ainda não for possível, a Braze listará esses usuários na métrica Users Errored.

## Pré-requisitos {#prerequisites}

Você precisará confirmar que os itens a seguir foram criados e concluídos antes de configurar sua etapa de público do Facebook no Canvas.

| Requisito | Origin | Descrição |
| ----------- | ------ | ----------- |
| Facebook Business Manager | [Facebook](https://www.facebook.com/business/help/113163272211510) | Uma ferramenta centralizada para gerenciar os ativos do Facebook da sua marca (por exemplo, contas de anúncios, páginas e apps). |
| Conta de anúncios do Facebook | [Facebook](https://www.facebook.com/business/help/910137316041095) | Uma conta de anúncios do Facebook ativa vinculada ao gerenciador de negócios da sua marca.<br><br>Certifique-se de que o administrador do seu Facebook Business Manager concedeu a você as permissões "Manage Campaigns" ou "Manage ad accounts" para as contas de anúncios do Facebook que você planeja usar com a Braze. Além disso, certifique-se de que você aceitou os termos e condições da sua conta de anúncios. |
| Termos de Públicos Personalizados do Facebook | [Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Aceite os Termos de Públicos Personalizados do Facebook para as contas de anúncios do Facebook que você planeja usar com a Braze. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Conectar ao Facebook {#step-1-connect-to-facebook}

{% alert important %}
Você deve ter a [permissão "Admin"]({{site.baseurl}}/user_guide/administrative/app_settings/manage_your_braze_users/user_permissions#admin) para conectar o Facebook à sua conta da Braze.
{% endalert %}

No dashboard da Braze, acesse **Integrações com Parceiros** > **Parceiros de Tecnologia** e selecione **Facebook**. Em Facebook Audience Export, selecione **Connect Facebook**.

![Página de tecnologia do Facebook na Braze que inclui uma seção de visão geral e uma seção de exportação de público do Facebook com o botão Connect Facebook.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:85%;"}

Uma janela de diálogo oAuth do Facebook aparecerá para autorizar a Braze a criar públicos personalizados nas suas contas de anúncios do Facebook.

![A primeira caixa de diálogo do Facebook solicitando "Conectar como X", onde X é o seu nome de usuário do Facebook.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![A segunda caixa de diálogo do Facebook solicitando permissão para gerenciar anúncios das suas contas de anúncios.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

Após vincular a Braze à sua conta do Facebook, selecione as contas de anúncios que você deseja sincronizar dentro do seu espaço de trabalho da Braze. Quando estiver conectado, você será redirecionado para a página de parceiro, onde poderá visualizar quais contas estão conectadas e desconectar contas existentes.

![Uma versão atualizada da página de parceiros de tecnologia do Facebook mostrando as contas de anúncios conectadas com sucesso.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:85%;"}

Sua conexão com o Facebook é aplicada no nível do espaço de trabalho da Braze. Se o administrador do Facebook remover você do Facebook Business Manager ou do acesso às contas do Facebook conectadas, a Braze detectará um token inválido. Como resultado, seus Canvas ativos que usam componentes de público do Facebook mostrarão erros, e a Braze não conseguirá sincronizar usuários.

{% alert important %}
Para clientes que já passaram pelo processo de revisão de aplicativo do Facebook para [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) e [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard), seu token de usuário do sistema ainda será válido para o componente de público do Facebook. Você não poderá editar ou revogar o token de usuário do sistema do Facebook pela página de parceiro do Facebook. Em vez disso, você pode conectar sua conta do Facebook para substituir o token de usuário do sistema do Facebook dentro do seu espaço de trabalho da Braze.

<br><br>A configuração oAuth do Facebook também se aplicará às [exportações do Facebook usando Segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook#prerequisites).
{% endalert %}

### Etapa 2: Aceitar os termos de serviço de públicos personalizados {#step-2-accept-custom-audiences-terms-of-service}

Antes de criar seu Canvas, você deve aceitar os seguintes termos de serviço do Facebook nos links a seguir:

- **Termos de públicos personalizados de lista de clientes para sua conta pessoal:** `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- **Termos de ferramentas de negócios do Facebook para sua conta empresarial:** `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

![Um exemplo dos termos a serem aceitos para públicos personalizados de lista de clientes.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos.png %}){: style="max-width:85%;"}
![Um exemplo dos termos a serem aceitos para ferramentas de negócios do Facebook.]({% image_buster /assets/img/fb_audience_sync/fb_sync_tos2.png %}){: style="max-width:85%;"}

Consulte a [seção de perguntas frequentes](#terms) para mais detalhes sobre como auditar sua conta do Facebook durante a integração.

### Etapa 3: Adicionar um componente de público do Facebook no Canvas {#step-3-add-a-facebook-audience-component-in-canvas}

Adicione um componente no seu Canvas e selecione **Facebook Audience**.

![Uma lista de componentes para adicionar ao Canvas.]({% image_buster /assets/img/audience_sync/audience_sync3.png %}){: style="max-width:35%;"} ![O componente de sincronização de público.]({% image_buster /assets/img/audience_sync/audience_sync5.png %}){: style="max-width:28%;"}

### Etapa 4: Configuração da sincronização {#step-4-sync-setup}

Selecione o botão **Custom Audience** para abrir o editor do componente. Em seguida, selecione **Facebook** como parceiro de sincronização de público.

![Configuração de sincronização de público com opções para escolher um parceiro.]({% image_buster /assets/img/audience_sync/audience_sync4.png %}){: style="max-width:80%;"}

Selecione a conta de anúncios do Facebook desejada. No menu suspenso **Choose a New or Existing Audience**, digite o nome de um público novo ou existente.

{% tabs %}
{% tab Criar um novo público %}

1. Insira um nome para o novo público personalizado.
2. Selecione **Add Users to Audience** e escolha os campos que você deseja sincronizar com o Facebook.
3. Em seguida, selecione **Create Audience** para salvar seu público.

![Configuração de sincronização de público para um público com informações de e-mail, telefone, nome e sobrenome para correspondência.]({% image_buster /assets/img/audience_sync/fb_sync.png %})

Você será notificado no topo do editor da etapa se o público for criado com sucesso ou se ocorrer um erro durante esse processo. Você também pode referenciar esse público para remoção de usuários posteriormente na jornada do Canvas, pois o público foi criado em modo de rascunho.

Quando você lança um Canvas com um novo público, a Braze cria o novo público personalizado ao lançar o Canvas e, em seguida, sincroniza os usuários em tempo quase real à medida que eles entram na etapa de sincronização de público.

Cada etapa de sincronização de público é mapeada para o público do Facebook configurado naquela etapa. Quando o Canvas é executado novamente (por exemplo, em um cronograma recorrente), a Braze sincroniza os usuários elegíveis para o mesmo público — ela não cria um novo público do Facebook para cada execução do Canvas.

{% endtab %}
{% tab Sincronizar com um público existente %}

A Braze oferece a capacidade de adicionar ou remover usuários de públicos personalizados existentes do Facebook para garantir que esses públicos estejam atualizados. Para sincronizar com um público existente, faça o seguinte:

1. Digite o nome do público existente no menu suspenso.
2. Escolha se deseja **Add to the Audience** ou **Remove from the Audience**.
3. A Braze adicionará ou removerá usuários em tempo quase real à medida que eles entrarem na etapa de público do Facebook.

![Configuração de sincronização de público para remover informações de e-mail, telefone, nome e sobrenome.]({% image_buster /assets/img/audience_sync/fb_sync3.png %})

{% alert important %}
O Facebook proíbe a remoção de usuários de públicos personalizados quando o tamanho do público é muito pequeno (geralmente menos de 1.000 usuários). Como resultado, a Braze não consegue sincronizar usuários para remoção da etapa de sincronização de público até que o público atinja o tamanho adequado.
{% endalert %}

{% endtab %}
{% endtabs %}

### Etapa 5: Lançar o Canvas {#step-5-launch-canvas}

Após configurar seu componente de público do Facebook, é hora de lançar o Canvas! O novo público personalizado é criado, e os usuários que passarem pela etapa de público do Facebook serão adicionados a esse público personalizado no Facebook. Se o seu Canvas contiver etapas subsequentes, seus usuários avançarão para a próxima etapa na jornada do usuário.

A guia **History** do público personalizado no Facebook Audience Manager refletirá o número de usuários enviados para o público pela Braze. Se um usuário entrar novamente na etapa, ele será enviado ao Facebook novamente.

![Detalhes do público e a guia History de um determinado público do Facebook que inclui uma tabela de histórico do público com colunas para a atividade, detalhes da atividade, itens alterados e a data e hora.]({% image_buster /assets/img/fb_audience_sync/audience_history.png %}){: style="max-width:80%;"}

## Entendendo a análise de dados {#understanding-analytics}

A tabela a seguir inclui métricas e descrições para ajudar você a entender melhor a análise de dados do seu componente de Audience Sync.

| Métrica | Descrição |
| --- | --- |
| Entered | Número de usuários que entraram neste componente para serem sincronizados com o Facebook. |
| Proceeded to Next Step | Quantos usuários avançaram para o próximo componente, se houver um. Todos os usuários avançarão automaticamente se esta for a última etapa na Branch do Canvas. |
| Users Synced | Número de usuários que foram sincronizados com sucesso com o Facebook. |
| Users Not Synced | Número de usuários que não foram sincronizados devido à falta de campos para correspondência. Os campos são correspondidos usando um operador "OR", o que significa que, desde que um usuário tenha um dos campos no Facebook, o Facebook fará a correspondência do usuário mesmo que não haja correspondência em todos os outros campos. |
| Users Pending | Número de usuários que estão sendo processados pela Braze para sincronização com o Facebook. |
| Users Errored | Número de usuários que não foram sincronizados com o Facebook devido a um erro de API após cerca de 13 horas de tentativas. Possíveis causas de erros podem incluir um token inválido do Facebook ou se o público personalizado foi excluído no Facebook. |
| Exited Canvas | Número de usuários que saíram do Canvas. Isso ocorre quando a última etapa em um Canvas é uma etapa do Facebook. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Entendendo a análise de dados" }

{% alert important %}
Há um atraso no relatório das métricas de usuários sincronizados e usuários com erro devido ao processamento interno.
{% endalert %}

## Perguntas frequentes {#frequently-asked-questions}

### Quanto tempo leva para meus públicos serem preenchidos no dashboard do parceiro de Audience Sync? {#how-long-does-it-take-for-my-audiences-to-populate-in-my-audience-sync-partner-dashboard}

O tempo necessário para preencher um público depende do parceiro específico. Todas as redes processarão as solicitações da Braze e tentarão fazer a correspondência dos usuários. Pode levar até 24 horas para que os públicos personalizados sejam atualizados.

### O que devo fazer se receber um erro de token inválido? {#what-should-i-do-next-if-i-receive-an-invalid-token-error}

Você pode simplesmente desconectar e reconectar sua conta do Facebook na página de parceiro do Facebook. Confirme com o administrador do seu Facebook Business Manager que você tem as permissões apropriadas para a conta de anúncios com a qual deseja sincronizar.

### Por que meu Canvas não pode ser lançado? {#why-is-my-canvas-not-allowed-to-launch}

- Verifique se o token do usuário do sistema está autenticado e tem acesso às contas de anúncios desejadas no Facebook Business Manager.
- Verifique se você selecionou uma conta de anúncios, inseriu um nome para o novo público personalizado e selecionou campos para correspondência.
- Você pode ter atingido o limite de 500 públicos personalizados no Facebook. Acesse o Facebook Audience Manager para excluir alguns desnecessários antes de criar novos públicos personalizados usando o Canvas.

### Como sei se houve correspondência de usuários após enviá-los ao Facebook? {#how-do-i-know-if-users-have-matched-after-passing-users-to-facebook}

O Facebook não fornece essa informação por motivos de privacidade.

### A Braze oferece suporte a públicos personalizados baseados em valor? {#does-braze-support-value-based-custom-audiences}

No momento, públicos personalizados baseados em valor não são compatíveis com a Braze. {% multi_lang_include product_feedback_cta.md context="gap" feature="value-based custom audience sync" %}

### A Braze faz hash dos dados antes de enviá-los aos parceiros de Audience Sync? {#does-braze-hash-data-before-sending-it-to-audience-sync-partners}

Depois que os dados de e-mail são normalizados, a Braze aplica hash com SHA256.

**IDFA/AAID/telefone:** a Braze aplica hash com SHA256. Os tipos de público que sincronizamos são sempre um dos seguintes:

- IDFA_SHA256
- AAID_SHA256
- EMAIL_SHA256
- PHONE_SHA256.

Em termos de frequência, a Braze só aplica hash nas informações de identificação pessoal (IPI) dos usuários quando eles entram na etapa de Audience Sync na jornada do usuário, em preparação para a sincronização.

### Como resolvo um problema de sincronização de um público personalizado semelhante baseado em valor? {#how-do-i-resolve-an-issue-with-syncing-a-value-based-lookalike-custom-audience}

No momento, públicos personalizados semelhantes baseados em valor não são compatíveis com a Braze. Se você tentar sincronizar com esse público, isso pode causar erros na sua etapa de Audience Sync. Para resolver isso, siga estas etapas:

1. Acesse o dashboard do Facebook Ad Manager e selecione **Públicos**.
2. Selecione **Criar público** > **Público personalizado**.
3. Selecione **Lista de clientes**.
4. Faça upload do seu CSV ou lista sem a coluna **Valor**. Selecione **Não, continuar com uma lista de clientes que não inclui valor do cliente**.
5. Conclua a criação do seu público personalizado.
6. Na Braze, atualize a etapa de Facebook Audience Sync com o público personalizado que você criou.

### Recebi um e-mail relacionado aos termos de serviço de público personalizado do Facebook. O que devo fazer para resolver isso? {#ive-received-an-email-related-to-facebook-custom-audience-terms-of-service-what-should-i-do-to-resolve-this}

Para usar o Audience Sync com o Facebook, você deve aceitar esses termos de serviço.

- Se sua conta de anúncios estiver diretamente associada à sua conta pessoal do Facebook, você pode aceitar os termos de serviço na sua conta pessoal aqui: `https://www.facebook.com/ads/manage/customaudiences/tos.php?act=<ACCOUNT_ID>`.
- Se sua conta de anúncios estiver vinculada à conta do Business Manager da sua empresa, você deve aceitar os termos de serviço na sua conta do Facebook Business Manager aqui: `https://business.facebook.com/customaudiences/value_based/tos.php?act=<ACCOUNT_ID>&business_id=<BUSINESS_ID>`.

Depois de aceitar os termos de serviço de público personalizado do Facebook, faça o seguinte:

1. Atualize seu token de acesso do Facebook na Braze desconectando e reconectando sua conta do Facebook.
2. Reative sua etapa de Facebook Audience Sync editando e atualizando seu Canvas.

Em seguida, a Braze poderá sincronizar os usuários assim que eles atingirem a etapa de Facebook Audience Sync.

### O que aconteceu com os filtros **Connected Facebook** e **Number of Facebook Friends Using App**? {#what-happened-to-the-connected-facebook-and-number-of-facebook-friends-using-app-filters}

Os filtros de segmentação da Braze **Number of Facebook Friends Using App** e **Connected Facebook** foram descontinuados. O Facebook e os SDKs da Braze não coletam mais os dados subjacentes nos quais esses filtros se baseavam.

Substitua os filtros descontinuados por atributos personalizados, eventos personalizados ou Segments baseados em engajamento — por exemplo, login do Facebook ou vinculação social em vez de **Connected Facebook**, ou indicações, convites e compartilhamentos em vez de **Number of Facebook Friends Using App**.

Para redirecionamento com Canvas, faça a correspondência de usuários com e-mail, telefone, nome e sobrenome, conforme demonstrado na [Etapa 4: Configuração da sincronização](#step-4-sync-setup). Para ampliar o alcance, sincronize um Segment de alto valor com o Facebook e crie um público semelhante no Meta Ads Manager.

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
      <td>As causas típicas incluem o usuário que conectou a integração ter alterado a senha, as credenciais terem expirado, entre outras.</td>
      <td>Acesse <b>Partner Integrations</b> > <b>Facebook</b> e desconecte e reconecte sua conta. Consulte <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-Facebook-account'>esta seção de solução de problemas</a> para etapas adicionais de auditoria da sua conta do Facebook.</td>
    </tr>
    <tr>
      <td><b>Tamanho do público muito baixo</b></td>
      <td>Esse erro pode ocorrer se você criou uma etapa de Audience Sync que remove usuários dos seus públicos. Se o tamanho do público se aproximar de zero, a rede pode sinalizar que o público é muito pequeno para ser veiculado.</td>
      <td>Use uma estratégia de Audience Sync que adicione e remova usuários regularmente, de modo que o tamanho do público não seja totalmente esgotado.</td>
    </tr>
    <tr>
      <td><b>Público não existe</b></td>
      <td>A etapa de Audience Sync usa um público que não existe ou foi excluído. Isso também pode ser acionado se você não tiver mais a permissão necessária para acessar o público.</td>
      <td>Peça a um administrador que verifique na plataforma do parceiro se o público ainda existe. <br><br>Se existir, confirme se o usuário que conectou a integração tem permissão para acessar o público. Se não tiver, o usuário deve receber acesso a esse público. <br><br>Se o público foi removido intencionalmente, adicione um público ativo e crie um novo público na etapa.</td>
    </tr>
    <tr>
      <td><b>Tentativa de acesso à conta de anúncios</b></td>
      <td>Você não tem permissões para a conta de anúncios ou o público que selecionou.</td>
      <td>Trabalhe com os administradores da sua conta de anúncios para obter o acesso e as permissões adequados.</td>
    </tr>
    <tr>
      <td><b>Termos de serviço não aceitos</b></td>
      <td>Para alguns destinos de Audience Sync, como o Facebook, a rede de anúncios exige a aceitação de termos de serviço específicos para usar o recurso de Audience Sync. Esse erro será acionado se você não tiver aceito os termos apropriados. Como resultado, você também pode ter recebido um e-mail da Braze com o assunto: "Your authorization credentials for Facebook are invalid."</td>
      <td>Verifique se você aceitou os termos exigidos do Facebook.</td>
    </tr>
    <tr>
      <td><b>Todos os usuários estão apresentando erro</b></td>
      <td>Se todos os usuários estão apresentando erro em uma etapa, apesar de confirmar que esses usuários possuem valores para os campos selecionados na etapa, isso pode indicar um problema com sua conta do Facebook.</td>
      <td>Siga as etapas em <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-Facebook-account'>esta seção de solução de problemas</a> para verificar se há problemas na sua conta.
      </td>
    </tr>
    <tr>
      <td><b>Falha ao criar público</b></td>
      <td>Na página da parceira de tecnologia do Facebook, você vê "Connected", mas há um erro na etapa de Facebook Audience Sync ao sincronizar um público: "Failed to create audience 'audience name'". A autorização da sua conta do Facebook falhou. Acesse a página de parceiros de tecnologia para reconectar sua conta.</td>
      <td>Siga as etapas em <a href='/docs/partners/canvas_steps/facebook_audience_sync/#audit-your-Facebook-account'>esta seção de solução de problemas</a> para verificar se há problemas na sua conta.
      </td>
    </tr>
    <tr>
      <td><b>Conta de anúncios ausente no menu suspenso</b></td>
      <td>Ao configurar a etapa de Facebook Audience, uma conta de anúncios esperada não está listada no seletor de contas de anúncios.</td>
      <td>Confirme se seu app do Facebook concluiu a <a href="https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management">Revisão do App</a> para <code>ads_management</code> com o nível de acesso que o Facebook exige para uso da Marketing API. No <a href="https://business.facebook.com/">Facebook Business Manager</a>, confirme se o token do usuário do sistema tem as permissões corretas, está associado às contas de anúncios que você usa na Braze e se os termos da conta de anúncios foram aceitos. <br><br>Se o menu suspenso funciona em um novo Canvas, mas não em um Canvas que você já editou, tente atualizar a página do navegador (ou limpar o cache) e confirme se você está conectado como um usuário que ainda tem acesso a essas contas de anúncios.</td>
    </tr>
    <tr>
      <td><b>Erro ao validar token de acesso</b></td>
      <td>Você vê um erro sobre a validação do token de acesso do Facebook ao conectar a Braze ao Facebook ou ao sincronizar públicos.</td>
      <td>Saia do Facebook no seu navegador. Na Braze, acesse <b>Partner Integrations</b> &gt; <b>Facebook</b>, remova as credenciais salvas do Facebook e conecte o Facebook novamente. Na página de parceiros de tecnologia do Facebook para a Braze, desconecte e reconecte a integração, se a opção estiver disponível. <br><br>Se os problemas continuarem, siga <a href="#audit-your-Facebook-account">Auditar sua conta do Facebook</a>.</td>
    </tr>
    <tr>
      <td><b>Erros de permissão de exportação ou sincronização de público</b></td>
      <td>A exportação ou sincronização de um público do Facebook falha com erros de autorização, administrador ou conta de anúncios.</td>
      <td>No <a href="https://developers.facebook.com/">Meta for Developers</a>, abra seu app e confirme se seu usuário tem a função de <b>Admin</b> em <b>App roles</b>. Em <b>App settings</b> &gt; <b>Advanced</b>, confirme se <b>Advertising accounts</b> inclui as contas que você usa com a Braze. Em <a href="https://business.facebook.com/latest/settings">Business settings</a>, confirme se o usuário que está conectando ou o usuário do sistema tem acesso à conta de anúncios correta.</td>
    </tr>
  </tbody>
</table>

### Auditar sua conta do Facebook {#audit-your-facebook-account}

Se você tiver problemas adicionais com sua integração, consulte as seções e etapas a seguir para auditar sua conta do Facebook.

#### Revisar permissões da conta {#review-account-permissions}

1. Consulte a [documentação do Facebook](https://www.facebook.com/business/help/186007118118684?id=829106167281625) sobre como gerenciar essas permissões na plataforma. Para o Facebook Business Manager, você precisa de pelo menos uma função de **Admin** ou **Employee** no Business Manager com acesso às contas de anúncios necessárias.
2. Como **Employee**, confirme se o Admin concede a você permissões completas de **Manage Ad Account** para cada conta de anúncios, a fim de criar um público ou sincronizar usuários com o público.
3. Depois que isso for concedido, você deve desconectar e reconectar sua conta.

#### Aceitar os termos de serviço {#terms}

Aceite quaisquer Termos de Serviço (TOS) pendentes do Facebook. O Facebook periodicamente exigirá que você (o usuário) e o gerente de negócios reaprovem seus termos de serviço.

1. O usuário conectado precisa aceitar todos os termos de serviço para cada uma de suas contas de anúncios:
- TOS de público personalizado para sua conta pessoal do Facebook:
`https://business.facebook.com/ads/manage/customaudiences/tos/?act=<AD_ACCOUNT_ID>`

![Uma conta com permissões de controle total para gerenciar uma conta de anúncios.]({% image_buster /assets/img/fb_audience_sync/ad_account_permission.png %}){: style="max-width:70%;"}

Para encontrar o ID da sua conta e o ID do negócio, siga estas etapas:

1. Acesse sua [conta do Facebook Ads Manager](https://adsmanager.facebook.com/).
2. Confirme se você está usando a conta de anúncios correta verificando no menu suspenso.
3. Na URL, encontre o ID da conta após `act=` e o ID do negócio após `business_id=`

![A URL com o ID da conta e o ID do negócio destacados.]({% image_buster /assets/img/fb_audience_sync/fb_businessid_url.png %}){: style="max-width:90%;"}

{:start="4"}

4. Leia e selecione **Accept** para os Termos de Público Personalizado. Recomendamos confirmar para qual conta os termos de serviço estão sendo assinados usando o menu suspenso no topo dos termos.

![O menu suspenso que mostra a conta que está assinando os termos de serviço.]({% image_buster /assets/img/fb_audience_sync/confirm_accept_tos.png %}){: style="max-width:90%;"}

{:start="5"}
5. Você deve selecionar **Accept** para os termos de serviço. Depois, você verá esta mensagem: "You have accepted these terms of service on behalf of Braze".
6. Atualize seu token de acesso do Facebook na Braze desconectando e reconectando sua conta do Facebook.
7. Reative sua etapa de Facebook Audience Sync editando e atualizando seu Canvas. A Braze poderá então sincronizar usuários assim que eles alcançarem a etapa de público do Facebook.
8. Se o problema persistir, tente usar um usuário separado com permissões de administrador para aceitar manualmente os termos pelo Ads Manager.

#### Concluir tarefas pendentes {#complete-any-pending-tasks}

Verifique se você tem tarefas pendentes com o Facebook que possam estar impedindo o uso dos serviços do Facebook Ads:

1. [Faça login no Facebook Ads Manager](https://adsmanager.facebook.com/).
2. Selecione a conta de anúncios com a qual você está tendo problemas.
3. Na navegação, selecione **Account Overview**. <br> ![A navegação com Account Overview selecionado.]({% image_buster /assets/img/fb_audience_sync/ads_manager_accouint_overview.png %})
4. Verifique se há alertas que precisam ser resolvidos. <br> ![Uma conta com cartão de crédito expirado.]({% image_buster /assets/img/fb_audience_sync/resolve_alerts.png %})

{:start="5"}

5. Verifique se há tarefas de configuração que precisam ser concluídas. <br> ![Uma conta com configuração parcialmente concluída.]({% image_buster /assets/img/fb_audience_sync/confirm_tasks.png %})

#### Conectar com um usuário diferente {#connect-with-a-different-user}

Como outra etapa de solução de problemas, recomendamos que um usuário administrador diferente tente conectar sua conta fazendo o seguinte:

1. Desconecte a integração atual.
2. Um usuário separado com permissões de administrador conecta sua conta de usuário do Facebook.