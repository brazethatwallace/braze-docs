---
nav_title: SDK .NET MAUI (Xamarin)
article_title: Guia do repositório do SDK .NET MAUI (Xamarin)
page_order: 10
description: "Referência do README do SDK .NET MAUI (Xamarin) da Braze, espelhada do GitHub."
---

<!-- BEGIN GENERATED README CONTENT -->
# Guia do repositório do SDK .NET MAUI (Xamarin) {#net-maui-xamarin-sdk-repository-guide}

## Sobre o SDK Braze .NET MAUI (Xamarin) {#about-the-braze-net-maui-xamarin-sdk}

O SDK Braze .NET MAUI (Xamarin) ajuda você a integrar recursos de envio de mensagens, análise de dados e engajamento de usuários da Braze ao seu app.

Para começar, consulte os seguintes recursos:

- [Guia do Usuário da Braze](https://www.braze.com/docs/user_guide/introduction/)
- [Guia do Desenvolvedor da Braze](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=xamarin)

## Componentes {#components}

O formato deste repositório é o de um componente Xamarin: em `appboy-component`, você encontrará os diretórios `src`,
`libs`, `component`, `nuget` e `samples`. `libs`, `src` e `samples` contêm dois diretórios cada, um para Android e outro para iOS. Os diretórios
contêm:

- `libs`: As DLLs de bindings compiladas para os SDKs da Braze.
- `src`: Os projetos de bindings Xamarin que geraram as DLLs encontradas na pasta `libs`.
- `samples`: Apps Xamarin que mostram como usar os bindings para acessar o conjunto de recursos da Braze.
- `nuget`: Arquivos Nuspec para nossos pacotes NuGet do Xamarin.

## Versionamento {#versioning}

### Bindings nativos {#native-bindings}

A tabela a seguir lista os frameworks compatíveis e as versões nativas do framework da Braze para cada binding Xamarin.

| Nome do arquivo de binding                 | Frameworks Xamarin compatíveis                            | Framework nativo da Braze                           | Versão do SDK Braze Xamarin |
| ------------------------------------------ | --------------------------------------------------------- | --------------------------------------------------- | --------------------------- |
| `BrazeAndroidBinding.sln`                  | .NET 9+                                                   | Android SDK 43.1.1+                                 | 10.0.0+                     |
| `AppboyPlatform.XamarinAndroidBinding.sln` | Xamarin.Android,<br/>Xamarin.Forms,<br/>.NET 5 e anteriores | Android SDK 23.3.0 e anteriores                     | 1.26.0 e anteriores         |
| `BrazeiOSBinding.sln`                      | .NET 9+                                                   | Swift SDK 18.2.0+                                   | 10.0.0+                     |
| `AppboyPlatformXamariniOSBinding.sln`      | Xamarin.iOS,<br/>Xamarin.Forms,<br/>.NET 5 e anteriores   | `Appboy_iOS_SDK.framework` versão 4.4.1 e anteriores | 1.27.0 e anteriores         |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 .reset-td-br-4 aria-label="Bindings nativos" }

### Xamarin e Xamarin.Forms {#xamarin-xamarinforms}

Em 1º de maio de 2024, a [Microsoft anunciou o fim do suporte para Xamarin e Xamarin.Forms](https://dotnet.microsoft.com/en-us/platform/support/policy/xamarin).

O SDK da Braze deixou de oferecer suporte ao Xamarin e Xamarin.Forms a partir da versão `4.0.0` e adicionou suporte ao [.NET MAUI](https://learn.microsoft.com/en-us/dotnet/maui/what-is-maui).

## Dúvidas? {#questions}

Para dúvidas, entre em contato com o suporte técnico da Braze para obter assistência.
<!-- END GENERATED README CONTENT -->

Para detalhes do repositório e projetos de exemplo, consulte [https://github.com/braze-inc/braze-xamarin-sdk](https://github.com/braze-inc/braze-xamarin-sdk).