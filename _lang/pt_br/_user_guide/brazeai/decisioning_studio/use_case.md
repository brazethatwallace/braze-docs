---
nav_title: Caso de uso
article_title: "Caso de uso: Decisioning Studio"
description: "Este exemplo mostra como uma marca fictícia usa o BrazeAI Decisioning Studio™ e um agente de decisão para entregar conteúdo personalizado e sugestões de produtos em momentos-chave do cliente."
---

# Caso de uso: Recupere clientes inativos com um agente de decisão focado em receita {#use-case-win-back-lapsed-customers-with-a-revenue-focused-decisioning-agent}

> Este exemplo mostra como uma marca fictícia usa o BrazeAI Decisioning Studio™ e um agente de decisão para direcionar cada cliente à decisão ideal a partir do banco de ações, personalizar mensagens para recuperação e otimizar para receita. Ele conecta o design do agente, público e experimentos, orquestração pela Braze e aprendizado pós-lançamento.

Vamos supor que Poppy é uma gerente de CRM na Kitchenerie, uma marca fictícia de varejo online especializada em utensílios de cozinha.

Muitos clientes apenas navegam pelas coleções sazonais uma ou duas vezes antes de sair. Programas anteriores de recuperação usavam jornadas fixas e testes A/B manuais, que eram úteis para testar textos, mas não para aprender qual combinação de oferta, canal, cadência e timing maximiza a receita de compra para cada cliente. A prioridade da liderança é clara: trazer de volta o maior número possível de compradores inativos e aumentar a receita sem ultrapassar as regras de desconto ou frequência.

Este passo a passo descreve como Poppy:

- Define clientes inativos ou em risco como o público do agente, estruturando grupos de experimento para uma comparação justa
- Permite que o agente escolha as melhores ações permitidas a partir de um banco de ações rico, para que as mensagens permaneçam personalizadas em escala
- Configura a orquestração para que as decisões fluam para a Braze como plataforma de engajamento com clientes
- Lança o agente, permitindo que ele aprenda de forma autônoma o que impulsiona a receita de recuperação

## Etapa 1: Defina métricas de sucesso e "quem" o agente deve atingir {#step-1-define-success-metrics-and-who-the-agent-targets}

Poppy confirma a métrica de sucesso que o agente deve maximizar: receita de recompras entre clientes que pararam de comprar.

Ela define quem entra no programa: um Segment da Braze com compradores inativos ou usuários de alto valor que estão inativos. Agora, Poppy só precisa compartilhar qual Segment o agente deve atingir com a equipe de AI Decisioning Services. A integração para extrair os dados desse Segment acontece em segundo plano, sem que Poppy precise configurar uma integração.

## Etapa 2: Construa o banco de ações e as restrições {#step-2-build-the-action-bank-and-constraints}

Poppy mapeia as dimensões que importam para estratégias de recuperação:

- Oferta: frete grátis, percentual de desconto ou pacote de itens
- Canal: e-mail, push ou SMS
- Horário de envio ou cadência
- Criativo: ilustrações pequenas ou texto focado em utilidade

Para cada dimensão, ela lista opções concretas no banco de ações — as únicas ações que o agente pode tomar (todo o resto fica fora dos limites por design). O agente então experimenta combinações permitidas para descobrir o que funciona para cada cliente, otimizando a métrica de sucesso escolhida.

## Etapa 3: Prepare os dados e conecte a orquestração à Braze {#step-3-prepare-data-and-connect-orchestration-to-braze}

Seguindo [Conecte seus dados]({{site.baseurl}}/user_guide/brazeai/decisioning_studio/prepare_data/connect_data_sources/), Poppy garante que sinais ricos de dados primários (incluindo histórico de compras, afinidade de categoria, comportamento de navegação e engajamento) alimentem o agente para que cada decisão seja baseada em comportamento real.

Para a orquestração, ela usa o caminho nativo da Braze: o Decisioning Studio decide o que enviar e quando; a Braze entrega. Ela planeja modelos base (Campaigns disparadas por API) por canal com campos dinâmicos para ofertas e criativos, e configura a reelegibilidade.

## Etapa 4: Lance, monitore e otimize para receita {#step-4-launch-monitor-and-optimize-for-revenue}

Após a revisão de configuração com a equipe de AI Decisioning Services, Poppy lança o agente. O agente começa a recomendar ações por usuário e a orquestrar envios pela Braze para melhorar ao longo do tempo.

Ao combinar uma métrica de sucesso focada em receita com um agente de decisão que testa continuamente ações permitidas, a Kitchenerie passa de disparos estáticos de recuperação para decisões 1:1 que se adaptam por cliente, com o objetivo de recuperar mais clientes e aumentar a receita, respeitando as regras de negócio que Poppy definiu.