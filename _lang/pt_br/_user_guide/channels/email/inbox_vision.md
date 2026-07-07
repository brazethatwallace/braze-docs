---
nav_title: Inbox Vision
article_title: Inbox Vision
page_order: 7
description: "Esta página cobre como configurar o Inbox Vision, um recurso que permite aos profissionais de marketing visualizar seus e-mails a partir da perspectiva de vários clientes de e-mail e dispositivos móveis."
tool:
  - Dashboard
channel:
  - email

---

# Inbox Vision {#inbox-vision}

> Inbox Vision permite que você visualize seus e-mails a partir da perspectiva de vários clientes de e-mail e dispositivos móveis. Por exemplo, você pode testar as diferenças entre o modo escuro e o modo claro para confirmar se seus e-mails são exibidos como pretendido.

{% alert important %}
O Inbox Vision pode não funcionar se o conteúdo do seu e-mail depender de informações de modelagem, como dados de perfil de usuário. A Braze modela um usuário vazio ao enviar e-mails para esse recurso.<br><br>Adicione valores padrão a qualquer Liquid na sua mensagem de e-mail. Sem valores padrão, você pode receber um falso positivo ou o teste pode falhar.
{% endalert %}

## Considerações {#considerations}

De modo geral, seu e-mail não funcionará com o Inbox Vision se o conteúdo depender de informações de modelagem, como dados do perfil de usuário. Isso acontece porque a Braze modela um usuário vazio ao enviar e-mails com esse recurso.

Você pode resolver isso adicionando valores padrão ou quaisquer valores ao Liquid na sua mensagem de e-mail antes de executar o Inbox Vision. Quando você terminar os testes no Inbox Vision, a mensagem de e-mail original será exibida. Se nenhum valor for fornecido, o teste pode falhar ao renderizar as pré-visualizações.

Sua empresa tem um limite de quantos e-mails podem ser pré-visualizados com o Inbox Vision. Você pode monitorar isso na guia **Email Previews** do Inbox Vision.

Inclua uma linha de assunto e um domínio de envio válido para visualizar as pré-visualizações. Fique atento às diferenças de renderização entre desktop e celular. Use as pré-visualizações para confirmar que o e-mail aparece conforme o esperado.

{% alert note %}
Se a pré-visualização de uma Campaign mostrar um erro de permissão, limpe o cache e os cookies ou tente uma janela anônima. Extensões do navegador às vezes bloqueiam a pré-visualização.
{% endalert %}

Para testar sua mensagem de e-mail no Inbox Vision:

1. Acesse o editor de arrastar e soltar ou o editor de e-mail HTML.
2. No editor, selecione **Preview & Test**.
3. Selecione **Inbox Vision**.
4. Selecione **Run Inbox Vision**. Isso leva até dez minutos.
5. Em seguida, selecione um bloco para visualizar a pré-visualização em mais detalhes. Essas pré-visualizações são agrupadas nestas seções: **Web Clients**, **Application Clients** e **Mobile Clients**.

![A opção de selecionar clientes de e-mail para pré-visualização.]({% image_buster /assets/img/select_email_preview_inbox_vision.png %}){: style="max-width:85%;"}

{:start="5"}
5. Selecione **Run Inbox Vision**. Isso pode levar de dois a dez minutos para ser concluído.

{% alert note %}
O Inbox Vision não oferece suporte a mensagens de e-mail que incluem [lógica de cancelamento]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid/aborting_messages) porque esses e-mails são renderizados como conteúdo estático.
{% endalert %}

### Pré-visualizando como um usuário {#previewing-as-a-user}

Quando você pré-visualiza como um usuário aleatório, o Inbox Vision não salva configurações ou atributos específicos do usuário (como nome ou preferências). Quando você seleciona um usuário personalizado, a pré-visualização do Inbox Vision pode diferir de outras pré-visualizações porque usa dados específicos do usuário.

## Análise de código {#code-analysis}

A análise de código destaca possíveis problemas de HTML, mostra o número de ocorrências e indica elementos HTML não suportados.

### Visualizando informações da análise de código {#viewing-code-analysis-information}

Encontre essas informações na guia **Inbox Vision** selecionando <i class="fas fa-list"></i> **List view**. A visualização em lista está disponível apenas para modelos de e-mail HTML. Para modelos de arrastar e soltar, use as pré-visualizações para resolver problemas.

![Exemplo de análise de código na pré-visualização do Inbox Vision.]({% image_buster /assets/img_archive/inboxvision2.png %})

{% alert note %}
A análise de código pode aparecer mais rápido do que a pré-visualização para um cliente específico, pois a Braze aguarda até que o e-mail chegue antes de capturar a tela.
{% endalert %}

## Teste de spam {#spam-testing}

O teste de spam estima se o e-mail pode ser filtrado como spam. Os testes são executados em filtros como IronPort, SpamAssassin e Barracuda, além de filtros de provedores de acesso à internet como Gmail e Outlook, usando caixas de entrada estáticas que não abrem nem clicam por padrão.

{% alert important %}
O posicionamento na caixa de entrada é impulsionado principalmente pelo engajamento real dos destinatários. Os resultados do teste de spam podem não corresponder ao que você observa em Campaigns reais.
{% endalert %}

Para uma leitura mais clara sobre entregabilidade, teste o conteúdo com pequenas coortes reais — aberturas e cliques consistentes são o sinal mais confiável. Use os testes de spam como um dado adicional junto ao monitoramento de engajamento.

### Visualizando resultados do teste de spam {#viewing-spam-test-results}

Para verificar os resultados do teste de spam:

1. Selecione a guia **Spam Testing** na seção **Inbox Vision**. A tabela **Spam Test Result** lista o nome do filtro de spam, o status e o tipo.
2. Revise esses resultados e faça os ajustes necessários na sua Campaign de e-mail.
3. Selecione **Re-run Test** para recarregar os resultados do teste de spam.

## Teste de acessibilidade {#accessibility-testing}

O teste de acessibilidade destaca possíveis problemas de acessibilidade no seu e-mail e mostra quais elementos não atendem aos padrões. A Braze analisa o conteúdo com base em diretrizes selecionadas das Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)), um conjunto de padrões reconhecidos internacionalmente, desenvolvidos pelo W3C para tornar o conteúdo da web mais acessível.

### Como funciona {#how-it-works}

Quando você executa o Inbox Vision, a Braze verifica automaticamente problemas comuns de acessibilidade no [conjunto de regras WCAG 2.2 AA](https://www.w3.org/WAI/WCAG22/quickref/?versions=2.2&currentsidebar=%23col_customize&levels=aaa) (como texto alternativo ausente, contraste de cores insuficiente, estrutura inadequada de cabeçalhos) e categoriza a severidade para ajudar você a priorizar as correções.

{% alert important %}
O teste de acessibilidade pode ser usado para apoiar os esforços de conformidade do cliente com regulamentações ou leis como o [European Accessibility Act](https://www.braze.com/resources/articles/european-accessibility-at-what-it-means-for-marketers). No entanto, o cliente reconhece que a Braze não faz representações ou garantias sobre se o uso do teste de acessibilidade satisfaz as obrigações de conformidade do cliente, e se isenta de toda responsabilidade a esse respeito.
{% endalert %}

### Visualizando resultados do teste de acessibilidade {#viewing-accessibility-testing-results}

O teste de acessibilidade gera resultados para cada regra como aprovado, reprovado ou necessita revisão na guia **Accessibility Testing**. A Braze categoriza cada regra usando POUR (Perceptível, Operável, Compreensível, Robusto), os quatro princípios por trás do WCAG.

#### Categorias POUR {#pour-categories}

O Inbox Vision categoriza os problemas sob os quatro [princípios fundamentais POUR](https://www.w3.org/WAI/WCAG22/Understanding/intro#understanding-the-four-principles-of-accessibility): Perceptível, Operável, Compreensível e Robusto.

| Princípio | Definição |
| --- | --- |
| Perceptível | As informações e os componentes da interface do usuário devem ser apresentados de formas que os usuários possam perceber.<br><br>Os usuários devem ser capazes de perceber as informações apresentadas (elas não podem ser invisíveis a todos os seus sentidos). |
| Operável | Os componentes da interface do usuário e a navegação devem ser operáveis.<br><br>Os usuários devem ser capazes de operar a interface (a interface não pode exigir interações que o usuário não consiga realizar). |
| Compreensível | As informações e a operação da interface do usuário devem ser compreensíveis.<br><br>Os usuários devem ser capazes de entender as informações e a operação da interface (o conteúdo ou a operação não podem estar além da sua compreensão). |
| Robusto | O conteúdo deve ser robusto o suficiente para ser interpretado de forma confiável por uma ampla variedade de agentes de usuário, incluindo tecnologias assistivas.<br><br>Os usuários devem ser capazes de acessar o conteúdo à medida que as tecnologias avançam (conforme as tecnologias e os agentes de usuário evoluem, o conteúdo deve permanecer acessível). |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Categorias POUR" }

#### Níveis de severidade {#severity-levels}

O Inbox Vision classifica os problemas de acessibilidade por severidade para ajudar você a priorizar as correções.

| Status | Definição |
| --- | --- |
| Crítico | Problemas que podem bloquear o acesso ao conteúdo ou à funcionalidade para usuários com deficiência. São os mais graves e devem ser priorizados para correção. |
| Grave | Problemas que podem causar barreiras significativas, mas podem não bloquear completamente o acesso. Devem ser resolvidos prontamente. |
| Moderado | Problemas que podem causar alguma dificuldade para usuários com deficiência, mas são menos propensos a bloquear o acesso completamente. |
| Menor | Problemas que têm um impacto relativamente baixo na acessibilidade e podem causar apenas pequenos inconvenientes. |
| Necessita revisão | Não foi possível detectar se há um problema ou não. Isso pode ocorrer quando não é possível determinar a taxa de contraste porque o texto está sobre uma imagem de fundo. Você deve revisar manualmente, pois não pode ser determinado automaticamente. |
| Aprovado | Aprovado nas regras WCAG A, AA ou nas melhores práticas de acessibilidade. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Níveis de severidade" }

{% alert important %}
O editor de arrastar e soltar não oferece suporte à definição de um elemento `<title>` no documento, então o scanner de acessibilidade sempre reprova nessa verificação.<br><br>Essa limitação está sendo acompanhada para melhorias futuras. Se isso afetar seus fluxos de trabalho ou seus usuários, [compartilhe seu feedback]({{site.baseurl}}/user_guide/administer/personal/the_braze_dashboard#sharing-feedback) para que possamos priorizar correções de maior impacto.
{% endalert %}

### Entendendo o teste automatizado de acessibilidade {#understanding-automated-accessibility-testing}

{% multi_lang_include accessibility/automated_testing.md %}

## Melhores práticas {#best-practices}

### Revise sua lista de assinantes de e-mail {#review-your-email-subscriber-list}

Consulte o [dashboard de insights de e-mail]({{site.baseurl}}/user_guide/analytics/dashboards/channel_performance#email-insights-dashboard) para determinar o tipo de dispositivo e os provedores mais populares entre seus assinantes. Se você precisar de mais granularidade, como navegador, modelo do dispositivo e mais, pode usar seus dados do [Currents]({{site.baseurl}}/user_guide/data/distribution/braze_currents) ou do [Criador de consultas]({{site.baseurl}}/user_guide/analytics/reports/query_builder) para obter esse nível de detalhe sobre o engajamento recente de e-mail dos seus usuários.

Caso contrário, a Braze usa como padrão as 20 principais pré-visualizações com base em dados gerais do setor e de especialistas, o que cobre a maioria dos ambientes onde seus assinantes estão engajando com seus e-mails. Se sua análise de dados apontar para outras pré-visualizações mais populares, você pode definir um conjunto padrão de pré-visualizações toda vez que executar o Inbox Vision.

### Selecione pré-visualizações significativas e impactadas {#select-meaningful-previews-and-impacted-previews}

Se o seu negócio é baseado principalmente nos EUA, pode haver pré-visualizações específicas, como pré-visualizações internacionais como GMX.de, que são usadas apenas por um número nominal de usuários. Recomendamos priorizar e otimizar para caixas de entrada com impacto significativo nos assinantes e reservar suas pré-visualizações para caixas de entrada de maior impacto.

Ao fazer correções que afetam pré-visualizações específicas, selecione apenas as pré-visualizações impactadas para evitar consumir pré-visualizações não utilizadas.

### Execute o Inbox Vision na versão final do e-mail {#run-inbox-vision-on-the-final-email-version}

Sugerimos executar o Inbox Vision quando a mensagem de e-mail estiver pronta para produção ou próxima disso. Isso permite reduzir o número de pré-visualizações geradas, já que o e-mail passa por várias iterações antes de ser finalizado e estar pronto para ser enviado aos usuários.

Executar o Inbox Vision toda vez que você faz uma única edição ou alteração pode consumir pré-visualizações rapidamente. Sugerimos fazer todas as alterações necessárias no e-mail primeiro e depois executar o Inbox Vision para verificar como todas as suas alterações podem afetar a renderização do e-mail em diferentes ambientes.

A Braze executa testes por meio de clientes de e-mail reais e trabalha para garantir que as renderizações sejam precisas. Se você observar um problema consistente com um cliente, abra um [ticket de suporte]({{site.baseurl}}/braze_support).

### Precisão do teste versus caixas de entrada reais {#test-accuracy-versus-live-inboxes}

Uma mensagem enviada pode parecer diferente da pré-visualização do editor porque os provedores interpretam o mesmo HTML de formas diferentes. Baixe uma cópia do HTML enviado para comparar e use CSS inline nos casos em que os clientes removem blocos `<style>`.