---
nav_title: Segments
article_title: Segments
page_order: 3
layout: dev_guide
guide_top_header: "Segments"
guide_top_text: "A segmentação de público é essencial para o marketing estratégico — ela pode evitar que você direcione demais, incomode ou perca uma conexão potencial com um cliente. Confira os artigos a seguir para saber como segmentar e filtrar seu público para o maior benefício de todos."
descriptions: "A segmentação de público é essencial para o marketing estratégico — ela pode evitar que você direcione demais, incomode ou perca uma conexão potencial com um cliente. Confira esta landing page para saber como segmentar e filtrar seu público para o maior benefício de todos."
search_rank: 4
tool: Segments
page_type: landing
description: "Esta landing page abrange artigos sobre segmentação dentro de Campaigns no dashboard. Aqui, você encontra informações sobre como configurar um Segment or segmento or segmento, filtros, funis, insights, extensões e muito mais."

guide_featured_title: "Artigos da seção"
guide_featured_list:
  - name: Criar um segmento
    link: /docs/user_guide/audience/segments/creating_a_segment
    image: /assets/img/braze_icons/pie-chart-01.svg
  - name: Gerenciar segmentos
    link: /docs/user_guide/audience/segments/managing_segments
    image: /assets/img/braze_icons/edit-05.svg
  - name: Filtros de segmentação
    link: /docs/user_guide/audience/segments/segmentation_filters
    image: /assets/img/braze_icons/flag-02.svg
  - name: Dados do segmento
    link: /docs/user_guide/audience/segments/segment_data
    image: /assets/img/braze_icons/bar-chart-01.svg
  - name: Extensões de segmento
    link: /docs/user_guide/audience/segments/segment_extension
    image: /assets/img/braze_icons/users-01.svg
  - name: Insights de segmento
    link: /docs/user_guide/audience/segments/segment_insights
    image: /assets/img/braze_icons/pie-chart-01.svg

guide_menu_title: "Mais artigos"
guide_menu_list:
  - name: Direcionamento por local
    link: /docs/user_guide/audience/segments/location_targeting
    image: /assets/img/braze_icons/marker-pin-06.svg
  - name: Expressões regulares
    link: /docs/user_guide/audience/segments/regex
    image: /assets/img/braze_icons/search-sm.svg
  - name: Medir o tamanho do segmento
    link: /docs/user_guide/audience/segments/measuring_segment_size
    image: /assets/img/braze_icons/pie-chart-02.svg
  - name: "Caso de uso: segmentar com atributos personalizados aninhados"
    link: /docs/user_guide/audience/segments/segment_with_nested_custom_attributes
    image: /assets/img/braze_icons/dataflow-02.svg
  - name: Solução de problemas
    link: /docs/user_guide/audience/segments/troubleshooting
    image: /assets/img/braze_icons/annotation-question.svg

---

## Sobre os segmentos da Braze {#about-braze-segments}

Na Braze, os segmentos são grupos dinâmicos de usuários que atendem a critérios específicos definidos por você, como atributos de usuário, comportamento do usuário e eventos personalizados. Você pode ser granular com os critérios aninhando segmentos dentro de outros segmentos e aplicando recursos adicionais, refinando o escopo do seu público para enviar conteúdo altamente personalizado e envolvente para os usuários certos.

Você pode criar quantos segmentos quiser para direcionar usuários. Explore diferentes combinações de recursos de Segment or segmento or segmento e filtros de segmentação para descobrir formas criativas de utilizar seus dados de usuários e desbloquear novas maneiras de enviar mensagens relevantes e aumentar o engajamento.

Confira os casos de uso abaixo para uma pequena prévia de como os segmentos da Braze podem ajudar você a direcionar seus usuários.

### Casos de uso {#use-cases}

- **Mensagens de boas-vindas:** segmente novos usuários para enviar e-mails de integração ou mensagens no app que apresentem seu aplicativo.
- **Recompensas de fidelidade:** segmente usuários com base na frequência de compras, aniversário de associação ou outros marcos, e envie ofertas exclusivas ou recompensas para seus usuários mais fiéis.
- **Gatilhos comportamentais:** segmente usuários com base em suas ações, como abandonar um carrinho no checkout, para disparar mensagens no app ou notificações por push.
- **Recomendações de itens:** segmente usuários que compraram produtos específicos e envie recomendações de produtos complementares ou de nível superior.
- **Testes A/B:** segmente usuários para testes A/B com diferentes mensagens, linhas de assunto ou conteúdos para determinar o que funciona melhor com usuários de idades, gêneros e outros atributos específicos.

#### Casos de uso de extensões de Segment or segmento or segmento {#segment-extension-use-cases}

Você pode refinar ainda mais seus segmentos usando [extensões de Segment or segmento or segmento]({{site.baseurl}}/user_guide/audience/segments/segment_extension) para direcionar usuários com base em eventos personalizados ou comportamento de compra armazenados durante toda a vida útil do perfil de usuário.

- **Compras históricas:** segmente usuários por terem comprado uma cor específica de um produto específico pelo menos duas vezes nos últimos dois anos.
- **Eventos e interações com mensagens:** segmente usuários por terem feito uma compra nos últimos trinta dias e também interagido com uma mensagem no app específica.
- **Consultar dados:**
  - **Consultar Snowflake:** segmente usuários com dados combinados da Braze e de fontes externas, como um CRM ou um data warehouse, usando [extensões de Segment or segmento or segmento SQL]({{site.baseurl}}/user_guide/audience/segments/segment_extension/sql_segments) para consultar o Snowflake.
  - **Sincronizar do data warehouse:** segmente usuários com dados sincronizados diretamente do seu data warehouse ou sistema de armazenamento de arquivos para a Braze usando [extensões de Segment or segmento or segmento CDI]({{site.baseurl}}/user_guide/audience/segments/segment_extension/cdi_segments).