{% multi_lang_include developer_guide/prerequisites/react_native.md %} Sie müssen außerdem [Push-Benachrichtigungen einrichten]({{site.baseurl}}/developer_guide/push_notifications/?sdktab=react%20native).

## Push-Anpassung in React Native {#push-customization-in-react-native}

Das Braze React Native SDK or Software-Development-Kit stellt keine Anpassungsmöglichkeiten für Push-Benachrichtigungen (Aktions-Buttons, Kategorien, angepasste Notification Factories) über seine JavaScript-API zur Verfügung. Diese Features erfordern eine native Konfiguration in Ihren iOS- und Android-Projekten.

Die folgende Tabelle zeigt, welche Features eine native Konfiguration erfordern:

| Feature | iOS | Android |
| --- | --- | --- |
| Aktions-Buttons | In nativem Swift/Objective-C konfigurieren | In nativem Java/Kotlin konfigurieren |
| Push-Kategorien | In nativem Swift/Objective-C konfigurieren | In nativem Java/Kotlin konfigurieren |
| Angepasste Notification Factory | N/A | In nativem Java/Kotlin konfigurieren |
| Badge-Anpassung | In nativem Swift/Objective-C konfigurieren | N/A |
| Angepasste Sounds | In nativem Swift/Objective-C konfigurieren | In nativem Java/Kotlin konfigurieren |
{: .reset-td-br-1 .reset-td-br-2 .reset-td-br-3 aria-label="Push customization in React Native" }

### iOS-Anpassung {#ios-customization}

Um Push-Aktions-Buttons, Kategorien, Badges oder angepasste Sounds unter iOS hinzuzufügen, implementieren Sie die native Konfiguration in Ihrem `AppDelegate` (Swift oder Objective-C). Eine Schritt-für-Schritt-Anleitung finden Sie unter [Push-Benachrichtigungen anpassen – Swift]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=swift).

### Android-Anpassung {#android-customization}

Um Push-Aktions-Buttons, Kategorien oder eine angepasste Notification Factory auf Android hinzuzufügen, implementieren Sie die native Konfiguration in Ihrem Android-Projekt. Eine Schritt-für-Schritt-Anleitung finden Sie unter [Push-Benachrichtigungen anpassen – Android]({{site.baseurl}}/developer_guide/push_notifications/customization/?sdktab=android).