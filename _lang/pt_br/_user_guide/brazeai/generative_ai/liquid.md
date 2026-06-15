---
nav_title: Código Liquid
article_title: Gerar código Liquid com BrazeAI
description: "Este artigo aborda como o Liquid Assistant de IA funciona e como você pode usá-lo para gerar snippets de Liquid para o envio de mensagens."
page_type: reference
page_order: 0.0
---

# Gerar código Liquid com BrazeAI {#generate-liquid-code-with-brazeai}

> O Liquid Assistant da BrazeAI<sup>TM</sup> é um assistente de bate-papo desenvolvido pela BrazeAI<sup>TM</sup> que ajuda a gerar o Liquid de que você precisa para personalizar o conteúdo das mensagens.

## Sobre o assistente Liquid da BrazeAI<sup>TM</sup> {#about-the-brazeaitm-liquid-assistant}

O Liquid Assistant da BrazeAI<sup>TM</sup> foi projetado para ajudar você a escrever código Liquid eficaz e adaptado às suas necessidades de marketing. Treinada na sintaxe do Liquid e em como os profissionais de marketing utilizam o Liquid em suas mensagens, nossa IA entende as nuances da elaboração de conteúdo personalizado.

Além disso, ao fornecer ao Liquid Assistant da BrazeAI<sup>TM</sup> os nomes dos seus atributos personalizados (como "favourite_color") e tipos de dados (como booleano e string), nosso Liquid Assistant da BrazeAI<sup>TM</sup> garante que suas mensagens sejam precisamente direcionadas e alinhadas com seus objetivos. Se você criar Diretrizes da marca, o Liquid Assistant da BrazeAI<sup>TM</sup> poderá usá-las para personalizar melhor os resultados gerados e adaptar o conteúdo à voz da sua própria marca. As Diretrizes da marca que você criar serão usadas apenas para personalizar o conteúdo para seu próprio uso.

## Canais compatíveis {#supported-channels}

Você pode usar o Liquid Assistant da BrazeAI<sup>TM</sup> ao criar:
- Mensagens SMS
- Notificações por push
- Mensagens de e-mail em HTML
- Canvas

{% alert note %}
O assistente funciona em mensagens de e-mail, não em modelos. Ele funciona melhor em mensagens de e-mail que já estão construídas.
{% endalert %}

## Gerando código Liquid {#generating-liquid-code}

Para iniciar o Liquid Assistant da BrazeAI<sup>TM</sup>, selecione o ícone do assistente de IA no criador de mensagens.

![Criador de mensagens com o assistente de IA.]({% image_buster /assets/img/ai_liquid/ai_assistant_icon.png %}){: style="max-width:50%;"}

Você pode escolher um dos prompts incluídos ou inserir o seu próprio na caixa de texto.

{% tabs local %}
{% tab Usar atividade do app %}
O prompt **Usar atividade do app** gera código Liquid para ajudar você a enviar mensagens diferentes com base na última vez em que o app foi usado. Poderão ser feitas perguntas complementares para que o assistente possa gerar um resultado mais preciso.

![Exemplo de saída do prompt "Usar atividade do app".]({% image_buster /assets/img/ai_liquid/use_app_activity.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab Adicionar contagem regressiva %}
Esse prompt gera código Liquid que envia uma mensagem com o tempo que falta para um evento acontecer. Ele solicitará que você forneça detalhes sobre a data e a hora do evento.

![Exemplo de saída do prompt "Adicionar contagem regressiva".]({% image_buster /assets/img/ai_liquid/add_countdown.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab Inspire-me %}
Esse prompt aparece quando há conteúdo na sua caixa de mensagens. Ele gera uma lista de opções que você pode escolher para personalizar sua mensagem com Liquid.

![Exemplo de saída do prompt "Inspire-me".]({% image_buster /assets/img/ai_liquid/inspire_me.png %}){: style="max-width:45%;"}
{% endtab %}

{% tab Melhorar meu Liquid %}
Esse prompt é exibido quando há conteúdo no seu criador de mensagens. Selecione-o quando quiser que o assistente torne seu código mais eficiente e mais fácil de ler.

![Exemplo de saída do prompt "Melhorar meu Liquid".]({% image_buster /assets/img/ai_liquid/improve_my_liquid.png %}){: style="max-width:45%;"}
{% endtab %}
{% endtabs %}

Para gerar seu código Liquid, selecione **Update composer**.

![Janela do assistente de IA com prompts fornecidos.]({% image_buster /assets/img/ai_liquid/ai_assistant_window.png %}){: style="max-width:50%;"}

Você pode gerar outra mensagem usando o mesmo prompt selecionando **Regenerate**. Para remover a mensagem e reverter para a anterior, selecione **Undo update**.

## Atributos Liquid {#supported-attributes}

Os seguintes atributos estão atualmente em beta para o Liquid Assistant da BrazeAI<sup>TM</sup>:

| Critério | Tipo de conhecimento |
| - | - |
| Liquid (incluindo loops `for`, declarações `if`, matemática e outros) | Codificação |
| Atributos de usuário padrão e standard | Atributos |
| Atributos personalizados que têm qualquer um desses tipos de dados: {::nomarkdown}<ul><li>Booleanos</li><li>Números</li><li>Strings</li><li>Arrays</li><li>Horário</li></ul>{:/} | Atributos |
| Conteúdo conectado | Codificação |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Liquid attributes" }

## Melhores práticas {#best-practices}

Para ajuda na redação de prompts eficazes para o Liquid Assistant da BrazeAI<sup>TM</sup>, confira nossas melhores práticas:

### Use linguagem natural {#use-natural-language}

O Liquid Assistant da BrazeAI<sup>TM</sup> é treinado para entender a linguagem natural. Converse com ele como faria com um colega de trabalho ao pedir ajuda. Isso torna mais fácil para o assistente compreender suas necessidades e fornecer assistência precisa.

### Dê contexto {#give-context}

Fornecer contexto ajuda o Liquid Assistant da BrazeAI<sup>TM</sup> a entender o panorama geral do seu projeto. É útil incluir contexto como:

- Nome e setor da sua empresa
- Uma campanha na qual você está trabalhando, como a Black Friday ou vendas de fim de ano
- Seu objetivo, como aumentar sua taxa de cliques
- Atributos personalizados específicos que deseja incluir na sua mensagem

Incluir contexto no seu prompt ajuda o assistente a adaptar as respostas para atender melhor às suas necessidades. Você também pode incluir detalhes da sua campanha, resumo de mensagens ou documento de brainstorming para que o assistente fique a par de tudo.

### Seja específico {#be-specific}

O Liquid Assistant da BrazeAI<sup>TM</sup> pode fazer perguntas de acompanhamento, mas fornecer detalhes antecipadamente pode agilizar a geração de resultados mais precisos. Considere incluir detalhes como:

- Quaisquer preferências ou requisitos conhecidos para a mensagem
- Instruções sobre como lidar com situações, como a falta de respostas do destinatário da mensagem ou opções de mensagem fallback
- Ao solicitar Liquid que usa Conteúdo conectado, a documentação do endpoint da API, uma amostra da resposta da API ou ambos

### Seja criativo {#get-creative}

Pense fora da caixa com seus prompts para ver como o Liquid Assistant da BrazeAI<sup>TM</sup> pode aprimorar seu envio de mensagens. Faça experiências com diferentes prompts e ideias, pois a criatividade pode levar a resultados mais engajadores.

## Exemplos de prompts {#example-prompts}

Aqui estão alguns exemplos para ajudar você a começar:

{% tabs local %}
{% tab Adquirindo conhecimento %}
- O que é o Liquid e como ele pode me ajudar a aprimorar a personalização das minhas campanhas de marketing na Braze?
- Que tipos de dados posso usar no Liquid para personalizar minhas mensagens de marketing, como informações demográficas ou compras anteriores?
{% endtab %}

{% tab Personalizando conteúdo dinâmico %}
- Crie uma mensagem que mostre conteúdo diferente com base no status de fidelidade do meu cliente. Se não soubermos o status de fidelidade dele, envie uma mensagem fallback.
- Escreva uma mensagem dinâmica que inclua o produto favorito de um usuário e a data da última compra. Se não houver uma última compra, cancele a mensagem.
- Escreva Liquid para incentivar alguém a clicar na minha mensagem, incluindo uma contagem regressiva com o tempo restante. Se a oferta tiver expirado, cancele a mensagem.
- Ajude-me a escrever uma mensagem para incentivar os usuários a voltarem e finalizarem a compra se tiverem itens restantes no carrinho.
- Escreva Liquid para personalizar uma mensagem com base no país de um cliente. Quero preencher a mensagem com o nome do país. Se não tivermos nenhum deles, sugira que ele clique em um link para atualizar seu perfil.
- Como posso personalizar uma mensagem de boas-vindas com o nome de um usuário e escrever um texto diferente com base no gênero do usuário?
- Escreva Liquid para exibir mensagens diferentes com base em um atributo personalizado, "CUSTOM_ATTRIBUTE_NAME" e seu valor. Há seis opções diferentes que eu poderia enviar. Se não houver nenhum valor para o atributo personalizado, quero enviar uma mensagem de espaço reservado.
{% endtab %}

{% tab Lidando com exceções %}
- Você pode me dar alguns exemplos de como o Liquid é usado em campanhas de marketing para aumentar o engajamento e as taxas de conversão?
- Quais são alguns casos de uso comuns para o Liquid em mensagens de texto para vendas de verão, como lembretes de abandono de carrinho ou promoções personalizadas?
{% endtab %}
{% endtabs %}

{% alert tip %}
Conte para nós se você teve algum prompt ou experiência interessante agendando uma [sessão de feedback](https://research.rallyuxr.com/braze/schedule/clxxhw8em0d071ak4b279553s?channel=share) conosco.
{% endalert %}

{% multi_lang_include brazeai/generative_ai/policy.md %}