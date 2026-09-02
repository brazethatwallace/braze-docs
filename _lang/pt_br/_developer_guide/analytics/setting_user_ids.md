---
nav_title: Definir IDs de usuário
article_title: Definir IDs de usuário
page_order: 1.1
description: "Aprenda como definir IDs de usuário através do SDK or kit de desenvolvimento de software da Braze."
---

# Definir IDs de usuário {#set-user-ids}

> Aprenda como definir IDs de usuário através do SDK or kit de desenvolvimento de software da Braze. Estes são identificadores únicos que permitem rastrear usuários em dispositivos e plataformas, importar seus dados através da [API or interface de programação do aplicativo (API) de dados de usuários]({{site.baseurl}}/api/endpoints/user_data) e enviar mensagens direcionadas através da [API or interface de programação do aplicativo (API) de envio de mensagens]({{site.baseurl}}/api/endpoints/messaging). Se você não atribuir um ID único a um usuário, a Braze atribuirá a ele um ID anônimo; no entanto, você não poderá usar esses recursos até que o faça.

{% alert note %}
Para wrapper SDKs não listados, use o método nativo relevante do Android ou Swift.
{% endalert %}

## Sobre usuários anônimos {#about-anonymous-users}

{% multi_lang_include anonymous_users/about_anonymous_users.md %}

### Impedindo o rastreamento de usuários anônimos {#preventing-anonymous-user-tracking}

Se o seu caso de uso exige que nenhum dado seja coletado antes que um usuário seja identificado, você pode adiar a inicialização do SDK or kit de desenvolvimento de software da Braze até que o usuário faça login e um `external_id` esteja disponível. Defina um sinalizador no seu código que mude para `true` quando o usuário fizer login e inicialize o SDK or kit de desenvolvimento de software somente quando esse sinalizador estiver definido.

{% alert warning %}
Adie a inicialização apenas na **primeira vez** que um usuário baixar seu app (antes de um `external_id` ser definido). Se você impedir que o SDK or kit de desenvolvimento de software seja inicializado toda vez que um usuário fizer logout ou iniciar uma nova sessão, isso interferirá no pré-carregamento de ativos de mensagens no app e cartões de conteúdo, o que pode causar erros de entregabilidade para essas Campaigns.
{% endalert %}

## Definir um ID de usuário {#setting-a-user-id}

Para definir um ID de usuário, chame o método `changeUser()` depois que o usuário fizer o login inicial. Os IDs devem ser exclusivos e seguir nossas [práticas recomendadas de nomenclatura](#naming-best-practices).

Se você estiver fazendo hash de um identificador exclusivo, normalize a entrada da sua função de hash. Por exemplo, ao fazer hash de um endereço de e-mail, remova espaços no início e no final e leve em conta a localização.

{% tabs local %}
{% tab WEB %}
Para uma implementação padrão do Web SDK or kit de desenvolvimento de software, você pode usar o seguinte método:

```javascript
braze.changeUser(YOUR_USER_ID_STRING);
```

Se preferir usar o Google Tag Manager, você pode usar o tipo de tag **Change User** para chamar o [método `changeUser`](https://js.appboycdn.com/web-sdk/latest/doc/modules/braze.html#changeuser). Use-o sempre que um usuário fizer login ou for identificado com seu identificador exclusivo `external_id`.

Certifique-se de inserir o ID exclusivo do usuário atual no campo **External User ID**, geralmente preenchido usando uma variável da camada de dados enviada pelo seu website.

![Uma caixa de diálogo mostrando as configurações da Braze Action Tag. As configurações incluem "tag type" e "external user ID".]({% image_buster /assets/img/web-gtm/gtm-change-user.png %})
{% endtab %}

{% tab ANDROID %}
{% subtabs %}
{% subtab JAVA %}
```java
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING);
```
{% endsubtab %}
{% subtab KOTLIN %}
```kotlin
Braze.getInstance(context).changeUser(YOUR_USER_ID_STRING)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab SWIFT %}
{% subtabs %}
{% subtab swift %}
```swift
AppDelegate.braze?.changeUser(userId: "YOUR_USER_ID")
```
{% endsubtab %}
{% subtab objective-c %}
```objc
[AppDelegate.braze changeUser:@"YOUR_USER_ID_STRING"];
```
{% endsubtab %}
{% endsubtabs %}

{% alert note %}
`changeUser` enfileira a troca de usuário e retorna imediatamente na thread de chamada. Qualquer setter de atributo chamado em `braze.user` depois disso é automaticamente serializado após as operações iniciadas por `changeUser`. A leitura de `braze.user.id` bloqueia a thread de chamada até que a troca de usuário seja totalmente concluída. Para contextos na thread principal ou sensíveis à latência, use as alternativas não bloqueantes.

{% subtabs local %}
{% subtab Swift %}
```swift
// Completion handler — always delivers on the main thread.
AppDelegate.braze?.user.getId { userId in
  print("User ID:", userId ?? "anonymous")
}

// Async/await (iOS 13.0+, tvOS 13.0+, watchOS 6.0+, macOS 10.15+)
let userId = await AppDelegate.braze?.user.getId()
```
{% endsubtab %}
{% subtab Objective-C %}
```objc
// Completion handler — always delivers on the main thread.
[AppDelegate.braze.user getIdWithCompletion:^(NSString * _Nullable userId) {
  NSLog(@"User ID: %@", userId ?: @"anonymous");
}];
```
{% endsubtab %}
{% endsubtabs local %}
{% endalert %}
{% endtab %}

{% tab CORDOVA %}
```javascript
BrazePlugin.changeUser("YOUR_USER_ID");
```
{% endtab %}

{% tab ROKU %}
```brightscript
m.Braze.setUserId(YOUR_USER_ID_STRING)
```
{% endtab %}

{% tab UNITY %}
```csharp
AppboyBinding.ChangeUser("YOUR_USER_ID_STRING");
```
{% endtab %}

{% tab React Native %}
```javascript
Braze.changeUser("YOUR_USER_ID_STRING");
```
{% endtab %}
{% endtabs %}

### Como o `changeUser()` funciona {#how-changeuser-works}

Quando você chama `changeUser()`, os seguintes comportamentos se aplicam:

- Chamar `changeUser()` com o **mesmo** ID de usuário que já está definido não afeta a contagem de sessões.
- Chamar `changeUser()` com um ID de usuário **diferente** encerra automaticamente a sessão atual e inicia uma nova.
- Quando um usuário anônimo chama `changeUser()` com um **novo** ID de usuário (que ainda não existe na Braze), os dados do perfil anônimo são mesclados ao novo perfil identificado.
- Quando um usuário anônimo chama `changeUser()` com um ID de usuário **existente**, os dados do perfil anônimo não são mesclados ao perfil identificado.

{% alert note %}
Chamar `changeUser()` dispara um envio de dados como parte do encerramento da sessão do usuário atual. O SDK or kit de desenvolvimento de software envia automaticamente todos os dados pendentes do usuário anterior antes de alternar para o novo usuário, então não é necessário solicitar manualmente um envio de dados antes de chamar `changeUser()`.
{% endalert %}

{% alert warning %}
Não atribua um único ID de usuário compartilhado (por exemplo, um ID externo padrão estático) nem chame `changeUser()` quando um usuário fizer logout. Fazer isso impede o reengajamento de qualquer usuário previamente conectado em dispositivos compartilhados e faz com que todos os dados sejam registrados em um único ID de usuário, o que pode causar comportamentos inesperados em outros recursos. Em vez disso, rastreie todos os IDs de usuário separadamente e garanta que o processo de logout do seu app permita alternar de volta para um usuário conectado anteriormente. Quando uma nova sessão é iniciada, a Braze atualiza automaticamente os dados do perfil recém-ativo.
{% endalert %}

## Aliases de usuário {#user-aliases}

### Como funcionam {#how-they-work}

{% multi_lang_include anonymous_users/about_user_aliases.md %}

### Definindo um alias de usuário {#setting-a-user-alias}

Um alias de usuário consiste em duas partes: um nome e um rótulo. O nome se refere ao identificador em si, enquanto o rótulo indica o tipo de identificador ao qual ele pertence. Por exemplo, se você tem um usuário em uma plataforma de atendimento ao cliente de terceiros com o ID externo `987654`, pode atribuir a ele um alias na Braze com o nome `987654` e o rótulo `support_id`, para rastreá-lo entre plataformas.

{% tabs local %}
{% tab web %}
```javascript
braze.getUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endtab %}

{% tab android %}
{% subtabs %}
{% subtab java %}
```java
Braze.getInstance(context).getCurrentUser().addAlias(ALIAS_NAME, ALIAS_LABEL);
```
{% endsubtab %}

{% subtab kotlin %}
```kotlin
Braze.getInstance(context).currentUser?.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab swift %}
{% subtabs %}
{% subtab swift %}
```swift
Appboy.sharedInstance()?.user.addAlias(ALIAS_NAME, ALIAS_LABEL)
```
{% endsubtab %}

{% subtab objective-c %}
```objc
 [[Appboy sharedInstance].user addAlias:ALIAS_NAME withLabel:ALIAS_LABEL];
```
{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab REST or transferir estado representacional API or interface de programação do aplicativo (API) %}
```json
{
  "alias_name" : (required, string),
  "alias_label" : (required, string)
}
```
{% endtab %}

{% tab React Native %}
```javascript
Braze.addAlias("ALIAS_NAME", "ALIAS_LABEL");
```
{% endtab %}
{% endtabs %}

## Melhores práticas de nomenclatura de IDs {#naming-best-practices}

Recomendamos que você crie IDs de usuário usando o padrão [Identificador Único Universal (UUID)](https://en.wikipedia.org/wiki/Universally_unique_identifier), o que significa que são strings de 128 bits aleatórias e bem distribuídas.

Alternativamente, você pode fazer hash de um identificador único existente (como um nome ou endereço de e-mail) para gerar seus IDs de usuário. Se fizer isso, certifique-se de implementar a [autenticação do SDK or kit de desenvolvimento de software]({{site.baseurl}}/developer_guide/sdk_integration/authentication) para evitar a simulação de usuários.

{% alert warning %}
Não use um valor previsível ou um número incremental para seu ID de usuário. Isso pode expor sua organização a ataques maliciosos ou exfiltração de dados.

Para maior segurança, use a [autenticação do SDK or kit de desenvolvimento de software]({{site.baseurl}}/developer_guide/sdk_integration/authentication).
{% endalert %}

Embora seja essencial que você nomeie corretamente seus IDs de usuário desde o início, você sempre pode renomeá-los no futuro usando o endpoint [`/users/external_ids/rename`]({{site.baseurl}}/api/endpoints/user_data/external_id_migration).

| Tipos de ID não recomendados | Exemplo não recomendado |
| ------------ | ----------- |
| ID de perfil visível do usuário ou nome de usuário | JonDoe829525552 |
| Endereço de e-mail | Anna@email.com |
| ID de usuário auto-incremental | 123 |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Melhores práticas de nomenclatura de IDs" }

{% alert warning %}
Evite compartilhar detalhes sobre como você cria IDs de usuário, pois isso pode expor sua organização a ataques maliciosos ou exfiltração de dados.
{% endalert %}