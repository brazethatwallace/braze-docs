---
nav_title: Guia de atualização do iOS 17
article_title: Guia de atualização do iOS 17
page_order: 7
platform:
  - iOS
description: "Este artigo aborda insights sobre a versão do iOS 17 para ajudar você a fazer upgrade do seu SDK or kit de desenvolvimento de software sem problemas."
hidden: true
noindex: true
---

# Guia de atualização do iOS 17 {#ios-17-upgrade-guide}

> Quer saber como a Braze está se preparando para o próximo lançamento do iOS? Este artigo resume nossos insights sobre o lançamento do iOS 17 para ajudar você a criar uma experiência perfeita para você e seus usuários.

## Compatibilidade com iOS 17 e Xcode 15 {#ios-17-and-xcode-15-compatibility}

O Braze Swift SDK or kit de desenvolvimento de software e o Objective-C SDK or kit de desenvolvimento de software são compatíveis com versões anteriores do Xcode 14 e do Xcode 15 e com dispositivos iOS 17.

## Alterações no iOS 17 {#changes-in-ios-17}

### Rastreamento de links e remoção de parâmetros UTM {#link-tracking-and-utm-parameter-stripping}

Uma das mudanças importantes no iOS 17 é o bloqueio de parâmetros UTM no Safari. Os parâmetros UTM são trechos de código adicionados aos URLs, frequentemente usados em campanhas de marketing para medir a eficácia de e-mails, SMS e outros canais de envio de mensagens.

Essa alteração não afeta o rastreamento de cliques por e-mail da Braze e os envios de encurtamento de links por SMS.

### Transparência no rastreamento de aplicativos {#app-tracking-transparency}

A Apple anunciou seu compromisso de expandir o escopo do [Ad Tracking Transparency (ATT)](https://support.apple.com/en-us/HT212025), que permite aos usuários controlar se um app pode acessar sua atividade em apps e sites pertencentes a outras empresas. A versão do iOS 17 contém dois recursos importantes da ATT: manifestos de privacidade e assinatura de código.

#### Manifestos de privacidade {#privacy-manifests}

A Apple agora exige um arquivo de manifesto de privacidade que descreva o motivo pelo qual seu app e os SDKs de terceiros coletam dados, juntamente com seus métodos de coleta de dados. A partir do iOS 17.2, a Apple bloqueará todos os endpoints de rastreamento declarados em seu app até que o usuário final aceite o prompt da ATT.

A Braze lançou seu próprio manifesto de privacidade, juntamente com novas APIs flexíveis que redirecionam automaticamente os dados de rastreamento declarados para endpoints dedicados `-tracking`. Para saber mais, consulte o [manifesto de privacidade da Braze]({{site.baseurl}}/developer_guide/analytics/managing_data_collection?sdktab=swift#swift_privacy-manifest).

#### Assinatura de código {#code-signing}

A assinatura de código permite que os desenvolvedores que usam um SDK or kit de desenvolvimento de software de terceiros em seu aplicativo validem que o mesmo desenvolvedor o assinou em versões anteriores no Xcode.

### SDK or kit de desenvolvimento de software da Braze e privacidade {#braze-sdk-and-privacy}

A Apple também anunciou que divulgará uma lista de SDKs de terceiros considerados "impactantes para a privacidade" no final de 2023. A expectativa é que esses SDKs tenham um impacto especialmente alto na privacidade do usuário, segundo a Apple.

Ao contrário dos SDKs de rastreamento tradicionais, projetados para monitorar usuários em vários sites e aplicativos, o SDK or kit de desenvolvimento de software da Braze se concentra no envio de mensagens com dados primários e nas experiências dos usuários.

Embora não esperemos que o SDK or kit de desenvolvimento de software da Braze seja incluído nessa lista, pretendemos monitorar essa situação de perto e lançar as atualizações necessárias.