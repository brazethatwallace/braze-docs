---
nav_title: Dados
article_title: "Plataforma de Dados da Braze"
page_order: 3
description: "Saiba mais sobre a Plataforma de Dados da Braze, incluindo como unificar, ativar e distribuir seus dados."
---

# Plataforma de Dados da Braze {#braze-data-platform}

> Saiba mais sobre a Plataforma de Dados da Braze, incluindo como unificar, ativar e distribuir seus dados.

A Plataforma de Dados da Braze (BDP) é um conjunto abrangente e componível de recursos de dados e integrações com parceiros que permite criar experiências personalizadas para seus clientes. Na Braze, pensamos em dados em termos de três tarefas relacionadas a dados: [Unificação]({{site.baseurl}}/user_guide/data/unification), [Ativação]({{site.baseurl}}/user_guide/data/activation) e [Distribuição]({{site.baseurl}}/user_guide/data/distribution).

Ao usar uma combinação de recursos da Plataforma de Dados da Braze, você pode alavancar seus dados para criar mensagens significativas e direcionadas que respondem ao que seus clientes fazem em tempo real.

## Como funciona {#how-it-works}

### Unifique seus dados {#unify-your-data}

Os dados de usuários fluem para a Braze por diversos pontos de entrada. Colete e consolide dados primários de qualquer fonte usando [APIs]({{site.baseurl}}/api/home) e [SDKs]({{site.baseurl}}/developer_guide/sdk_integration). Você também pode usar ferramentas de ingestão integradas, como a [Cloud Data Ingestion]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion), para criar uma integração direta do seu data warehouse ou solução de armazenamento de arquivos com a Braze, ou usar a [Data Transformation]({{site.baseurl}}/user_guide/data/unification/data_transformation) para criar e gerenciar integrações de webhook para transferir dados para a Braze.

### Ative seus dados {#activate-your-data}

Limpe, organize e prepare seus dados para uso. Isso envolve entender os comportamentos e preferências dos seus clientes em tempo real com perfis de usuários e segmentos. Consulte o [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/analytics/metrics_glossary) ao criar mensagens direcionadas e use [catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs) para enriquecer suas mensagens com dados de produtos ou conteúdo. Identifique como seus clientes estão respondendo a essas experiências personalizadas.

### Distribua seus dados {#distribute-your-data}

Transmita e [exporte seus dados]({{site.baseurl}}/user_guide/data/distribution/export_braze_data) para sistemas externos para insights e decisões de próximas etapas. Use o [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) para transmitir dados de eventos da Braze para um data warehouse e alimentar ferramentas de business intelligence. Você também pode expandir suas capacidades de dados com [integrações com parceiras de tecnologia]({{site.baseurl}}/partners/data_and_analytics).

## Infraestrutura de dados {#data-infrastructure}

A infraestrutura de dados da Braze inclui [centros de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_centers) que ajudam a minimizar a latência — o tempo que os dados levam para viajar entre o servidor e o usuário. Essa distribuição geográfica permite que nossos serviços sejam confiáveis e escalonáveis. Também oferecemos [criptografia em nível de campo]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption) para ajudar a proteger dados sensíveis e minimizar informações de identificação pessoal (IPI) compartilhadas na Braze. Para saber mais sobre uso e faturamento, consulte [Pontos de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points).

## Princípios fundamentais {#core-principles}

Os dados desempenham um papel crucial na melhoria da sua estratégia de engajamento do cliente, permitindo criar experiências personalizadas, entender o comportamento do cliente e otimizar estratégias de envio de mensagens. Na Braze, construímos todas as capacidades de dados com três princípios fundamentais em mente:

{% details Fazendo seus dados trabalharem mais %}
- **Flexível e baseado em componentes:** Nosso objetivo principal é ajudar você a utilizar seus dados de forma mais eficaz e completa. Construída com uma arquitetura componível, você pode alavancar as tecnologias que precisa para fazer seus dados trabalharem mais, sem middleware desnecessário.
- **Integrações com parceiros:** A Braze prioriza integrações com as melhores tecnologias do ecossistema (e oferece APIs) que tornam o compartilhamento de dados bidirecional e em tempo real algo simples.
- **Arquitetura de processamento de fluxo:** Você pode disparar ações com base em qualquer ponto de dados ingerido na Braze para segmentação, orquestração e personalização.
{% enddetails %}

{% details Aprimorando a agilidade dos dados para impulsionar o desempenho %}
- **Construção flexível de públicos:** Reduza a dependência de equipes técnicas para criar públicos e entregar engajamento personalizado do cliente em escala.
- **Velocidade e desempenho:** Dados e insights de engajamento são entregues em tempo real, o que apoia um engajamento iterativo e eficaz do cliente, além de uma tomada de decisão de negócios mais ampla.
{% enddetails %}

{% details Mantendo seus dados seguros, protegidos e em conformidade %}
- **Práticas de segurança líderes do setor:** Realizamos auditorias regulares de terceiros, incluindo SOC 2 Tipo 2 e ISO 27001, para cumprir os mais altos padrões do setor. Mantemos um programa público de recompensa por bugs para abordar proativamente vulnerabilidades potenciais e temos uma equipe de segurança dedicada a proteger seus dados.
- **Conformidade do setor:** Fornecemos ferramentas que promovem a adesão a regulamentações de proteção de dados, incluindo GDPR e CCPA.
- **Privacidade de dados:** Você pode gerenciar o consentimento do usuário final, processar solicitações e executar ações sobre os direitos do consumidor.
{% enddetails %}