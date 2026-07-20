---
nav_title: Grupo de controle global
article_title: Grupo de controle global
alias: /global_control_group/
page_order: 6
page_type: reference
description: "Saiba como configurar e usar o grupo de controle global para medir o impacto geral dos seus esforços de envio de mensagens ao longo do tempo."
tool:
  - Reports
search_rank: 1
toc_headers: h2

---

# Grupo de controle global {#global-control-group}

> Use o grupo de controle global para especificar uma porcentagem de todos os usuários que não devem receber nenhuma Campaign ou Canvas, permitindo que você analise o impacto geral dos seus esforços de envio de mensagens ao longo do tempo.

Ao comparar o comportamento dos usuários que recebem mensagens com aqueles que não recebem, você pode entender melhor como suas Campaigns e Canvas contribuem para um aumento em sessões e eventos personalizados.

## Como o grupo de controle global funciona {#how-the-global-control-group-works}

Com o grupo de controle global, você pode definir uma porcentagem de todos os usuários como grupo de controle. Quando salvo, os usuários do grupo não recebem nenhuma Campaign ou Canvas.

{% alert important %}
Seu grupo de controle global se aplica a todos os canais, Campaigns e Canvas, exceto [Campaigns da API]({{site.baseurl}}/api/api_campaigns). Isso significa que os usuários no seu grupo de controle ainda recebem Campaigns da API. No entanto, essa exceção não se aplica a Content Cards. Se você estiver usando uma Campaign de Content Card disparada por API, os usuários no seu grupo de controle não as receberão.
{% endalert %}

### Atribuir usuários aleatoriamente ao grupo de controle global {#assign-users-randomly-to-the-global-control-group}

A Braze seleciona aleatoriamente múltiplos intervalos de [números de bucket aleatórios]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers#create-segments-using-random-bucket-numbers) e inclui os usuários desses buckets selecionados. Se você está usando números de bucket aleatórios para qualquer outro propósito, confira [Pontos de atenção](#things-to-watch-for).

Quando seu grupo de controle global é gerado, todos os usuários com números de bucket aleatórios fazem parte do grupo. Além disso, novos usuários que ingressarem após esse ponto (aqueles adquiridos depois que o grupo de controle global foi gerado) que possuem esses números de bucket aleatórios também são adicionados ao grupo de controle global. Da mesma forma, se muitos usuários forem excluídos, você pode esperar que o tamanho do seu grupo de controle global diminua, pois uma porcentagem desses usuários excluídos pertencia a esse grupo. Isso mantém o tamanho do seu grupo como uma porcentagem constante em relação à sua base total de usuários.

### Atribuir usuários aleatoriamente ao grupo de tratamento para relatórios {#assign-users-randomly-to-the-treatment-group-for-reporting}

A Braze também cria um grupo de tratamento para relatórios de aumento. O grupo de tratamento é um grupo de usuários selecionados aleatoriamente que não fazem parte do seu grupo de controle global, e é gerado usando o mesmo método de número de bucket aleatório do grupo de controle global.

Seu grupo de tratamento tem tamanho semelhante ao do seu grupo de controle global, mas é improvável que tenha exatamente o mesmo tamanho. Para [relatórios](#reporting), a Braze mede os comportamentos dos usuários no seu grupo de controle e dos usuários na sua amostra de tratamento. Cada espaço de trabalho tem no máximo um grupo de controle global e um grupo de amostra de tratamento. O grupo de amostra de tratamento é o mesmo grupo de usuários independentemente de como você configura seus relatórios de controle global.

### Excluir usuários de Feature Flags {#exclude-users-from-feature-flags}

Você não pode ativar [Feature Flags]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/feature_flags) para usuários no seu grupo de controle global. Isso significa que os usuários no seu grupo de controle global também não podem participar de experimentos de Feature Flag.

### Excluir usuários do grupo de controle global {#exclude-users-from-the-global-control-group}

Você não pode remover usuários específicos do grupo de controle global, mas pode adicionar [configurações de exclusão](#step-3-assign-exclusion-settings) para que Campaigns e Canvas com tags especificadas **não** usem o grupo de controle global. Você também pode desativar e reativar seu grupo de controle global para reorganizar a composição. A duração ideal para reorganizar os usuários varia de acordo com o tipo de teste que você está executando, mas tente reorganizar no máximo uma vez por mês.

## Criar um grupo de controle global {#create-a-global-control-group}

### Etapa 1: Navegue até as configurações do grupo de controle global {#step-1-navigate-to-the-global-control-group-settings}

No dashboard, acesse **Audience** > **Global Control Group**.

### Etapa 2: Atribua uma porcentagem de todos os usuários a este grupo de controle {#step-2-assign-a-percentage-of-all-users-to-this-control-group}

Insira uma porcentagem para o seu grupo de controle e selecione **Save**. Quando inserido, a Braze mostra uma estimativa de quantos usuários se enquadram no seu controle global, tratamento e amostra de tratamento. Lembre-se de que quanto mais usuários você tiver no seu espaço de trabalho, mais precisa será essa estimativa.

O número de usuários no seu grupo de controle global é atualizado automaticamente após a configuração inicial para permanecer proporcional a essa porcentagem quando mais usuários são adicionados ao seu espaço de trabalho. Além disso, os usuários que ingressarem após a configuração do grupo de controle global e que possuem números de bucket aleatórios também são adicionados ao grupo de controle global. Se muitos usuários forem adicionados, o tamanho do seu grupo de controle global cresce para manter uma porcentagem constante em relação à sua base total de usuários. Quando o tamanho do seu grupo de controle global cresce, os usuários que já estavam no grupo permanecem nele (a menos que você faça alterações no grupo desativando-o e criando um novo).

Para diretrizes de porcentagem, consulte [Melhores práticas de teste](#percentage-guidelines).

![As configurações do grupo de controle global com as configurações de público definidas como "Atribuir cinco por cento de todos os usuários ao grupo de controle global".]({% image_buster /assets/img/control_group/control_group4.png %})

### Etapa 3: Atribua configurações de exclusão {#step-3-assign-exclusion-settings}

Use tags para adicionar configurações de exclusão ao seu grupo de controle global. Quaisquer Campaigns ou Canvas que usem as tags incluídas nas configurações de exclusão não usam seu grupo de controle global. Essas Campaigns e Canvas continuam sendo enviados para todos os usuários no público-alvo, incluindo aqueles no seu grupo de controle global.

{% alert tip %}
Você pode querer adicionar configurações de exclusão se tiver mensagens transacionais que devem ser enviadas a todos os usuários.
{% endalert %}

![A seção para adicionar ou editar configurações de exclusão para o seu grupo de controle global.]({% image_buster /assets/img/control_group/control_group5.png %})

### Etapa 4: Salve seu grupo de controle {#step-4-save-your-control-group}

Neste ponto, a Braze gera um grupo de usuários selecionados aleatoriamente que compõe a porcentagem selecionada da sua base total de usuários. Quando salvo, todas as Campaigns e Canvas ativos e futuros não enviam mais mensagens para os usuários deste grupo, exceto Campaigns ou Canvas que contenham qualquer uma das tags nas suas configurações de exclusão.

## Fazendo alterações no seu grupo de controle global {#making-changes-to-your-global-control-group}

Você só pode fazer alterações no seu grupo de controle global desativando-o e criando um novo. Por exemplo, se você configurou um grupo de controle global que é 10% do seu público e deseja diminuir seu tamanho para 5%, você deve desativar seu grupo de controle global atual e reativar um novo grupo de controle global.

Você pode desativar seu grupo de controle global a qualquer momento na guia **Global Control Group Settings**, mas lembre-se de que fazer isso resulta em os usuários deste grupo se tornarem imediatamente elegíveis para Campaigns e Canvas.

Antes de desativar seu grupo de controle, [exporte](#export-group-members) um CSV dos usuários desse grupo caso precise consultá-lo posteriormente. Quando você desativa um grupo de controle, não há como a Braze restaurar o grupo ou identificar quais usuários estavam nele.

Após desativar seu grupo de controle, você pode salvar um novo. Quando você insere uma porcentagem e salva, a Braze gera um novo grupo de usuários selecionados aleatoriamente. Se você inserir a mesma porcentagem de antes, a Braze gera um novo grupo de usuários para seus grupos de controle e tratamento.

![Uma caixa de diálogo intitulada "Você está fazendo alterações nas configurações globais de envio de mensagens" com texto alertando que, uma vez que seu grupo de controle global é desativado, ele não é mais excluído de nenhuma Campaign ou Canvas novo ou ativo.]({% image_buster /assets/img/control_group/control_group2.png %}){: style="max-width:60%" }

## Exportar os membros do seu grupo de controle {#export-group-members}

Se você quiser ver quais usuários estão no seu grupo de controle global, pode exportar os membros do seu grupo por CSV ou API.

Para executar uma exportação CSV, navegue até a guia **Global Control Group Settings** e clique em <i class="fas fa-download" aria-label="Baixar"></i>&nbsp;**Export**. Para exportar por API, use o [endpoint `/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group).

{% alert important %}
Grupos de controle históricos não são preservados, então você só pode exportar os membros do seu grupo atual. Certifique-se de exportar todas as informações necessárias antes de desativar um grupo de controle.
{% endalert %}

## Verificar se um usuário está em um grupo de controle global {#view-whether-a-user-is-in-a-global-control-group}

Você pode verificar a participação no grupo de controle global acessando a seção **Miscellaneous** na guia **Engagement** do perfil de um usuário individual.

![Uma seção "Miscellaneous" informando que o usuário tem um número de bucket aleatório de 6356 e não está no grupo de controle global.]({% image_buster /assets/img/control_group/control_group1.png %}){: style="max-width:50%;"}

## Relatórios {#reporting}

O relatório do grupo de controle global permite que você compare seu grupo com uma amostra de tratamento. Sua amostra de tratamento é uma seleção aleatória de usuários que não estão no controle, com aproximadamente o mesmo número de usuários do seu controle, gerada usando o método de número de bucket aleatório.

### Visualizar um relatório {#viewing-a-report}

Para visualizar um relatório do seu grupo de controle global no dashboard, acesse **Analytics** > **Global Control Group Report**.

Em seguida, selecione o parâmetro com o qual deseja executar seu relatório (sessões ou um evento personalizado específico) e selecione **Run Report**.

![Selecione o parâmetro com o qual deseja executar seu relatório (sessões ou um evento personalizado específico) e selecione Run Report.]({% image_buster /assets/img/control_group/control_group6.png %})

### Configurar seu relatório {#configuring-your-report}

Ao gerar seu relatório, escolha um evento — sessões ou qualquer evento personalizado — para comparar entre seus grupos de tratamento e controle. Em seguida, escolha um período para visualizar os dados. Lembre-se de que, se você salvou vários experimentos de grupo de controle em períodos diferentes, deve evitar incluir dados de mais de um experimento no seu relatório.

Lembre-se de que as métricas percentuais no seu relatório são arredondadas. Por exemplo, em casos onde o número de conversões é uma porcentagem muito baixa do seu grupo de controle ou tratamento geral, a taxa de conversão pode ser arredondada para 0%.

Este relatório também exibe uma porcentagem de [confiança]({{site.baseurl}}/user_guide/messaging/ab_testing/analytics#understanding-confidence) para sua métrica de variação em relação ao controle. Em casos onde a taxa de conversão entre seu controle e tratamento são idênticas, uma confiança de 0% é esperada — isso indica que há 0% de chance de uma diferença no desempenho entre os dois grupos.

#### Tamanhos dos grupos {#group-sizes}

Antes de maio de 2024, o grupo de controle global era excluído do arquivamento de usuários, mas o grupo de amostra de tratamento não era. A partir de maio de 2024, ambos os grupos são excluídos do arquivamento de usuários. Isso pode resultar em seu grupo de amostra de tratamento e grupo de controle global tendo tamanhos significativamente diferentes. Na próxima vez que você redefinir seu grupo de controle global, essa discrepância será resolvida e você verá tamanhos de grupo semelhantes.

{% alert note %}
Cada espaço de trabalho tem no máximo um grupo de controle global e um grupo de amostra de tratamento. O grupo de amostra de tratamento é o mesmo grupo de usuários independentemente de como você configura seus relatórios de controle global.
{% endalert %}

### Métricas do relatório {#report-metrics}

| Métrica | Definição | Cálculo |
| -- | -- | -- |
| Variação em relação ao controle | Calcula o aumento entre a taxa de conversão dos seus grupos de tratamento e controle. | ((Taxa de conversão do tratamento – taxa de conversão do controle) ÷ taxa de conversão do controle) \* 100 |
| Aumento incremental | A diferença no total de eventos entre seus grupos de tratamento e controle. Essa métrica busca responder à pergunta: "Quantos eventos de conversão a mais o grupo de tratamento alcançou?". | Total de eventos do tratamento – total de eventos do controle |
| Porcentagem de aumento incremental | A porcentagem do total de eventos do seu tratamento que pode ser atribuída ao seu tratamento (versus comportamento natural do usuário). É calculada dividindo o aumento incremental (número) pelo número total de eventos do seu grupo de tratamento. | Aumento incremental (número) ÷ Total de eventos do grupo de tratamento |
| Taxa de conversão | A porcentagem estimada de usuários no seu grupo de controle ou tratamento que completam o evento selecionado durante o período selecionado. É calculada somando o número de eventos do período e dividindo pela soma de usuários dentro do grupo a cada dia. Isso só pode ser aproximado porque o tamanho do grupo flutua regularmente à medida que novos usuários entram no seu grupo de controle global, e os eventos são totais — e não únicos. Se o número de conversões for muito pequeno e seus grupos de controle ou tratamento forem muito grandes, a taxa de conversão pode ser arredondada para 0%. Se o número de eventos for muito alto — por exemplo, em casos onde um usuário pode realizar mais de um evento por dia — a taxa de conversão pode ser superior a 100%. | Soma do número de eventos para esses usuários nesse período ÷ soma de usuários no grupo a cada dia |
| Tamanho estimado do grupo | O número estimado de usuários nos seus grupos de controle e tratamento durante o período selecionado. | O tamanho máximo de participação que seus grupos de controle e tratamento alcançaram durante o período que você escolheu para o relatório. |
| Número total de eventos | O número total de vezes que o evento selecionado ocorreu durante o período escolhido. Não é único (por exemplo, se um usuário realiza um evento duas vezes durante o período, o evento é contado duas vezes). | Soma do número de vezes que um evento ocorreu a cada dia durante o período escolhido. |
| Eventos por usuário | O número médio estimado de vezes que os usuários em cada grupo completaram seus eventos de conversão durante o período selecionado. | Total de eventos ÷ tamanho estimado do grupo. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Métricas do relatório" }

## Solução de problemas {#troubleshooting}

Ao configurar seus grupos de controle globais e visualizar relatórios, aqui estão os erros que você pode encontrar:

| Problema | Solução |
| --- | --- |
| Não é possível salvar a porcentagem inserida ao designar um grupo de controle global. | Esse problema ocorre se você inserir um valor não inteiro ou um inteiro que não esteja entre 1 e 15 (inclusive). |
| Erro "A Braze não consegue atualizar seu grupo de controle global" na página de configurações do controle global. | Isso geralmente indica que algum componente desta página foi alterado, provavelmente devido a ações realizadas por outro usuário na sua conta da Braze. Nesse caso, atualize a página e tente novamente. |
| O relatório do grupo de controle global não tem dados. | Se você acessar o relatório do grupo de controle global sem ter salvo um grupo de controle global, não verá dados no relatório. Crie e salve um grupo de controle global e tente novamente. |
| Minha taxa de conversão é 0% ou não estou vendo o gráfico, mesmo havendo mais de zero eventos ocorrendo. | Se o número de conversões for muito pequeno e seus grupos de controle ou tratamento forem muito grandes, a taxa de conversão pode ser arredondada para 0% e, portanto, não aparecer no gráfico. Você pode verificar isso conferindo a métrica de número total de eventos. Você pode comparar a eficácia dos seus dois grupos usando a métrica de porcentagem de aumento incremental. |
| Minha taxa de conversão (ou outras métricas) está mudando drasticamente dependendo do período que estou visualizando. | Se você estiver visualizando dados em períodos curtos, é possível que suas métricas flutuem de dia para dia ou de semana para semana. Visualize as métricas ao longo de pelo menos um mês. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solução de problemas" }

### Pontos de atenção {#things-to-watch-for}

#### Sobreposição de números de bucket aleatórios {#overlapping-random-bucket-numbers}

Seu grupo de controle global é formado usando números de bucket aleatórios e, portanto, se você estiver executando outros testes usando filtros de Segment com números de bucket aleatórios, lembre-se de que pode haver uma sobreposição entre os segmentos que você cria e os usuários do seu grupo de controle global.

#### Endereços de e-mail duplicados {#duplicate-email-addresses}

Se dois usuários com IDs de usuário externo diferentes tiverem o mesmo endereço de e-mail, e um desses usuários estiver no grupo de controle e o outro não, um e-mail ainda será enviado para esse endereço de e-mail quando o usuário que não está no grupo de controle for elegível para um e-mail. Quando isso ocorre, ambos os perfis de usuário são marcados como tendo recebido a Campaign ou Canvas contendo esse e-mail.

#### Grupo de controle global e grupos de controle específicos de mensagem {#global-control-group-and-message-specific-control-groups}

É possível ter tanto um grupo de controle global quanto usar um grupo de controle específico de Campaign ou Canvas. Ter um grupo de controle específico de Campaign ou Canvas permite medir o impacto de uma mensagem específica.

Os usuários no seu grupo de controle global são impedidos de receber quaisquer mensagens, exceto aquelas com exceções de tag, e se você adicionar um controle a uma Campaign ou Canvas, a Braze retém uma parte do seu grupo de tratamento global de receber essa Campaign ou Canvas específica. Isso significa que, se um membro do grupo de controle global não for elegível para receber uma Campaign ou Canvas específica, ele não estará presente no grupo de controle dessa Campaign ou Canvas específica.

{% alert note %}
Resumindo, os usuários no grupo de controle global são filtrados do público da Campaign ou Canvas antes da entrada. Dos usuários que entram na Campaign ou Canvas, uma porcentagem deles é então atribuída à variante de controle.
{% endalert %}

#### Segments do grupo de controle global no console de desenvolvedor {#global-control-group-segments-on-the-developer-console}

Você pode ver vários Segments de **Global Control** na seção **Additional API Identifiers** da página [Chaves de API]({{site.baseurl}}/user_guide/administer/global/workspace_settings/apis_and_identifiers). Isso ocorre porque cada vez que o grupo de controle global é ativado ou desativado, um novo grupo de controle global é formado. Isso resulta em vários segmentos rotulados como "Global Control Group".

Apenas um desses segmentos está ativo e pode ser consultado usando o [endpoint `/users/export/global_control_group`]({{site.baseurl}}/api/endpoints/export/user_data/post_users_global_control_group), ou exportado do dashboard. A exportação do dashboard indica especificamente quais subsegmentos compõem este grupo de controle global.

## Melhores práticas de teste {#testing-best-practices}

### Tamanho ideal do grupo de controle {#percentage-guidelines}

Duas regras principais a ter em mente:
1. Seu grupo de controle não deve ter menos de 1.000 usuários.
2. Seu grupo de controle não deve ser mais de 10% do seu público total.

Se você tem um público total menor que 10.000, deve aumentar sua porcentagem para criar um grupo de mais de 1.000 usuários; nesse caso, não deve aumentar sua porcentagem acima de 15%. Lembre-se de que quanto menor o tamanho geral do seu espaço de trabalho, mais desafiador é executar um teste estatisticamente rigoroso.

- Algumas compensações a considerar ao pensar no tamanho do seu grupo de controle: você precisa de um número significativamente grande de clientes no seu grupo de controle para que qualquer análise de comportamento criada seja confiável. No entanto, quanto maior for seu grupo de controle, menos clientes recebem suas Campaigns, o que é uma desvantagem se você está usando suas Campaigns para impulsionar engajamento e conversões.
- A porcentagem ideal do seu público total depende do tamanho do seu público total. Quanto maior for seu público total, menor pode ser sua porcentagem. Se você tem um público pequeno, no entanto, precisa de uma porcentagem maior para seu grupo de controle.

### Duração do experimento {#experiment-duration}

#### Escolha uma duração ideal {#reshuffle}

Quanto tempo executar seu experimento antes de reorganizar a composição do grupo de controle depende do que você está testando e quais são os comportamentos de base dos seus usuários. Se você não tem certeza, um bom ponto de partida é um trimestre (três meses), mas você não deve usar menos de um mês.

Para determinar o período de tempo apropriado para seu experimento, considere quais perguntas você espera responder. Por exemplo, você está procurando ver se há uma diferença em sessões? Se sim, pense em com que frequência seus usuários têm sessões organicamente. Marcas cujos usuários têm sessões todos os dias podem executar experimentos mais curtos do que marcas cujos usuários têm sessões apenas algumas vezes por mês.

Ou, você pode estar interessado em um evento personalizado, então seu experimento pode precisar ser executado por mais tempo do que um experimento onde você está examinando sessões, se for provável que seus usuários disparem esse evento personalizado com menos frequência.

{% alert tip %}
Quanto mais tempo você mantiver o mesmo grupo de controle fora, mais eles divergem do grupo de tratamento, o que pode criar viés. Redefinir o grupo de controle global reequilibra a população.
{% endalert %}

#### Tente limitar o encerramento prematuro de experimentos {#try-to-limit-ending-experiments-prematurely}

Decida quanto tempo executar seu experimento antes de iniciá-lo e, em seguida, só encerre seu experimento e colete os resultados finais depois de atingir esse ponto predeterminado. Encerrar seu experimento antecipadamente, ou sempre que você vir dados promissores, introduz viés.

#### Pense em métricas valiosas {#think-about-valuable-metrics}

Considere quaisquer comportamentos de base para as métricas nas quais você está mais interessado. Você está interessado em taxas de compra para planos de inscrição que são renovados apenas anualmente? Ou os clientes têm um hábito semanal para o evento que você gostaria de medir? Pense em quanto tempo leva para os usuários potencialmente alterarem seus comportamentos devido ao seu envio de mensagens. Depois de decidir quanto tempo seu experimento deve durar, certifique-se de não encerrar seu experimento ou registrar resultados finais antecipadamente, ou suas descobertas podem ser enviesadas.