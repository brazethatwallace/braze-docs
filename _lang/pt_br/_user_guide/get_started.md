---
nav_title: Começar
article_title: "Primeiros passos&#58; Visão geral da Braze"
page_order: 1
page_type: reference
description: "Familiarize-se com os conceitos principais que você precisará saber ao trabalhar na Braze."
---

# Primeiros passos: Visão geral da Braze {#get-started-braze-overview}

> Boas-vindas à Braze! Esta coleção de artigos vai ajudar você a começar a usar nossa plataforma e apresentar os principais termos, recursos e funcionalidades da Braze. Esta página apresenta os conceitos essenciais que você precisará conhecer ao trabalhar na Braze.

{% alert tip %}
Recomendamos fortemente que você confira nosso curso gratuito [Practitioner Learning Path](https://learning.braze.com/page/practitioner) junto com estes artigos. Não é necessário nenhum login ou conta especial. Se você é uma pessoa desenvolvedora e está buscando um resumo técnico da Braze, confira também <a href="/docs/developer_guide/getting_started/platform_overview">Primeiros passos para desenvolvedores</a>.
{% endalert %}

Nas seções de Primeiros passos, focamos nas implementações mais comuns da Braze. No entanto, a Braze é incrivelmente flexível e pode ser personalizada para agregar valor à sua organização de diversas formas. Para garantir clareza e objetividade, fornecemos uma visão geral descritiva da configuração padrão em vez de instruções rígidas. Reconhecemos que cada organização tem necessidades distintas, e a Braze foi criada para atender a uma ampla gama de opções de personalização que podem ser adaptadas às suas necessidades específicas.

Vamos explorar juntos o poder da Braze.

## Como a Braze funciona {#how-braze-works}

A Braze é uma plataforma de engajamento com clientes que ajuda marcas de todos os tamanhos a criar campanhas personalizadas e direcionadas em vários canais. A Braze oferece a capacidade de ouvir seus clientes, entender o que o comportamento deles está sinalizando e, então, agir enviando a mensagem certa, pelo canal certo, no momento certo.

{% alert tip %}
Não deixe de [adicionar seus colegas à Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users) para que eles possam explorar a plataforma com você.
{% endalert %}

## Usuários e Segments {#users-and-segments}

Os usuários são seus clientes — as pessoas que recebem as mensagens que você envia usando a Braze. Todos os dados que você coleta sobre um usuário e ingere na Braze são armazenados no perfil de usuário dele, como dados demográficos, informações pessoais, preferências e comportamentos. Essas informações alimentam o seu envio de mensagens e são a forma como você pode personalizar suas mensagens para o usuário certo.

![Captura de tela relacionada a usuários e Segments.]({% image_buster /assets/img/getting_started/user_profile.png %})

Segments dividem sua base de clientes em grupos menores que você pode direcionar com mensagens específicas. Você pode usar diferentes variáveis para criar Segments, desde características como gênero, local e idade até comportamentos como padrões de interação com Campaigns anteriores ou em que ponto da jornada do cliente eles estão.

Segments são dinâmicos — os usuários podem entrar e sair de Segments em tempo real com base no comportamento deles e na relação que têm com a sua marca. Isso garante que seus clientes recebam as mensagens mais relevantes para eles a qualquer momento. Você pode criar quantos Segments forem necessários para suas finalidades de direcionamento e envio de mensagens.

![Segments são dinâmicos — os usuários podem entrar e sair de Segments em tempo real com base no comportamento deles e na relação que têm com a sua marca. Isso garante que seus clientes recebam as mensagens mais relevantes para eles a qualquer momento. Você pode criar quantos Segments forem necessários para suas finalidades de direcionamento e envio de mensagens.]({% image_buster /assets/img/getting_started/segment.png %})

Para saber mais, confira: [Primeiros passos: Usuários e Segments]({{site.baseurl}}/user_guide/get_started/users_and_segments).

## Campaigns e Canvas {#campaigns-and-canvases}

Campaigns e Canvas são a forma como você envia mensagens para seus usuários.

As Campaigns são ideais para mensagens únicas enviadas a um Segment de público específico por meio de vários canais. Você pode utilizar qualquer um dos nossos canais de envio de mensagens compatíveis na sua Campaign (e-mail, push, In-App Messages, SMS e muito mais).

Os Canvas são fluxos de trabalho avançados de Campaign que permitem automatizar e orquestrar jornadas personalizadas do cliente em vários canais. Dentro de um Canvas, você pode configurar lógica de ramificação, postergações, pontos de decisão e eventos de conversão para guiar os clientes por uma série de interações. Os Canvas ajudam a garantir uma comunicação consistente e fluida em diferentes pontos de contato, aumentando as chances de engajamento e conversão do cliente.

Para saber mais, confira: [Primeiros passos: Campaigns e Canvas]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases).

## Espaços de trabalho {#workspaces}

Os espaços de trabalho agrupam seus dados — usuários, Segments, Campaigns e Canvas — em um único local. As informações não são compartilhadas entre espaços de trabalho, então leve isso em consideração ao adicionar websites e apps aos seus espaços de trabalho. Como prática recomendada, sugerimos colocar apenas versões diferentes do mesmo app ou de apps muito semelhantes no mesmo espaço de trabalho.

Exemplos de uso para espaços de trabalho incluem:

- Diferentes linhas de produtos ou apps
- Diferentes públicos (como motoristas de entrega versus clientes)
- Negócios separados
- Ambiente de testes

Para saber mais, confira: [Primeiros passos: Espaços de trabalho]({{site.baseurl}}/user_guide/get_started/workspaces).

## Integrando a Braze {#integrating-braze}

A Braze foi projetada para ser implementada de forma rápida e fácil. Nosso tempo médio de retorno de valor é de seis semanas em toda a nossa base de clientes com centenas de marcas.

![Captura de tela relacionada à integração da Braze.]({% image_buster /assets/img/getting_started/timetovalue.png %})

Aqui está o framework da Braze para estimar a duração da sua integração com base em quatro componentes nos quais você pode trabalhar em paralelo. O intervalo típico é de 30 a 180 dias, com a maioria das contas concluindo a integração entre 45 e 60 dias.

- **Nível de complexidade da migração de Campaigns:** O tempo necessário para migrar Campaigns depende de quantas você tem, do nível de personalização delas e dos seus recursos. Se você tem menos de dez Campaigns para migrar, levará menos de 60 dias. Mas se você tem mais de 100 Campaigns, será mais complicado. Se há apenas uma pessoa migrando 100 Campaigns, é diferente de 10 pessoas migrando 100.

{% alert tip %}
Precisa de ajuda com a sua migração? Nossos [parceiros certificados da Braze](https://www.braze.com/partners/solutions-partners) podem ajudar!
{% endalert %}

- **Volume de e-mail:** Para enviar e-mails, você precisará aquecer seus IPs. O [aquecimento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming) é o processo de construção da reputação do remetente com seus endereços de IP recém-atribuídos. Se você envia menos de 2 a 3 milhões de e-mails por dia, o aquecimento de IP deve levar 30 dias ou menos. Leve em conta o seu pico de envio. Se você normalmente envia 2 milhões de e-mails por dia, mas planeja enviar 7 milhões em um período sazonal, esse envio de "pico" é o que você deve usar como meta de aquecimento. Remetentes de alto volume podem usar vários IPs para acelerar o processo de aquecimento.
- **Complexidade organizacional:** Nosso processo de integração pode se adaptar às necessidades do seu negócio. Seja uma única unidade de negócios, um Centro de Excelência, várias unidades independentes ou uso de agências para complementar suas equipes, a Braze tem experiência em todos os cenários.
- **Sofisticação da infraestrutura de dados:** Se você está apenas implementando o SDK da Braze ou já tem uma plataforma de dados do cliente (CDP), é possível configurar tudo em apenas 30 dias. Usar uma CDP moderna pode acelerar o processo. Mas se você tem muitos sistemas de backend, ferramentas ou bancos de dados para conectar com a Braze, pode levar mais tempo e exigir mais recursos dedicados para concluir a configuração.

Para saber mais, confira: [Primeiros passos: visão geral da integração]({{site.baseurl}}/user_guide/get_started/integrations).