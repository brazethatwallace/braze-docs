---
nav_title: Outubro
page_order: 4
noindex: true
page_type: update
description: "Este artigo contém notas de versão de outubro de 2018."
---
# Outubro de 2018 {#october-2018}

{% comment %}
  Adicione-os em um momento posterior...
  Alternância do grupo de controle de seleção inteligente
  A caixa Intelligent Selection agora tem uma caixa de seleção que permite [ativar ou desativar o uso de um grupo de controle]({{site.baseurl}}/user_guide/engagement_tools/campaigns/testing_and_more/multivariate_testing#including-a-control-group). Quando ativado, o grupo de controle será 20% do tamanho do público e mudará à medida que o recurso Intelligent Selection otimizar os tamanhos de público por variante.
  Assistente de configurações de entrada de canvas (Beta)
  A interface do usuário do Canva será simplificada para evitar a perda de tarefas e os erros resultantes. As configurações de canvas, especificamente, agora serão exibidas em um assistente, semelhante ao design do assistente de campanhas. No momento, isso não está refletido em nossa documentação, pois está sendo implementado gradualmente. Volte em breve para saber mais sobre isso!
  API do grupo de inscrições (oculto)
  O Braze disponibilizou uma nova chamada GET para ativar a solicitação com base em um ID ou endereço de e-mail externo. Em seguida, serão fornecidos todos os grupos de inscrições associados a esse usuário.
{% endcomment %}

## Calcular estatísticas exatas de público para Campaigns {#calculate-exact-audience-stats-for-campaigns}

Agora você pode acessar **Campaign Analytics** e calcular as estatísticas exatas do seu público. Clique em **Calculate Exact Stats** no rodapé da seção **Target Audiences**, e as estatísticas exatas do público serão preenchidas. Você precisará salvar a Campaign antes de calcular (Campaigns em rascunho serão salvas como rascunhos).

## Descontinuação do Windows 8 {#windows-8-deprecation}

A Braze não oferece mais suporte ao Windows 8 desde 10 de outubro de 2018.

## Hub de parcerias {#partnerships-hub}

Agora você pode encontrar uma lista das suas integrações na plataforma Braze em **Integrações**, junto com chaves de integração e instruções.

## Cálculos de análise de dados de e-mail {#email-analytics-calculations}

A Braze agora está calculando todas as análises de dados de e-mail usando os dados de eventos do nosso parceiro de envio de e-mail (provedor de serviços de e-mail) para melhorar significativamente a precisão das nossas análises de dados de e-mail. Essa solução utiliza o Postgres, uma solução de banco de dados de código aberto, para garantir a integridade dos dados.

{% alert important %}
As aberturas únicas e os cliques únicos ainda dependem dos dados agregados fornecidos pelos nossos parceiros de envio de e-mail. Há um trabalho em andamento para calcular essas estatísticas de unicidade usando a mesma infraestrutura introduzida nesta versão.
{% endalert %}

## Controles do painel do criador {#composer-panel-controls}

Os controles do criador de mensagem foram atualizados para incluir descrições associadas aos ícones, possibilitando melhor usabilidade e navegação.

## Azure para Currents {#azure-for-currents}

Os clientes da Braze que usam o Currents agora podem ver o [Azure]({{site.baseurl}}/partners/data_and_analytics/cloud_storage/microsoft_azure_blob_storage_for_currents) como uma integração em potencial.

## Expansões dos campos de entrada {#input-field-expansions}

Agora é possível expandir as caixas de entrada para linhas de assunto de e-mail e títulos de push.