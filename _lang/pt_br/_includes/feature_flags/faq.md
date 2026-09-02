# Perguntas frequentes {#frequently-asked-questions}

> Este artigo fornece respostas a algumas perguntas frequentes sobre os Feature Flags.

## Funcionalidade e suporte {#functionality-and-support}

### Em quais plataformas as Feature Flags da Braze são suportadas? {#platforms}

A Braze suporta Feature Flags nas plataformas iOS, Android e web com os seguintes requisitos mínimos de versão do SDK or kit de desenvolvimento de software:

{% sdk_min_versions swift:5.9.0 android:24.2.0 web:4.6.0 unity:4.1.0 cordova:5.0.0 reactnative:4.1.0 flutter:6.0.0 roku:1.0.0 %}

Precisa de suporte em outras plataformas? Envie um e-mail para nossa equipe: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).

### Qual é o nível de esforço envolvido na implementação de uma Feature Flag? {#level-of-effort}

Uma Feature Flag pode ser criada e integrada em poucos minutos.

A maior parte do esforço envolvido estará relacionada à sua equipe de engenharia construindo o novo recurso que você planeja lançar. Mas quando se trata de adicionar uma Feature Flag, é tão simples quanto uma instrução `IF`/`ELSE` no código do seu app ou website:

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

As equipes de marketing podem usar Feature Flags para coordenar anúncios de produtos (como e-mails de lançamento de produto) quando um recurso está ativado apenas para uma pequena porcentagem de usuários.

Por exemplo, com as Feature Flags da Braze, você pode lançar um novo programa de fidelidade do cliente para 10% dos usuários no seu app e enviar um e-mail, push ou outro envio de mensagens para os mesmos 10% de usuários habilitados usando a etapa Feature Flag do Canvas.

### Como as Feature Flags podem beneficiar equipes de produto? {#product-teams}

As equipes de produto podem usar Feature Flags para realizar lançamentos graduais ou lançamentos suaves de novos recursos, monitorando indicadores chave de desempenho (KPIs) e feedback dos clientes antes de disponibilizar para todos os usuários.

As equipes de produto podem usar [propriedades de Feature Flag]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#properties) para preencher remotamente conteúdo em um app, como deep links, texto, imagens ou outro conteúdo dinâmico.

Usando a etapa Feature Flag do Canvas, as equipes de produto também podem executar um teste A/B para medir como um novo recurso impacta as taxas de conversão em comparação com usuários que têm o recurso desativado.

### Como as Feature Flags podem beneficiar equipes de engenharia? {#engineering-teams}

As equipes de engenharia podem usar Feature Flags para reduzir o risco inerente ao lançamento de novos recursos e evitar a correria de implementar correções de código no meio da noite.

Ao lançar novo código escondido atrás de uma Feature Flag, sua equipe pode ativar ou desativar o recurso remotamente pelo dashboard da Braze, evitando o atraso de enviar novo código ou aguardar a aprovação de uma atualização na loja de apps.

## Implementação de recursos e direcionamento {#feature-rollouts-and-targeting}

### Um Feature Flag pode ser liberado apenas para um grupo específico de usuários? {#target-users}

Sim, crie um Segment or segmento na Braze que direcione usuários específicos — por endereço de e-mail, `user_id` ou qualquer outro atributo nos perfis de usuário. Em seguida, implante o Feature Flag para 100% desse Segment or segmento.

### Como o ajuste da porcentagem de implementação afeta os usuários que já foram alocados no grupo ativado? {#random-buckets}

A implementação de Feature Flags permanece consistente para os usuários entre dispositivos e sessões.

- Quando um Feature Flag é liberado para 10% de usuários aleatórios, esses 10% permanecem ativados e persistem por toda a vida útil desse Feature Flag.
- Se você aumentar a implementação de 10% para 20%, os mesmos 10% continuarão ativados, e mais 10% de usuários adicionais serão incluídos no grupo ativado.
- Se você reduzir a implementação de 20% para 10%, apenas os 10% originais de usuários permanecerão ativados.

Essa estratégia ajuda a garantir que os usuários tenham uma experiência consistente no seu app, sem ficar alternando entre ativado e desativado entre sessões. É claro que desativar um recurso para 0% removerá todos os usuários do Feature Flag, o que é útil se você descobrir um bug ou precisar desativar o recurso por completo.

## Tópicos técnicos {#technical-topics}

### Feature Flags podem ser usados para controlar quando o SDK or kit de desenvolvimento de software da Braze é inicializado? {#initialization}

Não, o SDK or kit de desenvolvimento de software precisa ser inicializado para baixar e sincronizar as Feature Flags do usuário atual. Isso significa que você não pode usar Feature Flags para limitar quais usuários são criados ou rastreados na Braze.

### Com que frequência o SDK or kit de desenvolvimento de software atualiza as Feature Flags? {#refresh-frequency}

As Feature Flags são atualizadas no início da sessão e ao trocar de usuário ativo. As Feature Flags também podem ser atualizadas manualmente usando o [método de atualização]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#refreshing) do SDK or kit de desenvolvimento de software. As atualizações de Feature Flags têm um limite de frequência de uma vez a cada cinco minutos (sujeito a alterações).

Tenha em mente que boas práticas de dados recomendam não atualizar Feature Flags com muita rapidez (com possível limite de frequência se isso for feito), então o ideal é atualizar apenas antes de o usuário interagir com novos recursos ou periodicamente no app, se necessário.

### As Feature Flags ficam disponíveis enquanto o usuário está offline? {#offline}

Sim, após as Feature Flags serem atualizadas, elas são armazenadas localmente no dispositivo do usuário e podem ser acessadas enquanto estiver offline.

### O que acontece se as Feature Flags forem atualizadas no meio da sessão? {#listen-for-updates}

As Feature Flags podem ser atualizadas no meio da sessão. Existem cenários em que você pode querer atualizar seu app caso certas variáveis ou a configuração mudem. Existem outros cenários em que talvez você não queira atualizar o app, para evitar uma mudança brusca na renderização da interface.

Para controlar isso, [escute atualizações]({{site.baseurl}}/developer_guide/platform_wide/feature_flags/create#updates) das Feature Flags e determine se deve renderizar novamente seu app com base em quais Feature Flags foram alteradas.

### Por que os usuários do meu grupo de controle global não estão recebendo experimentos de Feature Flags? {#why-arent-users-in-my-global-control-group-receiving-feature-flags-experiments}

Não é possível ativar Feature Flags para usuários no seu [grupo de controle global]({{site.baseurl}}/user_guide/audience/global_control_group). Isso significa que os usuários no grupo de controle global também não podem fazer parte de experimentos de Feature Flags.

## Perguntas adicionais? {#additional-questions}

Tem dúvidas ou feedback? Envie um e-mail para nossa equipe: [feature-flags-feedback@braze.com](mailto:feature-flags-feedback@braze.com).