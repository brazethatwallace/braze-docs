---
nav_title: Testes de unidade (opcional)
article_title: Testes de unidade de notificações por push para iOS
platform: iOS
page_order: 29.5
description: "Este artigo de referência descreve como implementar testes de unidade opcionais para sua implementação push do iOS."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Testes de unidade {#unit-tests}

Este guia opcional descreve como implementar alguns testes de unidade que verificarão se o app delegate segue corretamente as etapas descritas em nossas [instruções de integração push]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration).

Se todos os testes forem aprovados, em geral, isso significa que a parte baseada em código da sua configuração push está funcionando. Se um teste falhar, isso pode significar que você seguiu incorretamente uma etapa ou pode ser resultado de uma personalização válida que não se alinha precisamente com nossas instruções padrão.

De qualquer forma, essa pode ser uma abordagem útil para verificar se você seguiu as etapas de integração e para ajudar a monitorar quaisquer regressões.

## Etapa 1: Criação de um target de testes de unidade {#step-1-creating-a-unit-tests-target}

Pule esta etapa se o projeto do seu app no Xcode já contiver um pacote de teste de unidade (Unit Testing Bundle).

No projeto do seu app, acesse o menu **File > New > Target** e adicione um novo "Unit Testing Bundle". Esse pacote pode usar Objective-C ou Swift e ter qualquer nome. Defina o "Target to be Tested" como o target principal do seu app.

## Etapa 2: Adicione o SDK or kit de desenvolvimento de software da Braze aos seus testes de unidade {#step-2-add-the-braze-sdk-to-your-unit-tests}

Usando o mesmo método que você usou inicialmente para [instalar o SDK or kit de desenvolvimento de software da Braze]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview), confira se a mesma instalação do SDK or kit de desenvolvimento de software também está disponível para o target dos seus testes de unidade. Por exemplo, usando o CocoaPods:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
  end
end
```

## Etapa 3: Adicione o OCMock aos seus testes de unidade {#step-3-add-ocmock-to-your-unit-tests}

Adicione o [OCMock](https://ocmock.org/) ao seu target de teste por meio do CocoaPods, do Carthage ou de sua biblioteca estática. Por exemplo, usando o CocoaPods:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
    pod 'OCMock'
  end
end
```

## Etapa 4: Concluir a instalação das bibliotecas adicionadas {#step-4-finish-installing-the-added-libraries}

Conclua a instalação do SDK or kit de desenvolvimento de software da Braze e do OCMock. Por exemplo, usando o CocoaPods, navegue até o diretório do seu projeto de app do Xcode no terminal e execute o seguinte comando:

```
pod install
```

Nesse ponto, você deve conseguir abrir o espaço de trabalho do projeto Xcode criado pelo CocoaPods.

## Etapa 5: Adição de testes push {#step-5-adding-push-tests}

Crie um novo arquivo Objective-C no target dos seus testes de unidade.

Se o target dos testes de unidade estiver em Swift, o Xcode poderá perguntar: "Would you like to configure an Objective-C bridging header?" O bridging header é opcional, portanto, você pode clicar em **Don't Create** e ainda assim executar esses testes de unidade com êxito.

Adicione o conteúdo do app de exemplo HelloSwift [`AppboyPushUnitTests.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftTests/AppboyPushUnitTests.m) ao novo arquivo.

## Etapa 6: Executar o conjunto de testes {#step-6-run-test-suite}

Execute os testes de unidade do seu app. Essa pode ser uma etapa de verificação única ou pode ser incluída indefinidamente no seu conjunto de testes para ajudar a detectar quaisquer regressões.