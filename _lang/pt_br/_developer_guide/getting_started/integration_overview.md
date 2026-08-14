---
nav_title: Visão geral da integração
article_title: Visão geral da integração
page_order: 2
description: "Este artigo fornece uma visão geral básica do processo de integração."
platform:
  - iOS
  - Android
  - Web
  - React Native
  - Flutter
  - Cordova
  - Roku
  - Swift
  - Unity
---

# [![Curso do Braze Learning]({% image_buster /assets/img/bl_icon3.png %})](https://learning.braze.com/sdk-integration-basics){: style="float:right;width:120px;border:0;" class="noimgborder"}Introdução: Visão geral da integração {#braze-learning-course-image_buster-assetsimgbl_icon3png-httpslearningbrazecomsdk-integration-basics-stylefloatrightwidth120pxborder0-classnoimgbordergetting-started-integration-overview}

> Este artigo fornece uma visão geral básica do processo de integração.

![Um diagrama de Venn com quatro círculos — descoberta, integração, garantia de qualidade e manutenção — centrado no "tempo para obter valor".]({% image_buster /assets/img/getting-started/getting-started-integrate-flower.png %}){: style="max-width:50%;float:right;margin-left:15px;border:none;"}

Como recurso técnico, você capacitará sua equipe integrando a Braze ao seu stack de tecnologia. A integração é dividida, em linhas gerais, em quatro etapas:
* [Descoberta e planejamento](#discovery): Trabalhe com sua equipe para alinhar o escopo, planejar uma estrutura para dados e campanhas e criar uma estrutura de espaço de trabalho apropriada.
* [Integração](#integration): Execute seu plano integrando o SDK e a API, ativando canais de envio de mensagens e configurando a importação e exportação de dados.
* [Controle de qualidade](#qa): Confirme se o loop de dados e envio de mensagens entre a plataforma Braze e seu app ou site está funcionando conforme o esperado.
* [Manutenção](#maintenance): Depois de passar a Braze para a sua equipe de marketing, você continuará a garantir que tudo funcione sem problemas.

<br>
{% alert tip %}
Reconhecemos que cada organização tem suas necessidades distintas, e a Braze foi criada para atender a uma gama diversificada de opções de personalização que podem ser adaptadas às suas necessidades específicas. Os tempos de integração variam de acordo com seu caso de uso.
{% endalert %}

## Descoberta e planejamento {#discovery}

Durante essa fase, você trabalhará com a sua equipe para definir o escopo das tarefas de integração e garantir que todas as partes interessadas estejam alinhadas a um objetivo comum.

Sua equipe realizará o planejamento de ponta a ponta dos seus casos de uso para garantir que tudo possa ser criado conforme o esperado, com os dados corretos disponíveis para isso. Essa fase inclui o líder do projeto, o líder de CRM, a engenharia de front e back-end, os proprietários de produtos e os profissionais de marketing.

A fase de descoberta e planejamento leva, em média, cerca de seis semanas. Os líderes de engenharia podem esperar passar de 2 a 4 horas por semana durante essa fase. Os desenvolvedores que trabalham com o produto podem esperar passar de 10 a 20 horas por semana na Braze durante a fase de descoberta e planejamento.

{% alert tip %}
Durante o período de integração da sua empresa, a Braze realizará sessões de visão geral técnica. Recomendamos enfaticamente que os engenheiros participem dessas sessões. As sessões de visão geral técnica oferecem a oportunidade de conversar sobre a escalabilidade da arquitetura da plataforma e ver exemplos práticos de como empresas do seu porte foram bem-sucedidas em casos de uso semelhantes.
{% endalert %}

![Ícones para diferentes canais, como e-mail, carrinho de compras, imagens, geolocalização e assim por diante.]({% image_buster /assets/img/getting-started/data-graphic-2.png %}){: style="max-width:40%;float:right;margin-left:15px;"}

### Planejamento de campanhas {#campaign-planning}

Sua equipe de CRM planejará os casos de uso de envio de mensagens que serão lançados em um futuro próximo. Isso inclui:
* [Canal]({{site.baseurl}}/user_guide/channels) (por exemplo, notificações por push ou mensagens no app)
* [Método de entrega]({{site.baseurl}}/user_guide/messaging/campaigns/schedule_your_campaign) (por exemplo, entrega programada ou entrega baseada em ação)
* [Público-alvo]({{site.baseurl}}/user_guide/audience/segments)
* [Métricas de sucesso]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/conversion_events)

Por exemplo, uma Campaign para novos clientes pode ser: um e-mail enviado diariamente às 10h para um segmento de clientes que registraram sua primeira sessão ontem. O evento de conversão (a métrica de sucesso) é o registro de uma sessão.

<br>
{% alert important %}
A integração não pode começar até que a etapa de planejamento de campanhas esteja concluída. Essa etapa determinará quais partes da Braze precisam ser configuradas durante a fase de integração.
{% endalert %}

### Criação de requisitos de dados {#creating-data-requirements}

Em seguida, sua equipe de CRM deve definir quais dados são necessários para lançar as campanhas planejadas, criando requisitos de dados.

Muitos tipos comuns de atributos de usuário, como nome, e-mail, data de nascimento, país e similares, são automaticamente rastreados após a integração do SDK da Braze. Outros tipos de dados precisarão ser definidos como dados personalizados.

Como desenvolvedor, você trabalhará com sua equipe para definir quais dados adicionais e personalizados fazem sentido rastrear. Seus dados personalizados afetarão a forma como sua base de usuários será classificada e segmentada. Você configurará uma taxonomia de eventos em todo o seu growth stack, estruturando seus dados para que sejam compatíveis com seus sistemas à medida que entram e saem da Braze.

{% alert tip %}
Mantenha a nomenclatura dos dados consistente em todas as ferramentas. Por exemplo, seu data warehouse pode registrar "comprar oferta por tempo limitado" de uma maneira específica. Você precisará decidir se é necessário um evento personalizado na Braze para corresponder a esse formato.
{% endalert %}

Saiba mais sobre [dados coletados automaticamente e dados personalizados]({{site.baseurl}}/developer_guide/analytics).

### Planejamento de personalizações {#customizations-planning}

Converse com seus profissionais de marketing sobre as personalizações desejadas. Por exemplo, você deseja implementar os Content Cards padrão da Braze? Deseja ajustar ligeiramente a aparência e o comportamento para que correspondam às diretrizes da sua marca? Deseja desenvolver uma interface de usuário totalmente nova para um componente e fazer com que a Braze rastreie sua análise de dados? Diferentes níveis de personalização exigem diferentes níveis de escopo.

### Como obter acesso ao dashboard {#getting-dashboard-access}

O dashboard da Braze é nossa interface de usuário na web. Os profissionais de marketing usarão o dashboard para fazer seu trabalho e criar conteúdo. Os desenvolvedores usam o dashboard para gerenciar as configurações de integração de apps, como chaves de API e credenciais de notificação por push.

O administrador da sua equipe deve adicionar você (e todos os outros membros da equipe que precisam de acesso à Braze) como usuários no seu dashboard.

### Espaços de trabalho e chaves de API {#workspaces-and-api-keys}

O administrador da sua equipe também criará diferentes [espaços de trabalho]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces). Os espaços de trabalho agrupam seus dados — usuários, segmentos, chaves de API — em um único local. Como prática recomendada, sugerimos colocar apenas versões diferentes do mesmo app ou de apps muito semelhantes em um único espaço de trabalho.

É importante ressaltar que os espaços de trabalho fornecem chaves de API para várias plataformas (como iOS e Android). Você usará as chaves de API correlacionadas para associar os dados do SDK a um espaço de trabalho específico. Navegue até seus espaços de trabalho para acessar a chave de API de cada um de seus apps. Confira se cada chave de API tem as permissões corretas para executar o trabalho que você definiu como escopo. Consulte o [artigo sobre provisionamento da API]({{site.baseurl}}/api/basics#rest-api-key-permissions) para saber mais.

Para implementações web que abrangem vários domínios raiz, consulte [Integração multidomínio para o SDK web da Braze]({{site.baseurl}}/developer_guide/platforms/web/multi_domain_integration) ao decidir se deve usar um único app ou apps e chaves de API separados.

{% alert important %}
É importante que você configure ambientes diferentes para desenvolvimento e produção. A configuração de um ambiente de teste evitará que você gaste dinheiro real durante a integração e o controle de qualidade. Para criar um ambiente de teste, configure um espaço de trabalho de teste e certifique-se de usar a respectiva chave de API para não preencher o espaço de trabalho de produção com dados de teste.
{% endalert %}

## Integração {#integration}

![Gráfico abstrato de pirâmide que representa o fluxo de informações de uma fonte de dados para um dispositivo de usuário.]({% image_buster /assets/img/getting-started/data-graphic.png %}){: style="max-width:45%;float:right;margin-left:15px;"}

A Braze oferece suporte a apps iOS, apps Android, apps web e muito mais. Você também pode optar por usar um wrapper SDK multiplataforma, como o React Native ou o Unity. Normalmente, vemos os clientes se integrarem em um período de 1 a 6 semanas. Muitos clientes integraram a Braze com apenas um engenheiro, dependendo da amplitude de suas habilidades técnicas e da disponibilidade. Depende inteiramente do seu escopo específico de integração e de quanto tempo sua equipe dedica ao projeto Braze.

Você precisará de desenvolvedores que estejam familiarizados com:
* Trabalhar na camada nativa do seu app ou site
* Criação de processos para acessar nossa REST API
* Teste de integração
* Autenticação de token da web JSON
* Habilidades gerais de gerenciamento de dados
* Configuração de registros DNS

### Integração com parceiros de CDP {#cdp-integration-partners}

Muitos clientes usam a integração da Braze como uma oportunidade de também se integrar a uma plataforma de dados do cliente (CDP) como parceiro de integração. A Braze oferece rastreamento e análise de dados, enquanto uma CDP pode oferecer roteamento e orquestração de dados adicionais. A Braze oferece integração perfeita com muitas CDPs, como a [mParticle]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/mparticle/mparticle) e o [Segment]({{site.baseurl}}/partners/data_and_analytics/customer_data_platform/segment/segment).

Se estiver realizando a integração lado a lado com uma CDP, você mapeará as chamadas do SDK da sua CDP para o SDK da Braze. Essencialmente, você irá:
* Mapear chamadas de identificação para `changeUser` ([Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/change-user.html), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/changeuser(userid:sdkauthsignature:fileid:line:)/), [web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser)) e definir atributos.
* Mapear chamadas de flush de dados para `requestImmediateDataFlush` ([Android](https://braze-inc.github.io/braze-android-sdk/kdoc/braze-android-sdk/com.braze/-i-braze/request-immediate-data-flush.html?query=abstract%20fun%20requestImmediateDataFlush()), [iOS](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/requestimmediatedataflush()), [web](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#requestimmediatedataflush)).
* Registrar eventos personalizados ou compras.

Exemplos de integrações entre o SDK da Braze e a CDP de sua escolha podem estar disponíveis, dependendo da plataforma que você escolheu. Para saber mais, consulte nossa [lista de parceiros de tecnologia CDP]({{site.baseurl}}/partners/data_and_analytics).

### Integração do SDK da Braze {#braze-sdk-integration}

O SDK da Braze fornece duas funcionalidades essenciais: coleta e sincroniza os dados de usuários em um perfil de usuário consolidado e alimenta os canais de envio de mensagens, como notificações por push, mensagens no app e Content Cards.

{% alert tip %}
Quando estiver totalmente integrado ao seu app ou site, o SDK da Braze oferece um nível de sofisticação de marketing totalmente realizado. Se você adiar a integração do SDK da Braze, algumas das funcionalidades descritas na documentação não estarão disponíveis.
{% endalert %}

{% alert note %}
Para adicionar uma camada adicional de segurança, você pode ativar a [autenticação do SDK]({{site.baseurl}}/developer_guide/sdk_integration/authentication) para evitar solicitações não autorizadas ao SDK. Este recurso está disponível em todas as principais plataformas, incluindo Web, iOS, Android, React Native, Flutter, Unity, Cordova, .NET MAUI (Xamarin) e Expo.
{% endalert %}

Durante a implementação do SDK, você irá:

* Escrever o código de integração do SDK para cada plataforma à qual deseja oferecer suporte.
* Ativar os canais de envio de mensagens para cada plataforma, garantindo que o SDK da Braze rastreie os dados das interações com seus clientes por e-mail, SMS, notificações por push e outros canais.
* Criar quaisquer personalizações de componentes de UI planejadas (por exemplo, Content Cards personalizados). Para conteúdo totalmente personalizado, será necessário registrar a análise de dados, pois a coleta automática de dados do SDK não estará ciente dos seus novos componentes. Você pode padronizar essa implementação com base nos nossos componentes padrão.

### Usando a API da Braze {#using-the-braze-api}

Você usará nossa REST API para diferentes tarefas em diferentes momentos ao longo do seu tempo de uso da Braze. A API da Braze é útil para:

1. Importação de dados históricos; e
2. Atualizações contínuas que não são disparadas na Braze. Por exemplo, o perfil de um usuário faz upgrade para VIP sem que ele faça login em um app, portanto, a API precisa comunicar essas informações à Braze.

Comece com a [API da Braze]({{site.baseurl}}/api/basics).

{% alert important %}
Ao usar a API, certifique-se de agrupar suas solicitações em lote e enviar apenas valores delta. A Braze reescreve todos os atributos que são enviados. Não atualize nenhum atributo personalizado se seu valor não tiver sido alterado.
{% endalert %}

### Configuração da análise de dados do produto {#setting-up-product-analytics}

A Braze tem tudo a ver com dados. Os dados na Braze são armazenados no perfil do usuário.

Os pontos de dados são uma estrutura por meio da qual você garante que está capturando os dados certos para seus profissionais de marketing, e não apenas "qualquer" dado que possa ser aspirado. Familiarize-se com os [pontos de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points).

### Migração de dados de usuários antigos {#migrating-legacy-user-data}

Você pode usar o [`/users/track endpoint`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) da Braze para migrar dados históricos que foram registrados fora da Braze. Exemplos de dados comumente importados incluem tokens por push e compras anteriores. Esse endpoint pode ser usado para importações pontuais ou atualizações regulares em lote.

Também é possível importar usuários e atualizar os valores dos atributos de clientes por meio de um único [upload de CSV]({{site.baseurl}}/user_guide/data_and_analytics/user_data_collection/user_import#importing-a-csv) para o dashboard. Fazer upload de CSVs pode ser útil para profissionais de marketing, enquanto nossa REST API permite maior flexibilidade.

### Configuração do rastreamento de sessão {#setting-up-session-tracking}

O SDK da Braze gera pontos de dados de "sessão aberta" e "sessão fechada". O SDK da Braze também libera os dados em intervalos regulares. Consulte esses links para obter os valores padrão de rastreamento de sessão, todos os quais podem ser personalizados ([Android]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=android), [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=swift), [web]({{site.baseurl}}/developer_guide/analytics/tracking_sessions?tab=web)).

### Rastreamento de eventos personalizados, atributos e eventos de compra {#tracking-custom-events-attributes-and-purchase-events}

Coordene-se com sua equipe para configurar o esquema de dados planejado, incluindo eventos personalizados, atributos de usuários e eventos de compra. Seu [esquema de dados personalizado]({{site.baseurl}}/user_guide/data/activation/events/custom_events) será inserido usando o dashboard e deve corresponder exatamente ao que foi implementado durante a integração do SDK.

{% alert tip %}
Os IDs de usuário, chamados de `external_id`s na Braze, devem ser definidos para todos os usuários conhecidos. Eles devem ser imutáveis e acessíveis quando um usuário abre o app, permitindo o rastreamento dos seus usuários entre dispositivos e plataformas. Consulte o artigo [Ciclo de vida do usuário]({{site.baseurl}}/user_guide/data/unification/user_data/user_profile_lifecycle) para obter as práticas recomendadas.
{% endalert %}

### Outras ferramentas {#other-tools}

Com base no seu caso de uso, pode haver outras ferramentas que você precise configurar. Por exemplo, talvez seja necessário configurar uma ferramenta como [geofences]({{site.baseurl}}/user_guide/engagement_tools/locations_and_geofences#about-locations-and-geofences) para realizar suas histórias de usuários. Descobrimos que os clientes que têm a capacidade de configurar essas ferramentas adicionais depois de concluir as etapas essenciais de integração são mais bem-sucedidos.

## Controle de qualidade {#qa}
Ao executar a integração, você realizará o controle de qualidade para garantir que tudo o que está sendo configurado esteja funcionando conforme o esperado. Esse controle de qualidade se divide em duas categorias gerais: ingestão de dados e canais de envio de mensagens.

{% alert important %}
Confira se os seus ambientes de produção e teste estão configurados antes de iniciar o controle de qualidade.
{% endalert %}

| **Ingestão de dados de controle de qualidade**  | **Envio de mensagens de controle de qualidade**                                              |
|---------------------------|---------------------------------------------------------------|
| Você realizará o controle de qualidade na forma como os dados são ingeridos, armazenados e exportados. | Você garantirá que as mensagens estão sendo enviadas corretamente aos usuários e que tudo está excelente. |
| Execute testes para confirmar que os dados estão armazenados corretamente. | Crie segmentos de usuários. |
| Confirme se os dados da sessão estão corretamente atribuídos ao espaço de trabalho pretendido na Braze. | Lance Campaigns e Canvas com sucesso. |
| Confirme se o início e o fim da sessão estão sendo registrados. | Confirme se as Campaigns corretas estão sendo exibidas para os segmentos de usuários corretos. |
| Confirme se as informações de atributos do usuário estão corretamente registradas nos perfis de usuário. | Confirme se os tokens por push estão sendo registrados corretamente. |
| Teste se os dados personalizados estão sendo registrados corretamente nos perfis de usuários. | Confirme se os tokens por push foram removidos corretamente. |
| Crie perfis de usuário anônimos. | Teste se as campanhas push estão sendo enviadas corretamente para os dispositivos e se o engajamento está registrado. |
| Confirme se os perfis de usuário anônimos se tornam perfis de usuário conhecidos quando o método `changeUser()` é chamado. | Teste se as mensagens no app são entregues e se as métricas são registradas. |
|                           | Teste se os Content Cards são entregues e se as métricas são registradas. |
|                           | Facilite o Connected Content (por exemplo, AccuWeather). |
|                           | Confirme se todas as integrações de canais de envio de mensagens estão funcionando corretamente. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Controle de qualidade" }

{% alert note %}
Ao realizar o controle de qualidade na sua integração de SDK, use o [Depurador do SDK]({{site.baseurl}}/developer_guide/sdk_integration/debugging) para solucionar problemas sem ativar o registro detalhado para seu app.
{% endalert %}

### Passando a Braze para os profissionais de marketing {#passing-braze-off-to-marketers}

Depois de integrar a plataforma ou o site, envolva a equipe de marketing para passar a propriedade da plataforma para eles. Esse processo é diferente em cada empresa, mas pode incluir o seguinte:

* Criação de uma [lógica Liquid]({{site.baseurl}}/user_guide/personalization_and_dynamic_content/liquid#about-liquid) complexa
* Ajuda para facilitar o [aquecimento de IP de e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup/ip_warming)
* Garantia de que outras partes interessadas entendam o tipo de dados que estão sendo rastreados

### Desenvolver para o futuro {#develop-for-the-future}

Você já herdou uma base de código e não tinha a menor ideia do que o desenvolvedor inicial estava pensando? Pior ainda, você já escreveu um código, entendeu-o completamente e depois ficou completamente perplexo quando voltou a ele um ano depois?

Durante a integração da Braze, as decisões coletivas tomadas em relação a dados, perfis de usuários, quais integrações estavam e não estavam no escopo, como as personalizações deveriam funcionar e muito mais, parecerão frescas em sua mente e, portanto, óbvias. Quando sua equipe quiser expandir a Braze ou quando outros recursos técnicos forem atribuídos ao seu projeto Braze, essas informações serão obscuras.

Crie um recurso para consolidar as informações que você aprendeu durante as sessões de visão geral técnica. Esse recurso ajudará a reduzir o tempo de integração de novos desenvolvedores que se juntam à sua equipe (ou servirá como um lembrete para você mesmo quando precisar expandir sua implementação atual da Braze).

## Manutenção {#maintenance}

Após a transferência para seus profissionais de marketing, você continuará a servir como um recurso para manutenção. Você prestará atenção às atualizações do iOS e do Android que possam afetar o SDK da Braze e garantirá que seus fornecedores terceirizados estejam atualizados.

Você fará o rastreamento das atualizações da plataforma Braze por meio do [GitHub](https://github.com/braze-inc/) da Braze. Ocasionalmente, seu administrador também receberá e-mails sobre atualizações urgentes e correções de bugs diretamente da Braze.

## Limites de frequência do SDK {#sdk-rate-limits}

### Monthly Active Users CY 24-25, Universal MAU, Web MAU e Mobile MAU {#monthly-active-users-cy-24-25-universal-mau-web-mau-and-mobile-mau}

Para clientes que adquiriram Monthly Active Users CY 24-25, Universal MAU, Web MAU e Mobile MAU, a Braze aplica limites de frequência no lado do servidor para solicitações de API usadas por nossos SDKs para atualizar sessões, atributos de usuários, eventos e outros dados de perfil de usuário. Isso garante a estabilidade da plataforma e mantém um serviço rápido e confiável.

* Os limites de frequência por hora são definidos de acordo com o tráfego esperado do SDK na sua conta, que pode corresponder ao número de usuários ativos mensais (MAU) que você adquiriu, ao setor, à sazonalidade ou a outros fatores. Quando o limite de frequência por hora é atingido, a Braze limita as solicitações até a próxima hora.
* Todas as solicitações limitadas são automaticamente reenviadas pelo SDK.
* As solicitações do SDK estão relacionadas à quantidade de dados personalizados coletados na sua implementação. Se você está consistentemente próximo ou no seu limite de frequência por hora, considere:
    * Revisar sua integração SDK para reduzir a coleta excessiva de dados.
    * Bloquear dados personalizados que não são essenciais para seus casos de uso de marketing.
* Os limites de frequência de pico são limites de curta duração que se aplicam quando um grande volume de solicitações chega em um período muito curto (ou seja, em segundos). Você não precisa tomar nenhuma ação quando os limites de pico ocorrem, e o SDK fará uma nova tentativa logo em seguida.
* Os limites de frequência contínuos controlam o volume sustentado de solicitações em uma janela móvel mais longa que a janela de pico (por exemplo, vários minutos) e ajudam a suavizar o tráfego contínuo entre os limites de pico e o seu limite de frequência por hora.

### Encontrando seus limites de frequência {#finding-your-rate-limits}

Para encontrar os limites atuais com base na taxa de transferência esperada do SDK, acesse **Configurações** > **APIs e Identificadores** > **Limites de API e SDK**.

Para o histórico de uso, acesse **Configurações** > **APIs e Identificadores** > **Dashboard de API e SDK**.

### Solicitando limites de frequência mais altos {#requesting-higher-rate-limits}

Se você precisa de um limite de frequência mais alto na Braze, entre em contato com o suporte da Braze ou com seu gerente de sucesso do cliente e inclua os seguintes detalhes:

* Se você precisa de um aumento temporário ou permanente.
* Por que você precisa do aumento.
* Quais endpoints e ambientes são afetados.
* Seu volume aproximado de tráfego e cronograma, incluindo data de início, duração e horários de pico.
* Se você pode agrupar chamadas ou distribuir o tráfego ao longo do tempo.

Após enviar sua solicitação, a Braze a analisa e informa o resultado.

### Alterações e suporte {#changes-and-support}

A Braze pode modificar os limites de frequência para proteger a estabilidade do sistema ou permitir maior taxa de transferência de dados na sua conta. Entre em contato com o suporte da Braze ou com seu gerente de sucesso do cliente para dúvidas ou preocupações sobre limites de frequência e como eles impactam o seu negócio.