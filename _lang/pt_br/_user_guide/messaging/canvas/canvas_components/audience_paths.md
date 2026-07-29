---
nav_title: Jornadas do público
article_title: Jornadas do público
alias: /audience_paths/
page_order: 3
page_type: reference
description: "Este artigo de referência descreve como usar as Jornadas do público no seu Canvas para filtrar e segmentar usuários de forma intuitiva e em grande escala, enviando cada usuário pela primeira ramificação correspondente."
tool: Canvas

---

# Jornadas do público {#audience-paths}

> As Jornadas do público do Canvas permitem filtrar e segmentar usuários de forma intuitiva e em grande escala, enviando cada usuário pela primeira jornada cujos critérios ele atende.

Esse componente do Canvas elimina a necessidade de criar etapas completas excessivas baseadas em público, permitindo combinar o que poderiam ser oito componentes completos em apenas um. Isso ajuda a simplificar o direcionamento de usuários, deixando seus Canvas mais limpos e menos complexos.

## Como funciona {#how-it-works}

![Uma Jornada do público com dois grupos: usuários engajados e restante do público.]({% image_buster /assets/img/audience_path/audience_path.png %}){: style="float:right;max-width:45%;margin-left:15px;margin-top:15px;"}

Os usuários avançam pela primeira ramificação cujos critérios eles atendem, então coloque a jornada mais importante primeiro. Isso reduz a ambiguidade sobre para onde os usuários vão e quais mensagens eles recebem. Essa ordem não é [editável após o lançamento]({{site.baseurl}}/post-launch_edits).

Com as Jornadas do público, você pode:

- Enviar usuários por diferentes jornadas do Canvas com base em critérios de público.
- Colocar os grupos de público mais importantes primeiro; os usuários seguem pela primeira jornada para a qual se qualificam.
- Direcionar usuários com precisão em grande escala.
  - Você pode criar até oito grupos de público (dois padrão e seis adicionais) por etapa de Jornadas do público, mas pode conectar várias etapas de Jornadas do público para segmentar ainda mais seus usuários.

Dentro de uma única etapa de Jornadas do público, os usuários são avaliados em relação aos grupos de público em ordem e avançam pela primeira jornada para a qual se qualificam. Se você conectar várias etapas de Jornadas do público em um Canvas, os usuários serão avaliados novamente cada vez que alcançarem uma nova etapa de Jornadas do público.

### Como os usuários são avaliados {#how-users-are-evaluated}

![Canvas mostrando uma postergação de 24 horas após uma etapa de Mensagem, seguida por uma Jornada do público.]({% image_buster /assets/img/audience_path/audience_path5.png %}){: style="float:right;max-width:40%;margin-left:15px;"}

Os usuários são avaliados em relação a filtros e pertencimento a Segments **no momento em que alcançam a etapa de Jornada do público**, e não quando entraram no Canvas. Após a avaliação, eles avançam imediatamente para a jornada correspondente. Quando um usuário é colocado em um grupo de público, ele permanece nesse grupo mesmo que seu perfil de usuário mude depois.

<div style="clear: both;"></div>

{% alert important %}
As Jornadas do público avaliam com base nos atributos atuais do usuário, filtros e pertencimento a Segments no momento da avaliação. Elas não avaliam com base no evento específico que disparou a entrada no Canvas. Para direcionar usuários com base em uma ação que eles realizam (como um evento personalizado), use as [jornadas de ação]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/action_paths).
{% endalert %}

### Dando tempo para a avaliação dos usuários {#allowing-time-for-user-evaluations}

Como a avaliação é imediata, é importante adicionar uma postergação antes da Jornada do público se os critérios da jornada dependem de uma interação do usuário com uma etapa anterior.

Por exemplo, se os usuários recebem a Mensagem A e a próxima etapa é uma Jornada do público que avalia se eles interagiram com essa mensagem, todos os usuários avançarão para a etapa dos que não interagiram com a mensagem. Isso acontece porque os usuários avançaram imediatamente para a etapa de Jornada do público sem tempo para interagir com a mensagem. Em outras palavras, os usuários são avaliados quanto à interação com a mensagem quase imediatamente após o envio.

Para dar tempo aos usuários de interagir com uma mensagem enviada, adicione uma postergação entre a etapa de Mensagem e a Jornada do público. Por exemplo, uma postergação de 24 horas dá aos usuários 24 horas após o envio da mensagem para interagir com a Mensagem A antes da avaliação.

## Criando uma Jornada do público {#creating-an-audience-path}

Para adicionar uma etapa de Jornadas do público, faça o seguinte:

1. Adicione uma etapa ao seu Canvas.
2. Arraste e solte o componente da barra lateral, ou selecione <i class="fas fa-plus-circle"></i> **Adicionar** na parte inferior de uma etapa e selecione **Jornadas do público**.

O componente padrão de Jornadas do público contém dois grupos de público padrão: **Grupo 1** e **Restante do público**. O grupo **Restante do público** inclui qualquer usuário que não se enquadre em um grupo de público definido. Esse grupo é sempre o último na ordem.

### Definindo grupos de público {#defining-audience-groups}

A captura de tela a seguir mostra a disposição de uma etapa expandida de Jornadas do público. Aqui, você pode definir até oito grupos de público (um predefinido e sete personalizáveis). Para definir um grupo de público, selecione o nome do grupo no editor de Jornadas do público. Você pode renomear seu grupo de público, escolher os filtros e Segments que se aplicam ao seu grupo e adicionar ou excluir grupos. Por exemplo, se você quisesse direcionar mensagens de integração para um grupo de usuários, poderia selecionar filtros de redirecionamento, como "Clicou em e-mail" e "Clicou em mensagem no app".

![Uma Jornada do público expandida com grupos para "Adora Culinária Asiática", "Adora Culinária Latina", "Adora Culinária Europeia" e "Restante do público".]({% image_buster /assets/img/audience_path/audience_path3.png %})

Após a conclusão da etapa de Jornadas do público, cada grupo de público terá uma ramificação separada. Você pode continuar usando Jornadas do público para filtrar ainda mais seu público ou prosseguir com a jornada do Canvas usando as etapas padrão do Canvas.

![Duas Jornadas do público com diferentes grupos baseados em engajamento.]({% image_buster /assets/img/audience_path/audience_path4.png %}){: style="max-width:50%"}

#### Usando filtros de comparação com variáveis de contexto {#using-comparison-filters-with-context-variables}

Ao dividir com base em uma variável de contexto que contém uma data, consulte [Filtros de dia do ano e hora para variáveis de contexto de data]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/sources/context_variables#day-of-year-and-time-filters-for-date-context-variables) para escolher o tipo de comparação correto.

### Testando grupos de público {#testing-audience-groups}

Após adicionar Segments e filtros aos seus grupos de público, você pode testar se os grupos estão configurados conforme esperado [pesquisando um usuário]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment) para confirmar que ele corresponde aos critérios de público.

![A seção "Pesquisa de usuário".]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

## Usando Jornadas do público {#using-audience-paths}

O verdadeiro poder das Jornadas do público está em colocar as jornadas mais importantes **primeiro**. Embora esse recurso não precise ser usado estrategicamente, alguns profissionais de marketing podem querer promover certos produtos para os usuários, como ofertas especiais ou edições limitadas.

Ao colocar esses Segments primeiro na lista, você pode direcionar usuários que se enquadram em filtros e Segments específicos, ao mesmo tempo em que direciona usuários que podem não atender a esses critérios específicos — tudo em uma única etapa do Canvas.

![Uma Jornada do público com grupos para "Gosta de Sapatos Big Brand", "Gosta de Big Brand" e "Restante do público".]({% image_buster /assets/img/audience_path/audience_path2.png %}){: style="float:right;max-width:50%;margin-left:15px;margin-bottom:15px;"}

Por exemplo, digamos que você queira enviar anúncios de novos produtos para um grupo de usuários. Você começaria colocando os filtros relacionados a esses produtos **primeiro** na Jornada do público. Se você estivesse criando uma campanha de marketing para a empresa "Big Brand" e uma nova marca de varejo tivesse acabado de ser lançada, poderia selecionar filtros como "Gosta de Sapatos Big Brand" ou "Gosta de Bolsas Big Brand" e enviar diferentes mensagens de e-mail com base no grupo filtrado em que se enquadram.

Quando os usuários entram nesse componente de Jornadas do público, eles são avaliados primeiro para o Grupo de público 1 "Gosta de Sapatos Big Brand" — a primeira jornada na lista. Se corresponderem, eles continuam para o próximo componente definido no seu Canvas. Se não "Gostam de Sapatos Big Brand", eles são avaliados para o próximo grupo de público, Grupo de público 2 "Gosta de Bolsas Big Brand", e continuam para a próxima etapa se os critérios forem atendidos. Por fim, os usuários que não se enquadram nos grupos anteriores caem no grupo "Restante do público" e também continuam para a próxima etapa do Canvas que você definir para essa jornada.

Você também pode ver o desempenho dessa etapa usando a [análise de dados do Canvas]({{site.baseurl}}/user_guide/messaging/canvas/testing_canvases/measuring_and_testing_with_canvas_analytics#performance-visualization).

### Segmentando Jornadas do público com números de bucket aleatórios {#segmenting-audience-paths-with-random-bucket-numbers}

Se o seu Canvas usa um [limite de frequência]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping) (como limitar o número total de usuários que receberão o Canvas), a Braze recomenda que você não use números de bucket aleatórios para segmentar suas Jornadas do público.

Um [número de bucket aleatório]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts/random_bucket_numbers) é um atributo de usuário que pode ser usado para criar segmentos uniformemente distribuídos de usuários aleatórios. A Braze usa o número de bucket aleatório para agrupar usuários durante a fase de segmentação da entrada no Canvas, e cada grupo é processado separadamente. Dependendo de quais grupos terminam o processamento primeiro, alguns usuários podem ser limitados na entrada devido ao limite de frequência, o que pode causar uma distribuição desigual de usuários quando eles alcançam a etapa de Jornadas do público.

Nesse cenário, tente usar as [jornadas experimentais]({{site.baseurl}}/user_guide/messaging/canvas/canvas_components/experiment_step).

### Usando o filtro de canal inteligente com Jornadas do público {#using-intelligent-channel-filter-with-audience-paths}

Usando uma combinação de etapas de Jornadas do público e filtros de canal inteligente, você pode personalizar sua experiência de mensagens de acordo com as preferências e comportamentos de cada usuário. Dessa forma, seus usuários receberão as mensagens mais relevantes pelos canais apropriados.

Por exemplo, em uma etapa de Jornadas do público, você pode criar três públicos: e-mail, push mobile e restante do público. Para o público de e-mail, adicione o filtro `Intelligent Channel is Email`. Para o público de push mobile, adicione o filtro `Intelligent Channel is Mobile Push`. Em seguida, você pode adicionar uma etapa de Mensagem para cada uma das jornadas do público para entregar mensagens personalizadas e relevantes.

{% alert tip %}
Confira nossos [modelos de Canvas da Braze]({{site.baseurl}}/user_guide/messaging/templates/canvas_templates/braze_templates) para ver exemplos de como personalizar esses modelos pré-construídos a seu favor.
{% endalert %}