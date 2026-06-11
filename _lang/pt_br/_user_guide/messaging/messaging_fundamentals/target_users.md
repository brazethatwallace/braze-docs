---
nav_title: Direcionar usuários
article_title: Direcionar usuários
page_order: 12
page_type: reference
description: "Este artigo de referência aborda como direcionar seu público nos editores de Campaign e Canvas."
tool:
    - Campaigns
    - Canvas
---

# Direcionar usuários {#target-users}

> Determinar como direcionar seus usuários é uma das etapas mais cruciais ao criar uma Campaign ou Canvas. Ao entender como segmentar seu público com base em comportamentos, preferências e dados demográficos, você pode personalizar e adaptar suas mensagens.

## Criando um público-alvo {#creating-a-target-audience}

### Etapa 1: Escolher usuários {#step-1-choose-users}

Em **Opções de direcionamento**, você pode usar as seguintes opções para escolher quais usuários deseja direcionar para sua Campaign ou Canvas. Somente os usuários que corresponderem aos critérios definidos receberão a mensagem. Lembre-se de que a associação exata ao segmento é sempre calculada imediatamente antes do envio da mensagem.

{% tabs local %}
{% tab segmento único %}
Para direcionar membros de um segmento criado anteriormente, selecione um segmento no menu suspenso em **Direcionar por segmento de usuários**.
{% endtab %}

{% tab múltiplos segmentos %}
Para direcionar usuários que se enquadram em múltiplos segmentos criados anteriormente, adicione vários segmentos no menu suspenso em **Direcionar por segmento de usuários**. O público-alvo resultante será composto por usuários que estão no primeiro segmento, no segundo segmento, no terceiro segmento, e assim por diante.
{% endtab %}

{% tab múltiplos filtros %}
Para direcionar usuários sem adicionar um segmento, você pode usar uma série de filtros. Esse é um público improvisado durante a criação da mensagem e permite que você pule a criação de segmentos ao enviar para públicos pontuais.

![Filtros adicionais para uma mensagem que direciona usuários que abriram o app pela última vez no dia, nunca receberam uma Campaign ou etapa do Canvas, e fizeram uma compra há menos de 30 dias.]({% image_buster /assets/img_archive/additional_filters.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab segmentos e filtros %}
Você também pode direcionar usuários de um ou mais segmentos criados anteriormente que também se enquadram em filtros adicionais. Após selecionar seus segmentos, você pode refinar ainda mais seu público na seção **Filtros adicionais**. Isso é demonstrado na captura de tela a seguir, que direciona usuários que estão no segmento "Daily Active Users", no segmento "Never opened email" e fizeram uma compra há mais de 30 dias.

![Opções de direcionamento para uma mensagem que inclui dois segmentos e tem um filtro adicional para última compra feita há menos de 30 dias.]({% image_buster /assets/img_archive/target_segmenter.png %}){: style="max-width:90%;"}
{% endtab %}

{% tab Apps específicos %}

Você pode entregar uma mensagem de Campaign ou etapa do Canvas para apps específicos, como enviar uma mensagem no app ou notificação por push apenas para apps Android ou iOS.

No entanto, lembre-se de que é possível que um usuário use vários apps. O filtro "Has app" identifica todos os usuários que possuem o app selecionado, mas não controla quais apps recebem as mensagens. Por exemplo, se você aplicar um filtro de segmento em que "Has app" está definido como Android, qualquer usuário que também tenha o app iOS também receberá a mensagem no app iOS.

![Um filtro para usuários que possuem o app "Hello, World (Android)".]({% image_buster /assets/img_archive/has_app_hello_world.png %}){: style="max-width:60%;"}

Digamos que você queira enviar uma mensagem no app apenas para apps Android.

1. Crie um segmento e defina **Apps e sites direcionados** como **Usuários de apps específicos**, depois selecione seu app Android.

![Um segmento direcionando usuários de um app específico, "Test_Android".]({% image_buster /assets/img_archive/app_test_android.png %}){: style="max-width:60%;"}

{: start="2"}
2. Na etapa **Públicos-alvo**, confirme que seu segmento foi adicionado na seção **Direcionar por segmento de usuários**.

![A etapa "Públicos-alvo" com um segmento de exemplo selecionado.]({% image_buster /assets/img_archive/target_users_by_segment_example.png %})

{% alert note %}
Isso não funcionará se você adicionar seu segmento na seção **Filtros adicionais** por meio de um filtro de associação a segmento. Você deve referenciar diretamente seu segmento em **Direcionar por segmento de usuários** para entregar sua mensagem apenas para aquele app.
{% endalert %}

{% endtab %}
{% endtabs %}

{% alert tip %}
Para Campaigns de e-mail, você pode direcionar grupos de teste na seção **Grupos de teste**. Os grupos de teste não estão disponíveis para Campaigns de API, embora você possa incluir grupos de teste por meio de uma entrada acionada por API em uma Campaign. Para saber mais, consulte [Grupos de teste]({{site.baseurl}}/user_guide/administer/global/user_management/internal_groups/#seed-groups).
{% endalert %}

### Etapa 2: Testar seu público {#step-2-test-your-audience}

Após adicionar segmentos e filtros ao seu público, você pode testar se o público está configurado conforme esperado [pesquisando um usuário]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/) para confirmar se ele corresponde aos critérios do público.

![A seção "Pesquisa de usuário" com um botão "Pesquisar usuário".]({% image_buster /assets/img_archive/user_lookup.png %}){: style="max-width:70%"}

#### Resumo do público {#audience-summary}

O **Resumo do público** mostrará uma visão geral de quem está no seu público-alvo. Aqui, você pode limitar ainda mais seu público definindo um limite máximo de usuários ou [limitando a taxa]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping/) de velocidade de entrega.

![A seção "Resumo do público" com opções para definir um limite máximo de usuários ou limitar a taxa de velocidade de entrega.]({% image_buster /assets/img_archive/audience_summary.png %})

#### Testes A/B {#ab-testing}

Na seção **Testes A/B**, você pode configurar um teste para comparar as respostas dos usuários a múltiplas versões da mesma Campaign de marketing. Essas versões compartilham objetivos de marketing semelhantes, mas diferem na redação e no estilo. O objetivo é identificar a versão da Campaign que melhor atinge seus objetivos de marketing.

Para saber mais e conhecer as práticas recomendadas, consulte [Testes multivariantes e A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/).

#### Estatísticas do público {#audience-statistics}

A Braze fornece estatísticas detalhadas do público dos canais direcionados no rodapé. Quanto maior for sua base de usuários, mais provável é que a quantidade de **Usuários contatáveis** seja uma estimativa aproximada. O número de usuários contatáveis pode diminuir se você usar um [Grupo de controle global]({{site.baseurl}}/user_guide/audience/global_control_group/) ou configurar a elegibilidade de mensagens.

- Para determinar um número preciso de usuários contatáveis, selecione [Calcular estatísticas exatas]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment/#calculating-exact-statistics), pois isso pesquisará cada usuário na sua base de usuários.
- Para ver qual porcentagem da sua base de usuários está sendo direcionada ou o Lifetime Value (LTV) desse segmento, selecione **Mostrar estatísticas adicionais**.

##### Por que a contagem do público-alvo pode diferir da contagem de usuários contatáveis {#why-the-target-audience-count-could-differ-from-the-reachable-users-count}

{% multi_lang_include segments.md section='Differing audience size' %}

![A seção "População total" com contagens estimadas de usuários contatáveis em cada canal direcionado.]({% image_buster /assets/img_archive/multi_channel_footer.png %})

{% alert note %}
O cálculo de estatísticas exatas pode levar alguns minutos para ser executado. Essa função calcula as estatísticas exatas apenas no nível do segmento, não no nível do filtro ou grupo de filtros.<br><br>
Para segmentos grandes, é normal observar pequenas variações mesmo ao calcular estatísticas exatas. A precisão dessa funcionalidade é esperada em 99,999% ou mais.
{% endalert %}

## Como o público-alvo e os critérios de entrada funcionam juntos {#how-target-audience-and-entry-criteria-work-together}

Ao criar uma Campaign ou Canvas na Braze, o direcionamento acontece em duas partes:

1. **Público-alvo:** Quem se qualifica
2. **Critérios de entrada:** O que aciona a entrega

A ordem importa: a Braze verifica se alguém está no público-alvo antes de avaliar os critérios de entrada. Se um usuário não se qualificar para o público naquele momento, ele não entrará na Campaign ou no Canvas — mesmo que depois acione o evento de entrada. Pense no público-alvo como uma sala de espera: somente os usuários que já estão dentro quando o gatilho ocorre podem seguir em frente.

### Exemplo 1 {#example-1}

Você quer enviar uma mensagem push durante a primeira sessão de um usuário.

Você define:

- **Público-alvo:** Usuários com contagem de sessões = 0
- **Evento de entrada:** Início de sessão

Quando o usuário abre seu app, a Braze vê que a contagem de sessões agora é 1 — e ele não se qualifica mais para o público. O evento de entrada acontece depois que ele já não é mais elegível, então a mensagem não será enviada.

Para que isso funcione, o usuário precisa se qualificar para o público antes do início da sessão (inverta o público-alvo e o gatilho de entrada).

### Exemplo 2 {#example-2}

Você quer enviar um e-mail para usuários que gastaram mais de $10 nos últimos 7 dias.

Você define:

- **Público-alvo:** Usuários que gastaram mais de $10 nos últimos 7 dias
- **Evento de entrada:** Qualquer compra

Agora imagine que um usuário gasta $12 hoje. Isso não aciona a mensagem — apenas o torna elegível para entrar no público. Ele não receberá o e-mail a menos que faça outra compra depois.

Uma abordagem melhor seria usar um público mais amplo e mover o filtro para os critérios de entrada:

- **Público:** Todos os usuários (ou seu público base)
- **Evento de entrada:** Fazer uma compra
- **Filtro de entrada:** Gasto total nos últimos 7 dias > $10

Dessa forma, uma compra qualificada atende ao filtro e aciona a mensagem ao mesmo tempo — sem necessidade de uma segunda ação.

## Práticas recomendadas {#best-practices}

- Certifique-se de que o segmento do público inclui os usuários antes que os critérios de entrada ocorram.
- Evite usar filtros de público que só se aplicam após o evento. Se um filtro depende de algo que acontece no momento do gatilho (como "contagem de sessões = 0"), o usuário pode não se qualificar mais quando a Braze fizer a verificação.
- Use lógica baseada em tempo com cuidado. Por exemplo, se você quer direcionar novos usuários:
    - Defina seu público-alvo como "usou o app pela primeira vez nos últimos 7 dias".
    - Defina seu evento de entrada como "início de sessão".
    - Dessa forma, somente os usuários que ainda estão na primeira semana se qualificarão e entrarão quando iniciarem uma sessão.