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
Recomendamos fortemente que você confira nosso curso gratuito [Braze Foundations for Everyone](https://learning.braze.com/page/braze-foundations-for-everyone) junto com estes artigos. Não é necessário nenhum login ou conta especial para esse curso. Se você é uma pessoa desenvolvedora e está buscando um resumo técnico da Braze, confira também [Primeiros passos para desenvolvedores]({{site.baseurl}}/developer_guide/getting_started/platform_overview/).
{% endalert %}

Nas seções de Primeiros passos, focamos nas implementações mais comuns da Braze. No entanto, a Braze é incrivelmente flexível e pode ser personalizada para agregar valor à sua organização de diversas formas. Para garantir clareza e objetividade, fornecemos uma visão geral descritiva da configuração padrão em vez de instruções rígidas. Reconhecemos que cada organização tem necessidades distintas, e a Braze foi criada para atender a uma ampla gama de opções de personalização que podem ser adaptadas às suas necessidades específicas.

Vamos explorar juntos o poder da Braze.

## Como a Braze funciona {#how-braze-works}

A Braze é uma plataforma de engajamento com clientes que ajuda marcas de todos os tamanhos a criar campanhas personalizadas e direcionadas em vários canais. A Braze oferece a capacidade de ouvir seus clientes, entender o que o comportamento deles está sinalizando e então agir, enviando a mensagem certa, pelo canal certo, no momento certo.

{% alert tip %}
Não se esqueça de [adicionar seus colegas à Braze]({{site.baseurl}}/user_guide/administer/global/user_management/manage_company_users/) para que possam explorar a plataforma com você.
{% endalert %}

## Usuários e segmentos {#users-and-segments}

Os usuários são seus clientes — as pessoas que recebem as mensagens que você envia usando a Braze. Todos os dados que você coleta sobre um usuário e ingere na Braze são armazenados no perfil do usuário, como dados demográficos, informações pessoais, preferências e comportamentos. Essas informações alimentam o envio de mensagens e permitem que você personalize suas mensagens para o usuário certo.

![]({% image_buster /assets/img/getting_started/user_profile.png %})

Os segmentos dividem sua base de clientes em grupos menores que podem ser direcionados com mensagens específicas. Você pode usar diferentes variáveis para criar segmentos, desde características como gênero, local e idade até comportamentos como padrões de interação com campanhas anteriores ou em que ponto da jornada do cliente eles se encontram.

Os segmentos são dinâmicos — os usuários podem entrar e sair dos segmentos em tempo real com base em seu comportamento e em sua relação com a sua marca. Isso garante que seus clientes recebam as mensagens mais relevantes para eles em qualquer momento. Você pode criar quantos segmentos forem necessários para fins de direcionamento e envio de mensagens.

![]({% image_buster /assets/img/getting_started/segment.png %})

Para saber mais, confira: [Primeiros passos: Usuários e segmentos]({{site.baseurl}}/user_guide/get_started/users_and_segments/).

## Campanhas e Canvas {#campaigns-and-canvases}

Campanhas e Canvas são as formas de enviar mensagens aos seus usuários.

As campanhas são ideais para mensagens individuais enviadas a um segmento específico de público em vários canais. Você pode usar qualquer um dos nossos canais de envio de mensagens compatíveis na sua campanha (e-mail, push, mensagens no app, SMS e muito mais).

Os Canvas são fluxos de trabalho avançados que permitem automatizar e orquestrar jornadas personalizadas de clientes em vários canais. Em um Canvas, você pode configurar lógica de ramificação, postergações, pontos de decisão e eventos de conversão para guiar os clientes por uma série de interações. Os Canvas ajudam a garantir uma comunicação consistente e contínua em diferentes pontos de contato, aumentando as chances de engajamento e conversão do cliente.

Para saber mais, confira: [Primeiros passos: Campanhas e Canvas]({{site.baseurl}}/user_guide/get_started/campaigns_and_canvases/).

## Espaços de trabalho {#workspaces}

Os espaços de trabalho agrupam seus dados — usuários, segmentos, campanhas e Canvas — em um único local. As informações não são compartilhadas entre espaços de trabalho, então tenha isso em mente ao adicionar sites e apps aos seus espaços de trabalho. Como prática recomendada, sugerimos colocar apenas versões diferentes do mesmo app ou de apps muito semelhantes em um único espaço de trabalho.

Exemplos de usos para espaços de trabalho incluem:

- Diferentes linhas de produtos ou apps
- Diferentes públicos (como motoristas de entrega e clientes)
- Negócios separados
- Ambiente de teste

Para saber mais, confira: [Primeiros passos: Espaços de trabalho]({{site.baseurl}}/user_guide/get_started/workspaces/).

## Integrando a Braze {#integrating-braze}

A Braze foi projetada para entrar em operação de forma rápida e fácil. Nosso tempo médio de obtenção de valor é de seis semanas em nossa base de clientes de centenas de marcas.

![]({% image_buster /assets/img/getting_started/timetovalue.png %})

Aqui está a estrutura da Braze para estimar a duração da sua integração com base em quatro componentes nos quais você pode trabalhar em paralelo. O intervalo típico é de 30 a 180 dias, com a maioria das contas concluindo sua integração em 45 a 60 dias.

- **Nível de complexidade da migração de campanhas:** O tempo necessário para migrar campanhas depende de quantas você tem, de quão personalizadas elas são e dos seus recursos. Se você tiver menos de dez campanhas para migrar, levará menos de 60 dias. Mas se tiver mais de 100 campanhas, será mais complicado. Uma pessoa migrando 100 campanhas é bem diferente de 10 pessoas migrando 100.

{% alert tip %}
Precisa de ajuda com sua migração? Nossos [parceiros certificados da Braze](https://www.braze.com/partners/solutions-partners) podem ajudar!
{% endalert %}

- **Volume de e-mail:** Para enviar e-mails, você precisará fazer o aquecimento dos seus IPs. O [aquecimento de IP]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming/) é o processo de construção da reputação do remetente com seus endereços IP recém-atribuídos. Se você enviar menos de 2-3 milhões de e-mails por dia, o aquecimento de IP deve levar 30 dias ou menos. Tenha em mente seu pico de envio. Se você normalmente envia 2 milhões de e-mails por dia, mas planeja enviar 7 milhões em um período sazonal, esse "pico" de envio é o que deve ser considerado no aquecimento. Remetentes de alto volume podem usar vários IPs para acelerar o processo de aquecimento.
- **Complexidade organizacional:** Nosso processo de integração pode se adaptar às necessidades da sua empresa. Seja você uma única unidade de negócios, tenha um Centro de Excelência, várias unidades independentes ou use agências para complementar suas equipes, a Braze tem experiência em trabalhar em todos os cenários.
- **Sofisticação da infraestrutura de dados:** Se você está implementando apenas o SDK da Braze ou já tem uma plataforma de dados do cliente (CDP), é possível ter tudo configurado em apenas 30 dias. O uso de uma CDP moderna pode acelerar o processo. Porém, se você tiver muitos sistemas de backend, ferramentas ou bancos de dados para conectar à Braze, pode levar mais tempo e exigir mais recursos dedicados para concluir a configuração.

Para saber mais, confira: [Primeiros passos: Visão geral da integração]({{site.baseurl}}/user_guide/get_started/integrations/).