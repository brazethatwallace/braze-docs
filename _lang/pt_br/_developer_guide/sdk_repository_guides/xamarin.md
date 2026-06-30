---
nav_title: SDK .NET MAUI (Xamarin)
article_title: Guia do repositório do SDK .NET MAUI (Xamarin)
page_order: 10
description: "Referência do README do SDK .NET MAUI (Xamarin) da Braze, espelhada do GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
## Sobre o SDK .NET MAUI (Xamarin) da Braze {#about-the-braze-net-maui-xamarin-sdk}

O SDK .NET MAUI (Xamarin) da Braze ajuda você a integrar recursos de envio de mensagens, análise de dados e engajamento de usuários da Braze ao seu aplicativo.

Para começar, consulte os seguintes recursos:

- [Guia do usuário da Braze]({{site.baseurl}}/user_guide/introduction)
- [Guia do desenvolvedor da Braze]({{site.baseurl}}/developer_guide/sdk_integration?sdktab=xamarin)

## Componentes {#components}

O formato deste repositório é o de um componente Xamarin: dentro de `appboy-component`, você encontrará os diretórios `src`,
`libs`, `component`, `nuget` e `samples`. `libs`, `src` e `samples` contêm dois diretórios cada, um para Android e outro para iOS. Os diretórios
contêm:

- `libs`: as DLLs compiladas de bindings para os SDKs da Braze.
- `src`: os projetos de bindings Xamarin que geraram as DLLs encontradas na pasta libs.
- `samples`: aplicativos Xamarin que mostram como usar os bindings para acessar o conjunto de recursos da Braze.
- `nuget`: arquivos Nuspec para nossos pacotes NuGet Xamarin.

## Versionamento {#versioning}

### Bindings nativos {#native-bindings}

| Nome do arquivo de binding                 | Frameworks Xamarin compatíveis                            | Framework nativo da Braze                           | Versão do SDK Xamarin da Braze |
| ------------------------------------------ | --------------------------------------------------------- | --------------------------------------------------- | ------------------------------ |
| `BrazeAndroidBinding.sln`                  | .NET 9+                                                   | Android SDK 41.0.0+                                 | 9.0.0+                         |
| `AppboyPlatform.XamarinAndroidBinding.sln` | Xamarin.Android,<br/>Xamarin.Forms,<br/>.NET 5 e anterior  | Android SDK 23.3.0 e anterior                       | 1.26.0 e anterior              |
| `BrazeiOSBinding.sln`                      | .NET 9+                                                   | Swift SDK 14.0.1+                                   | 9.0.0+                         |
| `AppboyPlatformXamariniOSBinding.sln`      | Xamarin.iOS,<br/>Xamarin.Forms,<br/>.NET 5 e anterior      | `Appboy_iOS_SDK.framework` versão 4.4.1 e anterior  | 1.27.0 e anterior              |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Bindings nativos" }

### Xamarin e Xamarin.Forms {#xamarin-xamarinforms}

Em 1º de maio de 2024, a [Microsoft anunciou o fim do suporte para Xamarin e Xamarin.Forms](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin).

O SDK da Braze deixou de oferecer suporte ao Xamarin e Xamarin.Forms a partir da versão `4.0.0` e adicionou suporte ao [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/what-is-maui).

## Dúvidas? {#questions}

Se você tiver dúvidas, entre em contato com [support@braze.com](mailto:support@braze.com).
<!-- END GENERATED README CONTENT -->

Para detalhes do repositório e projetos de exemplo, consulte [https://github.com/braze-inc/braze-xamarin-sdk](https://github.com/braze-inc/braze-xamarin-sdk).