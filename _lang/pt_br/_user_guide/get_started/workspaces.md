---
nav_title: Espaços de trabalho
article_title: "Primeiros passos: Espaços de trabalho"
page_order: 3
page_type: reference
description: "Tudo o que você faz na plataforma Braze acontece em um espaço de trabalho. Este artigo descreve como eles funcionam e quais considerações importantes devem ser levadas em conta."
---

# Primeiros passos: Espaços de trabalho {#get-started-workspaces}

> Tudo o que você faz na plataforma Braze acontece em um espaço de trabalho. Os espaços de trabalho funcionam como silos separados de dados e permitem que você mantenha marcas ou atividades diferentes separadas. Várias versões do seu site ou app móvel podem enviar dados para o mesmo espaço de trabalho. Referimo-nos aos diferentes sites e apps que são coletados em um espaço de trabalho como "instâncias do app".

## Entendendo espaços de trabalho {#understanding-workspaces}

Espaços de trabalho servem a dois propósitos principais:

- **Unificar dados de usuários:** Quando várias instâncias do app estão em um mesmo espaço de trabalho, você pode coletar e direcionar dados de usuários de forma integrada entre diferentes versões do seu app, como iOS, Android e web. Isso garante que você sempre tenha informações atualizadas sobre cada usuário, independentemente da plataforma que ele esteja usando.
- **Separar atividades distintas:** Espaços de trabalho também oferecem uma forma de manter marcas ou atividades distintas separadas. Por exemplo, se você tem várias submarcas com bases de usuários diferentes, é vantajoso criar espaços de trabalho separados para cada uma.

{% alert tip %}
Essa abordagem é particularmente útil para empresas como desenvolvedoras de jogos para dispositivos móveis, que podem gerenciar espaços de trabalho individuais para cada um de seus jogos, ou sites de eCommerce que desejam espaços de trabalho separados para cada região em que operam.
{% endalert %}

## Planejando espaços de trabalho {#planning-workspaces}

Você precisa criar instâncias de app separadas para cada versão do seu app em cada plataforma. Ao decidir quais instâncias de app incluir em um espaço de trabalho, pense nos usuários que você quer atingir e agrupe-os de acordo.

A ideia de ter várias instâncias de app em um único espaço de trabalho pode ser tentadora, pois permite aplicar limite de frequência no envio de mensagens em todo o seu portfólio de apps. No entanto, como prática recomendada, sugerimos colocar apenas versões diferentes do mesmo app (ou apps muito semelhantes) juntos em um único espaço de trabalho.

### Espaços de trabalho compartilhados {#shared-workspaces}

Exemplos comuns de quando você pode querer ter várias instâncias de app no mesmo espaço de trabalho:

- Quando você tem vários apps quase idênticos em diferentes plataformas
- Quando você tem diferentes revisões principais do app, mas quer continuar engajando os mesmos usuários quando eles fizerem upgrade
- Quando você tem diferentes versões do app entre as quais o mesmo usuário pode transitar (como de gratuito para premium)

#### Impacto nos filtros de segmentação {#impact-on-segmentation-filters}

Independentemente de quais apps você escolher ter em um espaço de trabalho, os dados deles serão agregados. Isso terá um impacto considerável nos seguintes filtros de segmentação na Braze (esta não é uma lista exaustiva):

- Último app usado
- Primeiro app usado
- Contagem de sessões
- Dinheiro gasto no app
- Inscrição push (Isso se torna uma situação de tudo ou nada — se seus usuários cancelarem a inscrição em um app, eles serão desinscritos de todos os apps no espaço de trabalho.)
- Inscrição de e-mail (Isso se torna uma situação de tudo ou nada e pode deixar você exposto a problemas de conformidade.)

{% alert note %}
A agregação de dados entre instâncias de app nesses filtros é o motivo pelo qual não recomendamos hospedar apps substancialmente diferentes dentro do mesmo espaço de trabalho. Isso pode tornar o direcionamento complicado!
{% endalert %}

### Espaços de trabalho separados {#separate-workspaces}

Em outros casos, você pode querer ter vários espaços de trabalho separados. Exemplos comuns incluem:

- Espaços de trabalho separados para ambientes de desenvolvimento e produção do mesmo app
- Sub-marcas diferentes, por exemplo, uma empresa de jogos para celular que oferece vários jogos
- Diferentes localizações do mesmo app ou website que operam em países diferentes ou direcionam idiomas diferentes

### Considerações importantes {#important-considerations}

Lembre-se de que espaços de trabalho funcionam como silos separados de dados. Todos os dados, sejam dados de usuários ou ativos de marketing, são armazenados dentro de um espaço de trabalho. Esses dados não podem ser facilmente compartilhados fora desse espaço de trabalho.

Os seguintes são todos elementos-chave que são configurados dentro de um espaço de trabalho:

- [Instâncias de app](#app-instances)
- [Equipes](#teams)
- [Permissões de usuários da empresa](#company-user-permissions) (mas não os usuários da empresa em si)
- [Conectores Currents](#currents-connectors)
- [Perfis de usuário](#user-profiles) e os dados de usuários associados
- [Segments, Campaigns e Canvas](#segments-campaigns-and-canvases)

#### Instâncias de app {#app-instances}

Você precisa criar instâncias de app separadas para cada versão do seu app em cada plataforma. Por exemplo, se você tem versões Free e Pro do seu app tanto no iOS quanto no Android, crie quatro instâncias de app dentro do seu espaço de trabalho (app iOS gratuito, app Android gratuito, app iOS pro e app Android pro). Isso fornecerá quatro chaves de API or interface de programação do aplicativo (API) para uso, uma para cada instância de app.

#### Equipes {#teams}

[Equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams) podem ser configuradas com base na localização da base de clientes, idioma e atributos personalizados para que membros e não membros da equipe tenham diferentes níveis de acesso a recursos de envio de mensagens e dados de clientes.

#### Permissões de usuários da empresa {#company-user-permissions}

Espaços de trabalho possuem definições independentes de acesso e permissões de usuário. As [permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions) permitem criar controles granulares sobre o que um usuário individual do dashboard ou equipe pode acessar dentro de um único espaço de trabalho.

#### Conectores Currents {#currents-connectors}

A ferramenta [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) é um fluxo de dados em tempo real dos seus eventos de engajamento, sendo a exportação mais robusta e ao mesmo tempo granular da plataforma Braze. Os conectores Currents estão incluídos em determinados pacotes da Braze, e você pode ter recebido inicialmente um, considerando um único espaço de trabalho.

Ao decidir entre criar espaços de trabalho separados ou combinados, é importante pensar no número de conectores Currents que você tem, pois os conectores Currents não são compartilhados entre espaços de trabalho.

Por exemplo, se você tem espaços de trabalho separados para os ambientes de desenvolvimento e produção do mesmo app, ative seu conector Currents no espaço de trabalho de produção. Para ativar Currents em ambos os espaços de trabalho, será necessário adquirir um conector Currents adicional.

#### Perfis de usuário {#user-profiles}

Todos os dados persistentes associados a um usuário são armazenados em seu [perfil de usuário]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles). No entanto, os perfis de usuário também são um ótimo recurso para solução de problemas e testes, pois você pode acessar facilmente informações sobre o histórico de engajamento, associação a Segments, dispositivo e sistema operacional de um usuário.

#### Segments, Campaigns e Canvas {#segments-campaigns-and-canvases}

Um Segment, Campaign ou Canvas não pode referenciar ou acessar dados armazenados em outro espaço de trabalho. Por outro lado, quando vários apps estão no mesmo espaço de trabalho, todos os apps terão seus dados agregados. Isso terá um [impacto nos filtros da Braze](#impact-on-segmentation-filters).

### Visão geral de cada abordagem {#overview-of-each-approach}

A tabela a seguir descreve os benefícios e desvantagens dessas duas abordagens para o planejamento de espaços de trabalho:

- **Espaços de trabalho e perfis de usuário separados:** Um espaço de trabalho tem uma instância de app e uma pessoa tem um perfil de usuário para essa instância de app.
- **Espaços de trabalho e perfis de usuário compartilhados:** Um espaço de trabalho tem várias instâncias de app e uma pessoa tem um perfil de usuário para todas essas instâncias de app.

<style type="text/css">
  table {
    width: 100%;
  }
  th, td {
    padding: 8px;
    text-align: left;
    border: 1px solid black;
    word-break: break-word !important;
  }
  th {
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
  }
  th[colspan="2"] {
    background-color: #fffae6;
  }
  th:last-child[colspan="2"] {
    background-color: #deebff;
  }
  td:nth-child(2), td:nth-child(3) {
    background-color: #fffae6;
  }
  td:nth-child(4), td:nth-child(5) {
    background-color: #deebff;
  }
  th:nth-child(2), th:nth-child(3) {
    background-color: #fffae6;
  }
  th:nth-child(4), th:nth-child(5) {
    background-color: #deebff;
  }
  th:first-child, td:first-child {
    min-width: 150px;
    background-color: #f4f4f7;
    font-size: 12px;
    font-weight: bold;
    text-transform: uppercase;
    color: #212123;
    font-family: "Aribau Grotesk Bold", "Aribau Grotesk", "Aribau Grotesk Regular", Arial, Helvetica, sans-serif;
  }
</style>

<table aria-label="Visão geral de cada abordagem">
  <caption>Visão geral de cada abordagem</caption>
    <thead>
    <tr>
        <th></th>
        <th colspan="2" scope="colgroup">Espaços de trabalho separados</th>
        <th colspan="2" scope="colgroup">Espaços de trabalho compartilhados</th>
    </tr>
    <tr>
        <th></th>
        <th scope="col">Benefícios</th>
        <th scope="col">Desvantagens</th>
        <th scope="col">Benefícios</th>
        <th scope="col">Desvantagens</th>
    </tr>
    </thead>
    <tbody>
    <tr>
        <th scope="row">Direcionamento</th>
        <td>Forma mais segura de manter as comunicações separadas. As Campaigns são garantidas para direcionar apenas perfis de usuário específicos.</td>
        <td>Impossibilidade de enviar mensagens de promoção cruzada mesmo que você saiba que um usuário possui outro perfil de usuário em um espaço de trabalho diferente.</td>
        <td>Pode enviar mensagens de promoção cruzada se souber que um usuário tem vários apps no seu espaço de trabalho.<br><br>Pode referenciar dados de usuários de diferentes apps. Por exemplo, João tem o atributo X relevante para o App 1 e o atributo Y relevante para o App 2, e ambos podem ser referenciados em uma Campaign.</td>
        <td>Mais espaço para erro humano — você pode acidentalmente direcionar usuários em várias instâncias de app.<br><br>Para enviar mensagens no app, você deve ter eventos personalizados específicos por app para que uma Campaign não seja exibida em outro app por acidente. Por exemplo, <code>app_1_action</code> versus <code>app_2_action</code>.</td>
    </tr>
    <tr>
        <th scope="row">Eventos e atributos personalizados</th>
        <td>Atributos e eventos personalizados são garantidos como específicos de uma instância de app.</td>
        <td>Não é possível rastrear o comportamento do usuário entre espaços de trabalho.<br><br><b>Dica:</b> Você pode alavancar vários conectores Currents para realizar isso.</td>
        <td>Pode rastrear o comportamento do usuário em todas as instâncias de app no espaço de trabalho.</td>
        <td>Atributos e eventos personalizados se aplicariam a todas as instâncias de app, o que pode dificultar saber quais dados em um perfil de usuário são relevantes para qual instância de app. Por exemplo, "date_of_parking" é relevante para o App 1 ou o App 2? Para combater isso, certifique-se de usar convenções de nomenclatura bem estruturadas.</td>
    </tr>
    <tr>
        <th scope="row">Limite de frequência</th>
        <td>O limite de frequência pode ser definido separadamente para cada instância de app (com base no espaço de trabalho).</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>O limite de frequência se aplica a todas as Campaigns, não por app, o que torna mais difícil evitar o envio excessivo de mensagens aos clientes.</td>
    </tr>
    <tr>
        <th scope="row">Status de inscrição para perfis de usuário</th>
        <td>O status de inscrição de cada perfil de usuário é exclusivo para cada instância de app.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>Os status de inscrição de um perfil de usuário são combinados entre instâncias de app.<br><br><b>Dica:</b> Você pode usar <a href='/docs/user_guide/data/activation/attributes/custom_attributes'>atributos personalizados</a> para gerenciar as inscrições dos seus usuários.</td>
    </tr>
    <tr>
        <th scope="row">Permissões de usuários da empresa</th>
        <td>N/A</td>
        <td>Atualizar as <a href='/docs/user_guide/administer/global/user_management/permissions'>permissões de usuário</a> para um usuário do dashboard deve ser feito separadamente para cada espaço de trabalho ao qual o usuário precisa de acesso.</td>
        <td>As <a href='/docs/user_guide/administer/global/user_management/permissions'>permissões de usuário</a> podem ser definidas uma única vez para um usuário do dashboard, e ele terá as mesmas permissões para todas as instâncias de app no espaço de trabalho.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <th scope="row">Duplicação de conteúdo</th>
        <td>N/A</td>
        <td>Alguns conteúdos, como Segments e Campaigns de cartão de conteúdo, não podem ser copiados entre espaços de trabalho.</td>
        <td>Pode <a href='{{site.baseurl}}/user_guide/messaging/governance/copy_across_workspaces'>copiar Campaigns, Canvas e landing pages entre espaços de trabalho</a>. O conteúdo suportado inclui Campaigns e Canvas para canais elegíveis, assim como landing pages, modelos de e-mail, Feature Flags e Content Blocks.<br><br>Pode duplicar Segments, Campaigns, Canvas e landing pages para reutilizar conteúdo de uma instância de app para outra.</td>
        <td>N/A</td>
    </tr>
    <tr>
        <th scope="row">Análise de dados</th>
        <td>As estatísticas globais serão precisas na página inicial.</td>
        <td>N/A</td>
        <td>N/A</td>
        <td>As estatísticas globais serão agregadas para todas as instâncias de app no espaço de trabalho na página inicial.</td>
    </tr>
    </tbody>
</table>

{% alert note %}
Para saber como o MAU difere ao visualizar todos os apps versus um único app, consulte [Usuários ativos mensais]({{site.baseurl}}/user_guide/analytics/dashboards/home#monthly-active-users).
{% endalert %}

## Práticas recomendadas {#best-practices}

### Configurar um espaço de trabalho de teste {#set-up-a-testing-workspace}

Como prática recomendada, sempre que você planejar configurar um espaço de trabalho de produção (um espaço de trabalho que enviará mensagens a usuários reais), você também deve configurar um espaço de trabalho de teste. Um espaço de trabalho de teste é uma cópia do seu espaço de trabalho de produção sem dados reais de usuários.

Isso é considerado uma prática recomendada por vários motivos:

- **Isolamento de mudanças:** Permite testar novos recursos, configurações ou atualizações em um ambiente isolado, sem afetar o ambiente de produção ativo. Dessa forma, se algo der errado durante os testes, o ambiente de produção não será afetado.
- **Testes mais precisos:** Permite testes mais precisos, já que os dados no ambiente de teste podem ser controlados e manipulados sem preocupação com dados reais.
- **Depuração:** É mais fácil depurar problemas em um ambiente de teste, pois você pode manipular o ambiente livremente sem se preocupar em impactar o ambiente de produção.
- **Treinamento:** Novos membros da equipe podem se familiarizar com o espaço de trabalho em um ambiente seguro, onde erros não terão consequências no mundo real.

{% alert tip %}
A ordem em que você configura um espaço de trabalho de teste e um de produção pode depender das suas necessidades e circunstâncias específicas. No entanto, geralmente é uma boa ideia configurar o espaço de trabalho de teste primeiro. Isso permite testar recursos, configurações e atualizações antes de implementá-los no espaço de trabalho de produção. Depois que estiver satisfeito com os testes e resultados, você pode então estabelecer seu espaço de trabalho de produção.
{% endalert %}

### Adicionar administradores {#add-administrators}

Você deve ter mais de um usuário da Braze com permissões de administrador em um único espaço de trabalho. Isso garante que haja pessoas suficientes na sua organização para gerenciar as permissões de outros usuários.

## Próximas etapas {#next-steps}

Depois de determinar o plano do seu espaço de trabalho, é hora de criar seu espaço de trabalho e adicionar instâncias do app. Para ver as etapas, confira [Criar e gerenciar espaços de trabalho]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces).