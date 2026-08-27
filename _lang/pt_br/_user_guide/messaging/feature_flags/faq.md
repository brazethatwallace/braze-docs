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

### Em quais plataformas os Feature Flags da Braze são suportados? {#platforms}

A Braze suporta Feature Flags nas plataformas iOS, Android e web com os seguintes requisitos mínimos de versão do SDK:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

Precisa de suporte em outras plataformas? Envie um e-mail para nossa equipe: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### Qual é o nível de esforço envolvido na implementação de um Feature Flag? {#level-of-effort}

Um Feature Flag pode ser criado e integrado em poucos minutos.

A maior parte do esforço envolvido estará relacionada à sua equipe de engenharia construindo o novo recurso que você planeja lançar. Mas quando se trata de adicionar um Feature Flag, é tão simples quanto uma instrução `IF`/`ELSE` no código do seu app ou website:

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

### Como os Feature Flags podem beneficiar equipes de marketing? {#marketing-teams}

Equipes de marketing podem usar Feature Flags para coordenar anúncios de produtos (como e-mails de lançamento de produto) quando um recurso está habilitado apenas para uma pequena porcentagem de usuários.

Por exemplo, com os Feature Flags da Braze, você pode disponibilizar um novo programa de fidelidade do cliente para 10% dos usuários do seu app e enviar um e-mail, push ou outro envio de mensagens para esses mesmos 10% de usuários habilitados usando a etapa de Feature Flag do Canvas.

### Como os Feature Flags podem beneficiar equipes de produto? {#product-teams}

Equipes de produto podem usar Feature Flags para realizar lançamentos graduais ou lançamentos suaves de novos recursos, monitorando indicadores-chave de desempenho e feedback dos clientes antes de disponibilizá-los para todos os usuários.

Equipes de produto podem usar [propriedades de Feature Flag]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#properties) para preencher remotamente conteúdo em um app, como deep links, texto, imagens ou outro conteúdo dinâmico.

Usando a etapa de Feature Flag do Canvas, equipes de produto também podem executar um teste A/B para medir como um novo recurso impacta as taxas de conversão em comparação com usuários que não têm o recurso habilitado.

### Como os Feature Flags podem beneficiar equipes de engenharia? {#engineering-teams}

Equipes de engenharia podem usar Feature Flags para reduzir o risco inerente ao lançamento de novos recursos e evitar a pressa de implementar correções de código no meio da madrugada.

Ao lançar novo código oculto por trás de um Feature Flag, sua equipe pode ativar ou desativar o recurso remotamente pelo dashboard da Braze, sem a demora de publicar novo código ou esperar pela aprovação de uma atualização na app store.

## Lançamentos de recursos e direcionamento {#feature-rollouts-and-targeting}

### Uma Feature Flag pode ser disponibilizada apenas para um grupo específico de usuários? {#target-users}

Sim, crie um Segment na Braze que direcione usuários específicos — por endereço de e-mail, `user_id` ou qualquer outro atributo nos perfis de usuário. Em seguida, faça a implantação da Feature Flag para 100% desse Segment.

### Como o ajuste da porcentagem de lançamento afeta usuários que já foram alocados no grupo habilitado? {#random-buckets}

Os lançamentos de Feature Flag permanecem consistentes para os usuários em todos os dispositivos e sessões.

- Quando uma Feature Flag é lançada para 10% de usuários aleatórios, esses 10% permanecerão habilitados durante toda a vida útil dessa Feature Flag.
- Se você aumentar o lançamento de 10% para 20%, os mesmos 10% permanecerão habilitados, e um novo grupo adicional de 10% de usuários será adicionado ao grupo habilitado.
- Se você reduzir o lançamento de 20% para 10%, apenas os 10% originais permanecerão habilitados.

Essa estratégia ajuda a garantir que os usuários tenham uma experiência consistente no seu app, sem ficar alternando entre estados a cada sessão. Naturalmente, desativar um recurso para 0% removerá todos os usuários da Feature Flag, o que é útil caso você descubra um bug ou precise desativar o recurso por completo.

## Tópicos técnicos {#technical-topics}

### Feature Flags podem ser usadas para controlar quando o SDK da Braze é inicializado? {#initialization}

Não, o SDK deve ser inicializado para baixar e sincronizar as feature flags para o usuário atual. Isso significa que você não pode usar feature flags para limitar quais usuários são criados ou rastreados na Braze.

### Com que frequência o SDK atualiza as feature flags? {#refresh-frequency}

As feature flags são atualizadas no início da sessão e ao trocar de usuário ativo. Elas também podem ser atualizadas manualmente usando o [método de atualização]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#refreshing) do SDK. As atualizações de feature flags têm um limite de frequência de uma vez a cada cinco minutos (sujeito a alterações).

Tenha em mente que boas práticas de dados recomendam não atualizar as feature flags com muita rapidez (com possível limite de frequência se isso ocorrer), então o ideal é atualizar apenas antes de o usuário interagir com novos recursos ou periodicamente no app, se necessário.

### As feature flags ficam disponíveis enquanto o usuário está offline? {#offline}

Sim, após serem atualizadas, as feature flags são armazenadas localmente no dispositivo do usuário e podem ser acessadas enquanto estiver offline.

### O que acontece se as feature flags forem atualizadas no meio de uma sessão? {#listen-for-updates}

As feature flags podem ser atualizadas no meio de uma sessão. Existem cenários em que você pode querer atualizar seu app caso certas variáveis ou a configuração tenham mudado. Em outros cenários, pode não ser desejável atualizar o app, para evitar uma mudança brusca na renderização da interface.

Para controlar isso, [escute as atualizações]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#updates) das feature flags e determine se deve renderizar novamente o app com base em quais feature flags foram alteradas.

### Por que os usuários no meu grupo de controle global não estão recebendo experimentos de feature flags? {#why-arent-users-in-my-global-control-group-receiving-feature-flags-experiments}

Você não pode ativar feature flags para usuários no seu [grupo de controle global]({{site.baseurl}}/user_guide/messaging/ab_testing/concepts). Isso significa que os usuários no seu grupo de controle global também não podem participar de experimentos de Feature Flag.

### A identificação de destinatários por e-mail faz parte das Feature Flags da Braze? {#is-email-based-recipient-identification-part-of-braze-feature-flags}

Não. Identificar destinatários por e-mail ao enviar uma mensagem não faz parte do produto Feature Flags desta página. Feature Flags controlam experiências dentro do app ou no site por meio do SDK da Braze.

Envios de Campaigns e Canvas disparados por API podem incluir `email` no [objeto de destinatários]({{site.baseurl}}/api/objects_filters/recipient_object) em vez de um `external_user_id`. Ao usar `email`, inclua `prioritization` para que a Braze possa selecionar o perfil de usuário correspondente. Essa opção de envio não está disponível em todos os espaços de trabalho.

Para o formato da requisição, consulte [POST: Enviar Campaigns usando entrega disparada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_campaigns) e [POST: Enviar mensagens de Canvas usando entrega disparada por API]({{site.baseurl}}/api/endpoints/messaging/send_messages/post_send_triggered_canvases).

## Dúvidas adicionais? {#additional-questions}

Tem dúvidas ou feedback? Envie um e-mail para nossa equipe: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).