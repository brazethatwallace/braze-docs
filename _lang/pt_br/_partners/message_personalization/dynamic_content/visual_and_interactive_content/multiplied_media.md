---
nav_title: Multiplied Media
article_title: Multiplied Media
description: "Saiba como usar a Multiplied Media com a Braze para enviar imagens personalizadas, GIFs e vídeos por e-mail, notificações por push, mensagens no app, Content Cards e WhatsApp."
alias: /partners/multiplied_media/
page_type: partner
search_tag: Partner
---

# Multiplied Media

> A [Multiplied Media](https://multiplied.media) é um estúdio de criação e automação que usa seus dados de CRM para criar imagens personalizadas, GIFs e vídeos — um ativo exclusivo para cada cliente. A integração entre a Multiplied Media e a Braze permite enviar essa mídia por e-mail, notificações por push, mensagens no app, Content Cards e WhatsApp.
>
> A Multiplied Media é um serviço gerenciado, não uma ferramenta de software. A equipe da Multiplied Media cuida do conceito, design, animação, conexão de dados e renderização. Para usar essa integração, insira uma URL de mídia com uma tag de mesclagem [Liquid]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/liquid) na sua Campaign ou Canvas.

_Essa integração é mantida pela Multiplied Media._

## Sobre esta integração {#about-this-integration}

A equipe da Multiplied Media trabalha com você desde o primeiro conceito até o lançamento. Eles projetam e animam mídia para sua marca, conectam seus dados e automatizam a renderização. Você não precisa aprender um novo software.

A integração conecta seus dados da Braze — atributos de clientes e Segments — à Multiplied Media. A Multiplied Media renderiza um ativo de mídia exclusivo para cada cliente e o hospeda em uma URL que contém o identificador desse cliente. Você referencia essa URL na sua mensagem da Braze com uma Liquid merge tag. Cada cliente então vê sua própria imagem, GIF ou vídeo.

A integração suporta dois fluxos:

- **Campaigns em lote:** Envie dados por CSV, S3 ou API or interface de programação do aplicativo (API). A Multiplied Media renderiza e hospeda toda a mídia antes do envio.
- **Automações de Canvas em tempo real:** Uma etapa de [webhook]({{site.baseurl}}/user_guide/channels/webhooks) no seu Canvas dispara a renderização quando um cliente chega a essa etapa.

## Casos de uso {#use-cases}

- **Campaigns personalizadas:** Lançamentos de produtos, campanhas de retrospectiva e "wrapped", promoções sazonais e visualizações de dados pessoais.
- **Automações sempre ativas:** Fluxos de boas-vindas, integração, celebrações de marcos, e-mails de recuperação, carrinho abandonado, notificações de envio, alertas de produto disponível e atualizações de fidelidade.
- **Jornadas omnicanal:** Um conceito, renderizado para cada canal. Os mesmos dados de cliente podem se tornar uma imagem hero de e-mail, uma imagem de push, um visual no app e um vídeo no WhatsApp — assim, a jornada mantém uma identidade visual única em cada ponto de contato.

## Pré-requisitos {#prerequisites}

A arquitetura da Multiplied Media suporta Campaigns baseadas em lotes por meio de S3 ou API or interface de programação do aplicativo (API) e automação de Canvas em tempo real por meio de webhooks. Ao pré-gerar e hospedar ativos de mídia exclusivos antes da entrega, a Multiplied Media garante que experiências visuais individualizadas estejam prontas para serem mescladas nos seus modelos com Liquid tags ou atributos personalizados no momento em que sua mensagem é disparada.

Antes de começar, confirme que você tem o seguinte:

| Requisito | Descrição |
| --- | --- |
| Engajamento ativo com a Multiplied Media | A Multiplied Media é um serviço gerenciado. Antes de começar na Braze, a equipe da Multiplied Media define o escopo da sua campanha, projeta e cria seus modelos de mídia e configura a renderização. Para começar, acesse [multiplied.media](https://multiplied.media) ou envie um e-mail para [hello@multiplied.media](mailto:hello@multiplied.media). |
| Fonte de dados | Conecte seus dados de cliente à Multiplied Media por CSV, S3, API or interface de programação do aplicativo (API) ou webhooks da Braze. A equipe da Multiplied Media configura isso com você durante a integração. |
| Identificador unificador | Seus dados devem incluir um identificador compartilhado entre a Braze e a Multiplied Media, como `external_id`. Esse identificador faz parte da URL de mídia de cada cliente, e sua mensagem na Braze o referencia com Liquid. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Usar Multiplied Media com a Braze {#use-multiplied-media-with-braze}

A Multiplied Media projeta, constrói e renderiza suas mídias personalizadas e ajuda você a conectar seus dados. As etapas a seguir são o que resta para fazer na Braze.

### Etapa 1: Confirmar que sua mídia está pronta {#step-1-confirm-your-media-is-ready}

Antes do lançamento, a equipe da Multiplied Media confirma que sua mídia foi renderizada (Campaigns em lote) ou que seu endpoint de renderização está ativo (fluxos de Canvas em tempo real). Em seguida, eles fornecem a URL de mídia da sua campanha. Por exemplo:

{% raw %}
```
https://cdn.multiplied.media/yourbrand/campaign-name/{{${user_id}}}.gif
```
{% endraw %}

O identificador no caminho da URL é o identificador unificador acordado durante a configuração.

### Etapa 2: Inserir a URL na sua Campaign ou Canvas {#step-2-insert-the-url-into-your-campaign-or-canvas}

Cole a URL da Multiplied Media — com a Liquid tag de mesclagem — no campo do seu canal:

- **E-mail:** A fonte da imagem no seu modelo de e-mail.
- **Notificações por push:** O campo de imagem da sua mensagem push.
- **In-App Messages e Content Cards:** O campo de mídia.
- **WhatsApp:** O campo de cabeçalho de mídia.

Para automações de Canvas em tempo real, adicione a etapa de webhook da Multiplied Media (configurada com você durante a integração) junto com um nó de postergação antes da etapa de mensagem. Isso garante que a mídia seja renderizada para cada cliente antes da entrega.

### Etapa 3: Pré-visualizar, testar e lançar {#step-3-preview-test-and-launch}

Use as prévias e os envios de teste da Braze para confirmar que a Liquid tag é resolvida e que cada usuário teste vê sua própria mídia. A equipe da Multiplied Media analisa os envios de teste com você antes do lançamento.

## Considerações {#considerations}

- O ativo de mídia de cada cliente é único. Se um cliente não estiver na fonte de dados conectada, a URL exibirá uma versão padrão (fallback) da mídia. A Multiplied Media projeta o fallback como parte de cada engajamento.
- A Multiplied Media renderiza e hospeda os ativos antes da entrega; não os renderiza no momento da abertura. A mídia carrega imediatamente ao abrir e exibe os dados do cliente no momento da renderização. Se os dados precisam estar atualizados no momento do envio — por exemplo, em fluxos de Canvas disparados —, use a etapa de webhook em tempo real.
- Para Campaigns agendadas em lote, seus dados devem chegar à Multiplied Media antes do horário de envio para que eles possam renderizar todos os ativos. Sua equipe da Multiplied Media define o horário de corte com você durante a configuração.

## Solução de problemas {#troubleshooting}

Multiplied Media é um serviço gerenciado, então sua equipe da Multiplied Media é sua primeira linha de suporte. Entre em contato pelo e-mail [hello@multiplied.media](mailto:hello@multiplied.media).

Consulte a tabela a seguir se sua imagem dinâmica não for exibida.

| Problema | Resolução |
| --- | --- |
| A imagem dinâmica não é exibida | Confirme se a Liquid tag na URL corresponde ao identificador unificador acordado durante a configuração (por exemplo, `user_id` versus um atributo personalizado). Confirme se o cliente existe na fonte de dados conectada. Se o identificador for resolvido, mas não existir um ativo personalizado, a mídia de fallback será exibida. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Solução de problemas" }