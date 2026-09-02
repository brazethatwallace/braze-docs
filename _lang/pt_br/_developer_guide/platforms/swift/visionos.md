---
nav_title: Suporte ao visionOS
article_title: Suporte ao visionOS
page_order: 7.2
platform:
  - iOS
description: "Este artigo aborda os recursos compatíveis com o visionOS."
---

# Suporte ao visionOS {#visionos-support}

> A partir do [Braze Swift SDK or kit de desenvolvimento de software 8.0.0](https://github.com/braze-inc/braze-swift-sdk/blob/main/CHANGELOG.md#800), você pode usar a Braze com o [visionOS](https://developer.apple.com/visionos/), a plataforma de computação espacial da Apple para o Apple Vision Pro. Para ver um exemplo de app do visionOS usando a Braze, consulte [Apps de exemplo]({{site.baseurl}}/developer_guide/references?tab=swift).

## Recursos totalmente compatíveis {#fully-supported-features}

A maioria dos recursos disponíveis no iOS também está disponível no visionOS, incluindo:

- Análise de dados (sessões, eventos personalizados, compras, etc.)
- Envio de mensagens no app (modelos de dados e UI)
- Content Cards (modelos de dados e UI)
- Notificações por push (visíveis ao usuário com botões de ação e notificações silenciosas)
- Feature Flags
- Análise de dados de local

## Recursos parcialmente compatíveis {#partially-supported-features}

Alguns recursos são compatíveis apenas parcialmente com o visionOS, mas é provável que a Apple resolva essas questões no futuro:

- Notificações por push avançadas
  - Há suporte para imagens.
  - GIFs e vídeos exibem a miniatura de pré-visualização, mas não podem ser reproduzidos.
  - Não há suporte para reprodução de áudio.
- Push Stories
  - Há suporte para rolagem e seleção da página do Push Story.
  - Não há suporte para a navegação entre as páginas do Push Story usando **Next**.

## Recursos incompatíveis {#unsupported-features}

- Não há suporte para o monitoramento de geofences. A Apple não disponibilizou as APIs de Core Location para monitoramento de região no visionOS.
- Não há suporte para Live Activities. No momento, o ActivityKit está disponível apenas para iOS e iPadOS.