---
nav_title: Swift Package Manager
article_title: Integração do Swift Package Manager para iOS
platform: iOS
page_order: 3
description: "Este tutorial cobre a instalação do SDK da Braze usando o Swift Package Manager para iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Integração do Swift Package Manager {#swift-package-manager-integration}

Instalar o iOS SDK via [Swift Package Manager](https://swift.org/package-manager/) (SPM) automatiza a maior parte do processo de instalação para você. Antes de começar este processo, certifique-se de usar o Xcode 12 ou superior.

{% alert note %}
tvOS não está disponível atualmente via Swift Package Manager.
{% endalert %}

## Etapa 1: Adicionando a dependência ao seu projeto {#step-1-adding-the-dependency-to-your-project}

### Importar versão do SDK {#import-sdk-version}

Abra seu projeto e navegue até as configurações do seu projeto. Selecione a guia **Swift Packages** e clique no botão adicionar <i class="fas fa-plus" aria-label="Adicionar"></i> abaixo da lista de pacotes.

![Configurações do projeto no Xcode com a guia Swift Packages selecionada.]({% image_buster /assets/img/ios/spm/swiftpackages.png %})

Ao importar a versão `3.33.1` do SDK ou posterior, insira a URL do nosso repositório de SDK para iOS (`https://github.com/braze-inc/braze-ios-sdk`) no campo de texto e clique em **Next**.

Para versões `3.29.0` até `3.32.0`, use a URL `https://github.com/Appboy/Appboy-ios-sdk`.

![Diálogo de adição de dependência de pacote no Xcode para a URL do repositório do SDK iOS da Braze.]({% image_buster /assets/img/ios/spm/importsdk_example.png %})

Na próxima tela, selecione a versão do SDK e clique em **Next**. As versões `3.29.0` e posteriores são compatíveis com o Swift Package Manager.

![Seleção de versão do pacote no Xcode para o SDK iOS da Braze.]({% image_buster /assets/img/ios/spm/select_version.png %})

### Selecionar pacotes {#select-packages}

Selecione o pacote que melhor atende às suas necessidades e clique em **Finish**. Certifique-se de selecionar `AppboyKit` ou `AppboyUI`. Incluir ambos os pacotes pode levar a um comportamento indesejado:

- `AppboyUI`
  - Mais adequado se você planeja usar os componentes de UI fornecidos pela Braze.
  - Inclui `AppboyKit` automaticamente.
- `AppboyKit`
  - Mais adequado se você não precisar usar nenhum dos componentes de UI fornecidos pela Braze (por exemplo, Content Cards, mensagens no app, etc.).
- `AppboyPushStory`
  - Inclua este pacote se você integrou Push Stories no seu app. Isso é suportado a partir da versão `3.31.0`.
  - No menu suspenso em `Add to Target`, selecione seu alvo `ContentExtension` em vez do alvo do seu app principal.

![Tela de adição de pacote no Xcode selecionando os alvos de biblioteca do SDK da Braze.]({% image_buster /assets/img/ios/spm/add_package.png %})

## Etapa 2: Configurando seu projeto {#step-2-configuring-your-project}

Em seguida, navegue até as **configurações de build** do seu projeto e adicione a flag `-ObjC` à configuração **Other Linker Flags**. Essa flag deve ser adicionada e quaisquer [erros](https://developer.apple.com/library/archive/qa/qa1490/_index.html) resolvidos para integrar o SDK corretamente.

![Configurações de build do Xcode mostrando o campo Other Linker Flags.]({% image_buster /assets/img/ios/spm/buildsettings.png %})

{% alert note %}
Se você não adicionar a flag `-ObjC`, partes da API podem ficar ausentes e o comportamento será indefinido. Você pode encontrar erros inesperados, como "unrecognized selector sent to class", falhas no aplicativo e outros problemas.
{% endalert %}

## Etapa 3: Editando o esquema do alvo {#step-3-editing-the-targets-scheme}
{% alert important %}
Se você estiver usando o Xcode 12.5 ou mais recente, pule esta etapa.
{% endalert %}

Se você estiver usando o Xcode 12.4 ou anterior, edite o esquema do alvo incluindo o pacote Appboy (**Product > Scheme > Edit Scheme** no menu):
1. Expanda o menu **Build** e selecione **Post-actions**. Pressione o botão de mais (+) e selecione **New Run Script Action**.
2. No menu suspenso **Provide build settings from**, selecione o alvo do seu app.
3.  Copie este script no campo aberto:
```sh
# iOS
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Appboy.bundle/appboy-spm-cleanup.sh"
# macOS (if applicable)
bash "$BUILT_PRODUCTS_DIR/Appboy_iOS_SDK_AppboyKit.bundle/Contents/Resources/Appboy.bundle/appboy-spm-cleanup.sh"
```

![Menu Build Phases do Xcode para adicionar uma fase de build com script de execução.]({% image_buster /assets/img/ios/spm/swiftmanager_buildmenu.png %})

## Próximos passos {#next-steps}

Siga as instruções para [concluir a integração]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/completing_integration).