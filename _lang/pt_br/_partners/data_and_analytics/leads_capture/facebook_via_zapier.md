---
nav_title: Anúncios de leads do Facebook via Zapier
article_title: Anúncios de leads do Facebook via Zapier
description: "Este artigo de referência descreve a integração entre a Braze e o Facebook Lead Ads via Zapier para automatizar a transferência de dados de leads do Facebook para a Braze, possibilitando engajamento em tempo real e ações de acompanhamento personalizadas."
alias: /partners/facebook_via_zapier/
page_type: partner
search_tag: Partner
---

# Integração de anúncios de leads do Facebook via Zapier {#facebook-lead-ads-via-zapier-integration}

> Com a integração do Facebook Lead Ads via <a href="https://zapier.com/" target="_blank">Zapier</a>, você pode importar seus leads do Facebook para a Braze e rastrear um evento personalizado quando os leads forem capturados.

O Facebook Lead Ads é um formato de anúncio que permite que as empresas coletem informações de leads diretamente no Facebook. Esses anúncios são projetados para tornar o processo de geração de leads fácil e prático. Ao utilizar uma integração com o Zapier e a Braze, você pode automatizar a transferência de dados de leads do Facebook para a Braze, possibilitando engajamento em tempo real e ações de acompanhamento personalizadas.

## Pré-requisitos {#prerequisites}

| Requisitos | Descrição |
|---|---|
| Conta Zapier | Uma conta Zapier é necessária para aproveitar essa parceria. Essa integração requer o uso de <a href="https://zapier.com/app/pricing/" target="_blank">apps premium do Zapier</a>, então verifique se o seu plano do Zapier tem acesso a apps premium. |
| <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862/" target="_blank">Acesso ao Facebook Leads</a> | O acesso ao Facebook Leads é necessário para cada conta de anúncios que você planeja usar com a Braze. |
| <a href="https://www.facebook.com/business/help/1710077379203657?id=180505742745347" target="_blank">Facebook Business Manager</a> | Você usará o Facebook Business Manager, uma ferramenta centralizada para gerenciar os ativos do Facebook da sua marca (por exemplo, contas de anúncios, páginas e apps), como parte dessa integração. |
| <a href="https://www.facebook.com/business/help/195296697183682?id=829106167281625/" target="_blank">Conta de anúncios do Facebook</a> | Você precisará de uma conta de anúncios do Facebook ativa vinculada ao gerenciador de negócios da sua marca. <br><br>Certifique-se de que você tem a permissão "Manage ad accounts" para cada conta de anúncios que planeja usar com a Braze e de que aceitou os termos e condições da sua conta de anúncios. |
| <a href="https://www.facebook.com/business/help/183277585892925?id=420299598837059/" target="_blank">Página do Facebook</a> | Você precisará de uma Página do Facebook ativa vinculada ao gerenciador de negócios da sua marca. <br><br>Certifique-se de que você tem as permissões "Manage Pages" para cada Página do Facebook que planeja usar com a Braze. |
| Endpoint REST da Braze | Certifique-se de saber a [URL do seu endpoint REST]({{site.baseurl}}/api/basics#api-definitions). Seu endpoint de API corresponde à URL do dashboard da sua instância da Braze. <br><br> Por exemplo, se a URL do seu dashboard é `https://dashboard-03.braze.com`, seu endpoint será `dashboard-03`. |
| Chave da API REST da Braze | Certifique-se de ter uma chave da API REST da Braze com permissões `users.track`. <br><br> Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API**. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

### Etapa 1: Criar uma campanha de Lead Ads com formulário instantâneo {#step-1-create-a-lead-ads-campaign-with-an-instant-form}

No Facebook Ads Manager, crie uma <a href="https://www.facebook.com/business/help/397336587121938?id=735435806665862&helpref=uf_permalink" target="_blank">campanha de Facebook Leads e um formulário de Facebook Lead Ads</a>.

Você pode usar um endereço de e-mail ou número de telefone ao fazer uma solicitação ao [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) para atualizar ou criar o perfil de usuário. Por esse motivo, inclua um **Campo de contato** para **e-mail** ou **telefone** no seu formulário de lead ad. Se estiver coletando nomes ou sobrenomes, colete-os separadamente no formulário em vez de usar nomes completos.

### Etapa 2: Conectar sua conta do Facebook ao Zapier {#step-2-connect-your-facebook-account-to-zapier}

#### Etapa 2a: Selecionar o método de conexão no Zapier {#step-2a-select-your-connection-method-in-zapier}

No Zapier, acesse **Apps** para buscar os apps disponíveis do Facebook. Selecione **Facebook Lead Ads** ou **Facebook Lead Ads (for Business admins)**.

Para saber mais sobre esses dois métodos de conexão da sua conta do Facebook ao Zapier, consulte:

- <a href="https://help.zapier.com/hc/en-us/articles/8496123584781-How-to-get-started-with-Facebook-Lead-Ads-for-Business-Admins-on-Zapier#h_01HC9VZFZG0GR2KRYM5EQJN329" target="_blank">Facebook Lead Ads (for Business Admins)</a>
- <a href="https://help.zapier.com/hc/en-us/articles/8496061306253#h_01HC9VMZ2XP0017AR6SE7S30JG" target="_blank">Facebook Lead Ads</a>

![Busca de apps no Zapier mostrando as opções de conexão do Facebook Lead Ads.]({% image_buster /assets/img/fb_lead_ads_zapier/integration1.png %}){: style="max-width:80%;"}

#### Etapa 2b: Adicionar o Zapier ao Leads Access no Facebook Business Manager {#step-2b-add-zapier-to-leads-access-in-facebook-business-manager}

No Facebook Business Manager, acesse **Integrations** > **Leads Access** no menu de navegação. Selecione sua página do Facebook e clique em **CRMs**. Na guia CRM, selecione **Assign CRMs** e adicione o **Zapier**.

![Página de Leads Access no Facebook Business Manager com o Zapier atribuído como integração de CRM.]({% image_buster /assets/img/fb_lead_ads_zapier/integration2.png %}){: style="max-width:80%;"}

Para ver as etapas de atribuição do Zapier como integração de CRM, consulte a <a href="https://www.facebook.com/business/help/540596413257598?id=735435806665862" target="_blank">documentação</a> do Facebook.

### Etapa 3: Criar seu Zap {#step-3-create-your-zap}

#### Etapa 3a: Criar o gatilho {#step-3a-create-the-trigger}

Depois de conectar sua conta do Facebook, você pode prosseguir para criar um Zap. Para o **Trigger**, selecione **Facebook Lead Ads** ou **Facebook Lead Ads (for Business Admins)** com base na sua escolha na etapa 2.

![Etapa de gatilho no Zapier com Facebook Lead Ads selecionado.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap1.png %}){: style="max-width:80%;"}

Para o **Event**, selecione **New Leads** > **Continue**.

![Seleção de evento de gatilho no Zapier mostrando New Leads.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap2.png %}){: style="max-width:80%;"}

Selecione sua conta do Facebook e depois **Continue**.

![Etapa de conexão da conta do Facebook no Zapier para o gatilho.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap3.png %}){: style="max-width:80%;"}

Selecione sua página do Facebook e o formulário instantâneo que você criou anteriormente, e depois **Continue**.

![Configuração do gatilho no Zapier selecionando uma página do Facebook e um formulário instantâneo.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap4.png %}){: style="max-width:80%;"}

Em seguida, teste esse gatilho. Após validar a saída do formulário, selecione **Continue with selected record**.

#### Etapa 3b: Criar uma ação {#step-3b-create-an-action}

Adicione uma nova etapa e selecione **Webhooks by Zapier**. Em seguida, selecione **Custom Request** no campo **Event** e clique em **Continue**.

![Etapa de ação no Zapier configurada com Webhooks by Zapier e Custom Request.]({% image_buster /assets/img/fb_lead_ads_zapier/create_zap5.png %}){: style="max-width:80%;"}

Por último, configure sua solicitação personalizada inserindo os campos na carga útil. O trecho de código a seguir mostra um exemplo de carga útil.

```
{
    "attributes": [
        {
            "email": "<insert_email_field>",
            "first_name": "<insert_first_name_field>",
            "last_name": "<insert_last_name_field>",
            "lead_form": "<insert_form_name_field>",
            "fb_campaign": "<insert_campaign_id_field>",
            "fb_ad_set": "<insert_campaign_id_field>",
            "fb_ad": "<insert_campaign_id_field>",
            "email_subscribe": "subscribed",
            "subscription_groups" : [{
                "subscription_group_id": "<subscription_group_id>",
                "subscription_state": "subscribed"
                }
            ]
        }
    ],
    "events": [
        {
            "email": "<insert_email_field>",
            "name": "<insert_custom_event_name>",
            "time": "<insert_timestamp_field>",
            "_update_existing_only": false
        }
    ]
}`
```

Veja um exemplo de como isso aparece no Zapier:

![Exemplo de mapeamento de carga útil do webhook no Zapier para enviar campos de lead do Facebook à Braze.]({% image_buster /assets/img/fb_lead_ads_zapier/configuration_example.png %}){: style="max-width:80%;"}

Após configurar seu webhook, selecione **Continue and test**. Se o teste for bem-sucedido, você pode publicar seu Zap.

### Etapa 4: Testar seu Zap de Facebook Lead Ads {#step-4-test-your-facebook-lead-ads-zap}

Para testar de ponta a ponta, use a ferramenta de teste de Lead Ads do Facebook no console de desenvolvedor do Facebook. Para saber mais, consulte <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/testing-troubleshooting/" target="_blank">Testing and Troubleshooting</a>.

## Gerenciamento de identidade do usuário {#user-identity-management}

Essa integração permite atribuir seus leads do Facebook por e-mail por meio do [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track#update-a-user-profile-by-phone-number).

* Se o e-mail corresponder a um perfil de usuário existente, a Braze atualizará o perfil com os dados de leads do Facebook.
* Se houver vários perfis de usuário com o mesmo e-mail, a Braze priorizará o perfil atualizado mais recentemente que tenha um ID externo para as atualizações.
* Se o ID externo não existir, a Braze priorizará o perfil atualizado mais recentemente com o e-mail correspondente.
* Se não existir nenhum perfil com o e-mail fornecido, a Braze criará um novo perfil e um novo perfil de usuário de alias será criado. Para identificar os perfis de usuário de alias recém-criados, use o [endpoint `/users/identify`]({{site.baseurl}}/api/endpoints/user_data/post_user_identify).

{% alert note %}
Você também pode usar um número de telefone ou ID externo como parte da solicitação à Braze, se esses campos estiverem disponíveis e forem o identificador principal que você deseja usar para a integração. Para fazer isso, modifique sua carga útil de solicitação conforme indicado no [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track).
{% endalert %}

## Solução de problemas {#troubleshooting}

{% details Testei o Trigger e a Action com sucesso, então por que não consigo publicar meu Zap no Zapier? %}
Para usar essa integração, você precisa ter um <a href="https://zapier.com/app/pricing/" target="_blank">plano do Zapier</a> que suporte apps premium.
{% enddetails %}

{% details Por que os leads do Facebook não estão sincronizando com a Braze? %}
1. Verifique se você tem acesso de administrador à sua página do Facebook, conta de anúncios e acesso a leads. Em seguida, reconecte sua conta no Zapier.
2. Confirme se o formulário instantâneo que você criou no Facebook corresponde ao formulário selecionado na etapa de Trigger.
3. Verifique se você atribuiu o Zapier ao acesso de leads acessando **Facebook Business Manager** > **Integrations** > **Lead Access**.
{% enddetails %}

{% details Por que estou vendo perfis de usuário duplicados com o mesmo e-mail? %}
Existem maneiras específicas de criar e gerenciar perfis de usuário na Braze com base no [ciclo de vida do perfil de usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle).

Dependendo dos seus processos internos e de quando você está disparando a criação de clientes na Braze, pode haver perfis de usuário duplicados devido a uma condição de corrida entre a criação do perfil de usuário pela integração e a criação do usuário pelo seu sistema. Você pode [mesclar perfis de usuário]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) na Braze.
{% enddetails %}

{% details Não tenho uma conta no Zapier. Como posso disparar webhooks do Facebook Lead Ads para a Braze? %}
Se você não usa o Zapier e não planeja usá-lo, pode construir a integração diretamente do Facebook para a Braze. Consulte a <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/" target="_blank">documentação de Lead Ads</a> para saber mais.

Para recuperar leads do Facebook, use <a href="https://developers.facebook.com/docs/marketing-api/guides/lead-ads/retrieving#webhooks" target="_blank">webhooks</a>. Consulte a <a href="https://developers.facebook.com/docs/graph-api/webhooks/getting-started" target="_blank">documentação de Webhooks</a> para começar a usar webhooks no Facebook.

Depois de estabelecer a URL de webhooks no Facebook, trabalhe com sua equipe para determinar a melhor jornada para encaminhar os dados ao [endpoint `/users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track). De forma semelhante à abordagem do Zapier, recomendamos fazer uma [requisição por e-mail]({{site.baseurl}}/api/endpoints/user_data/post_user_track#update-a-user-profile-by-phone-number) por meio do endpoint `users/track`.
{% enddetails %}

{% alert tip %}
Para mais dicas de solução de problemas, consulte o <a href="https://help.zapier.com/hc/en-us/articles/8495982030861-Common-Problems-with-Facebook-Lead-Ads#h_01HC9V6Y652KQYYY96YG99T423" target="_blank">guia de solução de problemas de leads do Facebook</a> do Zapier.
{% endalert %}