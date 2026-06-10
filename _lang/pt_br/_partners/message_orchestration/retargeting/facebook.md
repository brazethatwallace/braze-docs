---
nav_title: Facebook
article_title: Exportação do público do Facebook
alias: /partners/facebook/
description: "Este artigo de referência descreve a parceria entre a Braze e o Facebook, uma plataforma social líder para as marcas alcançarem e se engajarem com seus clientes."
page_type: partner
search_tag: Partner

---

# Exportação do público do Facebook {#facebook-audience-export}

> A integração entre a Braze e o Facebook permite que você exporte manualmente seus segmentos da Braze para o Facebook para criar públicos personalizados do Facebook. Essa é uma exportação única e estática de público e só criará novos públicos personalizados no Facebook.

Os casos de uso comuns para exportar públicos personalizados do Facebook incluem:
- Redirecionamento de usuários em pontos específicos do seu ciclo de vida
- Criação de listas de direcionamento de exclusão
- Criação de [públicos semelhantes](https://www.facebook.com/business/help/164749007013531?id=401668390442328) para adquirir novos usuários com mais eficiência
<br><br>

{% alert note %}
A exportação do público do Facebook usa o **token de acesso do usuário** para autorizar solicitações.<br><br>
Se você estiver usando esse recurso juntamente com o recurso de [sincronização do público do Facebook]({{site.baseurl}}/audience_sync_facebook/), a Braze usará, por padrão, o **token de usuário do sistema** mais confiável que você já gerou para autorizar solicitações.
{% endalert %}

{% alert note %}
Se estiver participando do teste das contas de trabalho do Meta na versão beta, desconecte e reconecte sua conta à [página de parceiro do Facebook]({{site.baseurl}}/partners/canvas_steps/facebook_audience_sync/#step-1-connect-to-facebook).
{% endalert %}

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| ----------- | ----------- |
| [Gerente de negócios do Facebook](https://www.facebook.com/business/help/113163272211510?id=180505742745347) | Uma ferramenta centralizada para gerenciar os ativos do Facebook da sua marca (por exemplo, contas de anúncios, páginas, apps). |
| [Conta de anúncios do Facebook](https://www.facebook.com/business/help/910137316041095?id=420299598837059) | Uma conta de anúncios ativa do Facebook vinculada ao gerente de negócios da sua marca que você deseja usar com os públicos personalizados da Braze.<br><br>Certifique-se de que o administrador do seu gerente de negócios do Facebook lhe concedeu permissões de administrador para as contas de anúncios do Facebook que você planeja usar com a Braze e que você aceitou os termos e condições da sua conta de anúncios. Caso contrário, não será possível acessar nenhuma conta de anúncios do Facebook na Braze. |
| [Termos de públicos personalizados do Facebook](https://www.facebook.com/ads/manage/customaudiences/tos.php)| Você deve aceitar os Termos de Públicos Personalizados do Facebook para suas contas de anúncios do Facebook que planeja usar com a Braze.|
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: conecte-se ao Facebook {#step-1-connect-to-facebook}

1. No dashboard da Braze, acesse **Integrações de parceiros** > **Parceiros de tecnologia** e selecione **Facebook**.

{: start="2"}
2. No módulo Facebook Audience Export, selecione **Connect Facebook**. <br><br>![Página de parceiros de tecnologia do Facebook na plataforma Braze.]({% image_buster /assets/img/fb/afb_1.png %}){: style="max-width:70%;"}

{: start="3"}
3. Na janela de diálogo oAuth do Facebook, autorize a Braze a criar públicos personalizados em suas contas de anúncios do Facebook. <br><br>![A primeira caixa de diálogo do Facebook solicitando para "Conectar como X", em que X é seu nome de usuário do Facebook.]({% image_buster /assets/img/fb/afb_3.png %}){: style="max-width:30%;"}  ![A segunda caixa de diálogo do Facebook solicitando permissão para gerenciar anúncios de suas contas de anúncios.]({% image_buster /assets/img/fb/afb_2.png %}){: style="max-width:40%;"}

{: start="4"}
4. Depois que a Braze estiver vinculada à sua conta do Facebook, selecione as contas de anúncios que deseja sincronizar em seu espaço de trabalho da Braze. <br><br>![Uma lista de contas de anúncios disponíveis que você pode conectar ao Facebook.]({% image_buster /assets/img/fb/afb_4.png %}){: style="max-width:70%;"}<br><br> Depois de se conectar, você será levado de volta à página do parceiro, onde poderá ver quais contas estão conectadas e desconectar contas existentes. <br><br> ![Uma versão atualizada da página de parceiros de tecnologia do Facebook mostrando as contas de anúncios conectadas com sucesso.]({% image_buster /assets/img/fb/afb_5.png %}){: style="max-width:70%;"}<br>
<br> Sua conexão com o Facebook é aplicada no nível do espaço de trabalho da Braze. Se o administrador do Facebook remover você do Facebook Business Manager ou do acesso às contas conectadas do Facebook, a Braze detectará um token inválido. Como resultado, seus Canvas ativos que usam etapas de público do Facebook mostrarão erros, e a Braze não poderá sincronizar usuários.

{% alert important %}
Para os clientes que já passaram pelo processo de revisão do app do Facebook para o [Gerenciamento de anúncios](https://developers.facebook.com/docs/facebook-login/permissions/#reference-ads_management) e [o Acesso padrão ao Gerenciamento de anúncios](https://developers.facebook.com/docs/marketing-api/access#standard), o token de usuário do sistema ainda será válido para a etapa do público do Facebook. Não será possível editar ou revogar o token de usuário do sistema do Facebook por meio da página de parceiro do Facebook. Em vez disso, é possível conectar sua conta do Facebook para substituir o token de usuário do sistema do Facebook no espaço de trabalho da Braze.

<br><br>A nova configuração do Facebook oAuth também se aplica às [exportações do Facebook por meio de segmentos]({{site.baseurl}}/partners/message_orchestration/additional_channels/retargeting/facebook/#prerequisites).
{% endalert %}

### Etapa 2: exporte seus usuários para o Facebook {#step-2-export-your-users-into-facebook}

Na Braze, a exportação do público do Facebook pode ser acessada por meio da página **Segments**.

1. Na página **Segments**, selecione o segmento que você deseja exportar.
2. Selecione **User Data** e, em seguida, selecione **Exportar como público do Facebook**. <br><br>![A seção "Segment Details" de um segmento com "User Data" selecionado para exibir um menu suspenso de opções que inclui "Export as Facebook Audience".]({% image_buster /assets/img/fb/afb_6.png %})

{: start="3"}
3. Se ainda não tiver ativado o Facebook na Braze, você verá uma indicação para acessar a página de parceiros de tecnologia do Facebook no dashboard. Se já tiver ativado o Facebook por meio de **Technology Partners** > **Facebook**, poderá selecionar sua conta de anúncios do Facebook e os campos de usuário a serem exportados. <br><br> Você pode exportar os seguintes campos:
- IDFA do dispositivo
- Número de telefone
- E-mail

{% alert note %}
Só é possível selecionar um campo de usuário em uma única exportação. Se você escolher mais de um tipo de dados, a Braze criará um público personalizado separado para cada um deles.
{% endalert %}

{: start="4"}
4. Depois de selecionar o campo do usuário, selecione **Export Segment**. Assim como as exportações CSV, você receberá um e-mail quando o segmento terminar de ser exportado para o Facebook.
5. Veja o público personalizado no [Gerenciador de Anúncios do Facebook](https://www.facebook.com/ads/manager/audiences/manage/).

{% alert important %}
Devido a razões de privacidade do usuário, o Facebook não permite que você veja:

- Os usuários exatos que foram adicionados com sucesso a um público personalizado. [Saiba mais.](https://www.facebook.com/business/help/112061095610075)
- O tamanho do público personalizado. [Saiba mais.](https://marketingland.com/exclusive-facebook-will-no-longer-show-audience-reach-estimates-for-custom-audiences-after-vulnerability-detected-236923)
{% endalert %}

#### Configuração de sua exportação de público {#configuring-your-audience-export}

Ao criar públicos do Facebook, talvez seja necessário incluir ou excluir determinados usuários com base em suas preferências e para cumprir as leis de privacidade, como o direito de "Não vender ou compartilhar" de acordo com a [CCPA](https://oag.ca.gov/privacy/ccpa). Os profissionais de marketing devem implementar os filtros relevantes para a elegibilidade dos usuários em seus critérios de entrada no Canvas. Abaixo, listamos algumas opções.

- Se você coletou o [IDFA do iOS por meio do SDK da Braze]({{site.baseurl}}/developer_guide/platform_integration_guides/swift/initial_sdk_setup/other_sdk_customizations/#optional-idfa-collection), poderá usar o filtro **Ads Tracking Enabled**. Selecione o valor como `true` para enviar os usuários apenas para destinos do Audience Sync que eles aceitaram.

![]({% image_buster /assets/img/tiktok/tiktok16.png %}){: style="max-width:75%;"}

- Se estiver coletando aceitações, recusas, `Do Not Sell Or Share` ou outros atributos personalizados relevantes, inclua-os nos critérios de entrada do Canvas como um filtro:

![Um Canvas com um público de entrada de "opted_in_marketing" é igual a "true".]({% image_buster /assets/img/tiktok/tiktok13.png %}){: style="max-width:75%;"}


#### Públicos semelhantes {#lookalike-audiences}

Depois de exportar com êxito um segmento como um público do Facebook, você poderá criar grupos adicionais usando o Facebook [Lookalike Audiences](https://www.facebook.com/business/help/164749007013531?id=401668390442328). Esse recurso analisa os dados demográficos, os interesses e outros atributos do público escolhido e cria um novo público de pessoas com atributos semelhantes.

## Solução de problemas {#troubleshooting}

### Erro ao validar o token de acesso {#error-validating-access-token}

Ao usar a exportação do Facebook, o erro `Error Validating Access Token` será exibido se:
- Você mudou sua senha, o que invalida sua sessão atual
- O Facebook fez você sair como uma precaução de segurança

Para resolver esse erro, siga estas etapas:
1. Saia do Facebook e faça login novamente.
2. Na Braze, remova suas credenciais do Facebook e salve. Confirme que as credenciais foram removidas tentando exportar um segmento (o ícone de exportação deve estar desativado).
3. Readicione e salve suas credenciais do Facebook.
4. Tente exportar novamente.

Se a exportação não funcionar, faça o seguinte:
1. Remova suas credenciais novamente e salve.
2. Readicione suas credenciais e salve.
3. Desconecte e reconecte a integração do Facebook na página **Technology Partners**.

### Erro ao exportar um público do Facebook {#error-when-exporting-a-facebook-audience}

Se você receber um erro ao exportar um segmento como um público do Facebook, a documentação para desenvolvedores do Facebook indica as seguintes causas comuns:

1. **O token de acesso é de um usuário que não é administrador do app e da conta de anúncios:** o usuário do Facebook cujas credenciais estão conectadas à Braze deve ter as permissões corretas.
2. **A conta de anúncios para a qual você está exportando não está associada ao seu app:** a conta de anúncios do Facebook deve estar vinculada ao seu app nas configurações do Facebook.

Use as verificações a seguir para validar sua configuração:

- **Verifique se você é administrador do app:** acesse [developers.facebook.com](https://developers.facebook.com/), abra **My Apps** e selecione o app da sua empresa. Se você não vir o app, sua equipe de desenvolvimento pode precisar adicioná-lo. No dashboard do app, acesse **Roles** no menu à esquerda para confirmar sua função (Admin, Developer, Tester ou Analytics User).
- **Verifique se sua conta de anúncios está associada ao seu app:** no dashboard do app do Facebook, acesse **Settings** > **Advanced**, role até **Advertising Accounts** e adicione o ID da conta de anúncios do Facebook que você deseja usar para exportações de público da Braze, caso ainda não esteja listado.
- **Verifique se você é administrador da conta de anúncios:** acesse [business.facebook.com](https://business.facebook.com/) e selecione **Business Settings** no menu suspenso no canto superior esquerdo. Em seguida, acesse **Accounts** > **Ad accounts** e selecione a conta de anúncios. Confirme seu acesso e que você tem as permissões necessárias para criar públicos personalizados.

Para mais detalhes, consulte a [documentação da API de públicos personalizados do Facebook](https://developers.facebook.com/docs/) e o [guia da Central de Ajuda para Empresas do Facebook sobre públicos personalizados](https://www.facebook.com/business/help).