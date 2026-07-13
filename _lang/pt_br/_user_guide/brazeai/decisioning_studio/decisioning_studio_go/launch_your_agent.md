---
nav_title: Lance seu agente
article_title: Lance seu agente
page_order: 4
description: "Aprenda como lançar seu agente BrazeAI Decisioning Studio Go e configurar relatórios de Business as Usual (BAU) para comparação de desempenho."
---

# Lance seu agente {#launch-your-agent}

> Depois de conectar suas fontes de dados, configurar a orquestração e projetar seu agente, você está pronto para lançar. Este artigo aborda a ativação do seu agente e a configuração de relatórios BAU opcionais.

## Etapas de lançamento {#launch-steps}

Após concluir todas as etapas de configuração no portal Decisioning Studio Go:

1. Revise a configuração do seu agente para garantir que todas as configurações estejam corretas.
2. Verifique se sua integração CEP está ativa e se a orquestração está pronta.
3. Selecione **Launch** (ou ação equivalente) no portal Decisioning Studio Go para ativar seu agente.

Uma vez lançado, seu agente irá:
- Começar a receber dados do público do seu CEP
- Começar a fazer recomendações personalizadas para cada cliente
- Orquestrar envios por meio do seu CEP configurado
- Coletar dados de engajamento para aprender e melhorar ao longo do tempo

## Configure relatórios BAU {#set-up-bau-reporting}

Por padrão, os relatórios do portal Decisioning Studio Go comparam o grupo do Decisioning Studio Go com o grupo de controle aleatório. Se você tiver uma campanha Business as Usual (BAU) existente com a qual gostaria de comparar, pode configurar relatórios BAU para visualizar os três grupos em um só lugar.

### Benefícios dos relatórios BAU {#benefits-of-bau-reporting}

O principal benefício de configurar relatórios BAU é a aplicação da filtragem de cliques inválidos do Decisioning Studio Go. Quando aplicada a todos os três grupos do experimento, isso permite a comparação de desempenho de cliques mais precisa e justa ("comparação equilibrada") ao remover ruídos de:
- Cliques suspeitos de máquina
- Cliques no link de cancelamento de inscrição

### Requisitos para relatórios BAU {#requirements-for-bau-reporting}

Antes de configurar os relatórios BAU, certifique-se de uma comparação justa entre o grupo de tratamento BAU, o grupo Decisioning Studio Go e o grupo de controle aleatório:

- **Sem sobreposição:** nenhum destinatário pode pertencer a mais de um grupo durante toda a duração do experimento
- **Atribuição aleatória:** os destinatários são atribuídos aleatoriamente aos grupos sem viés
- **Opções iguais:** quaisquer opções disponíveis para o grupo BAU (criativo, frequência, tempo, incentivo ou oferta) estão disponíveis para os grupos Decisioning Studio Go e controle aleatório

{% alert warning %}
Sem um design de experimento equilibrado, os relatórios BAU podem ser confusos ou enganosos.
{% endalert %}

### Informações necessárias {#required-information}

Após validar o design do seu experimento, reúna os seguintes detalhes para configurar os relatórios BAU:

**IDs de Campaign do seu CEP:**

| CEP | Tipos aceitos |
|-----|---------------|
| **Braze** | Campaigns e Canvas |
| **Salesforce Marketing Cloud** | Apenas jornadas |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Informações necessárias" }

**ID do público do seu CEP:**

| CEP | Tipos aceitos |
|-----|---------------|
| **Braze** | Apenas Segments |
| **Salesforce Marketing Cloud** | Apenas extensões de dados |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Informações necessárias" }

Se você não tiver um público existente que rastreie seu público BAU, deve criar um.

### Considerações {#considerations}

- **Apenas KPIs de cliques:** semelhante ao Decisioning Studio Go de forma mais geral, os relatórios BAU cobrem apenas KPIs de cliques, não KPIs de conversão.
- **Limitações do Canvas:** atualmente, não oferecemos suporte à filtragem por IDs de etapas específicas do Canvas. Eventos de todas as etapas do Canvas serão incluídos nos dados BAU. Isso pode invalidar comparações com o BAU se apenas certas etapas do Canvas devem ser incluídas.

### Configure relatórios BAU

Siga as instruções no portal do Decisioning Studio Go. Você deve ter:
- Um ou mais IDs de Campaign onde todas as comunicações são comunicações BAU
- Um ID de público que rastreia os destinatários no público BAU a cada dia

## Monitore seu agente {#monitor-your-agent}

Após o lançamento, monitore o desempenho do seu agente no portal do Decisioning Studio Go:

- **Métricas de engajamento:** rastreie as taxas de cliques entre os grupos do experimento
- **Progresso de aprendizado:** observe como as recomendações do agente evoluem ao longo do tempo
- **Comparações de grupos:** compare o desempenho do Decisioning Studio Go com o controle aleatório e o BAU (se configurado)

{% alert tip %}
Aguarde pelo menos 2 a 4 semanas de coleta de dados antes de tirar conclusões sobre o desempenho. O agente precisa de interações suficientes para aprender e otimizar de forma eficaz.
{% endalert %}

## Solução de problemas {#troubleshooting}

Se o seu agente não estiver se saindo como esperado:

1. **Verifique a orquestração:** confirme que sua integração CEP está ativa, que as Campaigns e jornadas estão em execução e que não há limites globais ou regras semelhantes interferindo na orquestração.
2. **Verifique o fluxo de dados:** confirme que os dados do público e os dados de engajamento estão sendo capturados corretamente.
3. **Revise os grupos do experimento:** garanta a atribuição aleatória adequada e que não haja sobreposição entre os grupos.
4. **Fale com o suporte:** entre em contato com o suporte da Braze para mais assistência.