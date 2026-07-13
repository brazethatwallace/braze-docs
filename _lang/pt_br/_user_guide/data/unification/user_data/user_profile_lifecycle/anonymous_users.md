---
nav_title: Usuários anônimos
article_title: Usuários anônimos
page_order: 0
page_type: reference
description: "Este artigo fornece uma visão geral dos usuários anônimos e aliases de usuário, descrevendo sua importância e como eles podem ser aproveitados em suas mensagens."

---

# Usuários anônimos {#anonymous-users}

> Os usuários que visitam seu site ou aplicativo sem fazer login, como um visitante convidado, são reconhecidos como usuários anônimos. Esses usuários não têm `external_ids`, que são usados para atualizar perfis de usuário com a API da Braze, mas eles ainda têm [pontos de dados]({{site.baseurl}}/user_guide/data/infrastructure/data_points) atribuídos a eles e podem ser direcionados em seus segmentos.

Quando um usuário anônimo visita seu site ou aplicativo, o SDK da Braze cria e atribui a ele um perfil de usuário "anônimo". Enquanto o usuário navega, o SDK captura automaticamente dados para o perfil anônimo do usuário, como informações de uso, informações do dispositivo e muito mais, se você tiver configurado atributos personalizados e eventos personalizados.

Você pode fazer o seguinte com usuários anônimos capturados:

- Enviar mensagens aos usuários antes que eles façam login
- Coletar o perfil de um usuário antes que ele faça login, para não perder dados relevantes
- Incentivar o preenchimento do perfil com uma mensagem quando um usuário preencher apenas parcialmente seu perfil
- Completar o perfil de um usuário quando ele fizer login, para que você possa cancelar o envio de mensagens em outras plataformas (por exemplo, não enviar uma mensagem de "frete grátis no primeiro pedido do app" quando o usuário já tiver feito pedidos pelo app)
- Engajar com usuários que demonstram intenção de sair, incentivando-os a criar um perfil, finalizar o carrinho ou realizar outra ação

## Como funciona {#how-it-works}

{% multi_lang_include anonymous_users/about_anonymous_users.md section='user_guide' %}

## Atribuição de aliases de usuário {#assigning-user-aliases}

{% multi_lang_include anonymous_users/about_user_aliases.md section='user_guide' %}

## Mesclando usuários anônimos {#merging-anonymous-users}

Às vezes, os perfis de usuários anônimos são duplicatas que têm o mesmo número de telefone ou endereço de e-mail que outros perfis de usuários. Uma das duplicatas pode até ser um perfil de usuário identificado. Essas duplicatas podem ser mescladas em um único perfil de usuário usando o [POST: Endpoint de mesclagem de usuários]({{site.baseurl}}/api/endpoints/user_data/post_users_merge) ou uma das ferramentas de mesclagem da plataforma Braze, como a [mesclagem baseada em regras]({{site.baseurl}}/user_guide/audience/manage_audience/merge_duplicate_users#rules-based-merging).

## Pesquisando um usuário anônimo {#looking-up-an-anonymous-user}

Como os usuários anônimos não têm um `external_id`, você pode usar um ID de dispositivo para pesquisar um perfil específico. As etapas a seguir mostram como obter o ID do dispositivo para o usuário atual na sua integração do Web SDK:

1. Abra as ferramentas de desenvolvedor do seu navegador (por exemplo, no Chrome, pressione **Command + Option + J** no Mac ou **Ctrl + Shift + I** no Windows).
2. Na guia **Console**, execute o seguinte:

```javascript
console.log(braze.getDeviceId());
```

{:start="3"}
3. No dashboard da Braze, use a [Pesquisa de usuários]({{site.baseurl}}/user_guide/engagement_tools/segments/using_user_search) para pesquisar o ID de dispositivo retornado.

## Casos de uso {#use-cases}

### Direcionar usuários anônimos no seu segmento {#target-anonymous-users-in-your-segment}

Como os usuários anônimos não têm um `external_id`, você pode direcioná-los em massa usando o filtro de segmentação **External User ID is blank**. Para maior precisão, você pode adicionar um atributo personalizado aos usuários anônimos que deseja direcionar e filtrar por ele.

Digamos que você atribua o atributo personalizado "is_lead_profile" a cada perfil de usuário anônimo. Você pode direcionar esses perfis com um ou ambos os filtros:

- **External User ID is blank**
- "is_lead_profile" **é verdadeiro**

![Filtros de segmento para um ID de usuário externo em branco e um atributo personalizado "is_lead_profile" verdadeiro.]({% image_buster /assets/img/getting_started/anonymous_users.png %})

### Capturar dados de checkout de um usuário anônimo {#capture-checkout-data-from-an-anonymous-user}

Você pode capturar dados de checkout de um usuário anônimo (ou visitante convidado) criando um perfil com alias de usuário durante o processo de checkout. Quando um usuário anônimo finaliza a compra usando um formulário de captura da web, faça com que uma chamada de API seja disparada para criar um perfil com alias de usuário e registrar um evento de compra. Você poderá então atualizar o perfil de usuário criado por meio da API da Braze.

Aqui está um exemplo de carga útil que será gerada quando o formulário de captura da web for enviado:

{% raw %}
```json
{
    "purchase":[
        {
            "user_alias": {"alias_name": "Joedoe", "alias_label": "full_name"},
            "app_id": "11dk3k9d-2183-3948-k02b-kw3938109k12od",
            "product_id": "jacket",
            "currency": "USD",
            "price": 80.00,
            "time": "2025-01-05T19:20:30+01:00",
            "properties": {
                "color": "brown",
                "monogram": "ABC",
                "checkout_duration": 180,
                "size": "Small",
                "brand": "Natural Essence"
            }
        }
    ]
}
```
{% endraw %}