{% tabs %}
{% tab Abandoned browse %}

### Navegação abandonada {#abandoned-browse}

Use o modelo de **Navegação abandonada** para engajar usuários que navegaram por produtos, mas não os adicionaram ao carrinho nem realizaram um pedido.

![Um modelo de Canvas "Navegação Abandonada" aplicado com "Regras de Entrada" expandidas.]({% image_buster /assets/img_archive/abandoned_browse.png %})

#### Configuração {#setup}

Na página do Canvas, selecione **Use a Canvas Template** > **Braze templates** e aplique o modelo **Navegação abandonada**.

##### Configurações padrão {#default-settings}

As seguintes configurações estão pré-configuradas no seu Canvas:
- Básico
    - Nome do Canvas: **Abandoned browse**
    - Evento de conversão: `ecommerce.order placed`
        - Prazo de conversão: 3 dias
- Cronograma de entrada
    - Baseado em ação quando um usuário realiza o evento `ecommerce.product_viewed`
    - O horário de início é quando você cria o modelo de Canvas<br><br>!["Opções Baseadas em Ação" para o Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry.png %})<br><br>
- Público-alvo
    - Público de entrada
        - E-mail **não está em branco**
        - Você também pode modificar os critérios de público de entrada para atender às necessidades do seu negócio
    - Controles de entrada
        - Os usuários são elegíveis para reentrar neste Canvas após a duração total do Canvas ser concluída
    - Critérios de saída
        - Realiza `ecommerce.cart_updated`, `ecommerce.checkout_started` ou `ecommerce.order_placed`<br><br>![Controles de entrada e critérios de saída para o Canvas.]({% image_buster /assets/img/ecommerce/abandoned_browse_entry_exit.png %})<br><br>
- Configurações de envio
    - Usuários inscritos ou que aceitaram receber mensagens
- Etapa de postergação
    - 1 hora de postergação
- Etapa de mensagem
    - Revise o modelo de e-mail e o bloco HTML com um exemplo de template Liquid para adicionar produtos à sua mensagem no modelo pré-construído. Se você usar seu próprio modelo de e-mail, também pode consultar as [variáveis Liquid](#message-personalization), conforme demonstrado na seção a seguir.

#### Personalização de produtos de navegação abandonada para e-mails {#abandoned-browse-product-personalization-for-emails}

Aqui está um exemplo de como você adicionaria um bloco de produto HTML ao seu e-mail de navegação abandonada.

{% raw %}
```java
<table aria-label="Abandoned browse product personalization for emails" style="width:100%">
  <tr>
    <th><img src="{{context.${image_url}}}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{context.${product_name}}}</li>
        <li>Price: ${{context.${price}}}</li>
      </ul>
    </th>
  </tr>
</table>
```
{% endraw %}

##### URL do produto {#product-url}

{% raw %}
```liquid
{{context.${product_url}}}
```
{% endraw %}

{% endtab %}
{% tab Abandoned cart %}

### Carrinho abandonado {#abandoned-cart}

Use o modelo **Carrinho abandonado** para recuperar vendas potencialmente perdidas de clientes que adicionaram produtos ao carrinho, mas não prosseguiram para o checkout nem realizaram um pedido.

![Um modelo de Canvas "Carrinho Abandonado" aplicado com "Regras de Entrada" expandidas.]({% image_buster /assets/img_archive/abandoned_cart.png %})

#### Configuração

Na página do Canvas, selecione **Use a Canvas Template** > **Braze templates** e aplique o modelo **Carrinho abandonado**.

##### Configurações padrão

As seguintes configurações estão pré-configuradas no seu Canvas:
- Básico
    - Nome do Canvas: **Abandoned cart**
    - Evento de conversão: `ecommerce.order_placed`
        - Prazo de conversão: 3 dias
- Cronograma de entrada
    - Gatilho baseado em ação quando um usuário aciona o **Perform Cart Updated Event** (localizado no dropdown)
    - O horário de início é quando você cria o modelo de Canvas<br><br>!["Opções Baseadas em Ação" para o Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry.png %})<br><br>
- Público-alvo
    - Público de entrada
        - Usou esses apps **mais de 0** vezes
        - E-mail **não está em branco**
    - Controles de entrada
        - Os usuários são imediatamente reelegíveis para entrada no Canvas
    - Critérios de saída
        - Realiza `ecommerce.cart_updated`, `ecommerce.checkout_started` ou `ecommerce.order_placed`<br><br>![Controles de entrada e critérios de saída para o Canvas.]({% image_buster /assets/img/ecommerce/abandoned_cart_entry_exit.png %})<br><br>
- Configurações de envio
    - Usuários inscritos ou que aceitaram receber mensagens
- Etapa de postergação
     - 4 horas de postergação
- Etapa de mensagem
    - Revise o modelo de e-mail e o bloco HTML com um exemplo de template Liquid para adicionar produtos à sua mensagem no modelo pré-construído. Se você usar seu próprio modelo de e-mail, também pode consultar as [variáveis Liquid](#message-personalization), conforme demonstrado na seção a seguir.

#### Como funciona a lógica de reentrada do carrinho abandonado {#how-abandoned-cart-re-entry-logic-works}

Quando um usuário inicia o processo de checkout, seu carrinho é marcado como `checkout_started`. A partir desse ponto, quaisquer atualizações adicionais do carrinho com o mesmo ID de carrinho não qualificarão o usuário para reentrar na jornada de carrinho abandonado.

1. Quando um usuário adiciona um item ao carrinho, ele entra no Canvas.
2. Cada vez que adiciona ou atualiza itens, ele reentra no Canvas — isso mantém os dados do carrinho e o envio de mensagens atualizados.
3. Quando o usuário inicia o processo de checkout, seu carrinho é marcado como `checkout_started` e ele sai do Canvas.
4. Quaisquer atualizações futuras do carrinho usando o mesmo ID de carrinho não dispararão a reentrada, pois esse carrinho já avançou para a fase de checkout.

Quando os usuários avançam para a jornada de checkout, eles passam a ser direcionados pelo [Canvas de checkout abandonado](#abandoned-checkout), que é projetado para usuários mais adiantados na jornada de compra.

#### Personalização de produtos de carrinho abandonado para e-mails {#abandoned-cart-checkout}

Jornadas de carrinho abandonado requerem uma Liquid tag especial `shopping_cart` para personalização de produtos.

Aqui está um exemplo de como você adicionaria um bloco HTML com sua Liquid tag `shopping_cart` para adicionar produtos ao seu e-mail.

{% raw %}
```java
<table aria-label="Abandoned cart product personalization for emails #abandoned-cart-checkout" style="width:100%">
  {% shopping_cart {{context.${cart_id}}} %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

{% alert note %}
Se você usar Shopify, adicione o nome do seu catálogo para obter a URL da imagem da variante.
{% endalert %}

##### URL do carrinho HTML {#html-cart-url}

Se você quiser direcionar os usuários de volta ao carrinho, pode adicionar uma propriedade de evento aninhada dentro do objeto de metadados, como:

{% raw %}
```liquid
{{context.${metadata}.cart_url}}
```
{% endraw %}

Se você usar Shopify, crie a URL do carrinho usando este modelo Liquid:

{% raw %}
```liquid
{{context.${source}}}/checkouts/cn/{{context.${cart_id}}}
```
{% endraw %}

{% endtab %}
{% tab Abandoned checkout %}

### Checkout abandonado {#abandoned-checkout}

Use o modelo **Checkout abandonado** para direcionar clientes que iniciaram o processo de checkout, mas saíram antes de finalizar o pedido.

![Um modelo de Canvas "Checkout Abandonado" aplicado com "Regras de Entrada" expandidas.]({% image_buster /assets/img_archive/abandoned_checkout.png %})

#### Configuração

Na página do Canvas, selecione **Use a Canvas Template** > **Braze templates** e aplique o modelo **Checkout abandonado**.

##### Configurações padrão

As seguintes configurações estão pré-configuradas no seu Canvas:

- Básico
    - Nome do Canvas: **Abandoned checkout**
    - Evento de conversão: `ecommerce.order_placed`
        - Prazo de conversão: 3 dias
- Cronograma de entrada
    - Gatilho baseado em ação quando um usuário realiza o evento `ecommerce.checkout_started`
    - O horário de início é quando você cria o modelo de Canvas<br><br>!["Opções Baseadas em Ação" para o Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry.png %})
- Público-alvo
    - Público de entrada
        - Usou esses apps **mais de 0** vezes
        - E-mail **não está em branco**
    - Controles de entrada
        - Os usuários são imediatamente reelegíveis para entrada no Canvas
        - Critérios de saída
            - Realiza os eventos `ecommerce.order_placed`<br><br>![Controles de entrada e critérios de saída para o Canvas.]({% image_buster /assets/img/ecommerce/abandoned_checkout_entry_exit.png %})<br><br>
- Configurações de envio
    - Usuários inscritos ou que aceitaram receber mensagens
- Etapa de postergação
    - 4 horas de postergação
- Etapa de mensagem
    - Revise o modelo de e-mail e o bloco HTML com um exemplo de template Liquid para adicionar produtos à sua mensagem no modelo pré-construído. Se você usar seu próprio modelo de e-mail, também pode consultar as [variáveis Liquid](#message-personalization), conforme demonstrado na seção a seguir.

#### Personalização de checkout abandonado para e-mails {#abandoned-checkout-personalization-for-emails}

Jornadas de checkout abandonado requerem uma Liquid tag especial `shopping_cart` para personalização de produtos.

Aqui está um exemplo de como você adicionaria um bloco HTML com sua Liquid tag `shopping_cart` para adicionar produtos ao seu e-mail.

{% raw %}
```java
<table aria-label="Abandoned checkout personalization for emails" style="width:100%">
  {% shopping_cart {{context.${cart_id}}} :abort_if_not_abandoned false %}
  {% for item in shopping_cart.products %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200"><img></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{ item.product_name }}</li>
        <li>Price: ${{ item.price }}</li>
        <li>Quantity: ${{ item.quantity }}</li>
        <li>Variant ID: {{ item.variant_id }}</li>
        <li>Product URL:{{ item.product_url }}</li>
        <li>SKU: {{ item.metadata.sku }}</li>
      </ul>
    </th>
    {% endfor %}
</table>
```
{% endraw %}

##### `abort_if_not_abandoned` {#abort-if-not-abandoned}

O parâmetro `abort_if_not_abandoned` é específico do caso de uso de checkout abandonado e é utilizado apenas com a Liquid tag `shopping_cart` em conjunto com o evento `ecommerce.checkout_started`.

| Valor | Comportamento |
| ----- | -------- |
| `true` (padrão) | A mensagem é cancelada se o carrinho não tiver sido abandonado — ou seja, se o usuário já tiver concluído o pedido. |
| `false` | A mensagem é enviada mesmo que o carrinho não esteja em estado de abandono, permitindo que o e-mail inclua os detalhes do carrinho independentemente do status atual do checkout. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="abortifnotabandoned #abort-if-not-abandoned" }

Defina `abort_if_not_abandoned` como `false` quando quiser enviar o lembrete de checkout independentemente de o carrinho ainda ser considerado abandonado no momento do envio. Se você omitir o parâmetro ou defini-lo como `true`, a Braze cancelará a mensagem para usuários que já concluíram a compra.

##### URL de checkout {#checkout-url}

{% raw %}
```liquid
{{context.${metadata}.checkout_url}}
```
{% endraw %}

{% endtab %}
{% tab Order confirmation and feedback survey %}

### Confirmação de pedido e pesquisa de feedback {#order-confirmation-and-feedback-survey}

Use o modelo **Confirmação de pedido e pesquisa de feedback** para confirmar pedidos bem-sucedidos e aumentar a satisfação do cliente.

![Um modelo de Canvas "Confirmação de pedido" aplicado com "Regras de Entrada" expandidas.]({% image_buster /assets/img_archive/order_confirmation_feedback.png %})

#### Configuração

Na página do Canvas, selecione **Use a Canvas Template** > **Braze templates** e aplique o modelo **Confirmação de pedido e pesquisa de feedback**.

##### Configurações padrão

As seguintes configurações estão pré-configuradas no seu Canvas:

- Básico
    - Nome do Canvas: **Order confirmation with feedback survey**
    - Evento de conversão: `ecommerce.session_start`
        - Prazo de conversão: 10 dias
- Cronograma de entrada
    - Gatilho baseado em ação quando um usuário realiza o evento `ecommerce.cart_updated`
    - O horário de início é quando você cria o modelo de Canvas<br><br>!["Opções Baseadas em Ação" para o Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry.png %})<br><br>
- Público-alvo
    - Público de entrada
        - Usou esses apps **mais de 0** vezes
        - E-mail **não está em branco**
    - Controles de entrada
        - Os usuários são imediatamente reelegíveis para entrada no Canvas
    - Critérios de saída
        - Não se aplica<br><br>![Filtros adicionais e controles de entrada para o Canvas.]({% image_buster /assets/img/ecommerce/feedback_entry_exit.png %})<br><br>
- Configurações de envio
    - Usuários inscritos ou que aceitaram receber mensagens
- Etapa de mensagem
    - Revise o modelo de e-mail e o bloco HTML com um exemplo de template Liquid para adicionar produtos à sua mensagem no modelo pré-construído. Se você usar seu próprio modelo de e-mail, também pode consultar as [variáveis Liquid](#message-personalization), conforme demonstrado na seção a seguir.

#### Personalização de confirmação de pedido para e-mails {#order-confirmation-personalization-for-emails}

Aqui está um exemplo de como você adicionaria um bloco de produto HTML à sua confirmação de pedido após um pedido ser realizado.

{% raw %}
```json
<table aria-label="Order confirmation personalization for emails" style="width:100%">
  {% for item in {{context.${products}}} %}
  {% catalog_items <add_your_catalog_name> {{item.variant_id}} %}
  <tr>
    <th><img src="{{ items[0].variant_image_url }}" width="200" height="200" /></th>
    <th align="left">
      <ul style="list-style-type: none">
        <li>Item: {{item.product_name}}</li>
        <li>Price: {{item.price}}</li>
        <li>Quantity: {{item.quantity}}</li>
      </ul>
    </th>
  </tr>
  {% endfor %}
</table>
```
{% endraw %}

##### URL de status do pedido {#order-status-url}

{% raw %}
```liquid
{{context.${metadata}.order_status_url}}
```
{% endraw %}

{% endtab %}
{% endtabs %}