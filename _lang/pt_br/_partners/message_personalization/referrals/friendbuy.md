---
nav_title: AmigoCompra
article_title: AmigoCompra
description: "Aprenda a integrar o Friendbuy com a Braze."
alias: /partners/friendbuy/
page_type: partner
search_tag: Partner

---

# Friendbuy

> Use a integração entre o [Friendbuy](https://www.friendbuy.com/) e a Braze para expandir seus recursos de e-mail e SMS e, ao mesmo tempo, automatizar sem esforço as comunicações do seu programa de indicação e fidelidade. A Braze gerará perfis de clientes para todos os números de telefone com opt-in coletados via Friendbuy.

_Essa integração é mantida pela Friendbuy._

## Pré-requisitos {#prerequisites}

Antes de começar, você precisará do seguinte:

| Pré-requisito | Descrição |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------|
| Uma conta Friendbuy | Uma [conta Friendbuy](https://retailer.friendbuy.io/) é necessária para aproveitar esta parceria. |
| Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões `users.track`. Isso pode ser criado no dashboard da Braze em **Settings** > **API or interface de programação do aplicativo (API) Keys**. |
| Um endpoint REST or transferir estado representacional da Braze | [A URL do seu endpoint REST or transferir estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints), que depende da URL da sua instância da Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integrando o Friendbuy {#integrating-friendbuy}

No [Friendbuy](https://retailer.friendbuy.io/), acesse **Developer Center** > **Integrations** e, no cartão de integração da Braze, selecione **Add integration**.

![O cartão de integração da Braze no Friendbuy.]({% image_buster /assets/img/friendbuy/choosing_braze.png %}){: style="max-width:75%;"}

No formulário, insira seu endpoint REST or transferir estado representacional e chave de API or interface de programação do aplicativo (API) e selecione **Install Integration**.

![O formulário de integração do Friendbuy.]({% image_buster /assets/img/friendbuy/install_form.png %}){: style="max-width:55%;"}

Volte à sua [conta do Friendbuy](https://retailer.friendbuy.io/) e atualize a página. Se a integração foi bem-sucedida, você verá uma mensagem semelhante à seguinte:

![Integração instalada]({% image_buster /assets/img/friendbuy/install_success.png %}){: style="max-width:55%;"}

### Atributos personalizados {#custom-attributes}

| Nome do atributo personalizado | Definição | Tipo de dados |
|----------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------|-----------|
| **Friendbuy Referral Status** | Os indicadores são categorizados como *Advocate* e os indicados são categorizados como *Referred Friend* | String |
| **Friendbuy Customer Name** | O nome que o cliente inseriu ao enviar suas informações por meio de um widget de indicação | String |
| **Friendbuy Referral Link** | Um link de indicação pessoal (PURL) gerado para um Advocate. Por exemplo, https://fbuy.io/EzcW | String |
| **Friendbuy Date of Last Share** | A data e hora em que o Advocate compartilhou pela última vez com um amigo por qualquer canal de compartilhamento. Se o Advocate ainda não compartilhou, a propriedade não estará visível. | Horário |
| **Friendbuy Campaign ID** | O ID da Campaign associado ao link de indicação pessoal gerado para um Advocate | String |
| **Friendbuy Campaign Name** | O nome da Campaign associado ao link de indicação pessoal gerado para um Advocate | String |
| **Friendbuy Coupon Code** | O código de cupom de indicação mais recente distribuído ao cliente. Nota: apenas um código será exibido | String |
| **Friendbuy Coupon Value** | O valor monetário do código de cupom mais recente distribuído ao cliente. | Número |
| **Friendbuy Coupon Status** | O status do código de cupom mais recente distribuído ao cliente. Nota: o status será "distributed" ou "redeemed" | String |
| **Friendbuy Coupon Currency** | Código da moeda (USD, CAD, etc.) ou porcentagem (%) associada ao código de cupom mais recente distribuído ao cliente. | String |
| **Friendbuy Coupon Campaign ID** | O ID da Campaign associado ao código de cupom gerado para um cliente. | String |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Atributos personalizados" }

## Comportamento padrão {#default-behavior}

Antes que os dados de cliente possam ser enviados para a Braze, os clientes devem fazer opt-in por meio do widget de indicação, marcando uma ou mais das seguintes caixas:

![Widget de indicação]({% image_buster /assets/img/friendbuy/referral_widget.png %})

{% alert note %}
O Friendbuy usa o padrão internacional (E.164) para verificar números de telefone reais. Números inválidos, como `555-555-5555`, não serão enviados para a Braze.
{% endalert %}

### Comportamento da caixa de seleção {#checkbox-behavior}

| Caixa de seleção marcada | Comportamento |
|-------------------|-----------------------------------------------------------------|
| Apenas e-mail | Apenas o endereço de e-mail do cliente é enviado para a Braze. |
| Apenas telefone | Apenas o número de telefone do cliente é enviado para a Braze. |
| Nenhuma | Nenhum dado de cliente é enviado para a Braze. |
| Ambas | O endereço de e-mail e o número de telefone do cliente são enviados para a Braze. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Comportamento da caixa de seleção" }