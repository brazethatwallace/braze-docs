{% alert important %}
Os geofences são suportados em **ambos iOS e Android** no SDK or kit de desenvolvimento de software do React Native. O método `requestLocationInitialization` é exclusivo do Android e não é necessário para iOS. O método `requestGeofences` está disponível em ambas as plataformas. Por padrão, o SDK or kit de desenvolvimento de software pode solicitar e monitorar geofences automaticamente quando a localização está disponível; você pode confiar nessa configuração automática ou chamar `requestGeofences` para solicitar manualmente.
{% endalert %}

{% multi_lang_include developer_guide/prerequisites/react_native.md %}

## Configurando geofences {#setting-up-geofences}

### Etapa 1: Ativar na Braze {#step-1-enable-in-braze}

{% multi_lang_include developer_guide/_shared/enable_geofences_in_braze.md %}

### Etapa 2: Completar a configuração nativa do Android {#step-2-complete-native-android-setup}

Como o SDK or kit de desenvolvimento de software do React Native usa o SDK or kit de desenvolvimento de software nativo da Braze para Android, complete a configuração nativa de geofence do Android para o seu projeto. O equivalente para iOS dessas etapas é abordado no guia de geofences do SDK or kit de desenvolvimento de software nativo Swift ([etapas 2.2 a 3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module); a etapa 2.1 (Adicionar o módulo BrazeLocation) não é necessária para o React Native porque o BrazeLocation já está incluído implicitamente no SDK or kit de desenvolvimento de software da Braze para React Native.

1. **Atualizar `build.gradle`:** Adicione `android-sdk-location` e os serviços de localização do Google Play. Veja [geofences do Android]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).
2. **Atualizar o manifesto:** Adicione permissões de localização e o receptor de inicialização da Braze. Veja [geofences do Android]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).
3. **Ativar a coleta de localização da Braze:** Atualize seu arquivo `braze.xml`. Veja [geofences do Android]({{site.baseurl}}/developer_guide/geofences/?sdktab=android).

### Etapa 3: Completar a configuração nativa do iOS {#step-3-complete-native-ios-setup}

Como o SDK or kit de desenvolvimento de software do React Native usa o SDK or kit de desenvolvimento de software nativo da Braze para iOS, complete a configuração nativa de geofence do iOS para o seu projeto seguindo as instruções do SDK or kit de desenvolvimento de software nativo Swift a partir da etapa 2.2: atualize seu `Info.plist` com descrições de uso de localização (etapa 2.2) e ative geofences na sua configuração da Braze, incluindo `automaticGeofenceRequests = true` (etapa 3); opcionalmente, ative o relatório em segundo plano (etapa 3.1). A etapa 2.1 (Adicionar o módulo BrazeLocation) não é necessária — o BrazeLocation já está incluído implicitamente no SDK or kit de desenvolvimento de software da Braze para React Native. Veja [geofences do iOS, etapas 2.2 a 3.1]({{site.baseurl}}/developer_guide/geofences/?sdktab=swift#swift_step-21-add-the-brazelocation-module).

### Etapa 4: Solicitar geofences pelo JavaScript {#step-4-request-geofences-from-javascript}

**No Android:** Depois que o usuário conceder permissões de localização, chame `requestLocationInitialization()` para inicializar os recursos de localização da Braze e solicitar geofences dos servidores da Braze. Esse método não é suportado no iOS e não é necessário para o iOS.

**No iOS:** O equivalente é ativar a configuração `automaticGeofenceRequests` na sua configuração nativa Swift ou Objective-C da Braze (veja a Etapa 3). Com isso ativado, o SDK or kit de desenvolvimento de software solicita e monitora automaticamente geofences quando a localização está disponível; nenhuma chamada JavaScript equivalente a `requestLocationInitialization` é necessária.

```javascript
import Braze from '@braze/react-native-sdk';

// Android only: call this after the user grants location permission
Braze.requestLocationInitialization();
```

### Etapa 5: Solicitar geofences manualmente (opcional) {#step-5-manually-request-geofences-optional}

Em iOS e Android, você pode solicitar manualmente uma atualização de geofence para uma coordenada GPS específica usando `requestGeofences`. Por padrão, a Braze recupera automaticamente a localização do dispositivo e solicita geofences. Para fornecer manualmente uma coordenada:

1. Desative as solicitações automáticas de geofence. No Android, defina `com_braze_automatic_geofence_requests_enabled` como `false` no seu `braze.xml`. No iOS, defina `automaticGeofenceRequests` como `false` na sua configuração da Braze.
2. Chame `requestGeofences` com a latitude e longitude desejadas:

```javascript
import Braze from '@braze/react-native-sdk';

Braze.requestGeofences(33.078947, -116.601356);
```

{% alert important %}
Os geofences só podem ser solicitados uma vez por sessão, seja automaticamente pelo SDK or kit de desenvolvimento de software ou manualmente com esse método.
{% endalert %}