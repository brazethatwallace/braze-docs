---
nav_title: Direcionamento por localização
article_title: Direcionamento por localização
page_order: 7
page_type: tutorial
tool:
- Segments
- Location
description: "Este artigo prático mostra como configurar o direcionamento por localização, permitindo segmentar usuários com base na localização."

---

# Direcionamento por localização {#location-targeting}

> Este artigo mostra como configurar o direcionamento por localização, permitindo segmentar usuários pela localização mais recente.

## Etapa 1: Crie seu Segment or segmento {#step-1-create-your-segment}

Navegue até a página **Segments**, em **Público**, para visualizar todos os seus Segments de usuários atuais. Nessa página, você pode criar e nomear novos Segments. Para começar, selecione **Create Segment** e dê um nome ao seu Segment.

![Modal para criar um Segment or segmento.]({% image_buster /assets/img_archive/createsegment2.png %}){: style="max-width:70%;"}

## Etapa 2: Personalize sua localização {#step-2-customize-your-location}

Depois de criar seu Segment or segmento, adicione um filtro `Most Recent Location` para destacar os usuários pelo último local em que usaram seu app. Você tem a opção de destacar usuários dentro ou fora de uma região circular padrão ou de uma região poligonal personalizável.

![Filtro para a localização mais recente dentro de um círculo.]({% image_buster /assets/img_archive/filter_recent_location.png %})

### Usuários sem dados de localização {#users-without-location-data}

Usuários sem dados de localização — incluindo usuários cuja localização foi registrada anteriormente e depois apagada — correspondem aos filtros `most recent location outside of circle` e `most recent location outside of polygon`. Para excluir usuários sem dados de localização, combine o filtro `Most Recent Location` com um filtro `Location Available`.

{% tabs %}
{% tab Circular %}

### Regiões circulares {#circular-regions}

Para regiões circulares, você pode mover a origem e ajustar o raio de localização para sua segmentação.

![Um contorno circular de cidades entre New Jersey e Nova York.]({% image_buster /assets/img_archive/location_circle.png %}){: style="max-width:70%;"}

{% endtab %}
{% tab Poligonal %}

### Regiões poligonais {#polygonal-regions}

Para regiões poligonais, você pode designar de forma mais específica quais áreas deseja incluir no seu Segment or segmento.

![Um contorno do estado de Nova York como a região poligonal selecionada.]({% image_buster /assets/img_archive/create_polygon.png %}){: style="max-width:70%;"}

{% endtab %}
{% endtabs %}

## Suporte de parceiros para beacons e geofences {#partnership-support-for-beacon-and-geofence}

Combinar o suporte existente a beacons ou geofences com nossos recursos de direcionamento e envio de mensagens fornece mais informações sobre as ações físicas dos seus usuários, permitindo enviar mensagens de acordo. Você pode alavancar o monitoramento de localização com alguns dos nossos parceiros:

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare)