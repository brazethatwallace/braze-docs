---
nav_title: Entrega otimizada
article_title: Mensagens de WhatsApp com entrega otimizada
page_order: 1
description: "Este artigo de referência aborda as etapas envolvidas na criação de uma mensagem de WhatsApp com entrega otimizada."
page_type: reference
tool:
  - Campaigns
channel:
  - WhatsApp
---

# Mensagens de WhatsApp com entrega otimizada {#whatsapp-messages-with-optimized-delivery}

> Aumente a entregabilidade e o engajamento alcançando mais usuários certos no WhatsApp com entrega dinâmica baseada em engajamento.

As mensagens de WhatsApp com entrega otimizada são enviadas usando a [Marketing Messages API for WhatsApp](https://developers.facebook.com/docs/whatsapp/marketing-messages-api-for-whatsapp) (MM API for WhatsApp) da Meta, que oferece entrega dinâmica baseada em engajamento. Isso significa que suas mensagens de alto engajamento (por exemplo, aquelas com maior probabilidade de serem lidas e clicadas) podem alcançar mais usuários propensos a interagir com elas. O WhatsApp considera suas mensagens como de alto engajamento se forem esperadas, relevantes e oportunas, e portanto mais propensas a serem lidas e clicadas.

As marcas podem esperar entregabilidade igual ou superior com a MM API for WhatsApp, em comparação com a Cloud API. Na Índia, mensagens de marketing de alto engajamento tiveram até 9% mais mensagens entregues em comparação com a Cloud API, de acordo com a Meta. Note que a MM API for WhatsApp ainda não garante 100% de entregabilidade.

### Disponibilidade regional {#regional-availability}

A disponibilidade e as capacidades de otimização da entrega otimizada dependem da região do número de telefone comercial e do usuário. Para saber mais, consulte [Geographic availability of features](https://developers.facebook.com/docs/whatsapp/marketing-messages-lite-api/get-started#geographic-availability-of-features).

## Configurando a entrega otimizada {#setting-up-optimized-delivery}

1. Na Braze, acesse **Integrações de parceiros** > **Parceiros de tecnologia** > **WhatsApp**.
2. Na seção **Optimize your sending with optimized delivery**, selecione **Upgrade setting** para iniciar o [fluxo de cadastro integrado]({{site.baseurl}}/user_guide/channels/whatsapp/whatsapp_setup/embedded_signup/).

![A seção de integração de mensagens do WhatsApp com uma opção para otimizar o envio com entrega otimizada.]({% image_buster /assets/img/whatsapp/whatsapp_messaging_integration.png %})

{: start="3"}
3. Após a entrega otimizada ser ativada, os detalhes da sua conta em **WhatsApp Business Account Management** exibirão o status da entrega otimizada.

![Seção de gerenciamento de conta do WhatsApp Business com um grupo de inscrições listado que possui um status de número ativo.]({% image_buster /assets/img/whatsapp/optimized_delivery_message.png %})

Alternativamente, você pode ativar a entrega otimizada diretamente no seu WhatsApp Manager e então começar a enviar pela Braze.

### Solução de problemas na configuração {#troubleshooting-your-setup}

- **Erro geral:** Se algo der errado durante o upgrade, este banner de erro será exibido e aconselhará você a [entrar em contato com o Suporte]({{site.baseurl}}/braze_support/).
- **Erro de inelegibilidade:** Se você estiver restrito pela Meta, este banner de erro será exibido: "At least one WhatsApp Business Account is restricted by Meta. Accounts must be in good standing to upgrade." Ele não pode ser descartado até que o problema seja resolvido.

## Usando a entrega otimizada em Campaigns e Canvas {#using-optimized-delivery-in-campaigns-and-canvases}

A entrega otimizada deve ser usada para **mensagens de marketing**. A Braze removerá automaticamente a opção de entrega otimizada para **mensagens de utilidade, autenticação, serviço e resposta**, que devem continuar sendo enviadas pela Cloud API, que é a configuração padrão.

### Selecionando o método de entrega {#selecting-the-delivery-method}

1. No criador de mensagens de WhatsApp da Braze para uma Campaign ou uma etapa de mensagem do Canvas, acesse a guia **Settings**.
2. Na seção **Delivery method**, a caixa de seleção **Optimized Delivery (Recommended)** estará marcada por padrão se sua conta do WhatsApp Business (WABA) estiver ativada. Se você não quiser usar a entrega otimizada para essa mensagem específica, desmarque a caixa de seleção.
- Se você selecionar a entrega otimizada, mas ela não estiver disponível, a mensagem automaticamente voltará para o método da Cloud API.

![Criador de mensagens com uma guia de pré-visualização que possui uma caixa de seleção para selecionar a entrega otimizada.]({% image_buster /assets/img/whatsapp/delivery_method_settings.png %})

### Redirecionando usuários em outros canais da Braze {#retargeting-users-on-other-braze-channels}

Como a MM API for WhatsApp não oferece 100% de entregabilidade, é importante entender como redirecionar usuários que podem não ter recebido sua mensagem em outros canais.

Para redirecionar usuários, recomendamos criar um segmento de usuários que não receberam uma mensagem específica. Para isso, filtre pelo código de erro `131049`, que indica que uma mensagem de modelo de marketing não foi enviada devido à aplicação do limite de modelo de marketing por usuário do WhatsApp. Você pode fazer isso usando Braze Currents ou extensões de segmento SQL:

- **Braze Currents:** Exporte eventos de falha de mensagem usando Braze Currents. Você pode então usar esses dados para atualizar um atributo personalizado no perfil de usuário (como `whatsapp_failed_last_msg: true`), que pode ser usado como filtro para sua Campaign de redirecionamento.
- **Extensões de segmento SQL:** Se você tiver acesso a esse recurso, pode usar SQL para consultar os registros de falha de mensagem e criar um segmento desses usuários, e então direcionar esse segmento em um canal diferente.