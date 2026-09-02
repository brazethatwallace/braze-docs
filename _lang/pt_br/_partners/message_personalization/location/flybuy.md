---
nav_title: Flybuy
article_title: Flybuy
alias: /partners/flybuy/
description: "Este artigo de referência descreve a parceria entre a Braze e a Flybuy, uma plataforma de serviços de localização, para adicionar inteligência de localização às suas operações e capacidades de marketing."
page_type: partner
search_tag: Partner

---

# Flybuy

> A [Flybuy](https://www.flybuy.com/), da Radius Networks, é a principal plataforma omnicanal de localização que utiliza tecnologia baseada em IA para otimizar a velocidade do atendimento em retirada, entrega, drive-thru e consumo no local. Por meio de seu Marketing Suite integrado, a Flybuy também permite que as marcas entreguem mensagens hiperdirecionadas e baseadas em momentos, ajudando a impulsionar o engajamento, aumentar o ticket médio e apoiar iniciativas mais amplas de fidelidade.

_Esta integração é mantida pela Flybuy._

## Sobre a integração {#about-the-integration}

A Flybuy entrega eventos ricos de inteligência do usuário na Braze, permitindo que as marcas enviem mensagens hiperrelevantes e baseadas em localização com o mais alto nível de personalização. Quando um usuário gera um evento na Flybuy, eventos personalizados com atributos personalizados ricos são entregues à Braze. Esses eventos e atributos podem ser usados para potencializar operações omnicanal e disparar mensagens baseadas em proximidade.

## Pré-requisitos {#prerequisites}

O seguinte é necessário antes de ativar a integração:

| Requisito | Descrição |
|---|---|
| Conta Flybuy | Uma conta Flybuy com pelo menos um projeto. |
| Chave da API REST da Braze | Uma chave da API REST da Braze com permissões `users.track`. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Pré-requisitos" }

## Integração {#integration}

Para ativar a integração, siga as etapas a seguir:

1. No portal Flybuy Merchant, navegue até **Project Info** e clique em **Events Engine**.
2. Clique em **Add a Destination** e selecione **Braze**.
3. Adicione sua chave de API e endpoint da Braze e selecione os eventos que deseja ativar.
4. Clique em **Finish Setup**.

{% alert important %}
A Flybuy mapeia `loyalty_id` para o `external_id` da Braze para usuários logados.
{% endalert %}

## Casos de uso {#use-cases}

- [Pickup](https://www.flybuy.com/flybuypickup)
- [Delivery](https://www.flybuy.com/flybuydelivery)
- [Drive-Thru](https://www.flybuy.com/flybuydrivethru)
- [Table Service](https://www.flybuy.com/flybuytableservice)
- [Hotel Mobile Check-In and Ordering](https://www.flybuy.com/industries/hospitality)
- [Marketing Suite](https://www.flybuy.com/flybuy-marketing-suite)

## Exemplos de gatilhos baseados em eventos e atributos {#event-and-attribute-based-trigger-examples}

Eventos personalizados e atributos personalizados podem ser usados para potencializar uma variedade de experiências personalizadas.

### Criar um Segment de público de clientes que tiveram uma experiência ruim de retirada {#build-an-audience-segment-of-customers-who-had-a-bad-pickup-experience}

Por exemplo, direcione qualquer cliente que avaliou sua experiência de retirada com menos de 5 estrelas.

![Segmento para experiência ruim de retirada]({% image_buster /assets/img/flybuy/flybuy1.png %})

### Disparar um alerta quando um cliente entra em uma área virtual de retirada {#trigger-an-alert-when-a-customer-enters-a-virtual-pickup-area}

Envie um SMS personalizado direcionado a clientes sem conta de fidelidade para baixar o app e criar uma conta de fidelidade.

![Disparar um alerta quando um cliente entra em uma área virtual de retirada]({% image_buster /assets/img/flybuy/flybuy2.png %})

![Mensagem de alerta quando um cliente entra em uma área virtual de retirada]({% image_buster /assets/img/flybuy/flybuy2a.png %})

### Criar um Segment de público de clientes que tiveram um longo tempo de espera {#build-an-audience-segment-of-customers-who-had-a-long-wait-time}

Por exemplo, direcione qualquer cliente que teve um tempo de espera superior a dois minutos ao sair de uma área virtual da loja.

![Criar um segmento de público de clientes que tiveram um longo tempo de espera]({% image_buster /assets/img/flybuy/flybuy3.png %})

### Disparar um alerta de correção de rota quando um cliente está indo para o local errado {#trigger-a-course-correction-alert-when-a-customer-is-headed-to-the-wrong-location}

Envie uma notificação por push para clientes quando eles estiverem indo ou tiverem chegado a um local diferente de onde fizeram o pedido.

### Entregar ofertas especiais com base em marcos de viagem {#deliver-special-offers-based-on-trip-milestones}

Por exemplo, envie uma oferta especial quando um cliente VIP chegar aos seus locais favoritos.

### Criar um Segment de público de clientes com itens faltando no pedido {#build-an-audience-segment-of-customers-who-were-missing-items-in-their-order}

Por exemplo, direcione qualquer cliente que comentou que itens estavam faltando em seu pedido digital.

Para mais detalhes sobre APIs e SDKs, consulte a [documentação para desenvolvedores da Flybuy](https://www.radiusnetworks.com/developers/flybuy/#/).