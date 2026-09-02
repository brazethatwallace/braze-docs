---
nav_title: Inbox Vision
article_title: Inbox Vision
page_order: 7
description: "Esta página explica como configurar o Inbox Vision, um recurso que permite aos profissionais de marketing visualizar seus e-mails a partir da perspectiva de vários clientes de e-mail e dispositivos móveis."
tool:
  - Dashboard
channel:
  - email
---

# Inbox Vision {#inbox-vision}

> O Inbox Vision permite que você visualize seus e-mails a partir da perspectiva de vários clientes de e-mail e dispositivos móveis. Por exemplo, você pode testar as diferenças entre o modo escuro e o modo claro para confirmar se seus e-mails são exibidos como pretendido.

{% alert important %}
O Inbox Vision pode não funcionar se o conteúdo do seu e-mail depender de informações de template, como dados de perfil de usuário. A Braze usa um usuário vazio como modelo ao enviar e-mails para esse recurso.<br><br>Adicione valores padrão a qualquer Liquid na sua mensagem de e-mail. Sem valores padrão, você pode receber um falso positivo ou o teste pode falhar.
{% endalert %}

## Considerações {#considerations}

De modo geral, seu e-mail não funcionará com o Inbox Vision se o conteúdo depender de informações de modelagem, como dados do perfil de usuário. Isso acontece porque a Braze usa um usuário vazio como modelo ao enviar e-mails com esse recurso.

Você pode resolver isso adicionando valores padrão ou quaisquer valores ao Liquid na sua mensagem de e-mail antes de executar o Inbox Vision. Quando você terminar os testes no Inbox Vision, a mensagem de e-mail original será exibida novamente. Se nenhum valor for fornecido, o teste pode não conseguir renderizar as prévias corretamente.

Sua empresa tem um limite de quantos e-mails você pode pré-visualizar com o Inbox Vision. Você pode monitorar isso na guia **Email Previews** do Inbox Vision.

Inclua uma linha de assunto e um domínio de envio válido para visualizar as prévias. Fique atento às diferenças de renderização entre desktop e dispositivos móveis. Use as prévias para confirmar que o e-mail aparece conforme esperado.

{% alert note %}
Se a prévia de uma Campaign exibir um erro de permissão, limpe o cache e os cookies, ou tente em uma janela anônima. Extensões do navegador às vezes bloqueiam a prévia.
{% endalert %}

Para testar sua mensagem de e-mail no Inbox Vision:

1. Acesse o editor de arrastar e soltar ou o editor de HTML de e-mail.
2. No editor, selecione **Preview & Test**.
3. Selecione **Inbox Vision**.
4. Selecione **Run Inbox Vision**. Isso leva até dez minutos.
5. Em seguida, selecione um bloco para visualizar a prévia com mais detalhes. Essas prévias são agrupadas nas seguintes seções: **Web Clients**, **Application Clients** e **Mobile Clients**.

![A opção de selecionar clientes de e-mail para pré-visualização.]({% image_buster /assets/img/select_email_preview_inbox_vision.png %}){: style="max-width:85%;"}

{:start="5"}
5. Selecione **Run Inbox Vision**. Isso pode levar de dois a dez minutos para ser concluído.

{% alert note %}
O Inbox Vision não oferece suporte a mensagens de e-mail que incluam [lógica de interrupção]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages), pois esses e-mails são renderizados como conteúdo estático.
{% endalert %}

### Pré-visualizando como um usuário {#previewing-as-a-user}

Quando você pré-visualiza como um usuário aleatório, o Inbox Vision não salva configurações ou atributos específicos do usuário (como nome ou preferências). Quando você seleciona um usuário personalizado, a prévia do Inbox Vision pode ser diferente de outras prévias, pois utiliza dados específicos daquele usuário.

## Análise de código {#code-analysis}

A análise de código destaca possíveis problemas de HTML, mostra o número de ocorrências e indica elementos HTML não suportados.

### Visualizando informações da análise de código {#viewing-code-analysis-information}

Encontre essas informações na guia **Inbox Vision** selecionando <i class="fas fa-list"></i> **List view**. A visualização em lista está disponível apenas para modelos de e-mail em HTML. Para modelos de arrastar e soltar, use as prévias para resolver problemas.

![Exemplo de análise de código na prévia do Inbox Vision.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
A análise de código pode aparecer mais rápido do que a prévia para um determinado cliente, porque a Braze aguarda até que o e-mail chegue antes de capturar a tela.
{% endalert %}

## Testes de SPAM {#spam-testing}

Os testes de SPAM estimam se um e-mail pode ser filtrado como SPAM. Os testes são executados em filtros como IronPort, SpamAssassin e Barracuda, além de filtros de ISP como Gmail e Outlook, usando caixas de entrada de teste estáticas que não abrem nem clicam por padrão.

{% alert important %}
O posicionamento na caixa de entrada é determinado principalmente pelo engajamento dos destinatários em tempo real. Os resultados dos testes de SPAM podem não corresponder ao que você observa em Campaigns reais.
{% endalert %}

Para uma leitura mais clara sobre entregabilidade, teste o conteúdo com pequenas coortes ativas — aberturas e cliques fortes são o sinal mais confiável. Use os testes de SPAM como uma entrada complementar junto ao monitoramento de engajamento.

### Visualizando os resultados do teste de SPAM {#viewing-spam-test-results}

Para verificar os resultados do seu teste de SPAM:

1. Selecione a guia **Spam Testing** na seção **Inbox Vision**. A tabela **Spam Test Result** lista o nome do filtro de SPAM, o status e o tipo.
2. Analise esses resultados e faça os ajustes necessários na sua campanha de e-mail.
3. Selecione **Re-run Test** para recarregar os resultados do teste de SPAM.

## Testes de acessibilidade {#accessibility-testing}

Os testes de acessibilidade destacam possíveis problemas de acessibilidade no seu e-mail e mostram quais elementos não atendem aos padrões. A Braze analisa o conteúdo com base em diretrizes selecionadas das Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)), um conjunto de padrões internacionalmente reconhecidos desenvolvidos pelo W3C para tornar o conteúdo da web mais acessível.

### Como funciona {#how-it-works}

Quando você executa o Inbox Vision, a Braze verifica automaticamente problemas comuns de acessibilidade no [conjunto de regras WCAG 2.2 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa) (como texto alternativo ausente, contraste de cores insuficiente, estrutura de cabeçalhos inadequada) e categoriza a gravidade para ajudar você a priorizar as correções. Observe que, mesmo quando o texto alternativo está presente, [como ele é exibido]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/accessibility#how-email-clients-display-alt-text) é controlado pelo cliente de e-mail do destinatário, não pela Braze.

{% alert important %}
Os Testes de Acessibilidade podem ser usados para apoiar os esforços de conformidade do Cliente com regulamentos ou leis como o [European Accessibility Act](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers); no entanto, o Cliente reconhece que a Braze não faz representações ou garantias sobre se o uso dos Testes de Acessibilidade atende ou não às obrigações de conformidade do Cliente, e se isenta de toda responsabilidade em relação a isso.
{% endalert %}

### Visualizando os resultados dos testes de acessibilidade {#viewing-accessibility-testing-results}

Os testes de acessibilidade geram resultados para cada regra como aprovado, reprovado ou necessita de revisão na guia **Accessibility Testing**. A Braze categoriza cada regra usando POUR (Perceivable, Operable, Understandable, Robust), os quatro princípios que fundamentam o WCAG.

#### Categorias POUR {#pour-categories}

O Inbox Vision categoriza os problemas sob os quatro [princípios fundamentais POUR](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility): Perceptível, Operável, Compreensível e Robusto.

| Princípio | Definição |
| --- | --- |
| Perceptível | As informações e os componentes da interface do usuário devem ser apresentados de maneiras que os usuários possam perceber.<br><br>Os usuários devem ser capazes de perceber as informações apresentadas (elas não podem ser invisíveis para todos os seus sentidos). |
| Operável | Os componentes da interface do usuário e a navegação devem ser operáveis.<br><br>Os usuários devem ser capazes de operar a interface (a interface não pode exigir interações que o usuário não consiga realizar). |
| Compreensível | As informações e a operação da interface do usuário devem ser compreensíveis.<br><br>Os usuários devem ser capazes de entender as informações, bem como a operação da interface (o conteúdo ou a operação não podem estar além da sua compreensão). |
| Robusto | O conteúdo deve ser robusto o suficiente para ser interpretado de forma confiável por uma ampla variedade de agentes de usuário, incluindo tecnologias assistivas.<br><br>Os usuários devem ser capazes de acessar o conteúdo à medida que as tecnologias avançam (conforme as tecnologias e os agentes de usuário evoluem, o conteúdo deve permanecer acessível). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Categorias POUR" }

#### Níveis de gravidade {#severity-levels}

O Inbox Vision classifica os problemas de acessibilidade por gravidade para ajudar você a priorizar a correção.

| Status | Definição |
| --- | --- |
| Crítico | Problemas que podem bloquear o acesso ao conteúdo ou à funcionalidade para usuários com deficiência. São os mais graves e devem ser priorizados para correção. |
| Grave | Problemas que podem causar barreiras significativas, mas podem não bloquear completamente o acesso. Devem ser tratados prontamente. |
| Moderado | Problemas que podem causar alguma dificuldade para usuários com deficiência, mas são menos propensos a bloquear o acesso completamente. |
| Menor | Problemas que têm impacto relativamente baixo na acessibilidade e podem causar apenas inconveniências menores. |
| Necessita de revisão | Não foi possível detectar se há um problema ou não. Isso pode ocorrer quando não é possível determinar a taxa de contraste porque o texto está sobre uma imagem de fundo. Você deve revisar manualmente, pois não pode ser determinado automaticamente. |
| Aprovado | Aprovado nas diretrizes WCAG A, AA ou nas boas práticas de acessibilidade. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Níveis de gravidade" }

{% alert important %}
O editor de arrastar e soltar não suporta a definição de um elemento `<title>` no documento, então o scanner de acessibilidade sempre reprova nessa verificação.<br><br>Essa limitação está sendo acompanhada para melhorias futuras. {% multi_lang_include product_feedback_cta.md context="pain_point" channel="ux" feature="the drag-and-drop editor document title limitation in Inbox Vision" %}
{% endalert %}

### Entendendo os testes automatizados de acessibilidade {#understanding-automated-accessibility-testing}

{% multi_lang_include accessibility/automated_testing.md %}

## Práticas recomendadas {#best-practices}

### Revise sua lista de assinantes de e-mail {#review-your-email-subscriber-list}

Consulte o [dashboard de insights de e-mail]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#email-insights-dashboard) para determinar o tipo de dispositivo e os provedores mais populares onde seus assinantes estão engajando.

Se você precisar de mais granularidade, como navegador, modelo de dispositivo e outros detalhes, pode alavancar seus dados do [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) ou do [Query Builder]({{site.baseurl}}/user_guide/analytics/reports/query_builder) para obter esse nível de detalhamento sobre o engajamento recente de e-mail dos seus usuários.

### Selecione prévias significativas e impactadas {#select-meaningful-previews-and-impacted-previews}

Se o seu negócio é baseado principalmente nos EUA, pode haver prévias específicas, como prévias internacionais como GMX.de, que são usadas apenas por um número mínimo de usuários. Recomendamos priorizar e otimizar para caixas de entrada com um impacto significativo de assinantes e reservar suas prévias para caixas de entrada de maior impacto.

Ao fazer correções que afetam prévias específicas, certifique-se de selecionar apenas as prévias impactadas para evitar o consumo de prévias não utilizadas.

### Execute o Inbox Vision na versão final do e-mail {#run-inbox-vision-on-the-final-email-version}

Sugerimos executar o Inbox Vision quando a mensagem de e-mail estiver pronta para produção ou próxima disso. Isso permite reduzir o número de prévias geradas, já que o e-mail passa por várias iterações antes de ser finalizado e estar pronto para ser enviado aos usuários.

Executar o Inbox Vision toda vez que você fizer uma única edição ou alteração pode consumir prévias rapidamente. Sugerimos fazer todas as alterações necessárias no e-mail primeiro e depois executar o Inbox Vision para visualizar como todas as suas alterações podem afetar a renderização do seu e-mail em diferentes ambientes.

A Braze executa testes por meio de clientes de e-mail reais e trabalha para garantir que as renderizações sejam precisas. A Braze utiliza por padrão as 20 principais prévias com base em dados gerais do setor e de especialistas, o que cobre a maioria dos ambientes onde seus usuários estão engajando com seus e-mails. Se sua análise de dados apontar para outras prévias mais populares, você pode definir um conjunto padrão de prévias toda vez que executar o Inbox Vision.

Se você identificar consistentemente um problema com um cliente, abra um [ticket de suporte]({{site.baseurl}}/user_guide/administer/personal/braze_support).

### Precisão dos testes versus caixas de entrada reais {#test-accuracy-versus-live-inboxes}

Uma mensagem enviada pode parecer diferente da prévia do editor porque os provedores interpretam o mesmo HTML de forma diferente. Baixe uma cópia do HTML enviado para comparar e use CSS inline onde os clientes removem blocos `<style>`.

#### Corpos de e-mail em branco {#blank-email-bodies}

Se os destinatários relatarem corpos de e-mail em branco, mas ainda conseguirem ver o nome do remetente ou a linha de assunto:

1. Confirme quais clientes de e-mail são afetados.
2. Use o Inbox Vision para testar a variante nesses clientes e identificar problemas de compatibilidade de HTML ou CSS.
3. Se um cliente remover blocos `<style>`, adicione atributos `style` aos elementos HTML afetados. Para mais informações sobre o comportamento de inlining e suas limitações, consulte [CSS inline]({{site.baseurl}}/user_guide/channels/email/html_editor/css_inline). No Gmail, excesso de CSS pode fazer com que todo o bloco `<style>` seja descartado, o que é uma causa comum de corpos de e-mail em branco.
4. No editor de HTML, você também pode ativar **Enable inline CSS** em **Sending Info** > **Advanced** para aplicar regras de folha de estilo inline em toda a mensagem. Essa opção não está disponível para e-mails de arrastar e soltar, que já são processados com inline pelo editor.
5. Teste novamente no Inbox Vision antes de enviar futuras campanhas.