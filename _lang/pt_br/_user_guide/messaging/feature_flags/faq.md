---
nav_title: FAQ
article_title: Perguntas frequentes
page_order: 50
description: "Esta página fornece respostas para perguntas frequentes sobre Feature Flags."
tool: Feature Flags
platform:
  - iOS
  - Android
  - Web
---

# Perguntas frequentes {#frequently-asked-questions}

> Este artigo fornece respostas para algumas perguntas frequentes sobre Feature Flags.

## Funcionalidade e suporte {#functionality-and-support}

### Em quais plataformas as Feature Flags da Braze são compatíveis? {#platforms}

A Braze oferece suporte a Feature Flags nas plataformas iOS, Android e Web com os seguintes requisitos mínimos de versão do SDK:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

Precisa de suporte em outras plataformas? Envie um e-mail para nossa equipe: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### Qual é o nível de esforço envolvido na implementação de uma Feature Flag? {#level-of-effort}

Uma Feature Flag pode ser criada e integrada em poucos minutos.

A maior parte do esforço estará relacionada à sua equipe de engenharia construindo a nova funcionalidade que você planeja lançar. Mas quando se trata de adicionar uma Feature Flag, é tão simples quanto uma instrução `IF`/`ELSE` no código do seu app ou site:

{% tabs %}
{% tab JavaScript %}

```javascript
import { getFeatureFlag } from "@braze/web-sdk";

if (getFeatureFlag("new_shopping_cart").enabled) {
    // Show the new homepage your team has built
}
else {
    // Show the old homepage
}
```

{% endtab %}
{% tab Java %}

```java
if (braze.getFeatureFlag("new_shopping_cart").getEnabled()) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% tab KOTLIN %}

```kotlin
if (braze.getFeatureFlag("new_shopping_cart")?.enabled == true) {
  // Show the new homepage your team has built
} else {
  // Show the old homepage
}
```

{% endtab %}
{% endtabs %}

### Como as Feature Flags podem beneficiar equipes de marketing? {#marketing-teams}

Equipes de marketing podem usar Feature Flags para coordenar anúncios de produtos (como e-mails de lançamento de produto) quando uma funcionalidade está ativada apenas para uma pequena porcentagem de usuários.

Por exemplo, com as Feature Flags da Braze, você pode lançar um novo programa de fidelidade para 10% dos usuários no seu app e enviar um e-mail, push ou outro envio de mensagens para esses mesmos 10% de usuários ativados usando a etapa Feature Flag do Canvas.

### Como as Feature Flags podem beneficiar equipes de produto? {#product-teams}

Equipes de produto podem usar Feature Flags para realizar lançamentos graduais ou soft launches de novas funcionalidades, monitorando indicadores-chave de desempenho e feedback dos clientes antes de disponibilizar para todos os usuários.

Equipes de produto podem usar [propriedades de Feature Flags]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#properties) para preencher remotamente conteúdo em um app, como deep links, textos, imagens ou outro conteúdo dinâmico.

Usando a etapa Feature Flag do Canvas, equipes de produto também podem executar um teste A/B para medir como uma nova funcionalidade impacta as taxas de conversão em comparação com usuários que não têm a funcionalidade ativada.

### Como as Feature Flags podem beneficiar equipes de engenharia? {#engineering-teams}

Equipes de engenharia podem usar Feature Flags para reduzir o risco inerente ao lançamento de novas funcionalidades e evitar a correria de implementar correções de código no meio da madrugada.

Ao lançar novo código oculto por trás de uma Feature Flag, sua equipe pode ativar ou desativar a funcionalidade remotamente pelo dashboard da Braze, evitando a demora de publicar novo código ou esperar pela aprovação de uma atualização na loja de apps.

## Lançamentos de funcionalidades e direcionamento {#feature-rollouts-and-targeting}

### Uma Feature Flag pode ser lançada apenas para um grupo específico de usuários? {#target-users}

Sim, crie um Segment na Braze que direcione usuários específicos — por endereço de e-mail, `user_id` ou qualquer outro atributo nos perfis de usuário. Em seguida, implante a Feature Flag para 100% desse Segment.

### Como o ajuste da porcentagem de lançamento afeta os usuários que já foram incluídos no grupo ativado? {#random-buckets}

Os lançamentos de Feature Flags permanecem consistentes para os usuários entre dispositivos e sessões.

- Quando uma Feature Flag é lançada para 10% de usuários aleatórios, esses 10% permanecerão ativados durante toda a vida útil dessa Feature Flag.
- Se você aumentar o lançamento de 10% para 20%, os mesmos 10% permanecerão ativados, e mais 10% adicionais de usuários serão incluídos no grupo ativado.
- Se você reduzir o lançamento de 20% para 10%, apenas os 10% originais de usuários permanecerão ativados.

Essa estratégia ajuda a garantir que os usuários tenham uma experiência consistente no seu app e não fiquem alternando entre estados ao longo das sessões. Claro, desativar uma funcionalidade para 0% removerá todos os usuários da Feature Flag, o que é útil se você descobrir um bug ou precisar desativar a funcionalidade completamente.

## Tópicos técnicos {#technical-topics}

### Feature Flags podem ser usadas para controlar quando o SDK da Braze é inicializado? {#initialization}

Não, o SDK precisa ser inicializado para baixar e sincronizar as Feature Flags do usuário atual. Isso significa que você não pode usar Feature Flags para limitar quais usuários são criados ou rastreados na Braze.

### Com que frequência o SDK atualiza as Feature Flags? {#refresh-frequency}

As Feature Flags são atualizadas no início da sessão e ao trocar de usuário ativo. As Feature Flags também podem ser atualizadas manualmente usando o [método de atualização]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#refreshing) do SDK. As atualizações de Feature Flags têm um limite de taxa de uma vez a cada cinco minutos (sujeito a alterações).

Tenha em mente que boas práticas de dados recomendam não atualizar Feature Flags com muita frequência (com possível limitação de taxa se isso acontecer). Portanto, o ideal é atualizar apenas antes de um usuário interagir com novas funcionalidades ou periodicamente no app, se necessário.

### As Feature Flags ficam disponíveis enquanto o usuário está offline? {#offline}

Sim, após as Feature Flags serem atualizadas, elas são armazenadas localmente no dispositivo do usuário e podem ser acessadas offline.

### O que acontece se as Feature Flags forem atualizadas no meio de uma sessão? {#listen-for-updates}

As Feature Flags podem ser atualizadas no meio de uma sessão. Existem cenários em que você pode querer atualizar seu app se determinadas variáveis ou sua configuração mudarem. Existem outros cenários em que você pode não querer atualizar seu app, para evitar uma mudança brusca na forma como sua interface é renderizada.

Para controlar isso, [escute atualizações]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#updates) das Feature Flags e determine se deve re-renderizar seu app com base em quais Feature Flags foram alteradas.

### Por que os usuários do meu Grupo de controle global não estão recebendo experimentos de Feature Flags? {#why-arent-users-in-my-global-control-group-receiving-feature-flags-experiments}

Você não pode ativar Feature Flags para usuários no seu [Grupo de controle global]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts). Isso significa que os usuários no seu Grupo de controle global também não podem participar de experimentos de Feature Flags.

## Mais perguntas? {#additional-questions}

Tem perguntas ou feedback? Envie um e-mail para nossa equipe: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).