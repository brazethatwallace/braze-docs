---
nav_title: Criar e gerenciar espaços de trabalho
article_title: Criar e gerenciar espaços de trabalho
page_order: 0
layout: dev_guide
guide_top_header: "Criar e gerenciar espaços de trabalho"
guide_top_text: "Este artigo aborda como criar, configurar e gerenciar seus espaços de trabalho."
page_type: reference
description: "Este artigo aborda como criar, configurar e gerenciar seus espaços de trabalho."

guide_featured_title: "Artigos da seção"
guide_featured_list:
- name: Migrar dados entre espaços de trabalho
  link: /docs/user_guide/administer/global/create_and_manage_workspaces/migrate_workspace_data
  image: /assets/img/braze_icons/switch-horizontal-01.svg
---

<br>

# Criar e gerenciar espaços de trabalho {#create-and-manage-workspaces}

> Este artigo aborda como criar, configurar e gerenciar seus espaços de trabalho.

## O que é um espaço de trabalho? {#what-is-a-workspace}

Tudo o que você faz na Braze acontece dentro de um espaço de trabalho. Espaços de trabalho são um ambiente compartilhado para você acompanhar e gerenciar o engajamento de apps móveis ou sites relacionados. Espaços de trabalho agrupam apps iguais ou muito semelhantes: por exemplo, as versões Android e iOS do seu app móvel.

## Criando um espaço de trabalho {#creating-a-workspace}

### Etapa 1: Tenha um plano {#step-1-have-a-plan}

Antes de começar, certifique-se de que você trabalhou com sua equipe e com o gerente de integração da Braze para determinar a melhor configuração de espaço de trabalho para o seu caso de uso. Para saber mais sobre o planejamento dos seus espaços de trabalho na Braze, confira nosso guia [Primeiros passos: Espaços de trabalho]({{site.baseurl}}/user_guide/get_started/workspaces/).

### Etapa 2: Adicione seu espaço de trabalho {#step-2-add-your-workspace}

Você pode criar novos espaços de trabalho ou alternar entre espaços de trabalho existentes a partir do menu suspenso de espaço de trabalho no cabeçalho global.

1. Selecione o menu suspenso de espaço de trabalho e, em seguida, selecione <i class="fa-solid fa-square-plus" style="color: #0b8294;" aria-hidden="true"></i> **Criar espaço de trabalho**.

![O menu suspenso de espaço de trabalho com o botão "Criar espaço de trabalho".]({% image_buster /assets/img/workspaces/workspace_create.png %}){: style="max-width:60%;"}

{:start="2"}
2. Dê um nome ao seu espaço de trabalho.

{% alert tip %}
Você pode adotar uma convenção de nomenclatura para que outras pessoas na sua empresa encontrem facilmente o seu espaço de trabalho. Por exemplo: "Upon Voyage US – Production" e "Upon Voyage US – Staging".
{% endalert %}

{:start="3"}
3. Selecione **Criar**. Pode levar alguns segundos para a Braze criar seu espaço de trabalho.

![Modal "Criar espaço de trabalho" com o nome "Upon Voyage US - Staging".]({% image_buster /assets/img/workspaces/workspace_name.png %}){: style="max-width:60%" }

Você será direcionado para a página **Configurações do app** para começar a adicionar suas instâncias do app. Você pode acessar essa página a qualquer momento em **Configurações** > **Configurações do app**.

![Página "Configurações do app" para o espaço de trabalho Upon Voyage US - Staging com um botão para adicionar um app.]({% image_buster /assets/img/workspaces/workspace_empty_state.png %})

### Etapa 3: Adicione suas instâncias do app {#step-3-add-your-app-instances}

Nos referimos aos diferentes sites e apps coletados dentro de um espaço de trabalho como "instâncias do app".

1. Na página **Configurações do app**, selecione **+ Add app**.
2. Dê um nome à sua instância do app e selecione em qual plataforma ou plataformas essa instância do app está. Se você selecionar múltiplas plataformas, a Braze criará uma instância do app para cada plataforma.

![Modal "Add New App to Upon Voyage US - Staging" com opções para selecionar detalhes do app.]({% image_buster /assets/img/workspaces/workspace_add_app.png %}){: style="max-width:60%" }

{:start="3"}
3. Selecione **Add app** para confirmar.

#### Chaves de API do app {#app-api-keys}

Após adicionar sua instância do app, você terá acesso à sua chave de API. A chave de API é usada ao fazer solicitações entre sua instância do app e a API da Braze. A chave de API também é importante para integrar o SDK da Braze com seu app ou site.

![Página de configurações do app Upon Voyage iOS com campos para a chave de API e o endpoint de SDK.]({% image_buster /assets/img/workspaces/app_api_key.png %})

{% alert note %}
Você deve criar instâncias do app separadas para cada versão do seu app em cada plataforma. Por exemplo, se você tem versões Free e Pro do seu app tanto no iOS quanto no Android, crie quatro instâncias do app dentro do seu espaço de trabalho (app Free iOS, app Free Android, app Pro iOS e app Pro Android). Isso fornecerá quatro chaves de API para usar, uma para cada instância do app.
{% endalert %}

#### Versão ativa do SDK {#live-sdk-version}

A versão ativa do SDK exibida na página Configurações do app para um app específico é a versão mais alta do app com pelo menos 5% do total de sessões diárias e que teve pelo menos 500 sessões no último dia.

Esse campo aparece depois que você integra o SDK da Braze com seu app ou site. Se uma versão mais recente do SDK da Braze estiver disponível para sua plataforma, isso será indicado aqui com a tag "Newer Version Available".

![Seção "Versão ativa do SDK" com o valor do campo "5.4.0" e um ícone indicando que uma nova versão está disponível.]({% image_buster /assets/img/workspaces/app_live_sdk_version.png %})

### Etapa 4: Repita conforme necessário {#step-4-repeat-as-needed}

Repita as etapas 2 e 3 para configurar quantos espaços de trabalho seu plano exigir. Como prática recomendada, sugerimos que você crie um espaço de trabalho de teste para testes de integração e de Campaigns.

{% alert tip %}
**Adicione um espaço de trabalho de teste**<br>Você pode realizar testes do app isolando completamente certos usuários da sua instância de produção. Crie um novo espaço de trabalho e, ao publicar seu aplicativo, certifique-se de alterar a chave de API que a Braze está usando para que corresponda à do seu espaço de trabalho de produção, e não à do espaço de trabalho de teste.
{% endalert %}

## Gerenciando espaços de trabalho {#managing-workspaces}

### Adicionando favoritos {#adding-favorites}

Você pode adicionar espaços de trabalho favoritos para acessar os espaços de trabalho que você mais usa de forma ainda mais rápida.

![Menu suspenso de espaço de trabalho com a guia "Espaços de trabalho favoritos".]({% image_buster /assets/img/workspaces/workspace_favorites.png %}){: style="max-width:50%;"}

Para adicionar espaços de trabalho favoritos:

1. Selecione o menu suspenso do seu perfil e, em seguida, selecione **Gerenciar sua conta**.
2. Na seção **Perfil da conta**, localize o campo **Espaços de trabalho favoritos**.
3. Selecione seus espaços de trabalho na lista.
4. Selecione **Salvar alterações**.

Não há limite para o número de espaços de trabalho que você pode favoritar, mas recomendamos manter essa lista curta por conveniência.

### Renomeando espaços de trabalho {#renaming-workspaces}

Para renomear seu espaço de trabalho:

1. Acesse **Configurações** > **Configurações do app**.
2. Passe o cursor sobre o nome do seu espaço de trabalho e selecione <i class="fa-solid fa-pencil" style="color: #0b8294;" aria-hidden="true"></i> **Editar**.
3. Dê um novo nome ao seu espaço de trabalho e selecione <i class="fa-solid fa-square-check" style="color: #0b8294;" aria-hidden="true"></i> **Salvar**.

![O ícone de lápis aparecendo ao lado do nome do espaço de trabalho.]({% image_buster /assets/img/workspaces/workspace_rename.gif %}){: style="max-width:50%;"}

### Excluindo espaços de trabalho e instâncias do app {#deleting-workspaces-and-app-instances}

Para excluir seu espaço de trabalho ou instância do app:

1. Acesse **Configurações** > **Configurações do app**.
2. Selecione **Excluir espaço de trabalho** para excluir o respectivo espaço de trabalho, ou selecione o ícone de lixeira ao lado da respectiva instância do app.

Você não pode excluir instâncias do app ou espaços de trabalho que estejam sendo usados para direcionamento de usuários ou que tenham mais de 1.000 usuários. Se você tentar fazer isso, receberá uma mensagem de erro. Para prosseguir e excluí-los, [crie um caso de Suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support/) que inclua um link do dashboard e o nome da instância do app ou espaço de trabalho a ser excluído.

{% alert warning %}
Tenha cuidado ao excluir espaços de trabalho! Depois que um espaço de trabalho é excluído, ele não pode ser restaurado.
{% endalert %}

![A página Configurações do app com um botão para excluir um espaço de trabalho e um ícone de lixeira para excluir um app.]({% image_buster /assets/img/workspaces/workspace_delete.png %})

## Perguntas frequentes {#frequently-asked-questions}

### Devo criar um novo espaço de trabalho quando estou lançando um app atualizado? {#should-i-create-a-new-workspace-when-im-releasing-an-updated-app}

Isso depende de você estar atualizando seu app ou criando um totalmente novo.

#### Atualizando seu app {#updating-your-app}

Se você está atualizando seu app, deve separar as versões antiga e nova criando uma nova instância do app dentro do mesmo espaço de trabalho. Dessa forma, você pode direcionar efetivamente os usuários na nova versão ao selecionar esse app durante a segmentação. Se quiser enviar mensagens para usuários que estão na versão antiga, você pode usar filtros para [direcionar a versão anterior do app]({{site.baseurl}}/user_guide/messaging/campaigns/ideas_and_strategies/new_features/#filtering-by-most-recent-app-versions).

Se você criar um novo espaço de trabalho, seus usuários existirão em dois lugares: o espaço de trabalho antigo e o novo. Eles também podem potencialmente ter o mesmo token por push. Isso pode fazer com que os usuários recebam uma mensagem de marketing destinada apenas aos usuários do espaço de trabalho antigo, mesmo que já tenham feito o upgrade.

#### Lançando um novo app {#releasing-a-new-app}

Se você está lançando um app totalmente novo na loja de aplicativos, deve criar um novo espaço de trabalho. Ao criar um novo espaço de trabalho, todos os dados históricos e perfis de usuário da versão anterior do app não existirão nesse novo espaço de trabalho. Portanto, depois que os usuários existentes fizerem o upgrade para a nova versão do app, eles terão um novo perfil criado sem nenhum dos dados comportamentais do app antigo.

### Tenho múltiplas instâncias do app em um espaço de trabalho — como posso garantir que minha mensagem seja direcionada apenas para um único app? {#singular-app}

Para garantir que sua mensagem seja direcionada apenas para um app específico, adicione um segmento que inclua apenas usuários das instâncias do app escolhidas. Isso é especialmente importante se um usuário puder ter dois tokens por push para diferentes instâncias do app no mesmo espaço de trabalho. Nesse cenário, os usuários podem receber uma notificação de um app diferente daquele em que estão. Não é uma experiência ideal!

Por padrão, um segmento inclui todos os apps e sites no espaço de trabalho. Para configurar um segmento que inclua apenas um app ou site:

1. Crie um segmento com um nome significativo. Na Braze, usamos o formato "All Users ({Name} {Platform})". Por exemplo, "All Users (Upon Voyage iOS)".
2. Em **Apps and websites targeted**, selecione **Users from specific apps**.
3. No menu suspenso **Specific apps**, selecione seu app ou site.

![Segmento que está direcionando usuários de apps específicos.]({% image_buster /assets/img/workspaces/users_from_specific_apps_filter.png %})

Você pode então adicionar esse segmento à sua mensagem e começar a refinar ainda mais seu público com segmentos e filtros adicionais, se necessário.

#### Campaigns

Para Campaigns, adicione seu segmento à etapa **Público-alvo** do criador.

#### Canvas

No Canvas, adicione seu segmento às etapas de Mensagem, na seção **Delivery Validations**. As validações de entrega verificam novamente se seu público atende aos critérios de entrega no momento do envio da mensagem. Lembre-se de especificar validações de entrega para cada etapa de Mensagem para garantir que ela seja entregue ao app correto. Não é necessário segmentar no nível de entrada.

{% details Expandir para ver as etapas no fluxo de trabalho original do Canvas %}

No fluxo de trabalho original do Canvas, adicione seu segmento no nível do componente do Canvas, na seção **Audience**. Não é necessário segmentar no nível de entrada.

{% enddetails %}

## Próximas etapas {#next-steps}

Após criar seu espaço de trabalho, configure-o:

- [Configurações do espaço de trabalho]({{site.baseurl}}/user_guide/administer/global/workspace_settings/) para configurar chaves de API, preferências de e-mail, configurações de push e mais.
- [Gerenciar usuários da empresa]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/) para adicionar usuários e atribuir permissões para este espaço de trabalho.