---
nav_title: Exemplos de aplicativos
article_title: Exemplos de aplicativos para iOS
platform: iOS
page_order: 9
description: "Este artigo de referência aborda os apps de amostra do iOS."

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Exemplos de aplicativos {#sample-apps}

Os SDKs da Braze vêm com aplicativos de amostra no repositório para sua conveniência. Cada um desses apps é totalmente compilável, portanto, você pode testar os recursos da Braze e implementá-los em seus próprios aplicativos. Testar o comportamento em seu próprio aplicativo em comparação com o comportamento esperado e as jornadas de código nos aplicativos de amostra é uma excelente maneira de depurar quaisquer problemas que você possa encontrar.

## Criando aplicativos de teste {#building-test-applications}
Vários aplicativos de teste estão disponíveis no [repositório GitHub do SDK or kit de desenvolvimento de software para iOS](https://github.com/appboy/appboy-ios-sdk). Siga estas instruções para compilar e executar nossos aplicativos de teste.

1. Crie um novo [espaço de trabalho]({{site.baseurl}}/user_guide/get_started/workspaces) e anote a chave de API or interface de programação do aplicativo (API) do identificador do app.
2. Insira sua chave de API or interface de programação do aplicativo (API) no campo apropriado no arquivo `AppDelegate.m`.

As notificações por push para o aplicativo de teste do iOS exigem configuração adicional. Consulte nossa [integração de push para iOS]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) para mais detalhes.