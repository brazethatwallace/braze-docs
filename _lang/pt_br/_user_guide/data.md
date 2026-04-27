---
nav_title: Dados
article_title: Dados
page_order: 3
description: "Saiba mais sobre a Plataforma de Dados da Braze, incluindo como unificar, ativar e distribuir seus dados."
---

# Plataforma de Dados da Braze {#braze-data-platform}

> Saiba mais sobre a Plataforma de Dados da Braze, incluindo como unificar, ativar e distribuir seus dados.

A Plataforma de Dados da Braze (BDP) é um conjunto abrangente e componível de recursos de dados e integrações de parceiros que permite criar experiências personalizadas para seus clientes. Na Braze, pensamos em dados em termos de três tarefas relacionadas a dados: [Unificação]({{site.baseurl}}/user_guide/data/unification/), [Ativação]({{site.baseurl}}/user_guide/data/activation/) e [Distribuição]({{site.baseurl}}/user_guide/data/distribution/).

Ao usar uma combinação de recursos da Plataforma de Dados da Braze, você pode aproveitar seus dados para criar mensagens significativas e direcionadas que respondem ao que seus clientes fazem em tempo real.

## Como funciona {#how-it-works}

### Unifique seus dados {#unify-your-data}

Os dados de usuários fluem para a Braze por muitos pontos de entrada. Colete e consolide dados primários de qualquer origem usando [APIs]({{site.baseurl}}/api/home/) e [SDKs]({{site.baseurl}}/developer_guide/sdk_integration/). Você também pode usar ferramentas de ingestão integradas, como a [Ingestão de dados na nuvem]({{site.baseurl}}/user_guide/data/unification/cloud_ingestion/), para criar uma integração direta do seu data warehouse ou solução de armazenamento de arquivos com a Braze, ou usar a [Transformação de dados]({{site.baseurl}}/user_guide/data/unification/data_transformation/) para criar e gerenciar integrações de webhook para transferir dados para a Braze.

### Ative seus dados {#activate-your-data}

Limpe, organize e prepare seus dados para uso. Isso envolve entender os comportamentos e preferências dos seus clientes em tempo real com perfis de usuário e segmentos. Consulte o [Glossário de métricas de relatórios]({{site.baseurl}}/user_guide/analytics/metrics_glossary/) ao criar mensagens direcionadas e use [catálogos]({{site.baseurl}}/user_guide/data/activation/catalogs/) para enriquecer suas mensagens com dados de produtos ou conteúdo. Identifique como seus clientes estão respondendo a essas experiências personalizadas.

### Distribua seus dados {#distribute-your-data}

Transmita e [exporte seus dados]({{site.baseurl}}/user_guide/data/distribution/export_braze_data/) para sistemas externos para obter insights e tomar decisões. Use o [Braze Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) para transmitir dados de eventos da Braze para um data warehouse e alimentar ferramentas de business intelligence. Você também pode estender seus recursos de dados com [integrações de parceiros de tecnologia]({{site.baseurl}}/partners/data_and_analytics/).

## Infraestrutura de dados {#data-infrastructure}

A infraestrutura de dados da Braze inclui [centros de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_centers/) que ajudam a minimizar a latência — o tempo que os dados levam para trafegar entre o servidor e o usuário. Essa distribuição geográfica permite que nossos serviços sejam confiáveis e escaláveis. Também oferecemos [criptografia em nível de campo]({{site.baseurl}}/user_guide/data/infrastructure/field_level_encryption/) para ajudar a proteger dados sensíveis e minimizar informações pessoais identificáveis (IPI) compartilhadas na Braze. Para mais informações sobre uso e faturamento, consulte [Pontos de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points/).

## Princípios fundamentais {#core-principles}

Os dados desempenham um papel crucial no aprimoramento da sua estratégia de engajamento do cliente, permitindo criar experiências personalizadas, entender o comportamento do cliente e otimizar estratégias de envio de mensagens. Na Braze, desenvolvemos todos os recursos de dados com três princípios fundamentais em mente:

{% details Fazendo seus dados trabalharem mais %}
- **Flexível e baseado em componentes:** Nosso objetivo principal é ajudar você a utilizar seus dados de forma mais eficaz e completa. Com uma arquitetura componível, você pode aproveitar as tecnologias necessárias para fazer seus dados trabalharem mais, sem middleware desnecessário.
- **Integrações de parceiros:** A Braze prioriza integrações com as melhores tecnologias do ecossistema (e oferece APIs) que facilitam o compartilhamento bidirecional de dados em tempo real.
- **Arquitetura de processamento de fluxo:** Você pode disparar ações em qualquer ponto de dados ingerido na Braze para segmentação, orquestração e personalização.
{% enddetails %}

{% details Aumentando a agilidade dos dados para impulsionar o desempenho %}
- **Construção flexível de público:** Reduza a dependência de equipes técnicas para criar públicos e proporcionar engajamento personalizado do cliente em escala.
- **Velocidade e desempenho:** Os dados de engajamento e os insights são fornecidos em tempo real, o que dá suporte ao engajamento iterativo e eficaz do cliente, bem como à tomada de decisões de negócios mais amplas.
{% enddetails %}

{% details Mantendo seus dados seguros, protegidos e em conformidade %}
- **Práticas de segurança líderes do setor:** Realizamos auditorias regulares de terceiros, incluindo SOC 2 Tipo 2 e ISO 27001, para cumprir os mais altos padrões do setor. Mantemos um programa público de recompensa por bugs para lidar proativamente com possíveis vulnerabilidades e temos uma equipe de segurança dedicada e comprometida com a proteção dos seus dados.
- **Conformidade com o setor:** Fornecemos ferramentas que promovem a adesão aos regulamentos de proteção de dados, incluindo o GDPR e a CCPA.
- **Privacidade de dados:** Você pode gerenciar o consentimento do usuário final, processar solicitações e agir de acordo com os direitos do consumidor.
{% enddetails %}