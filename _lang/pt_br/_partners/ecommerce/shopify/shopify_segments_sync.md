---
nav_title: Sincronização de segmentos do Shopify
article_title: Sincronização de segmentos do Shopify
alias: /shopify_segments_sync/
page_order: 8
description: "Este artigo de referência explica como sincronizar segmentos do Shopify na Braze como coortes para gerenciamento e direcionamento unificado de público."
---

# Sincronização de segmentos do Shopify {#shopify-segments-sync}

> A sincronização de segmentos do Shopify estende sua loja Shopify para a Braze, dando à sua equipe de marketing acesso direto a dados de usuários mais ricos que residem no Shopify, incluindo sinais que não são capturados pela integração padrão da Braze com o Shopify. Ao sincronizar segmentos do Shopify como coortes, você alinha as definições de público em ambas as plataformas e entrega experiências de usuário consistentes e coordenadas, seja quando um usuário é direcionado no Shopify ou engajado por meio de uma Campaign na Braze.

{% alert important %}
A sincronização de segmentos do Shopify está atualmente em beta. Para solicitar acesso, entre em contato com seu gerente de sucesso do cliente.
{% endalert %}

## Pré-requisitos {#prerequisites}

| Requisito | Descrição |
| --- | --- |
| Integração da Braze com o Shopify | O app Braze Shopify deve estar instalado na sua loja Shopify e conectado a um espaço de trabalho da Braze. Para instruções de configuração, consulte [Configuração da integração padrão do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_standard_integration/) ou [Configuração da integração personalizada do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_custom_integration/). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Prerequisites" }

## Como funciona {#how-it-works}

A sincronização de segmentos do Shopify funciona em duas fases.

1. Quando você sincroniza um segmento pela primeira vez, a Braze faz o backfill de todos os membros atuais e cria uma coorte correspondente na Braze. O backfill é executado de forma assíncrona e pode levar alguns instantes para ser concluído.
2. Durante a sincronização inicial, a Braze faz o backfill dos membros atuais e se inscreve nos webhooks do Shopify para que a associação permaneça sincronizada em tempo quase real.

| Tópico do webhook | Efeito na Braze |
| --- | --- |
| `customer.joined_segment` | O usuário é adicionado à coorte correspondente na Braze. |
| `customer.left_segment` | O usuário é removido da coorte correspondente na Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Webhook topic" }

Se uma sincronização falhar, o modal da extensão de ação exibirá um banner de erro com uma ação recomendada. Selecione **Sync with Braze** para tentar novamente.

## Integração de importação de dados {#data-import-integration}

### Etapa 1: Selecionar um segmento do Shopify para sincronizar {#step-1-select-a-shopify-segment-to-sync}

No Shopify, acesse **Customers** > **Segments** e selecione o segmento que deseja sincronizar com a Braze. Você pode sincronizar qualquer segmento criado usando a segmentação nativa do Shopify, incluindo segmentos baseados em histórico de pedidos, compras de produtos, tags de clientes, gasto vitalício e metafields.

![Painel de segmentos com lista de segmentos do Shopify.]({% image_buster /assets/img/shopify/shopify_segments.png %})

### Etapa 2: Iniciar a sincronização {#step-2-initiate-the-sync}

1. Na página de detalhes do segmento no Shopify, abra o menu suspenso **Use segment** e selecione **Braze Segment Sync**.

![Página de detalhes do segmento com um menu suspenso "Use segment" que possui a opção "Braze Segment Sync".]({% image_buster /assets/img/shopify/braze_segment_sync.png %})

{: start="2"}
2. No modal da extensão de ação da Braze que se abre, exibindo o nome do segmento e o tamanho do público, selecione **Sync with Braze** para iniciar a importação.

![Modal com um botão para sincronizar com a Braze.]({% image_buster /assets/img/shopify/sync_with_braze.png %}){:style="max-width:70%;"}

{: start="3"}
3. Selecione **Done**.

![Modal confirmando que a sincronização está ativa.]({% image_buster /assets/img/shopify/braze_sync_active.png %}){:style="max-width:70%;"}

### Etapa 3: Criar um Segment na Braze com o filtro Cohort Membership {#step-3-create-a-braze-segment-with-the-cohort-membership-filter}

Na Braze, acesse **Audience** > **Segments** e crie um novo Segment. Em **Add Filter**, selecione o filtro **Cohort Membership** e escolha o segmento do Shopify sincronizado no menu suspenso. Após salvar, você pode referenciar esse Segment da Braze ao direcionar usuários em uma Campaign ou Canvas.

![Criador de segmentos com o filtro "Shopify Cohorts".]({% image_buster /assets/img/shopify/segment_builder_cohort_import.png %})

## Correspondência de usuários {#user-matching}

Os usuários sincronizados a partir de segmentos do Shopify são correspondidos aos perfis de usuário da Braze usando o alias `shopify_customer_id`, que é definido como parte da integração da Braze com o Shopify. Usuários sem um perfil de usuário correspondente na Braze são ignorados durante a sincronização.

Para saber mais sobre como a integração com o Shopify identifica e cria aliases de usuários, consulte [Recursos de dados do Shopify]({{site.baseurl}}/partners/ecommerce/shopify/shopify_data_features/).

## Limitações {#limitations}

- **Sincronização unidirecional.** A associação ao segmento flui apenas do Shopify para a Braze. Alterações na associação à coorte feitas diretamente na Braze não são enviadas de volta ao Shopify.
- **Sem criação de perfil.** Apenas clientes do Shopify que já possuem um perfil de usuário na Braze são adicionados à coorte.
- **Sincronizações não podem ser desfeitas.** Quando um segmento do Shopify é sincronizado, a ação não pode ser desfeita.