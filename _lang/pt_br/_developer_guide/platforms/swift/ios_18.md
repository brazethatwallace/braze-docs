---
nav_title: Fazendo upgrade para o iOS 18
article_title: Fazendo upgrade para o iOS 18
page_order: 7.1
platform:
  - iOS
description: "Este artigo aborda insights sobre a versão do iOS 18 para ajudar você a fazer upgrade do seu SDK sem problemas."
---

# Fazendo upgrade para o iOS 18 {#upgrading-to-ios-18}

> Quer saber como a Braze está se preparando para o próximo lançamento do iOS? Este artigo resume nossos insights sobre o lançamento do iOS 18 para ajudar você a criar uma experiência perfeita para você e seus usuários.

A [WWDC](https://developer.apple.com/wwdc24/) da Apple foi realizada de 9 a 11 de junho de 2024. Saiba mais sobre os anúncios em nossa [publicação no blog](https://www.braze.com/resources/articles/wwdc-announcements-bring-apple-intelligence-rcs-and-more-to-ios-18) ou continue lendo para saber como aproveitar o iOS 18 com a Braze.

## Alterações no iOS 18 {#changes-in-ios-18}

### Live Activities no Apple Watch {#live-activities-on-apple-watch}

O [Live Activities]({{site.baseurl}}/developer_guide/push_notifications/live_notifications?sdktab=swift) será compatível com o watchOS 11. Não é necessária nenhuma configuração adicional. No entanto, a Apple oferece a opção de personalizar a interface do relógio.

### Apple Vision Pro

O Vision Pro já está disponível na China, Japão, Cingapura, Austrália, Canadá, França, Alemanha e Reino Unido. Confira nosso blog para ver como a [Braze oferece suporte ao visionOS](https://www.braze.com/resources/articles/building-braze-a-new-era-of-customer-engagement-braze-announces-visionos-support).

### Notificações do iPhone no macOS {#iphone-notifications-on-macos}

O novo recurso de [espelhamento do iPhone](https://www.apple.com/newsroom/2024/06/macos-sequoia-takes-productivity-and-intelligence-on-mac-to-new-heights/) da Apple permite que os usuários recebam notificações do iPhone em seus dispositivos macOS. Lembre-se de que alguns tipos de mídia, como imagens de story por push e GIFs, não são compatíveis, pois não podem ser renderizados como uma notificação no macOS.

### Apple Intelligence

O [Apple Intelligence](https://developer.apple.com/documentation/Updates/Apple-Intelligence) já está disponível para dispositivos com iOS 18.1 e posterior.

Como usuário da Braze, o novo recurso mais importante que você deve conhecer são os [resumos de notificação](https://support.apple.com/en-us/108781), que usam o processamento no dispositivo para agrupar e gerar automaticamente resumos de texto para notificações por push relacionadas enviadas de um único app. Os usuários finais podem tocar para expandir um resumo e visualizar cada notificação por push como foi enviada originalmente.

Devido à forma como esses resumos são gerados, você não terá controle sobre o comportamento específico deles ou sobre o texto gerado. No entanto, isso não afetará nenhum recurso de análise de dados ou relatórios, como o rastreamento de cliques em push.

![Exemplo de captura de tela de um resumo de pré-visualização de notificação por push.]({% image_buster /assets/img/apple/apple_intelligence/notification_preview_summary.png %})