---
nav_title: Estilização de e-mail
article_title: Estilização de e-mail
page_order: 2
page_type: reference
description: "Este artigo descreve as melhores práticas de estilização de e-mail para consultar ao criar suas campanhas de e-mail."
channel: email

---

# Estilização de e-mail

> Este artigo descreve as melhores práticas de estilização de e-mail, incluindo linhas de assunto, pré-cabeçalho, tamanho do e-mail e recomendações de imagens.

## Estilização de endereço

A linha de assunto é uma das primeiras coisas que os destinatários veem ao receber sua mensagem. Mantê-la entre 6 e 10 palavras gera as maiores taxas de abertura.

Existem também diferentes abordagens para criar uma boa linha de assunto, desde fazer uma pergunta para despertar o interesse do leitor, ser mais direto ou personalizá-la para engajar sua clientela. Não se limite a uma única linha de assunto — use [testes A/B]({{site.baseurl}}/user_guide/messaging/ab_testing/#what-are-multivariate-and-ab-testing/) para experimentar novas opções e avaliar sua eficácia. As linhas de assunto devem ter no máximo 35 caracteres para serem exibidas corretamente em dispositivos móveis.

O campo "De" deve mostrar claramente quem é o remetente. Evite usar o nome de uma pessoa ou uma abreviação incomum. Em vez disso, use um nome reconhecível, como o nome da sua marca. Se usar o nome de uma pessoa for adequado aos métodos de personalização de e-mail da sua marca, mantenha a consistência para desenvolver um relacionamento com o destinatário. O nome do remetente deve ter no máximo 25 caracteres para ser exibido corretamente em dispositivos móveis.

### Endereços sem resposta (no-reply)

Endereços de e-mail sem resposta geralmente não são recomendados por vários motivos, pois afastam seus leitores. Muitos destinatários respondem ao e-mail para cancelar a inscrição. Se não puderem fazer isso, a próxima ação mais comum é marcar o e-mail como spam.

Receber respostas automáticas de ausência pode fornecer informações valiosas, aumentando as taxas de abertura e reduzindo os relatórios de spam (ao remover aqueles que não desejam receber e-mails). Em um nível pessoal, um endereço sem resposta pode parecer impessoal para os destinatários e pode afastá-los de receber mais e-mails da sua empresa.

## Pré-cabeçalho

O pré-cabeçalho de um e-mail comunica o ponto principal da mensagem de forma eficiente para captar o interesse do leitor e incentivar a abertura. O pré-cabeçalho também é frequentemente usado por profissionais de marketing para fornecer informações adicionais sobre o conteúdo do e-mail. O pré-cabeçalho é o texto de pré-visualização exibido imediatamente após o assunto do e-mail. No exemplo a seguir, o pré-cabeçalho é `- Brand. New. Lounge Shorts`.

![Pré-cabeçalho em uma caixa de entrada do Gmail com o texto "Brand. New. Lounge Shorts".]({% image_buster /assets/img_archive/preheader_example.png %})

A quantidade de pré-cabeçalho visível depende do cliente de e-mail do usuário e do comprimento da linha de assunto do e-mail. De modo geral, recomendamos que os pré-cabeçalhos tenham entre 50 e 100 caracteres.

{% alert note %}
O pré-cabeçalho pode referenciar Liquid no corpo do e-mail, e o corpo do e-mail pode referenciar Liquid no pré-cabeçalho. Isso ocorre porque o pré-cabeçalho faz parte do corpo do e-mail quando você envia mensagens aos destinatários.
{% endalert %}

Aqui estão algumas melhores práticas para ter em mente ao escrever seus pré-cabeçalhos:

1. As chamadas para ação entram em cena depois que os leitores abrem seu e-mail.
  - Direcione seus leitores na direção certa, seja para se inscrever, comprar um produto ou visitar seu site.
  - Use palavras fortes para que o leitor saiba exatamente o que você está pedindo, mas certifique-se de que isso reflita a voz da marca da sua empresa e que cada chamada para ação apresente algum tipo de valor para o consumidor.
  - O pré-cabeçalho deve ter no máximo 85 caracteres e conter algum tipo de chamada para ação descritiva que complemente a linha de assunto.

2. Os e-mails e as páginas de destino para os quais você direciona seus usuários devem ser otimizados para dispositivos móveis:
  - Sem caixas intersticiais
  - Campos de formulário grandes
  - Navegação fácil
  - Texto grande
  - Espaço em branco generoso
  - Texto do corpo curto e conciso
  - Chamadas para ação claras

### Limites de caracteres do pré-cabeçalho

  |   Cliente de e-mail móvel  |  Limite  |
  |:----------------------:|:-------:|
  | iOS Outlook            | 74      |
  | Android Nativo         | 43      |
  | Android Gmail          | 24      |
  | iOS Nativo             | 82      |
  | iOS Gmail              | 30      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }

  |  Cliente de e-mail desktop  |  Limite  |
  |:----------------------:|:-------:|
  | Apple Mail             | 33      |
  | Outlook '13            | 38      |
  | Outlook for Mac '15   | 53      |
  | Outlook '16            | 50      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }


  |  Cliente de e-mail webmail  |  Limite  |
  |:----------------------:|:-------:|
  | AOL Mail               | 81      |
  | Gmail                  | 119     |
  | Outlook.com            | 49      |
  | Office 365             | 40      |
  | Mail.ru                | 64      |
  {: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Tamanho do e-mail

O tamanho do e-mail refere-se ao tamanho do HTML da sua mensagem na Braze (o corpo que você cria e o que a Braze adiciona quando a mensagem é enviada).

- Certifique-se de limitar o tamanho do seu e-mail. Corpos de e-mail maiores que 102&nbsp;KB não apenas sobrecarregam os servidores da Braze, mas também são cortados pelo Gmail e outros clientes de e-mail.
- Imagens hospedadas que você referencia por URL não são incorporadas no HTML da mesma forma que colar grandes ativos inline. Recomendamos usar a [Biblioteca de mídia]({{site.baseurl}}/user_guide/messaging/design_and_edit/media_library/) e vincular por `href`, o que ajuda a manter a mensagem menor.

|   Somente texto   | Texto com imagens |     Largura do e-mail    |
|:-------------:|:----------------:|:------------------:|
| 25&nbsp;KB máximo |   60&nbsp;KB máximo   | 600 pixels máximo |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 role="presentation" }

Para reduzir o risco de corte:

- Encurte textos e links.
- Aplique CSS crítico inline quando necessário. Remova espaços em branco extras no HTML.
- Comprima imagens e ativos HTML.

{% alert note %}
Para salvar sua campanha de e-mail ou modelo, certifique-se de que o corpo do e-mail não exceda 400&nbsp;KB.
{% endalert %}

### O que pode aumentar o tamanho final do e-mail?

Esses recursos aumentam o tamanho da mensagem renderizada em pequenas quantidades:

- Pixel de rastreamento de abertura: adiciona uma tag de imagem de 1 x 1&nbsp;px ao corpo da mensagem
- Pré-cabeçalho: adiciona um `<div>` oculto no topo do corpo
- Alias de link: adiciona um parâmetro de consulta de 16 caracteres (`lid=`) a cada URL rastreada
- Modelos de link: adiciona quaisquer parâmetros de consulta configurados no dashboard às URLs correspondentes
- CSS inline (opcional): aplica regras de folha de estilo incorporadas inline aos elementos HTML, o que pode adicionar CSS redundante dependendo da complexidade da folha de estilo

O pré-cabeçalho e o pixel de rastreamento adicionam aproximadamente 600 caracteres (menos de 1&nbsp;KB). A Braze normalmente adiciona entre 0&nbsp;KB e 5&nbsp;KB dependendo do número de links, da complexidade do modelo de link e se o CSS inline está ativado. Se o tamanho do seu e-mail estiver próximo do limite, recomendamos testar os e-mails antes de enviar, pois o tamanho final renderizado depende dessas variáveis.

## Comprimento do texto

Consulte a tabela a seguir para os comprimentos de texto recomendados.

| Especificações de texto | Propriedades recomendadas |
| --- | --- |
| Comprimento da linha de assunto | 35 caracteres máximo (para exibição ideal em dispositivos móveis) (6 a 10 palavras) |
| Comprimento do nome do remetente | 25 caracteres máximo (para exibição ideal em dispositivos móveis) |
| Comprimento do pré-cabeçalho | 85 caracteres máximo |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Tamanho da imagem

Consulte a tabela a seguir para os tamanhos de imagem recomendados. Imagens menores e de alta qualidade carregam mais rápido, então use o menor ativo possível para alcançar o resultado desejado.

|     Tamanho    | Largura da imagem do cabeçalho |  Largura da imagem do corpo  |   Tipos de arquivo  |
|:-----------:|:------------------:|:------------------:|:-------------:|
| 5&nbsp;MB máximo | 600 pixels máximo | 480 pixels máximo | PNG, JPEG, GIF |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 role="presentation" }

## Deep linking

Com notificações por push e mensagens no app, um [deep link]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/actions_and_media_urls/) leva os usuários diretamente a um destino específico dentro de um app. No entanto, deep links exigem que o app esteja instalado, e os e-mails não oferecem uma forma de saber se os destinatários têm o app. Isso significa que deep links em e-mails podem resultar em erros para destinatários que não têm o app instalado.

Em vez disso, use [links universais e App Links]({{site.baseurl}}/user_guide/channels/email/customize/universal_links_and_app_links/), que funcionam como URLs padrão. Você pode configurá-los para abrir o app ou direcionar os usuários a uma página específica. Eles também podem redirecionar para a loja de apps ou voltar para uma página da web quando o app não está instalado.

## Blocos de conteúdo com imagens transparentes

Quando um bloco de conteúdo contém uma imagem com fundo transparente (por exemplo, um logotipo) e é inserido por uma Liquid tag, você pode ver uma cor de fundo aparecer atrás da imagem. Essa cor vem das [configurações de estilo global de e-mail]({{site.baseurl}}/user_guide/channels/email/customize/email_global_style_settings/) do editor de arrastar e soltar — especificamente a **Cor de fundo do e-mail**. Se suas configurações de estilo global usam uma cor diferente de branco, essa cor aparecerá no lugar.

Para exibir o bloco de conteúdo conforme o esperado:

- Defina a cor de fundo da coluna do bloco de conteúdo para corresponder ao fundo do e-mail ou modelo.
- Alternativamente, converta o bloco de conteúdo de arrastar e soltar em um bloco de conteúdo HTML e defina seu fundo como transparente.

Se você precisar usar o mesmo bloco de conteúdo em áreas com fundos diferentes (por exemplo, corpo e rodapé), crie duas versões do bloco, cada uma com a cor de fundo de coluna apropriada.

Se preferir arrastar o bloco de conteúdo para o e-mail como uma linha, você pode definir o fundo da coluna da linha como transparente para substituir o fundo global.

{% alert note %}
Arrastar um bloco de conteúdo como uma linha insere um snapshot pré-renderizado, que não é atualizado automaticamente se o bloco de conteúdo de origem for alterado.
{% endalert %}