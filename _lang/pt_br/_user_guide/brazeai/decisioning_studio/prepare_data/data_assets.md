---
nav_title: Ativos de dados críticos
article_title: Ativos de dados críticos para o Decisioning Studio
page_order: 3
page_type: reference
description: "Este artigo de referência aborda os ativos de dados obrigatórios e opcionais para o BrazeAI Decisioning Studio, incluindo os dados de feedback necessários para fechar o ciclo de tomada de decisões por IA."
---

# Ativos de dados críticos {#critical-data-assets}

> O Decisioning Studio requer determinados ativos de dados para funcionar e se beneficia de dados opcionais adicionais. Este artigo descreve o que é cada ativo, por que ele é importante e quais campos são obrigatórios.

## Fechar o ciclo de tomada de decisões por IA {#close-the-ai-decisioning-loop}

Os três ativos de eventos obrigatórios (ativações, engajamentos e conversões) formam juntos o ciclo de feedback que permite ao Decisioning Studio aprender e melhorar ao longo do tempo.

- **Ativações** informam ao modelo o que ele decidiu fazer
- **Engajamentos** informam ao modelo como os clientes responderam à mensagem
- **Conversões** informam ao modelo se o resultado de negócio desejado foi alcançado

Cada um desses ativos deve ser estruturado como um fluxo de eventos incremental (não um snapshot). Consulte [Snapshots versus fluxos de eventos]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/data_streams/) para mais detalhes.

{% alert note %}
Se o Decisioning Studio estiver integrado nativamente à sua plataforma de engajamento com clientes (como a Braze ou o Salesforce Marketing Cloud), os dados de ativação e engajamento podem ser coletados automaticamente sem configuração adicional. Consulte a documentação de configuração para confirmar.
{% endalert %}

## Ativos obrigatórios {#required-assets}

### Perfil do cliente {#customer-profile}

Os dados de perfil do cliente descrevem quem são seus clientes. O Decisioning Studio usa esses dados para entender o estado atual de cada cliente e gerar recomendações relevantes.

Atributos de perfil comuns incluem:

- Anos como cliente
- Localização geográfica (quando permitido pelo seu setor e requisitos de privacidade)
- Canal de aquisição (por exemplo, web, telefone, loja física)
- Pontuação de satisfação ou sentimento
- Pontuações derivadas de modelos (por exemplo, propensão ao churn, estimativa de lifetime value)
- Nível de fidelidade ou participação em programa

### Dados de ativação e engajamento {#activation-and-engagement-data}

Os dados de ativação registram o que o Decisioning Studio realmente enviou: qual recomendação foi entregue a qual cliente por qual canal. Os dados de engajamento registram o que o cliente fez em resposta: se abriu, clicou ou interagiu de alguma outra forma com a mensagem.

Para integrações nativas com a Braze, os dados de ativação e engajamento podem estar disponíveis automaticamente por meio do Braze Currents. Para outras configurações, esses dados devem ser fornecidos explicitamente.

Esses dados são essenciais porque fecham o ciclo entre uma recomendação e seu resultado. Sem eles, o modelo não consegue aprender quais decisões estão funcionando.

### Dados de conversões {#conversions-data}

Os dados de conversão descrevem o que aconteceu com o cliente após uma recomendação ter sido feita e uma mensagem ter sido enviada. Esse é o sinal principal que o modelo usa para avaliar se uma recomendação foi bem-sucedida.

| Requisito | Motivo |
|-------------|--------|
| Cada registro contém o identificador do cliente, consistente com todos os outros ativos | O Decisioning Studio precisa conseguir associar as conversões às recomendações que as precederam. |
| Cada registro tem um timestamp de quando o evento de conversão ocorreu | A precisão do timing é essencial para a atribuição. O modelo precisa saber a qual recomendação uma conversão pode ser atribuída. |
| Se estiver usando uma métrica de sucesso não binária (por exemplo, receita em vez de convertido ou não convertido), o valor da métrica deve ser incluído em cada registro de conversão | O Decisioning Studio usa o valor da métrica para gerar experiências de treinamento. Sem o valor, o modelo só consegue aprender que uma conversão aconteceu, não o quão valiosa ela foi. |
| Se as conversões podem ser atribuídas diretamente a uma comunicação específica (por exemplo, resgate de cupom), inclua os campos necessários para associar a conversão ao registro de ativação | A atribuição direta fornece ao modelo o sinal de aprendizado mais claro. Se a atribuição direta não for possível, o Decisioning Studio usa atribuição baseada em proximidade como fallback. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Ativos opcionais {#optional-assets}

Mais dados geralmente levam a um melhor desempenho do modelo, mas isso deve ser equilibrado com o esforço de implementação necessário. Os seguintes ativos opcionais são comumente úteis:

### Comportamento do cliente {#customer-behavior}

- Histórico de login na conta
- Tipo de dispositivo e sistema operacional
- Interações com o atendimento ao cliente (por exemplo, número de chamadas de suporte, tópicos discutidos)
- Uso do produto (por exemplo, horas de uso por dia, funcionalidades acessadas, categorias de conteúdo visualizadas)

### Outras transações {#other-transactions}

- Produtos comprados por data, incluindo atributos do produto
- Valores das transações
- Canais de transação (por exemplo, loja física versus online)
- Métodos de pagamento

### Outros engajamentos de marketing {#other-marketing-engagement}

- Comunicações enviadas fora das recomendações do Decisioning Studio (por exemplo, e-mails, SMS)
- Engajamento de e-mail não disparado pelo Decisioning Studio (por exemplo, aberturas, cliques)
- Respostas a pesquisas (por exemplo, pontuações NPS, pesquisas de engajamento)
- Atividade em web e app mobile (por exemplo, páginas navegadas, produtos visualizados)