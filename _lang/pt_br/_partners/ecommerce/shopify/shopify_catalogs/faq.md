---
nav_title: FAQ
article_title: FAQ sobre sincronização de produtos do Shopify
page_order: 0
page_type: FAQ
description: "Esta página fornece respostas para perguntas frequentes sobre a sincronização de produtos do Shopify com catálogos da Braze."
---

# Perguntas frequentes {#frequently-asked-questions}

> Esta página fornece respostas para algumas perguntas frequentes sobre a [sincronização de produtos do Shopify]({{site.baseurl}}/shopify_catalogs).

## Comportamento do catálogo e da sincronização {#catalog-and-sync-behavior}

### Posso editar meu catálogo do Shopify diretamente na Braze? {#can-i-edit-my-shopify-catalog-directly-in-braze}

Não. O catálogo do Shopify é somente leitura na Braze. Qualquer edição manual pode ser sobrescrita pela próxima sincronização. Faça todas as atualizações de produtos diretamente no Shopify.

### Como excluo meu catálogo do Shopify? {#how-do-i-delete-my-shopify-catalog}

Para excluir seu catálogo do Shopify, desative a sincronização na página de parceiro do Shopify. Não exclua o catálogo diretamente pela página **Catálogos**. A desativação remove todo o catálogo, incluindo todas as tags, coleções e dados de metafield sincronizados. Antes de desativar, atualize ou pause quaisquer Campaigns ou Canvas que façam referência a esse catálogo, pois eles podem enviar mensagens com detalhes de produto ausentes.

### O que acontece se eu excluir um produto ou campo de produto previamente sincronizado no Shopify? {#what-happens-if-i-delete-a-previously-synced-product-or-product-field-in-shopify}

A Braze remove automaticamente o produto ou campo do seu catálogo do Shopify quando detecta a exclusão. No entanto, quaisquer Campaigns, Canvas ou Segments que façam referência ao produto ou campo excluído deixarão de funcionar. Antes de excluir produtos ou campos no Shopify, verifique se eles não estão sendo usados ativamente na Braze.

### Como altero meu ID de catálogo (identificador de produto)? {#how-do-i-change-my-catalog-id-product-identifier}

Para alterar seu ID de catálogo, primeiro desative a sincronização e confirme que nenhuma mensagem ativa faz referência a esses dados do catálogo. Em seguida, execute novamente a sincronização inicial e selecione o identificador desejado.

### Alterar minhas tags, coleções ou metafields sincronizados afetará Campaigns ativas? {#will-changing-my-synced-tags-collections-or-metafields-affect-active-campaigns}

Sim. Alterar suas seleções sincronizadas pode afetar Campaigns, Canvas ou [seleções de catálogo]({{site.baseurl}}/catalog_selections) ativas que façam referência a elas. Verifique se seu conteúdo ativo está atualizado antes de fazer alterações.

### Quanto tempo leva a sincronização inicial? {#how-long-does-the-initial-sync-take}

O tempo de sincronização depende do número de produtos e variantes na sua loja. A sincronização inicial busca os produtos em lotes, então pode levar algum tempo para que todas as tags de produto, metafields e associações de coleção apareçam. Monitore o status da sincronização na página de parceiro do Shopify.

## Configuração e limites {#configuration-and-limits}

### Quantas tags, coleções ou metafields posso sincronizar? {#how-many-tags-collections-or-metafields-can-i-sync}

Você pode sincronizar até 20 de cada por configuração:

- Até 20 tags de produto
- Até 20 coleções
- Até 20 metafields de produto

### E se um produto pertencer a mais de 250 coleções? {#what-if-a-product-belongs-to-more-than-250-collections}

O Shopify permite que produtos pertençam a mais de 250 coleções, mas a Braze só consegue buscar as primeiras 250 associações de coleção por produto. Se um produto pertence a uma coleção selecionada que está fora das primeiras 250 buscadas, essa associação não será refletida no seu catálogo do Shopify. Se você notar associações de coleção ausentes, entre em contato com seu gerente de sucesso do cliente.

### Por que não vejo todas as minhas coleções no modal de configuração? {#why-dont-i-see-all-my-collections-in-the-configuration-modal}

O modal de configuração exibe até 5.000 das coleções atualizadas mais recentemente. Se sua loja exceder esse limite, coleções mais antigas podem não aparecer. Coleções previamente selecionadas que estejam fora das 5.000 principais ainda serão exibidas na sua seleção.

### Posso filtrar por tags e coleções ao mesmo tempo em uma única seleção de catálogo? {#can-i-filter-by-both-tags-and-collections-in-a-single-catalog-selection}

Não. As seleções de catálogo suportam apenas um campo de array por filtro de seleção. Não é possível combinar tags e coleções na mesma seleção. Se você precisa segmentar usuários com base em critérios de tag e coleção simultaneamente, use [extensões de segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension) com consultas de SQL.

### Quais são os limites de seleção de catálogo? {#what-are-the-catalog-selection-limits}

As seleções de catálogo estão sujeitas aos mesmos limites das seleções de catálogo padrão. Para detalhes sobre limites de itens, restrições de filtro e limites de armazenamento por plano, consulte [Seleções de catálogo]({{site.baseurl}}/catalog_selections).

## Metacampos e solução de problemas {#metafields-and-troubleshooting}

### Por que alguns dos meus tipos de metacampo não aparecem? {#why-are-some-of-my-metafield-types-not-showing-up}

Apenas os tipos de metacampo compatíveis aparecem no modal de configuração. Os seguintes tipos não são compatíveis no momento: `dimension`, `json`, `link`, `money`, `rating`, `rich_text_field`, `volume` e `weight`. Para ver os tipos compatíveis e a lista completa, consulte [Metacampos de produto do Shopify]({{site.baseurl}}/shopify_catalogs#shopify-product-metafields) na página de sincronização de produtos do Shopify.

### Recebi o erro "Duplicate Metafield Column Name". O que devo fazer? {#i-got-a-duplicate-metafield-column-name-error-what-do-i-do}

Dois ou mais dos metacampos selecionados criariam o mesmo nome de coluna no catálogo. Desmarque um dos metacampos conflitantes ou renomeie a chave do metacampo no Shopify para que cada um corresponda a um nome de coluna único. Em seguida, salve novamente sua configuração.

### Por que minhas tags estão demorando mais do que o esperado para carregar? {#why-are-my-tags-taking-longer-than-expected-to-load}

As tags são buscadas diretamente do Shopify quando você abre o modal de configuração. Se sua loja tem um grande número de produtos ou tags, o carregamento pode demorar mais. Esse é um comportamento esperado e não afeta o desempenho da sincronização. Se o carregamento expirar consistentemente, tente reduzir o número total de tags na sua loja do Shopify ou entre em contato com o suporte.

## Armazenamento {#storage}

### A sincronização de dados adicionais de produtos afeta meu armazenamento de catálogo? {#will-syncing-additional-product-data-affect-my-catalog-storage}

Sim. Sincronizar tags, metafields e coleções aumenta o uso de armazenamento do seu catálogo. O nível gratuito de catálogo tem um limite de armazenamento de 100 MB. Se a sua sincronização exceder o limite, a Braze para de sincronizar e as atualizações de produtos não serão mais refletidas. Entre em contato com o seu gerente de conta para fazer upgrade do seu nível, se necessário.