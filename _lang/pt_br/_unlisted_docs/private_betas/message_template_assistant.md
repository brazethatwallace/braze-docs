---
nav_title: Assistente de modelo de mensagem
article_title: Assistente de modelo de mensagem
permalink: "/template_assistant/"
description: "Este artigo de referência aborda como usar o assistente de modelo de mensagem para gerar modelos para seu envio de mensagens por e-mail."
page_type: reference
---

# Assistente de modelo de mensagem {#message-template-assistant}

> O assistente de modelo de mensagem ajuda você a iterar em um modelo de e-mail HTML existente usando IA generativa para gerar modelos com base nas suas necessidades específicas. Essa funcionalidade pode ajudar a otimizar seu conteúdo para um caso de uso, público ou conversão específicos, além de reduzir o tempo e o esforço na composição de e-mails.

{% alert important %}
O assistente de modelo de mensagem está em acesso antecipado. Entre em contato com seu gerente de sucesso do cliente se tiver interesse em participar desse acesso antecipado. <br><br>Essa funcionalidade atualmente é compatível apenas com o canal de e-mail e somente no editor de HTML, não em outros editores (como arrastar e soltar ou AMP).
{% endalert %}

## Como funciona {#how-it-works}

O assistente de modelo de mensagem usa suas [diretrizes da marca](https://www.braze.com/docs/user_guide/administrative/app_settings/brand_guidelines) e [configurações de estilo global](https://www.braze.com/docs/user_guide/message_building_by_channel/email/drag_and_drop/dnd_email_style_settings) para adaptar o conteúdo e o estilo da mensagem à sua marca.

Por exemplo, se você tiver configurações de estilo global definidas, o assistente de modelo de mensagem incorporará as cores e os estilos da sua marca. Se você tiver diretrizes da marca definidas na Braze, o assistente também poderá consultá-las para criar textos no tom e na personalidade da sua marca.

O assistente de modelo de mensagem consegue lembrar do histórico do chat apenas enquanto você ainda estiver na mesma janela de chat. Isso significa que ele pode consultar prompts anteriores usados para gerar os próximos. O assistente também tentará iterar seu modelo para responsividade em dispositivos móveis.

Por exemplo, se você passar de um prompt especificamente sobre uma marca de fitness para uma marca genérica nos prompts seguintes, o assistente de modelo de mensagem pode informar ao modelo que se trata daquela mesma marca de fitness. Para iniciar um novo chat, selecione **Limpar histórico** na janela de chat e abra o assistente de modelo de mensagem novamente.

## Criando um modelo {#creating-a-template}

1. No dashboard, acesse **Modelos** > **Modelos de e-mail**.
2. Selecione um modelo de e-mail existente.
3. Na seção **Criar com IA** do editor de HTML, selecione **Modelo**.
4. A partir daqui, você pode inserir diversos prompts ou fazer perguntas sobre seu conteúdo.
5. O assistente de modelo de mensagem fornecerá uma resposta e determinará quais alterações são necessárias no seu modelo.
6. Selecione **Gerar** para aplicar as sugestões.

{% alert important %}
Recomendamos fortemente testar o resultado gerado para garantir que ele corresponda ao seu envio de mensagens.
{% endalert %}

![Um exemplo de prompt para criar um modelo com múltiplas seções para ser usado em vários e-mails. O assistente de modelo de mensagem explica as modificações no modelo atual.]({% image_buster /assets/unlisted_docs/img/ai_message_template_assistant1.png %}){: style="width:70%;"}

### Exemplos de prompts {#example-prompts}

Aqui estão alguns exemplos de prompts para você começar:

- Adicionar uma pesquisa de feedback no final do e-mail
- Alterar a fonte para {% raw %}`{{font name}}` e o tamanho da fonte do parágrafo para o tamanho `{{number}}`{% endraw %}
- Fazer com que todas as imagens tenham cantos arredondados
- Adicionar outra seção com uma imagem e um call-to-action

{% alert note %}
Dependendo do seu prompt e da resposta, o assistente de modelo de mensagem pode adicionar imagens de placeholder ao gerar o novo modelo.
{% endalert %}