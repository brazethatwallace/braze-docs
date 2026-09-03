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

### Em quais plataformas os feature flags da Braze são suportados? {#platforms}

A Braze oferece suporte a feature flags nas plataformas iOS, Android e web com os seguintes requisitos mínimos de versão do SDK:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

Precisa de suporte em outras plataformas? Envie um e-mail para nossa equipe: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### Qual é o nível de esforço envolvido na implementação de um Feature Flag? {#level-of-effort}

Um Feature Flag pode ser criado e integrado em poucos minutos.

A maior parte do esforço estará relacionada à equipe de engenharia construindo o novo recurso que você planeja lançar. Quando se trata de adicionar um Feature Flag, é tão simples quanto uma instrução `IF`/`ELSE` no código do seu app ou website:

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

### Como os feature flags podem beneficiar as equipes de marketing? {#marketing-teams}

As equipes de marketing podem usar feature flags para coordenar anúncios de produtos (como e-mails de lançamento de produto) quando um recurso está ativado apenas para uma pequena porcentagem de usuários.

Por exemplo, com os feature flags da Braze, você pode lançar um novo programa de fidelidade para 10% dos usuários no seu app e enviar um e-mail, push ou outro envio de mensagens para esses mesmos 10% de usuários habilitados usando a etapa Feature Flag do Canvas.

### Como os feature flags podem beneficiar as equipes de produto? {#product-teams}

As equipes de produto podem usar feature flags para realizar lançamentos graduais ou soft launches de novos recursos, monitorando KPIs e feedback de clientes antes de disponibilizar para todos os usuários.

As equipes de produto podem usar [propriedades de Feature Flag]({{site.baseurl}}/developer_guide/feature_flags/create#accessing-properties) para popular remotamente conteúdo em um app, como deep links, texto, imagens ou outro conteúdo dinâmico.

Usando a etapa Feature Flag do Canvas, as equipes de produto também podem executar um teste A/B para medir como um novo recurso impacta as taxas de conversão em comparação com usuários que não têm o recurso ativado.

### Como os feature flags podem beneficiar as equipes de engenharia? {#engineering-teams}

As equipes de engenharia podem usar feature flags para reduzir o risco inerente ao lançamento de novos recursos e evitar a necessidade de implantar correções de código de última hora durante a madrugada.

Ao lançar um novo código oculto por trás de um Feature Flag, sua equipe pode ativar ou desativar o recurso remotamente a partir do dashboard da Braze, evitando o atraso de publicar novo código ou aguardar a aprovação de uma atualização na app store.

## Lançamentos de recursos e direcionamento {#feature-rollouts-and-targeting}

### Um Feature Flag pode ser lançado apenas para um grupo específico de usuários? {#target-users}

Sim, crie um Segment na Braze que direcione usuários específicos&mdash;por endereço de e-mail, `user_id` ou qualquer outro atributo nos seus perfis de usuário. Em seguida, implante o Feature Flag para 100% desse Segment.

### Como o ajuste da porcentagem de lançamento afeta usuários que já foram alocados no grupo ativado? {#random-buckets}

Os lançamentos de Feature Flag permanecem consistentes para os usuários em todos os dispositivos e sessões.

- Quando um Feature Flag é lançado para 10% de usuários aleatórios, esses 10% permanecerão ativados e persistirão durante toda a vida útil desse Feature Flag.
- Se você aumentar o lançamento de 10% para 20%, os mesmos 10% continuarão ativados, e outros 10% adicionais de usuários serão incluídos no grupo ativado.
- Se você reduzir o lançamento de 20% para 10%, apenas os 10% originais de usuários permanecerão ativados.

Essa estratégia ajuda a garantir que os usuários tenham uma experiência consistente no seu app e não fiquem alternando entre estados ao longo das sessões. É claro que desativar um recurso até 0% removerá todos os usuários do Feature Flag, o que é útil se você descobrir um bug ou precisar desativar o recurso por completo.

## Tópicos técnicos {#technical-topics}

### As Feature Flags podem ser usadas para controlar quando o SDK da Braze é inicializado? {#initialization}

Não, o SDK deve ser inicializado para baixar e sincronizar as Feature Flags para o usuário atual. Isso significa que você não pode usar Feature Flags para limitar quais usuários são criados ou rastreados na Braze.

### Com que frequência o SDK atualiza as Feature Flags? {#refresh-frequency}

As Feature Flags são atualizadas no início da sessão e ao trocar de usuário ativo. As Feature Flags também podem ser atualizadas manualmente usando o [método de atualização]({{site.baseurl}}/developer_guide/feature_flags/create#refreshing) do SDK. As atualizações de Feature Flags são limitadas a uma vez a cada cinco minutos (sujeito a alterações).

Tenha em mente que boas práticas de dados recomendam não atualizar as Feature Flags com muita frequência (com possível limitação de frequência se isso ocorrer), então o melhor é atualizar apenas antes de um usuário interagir com novos recursos ou periodicamente no app, se necessário.

### As Feature Flags estão disponíveis quando o usuário está offline? {#offline}

Sim. Depois que as Feature Flags são atualizadas, elas são armazenadas localmente no dispositivo do usuário e podem ser acessadas offline.

### O que acontece se as Feature Flags forem atualizadas no meio da sessão? {#listen-for-updates}

As Feature Flags podem ser atualizadas no meio da sessão. Há cenários em que você pode querer atualizar seu app se determinadas variáveis ou sua configuração mudarem. Há outros cenários em que talvez você não queira atualizar seu app, para evitar uma mudança brusca na forma como sua interface é renderizada.

Para controlar isso, [escute as atualizações]({{site.baseurl}}/developer_guide/feature_flags/create#updates) das Feature Flags e determine se deve re-renderizar seu app com base em quais Feature Flags foram alteradas.

### Por que os usuários do meu grupo de controle global não estão recebendo experimentos de Feature Flags? {#why-arent-users-in-my-global-control-group-receiving-feature-flags-experiments}

Você não pode ativar Feature Flags para usuários no seu [grupo de controle global]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts). Isso significa que os usuários no seu grupo de controle global também não podem fazer parte de experimentos de Feature Flag.

### A identificação de destinatários por e-mail faz parte das Feature Flags da Braze? {#is-email-based-recipient-identification-part-of-braze-feature-flags}

Não. Identificar destinatários por e-mail ao enviar uma mensagem não faz parte do produto Feature Flags desta página. As Feature Flags controlam experiências dentro do app ou no site por meio do SDK da Braze.

Envios de Campaigns e Canvas disparados por API podem incluir `email` no [objeto de destinatários]({{site.baseurl}}/api/objects_filters/recipient_object) em vez de um `external_user_id`. Quando você usa `email`, inclua `prioritization` para que a Braze possa selecionar o perfil de usuário correspondente. Essa opção de envio não está disponível em todos os espaços de trabalho.

Para o formato da requisição, consulte [POST: Enviar Campaigns usando entrega disparada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) e [POST: Enviar mensagens de Canvas usando entrega disparada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).

## Dúvidas adicionais? {#additional-questions}

Tem perguntas ou feedback? Envie um e-mail para nossa equipe: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).