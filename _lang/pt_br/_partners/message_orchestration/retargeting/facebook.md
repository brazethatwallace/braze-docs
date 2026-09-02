---
nav_title: Facebook
article_title: Exportação do público do Facebook
alias: /partners/facebook/
description: "Este artigo de referência descreve a parceria entre a Braze e o Facebook, uma plataforma social líder para as marcas alcançarem e se engajarem com seus clientes."
page_type: partner
search_tag: Partner
---

# Exportação do público do Facebook {#facebook-audience-export}

> A integração entre a Braze e o Facebook permite que você exporte manualmente seus Segments da Braze para o Facebook para criar públicos personalizados do Facebook. Essa é uma exportação única e estática de público e só criará novos públicos personalizados no Facebook.

Os casos de uso comuns para exportar públicos personalizados do Facebook incluem:
- Redirecionamento de usuários em pontos específicos do seu ciclo de vida
- Criação de listas de direcionamento de exclusão
- Criação de [públicos semelhantes](https://www.facebook.com/business/help/164749007013531?id=401668390442328) para adquirir novos usuários com mais eficiência
<br><br>

{% alert note %}
A exportação do público do Facebook usa o **token de acesso do usuário** para autorizar solicitações.<br><br>
Se você estiver usando esse recurso juntamente com o recurso de [sincronização de público com o Facebook]({{site.baseurl}}/audience_sync_facebook), a Braze usará, por padrão, o **token de usuário do sistema** mais confiável que você já gerou para autorizar solicitações.
{% endalert %}

{% alert note %}
Se estiver participando do teste das contas de trabalho do Meta na versão beta, desconecte e reconecte sua conta à [página de parceiro do Facebook]({{site.baseurl}}/partners/canvas_audience_sync/facebook_audience_sync#step-1-connect-to-facebook).
{% endalert %}

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| [Facebook Business Manager](https://www.facebook.com/business/help/113163272211510?id=180505742745347) | Uma ferramenta centralizada para gerenciar os ativos da sua marca no Facebook (por exemplo, contas de anúncios, páginas, apps). |
| [Conta de anúncios do Facebook](https://www.facebook.com/business/help/910137316041095?id=420299598837059) | Uma conta de anúncios ativa do Facebook vinculada ao gerenciador de negócios da sua marca que você deseja usar com os públicos personalizados da Braze.<br><br>Certifique-se de que o administrador do seu Facebook Business Manager concedeu a você permissões de administrador para as contas de anúncios do Facebook que você pretende usar com a Braze e que você aceitou os termos e condições da sua conta de anúncios. Caso contrário, você não poderá acessar nenhuma conta de anúncios do Facebook na Braze. |
| [Termos de Públicos Personalizados do Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php) | Você deve aceitar os Termos de Públicos Personalizados do Facebook para as contas de anúncios do Facebook que pretende usar com a Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Conectar ao Facebook {#step-1-connect-to-facebook}

1. No dashboard da Braze, acesse **Integrações com Parceiros** > **Parceiros de Tecnologia** e selecione **Facebook**.

{: start="2"}
2. No módulo de exportação de público do Facebook, selecione **Connect Facebook**. <br><br>![Página de parceiros de tecnologia do Facebook na plataforma Braze.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:70%;"}

{: start="3"}
3. Na janela de diálogo oAuth do Facebook, autorize a Braze a criar Públicos Personalizados nas suas contas de anúncios do Facebook. <br><br>![A primeira caixa de diálogo do Facebook solicitando "Conectar como X", onde X é seu nome de usuário do Facebook.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![A segunda caixa de diálogo do Facebook solicitando permissão para gerenciar anúncios das suas contas de anúncios.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

{: start="4"}
4. Depois que a Braze estiver vinculada à sua conta do Facebook, selecione quais contas de anúncios você deseja sincronizar no seu espaço de trabalho da Braze. <br><br>![Uma lista de contas de anúncios disponíveis que você pode conectar ao Facebook.]({% image_buster /assets/img/fb/afb_4.png %}){: style="max-width:70%;"}<br><br> Depois de conectar, você será levado de volta à página de parceiros, onde poderá ver quais contas estão conectadas e desconectar contas existentes. <br><br> ![Uma versão atualizada da página de parceiros de tecnologia do Facebook mostrando as contas de anúncios conectadas com sucesso.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:70%;"}<br>
<br> Sua conexão com o Facebook é aplicada no nível do espaço de trabalho da Braze. Se o administrador do Facebook remover você do Facebook Business Manager ou do acesso às contas do Facebook conectadas, a Braze detecta um token inválido. Como resultado, seus Canvas ativos que usam etapas de público do Facebook mostrarão erros, e a Braze não conseguirá sincronizar usuários.

{% alert important %}
Para clientes que já passaram pelo processo de revisão de app do Facebook para [Ads Management](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) e [Ads Management Standard Access](https://developers.facebook.com/docs/marketing-api/access#standard), seu token de usuário do sistema ainda é válido para a etapa de público do Facebook. Não é possível editar ou revogar o token de usuário do sistema do Facebook pela página de parceiros do Facebook. Em vez disso, você pode conectar sua conta do Facebook para substituir o token de usuário do sistema do Facebook no seu espaço de trabalho da Braze.

<br><br>A nova configuração oAuth do Facebook também se aplica às [exportações do Facebook via Segments]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook#prerequisites).
{% endalert %}

### Etapa 2: Exportar seus usuários para o Facebook {#step-2-export-your-users-into-facebook}

Na Braze, a exportação de público do Facebook é acessível pela página **Segments**.

1. Na página **Segments**, selecione o Segment que você deseja exportar.
2. Selecione **User Data** e depois selecione **Export as Facebook Audience**. <br><br>![A seção "Detalhes do Segment" de um Segment com "User Data" selecionado para exibir um menu suspenso de opções que inclui "Export as Facebook Audience".]({% image_buster /assets/img/fb/afb_6.png %})

{: start="3"}
3. Se você ainda não ativou o Facebook na Braze, será solicitado a acessar a página de Parceiros de Tecnologia do Facebook no dashboard. Se já ativou o Facebook através de **Parceiros de Tecnologia** > **Facebook**, você pode selecionar sua conta de anúncios do Facebook e os campos de usuário para exportar. <br><br> Você pode exportar os seguintes campos:
- IDFA do dispositivo
- Número de telefone
- E-mail

{% alert note %}
Você pode selecionar apenas um campo de usuário por exportação. Se escolher mais de um tipo de dado, a Braze criará um público personalizado separado para cada um.
{% endalert %}

{: start="4"}
4. Depois de selecionar o campo de usuário, selecione **Export Segment**. Assim como nas exportações CSV, você receberá um e-mail quando o Segment terminar de ser exportado para o Facebook.
5. Visualize o público personalizado no [Facebook Ads Manager](https://www.facebook.com/ads/manager/audiences/manage/).

{% alert important %}
Por motivos de privacidade do usuário, o Facebook não permite que você veja:

- Os usuários exatos que foram adicionados com sucesso a um Público Personalizado. [Veja os detalhes do Facebook sobre por que membros individuais do público estão ocultos](https://www.facebook.com/business/help/112061095610075).
- O tamanho do Público Personalizado. [Veja os detalhes sobre as mudanças na estimativa de tamanho de público do Facebook](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923).
{% endalert %}

#### Configurando sua exportação de público {#configuring-your-audience-export}

Ao criar públicos do Facebook, você pode querer incluir ou excluir determinados usuários com base em suas preferências, e para cumprir leis de privacidade, como o direito de "Não Vender ou Compartilhar" sob a [CCPA](https://oag.ca.gov/privacy/ccpa). Os profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários nos critérios de entrada do Canvas. As opções a seguir podem ajudar.

- Se você coletou o [IDFA do iOS através do SDK da Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations#optional-idfa-collection), pode usar o filtro **Ads Tracking Enabled**. Selecione o valor como `true` para enviar usuários para destinos de sincronização de público apenas quando eles tiverem optado por participar.

![Filtro de entrada do Canvas mostrando Ads Tracking Enabled definido como true.]({% image_buster /assets/img/tiktok/tiktok16.png %}){: style="max-width:75%;"}

- Se você estiver coletando opt ins, opt outs, `Do Not Sell Or Share` ou outros atributos personalizados relevantes, inclua-os nos critérios de entrada do Canvas como filtro:

![Um Canvas com público de entrada de "opted_in_marketing" igual a "true".]({% image_buster /assets/img/tiktok/tiktok13.png %}){: style="max-width:75%;"}


#### Públicos Semelhantes (Lookalike Audiences) {#lookalike-audiences}

Depois de exportar com sucesso um Segment como público do Facebook, você pode criar grupos adicionais usando os [Públicos Semelhantes](https://www.facebook.com/business/help/164749007013531?id=401668390442328) do Facebook. Esse recurso analisa os dados demográficos, interesses e outros atributos do público escolhido e cria um novo público de pessoas com atributos semelhantes.

## Solução de problemas {#troubleshooting}

### Erro ao validar token de acesso {#error-validating-access-token}

Ao usar a exportação para o Facebook, o erro `Error Validating Access Token` aparece se:
- Você alterou sua senha, o que invalida a sessão atual
- O Facebook desconectou você como medida de segurança

Para resolver esse erro, siga estas etapas:
1. Saia do Facebook e faça login novamente.
2. Na Braze, remova suas credenciais do Facebook e salve. Confirme que as credenciais foram removidas tentando exportar um Segment (o ícone de exportação deve estar desativado).
3. Adicione novamente e salve suas credenciais do Facebook.
4. Tente exportar novamente.

Se a exportação não funcionar, faça o seguinte:
1. Remova suas credenciais novamente e salve.
2. Adicione novamente suas credenciais e salve.
3. Desconecte e reconecte a integração com o Facebook na página de **parceiros de tecnologia**.

### Erro ao exportar um público do Facebook {#error-when-exporting-a-facebook-audience}

Se você receber um erro ao exportar um Segment como público do Facebook, a documentação para desenvolvedores do Facebook destaca as seguintes causas comuns:

1. **O token de acesso é de um usuário que não é administrador do app e da conta de anúncios:** O usuário do Facebook cujas credenciais estão conectadas à Braze deve ter as permissões corretas.
2. **A conta de anúncios para a qual você está exportando não está associada ao seu app:** A conta de anúncios do Facebook deve estar vinculada ao seu app nas configurações do Facebook.

Use as verificações a seguir para confirmar sua configuração:

- **Verifique se você é administrador do app:** Acesse [developers.Facebook.com](https://developers.facebook.com/), abra **My Apps** e selecione o app da sua empresa. Se você não vir o app, sua equipe de desenvolvimento pode precisar adicioná-lo. No dashboard do app, acesse **Roles** para confirmar sua função (Admin, Developer, Tester ou Analytics User).
- **Verifique se sua conta de anúncios está associada ao seu app:** No dashboard do app do Facebook, acesse **Settings** > **Advanced**, role até **Advertising Accounts** e adicione o ID da conta de anúncios do Facebook que você deseja usar para exportações de público da Braze, caso ainda não esteja listado.
- **Verifique se você é administrador da conta de anúncios:** Acesse [business.Facebook.com](https://business.facebook.com/), abra **Business Settings** no menu principal e acesse **Accounts** > **Ad accounts** e selecione a conta de anúncios. Confirme seu acesso e que você tem as permissões necessárias para criar públicos personalizados.

Para mais detalhes, consulte a [documentação da API de públicos personalizados do Facebook](https://developers.facebook.com/docs/) e o [guia do Central de Ajuda para Empresas do Facebook sobre públicos personalizados](https://www.facebook.com/business/help).