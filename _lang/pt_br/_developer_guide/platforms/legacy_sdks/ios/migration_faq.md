---
nav_title: FAQ de migração
article_title: FAQ de migração do SDK or kit de desenvolvimento de software para iOS
platform: iOS
page_order: 12
description: "Esta página responde a perguntas frequentes sobre a migração do SDK or kit de desenvolvimento de software Appboy para iOS (Objective-C) para o SDK or kit de desenvolvimento de software Swift da Braze."
noindex: true
---

# FAQ de migração do SDK or kit de desenvolvimento de software para iOS {#ios-sdk-migration-faq}

> Esta página responde a perguntas frequentes sobre a migração do SDK or kit de desenvolvimento de software Appboy legado para iOS (também conhecido como SDK or kit de desenvolvimento de software Objective-C) para o SDK or kit de desenvolvimento de software Swift da Braze.

{% multi_lang_include deprecations/objective-c.md %}

## Suporte de versão e fim de vida útil {#version-support-and-end-of-life}

### O Appboy iOS SDK or kit de desenvolvimento de software 4.7.0 chegou ao fim de vida útil? {#is-appboy-ios-sdk-470-end-of-life}

Sim, o Appboy iOS SDK or kit de desenvolvimento de software 4.7.0 (e todas as versões 4.x) chegou ao fim de vida útil. Nenhuma correção de segurança ou correção crítica de bug é fornecida. Embora o envio de mensagens e a análise de dados continuem funcionando normalmente, a versão 4.7.0 deve ser tratada como sem suporte do ponto de vista de segurança.

### Qual é a versão mínima do Swift SDK or kit de desenvolvimento de software para suporte em produção? {#what-is-the-minimum-swift-sdk-version-for-production-support}

As versões principais atuais (16.x e posteriores) são o alvo de suporte contínuo, correções de bugs e novos recursos. Versões secundárias mais antigas podem não receber manutenção contínua.

## Bibliotecas de compatibilidade {#compatibility-libraries}

### BrazeKitCompat e BrazeUICompat são compatíveis para uso em produção no Swift SDK or kit de desenvolvimento de software 17.x? {#are-brazekitcompat-and-brazeuicompat-supported-for-production-use-on-swift-sdk-17x}

Sim, `BrazeKitCompat` e `BrazeUICompat` são compatíveis para uso em produção durante a migração. Elas são posicionadas como um "ponto de passagem" de migração mínima para ajudar você a migrar do SDK or kit de desenvolvimento de software do Appboy para o Swift SDK or kit de desenvolvimento de software com o mínimo de alterações no código, e não como uma solução de longo prazo. Embora sejam formalmente compatíveis e ainda recebam correções de bugs, a intenção é que eventualmente você migre dessas bibliotecas de compatibilidade para as APIs modernas do Swift SDK or kit de desenvolvimento de software.

### Quando BrazeKitCompat e BrazeUICompat serão removidas? {#when-will-brazekitcompat-and-brazeuicompat-be-removed}

A equipe do Swift SDK or kit de desenvolvimento de software planeja descontinuar a biblioteca `BrazeKitCompat`, mas nenhum cronograma específico foi anunciado ainda. É recomendável planejar a migração completa para as APIs modernas do Swift SDK or kit de desenvolvimento de software (`BrazeKit`, `BrazeUI`) em vez de depender das bibliotecas de compatibilidade indefinidamente.

## Inicialização atrasada {#delayed-initialization}

### Posso atrasar a inicialização do SDK or kit de desenvolvimento de software até depois do consentimento do usuário? {#can-i-delay-sdk-initialization-until-after-user-consent}

Sim. O Swift SDK or kit de desenvolvimento de software suporta inicialização atrasada, o que é útil para apps que precisam aguardar o consentimento do usuário antes de iniciar o SDK or kit de desenvolvimento de software. Chame `Braze.prepareForDelayedInitialization()` (opcionalmente com um parâmetro `analyticsBehavior`) no início de `application(_:didFinishLaunchingWithOptions:)`, e depois inicialize o SDK or kit de desenvolvimento de software chamando o inicializador padrão da Braze após o consentimento ser obtido.

Para detalhes de implementação, consulte [Configurar a inicialização atrasada]({{site.baseurl}}/developer_guide/sdk_integration/?sdktab=swift#swift_step-2-set-up-delayed-initialization-optional).

### Qual é a versão mínima do Swift SDK or kit de desenvolvimento de software necessária para a inicialização atrasada? {#what-is-the-minimum-swift-sdk-version-required-for-delayed-initialization}

O Swift SDK or kit de desenvolvimento de software 11.2.0 é a versão mínima para inicialização atrasada. A robustez de push e deep link para inicialização atrasada foi aprimorada na versão 14.1.0. O Swift SDK or kit de desenvolvimento de software 17.0.0 está bem acima desses dois limites.

### O que acontece com os eventos recebidos antes da inicialização do SDK or kit de desenvolvimento de software? {#what-happens-to-events-received-before-the-sdk-is-initialized}

Quando o SDK or kit de desenvolvimento de software é inicializado, os itens na fila são processados. No entanto, o comportamento varia por canal:

| Canal | Comportamento antes da inicialização |
|-------|---------------------------------------|
| Tokens por push | Enfileirados; processados na inicialização |
| Aberturas/análise de push | Enfileirados por padrão (configurável para descartar via `analyticsBehavior`) |
| Deep links | Enfileirados; processados na inicialização |
| In-App Messages | Não armazenados em buffer antes da inicialização; exigem que o SDK or kit de desenvolvimento de software esteja em execução |
| Content Cards | Não armazenados em buffer antes da inicialização; sincronizados do servidor após a inicialização |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

{% alert important %}
In-App Messages e Content Cards recebidos antes da inicialização não têm garantia de entrega. Certifique-se de que o SDK or kit de desenvolvimento de software esteja inicializado antes de tentar exibir esses canais.
{% endalert %}

## Pacotes de recursos e integração com SPM {#resource-bundles-and-spm-integration}

### Por que estou vendo um erro de tempo de execução sobre `braze-swift-sdk_BrazeUI.bundle` ausente? {#why-am-i-seeing-a-runtime-error-about-missing-braze-swift-sdk_brazeuibundle}

Isso não é um bug conhecido do SDK or kit de desenvolvimento de software e provavelmente se deve a uma configuração incorreta da integração. A partir do Swift SDK or kit de desenvolvimento de software 12.0.0, os XCFrameworks estáticos incluem recursos diretamente, em vez de depender de pacotes de recursos externos.

### Quais são os requisitos de SPM/Xcode/archive para incorporação de recursos? {#what-are-the-spmxcodearchive-requirements-for-resource-embedding}

A partir do Swift SDK or kit de desenvolvimento de software 12.0.0, você deve selecionar **Embed & Sign** para os XCFrameworks da Braze nas configurações do seu projeto no Xcode — isso se aplica tanto às variantes estáticas quanto às dinâmicas. Essa é a causa raiz mais comum para erros de pacote ausente durante o archive ou o lançamento.

### Como substituir pacotes de recursos para sistemas de build não padrão? {#how-do-i-override-resource-bundles-for-non-standard-build-systems}

Para sistemas de build não padrão (Tuist, Bazel, Buck, CI), use as APIs de substituição aprovadas:

- `BrazeKit.overrideResourcesBundle` (observe o plural "Resources")
- `BrazeUI.overrideResourcesBundle` (observe o plural "Resources")

O singular `overrideResourceBundle` foi descontinuado no Swift SDK or kit de desenvolvimento de software 8.1.0 e não deve ser usado.

## Identidade do usuário e tokens por push {#user-identity-and-push-tokens}

### Existe uma lista de verificação para preservar perfis, associações de dispositivos e tokens por push? {#is-there-a-validation-checklist-for-preserving-profiles-device-associations-and-push-tokens}

Não existe uma lista de verificação oficial específica para migração na documentação. Recomendamos que você realize as seguintes etapas de validação:

1. Confirme que `registerDeviceToken` ou a automação de push está configurada corretamente após a migração.
2. Verifique a contagem de usuários registrados para push no dashboard antes e depois do lançamento.
3. Faça uma verificação pontual de alguns IDs externos específicos para confirmar que as associações de dispositivos permanecem intactas.

### O `changeUser` garante que os tokens por push acompanham o novo usuário? {#does-changeuser-guarantee-that-push-tokens-follow-the-new-user}

Não há garantia explícita documentada por escrito. No entanto, a intenção do design é que os tokens por push acompanhem o dispositivo, não o usuário. Chamar `changeUser` deve reassociar o token de dispositivo existente ao novo perfil de usuário. Você deve testar o `changeUser`, verificar no dashboard e confirmar que o token aparece no novo perfil antes de fazer o lançamento em massa.