---
nav_title: monitoramento de localização
article_title: monitoramento de localização
page_order: 0
page_type: reference
description: "Este artigo de referência explica como usar o monitoramento de localização e o direcionamento por localização nos seus apps e quais parceiros oferecem suporte ao monitoramento de localização."
tool: Location
search_rank: 2
---

# Monitoramento de localização {#location-tracking}

> A coleta de localização captura a localização mais recente do usuário quando o app foi aberto, usando dados de localização por GPS. Você pode usar essas informações para segmentar dados com base em usuários que estiveram em um local definido.

## Ativação do monitoramento de localização {#enabling-location-tracking}

Para ativar a coleta de localização no seu app, consulte o guia do desenvolvedor para a plataforma que você está usando:

- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=swift)
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=android)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=web)

De modo geral, apps móveis usam o chip GPS do dispositivo e outros sistemas (como escaneamento de Wi-Fi) para rastrear a localização do usuário. Apps web usam WPS (Wi-Fi Positioning System) para rastrear a localização do usuário. Todas essas plataformas exigem que os usuários façam aceitação do monitoramento de localização. A precisão dos seus dados de monitoramento de localização pode ser afetada dependendo de o usuário ter ou não o Wi-Fi ativado no dispositivo. Usuários Android também podem escolher diferentes modos de localização — usuários que estão no modo "Economia de bateria" ou "Somente dispositivo" podem ter dados imprecisos.

### Localização do usuário no SDK por endereço IP {#sdk-user-location-by-ip-address}

A Braze detecta a localização dos usuários a partir do país geolocalizado usando o endereço IP desde o início da primeira sessão do SDK.

Anteriormente, a Braze usava o código do país da localidade do dispositivo durante a criação do usuário no SDK e durante toda a primeira sessão. Somente após o processamento do início da primeira sessão o endereço IP era usado para definir o país mais confiável no perfil do usuário. Isso significava que o país do usuário era definido com maior precisão somente a partir da segunda sessão em diante, apenas após o processamento do início da primeira sessão.

Agora, a Braze usa o endereço IP para definir o valor do país nos perfis de usuário criados pelo SDK, e essa definição de país baseada em IP está disponível durante e após a primeira sessão.

#### Coleta automática de localização {#automatic-location-collection}

Quando ativada, a coleta automática de localização no SDK é separada do comportamento de país baseado em IP. Ela se refere a sinais de localização do dispositivo, como GPS, quando o usuário concedeu permissão, e alimenta filtros como `Most Recent Location`. Ela não preenche automaticamente campos detalhados, como cidade, apenas a partir do IP.

Para direcionamento por cidade ou código postal, use [`setLastKnownLocation()`]({{site.baseurl}}/developer_guide/analytics/tracking_location) (consulte o artigo do SDK para a sua plataforma), seu próprio serviço de geolocalização por IP gravando atributos personalizados ou [Direcionamento por localização]({{site.baseurl}}/user_guide/audience/segments/location_targeting) com os dados que você coletar.

## Direcionamento por localização {#location-targeting}

Usando dados de monitoramento de localização e segmentos, você pode configurar campanhas e estratégias baseadas em localização. Por exemplo, você pode querer executar uma campanha promocional para usuários que moram em uma região específica ou excluir usuários em uma região que possui regulamentações mais rígidas.

Consulte [Direcionamento por localização]({{site.baseurl}}/user_guide/audience/segments/location_targeting) para mais informações sobre como criar um segmento de localização.

## Definição fixa do atributo de localização padrão {#hard-setting-the-default-location-attribute}

Você também pode usar o [endpoint `users/track`]({{site.baseurl}}/api/endpoints/user_data/post_user_track) na nossa API para atualizar o atributo padrão [`current_location`]({{site.baseurl}}/api/objects_filters/user_attributes_object#braze-user-profile-fields). Um exemplo:

```
https://[your_braze_rest_endpoint]/users/track
Content-Type: application/json
Authorization: Bearer YOUR-REST-API-KEY
{
  "attributes": [
 	{
 	  "external_id" : "XXX",
 	  "current_location" : {"longitude":-0.118092, "latitude": 51.509865}
      }
   ]
}
```

## Suporte de parceiros para beacons e geofences {#partnership-support-for-beacon-and-geofence}

Combinar o suporte existente a beacons ou geofences com nossos recursos de direcionamento e envio de mensagens fornece mais informações sobre as ações físicas dos seus usuários, permitindo que você envie mensagens de acordo. Você pode alavancar o monitoramento de localização com alguns dos nossos parceiros:

- [Radar]({{site.baseurl}}/partners/message_personalization/location/radar)
- [Infillion]({{site.baseurl}}/partners/message_personalization/location/infillion)
- [Foursquare]({{site.baseurl}}/partners/message_personalization/location/foursquare)

## Diferenças entre geofences e monitoramento de localização {#differences-between-geofences-and-location-tracking}

{% multi_lang_include locations_and_geofences/geofences_vs_location_tracking.md %}

## Perguntas frequentes {#frequently-asked-questions}

### Quando a Braze coleta dados de localização? {#when-does-braze-collect-location-data}

A Braze só coleta a localização quando o aplicativo está aberto em primeiro plano. Como resultado, nosso filtro `Most Recent Location` direciona os usuários com base no local onde eles abriram o aplicativo pela última vez (também chamado de início de sessão).

Você também deve ter em mente as seguintes nuances:

- Se a localização estiver desativada, o filtro `Most Recent Location` mostra a última localização registrada.
- Se um usuário já teve uma localização armazenada no perfil, ele se qualifica para o filtro `Location Available`, mesmo que tenha desativado o monitoramento de localização desde então.

### Qual é a diferença entre os filtros Most Recent Device Locale e Most Recent Location? {#whats-the-difference-between-the-most-recent-device-locale-and-most-recent-location-filters}

O `Most Recent Device Locale` vem das configurações do dispositivo do usuário. Por exemplo, para usuários de iPhone, isso aparece no dispositivo em **Ajustes** > **Geral** > **Idioma e Região**. Esse filtro é usado para capturar idioma e formatação regional, como datas e endereços, e é independente do filtro `Most Recent Location`.

O `Most Recent Location` é a última localização GPS conhecida do dispositivo. Ele é atualizado no início da sessão e armazenado no perfil do usuário.

### Se um usuário desativar o monitoramento de localização, os dados de localização anteriores são removidos da Braze? {#if-a-user-opts-out-of-location-tracking-is-their-previous-location-data-removed-from-braze}

Não. Se um usuário já teve uma localização armazenada no perfil, esses dados não são removidos automaticamente se ele desativar o monitoramento de localização posteriormente.

## Solução de problemas {#troubleshooting}

### Nenhum usuário tem localização disponível {#no-users-have-available-locations}

A Braze captura a localização mais recente do usuário por padrão pelo SDK. Isso normalmente significa que a "localização recente" é o local de onde o usuário usou o app pela última vez. Se você enviar dados de localização em segundo plano para a Braze, pode ter dados mais detalhados disponíveis.

Se nenhum usuário tiver localização disponível, duas verificações rápidas podem ajudar a confirmar a coleta e a transferência de dados.

#### Coleta de dados {#data-collection}

Confirme que seu app está coletando dados de localização:

- Para iOS, isso significa que os usuários fazem aceitação para compartilhar seus dados de localização por meio de um prompt em algum momento da jornada do usuário.
- Para Android, confirme que seu app solicita permissões de localização precisa ou aproximada na instalação.

Para verificar se os dados de localização do usuário estão sendo enviados para a Braze, use o filtro **Location Available**. Esse filtro permite ver a porcentagem de usuários com uma "localização mais recente".

![Um segmento "Test Location" que usa o filtro "Location Available".]({% image_buster /assets/img_archive/trouble7.png %})

#### Transferência de dados {#data-transfer}

Confirme que seus desenvolvedores estão enviando dados de localização para a Braze. Normalmente, o envio de dados de localização é tratado automaticamente pelo SDK após o usuário conceder permissões, mas seus desenvolvedores podem ter desativado o monitoramento de localização na Braze. Para saber mais sobre monitoramento de localização, consulte:
- [Android]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=android)
- [iOS]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=swift)
- [Web]({{site.baseurl}}/developer_guide/analytics/tracking_location?sdktab=web)