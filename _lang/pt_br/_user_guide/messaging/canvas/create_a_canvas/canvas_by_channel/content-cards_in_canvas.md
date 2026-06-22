---
nav_title: Content Cards
article_title: Content Cards no Canvas
page_order: 1
page_type: reference
description: "Este artigo de referência descreve recursos e nuances específicos do uso de Content Cards como canal de envio de mensagens no Canvas."
tool: Canvas
channel: content cards

---

# Content Cards no Canvas {#content-cards-in-canvas}

> Os Content Cards podem ser enviados aos seus clientes como parte da jornada no Canvas. Este artigo descreve recursos e nuances específicos do uso de Content Cards como canal de envio de mensagens no Canvas.

Assim como outros canais de envio de mensagens do Canvas, os Content Cards serão enviados ao dispositivo do usuário quando ele atender aos critérios de público e direcionamento especificados para a etapa. Depois que o cartão de conteúdo for enviado, ele ficará disponível no feed de cada usuário elegível na próxima vez que o feed de cartões for atualizado.

![Content Cards selecionados como canal de envio de mensagens para uma etapa de Mensagem.]({% image_buster /assets/img_archive/content-cards-in-canvas.png %})

Duas opções que alteram a forma como a etapa de cartão de conteúdo interage com o Canvas são a [expiração](#content-card-expiration) e a [remoção](#removal).

## Expiração do cartão de conteúdo {#content-card-expiration}

Ao criar um novo cartão de conteúdo, você pode escolher quando ele deve expirar no feed do usuário com base no horário de envio. A contagem regressiva para a expiração de um cartão de conteúdo começa quando o usuário chega à etapa de Mensagem no Canvas em que o cartão é enviado. O cartão ficará ativo no feed do usuário a partir desse momento até expirar. Um cartão pode existir no feed de um usuário por até 30 dias.

![Configurações de expiração de um cartão de conteúdo para uma etapa de Mensagem que será removido após três horas no feed do usuário.]({% image_buster /assets/img_archive/content-cards-in-canvas-expiration.png %})

### Tipos de expiração {#types-of-expiration}

Existem duas formas de definir quando um cartão deve desaparecer do feed de um usuário: uma data relativa ou uma data absoluta.

#### Datas relativas {#relative-dates}

Ao escolher uma data relativa, como "Remover cartões enviados após 5 dias no feed do usuário", você pode definir uma data de expiração de até 30 dias.

#### Datas absolutas {#absolute-dates}

Ao escolher uma data absoluta, como "Remover cartões enviados em 1º de dezembro de 2023 às 16h", existem algumas nuances envolvidas.

Embora você possa especificar uma duração de expiração superior a 30 dias, o cartão de conteúdo existirá no feed do usuário por no máximo 30 dias. Especificar uma duração superior a 30 dias permite considerar possíveis atrasos antes de acionar a etapa de Mensagem, mas não estende a vida máxima do cartão no feed do usuário.

Tenha cuidado ao definir uma data de expiração com mais de 30 dias de antecedência em relação ao lançamento do Canvas. Se um usuário chegar à etapa de Mensagem mais de 30 dias antes da data de expiração especificada, o cartão não será enviado.

#### Expiração personalizada com Liquid {#personalized-expiry-with-liquid}

Quando você usa personalização com Liquid para definir a duração da expiração (por exemplo, usando atributos personalizados ou propriedades de entrada do Canvas), o comportamento difere das datas absolutas ou relativas:

- Se a expiração personalizada resultar em uma duração superior a 30 dias, a Braze automaticamente limita ao máximo de 30 dias.
- O cartão de conteúdo ainda é enviado ao usuário com a expiração limitada.
- O usuário avança para a próxima etapa no Canvas.

Essa limitação garante que cartões com expiração personalizada sejam entregues mesmo quando a duração calculada excede o limite da plataforma. O resultado no registro de processamento mostrará "Personalized expiration capped by max TTL" com detalhes indicando `reason=capped_by_max_ttl` e `capped=true`.

### Comportamento de expiração {#expiration-behavior}

O cartão de conteúdo permanece disponível no feed do usuário até atingir sua data de expiração, mesmo que o usuário avance para etapas subsequentes na jornada do Canvas. Se você não quiser que o cartão de conteúdo esteja ativo quando as próximas etapas do Canvas forem entregues, certifique-se de que a expiração seja menor do que a postergação nas etapas subsequentes.

Depois que um cartão de conteúdo expira, ele será automaticamente removido do feed do usuário na próxima atualização, mesmo que o usuário ainda não o tenha visualizado.

## Remoção do cartão de conteúdo {#removal}

Os Content Cards podem ser removidos quando os usuários concluem uma compra ou realizam um evento personalizado. Você pode selecionar uma das seguintes opções como evento de remoção: **Perform Custom Event** e **Place Order**. Em seguida, selecione **Add Trigger**.

!["Remover cartões quando os usuários concluírem uma compra ou realizarem um evento personalizado." selecionado com o gatilho para remover cartões de usuários que fazem uma compra específica.]({% image_buster /assets/img_archive/content-cards-in-canvas-removal-event.png %})

## Relatórios e análise de dados {#reporting-and-analytics}

Após lançar uma etapa de Content Cards no Canvas, você pode começar a analisar diversas métricas para essa etapa. Essas métricas incluem o número de mensagens enviadas, impressões diárias únicas, taxas de conversão, receita total e muito mais.

![Análise de dados de uma etapa de Mensagem com o desempenho de mensagens do cartão de conteúdo.]({% image_buster /assets/img_archive/content-cards-in-canvas-analytics.png %})

Para saber mais sobre as métricas disponíveis e suas definições, consulte nosso [Glossário de métricas de relatório]({{site.baseurl}}/user_guide/analytics/metrics_glossary/).

## Casos de uso {#use-cases}

### Ofertas promocionais {#promotional-offers}

Adicione cartões ao feed de um usuário quando ele se qualificar para promoções e anúncios específicos. Por exemplo, se um usuário se tornar elegível para uma nova oferta após realizar uma ação ou fazer uma compra, usando o Canvas você pode enviar um Content Card, além de outros canais de envio de mensagens, para que na próxima vez que ele abrir o app a oferta esteja disponível.

### Caixa de entrada de notificações por push {#push-notification-inbox}

Há momentos em que um usuário pode dispensar uma notificação por push ou excluir um e-mail, mas você deseja lembrá-lo ou promover a oferta caso ele mude de ideia.

Usando o Canvas, você pode adicionar um componente que envia tanto um Content Card quanto uma notificação por push, oferecendo aos usuários uma "caixa de entrada" persistente de cartões alinhados com as mensagens promocionais enviadas via push.

### Múltiplos feeds baseados em categorias {#multiple-feeds-based-on-categories}

Você pode separar seus Content Cards em múltiplos feeds com base em categorias, como diferentes tópicos que os usuários podem explorar, ou feeds transacionais e de marketing. Para saber mais sobre como criar múltiplos feeds usando pares chave-valor, confira nosso guia para [Personalizar feeds de Content Cards]({{site.baseurl}}/developer_guide/customization_guides/content_cards/customizing_feed/#multiple-feeds).