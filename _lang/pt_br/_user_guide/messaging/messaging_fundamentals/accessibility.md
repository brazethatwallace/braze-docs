---
nav_title: Acessibilidade
article_title: Crie mensagens acessíveis na Braze
page_order: 0.5
page_type: reference
description: "Este artigo de referência explica por que a acessibilidade é importante no conteúdo de marketing, como o idioma de acessibilidade (HTML lang) da Braze funciona nos diferentes canais e como você pode criar mensagens acessíveis na Braze."
---

# Crie mensagens acessíveis na Braze {#build-accessible-messages-in-braze}

> Entenda por que a acessibilidade é importante no seu conteúdo de marketing e como você pode criar mensagens acessíveis na Braze. Para mais orientações, confira nosso curso [Fundamentos de Mensagens Acessíveis](https://learning.braze.com/accessible-messaging-foundations) no Braze Learning.

Conteúdo de marketing que exclui pessoas com deficiência, mesmo sem intenção, pode impedir milhões de pessoas de interagir com a sua marca. Acessibilidade no marketing é sobre permitir que todos experimentem seu marketing, entendam sua comunicação e tenham a oportunidade de investir ou se tornar fã do seu produto, serviço ou marca.

Ao projetar suas mensagens, dedique um tempo extra para considerar como tornar seus designs acessíveis a todos os seus clientes.

{% alert important %}
Este conteúdo é destinado a orientações gerais e não garante conformidade com padrões de acessibilidade como WCAG. A Braze oferece ferramentas que apoiam a criação de mensagens mais acessíveis, mas é sua responsabilidade garantir que seu conteúdo final atenda a quaisquer requisitos aplicáveis. Acessibilidade é um tema complexo com muitas partes envolvidas. Muitas empresas trabalham com especialistas ou consultores de acessibilidade para garantir que suas práticas de conteúdo, design e desenvolvimento atendam às necessidades de todos os usuários.
{% endalert %}

## Acessibilidade na Braze {#accessibility-at-braze}

Apoiar a comunicação acessível significa manter-se aberto, curioso e disposto a aprender. Na Braze, nos importamos em ajudar as pessoas a se conectarem — e sabemos que abrir espaço para todos faz parte disso. Acessibilidade não é algo que consideramos "concluído", e agradecemos a oportunidade de continuar aprendendo.

{% multi_lang_include accessibility/feedback.md %}

## Áreas de deficiência a considerar {#areas-of-disability-to-consider}

*Esta seção é parcialmente adaptada de [W3C: Diverse Abilities and Barriers](https://www.w3.org/WAI/people-use-web/abilities-barriers/).*

{% tabs local %}
{% tab Visual %}

Deficiências visuais podem variar de perda leve ou moderada de visão em um ou ambos os olhos, até perda substancial ou completa de visão em ambos os olhos. Algumas pessoas têm sensibilidade reduzida ou ausente a certas cores, ou sensibilidade aumentada a cores brilhantes.

Para interagir com seu conteúdo, esses usuários precisam da capacidade de:

- Aumentar ou reduzir o tamanho do texto e das imagens
- Personalizar configurações de fontes, cores e espaçamento
- Ouvir a síntese de texto para fala do conteúdo (ou seja, usar um leitor de tela)
- Ouvir audiodescrições de vídeos
- Ler texto usando Braille atualizável

{% alert note %}
- Globalmente, pelo menos 2,2 bilhões de pessoas têm deficiência visual de perto ou de longe (veja [OMS](https://www.who.int/news-room/fact-sheets/detail/blindness-and-visual-impairment))
- Cerca de 1 em cada 12 homens e 1 em cada 200 mulheres têm algum grau de deficiência na visão de cores, estimando-se 300 milhões de pessoas no mundo (veja [NHS](https://www.nhs.uk/conditions/colour-vision-deficiency/))
{% endalert %}

{% endtab %}
{% tab Auditiva %}

Deficiências auditivas podem incluir perda auditiva leve a moderada em um ou ambos os ouvidos. Mesmo a perda parcial de audição pode ser problemática em relação a conteúdo de áudio.

Para entender seu conteúdo, esses usuários dependem de:

- Transcrições e legendas de conteúdo de áudio
- Players de mídia que exibem legendas e oferecem opções para ajustar o tamanho e as cores do texto das legendas
- Opções para parar, pausar e ajustar o volume do conteúdo de áudio (independente do volume do sistema)
- Áudio em primeiro plano de alta qualidade que seja claramente distinguível de qualquer ruído de fundo

{% alert note %}
- Uma em cada oito pessoas nos Estados Unidos (13%, ou 30 milhões) com 12 anos ou mais tem perda auditiva em ambos os ouvidos, com base em exames auditivos padrão
- Aproximadamente 15% dos adultos americanos (37,5 milhões) com 18 anos ou mais relatam alguma dificuldade auditiva (veja [NIH](https://www.nidcd.nih.gov/health/statistics/quick-statistics-hearing))
{% endalert %}

{% endtab %}
{% tab Física %}

Deficiências físicas podem incluir fraqueza e limitações de controle muscular ou sensação, distúrbios articulares, dor que impede o movimento e membros ausentes.

Esses usuários dependem do suporte a teclado para ativar funcionalidades (mesmo que não estejam usando um teclado padrão). Para interagir com seu conteúdo, esses usuários precisam de:

- Áreas clicáveis grandes
- Tempo suficiente para concluir tarefas
- Indicadores visíveis do foco atual
- Mecanismos para pular blocos de conteúdo, como cabeçalhos de página ou barras de navegação

{% alert note %}
Quase 2 milhões de pessoas nos EUA vivem com perda de membros (veja [Amputee Coalition](https://www.amputee-coalition.org/limb-loss-resource-center/resources-filtered/resources-by-topic/limb-loss-statistics/limb-loss-statistics/#1))
{% endalert %}

{% endtab %}
{% tab Cognitiva %}

Deficiências cognitivas, de aprendizagem e neurológicas envolvem neurodiversidade e distúrbios neurológicos, bem como distúrbios comportamentais e de saúde mental que não são necessariamente neurológicos. Elas podem afetar qualquer parte do sistema nervoso e impactar a capacidade das pessoas de ouvir, se mover, ver, falar e entender informações.

Dependendo das necessidades individuais, esses usuários dependem de:

- Conteúdo claramente estruturado
- Rotulagem consistente de formulários, botões e outros conteúdos
- Destinos de links previsíveis e interação geral
- Diferentes formas de navegação, como menus e barras de pesquisa
- Configurações para desativar conteúdo piscante, intermitente ou que cause distração
- Texto mais simples apoiado por imagens


{% alert note %}
- Uma em cada cinco pessoas nos Estados Unidos tem problemas de aprendizagem e atenção (veja [LDA](https://ldaamerica.org/lda_today/the-state-of-learning-disabilities-today/#:~:text=LD%20Today,have%20learning%20and%20attention%20issues.))
- Aproximadamente 10-20% da população global é considerada neurodivergente (veja [Deloitte](https://www2.deloitte.com/us/en/insights/topics/talent/neurodiversity-in-the-workplace.html))
- Cerca de 1 em cada 100 crianças tem autismo no mundo (veja [OMS](https://www.who.int/news-room/fact-sheets/detail/autism-spectrum-disorders))
{% endalert %}

{% endtab %}
{% endtabs %}

## Boas práticas {#best-practices}

Criar conteúdo acessível não precisa ser algo complicado. Pequenas escolhas cuidadosas podem fazer uma grande diferença. Esta seção apresenta dicas práticas que ajudam mais pessoas a ler, navegar e interagir com suas mensagens com sucesso. Seja ajustando seu texto, estilizando seus botões ou adicionando texto alternativo às imagens, cada melhoria contribui para uma experiência mais inclusiva. Vamos lá.

### Conteúdo {#content}

#### Estrutura e fluxo {#structure-and-flow}

Vamos começar pela base. Quando seu conteúdo tem uma estrutura clara, é mais fácil para todos acompanharem — especialmente pessoas que dependem de leitores de tela ou navegação por teclado.

- **Divida seu conteúdo em seções:** Usar títulos, marcadores e listas ajuda as pessoas a entender e escanear rapidamente seu conteúdo — mesmo quando estão com pressa.
- **Não pule níveis de título:** Os títulos dão estrutura ao seu conteúdo, ajudando os leitores a entender rapidamente como as seções se relacionam entre si. Quando você pula níveis de título (por exemplo, indo direto de um H2 para um H4), você quebra essa estrutura lógica. Isso dificulta a navegação e compreensão da sua mensagem para os usuários, especialmente aqueles que usam leitores de tela. Sempre siga uma hierarquia lógica e sequencial de títulos (H1 para H2 para H3, e assim por diante) para garantir que seu conteúdo permaneça organizado, acessível e fácil de acompanhar para todos.

#### Legibilidade {#readability}

Com a estrutura definida, o próximo passo é garantir que suas palavras sejam realmente fáceis de ler. Isso significa manter as coisas simples, escaneáveis e confortáveis de ler em diferentes dispositivos e necessidades dos usuários.

- **Escreva frases curtas e claras:** Frases curtas são fáceis de entender para todos, especialmente pessoas que usam leitores de tela ou que têm dificuldade em processar informações complexas. Escreva para um nível de leitura equivalente ao sétimo ano nos Estados Unidos. Você pode usar recursos como o [Hemingway App](https://hemingwayapp.com/) para verificar o nível de leitura do seu texto.
- **Escolha tamanhos de fonte e espaçamento legíveis:** Texto muito pequeno pode ser difícil de ler — especialmente em dispositivos móveis. Use pelo menos 14px para o texto do corpo. Faça os títulos maiores para que os usuários possam ver claramente a diferença. Espaçamento extra entre linhas (cerca de 1,5 de altura de linha) e parágrafos melhora a legibilidade, especialmente para pessoas com necessidades visuais ou cognitivas.
- **Evite texto justificado:** Texto justificado cria espaçamento irregular entre palavras, dificultando a leitura para pessoas com dislexia ou deficiências cognitivas. Considere alinhar à esquerda o conteúdo que ocupa mais de duas linhas para idiomas da esquerda para a direita, ou alinhar à direita para [idiomas da direita para a esquerda]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/right_to_left_messages).
- **Use negrito, itálico e texto em maiúsculas com moderação:** Enfatizar muito texto dificulta a leitura — especialmente para pessoas com dislexia ou deficiências visuais. Mantenha a simplicidade.

#### Clareza e usabilidade {#clarity-and-usability}

Por fim, vamos falar sobre os detalhes mais finos — as coisas que ajudam os usuários não apenas a ver seu conteúdo, mas a entendê-lo e interagir com ele.

- **Rotule links e botões claramente:** Certifique-se de que o texto dos seus [links](#links) e [botões](#buttons) explique claramente o que acontece em seguida. Isso ajuda pessoas que usam leitores de tela ou navegam com teclado a saber o que esperar.
- **Pegue leve com símbolos e emojis:** Caracteres especiais e emojis podem tornar seu conteúdo divertido, mas podem ser confusos quando lidos por leitores de tela. Use-os com moderação e certifique-se de que não substituam texto claro e descritivo.
- **Teste se há truncamento:** Sempre teste seu texto [enviando uma mensagem de teste]({{site.baseurl}}/developer_guide/in_app_messages/sending_test_messages) para um dispositivo para garantir que seu texto não seja truncado. Se sua mensagem estiver sendo cortada, isso prejudica tanto você quanto seu público, pois impede que seu conteúdo chegue até eles.

### Idioma de acessibilidade {#accessibility-language}

O **idioma de acessibilidade** informa aos leitores de tela e outras ferramentas assistivas em qual idioma seu conteúdo está. Para canais que enviam uma página HTML completa ou e-mail, a Braze pode adicionar uma tag de idioma (`lang`) quando você a define no editor ou via Liquid. Isso atende ao [Critério de Sucesso 3.1.1 do WCAG 2.1 — Idioma da Página (Nível A)](https://www.w3.org/WAI/WCAG21/Understanding/language-of-page.html).

Se você deixar o idioma de acessibilidade em branco e não houver um padrão seguro disponível, a Braze omite a tag de idioma. Se nenhum idioma for definido, as ferramentas assistivas geralmente recorrem ao idioma do telefone ou computador da pessoa. Se esse idioma for diferente do idioma da mensagem, a pronúncia pode soar incorreta.

Campaigns e Canvas usam os mesmos editores para essas opções, a menos que um recurso não esteja disponível para o seu espaço de trabalho.

#### Configurar o idioma de acessibilidade {#configure-accessibility-language}

Quando seu editor inclui essa opção, vá até a seção **Acessibilidade** nas configurações da mensagem. Escolha um idioma no menu suspenso ou use Liquid (por exemplo, {% raw %}`{{accessibility_language}}`{% endraw %} quando [mensagens multilíngues]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages) estiverem ativadas e as **Configurações de localização** estiverem definidas).

#### Mensagens multilíngues {#multi-language-messages}

Em **Configurações de localização**, defina um idioma de acessibilidade para cada localidade para que o Liquid possa preencher {% raw %}`{{accessibility_language}}`{% endraw %} para envios localizados. Se esse valor já está escolhido para novas mensagens depende do canal. Para fluxos de trabalho com CSV e tradução, comece com [Configurações de idioma e acessibilidade]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/localization/locales_in_messages#language-settings-and-accessibility).

#### Suporte por canal e editor {#channel-and-editor-support}

Use esta tabela para comparar os canais. Os padrões podem variar, então verifique o que seu público realmente recebe.

| Canal | O que saber |
| --- | --- |
| E-mail (arrastar e soltar, modelo completo) | Defina o idioma no editor. Com mensagens multilíngues, um modelo de e-mail completo pode corresponder ao idioma de cada localidade automaticamente. Se você usa apenas Content Blocks (linha única), esses atalhos não funcionam da mesma forma — escolha o idioma você mesmo onde o editor permitir. |
| E-mail (código HTML) | A Braze não adiciona uma tag de idioma para você. Adicione-a no seu HTML se precisar. |
| Mensagens no app (arrastar e soltar) | Quando você escolhe um idioma em **Acessibilidade**, a Braze adiciona esse idioma ao HTML externo da mensagem para que os leitores de tela tratem toda a mensagem nesse idioma. Com mensagens multilíngues ativadas, novas mensagens podem usar como padrão os idiomas das suas localidades. A **pré-visualização** pode não mostrar nenhum idioma até que você escolha um em **Configurações**. |
| Banners | Mesmo comportamento das mensagens no app. |
| Landing pages | Você pode definir o idioma na página publicada. Escolha um idioma ou use Liquid se sua conta permitir Liquid em landing pages. Os padrões também diferem das mensagens no app e Banners — verifique a página publicada. |
| Content Cards | Os cartões usam um campo **Idioma** para apps em vez de um idioma de acessibilidade explícito. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Suporte por canal e editor" }

Quando você escreve HTML por conta própria, ainda pode adicionar uma tag de idioma em parte da mensagem (por exemplo, uma frase em outro idioma). Para mais padrões, veja [HTML personalizado](#custom-html).

#### Referência de padrões {#standards-reference}

Quando a Braze adiciona uma tag de idioma no nível raiz ao HTML, ela segue a regra do atributo HTML [`lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang). Ferramentas de teste geralmente procuram por [`html-has-lang`](https://dequeuniversity.com/rules/axe/4.2/html-has-lang). Content Cards usam o campo **idioma** em vez desse padrão HTML.

### Botões {#buttons}

Use **botões** para indicar uma ação, como enviar um formulário ou reproduzir um carrossel. Se você está navegando para uma nova URL, considere usar um [link](#links).

#### Escreva texto claro e orientado à ação {#write-clear-action-oriented-text}

Assim como o texto de links, os rótulos dos botões devem descrever claramente a ação. Texto de botão eficaz é específico e orientado à ação. Por exemplo, "Enviar pedido" diz claramente aos usuários o que acontecerá quando clicarem, enquanto simplesmente "Enviar" pode ser ambíguo. Cada rótulo deve descrever precisamente a ação pretendida, para que leitores de tela e todos os usuários possam entender e prever facilmente o resultado ao interagir com seus botões.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bom texto de botão <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Texto de botão ruim <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Enviar pedido"</td>
      <td>"Enviar"</td>
    </tr>
    <tr>
      <td>"Criar conta"</td>
      <td>"Cadastrar"</td>
    </tr>
    <tr>
      <td>"Baixar nosso folheto"</td>
      <td>"Baixar"</td>
    </tr>
    <tr>
      <td>"Ver detalhes do produto"</td>
      <td>"Saiba mais"</td>
    </tr>
    <tr>
      <td>"Assinar para receber atualizações"</td>
      <td>"Assinar"</td>
    </tr>
  </tbody>
</table>

Mantenha o texto do botão conciso para evitar truncamento. Se o texto de um botão for muito longo, ele pode ser cortado com reticências em vez de quebrar a linha.

#### Use contraste de cores suficiente {#use-sufficient-color-contrast}

O texto do botão deve ser fácil de ler contra a cor de fundo do botão. Verifique se o texto do seu botão atende aos [mínimos de contraste](https://www.w3.org/WAI/WCAG22/Understanding/contrast-minimum.html) WCAG 2.2 AA:

- Proporção de contraste de 4.5:1 para texto de tamanho normal (a maioria dos botões)
- Proporção de contraste de 3:1 para texto grande (geralmente acima de 18pt)

Alto contraste ajuda os botões a permanecerem legíveis e clicáveis para todos, incluindo usuários com deficiências visuais ou aqueles que visualizam sua mensagem em ambientes desafiadores. Para mais orientações, veja a seção [Contraste de cores](#color-contrast).

#### Facilite o toque nos botões {#make-buttons-easy-to-tap}

Certifique-se de que seus botões (e links) sejam grandes o suficiente e espaçados o bastante para usuários em dispositivos móveis. [Alvos de toque](#touch-targets) pequenos ou aglomerados podem ser frustrantes ou impossíveis de interagir para usuários com deficiências motoras.

### Links {#links}

Use links para navegação, como direcionar usuários para uma página externa.

#### Escreva texto de link descritivo {#write-descriptive-link-text}

Escreva texto de link que descreva claramente para onde o link levará o usuário. Usuários de leitores de tela frequentemente pulam de link em link como forma de escanear o conteúdo, então certifique-se de que o texto do link faça sentido por si só. Evite frases como "clique aqui", "mais" e "clique para detalhes", pois são ambíguas quando lidas fora de contexto.

Por exemplo, considere como você escreveria um link para ver um relatório meteorológico.

| Ruim | Melhor | Ideal |
| --- | --- | --- |
| Clique aqui | Clique aqui para acessar o clima de hoje | Clima de hoje |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Escreva texto de link descritivo" }

Como em todo conteúdo, mantenha a objetividade com o mínimo de palavras extras possível.

#### Evite estilizar links como botões {#avoid-styling-links-like-buttons}

Os editores de arrastar e soltar da Braze geram HTML semântico por padrão, então os links não são estilizados como botões neles. No entanto, se você estiver trabalhando com [HTML personalizado](#custom-html) ou fazendo alterações no nível do código, tenha isso em mente:

- **Links (`<a>`)** respondem à tecla <kbd>Enter</kbd>.
- **Botões (`<button>`)** respondem às teclas <kbd>Enter</kbd> e <kbd>Space</kbd>.

Estilizar um link para parecer um botão pode confundir pessoas que navegam com teclado — elas podem tentar pressionar <kbd>Space</kbd> e esperar que funcione.

Use o elemento correto para a ação:

- Use `<button>` para ações, como enviar um formulário ou abrir um modal.
- Use `<a>` para navegação, como vincular a outra página ou arquivo.

{% raw %}

```html
<!-- Recommended: A true button for an action -->
<button type="button">Download report</button>

<!-- Not recommended: A link styled as a button -->
<a href="#" class="btn">Download report</a>
```

{% endraw %}

### Alvos de toque {#touch-targets}

Alvos de toque são qualquer parte da sua mensagem que os usuários tocam para realizar uma ação, como botões, links ou ícones. Esses elementos precisam ser grandes o suficiente e espaçados o bastante para que as pessoas possam tocá-los facilmente, especialmente em dispositivos móveis.

Quando os alvos de toque são muito pequenos ou muito próximos, pode ser frustrante ou impossível para usuários com desafios de mobilidade ou destreza interagir com sua mensagem. Melhorar isso pode ajudar a reduzir erros e criar uma experiência mais fluida para todos.

Veja o que ter em mente:
- **Use tamanho adequado para alvos de toque.** Mire em um tamanho mínimo de alvo de toque de 44 x 44 pixels. Isso está alinhado com as diretrizes WCAG 2.2 para [alvos de toque](https://www.w3.org/WAI/WCAG22/Understanding/target-size-minimum.html) e padrões comuns de usabilidade móvel.
- **Dê espaço para cada alvo.** Se os alvos de toque estiverem muito próximos — como links empilhados ou botões agrupados — pode ser fácil errar ou tocar no errado. Adicione espaçamento ou preenchimento entre os elementos para evitar isso.
- **Não dependa apenas de elementos visuais.** Mesmo ícones pequenos podem se tornar mais usáveis com preenchimento extra, permitindo que atendam aos requisitos mínimos de tamanho sem alterar o layout.
- **Visualize no celular.** Teste sua mensagem em diferentes tamanhos de tela e certifique-se de que os elementos interativos sejam fáceis de usar.

Melhorar os alvos de toque é uma das formas mais eficazes de tornar sua mensagem mais acessível em dispositivos móveis — e é uma boa experiência de usuário para todos.

### Imagens {#images}

#### Forneça texto alternativo {#provide-alt-text}

Texto alternativo (alt text) é uma descrição curta do conteúdo ou função de uma imagem que leitores de tela e outras tecnologias assistivas fornecem aos usuários. Para cada imagem significativa, escreva texto alternativo descritivo para que os usuários que não podem ver os elementos visuais ainda entendam sua mensagem ou chamada para ação.

#### Evite imagens de texto {#avoid-images-of-text}

Sempre que possível, evite colocar texto dentro de imagens — leitores de tela não conseguem ler texto baseado em imagem, e os usuários não podem ajustar facilmente o tamanho da fonte ou a cor para melhor visibilidade. Considere estas dicas:

- **Remova texto quando possível:** Mova qualquer texto descritivo ou promocional da imagem para um campo de texto na sua mensagem. Dessa forma, os usuários podem redimensionar ou recolorir conforme necessário usando as preferências do dispositivo ou navegador.
- **Teste legibilidade e contraste:** Se você precisar manter texto na imagem, siga as boas práticas de [contraste de cores](#color-contrast) e use uma [fonte em escala grande](https://www.w3.org/WAI/WCAG21/Understanding/contrast-minimum.html#dfn-large-scale). Isso significa que o texto deve ter pelo menos 18 pontos (cerca de 24 pixels) para texto sem negrito ou 14 pontos (cerca de 18 pixels) se estiver em negrito. Usar esses tamanhos ajuda o texto a permanecer legível sem forçar os usuários a dar zoom, e melhora o contraste geral e a legibilidade do conteúdo. Teste para confirmar que ainda é legível em telas menores.
- **Forneça texto alternativo:** Para texto essencial que deve permanecer na imagem, inclua texto alternativo descrevendo as palavras.

Quando imagens contêm texto que não pode ser editado, usuários com deficiências visuais perdem a flexibilidade de fazer ajustes de leitura. Ao separar texto de imagens, você ajuda mais usuários a ler e interagir com sua mensagem confortavelmente.

#### Dicas para escrever texto alternativo {#tips-for-writing-alt-text}

- [Descreva o que realmente está na imagem](#tip-1)
- [Mantenha curto, mas específico](#tip-2)
- [Evite "imagem de" ou "foto de"](#tip-3)
- [Reflita o texto que aparece na imagem](#tip-4)
- [Atenha-se ao contexto relevante — sem jargão de marketing extra](#tip-5)
- [Considere o propósito da imagem](#tip-6)

##### Descreva o que realmente está na imagem {#tip-1}

Usuários de leitores de tela dependem do texto alternativo para entender o conteúdo ou função de uma imagem. Evite "linguagem de marketing" genérica que não corresponde ao que é mostrado visualmente.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Exemplos ruins <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Mulher sorridente usando jaqueta jeans azul, segurando uma sacola de compras."</td>
      <td>"Hora de se presentear!" (Sem menção ao que realmente está na imagem)</td>
    </tr>
    <tr>
      <td>"Homem usando camiseta preta, apoiado em uma bicicleta em uma rua da cidade."</td>
      <td>"Abrace sua melhor vida agora!" (Ignora a bicicleta e o cenário urbano)</td>
    </tr>
    <tr>
      <td>"Prédio de apartamentos azul com uma placa 'Aluga-se' na frente."</td>
      <td>"A chave para um amanhã melhor!" (Não reflete o apartamento ou a placa)</td>
    </tr>
  </tbody>
</table>

##### Mantenha curto, mas específico {#tip-2}

Texto alternativo conciso facilita o processamento pelos usuários. Inclua detalhes suficientes para transmitir o propósito, mas pule qualquer excesso. Como regra geral, mantenha o texto alternativo em 125 caracteres ou menos. Se algo mais do que uma frase breve for necessário, considere usar um dos [métodos de descrição longa](https://www.w3.org/WAI/tutorials/images/complex/) do W3C.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Bons exemplos <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Exemplos ruins <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Tênis de corrida vermelhos em fundo branco"</td>
      <td>"Tênis de corrida extremamente confortáveis e perfeitos para seu estilo de vida ativo em um vibrante tom de vermelho." (Muito longo e cheio de linguagem promocional)</td>
    </tr>
    <tr>
      <td>"Quatro laptops em um suporte de exposição"</td>
      <td>"Descubra o impulsionador de produtividade definitivo que redefine como você trabalha todos os dias, de todas as formas imagináveis." (Não descreve o que é realmente mostrado)</td>
    </tr>
    <tr>
      <td>"Grupo de amigos tomando sorvete em um dia ensolarado"</td>
      <td>"Capture a felicidade pura com o doce mais gostoso — a vida é melhor com nosso sorvete!" (Muito abstrato e focado na marca)</td>
    </tr>
  </tbody>
</table>

##### Evite "imagem de" ou "foto de" {#tip-3}

Leitores de tela já anunciam que é uma imagem. Vá direto à descrição do assunto.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Exemplos ruins <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Mesa posta para brunch com panquecas, frutas e café."</td>
      <td>"Imagem de uma mesa posta para brunch"</td>
    </tr>
    <tr>
      <td>"Outdoor na beira da estrada com texto em negrito 'Grande Inauguração'"</td>
      <td>"Foto de um outdoor na beira da estrada"</td>
    </tr>
    <tr>
      <td>"Paisagem de montanha nevada ao pôr do sol"</td>
      <td>"Foto de neve e montanhas"</td>
    </tr>
  </tbody>
</table>

##### Reflita o texto que aparece na imagem {#tip-4}

Se uma imagem inclui texto essencial, coloque essa informação no texto alternativo para que os usuários não percam.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">
        Bons exemplos <span aria-hidden="true">✅</span>
      </th>
      <th style="width: 50%">
        Exemplos ruins <span aria-hidden="true">🚫</span>
      </th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Banner com o texto 'Liquidação de Verão — 50% de desconto em todos os trajes de banho.'"</td>
      <td>"Banner promovendo uma liquidação." (Não menciona o desconto real)</td>
    </tr>
    <tr>
      <td>"Logo com o texto 'Café Toscana' em fonte cursiva"</td>
      <td>"Imagem de logo de um café." (Não inclui o texto 'Café Toscana')</td>
    </tr>
    <tr>
      <td>"Anúncio informando 'Ingressos para o Show Disponíveis Agora — Começa em 5 de Junho'"</td>
      <td>"Anúncio de show." (Sem detalhes do evento)</td>
    </tr>
  </tbody>
</table>

##### Atenha-se ao contexto relevante — sem jargão de marketing extra {#tip-5}

Não preencha o texto alternativo com termos de SEO ou chamadas para ação que não estejam diretamente relacionadas à imagem. Forneça valor para quem não pode ver a imagem.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Bons exemplos <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Exemplos ruins <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Laptop mostrando o gráfico de análise de dados do dashboard da Braze"</td>
      <td>"Aumente conversões e dispare o ROI com a melhor plataforma do mundo!" (Adiciona linguagem de marketing desnecessária)</td>
    </tr>
    <tr>
      <td>"Conjunto de pátio com quatro cadeiras e uma mesa de vidro"</td>
      <td>"Organize uma festa de verão incrível para todos os seus amigos e família agora!" (Descreve um cenário, não a imagem)</td>
    </tr>
    <tr>
      <td>"Celular exibindo um app de previsão do tempo com 75°F na tela"</td>
      <td>"Experimente inovações em tempo real no rastreamento do clima que são revolucionárias" (Não reflete o que é visualmente mostrado)</td>
    </tr>
  </tbody>
</table>

##### Considere o propósito da imagem {#tip-6}

Se uma imagem funciona como um link ou chamada para ação, descreva a ação pretendida ("Comprar", "Link para", "Cadastrar"), não apenas o rótulo ou produto mostrado.

<table role="presentation" class="reset-td-br-1 reset-td-br-2">
  <thead>
    <tr>
      <th style="width: 50%">Bons exemplos <span aria-hidden="true">✅</span></th>
      <th style="width: 50%">Exemplos ruins <span aria-hidden="true">🚫</span></th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td>"Comprar a Coleção de Outono"</td>
      <td>"Coleção de Outono" (Falta a ação pretendida)</td>
    </tr>
    <tr>
      <td>"Link para e-book gratuito"</td>
      <td>"E-book gratuito" (Não deixa claro que é um link)</td>
    </tr>
    <tr>
      <td>"Cadastrar na lista de e-mails"</td>
      <td>"Lista de e-mails" (Não descreve o que o usuário pode fazer)</td>
    </tr>
  </tbody>
</table>

Se a imagem não tem um propósito, deixe isso claro também. Imagens decorativas, como logos, devem ter uma tag alt vazia (`alt=""`) para que os leitores de tela saibam que devem ignorá-la. Sem isso, geralmente o nome do arquivo da imagem é lido.

### Vídeos {#videos}

Vídeos são envolventes, mas se não forem acessíveis, você corre o risco de excluir parte do seu público. Use as dicas a seguir para tornar seu conteúdo de vídeo mais inclusivo:

- [Forneça legendas ocultas](#closed-captions)
- [Forneça controles de reprodução](#playback-controls)
- [Evite reprodução automática](#no-auto-play)
- [Evite conteúdo com flashes ou efeitos estroboscópicos](#no-seizures)

#### Forneça legendas ocultas {#closed-captions}

Inclua legendas ocultas nos seus vídeos para que os usuários possam acompanhar os diálogos, efeitos sonoros e outros conteúdos de áudio. As legendas ajudam:

- Pessoas surdas ou com dificuldade auditiva
- Espectadores assistindo sem som
- Falantes não nativos que preferem ler junto

Legendas ocultas podem ser ativadas ou desativadas, permitindo que os usuários escolham o que funciona melhor para eles.

{% multi_lang_include accessibility/video.md %}

#### Forneça controles de reprodução {#playback-controls}

Certifique-se de que seu vídeo incorporado inclua controles de reprodução acessíveis — como reproduzir, pausar, silenciar e avançar — para que os usuários possam interagir da forma que funciona melhor para eles.

#### Evite reprodução automática {#no-auto-play}

Sempre que possível, evite configurar vídeos para reprodução automática. A reprodução automática pode ser perturbadora ou desorientadora para:

- Usuários que dependem de leitores de tela ou navegação por teclado
- Pessoas com sensibilidade a movimento
- Qualquer pessoa em um ambiente silencioso (como um local de trabalho ou à noite)

Deixe os usuários escolherem quando reproduzir um vídeo incluindo controles claros.

#### Evite conteúdo com flashes ou efeitos estroboscópicos {#no-seizures}

Não inclua vídeos com efeitos de flash ou estroboscópicos, especialmente em alta frequência. Eles podem provocar convulsões em usuários com epilepsia fotossensível e causar desconforto em outros.

### Contraste de cores {#color-contrast}

Contraste de cores suficiente ajuda a garantir que suas mensagens sejam fáceis de ler para todos, incluindo pessoas com baixa visão ou aquelas que visualizam seu conteúdo em condições de iluminação brilhante ou desafiadoras. Mire em proporções de contraste que estejam em conformidade com os [requisitos de nível AA do WCAG 2.2](https://www.w3.org/TR/WCAG/#contrast-minimum):

- Proporção de contraste de 4.5:1 para texto normal (pense em texto do corpo, botões e links)
- Proporção de contraste de 3:1 para texto grande (pense em títulos e rótulos maiores)

Você pode testar suas escolhas de cores usando a [Ferramenta de Verificação de Contraste do WebAim](https://webaim.org/resources/contrastchecker/).

{% multi_lang_include accessibility/color.md %}

### HTML personalizado {#custom-html}

Se você usa qualquer HTML personalizado nas suas mensagens:

- Use [HTML semântico](https://developer.mozilla.org/en-US/docs/Learn/Accessibility/HTML). Isso significa usar os elementos HTML corretos para o propósito pretendido, em vez de estilizar um elemento para parecer outro. A maioria dos elementos HTML tem seu próprio suporte de acessibilidade integrado.
- Para o idioma no nível do documento, onde a Braze pode adicionar metadados HTML na exportação, consulte [Idioma de acessibilidade](#accessibility-language); o comportamento varia por canal. Quando você marca o conteúdo por conta própria, defina o [atributo `lang`](https://developer.mozilla.org/en-US/docs/Web/HTML/Reference/Global_attributes/lang) no seu HTML para identificar o idioma do seu conteúdo. Leitores de tela usam diferentes bibliotecas de som para cada idioma com base na pronúncia e características desse idioma. Se isso não for especificado, o leitor de tela assume que o conteúdo está escrito no idioma padrão que o usuário escolheu ao configurar o leitor de tela. Se a mensagem não estiver realmente no idioma padrão, o leitor de tela pode não pronunciar a mensagem corretamente.

{% raw %}
```html
<html lang="en-us">
```
{% endraw %}

{% alert note %}
Ao usar o editor de arrastar e soltar de e-mail, defina o idioma na guia **Configurações** quando esse controle estiver disponível. E-mails com modelo completo e apenas com Content Blocks podem usar padrões diferentes para o idioma de acessibilidade — veja [Idioma de acessibilidade](#accessibility-language). Outros canais também são abordados nessa seção.
{% endalert %}

- Use [atributos ARIA](#aria-attributes) para fornecer contexto extra. Esses atributos fornecem informações adicionais para tecnologias assistivas, ajudando a esclarecer o papel, estado ou propriedades de elementos de interface que podem não ser claros de outra forma.

### Atributos ARIA {#aria-attributes}

Quando você está usando código personalizado nos editores da Braze, pode usar Accessible Rich Internet Applications ([ARIA](https://developer.mozilla.org/en-US/docs/Web/Accessibility/ARIA)) para fornecer suporte extra de acessibilidade para usuários que dependem de tecnologia assistiva. Papéis e atributos ARIA ajudam leitores de tela a interpretar seu conteúdo com mais clareza, especialmente quando você está usando elementos que não transmitem significado por si só (como `<div>` ou `<span>`).

{% alert important %}
Embora o ARIA seja projetado para tornar o conteúdo web mais acessível, se usado incorretamente, pode causar mais mal do que bem. O ARIA não substitui o HTML semântico, ele o complementa — então use ARIA apenas quando elementos HTML nativos não atenderem às suas necessidades.
{% endalert %}

Aqui estão alguns exemplos especialmente úteis em contextos de envio de mensagens:

- [aria-label](#aria-label)
- [aria-labelledby](#aria-labelledby)
- [aria-hidden="true"](#aria-hiddentrue)
- [role="presentation"](#rolepresentation)
- [aria-live="polite"](#aria-livepolite)

#### aria-label {#aria-label}

`aria-label` adiciona um nome acessível a elementos que não têm texto visível. Se você está usando um ícone sem texto (como uma lixeira ou "X" para fechar), alguém usando um leitor de tela não saberá o que ele faz — a menos que você o rotule. `aria-label` dá voz a esse ícone.

{% raw %}
```html
<button aria-label="Close message">
  <svg ...></svg>
</button>
```
{% endraw %}

#### aria-labelledby {#aria-labelledby}

`aria-labelledby` conecta um elemento a algo que já tem um rótulo visível. Então, se você tem um banner ou região que deve ser lido em voz alta com um título, pode usar `aria-labelledby` para dizer à tecnologia assistiva: "Use aquele título ali para nomear esta parte."

{% raw %}
```html
<h2 id="banner-title">Important Update</h2>
<div role="region" aria-labelledby="banner-title">...</div>
```
{% endraw %}

#### aria-hidden="true" {#aria-hiddentrue}

`aria-hidden="true"` oculta elementos dos leitores de tela. É útil para texto ou elementos visuais que não transmitem significado importante — como um brilho, marca de verificação ou emoji usado puramente para estilo.

Isso mantém a experiência mais limpa para usuários de leitores de tela, que de outra forma poderiam ouvir conteúdo redundante ou confuso. Também é útil para ocultar coisas como conteúdo de acordeão fora da tela que ainda não foi expandido.

{% raw %}
```html
<span aria-hidden="true">✔️</span>
```
{% endraw %}

Em geral, é melhor usar `alt=""` para [imagens decorativas](#images) e ícones em vez de `aria-hidden="true"`. Embora o HTML semântico seja amplamente suportado por todos os leitores de tela e softwares assistivos, o suporte ao ARIA varia. Mesmo se você usar `aria-hidden`, ainda deve incluir um atributo alt vazio.

#### role="presentation" {#rolepresentation}

`role="presentation"` diz à tecnologia assistiva para ignorar elementos que servem apenas para layout, como tabelas de design. Por exemplo, e-mails frequentemente usam tabelas apenas para alinhar elementos. Sem esse papel, leitores de tela podem assumir que seu layout é uma tabela de dados e começar a ler números de linhas e colunas.

{% raw %}
```html
<table role="presentation">...</table>
```
{% endraw %}

E-mails criados no editor de arrastar e soltar de e-mail têm elementos de apresentação automaticamente marcados com o atributo ARIA `role="presentation"`.

#### aria-live="polite" {#aria-livepolite}

`aria-live="polite"` anuncia atualizações quando o conteúdo muda sem necessidade de interação do usuário. Use quando você exibir atualizações dinâmicas dentro de uma mensagem, como sucessos, erros ou outras notificações.

{% raw %}
```html
<div aria-live="polite">Your preferences have been saved.</div>
```
{% endraw %}

## Testes automatizados de acessibilidade {#automated-accessibility-testing}

Para ajudar você a identificar e corrigir problemas de acessibilidade cedo, a Braze oferece testes automatizados de acessibilidade nas seguintes áreas:

- [Inbox Vision]({{site.baseurl}}/user_guide/channels/email/inbox_vision#accessibility-testing) para e-mails
- [Scanner de acessibilidade]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages?tab=in-app%20message#accessibility-scanner) para mensagens criadas usando nosso editor de HTML (por exemplo, mensagens no app em HTML, Content Blocks em HTML, [rodapés de e-mail personalizados]({{site.baseurl}}/user_guide/channels/email/customize/custom_email_footer), [páginas de opt-in de e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup/consent_and_address_collection#creating-a-custom-opt-in-page) e [páginas de cancelamento de inscrição de e-mail]({{site.baseurl}}/user_guide/channels/email/email_setup/consent_and_address_collection#creating-a-custom-unsubscribe-page)).

Esses testes verificam sua mensagem em relação ao padrão Web Content Accessibility Guidelines ([WCAG](https://www.w3.org/WAI/standards-guidelines/wcag/)) — um conjunto de padrões técnicos internacionalmente reconhecidos para conteúdo acessível. Quaisquer problemas que possam ser detectados automaticamente são sinalizados e categorizados por gravidade para ajudar você a priorizar.

{% alert note %}
O Inbox Vision funciona tanto para e-mails em HTML quanto para e-mails de arrastar e soltar. O scanner funciona apenas em conteúdo criado com o editor de HTML.
{% endalert %}

### O que os testes automatizados podem e não podem detectar {#what-automated-testing-can-and-cant-catch}

Testes automatizados de acessibilidade são um ótimo ponto de partida — mas não conseguem detectar tudo. Alguns problemas precisam de um olhar humano para serem avaliados adequadamente, especialmente quando o contexto ou o design visual desempenha um papel na forma como os usuários experimentam seu e-mail.

Você pode ver alguns problemas marcados como **Precisa de revisão**. Esses são casos em que o verificador não consegue determinar com certeza se algo é um problema de acessibilidade. Quando isso acontecer, recomendamos revisá-lo manualmente.

Alguns exemplos do que ferramentas automatizadas não conseguem detectar de forma confiável incluem:

- Se a ordem de foco dos elementos interativos segue uma sequência lógica
- Se o conteúdo é totalmente operável com teclado, sem necessidade de mouse
- Se o texto alternativo descreve significativamente uma imagem
- Se os títulos são usados adequadamente para organizar o conteúdo
- Se links e botões estão claramente rotulados e são fáceis de entender
- Se os alvos de toque são grandes o suficiente e espaçados adequadamente
- Se o texto sobre imagens de fundo atende aos requisitos de contraste de cores
- Se as instruções ou rótulos são claros e úteis para todos os usuários

Essas limitações não são exclusivas da Braze — são comuns a todas as ferramentas automatizadas de acessibilidade. Verificações automatizadas não conseguem simular cada tecnologia assistiva, leitor de tela ou necessidade do usuário. É por isso que acessibilidade não é uma verificação única — é uma prática contínua.

Mesmo que sua mensagem passe em todas as verificações automatizadas, ainda é importante:

- Revisar cuidadosamente os problemas sinalizados, especialmente aqueles rotulados como **Precisa de revisão**.
- Testar manualmente quando possível, especialmente para padrões de layout e interação.
- Usar ferramentas como leitores de tela, navegação apenas por teclado e zoom do navegador para simular diferentes necessidades de acesso.

Ao combinar testes automatizados com uma revisão manual cuidadosa, você detectará mais problemas potenciais e criará campanhas mais inclusivas e utilizáveis para cada destinatário.