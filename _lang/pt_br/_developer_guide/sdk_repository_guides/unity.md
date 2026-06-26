---
nav_title: Unity SDK
article_title: Guia do repositório do Unity SDK
page_order: 9
description: "Referência do README do Braze Unity SDK espelhada do GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## Sobre o Braze Unity SDK {#about-the-braze-unity-sdk}

O Braze Unity SDK ajuda você a integrar recursos de envio de mensagens, análise de dados e engajamento de usuários da Braze ao seu aplicativo.

Para começar, consulte os seguintes recursos:

- [Guia do Usuário da Braze]({{site.baseurl}}/user_guide/introduction/)
- [Guia do Desenvolvedor da Braze]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=unity)

## Configuração do plugin {#plugin-setup}

Antes de começar a usar a Braze em scripts Unity, você precisará importar os arquivos do plugin para o seu projeto Unity.

**Recomendado:** Os plugins para Android e iOS estão empacotados como um pacote Unity disponível para baixar na [página de lançamentos do SDK][1].

**Configuração manual do plugin:** Como alternativa, você pode copiar os plugins para o seu projeto Unity:
  1. Primeiro, clone este repositório.
  2. Se você não estiver usando nenhum outro plugin, basta copiar o diretório `Plugins` deste repositório para a pasta `Assets` do seu projeto Unity.
  3. Se você já tiver um diretório `/<your-project>/Assets/Plugins` (provavelmente porque já está usando outro plugin), copie `Plugins/Appboy/AppboyBinding.cs` para `/<your-project>/Assets/Plugins`. Em seguida, copie o conteúdo de `Plugins/iOS` e `Plugins/Android` deste repositório para `/<your-project>/Assets/Plugins/iOS` e `/<your-project>/Assets/Plugins/Android`, respectivamente.

## Configuração da integração {#integration-setup}

Para integrar a Braze ao seu aplicativo Unity, siga nossas instruções para [Integração do SDK do Unity da Braze][2].

[1]: https://github.com/braze-inc/braze-unity-sdk/releases
[2]: {{site.baseurl}}/developer_guide/sdk_integration?sdktab=unity

## Fale com o suporte {#contact}

Se você tiver dúvidas, entre em contato pelo e-mail [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

Para informações sobre o repositório e projetos de exemplo, acesse [https://github.com/braze-inc/braze-unity-sdk](https://github.com/braze-inc/braze-unity-sdk).