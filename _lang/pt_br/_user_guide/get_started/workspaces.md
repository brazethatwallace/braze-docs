---
nav_title: Espaços de trabalho
article_title: "Primeiros passos: Espaços de trabalho"
page_order: 3
page_type: reference
description: "Tudo o que você faz na plataforma Braze acontece em um espaço de trabalho. Este artigo descreve como eles funcionam e quais considerações importantes devem ser levadas em conta ao planejar seus espaços de trabalho na Braze."
---

# Primeiros passos: Espaços de trabalho {#get-started-workspaces}

> Tudo o que você faz na plataforma Braze acontece em um espaço de trabalho. Os espaços de trabalho funcionam como silos separados de dados e permitem que você mantenha marcas ou atividades diferentes separadas. Várias versões do seu site ou app móvel podem enviar dados para o mesmo espaço de trabalho. Referimo-nos aos diferentes sites e apps que são coletados em um espaço de trabalho como "instâncias do app".

## Entendendo os espaços de trabalho {#understanding-workspaces}

Os espaços de trabalho têm dois objetivos principais:

- **Unificação dos dados de usuários:** Quando várias instâncias do app estão em um espaço de trabalho, é possível coletar e direcionar dados de usuários de forma integrada em diferentes versões do seu app, como iOS, Android e web. Isso garante que você sempre tenha informações atualizadas sobre cada usuário, independentemente da plataforma que ele estiver usando.
- **Separação de atividades distintas:** Os espaços de trabalho também oferecem um meio de manter marcas ou atividades distintas separadas. Por exemplo, se você tiver várias submarcas com diferentes bases de usuários, é vantajoso criar espaços de trabalho separados para cada uma delas.

{% alert tip %}
Essa abordagem é particularmente útil para empresas como as de jogos móveis, que podem gerenciar espaços de trabalho individuais para cada um de seus jogos, ou sites de comércio eletrônico que desejam espaços de trabalho separados para cada região em que operam.
{% endalert %}

## Planejamento de espaços de trabalho {#planning-workspaces}

Você deve criar instâncias do app separadas para cada versão do seu app em cada plataforma. Ao decidir quais instâncias do app incluir em um espaço de trabalho, pense nos usuários que deseja direcionar e agrupe-os de acordo.

A vantagem de ter várias instâncias do app em um único espaço de trabalho pode ser atraente, pois permite limitar o envio de mensagens em todo o seu portfólio de apps. No entanto, como prática recomendada, sugerimos apenas colocar versões diferentes do mesmo app (ou de apps muito semelhantes) em um único espaço de trabalho.

### Espaços de trabalho compartilhados {#shared-workspaces}

Exemplos comuns de quando você desejaria ter várias instâncias do app no mesmo espaço de trabalho:

- Quando você tem vários apps quase idênticos em diferentes plataformas
- Quando você tem diferentes revisões principais do app, mas deseja manter o engajamento dos mesmos usuários quando eles fazem upgrade
- Quando você tem versões diferentes do app que o mesmo usuário pode usar ou deixar de usar (por exemplo, de gratuito para premium)

#### Impacto nos filtros de segmentação {#impact-on-segmentation-filters}

Todos os apps que você optar por ter em um espaço de trabalho terão seus dados agregados. Isso terá um impacto notável nos seguintes filtros de segmentação na Braze (essa não é uma lista exaustiva):

- Último uso do app
- Usou o app pela primeira vez
- Contagem de sessões
- Dinheiro gasto no app
- Inscrição por push (isso se torna uma situação de tudo ou nada: se os usuários cancelarem a inscrição em um app, eles cancelarão a inscrição em todos os apps do espaço de trabalho.)
- Inscrição de e-mail (isso se torna uma situação de tudo ou nada e pode deixá-lo exposto a problemas de conformidade.)

{% alert note %}
A agregação de dados entre instâncias do app nesses filtros é o motivo pelo qual não recomendamos hospedar apps substancialmente diferentes no mesmo espaço de trabalho. Isso pode tornar o direcionamento complicado!
{% endalert %}

### Espaços de trabalho separados {#separate-workspaces}

Outras vezes, você pode desejar ter vários espaços de trabalho separados. Exemplos comuns disso incluem:

- Espaços de trabalho separados para ambientes de desenvolvimento e produção do mesmo app
- Diferentes submarcas, por exemplo, uma empresa de jogos para celular que oferece vários jogos
- Diferentes localizações do mesmo app ou site que operam em diferentes países ou direcionam para diferentes idiomas

### Considerações importantes {#important-considerations}

Lembre-se de que os espaços de trabalho funcionam como silos separados de dados. Todos os dados, sejam eles dados de usuários ou ativos de marketing, são armazenados em um espaço de trabalho. Esses dados não podem ser facilmente compartilhados fora desse espaço de trabalho.

A seguir estão todos os elementos-chave que são configurados em um espaço de trabalho:

- [Instâncias do app](#app-instances)
- [Equipes](#teams)
- [Permissões de usuário da empresa](#company-user-permissions) (mas não usuários da empresa)
- [Conectores Currents](#currents-connectors)
- [Perfis de usuário](#user-profiles) e os dados de usuários associados
- [Segments, Campaigns e Canvas](#segments-campaigns-and-canvases)

#### Instâncias do app {#app-instances}

Você deve criar instâncias do app separadas para cada versão do seu app em cada plataforma. Por exemplo, se você tiver versões Free e Pro do seu app no iOS e no Android, crie quatro instâncias do app em seu espaço de trabalho (app gratuito para iOS, app gratuito para Android, app pro para iOS e app pro para Android). Isso lhe dará quatro chaves de API para usar, uma para cada instância do app.

#### Equipes {#teams}

[As equipes]({{site.baseurl}}/user_guide/administer/global/user_management/teams/) podem ser configuradas de acordo com o local, o idioma e os atributos personalizados da base de clientes, de modo que os membros e não membros da equipe tenham acesso diferente aos recursos de envio de mensagens e aos dados de clientes.

#### Permissões de usuário da empresa {#company-user-permissions}

Os espaços de trabalho têm acesso independente e definições de permissão de usuário. [As permissões de usuário]({{site.baseurl}}/user_guide/administer/global/user_management/permissions/) permitem criar controles granulares em relação ao que um usuário individual do dashboard ou uma equipe tem acesso em um único espaço de trabalho.

#### Conectores Currents {#currents-connectors}

A ferramenta [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents/) é um fluxo de dados em tempo real de seus eventos de engajamento que é a exportação mais robusta e granular da plataforma Braze. Os conectores Currents estão incluídos em determinados pacotes da Braze, e você pode ter recebido um inicialmente, supondo um único espaço de trabalho.

Quando estiver decidindo entre criar espaços de trabalho separados ou combinados, é importante pensar no número de conectores Currents que você tem, pois os conectores Currents não são compartilhados entre os espaços de trabalho.

Por exemplo, se você tiver espaços de trabalho separados para os ambientes de desenvolvimento e produção do mesmo app, ative seu conector Currents no espaço de trabalho de produção. Para ativar o Currents em ambos os espaços de trabalho, você precisará adquirir um conector Currents adicional.

#### Perfis de usuário {#user-profiles}

Todos os dados persistentes associados a um usuário são armazenados em seu [perfil de usuário]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles/). No entanto, os perfis de usuário também são um ótimo recurso para solução de problemas e testes, pois é possível acessar facilmente informações sobre o histórico de engajamento, a associação ao Segment, o dispositivo e o sistema operacional de um usuário.

#### Segments, Campaigns e Canvas {#segments-campaigns-and-canvases}

Um Segment, uma Campaign ou um Canvas não pode fazer referência ou acessar dados armazenados em outro espaço de trabalho. Por outro lado, quando vários apps estiverem no mesmo espaço de trabalho, todos os apps terão seus dados agregados. Isso terá um [impacto sobre os filtros na Braze](#impact-on-segmentation-filters).

### Visão geral de cada abordagem {#overview-of-each-approach}

A tabela a seguir descreve os benefícios e as desvantagens dessas duas abordagens para o planejamento do espaço de trabalho:

- **Espaços de trabalho e perfis de usuário separados:** Um espaço de trabalho tem uma instância do app e uma pessoa tem um perfil de usuário para essa instância do app.
- **Espaços de trabalho e perfis de usuário compartilhados:** Um espaço de trabalho tem várias instâncias do app e uma pessoa tem um perfil de usuário para todas essas instâncias do app.

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
    font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
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
    font-family: "Sailec W00 Bold",Arial,Helvetica,sans-serif;
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
        <td>A maneira mais segura de manter as comunicações separadas. As Campaigns têm a garantia de direcionar apenas perfis de usuários específicos.</td>
        <td>Não é possível enviar mensagens promocionais cruzadas, mesmo sabendo que um usuário tem outro perfil de usuário em um espaço de trabalho diferente.</td>
        <td>Pode enviar mensagens promocionais cruzadas se souber que um usuário tem vários apps em seu espaço de trabalho.<br><br>Pode fazer referência a dados de usuários de vários apps. Por exemplo, João tem um atributo X relevante para o App 1 e um atributo Y relevante para o App 2, que podem ser referenciados em uma Campaign.</td>
        <td>Mais espaço para erro humano — você pode direcionar acidentalmente os usuários em várias instâncias do app.<br><br>Para enviar mensagens no app, é necessário ter eventos personalizados específicos do app para que uma Campaign não seja exibida em outro app por acidente. Por exemplo, <code>app_1_action</code> versus <code>app_2_action</code>.</td>
    </tr>
    <tr>
        <th scope="row">Eventos e atributos personalizados</th>
        <td>É garantido que os atributos e eventos personalizados sejam específicos de uma instância do app.</td>
        <td>Não é possível rastrear o comportamento do usuário nos espaços de trabalho.<br><br><b>Dica:</b> Você pode utilizar vários conectores Currents para fazer isso.</td>
        <td>Pode rastrear o comportamento do usuário em todas as instâncias do app no espaço de trabalho.</td>
        <td>Atributos e eventos personalizados se aplicariam a todas as instâncias do app, o que poderia dificultar a identificação de quais dados de um perfil de usuário são relevantes para qual instância do app. Por exemplo, "date_of_parking" é relevante para o App 1 ou o App 2? Para combater isso, certifique-se de usar convenções de nomenclatura bem estruturadas.</td>
    </tr>
    <tr>
        <th scope="row">Limite de frequência</th>
        <td>O limite de frequência pode ser definido separadamente para cada instância do app (com base no espaço de trabalho).</td>
        <td>N/D</td>
        <td>N/D</td>
        <td>O limite de frequência se aplica a todas as Campaigns, e não por app, o que torna mais difícil evitar o envio excessivo de mensagens aos clientes.</td>
    </tr>
    <tr>
        <th scope="row">Status da inscrição para perfis de usuário</th>
        <td>O status de inscrição de cada perfil de usuário é exclusivo para cada instância do app.</td>
        <td>N/D</td>
        <td>N/D</td>
        <td>Os status de inscrição de um perfil de usuário são combinados entre as instâncias do app.<br><br><b>Dica:</b> Em vez disso, é possível usar <a href='/docs/user_guide/data/activation/attributes/custom_attributes'>atributos personalizados</a> para gerenciar as inscrições de seus usuários.</td>
    </tr>
    <tr>
        <th scope="row">Permissões de usuário da empresa</th>
        <td>N/D</td>
        <td>A atualização das <a href='/docs/user_guide/administer/global/user_management/permissions'>permissões de usuário</a> para um usuário do dashboard deve ser feita separadamente para cada espaço de trabalho ao qual o usuário precisa ter acesso.</td>
        <td>As <a href='/docs/user_guide/administer/global/user_management/permissions'>permissões de usuário</a> podem ser definidas uma vez para um usuário do dashboard, e ele terá as mesmas permissões para todas as instâncias do app no espaço de trabalho.</td>
        <td>N/D</td>
    </tr>
    <tr>
        <th scope="row">Duplicação de conteúdo</th>
        <td>N/D</td>
        <td>Não é possível duplicar Segments, Campaigns de push ou de cartão de conteúdo, nem Canvas entre espaços de trabalho.</td>
        <td>Pode <a href='{{site.baseurl}}/user_guide/messaging/governance/copy_across_workspaces/'>duplicar Campaigns entre espaços de trabalho</a> para os seguintes canais suportados: SMS, mensagens no app, e-mail, modelos de e-mail e Content Blocks. <br><br>Pode duplicar Segments, Campaigns e Canvas para reutilizar conteúdo de uma instância do app para outra.</td>
        <td>N/D</td>
    </tr>
    <tr>
        <th scope="row">Análise de dados</th>
        <td>As estatísticas globais serão precisas na página inicial.</td>
        <td>N/D</td>
        <td>N/D</td>
        <td>As estatísticas globais serão agregadas para todas as instâncias do app no espaço de trabalho na página inicial.</td>
    </tr>
    </tbody>
</table>

## Práticas recomendadas {#best-practices}

### Configure um espaço de trabalho para testes {#set-up-a-testing-workspace}

Como prática recomendada, sempre que planejar configurar um espaço de trabalho de produção (um espaço de trabalho que enviará mensagens para usuários reais), você também deve configurar um espaço de trabalho de teste. Um espaço de trabalho de teste é uma duplicata do seu espaço de trabalho de produção sem dados reais de usuários.

Essa é considerada uma prática recomendada por vários motivos:

- **Isolamento de alterações:** Permite testar novos recursos, configurações ou atualizações em um ambiente isolado sem afetar o ambiente de produção ao vivo. Dessa forma, se algo der errado durante o teste, seu ambiente de produção não será afetado.
- **Testes precisos:** Permite testes mais precisos, pois os dados no ambiente de teste podem ser controlados e manipulados sem a preocupação com os dados do mundo real.
- **Depuração:** É mais fácil depurar problemas em um ambiente de teste, pois você pode manipular livremente o ambiente sem se preocupar em afetar o ambiente de produção.
- **Treinamento:** Os novos membros da equipe podem se familiarizar com o espaço de trabalho em um ambiente seguro, onde os erros não terão consequências no mundo real.

{% alert tip %}
A ordem em que você configura um espaço de trabalho de teste e um espaço de trabalho de produção pode depender de suas necessidades e circunstâncias específicas. No entanto, geralmente é uma boa ideia configurar um espaço de trabalho de teste primeiro. Isso permite que você teste recursos, configurações e atualizações antes de serem implementados no espaço de trabalho de produção. Quando estiver satisfeito com os testes e os resultados, você poderá estabelecer seu espaço de trabalho de produção.
{% endalert %}

### Adicionar administradores {#add-administrators}

Você deve ter mais de um usuário da Braze com permissões de administrador para um único espaço de trabalho. Isso garante que haja um número suficiente de pessoas em sua organização para gerenciar as permissões de outros usuários.

## Próximas etapas {#next-steps}

Depois de determinar o plano do espaço de trabalho, é hora de criar o espaço de trabalho e adicionar instâncias do app. Para ver as etapas, confira [Criar e gerenciar espaços de trabalho]({{site.baseurl}}/user_guide/administer/global/create_and_manage_workspaces/).