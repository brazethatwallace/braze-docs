---
nav_title: Lançar seu agente
article_title: Lançar seu agente
page_order: 5
page_type: reference
description: "Saiba como lançar seu agente do Decisioning Studio e fechar o loop de tomada de decisões por IA para otimização com autoaprendizado."
---

# Lançar seu agente {#launch-your-agent}

> Depois de conectar as fontes de dados, configurar a orquestração e projetar seu agente, você está pronto para o lançamento. Este artigo aborda a ativação do seu agente e o fechamento do loop de tomada de decisões por IA para que o agente possa aprender e melhorar continuamente.

## Etapas de lançamento {#launch-steps}

Após concluir todas as etapas de configuração com sua equipe de AI Decisioning Services:

1. Revise a configuração do seu agente para garantir que todos os ajustes estejam corretos.
2. Verifique se suas conexões de dados e integrações de orquestração estão ativas.
3. Trabalhe com sua equipe de AI Decisioning Services para ativar o agente.

Uma vez lançado, seu agente vai:
- Começar a receber dados de público e dados de cliente
- Começar a fazer recomendações personalizadas para cada cliente
- Orquestrar ações por meio da sua plataforma de engajamento com clientes configurada
- Coletar dados de feedback para aprender e melhorar ao longo do tempo

## Fechar o loop de tomada de decisões por IA {#close-the-ai-decisioning-loop}

Uma vez lançado, seu agente precisa de dados de feedback para aprender e melhorar. Isso inclui dados de conversões, dados de engajamento e dados de ativações que informam ao agente o que aconteceu após as decisões de engajamento com clientes serem enviadas.

Para requisitos detalhados sobre a preparação desses ativos de dados de feedback essenciais, consulte [Preparando suas fontes de dados]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data).

{% alert note %}
Se o agente estiver nativamente integrado com a plataforma de engajamento com clientes (como a Braze ou o Salesforce Marketing Cloud), pode não haver etapas de configuração adicionais necessárias para os dados de feedback, já que eles podem ser enviados automaticamente com os dados de cliente.
{% endalert %}

## Monitorar seu agente {#monitor-your-agent}

Após o lançamento, trabalhe com sua equipe de AI Decisioning Services para monitorar o desempenho:

- **Métricas de desempenho:** acompanhe sua métrica de sucesso entre os grupos de experimento
- **Progresso de aprendizado:** observe como as recomendações do agente evoluem ao longo do tempo
- **Insights:** entenda quais dimensões e opções estão gerando resultados para diferentes segmentos de clientes

## Otimização contínua {#ongoing-optimization}

Sua equipe de AI Decisioning Services continuará trabalhando com você para:

- Analisar o desempenho do agente e identificar oportunidades de otimização
- Expandir dimensões ou opções conforme necessário
- Ajustar restrições com base em mudanças nas regras de negócios
- Escalar agentes bem-sucedidos para casos de uso adicionais

{% alert tip %}
O agente aprende e melhora continuamente ao longo do tempo. Permita tempo suficiente para que o agente colete dados e otimize antes de fazer mudanças significativas na configuração.
{% endalert %}