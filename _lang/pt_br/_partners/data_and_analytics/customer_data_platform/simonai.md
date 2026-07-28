---
nav_title: Simon AI
article_title: Simon AI
description: "Use a integração da Braze com o Simon AI para criar e sincronizar públicos sofisticados com a Braze para orquestração, em tempo real e sem código."
alias: /partners/simon_data/
page_type: partner
search_tag: Partner
---

# Simon AI

> A plataforma de marketing agêntico [Simon AI][1] ajuda equipes de marketing a alcançar uma personalização verdadeiramente individual. Ela combina uma plataforma de dados do cliente composável com agentes de IA que operam diretamente no Snowflake AI Data Cloud para atuar como a equipe de dados e execução de um profissional de marketing.

Use a integração da Braze com o Simon AI para criar e sincronizar públicos avançados com a Braze para orquestração em tempo real e sem código. Com essa integração, você pode aproveitar a resolução de identidade, a unificação de dados de clientes e a segmentação orientada por IA do Simon AI para potencializar campanhas da Braze mais personalizadas e impactantes.

## Pré-requisitos {#prerequisites}

Para começar, você precisa autenticar sua conta da Braze dentro da sua conta do Simon AI.

| Requisito | Descrição |
| ------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Simon AI | Você precisa ter uma conta existente do Simon AI para aproveitar a integração com a Braze de dentro do Simon AI. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com as permissões `users.track`, `campaigns.trigger.schedule.create` e `campaigns.trigger.send`. <br><br> Ela pode ser criada no dashboard da Braze em **Configurações** > **Chaves de API**. |
| URL do dashboard da Braze | [Sua URL de endpoint REST][3]. Seu endpoint dependerá da URL da Braze para a sua instância. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

- Disparar um Canvas ou e-mail da Braze
- Passar e manter propriedades de Segment
- Sincronizar traits e propriedades de contato

{% alert note %}
Ao usar a integração do Simon com a Braze, o Simon envia apenas os deltas em cada sincronização para a Braze, evitando custos com dados irrelevantes. Consulte [Sincronizar traits e propriedades de contato](#sync-traits-and-contact-properties) para saber mais.
{% endalert %}

## Integração {#integration}

### Autentique sua conta da Braze no Simon AI {#authenticate-your-braze-account-in-simon-ai}

Para usar a integração com a Braze, primeiro autentique sua conta da Braze no Simon:

1. No menu de navegação, clique em **Integrations** e role até Braze.
2. Insira sua [chave da API REST][2] da Braze e sua [URL do dashboard][3].
3. Clique em **Save Changes**.

Uma conexão bem-sucedida exibe **Connected** na janela.

![Tela de integração no Simon AI][8]{: style="max-width:70%"}

### Adicione ações da Braze a Flows ou Journeys no Simon AI {#add-braze-actions-to-flows-or-journeys-in-simon-ai}

Depois de autenticar sua conta da Braze no Simon AI, você pode adicionar ações da Braze a [Flows][4] e [Journeys][5].

Três ações estão disponíveis:

- **Sync Simon segment attribute**: sincronize os detalhes do seu segmento com um atributo personalizado novo ou existente na Braze.
- **Trigger a Braze Canvas**: dispare um Canvas da Braze que aproveita os dados do seu segmento do Simon.
- **Send a Braze campaign**: lance uma Campaign inteira da Braze a partir do Simon.

![Menu suspenso mostrando a lista de ações disponíveis da Braze no Simon AI.][9]{: style="max-width:60%"}

Algumas ações estão disponíveis apenas para tipos específicos de Flows ou apenas para Journeys. Saiba mais em [docs.simondata.com][6].

### Sincronizar traits e propriedades de contato {#sync-traits-and-contact-properties}

Para minimizar o consumo de dados, você pode escolher traits específicos para sincronizar por padrão, em vez de atualizar todos os campos para todos os clientes em um segmento.

{% alert note %}
Para começar com a sincronização de traits, envie uma solicitação no [Simon Support Center](https://docs.simondata.com/docs/support-center). Seu gerente de conta informará quando você poderá prosseguir com as etapas a seguir.
{% endalert %}

Depois que o Contact Traits for ativado pelo seu gerente de conta:

1. No Simon, expanda **Admin Center** na navegação à esquerda e selecione **Sync Contact Traits**.
2. Escolha **Braze**. As propriedades de contato são exibidas aqui, aninhadas por dataset.
3. Selecione os campos que deseja sincronizar ao usar a integração do Simon com a Braze:
   1. **Number of traits** indica quantos traits estão disponíveis para escolha naquele dataset. Você pode escolher todos ou expandir a linha para selecionar campos individuais.
   2. Edite o **Downstream name** se quiser que os nomes dos campos apareçam de forma diferente quando chegarem na Braze.
   3. Se esta é a primeira vez que você integra com a Braze a partir do Simon, clique em **Backfill all contacts**. O backfill envia todos os pontos de dados para a Braze na primeira vez que você usa uma ação em um flow ou journey para garantir que todos os seus dados estejam totalmente sincronizados. Nas sincronizações subsequentes, apenas os traits que você escolher nesta tela serão enviados para a Braze. Isso ajuda a garantir que você seja cobrado apenas pelos dados de que precisa.

![Selecionando traits de sincronização no Simon AI.][10]

[1]: https://www.simon.ai/
[2]: {{site.baseurl}}/api/basics#creating-rest-api-keys
[3]: {{site.baseurl}}/user_guide/administer/personal/sdk_endpoints
[4]: https://docs.simondata.com/docs/campaigns-flows
[5]: https://docs.simondata.com/docs/campaigns-journeys-two
[6]: https://docs.simondata.com
[7]: https://docs.simondata.com/docs/support-center
[8]: {% image_buster /assets/img/simon_data/ConnecttoBraze.png %}
[9]: {% image_buster /assets/img/simon_data/BrazeActions.png %}
[10]: {% image_buster /assets/img/simon_data/BrazeTraitSyncing.png %}