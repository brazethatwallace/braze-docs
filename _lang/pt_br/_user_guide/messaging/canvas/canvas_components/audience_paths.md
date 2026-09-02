---
nav_title: Jornadas do público
article_title: Jornadas do público
alias: /audience_paths/
page_order: 3
page_type: reference
description: "Este artigo de referência descreve como usar as Jornadas do público no seu Canvas para filtrar e segmentar usuários de forma intuitiva e em grande escala, enviando cada usuário pela primeira Branch or ramificação or ramificação correspondente."
tool: Canvas

---

# Jornadas do público {#audience-paths}

> As Jornadas do público do Canvas permitem filtrar e segmentar usuários de forma intuitiva e em grande escala, enviando cada usuário pela primeira jornada cujos critérios ele atende.

Esse componente do Canvas elimina a necessidade de criar etapas completas excessivas baseadas em público, permitindo combinar o que poderiam ser oito componentes completos em apenas um. Isso ajuda a simplificar o direcionamento de usuários, deixando seus Canvas mais limpos e menos complexos.

## Como funciona {#how-it-works}

![Uma jornada do público com dois grupos: usuários engajados e todos os demais.]({% image_buster /assets/img/audience_path/audience_path.png %}){: style="float:right;max-width:45%;margin-left:15px;margin-top:15px;"}

Os usuários avançam pela primeira Branch or ramificação or ramificação cujos critérios eles atendem, então coloque a jornada mais importante primeiro. Isso reduz a ambiguidade sobre para onde os usuários vão e quais mensagens eles recebem. Note que essa ordem não é [editável após o lançamento]({{site.baseurl}}/post-launch_edits).

Com as jornadas do público, você pode:

- Enviar usuários por diferentes jornadas do Canvas com base em critérios de público.
- Colocar seus grupos de público mais importantes primeiro; os usuários seguem pela primeira jornada para a qual se qualificam.
- Direcionar usuários com precisão em grande escala.
  - Você pode criar até oito grupos de público (dois padrão e seis grupos adicionais) por etapa de jornada do público, mas talvez queira conectar várias etapas de jornada do público para classificar ainda mais seus usuários.

Dentro de uma única etapa de jornada do público, os usuários são avaliados em relação aos grupos de público em ordem e avançam pela primeira jornada para a qual se qualificam. Se você conectar várias etapas de jornada do público em um Canvas, os usuários serão avaliados novamente cada vez que chegarem a uma nova etapa de jornada do público.

### Como os usuários são avaliados {#how-users-are-evaluated}

![Canvas mostrando uma postergação de 24 horas após uma etapa de mensagem, seguida por uma jornada do público.]({% image_buster /assets/img/audience_path/audience_path5.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Os usuários são avaliados em relação a filtros e pertencimento a Segments **no momento em que chegam à etapa de jornada do público** — não quando entraram no Canvas. Após a avaliação, eles avançam imediatamente para a jornada correspondente. Quando um usuário é colocado em um grupo de público, ele permanece nesse grupo mesmo que seu perfil de usuário mude depois.

<div style="clear: both;"></div>

{% alert important %}
As jornadas do público avaliam com base nos atributos atuais do usuário, filtros e pertencimento a Segments no momento da avaliação. Elas não avaliam com base no evento específico que disparou a entrada no Canvas. Para direcionar usuários com base em uma ação que eles realizam (como um evento personalizado), use [jornadas de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths) em vez disso.
{% endalert %}

Os usuários não são reavaliados em relação ao seu grupo de público depois de avançarem por uma jornada. Se a mensagem que vem em seguida for postergada por uma etapa de postergação, horário de silêncio, Intelligent Timing, limite de frequência ou entrega por fuso local, o perfil de um usuário pode mudar antes do envio dessa mensagem.

Para confirmar que os usuários ainda atendem aos critérios de Segment or segmento e filtro antes que a etapa de mensagem envie, ative **Validar público no envio da mensagem** nas [validações de entrega]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/message_step#delivery-validations) da etapa de mensagem. As validações de entrega verificam apenas os Segments e filtros que você adiciona àquela etapa de mensagem, então elas não reutilizam os critérios da sua jornada do público. Para In-App Messages, as validações de entrega são verificadas quando o usuário entra na etapa de mensagem, não quando a mensagem é exibida.

### Permitindo tempo para avaliações de usuários {#allowing-time-for-user-evaluations}

Como a avaliação é imediata, é importante adicionar uma postergação antes da jornada do público se os critérios da jornada dependerem de uma interação do usuário com uma etapa anterior.

Por exemplo, se os usuários receberem a Mensagem A e a próxima etapa for uma jornada do público que avalia se eles interagiram com essa mensagem, todos os usuários avançarão para a etapa dos que não interagiram com a mensagem. Isso acontece porque os usuários avançaram imediatamente para a etapa de jornada do público sem tempo para interagir com a mensagem. Em outras palavras, os usuários são avaliados quanto à interação com a mensagem quase imediatamente após o envio.

Para dar tempo aos usuários de interagir com uma mensagem enviada, adicione uma postergação entre a etapa de mensagem e a jornada do público. Por exemplo, uma postergação de 24 horas dá aos usuários 24 horas após o envio da mensagem para interagir com a Mensagem A antes da avaliação.

## Criando uma jornada do público {#creating-an-audience-path}

Para adicionar uma etapa de jornadas do público, faça o seguinte:

1. Adicione uma etapa ao seu Canvas.
2. Arraste e solte o componente a partir da barra lateral, ou selecione <i class="fas fa-plus-circle"></i> **Adicionar** na parte inferior de uma etapa e selecione **Audience Paths**.

O componente padrão de jornadas do público contém dois grupos de público padrão: **Grupo 1** e **Todos os outros**. O grupo **Todos os outros** inclui qualquer usuário que não se encaixe em um grupo de público definido. Esse grupo está sempre por último na ordem.

### Definindo grupos de público {#defining-audience-groups}

A captura de tela a seguir mostra o layout de uma etapa de jornadas do público expandida. Aqui, você pode definir até oito grupos de público (um predefinido e sete personalizáveis). Para definir um grupo de público, selecione o nome do grupo no editor de jornadas do público. Você pode renomear seu grupo de público, escolher os filtros e Segments que se aplicam ao seu grupo e adicionar ou excluir grupos. Por exemplo, se você quisesse direcionar mensagens de integração para um grupo de usuários, poderia selecionar filtros de redirecionamento, como "Clicou em e-mail" e "Clicou em mensagem no app".

![Uma jornada do público expandida com grupos para "Ama Culinária Asiática", "Ama Culinária Latina", "Ama Culinária Europeia" e "Todos os Outros".]({% image_buster /assets/img/audience_path/audience_path3.png %})

Após a conclusão da etapa de jornadas do público, cada grupo de público terá uma Branch or ramificação or ramificação separada. Você pode continuar usando jornadas do público para filtrar ainda mais seu público, ou prosseguir na sua jornada do Canvas com as etapas padrão do Canvas.

![Duas jornadas do público com diferentes grupos baseados em engajamento.]({% image_buster /assets/img/audience_path/audience_path4.png %}){: style="max-width:50%"}

#### Usando filtros de comparação com variáveis de contexto {#using-comparison-filters-with-context-variables}

Ao dividir por uma variável de contexto que contém uma data, consulte [Filtros de dia do ano e hora para variáveis de contexto de data]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#day-of-year-and-time-filters-for-date-context-variables) para escolher o tipo de comparação correto.

### Testando grupos de público {#testing-audience-groups}

Após adicionar Segments e filtros ao seu público, você pode testar se os grupos de público estão configurados conforme o esperado [pesquisando um usuário]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) para confirmar que ele corresponde aos critérios do público.

![A seção "Pesquisa de Usuário".]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

## Usando jornadas do público {#using-audience-paths}

O verdadeiro poder das jornadas do público está em colocar as jornadas mais importantes **primeiro**. Embora esse recurso não precise necessariamente ser usado de forma estratégica, alguns profissionais de marketing podem querer promover certos produtos para os usuários, como ofertas especiais ou lançamentos de edição limitada.

Ao colocar esses Segments primeiro na lista, você pode direcionar usuários que se enquadram em filtros e Segments específicos e, ao mesmo tempo, direcionar usuários que talvez não atendam a esses critérios — tudo em uma única etapa do Canvas.

![Uma jornada do público com grupos para "Likes Big Brand Shoes", "Likes Big Brand" e "Everyone Else".]({% image_buster /assets/img/audience_path/audience_path2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Por exemplo, digamos que você queira enviar anúncios de novos produtos para um grupo de usuários. Você começaria colocando os filtros referentes a esses produtos **primeiro** na jornada do público. Se você estivesse criando uma campanha de marketing para a empresa "Big Brand" e uma nova marca de varejo tivesse acabado de ser lançada, você poderia selecionar filtros como "Likes Big Brand Shoes" ou "Likes Big Brand Bags" e enviar diferentes mensagens de e-mail com base no grupo filtrado em que cada usuário se enquadra.

Quando os usuários entram nesse componente de jornadas do público, eles são avaliados primeiro pelo Grupo de Público 1, "Likes Big Brand Shoes" — a primeira jornada da lista. Se corresponderem, eles seguem para o próximo componente definido no seu Canvas. Se não corresponderem a "Like Big Brand Shoes", são avaliados pelo próximo grupo de público, Grupo de Público 2, "Likes Big Brand Bags", e seguem para a próxima etapa se os critérios forem atendidos. Por fim, os usuários que não se enquadram nos grupos anteriores são direcionados ao grupo "Everybody Else" e também seguem para a próxima etapa do Canvas que você definir para essa jornada.

Você também pode ver o desempenho dessa etapa usando a [análise de dados do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics#performance-visualization).

### Segmentando jornadas do público com números de bucket aleatórios {#segmenting-audience-paths-with-random-bucket-numbers}

Se o seu Canvas usa um [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) (como limitar o número total de usuários que receberão o Canvas), a Braze recomenda que você não use números de bucket aleatórios para segmentar suas jornadas do público.

Um [número de bucket aleatório]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) é um atributo de usuário que pode ser usado para criar Segments de usuários aleatórios distribuídos uniformemente. A Braze usa o número de bucket aleatório para agrupar usuários durante a fase de segmentação da entrada no Canvas, e cada grupo é processado separadamente. Dependendo de quais grupos terminam o processamento primeiro, alguns usuários podem ser limitados na entrada devido ao limite de frequência, o que pode causar uma distribuição desigual de usuários quando eles chegam à etapa de jornadas do público.

Nesse cenário, tente usar [jornadas experimentais]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step) em vez disso.

### Usando o filtro de canal inteligente com jornadas do público {#using-intelligent-channel-filter-with-audience-paths}

Ao combinar etapas de jornadas do público com filtros de canal inteligente, você pode personalizar a experiência de mensagens de acordo com as preferências e comportamentos de cada usuário. Dessa forma, seus usuários recebem as mensagens mais relevantes pelos canais mais adequados.

Por exemplo, em uma etapa de jornadas do público, você pode criar três públicos: E-mail, Push Móvel e Todos os Outros. Para o público de E-mail, adicione o filtro `Intelligent Channel is Email`. Para o público de Push Móvel, adicione o filtro `Intelligent Channel is Mobile Push`. Em seguida, você pode adicionar uma etapa de mensagem para cada jornada do público para entregar mensagens personalizadas e relevantes.

{% alert tip %}
Confira nossos [modelos de Canvas da Braze]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) para ver exemplos de como personalizar esses modelos pré-criados a seu favor.
{% endalert %}