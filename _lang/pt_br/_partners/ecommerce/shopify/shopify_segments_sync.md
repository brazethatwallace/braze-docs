---
nav_title: Sincronização de segmentos do Shopify
article_title: Sincronização de segmentos do Shopify
alias: /shopify_segments_sync/
page_order: 8
description: "Este artigo de referência explica como sincronizar segmentos do Shopify na Braze como coortes para gerenciamento e direcionamento unificado de público."
---

# Sincronização de segmentos do Shopify {#shopify-segments-sync}

> A sincronização de segmentos do Shopify estende sua loja Shopify para a Braze, dando à sua equipe de marketing acesso direto a dados de usuários mais ricos que residem no Shopify, incluindo sinais que não são capturados pela integração padrão da Braze com o Shopify. Ao sincronizar segmentos do Shopify como coortes, você alinha as definições de público em ambas as plataformas e entrega experiências de usuário consistentes e coordenadas, seja direcionando-os no Shopify ou alcançando-os por meio de uma Campaign na Braze.

{% alert important %}
A sincronização de segmentos do Shopify está atualmente em beta. Para solicitar acesso, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Integração Braze com Shopify | O app Braze Shopify deve estar instalado na sua loja Shopify e conectado a um espaço de trabalho da Braze. Para instruções de configuração, consulte [Configuração da integração padrão com Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration) ou [Configuração da integração personalizada com Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration). |
| Permissão de usuário no Shopify | O usuário do Shopify que iniciar a sincronização de segmentos deve ter a permissão **Export** para exportar dados de usuários. Para saber mais sobre permissões no Shopify, consulte a [documentação de permissões de loja do Shopify](https://help.shopify.com/en/manual/your-account/users/roles/permissions/store-permissions#customers-permissions). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Como funciona {#how-it-works}

A sincronização de segmentos da Shopify funciona em duas fases.

1. **Preenchimento inicial:** Quando você sincroniza um segmento pela primeira vez, a Braze preenche todos os membros atuais e cria uma coorte correspondente na Braze. O preenchimento é executado de forma assíncrona e pode levar alguns instantes para ser concluído.
2. **Sincronização contínua:** Após o preenchimento inicial, a Braze também se inscreve nos webhooks da Shopify para que a associação permaneça sincronizada em tempo quase real.

| Tópico do webhook | Efeito na Braze |
| --- | --- |
| `customer.joined_segment` | O usuário é adicionado à coorte correspondente na Braze. |
| `customer.left_segment` | O usuário é removido da coorte correspondente na Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Tópico do webhook" }

Se uma sincronização falhar, o modal da extensão de ação exibe um banner de erro explicando o que aconteceu e como proceder. Alguns erros oferecem a ação **Retry sync**. Outros exigem uma alteração de administrador ou de configuração.

## Integração de importação de dados {#data-import-integration}

### Etapa 1: Selecione um segmento do Shopify para sincronizar {#step-1-select-a-shopify-segment-to-sync}

No Shopify, acesse **Customers** > **Segments** e selecione o segmento que deseja sincronizar com a Braze. Você pode sincronizar qualquer segmento criado usando a segmentação nativa do Shopify, incluindo segmentos baseados em histórico de pedidos, compras de produtos, tags de clientes, gasto vitalício e metafields.

![Painel de segmentos com lista de segmentos do Shopify.]({% image_buster /assets/img/shopify/shopify_segments.png %})

### Etapa 2: Inicie a sincronização {#step-2-initiate-the-sync}

1. Na página de detalhes do segmento no Shopify, abra o menu suspenso **Use segment** e selecione **Braze Segment Sync**.

![Página de detalhes do segmento com um menu suspenso "Use segment" que possui a opção "Braze Segment Sync".]({% image_buster /assets/img/shopify/braze_segment_sync.png %})

{: start="2"}
2. O modal da extensão de ação da Braze é aberto, exibindo o nome do segmento e o tamanho do público. Selecione **Sync with Braze** para iniciar a importação.

![Modal com um botão para sincronizar com a Braze.]({% image_buster /assets/img/shopify/sync_with_braze.png %}){:style="max-width:70%;"}

{: start="3"}
3. O modal transiciona para um estado de sincronização e exibe um banner de progresso enquanto a Braze importa os membros.

![Modal mostrando a sincronização em andamento.]({% image_buster /assets/img/shopify/sync_in_progress.png %}){:style="max-width:70%;"}

{: start="4"}
4. Selecione **Close**. A sincronização continua em segundo plano. Fechar o modal não a interrompe.

Para verificar se a sincronização foi concluída, feche e reabra o modal. Quando a sincronização terminar, o modal será aberto com um banner de sucesso.

![Modal confirmando que a sincronização está ativa.]({% image_buster /assets/img/shopify/braze_sync_active.png %}){:style="max-width:70%;"}

### Etapa 3: Crie um Segment na Braze com o filtro de participação em coorte {#step-3-create-a-braze-segment-with-the-cohort-membership-filter}

Na Braze, acesse **Audience** > **Segments** e crie um novo segmento. Em **Add Filter**, selecione o filtro **Cohort Membership** e escolha o segmento sincronizado do Shopify no menu suspenso. Após salvar, você pode referenciar esse Segment da Braze ao direcionar usuários em uma Campaign ou Canvas.

![Criador de segmentos com o filtro "Shopify Cohorts".]({% image_buster /assets/img/shopify/segment_builder_cohort_import.png %})

## Ressincronização de um segmento {#re-syncing-a-segment}

Depois que um segmento é sincronizado, você pode atualizar a associação de coorte a qualquer momento usando a mesma extensão de ação.

1. No Shopify, abra o segmento sincronizado e selecione **Use segment** > **Braze Segment Sync**.
2. No modal, selecione **Sync now**.
3. Na caixa de diálogo de confirmação, selecione **Sync now** para iniciar a ressincronização.

A ressincronização é aditiva: usuários que correspondem ao segmento atual do Shopify são adicionados à coorte, mas os usuários que não correspondem mais permanecem na coorte.

## Gerenciando segmentos sincronizados na Braze {#managing-synced-segments-in-braze}

Você pode gerenciar todos os segmentos sincronizados a partir do dashboard da Braze. Acesse **Integrações com parceiros** > **Parceiros de tecnologia**, selecione sua integração com a Shopify e abra a guia **Gerenciar usuários**.

### Status de sincronização {#sync-status}

Cada segmento sincronizado tem um status de sincronização.

| Status | Descrição |
| --- | --- |
| **Sincronizando** | A Braze está importando os membros do segmento. |
| **Na fila** | O segmento está aguardando um slot de sincronização disponível. |
| **Ativo** | O segmento está sincronizado e as atualizações de membros ocorrem quase em tempo real. |
| **Pausado** | As atualizações de membros para este segmento estão pausadas. |
| **Erro** | A última tentativa de sincronização falhou. Selecione **Tentar sincronização novamente** para tentar de novo. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Status de sincronização" }

### Sincronizando segmentos em massa {#syncing-segments-in-bulk}

Para sincronizar segmentos adicionais, edite a integração, acesse a etapa **Gerenciar usuários** e selecione **Editar segmentos** na seção **Sincronizar segmentos**. No modal de seleção:

- Selecione qualquer quantidade de segmentos. 25 segmentos são sincronizados por vez; o restante entra na fila automaticamente.
- Segmentos que já estão sendo sincronizados ficam bloqueados. Para remover um segmento, exclua-o na Shopify.

Salve suas alterações para iniciar as sincronizações.

### Pausando um único segmento {#pausing-a-single-segment}

Para pausar a sincronização de um segmento, selecione **Pausar sincronização** na linha correspondente na tabela de segmentos e confirme. Quando a sincronização de um segmento é pausada:

- A coorte e seus membros permanecem na Braze e continuam disponíveis para direcionamento. Campaigns e Canvas que utilizam a coorte continuam enviando para os membros atuais da coorte.
- As atualizações de membros são interrompidas.
- Renomear o segmento na Shopify ainda atualiza o nome de exibição da coorte.
- Excluir o segmento na Shopify ainda encerra o rastreamento.
- Solicitações de **Sincronizar agora** da extensão de ação da Shopify são rejeitadas.

Para retomar, selecione **Retomar sincronização** na linha correspondente. A Braze retoma as atualizações de membros e executa uma sincronização de recuperação. Usuários que saíram do segmento na Shopify enquanto a sincronização estava pausada permanecem na coorte da Braze.

### Pausando a sincronização de todos os segmentos {#pausing-all-segment-syncing}

Para pausar a sincronização de todos os segmentos de uma vez, edite a integração, selecione **Pausar sincronização** na seção **Sincronizar segmentos** da etapa **Gerenciar usuários** e salve suas configurações. Enquanto toda a sincronização de segmentos estiver pausada:

- A tabela de segmentos exibe apenas os nomes dos segmentos, com o status **Pausado** ao lado do título.
- As ações no nível da linha ficam indisponíveis até que você retome.
- A Braze não atualiza os nomes das coortes para renomeações na Shopify. Os nomes das coortes são atualizados quando você retomar.
- Solicitações de **Sincronizar agora** da extensão de ação são rejeitadas. A extensão continua exibindo o último status conhecido de cada segmento, e selecionar **Sincronizar agora** não inicia uma sincronização.

Para retomar, selecione **Retomar sincronização** na mesma seção e salve. A Braze sincroniza novamente de forma automática todos os segmentos previamente selecionados com uma sincronização de recuperação. Você não precisa selecioná-los novamente. Segmentos que você pausou individualmente permanecem pausados até que você os retome a partir da linha correspondente na tabela de segmentos.

## Atualizações de Segment no Shopify {#segment-updates-in-shopify}

### Renomear um segment {#renaming-a-segment}

Quando você renomeia um segment do Shopify, a Braze atualiza automaticamente o nome de exibição da coorte correspondente. Nenhuma ressincronização é necessária. A Braze também atualiza o nome da coorte enquanto a sincronização de um segment está pausada individualmente. Enquanto toda a sincronização de segments está pausada, a Braze atualiza os nomes das coortes quando você retoma.

### Alterar os critérios de um segment {#changing-segment-criteria}

A Braze não atualiza automaticamente os membros da coorte quando você altera os critérios de um segment do Shopify. Para incluir usuários que passaram a atender aos critérios, faça a ressincronização do segment a partir da extensão de ação. Os usuários que não atendem mais aos critérios permanecem na coorte porque a ressincronização não remove membros. Para saber mais, consulte [Ressincronizar um segment](#re-syncing-a-segment).

## Correspondência de usuários {#user-matching}

Os usuários sincronizados a partir de Segments da Shopify são correspondidos a perfis de usuário da Braze usando o alias `shopify_customer_id`, que é definido como parte da integração Braze com Shopify. Usuários sem um perfil de usuário correspondente na Braze são ignorados durante a sincronização.

Para saber mais sobre como a integração com a Shopify identifica e cria aliases de usuários, consulte [Recursos de dados da Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features).

A Braze faz a correspondência dos usuários sincronizados com os perfis de usuário existentes na Braze, independentemente de como esses perfis foram criados, incluindo por meio do preenchimento histórico da Shopify, da sua própria plataforma de dados (como Snowflake ou outro data warehouse) ou de importações diretas pela API. Se a sua coorte for menor do que o seu Segment da Shopify, isso significa que alguns membros do segmento ainda não possuem um perfil correspondente na Braze. Para aumentar a cobertura de correspondência, preencha os perfis de usuário na Braze pelo método de sua preferência antes de realizar a sincronização.

## Limitações {#limitations}

- **Sincronização unidirecional.** A associação ao Segment flui apenas do Shopify para a Braze. Alterações na associação à coorte feitas diretamente na Braze não são enviadas de volta ao Shopify.
- **Sem criação de perfil.** Apenas clientes do Shopify que já possuem um perfil de usuário na Braze são adicionados à coorte.
- **Não é possível interromper a sincronização a partir da Braze.** Para interromper a sincronização de um Segment, exclua-o no Shopify. A coorte e seus membros permanecem na Braze e param de ser atualizados.
- **A ressincronização apenas adiciona membros.** Ressincronizar um Segment adiciona novos usuários correspondentes à coorte, mas não remove usuários que não fazem mais parte do Segment no Shopify.