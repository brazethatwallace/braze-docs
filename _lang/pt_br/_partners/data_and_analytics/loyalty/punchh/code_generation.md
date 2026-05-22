---
nav_title: Geração de código dinâmico
article_title: Geração de código dinâmico Punchh
page_order: 2
description: "Este artigo de referência descreve como usar a geração de código dinâmico Punchh na Braze."
page_type: partner
search_tag: Partner
---

# Geração de código dinâmico com Punchh {#dynamic-code-generation-with-punchh}

> Um código de cupom é um código exclusivo que pode ser usado por um único usuário (uso único ou múltiplo). A estrutura Punchh gera códigos de cupom, que podem ser processados em um app móvel ou no sistema de ponto de venda (POS).

_Essa integração é mantida pela Punchh._

## Sobre a integração {#about-the-integration}

Usando a estrutura de cupom Punchh e a Braze, você pode realizar os seguintes cenários:

- Gerar um código de cupom quando o convidado clicar em um link de geração de cupom em um e-mail: o código do cupom será gerado dinamicamente e exibido em uma página da web.
- Gerar um código de cupom quando o convidado abrir um e-mail: o código do cupom será gerado dinamicamente e mostrado como uma imagem no e-mail.

## Integração da geração de código de cupom dinâmico {#integrating-dynamic-coupon-code-generation}

### Etapa 1: Criar uma campanha de cupons {#step-1-create-a-coupon-campaign}

1. Usando uma campanha de cupom Punchh, crie uma campanha de cupom de geração dinâmica, conforme mostrado na imagem a seguir.
2. A estrutura de cupons da Punchh gerará os seguintes parâmetros para ativar a geração dinâmica de cupons:
    - Token de geração de cupom dinâmico: esse é um token de segurança gerado pelo sistema para criptografia.
    - URL de geração de cupom dinâmico: esse URL será incorporado ao e-mail como um link ou imagem, conforme exigido pela empresa.

![O formulário para criar uma campanha de cupom no Punchh.]({% image_buster /assets/img/punchh/punchh8.png %}){: style="max-width:60%;"}

### Etapa 2: Gerar a assinatura e construir o URL {#step-2-generate-signature-and-construct-url}

A biblioteca JWT.IO decodifica, verifica e gera JSON web tokens, um método RFC 7519 aberto e padrão do setor para representar declarações de forma segura entre duas partes.

Os seguintes nomes `ClaimType` podem ser usados para garantir a exclusividade de convidados e cupons:

- `campaign_id`: representa o ID da campanha Punchh gerado pelo sistema.
- `email`: representa o endereço de e-mail do usuário.
- `first_name`: captura o nome do usuário.
- `last_name`: captura o sobrenome do usuário.

Para usar a API de código de cupom dinâmico da Punchh, um token JWT deve ser construído. Adicione o seguinte modelo Liquid ao seu dashboard da Braze no corpo da mensagem do canal que deseja usar:

{% raw %}
```liquid
{% assign header = '{"alg":"HS256","typ":"JWT"}' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% capture payload_raw %}

{
  "campaign_id": "CAMPAIGN_ID",
  "email": "{{${email_address}}}",
  "first_name": "{{${first_name}}}",
  "last_name": "{{${last_name}}}"
}

{% endcapture %}

{% assign payload = payload_raw | replace: ' ', '' | replace: '\n', '' | base64_encode | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign unsigned_token = header | append: "." | append: payload %}

{% assign secret = "DYNAMIC_COUPON_GENERATION_TOKEN" %}

{% assign signature_raw = unsigned_token | hmac_sha256_base64: secret %}

{% assign signature = signature_raw | replace: '=', '' | replace: '+', '-' | replace: '/', '_' %}

{% assign jwt = unsigned_token | append: "." | append: signature %}

```
{% endraw %}


Substitua o seguinte:

| Espaço reservado | Descrição |
|--------------------|------------------------------------------------------|
| `DYNAMIC_COUPON_GENERATION_TOKEN` | Seu token de geração de cupom dinâmico. |
| `CAMPAIGN_ID` | Seu ID de campanha. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Step 2: Generate signature and construct URL" }

### Etapa 3: Anexar o código do cupom ao corpo da mensagem {#step-3-append-coupon-code-to-message-body}

#### Vinculando à página web da Punchh {#linking-to-punchh-web-page}

Para criar um link para uma página da web hospedada pela Punchh, adicione `{% raw %}{{jwt}}{% endraw %}` ao URL de geração dinâmica [que você criou anteriormente](#step-1-create-a-coupon-campaign-in-punchh). Seu link deve ser semelhante ao seguinte:

{% raw %}
```
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX?sign={{jwt}}
```
{% endraw %}

Quando um usuário clicar no URL do cupom, ele será redirecionado para uma página da web hospedada pela Punchh, onde o cupom gerado será exibido.

![Exemplo de mensagem de confirmação depois que um usuário gera com sucesso um código de cupom.]({% image_buster /assets/img/punchh/punchh7.png %})

#### Extraindo o código via JSON como texto simples {#extracting-code-via-json-as-plain-text}

Para retornar uma resposta JSON, acrescente `{% raw %}{{jwt}}{% endraw %}` ao URL de geração dinâmica [que você criou anteriormente](#step-1-create-a-coupon-campaign-in-punchh) e, em seguida, adicione `.json` após o token na string do URL. Seu link deve ser semelhante ao seguinte:

{% raw %}
```liquid
https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}}
```
{% endraw %}

Você pode então aproveitar o [Conteúdo conectado]({{site.baseurl}}/user_guide/messaging/design_and_edit/personalize/connected_content/making_an_api_call/) para inserir o código como texto simples em qualquer corpo de mensagem. Por exemplo:

{% raw %}
```liquid
{% connected_content https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.json?sign={{jwt}} :save punchh_coupon %}
{{punchh_coupon.coupon}}
````
{% endraw %}

#### Vinculando uma imagem no conteúdo do e-mail {#linking-an-image-inside-email-content}

Para vincular o código do cupom em uma imagem:

1. Acrescente `{% raw %}{{jwt}}{% endraw %}` ao URL de geração dinâmica [que você criou anteriormente](#step-1-create-a-coupon-campaign-in-punchh).
2. Adicione `.png` após o token na string do URL.
3. Incorpore seu link em uma tag HTML {% raw %}`<img>`{% endraw %}.

{% tabs local %}
{% tab exemplo de entrada %}
{% raw %}
```liquid
<img src="https://fakebrandz.punchh.com/request_coupons/7xY3bL9jRfZ1pA6mc8qD2eS4vT5wX.png?sign={{jwt}}">
````
{% endraw %}
{% endtab %}

{% tab exemplo de saída %}
![Saída renderizada da tag de imagem do código do cupom.]({% image_buster /assets/img/punchh/punchh9.png %})
{% endtab %}
{% endtabs %}

## Mensagens de erro {#error-messages}

| Código de erro | Mensagem de erro | Descrição |
| --- | --- | --- |
| `coupon_code_expired` | This promo code has expired | O código é usado após a data de expiração configurada. |
| `coupon_code_success` | Congratulations, Promo Code Applied Successfully. | O código é usado com sucesso. |
| `coupon_code_error` | Please enter a valid promo code | O código usado é inválido. |
| `coupon_code_type_error` | Incorrect coupon type. This coupon can only be redeemed at `%{coupon_type}`. | Quando um código que deveria ser usado no POS é usado no app móvel, esse erro ocorre. |
| `usage_exceeded` | The usage for this coupon code's campaign is full. Please try next time. | O uso do código excede o número de usuários autorizados a usá-lo. Por exemplo, se a configuração do dashboard permitir que um código seja usado por 3.000 usuários e o número de usuários exceder 3.000, esse erro ocorrerá. |
| `usage_exceeded_by_guest` | This promo code has already been processed. | O uso do código por um usuário excede o número de vezes que ele pode usá-lo. Por exemplo, a configuração do dashboard permite que um único código seja usado três vezes por um usuário. Se for usado mais do que isso, esse erro ocorrerá. |
| `already_used_by_other_guest` | This promo code has already been used by some other guest. | Outro usuário já usou o código. |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Error messages" }