---
nav_title: MetaRouter
article_title: MetaRouter
description: "Melhore a gestão de dados de cliente na Braze com a MetaRouter. Essa solução de gerenciamento de tags no lado do servidor e de alta performance oferece o máximo de conformidade e controle com opções de implementação perfeitas, seja em uma nuvem privada hospedada pela MetaRouter ou em sua própria infraestrutura."
alias: /partners/metarouter/
page_type: partner
search_tag: Partner
---

# MetaRouter

> A [MetaRouter](https://www.metarouter.io/) eleva sua experiência na Braze ao se integrar perfeitamente como uma poderosa plataforma de gerenciamento de tags no lado do servidor. Ela permite que você orquestre uma jornada completa de dados de cliente na Braze, desde a coleta confiável de dados totalmente primários, enriquecida em até 30%, até a ativação do fluxo de eventos em tempo real para jornadas personalizadas. Além disso, a MetaRouter agiliza a implementação, eliminando a necessidade de tags da Braze ou de outras tags de terceiros. Dessa forma, você tem controle granular, parâmetro por parâmetro, dos dados transferidos para a Braze.

_Essa integração é mantida pela Metarouter._

## Recursos suportados {#supported-features}

- As novas tentativas podem ser incorporadas.
- As solicitações são agrupadas em lote.
- Os problemas de limite de taxa são tratados com uma nova tentativa.
- Há suporte para ID externo e IPI. A MetaRouter passa o ID anônimo e qualquer IPI (e-mail, número de telefone, nome) que os clientes desejarem.
- Você pode enviar dados de compras e eventos personalizados para a Braze.
  - Há suporte para propriedades de eventos.
  - Não há suporte para propriedades de eventos aninhadas.

## Pré-requisitos {#prerequisites}

Antes de começar, você precisará do seguinte:

| Requisito | Descrição |
|-----------------------|------------------------------------------------------------------------------------------------------------------------------------------------------|
| Uma conta do MetaRouter | Uma [conta do MetaRouter Enterprise](https://enterprise.metarouter.io/). |
| Chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze | Uma chave da API or interface de programação do aplicativo (API) REST or transferir estado representacional da Braze com permissões `users.track`. Para criar uma, acesse **Settings** > **API or interface de programação do aplicativo (API) Keys**. |
| Um endpoint REST or transferir estado representacional da Braze | [Sua URL de endpoint REST or transferir estado representacional]({{site.baseurl}}/developer_guide/rest_api/basics/#endpoints). Seu endpoint dependerá da URL da Braze para sua instância. |
{: .reset-td-br-1 .reset-td-br-2 role="presentation" }

## Configuração do MetaRouter {#setting-up-metarouter}

Para configurar o MetaRouter para sua integração com a Braze:

1. Acesse o MetaRouter e crie um novo cluster.
2. Escolha os eventos que deseja rastrear.
3. Instale um SDK or kit de desenvolvimento de software da MetaRouter e integre os eventos ao seu site.
4. Conecte seu cluster à interface do usuário do seu site.
5. Crie um novo pipeline.
6. Verifique se o seu site está enviando eventos para o MetaRouter.

## Integração com a Braze {#integrating-braze}

### Etapa 1: Adicionar a integração da Braze {#step-1-add-the-braze-integration}

No Enterprise MetaRouter, selecione **Integrations** > **New Integration** > **Braze** e nomeie sua integração. Em seguida, insira a URL da instância e a chave de API or interface de programação do aplicativo (API) e selecione **Apply Changes**.

![Adição da Braze como uma integração no MetaRouter.]({% image_buster /assets/img/metarouter/img1.png %}){: style="max-width:50%;"}

### Etapa 2: Adicionar mapeamento de eventos {#step-2-add-event-mapping}

Adicione o mapeamento de eventos para cada saída de identidade e, em seguida, configure os eventos que deseja enviar para a Braze. Quando terminar, selecione **Save as New Revision**.

![Adicione o mapeamento de eventos para cada uma das saídas de identidade.]({% image_buster /assets/img/metarouter/img2.png %})