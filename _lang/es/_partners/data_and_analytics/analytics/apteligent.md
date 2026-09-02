---
nav_title: Apteligent
article_title: Apteligent
alias: /partners/apteligent/
description: "Este artículo de referencia describe la asociación entre Braze y Apteligent, una aplicación móvil que detalla los informes de fallos, permitiéndote registrar datos críticos en tu solución Braze existente."
page_type: partner
search_tag: Partner

---

# Apteligent

> [Apteligent](https://www.vmware.com/products/workspace-one/intelligence-consumer-apps.html) es una plataforma de rendimiento de aplicaciones móviles que proporciona herramientas e información a desarrolladores y administradores de productos.

_Esta integración está mantenida por Apteligent._

## Sobre la integración {#about-the-integration}

La integración de Braze y Apteligent proporciona informes detallados de fallos de iOS, lo que te permite registrar datos críticos en tu solución Braze existente, así como segmentar, comprender e interactuar con los usuarios que han experimentado fallos en la aplicación.

## Requisitos previos {#prerequisites}

| Requisito | Descripción |
|---|---|
| Cuenta TestDrive | Se necesita una cuenta de TestDrive para beneficiarte de esta asociación. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Requisitos previos" }

{% alert warning %}
Actualmente, esta integración solo es compatible con iOS.
{% endalert %}

## Integración {#apteligent-ios-integration}

### Paso 1: Registrar un observador {#step-1-register-an-observer}

En primer lugar, debes registrar un observador. Asegúrate de que esto esté hecho antes de inicializar Apteligent.

```objc
[[NSNotificationCenter defaultCenter] addObserver:self
                                         selector:@selector(crashDidOccur:)
                                             name:@"CRCrashNotification"
                                           object:nil];
```

### Paso 2: Registrar análisis de fallos personalizados {#step-2-log-custom-crash-analytics}

El SDK or kit de desarrollo de software de Apteligent enviará una notificación cuando el usuario cargue la aplicación después de que se produzca un fallo. La notificación contendrá el nombre del fallo, el motivo y la fecha en que ocurrió.

Al recibir la notificación, registra un evento de fallo personalizado y actualiza los atributos del usuario con los análisis de informes de fallos de Apteligent:

```objc
- (void)crashDidOccur:(NSNotification*)notification {
  NSDictionary *crashInfo = notification.userInfo;
  [[Appboy sharedInstance] logCustomEvent:@"ApteligentCrashEvent" withProperties:crashInfo];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashName" andStringValue:crashInfo[@"crashName"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashReason" andStringValue:crashInfo[@"crashReason"]];
  [[Appboy sharedInstance].user setCustomAttributeWithKey:@"lastCrashDate" andDateValue:crashInfo[@"crashDate"]];
}
```

Una vez completado, podrás aprovechar el poder de la segmentación y los análisis de interacción de Braze utilizando la información sobre fallos que se encuentra en la plataforma Apteligent.