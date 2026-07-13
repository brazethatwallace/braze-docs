---
nav_title: RevenueCat
article_title: RevenueCat
description: "A integração do RevenueCat e da Braze permite que você sincronize automaticamente os eventos do ciclo de vida de compra e inscrição dos seus clientes em todas as plataformas. Isso permite que você crie campanhas que reagem ao estágio do ciclo de vida da inscrição de seus clientes, como engajar com clientes que optaram por sair durante o período de teste gratuito ou enviar lembretes para clientes com problemas de faturamento."
alias: /partners/revenuecat/
page_type: partner
search_tag: Partner

---

# RevenueCat

> A [RevenueCat](https://www.revenuecat.com/) é a única fonte da verdade do status da sua inscrição em iOS, Android e web. Quer você esteja construindo um novo app ou já tenha milhões de assinantes, é possível usar a RevenueCat para criar compras em aplicativos multiplataforma, gerenciar seus produtos e assinantes e analisar seus dados – sem necessidade de código de servidor.

_Esta integração é mantida pela RevenueCat._

## Sobre a integração {#about-the-integration}

A integração do RevenueCat e da Braze permite que você sincronize automaticamente os eventos do ciclo de vida de compra e inscrição dos seus clientes em todas as plataformas. Isso permite que você crie campanhas que reagem ao estágio do ciclo de vida da inscrição de seus clientes, como engajar com clientes que optaram por sair durante o período de teste gratuito ou enviar lembretes para clientes com problemas de faturamento.

## Pré-requisitos {#prerequisites}

No mínimo, será necessário ativar a integração no dashboard da RevenueCat para conectá-la à Braze. Se você estiver usando o SDK da Braze, poderá usar os SDKs da RevenueCat e da Braze juntos para aprimorar a integração, garantindo que o mesmo identificador de cliente seja usado em ambos os sistemas.

| Requisito | Descrição |
|---|---|
| Conta e app do RevenueCat | Uma [conta RevenueCat](https://app.revenuecat.com/login) é necessária para aproveitar esta parceria. Você também deve ter um app RevenueCat configurado. |
| SDK RevenueCat | Além do SDK da Braze necessário, recomendamos a instalação do [SDK RevenueCat](https://docs.revenuecat.com/docs/configuring-sdk) para fornecer aliases de usuário para a RevenueCat. |
| Instância da Braze | Sua instância da Braze pode ser obtida com seu gerente de integração da Braze ou pode ser encontrada na [página de visão geral da API]({{site.baseurl}}/api/basics#endpoints).<br><br>A RevenueCat requer a instância da Braze para enviar do lado do servidor para o endpoint REST correto da Braze. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. <br><br> Isso pode ser criado no dashboard da Braze em **Configurações** > **Chaves de API**. |
| Chave da API REST de teste da Braze (opcional) | Uma chave de API de teste pode ser usada para compras de teste e produção se você quiser que essas solicitações sejam enviadas para instâncias da Braze separadas. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Casos de uso {#use-cases}

- Disparar uma campanha de integração destacando seus recursos premium quando um cliente iniciar um teste gratuito.
- Enviar um lembrete para atualizar as informações de cobrança quando um evento de "Problema de cobrança" for recebido.
- Enviar uma pesquisa de feedback após um cliente cancelar um teste gratuito.

## Integração {#integration}

### Etapa 1: Definir identidade de usuário da Braze {#step-1-set-braze-user-identity}

No SDK da Braze, você pode definir o ID de usuário da Braze para corresponder ao ID de usuário do app da RevenueCat, garantindo que os eventos enviados da Braze e da RevenueCat possam ser sincronizados para o mesmo usuário.

Configure o SDK da Braze com o mesmo ID de usuário do app da RevenueCat ou use o método `.changeUser()` do SDK da Braze.

{% tabs local %}
{% tab swift %}
```swift
// Configure Purchases SDK
Purchases.configure(withAPIKey: "public_sdk_key", appUserID: "my_app_user_id")

// Change user in Braze SDK
Appboy.sharedInstance()?.changeUser("my_app_user_id")

// Optional User Alias Object attributes
Purchases.shared.setAttributes(["$brazeAliasName" : "name",
                             "$brazeAliasLabel" : "label"])
```
{% endtab %}
{% tab objective-c %}
```objc
// Configure Purchases SDK
[RCPurchases configureWithAPIKey:@"public_sdk_key" appUserID:@"my_app_user_id"];

// Change user in Braze SDK
[[Appboy sharedInstance] changeUser:@"my_app_user_id"];

// Optional User Alias Object attributes
[[RCPurchases sharedPurchases] setAttributes:@{
    @"$brazeAliasName": @"name",
    @"$brazeAliasLabel": @"label"
}];
```
{% endtab %}
{% tab java %}
```java
// Configure Purchases SDK
Purchases.configure(this, "public_sdk_key", "my_app_user_id");

// Change user in Braze SDK
Braze.getInstance(context).changeUser(my_app_user_id);

// Optional User Alias Object attributes
Map<String, String> attributes = new HashMap<String, String>();
attributes.put("$brazeAliasName", "name");
attributes.put("$brazeAliasLabel", "label");

Purchases.getSharedInstance().setAttributes(attributes);
```
{% endtab %}
{% endtabs %}

#### Enviar objeto de alias de usuário para a Braze (opcional) {#send-user-alias-object-to-braze-optional}

Se você deseja enviar um identificador de usuário único alternativo diferente do ID de usuário do app RevenueCat, atualize os usuários com os seguintes dados como atributos de assinante do RevenueCat.

| Chave | Descrição |
|---|---|
| `$brazeAliasName` | O `alias_name` da Braze no [objeto de alias do usuário]({{site.baseurl}}/api/objects_filters/user_alias_object) |
| `$brazeAliasLabel` | O `alias_label` da Braze no [objeto de alias do usuário]({{site.baseurl}}/api/objects_filters/user_alias_object) |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Enviar objeto de alias de usuário para a Braze (opcional)" }

Ambos os atributos são necessários para que o [objeto de alias do usuário]({{site.baseurl}}/api/objects_filters/user_alias_object) seja enviado junto com seus dados de evento. Essas propriedades podem ser definidas manualmente, como qualquer outro [atributo de assinante RevenueCat](https://docs.revenuecat.com/docs/subscriber-attributes). Exemplos de snippets de código são mostrados na etapa 1.

### Etapa 2: Enviar eventos do RevenueCat para a Braze {#step-2-send-revenuecat-events-to-braze}

Depois de configurar o SDK de compras da RevenueCat e o SDK da Braze para ter a mesma identidade de usuário, você pode ativar a integração e configurar os nomes dos eventos no dashboard da RevenueCat.

1. Navegue até o seu projeto no dashboard da RevenueCat e encontre o cartão **Integrations** no menu de navegação. Selecione **+ New**.
2. Em seguida, selecione **Braze** entre as integrações disponíveis e adicione sua instância da Braze e a chave da API REST da Braze.
3. Digite os nomes dos eventos que o RevenueCat enviará ou escolha os nomes dos eventos padrão. Mais detalhes sobre os eventos disponíveis podem ser encontrados na [etapa 3](#configure-event-names).
4. Selecione se deseja que a RevenueCat relate os rendimentos (após a comissão da app store) ou a receita (vendas brutas).

![Configurações da Braze na RevenueCat com campos para a instância da Braze, identificador da chave de API e identificador da sandbox.]({% image_buster /assets/img/revenuecat/braze_settings_in_revenuecat.png %})

### Etapa 3: Configurar nomes de eventos {#configure-event-names}

Digite os nomes dos eventos que o RevenueCat enviará ou selecione entre os nomes de eventos padrão selecionando **Use Default Event Names**. Os eventos que a RevenueCat pode enviar estão descritos na tabela a seguir.

| Evento | Descrição |
|---|---|
| Compra inicial | A primeira compra de um produto de inscrição com renovação automática que não contém um teste gratuito. |
| Teste iniciado | O início de um período de teste gratuito de um produto de inscrição com renovação automática. |
| Teste convertido | Quando um produto de inscrição com renovação automática é convertido de um teste gratuito para um período pago normal. |
| Teste cancelado | Quando um usuário desativa as renovações de um produto de inscrição com renovação automática durante um período de teste gratuito. |
| Renovação | Quando um produto de inscrição com renovação automática é renovado, ou um usuário recompra o produto de inscrição com renovação automática após uma interrupção na sua inscrição. |
| Cancelamento | Quando um usuário desativa as renovações de um produto de inscrição com renovação automática durante o período pago normal. |
| Compra sem inscrição | A compra de qualquer produto que não seja uma inscrição com renovação automática. |
| Expiração | Quando uma inscrição expira. |
| Problema de cobrança | Quando houve um problema ao tentar cobrar o usuário. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Etapa 3: Configurar nomes de eventos" }

Para eventos que incluem receita, a RevenueCat registrará automaticamente esse valor junto com o evento na Braze, como conversões de teste e renovações.

## Usando esta integração {#using-this-integration}

Depois de definir as configurações da Braze na RevenueCat, os eventos começarão a fluir automaticamente da RevenueCat para a Braze sem qualquer outra ação da sua parte.

## Personalização {#customization}

### Adicionar uma chave de API sandbox para testes {#add-a-sandbox-api-key-for-testing}

Se você fornecer apenas uma chave da API REST da Braze para a RevenueCat, apenas eventos de produção serão enviados. Se você também quiser enviar eventos de teste em sandbox, [crie outra chave da API REST da Braze]({{site.baseurl}}/api/basics#app-group-rest-api-keys) e adicione-a às suas configurações da Braze na RevenueCat.