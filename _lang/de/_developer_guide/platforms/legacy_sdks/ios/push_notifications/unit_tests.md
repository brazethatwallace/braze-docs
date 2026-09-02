---
nav_title: Unit-Tests (optional)
article_title: Push-Benachrichtigung Unit-Tests für iOS
platform: iOS
page_order: 29.5
description: "Dieser Referenzartikel beschreibt, wie Sie optionale Unit-Tests für Ihre iOS-Push-Implementierung implementieren."
channel:
  - push

noindex: true
---

{% multi_lang_include deprecations/objective-c.md %}

# Unit-Tests {#unit-tests}

Diese optionale Anleitung beschreibt, wie Sie einige Unit-Tests implementieren, mit denen Sie überprüfen können, ob Ihr App-Delegate die in unseren [Anweisungen zur Push-Integration]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/push_notifications/integration) beschriebenen Schritte korrekt ausführt.

Wenn alle Tests bestanden werden, bedeutet dies im Allgemeinen, dass der codebasierte Teil Ihrer Push-Einrichtung funktionsfähig ist. Wenn ein Test fehlschlägt, kann dies bedeuten, dass Sie einen Schritt falsch befolgt haben, oder es kann das Ergebnis einer gültigen Anpassung sein, die nicht genau mit unseren Standardanweisungen übereinstimmt.

In jedem Fall kann dies ein hilfreicher Ansatz sein, um zu überprüfen, ob Sie die Integrationsschritte befolgt haben, und um eventuelle Regressionen zu erkennen.

## 1. Schritt: Ein Unit-Tests-Ziel erstellen {#step-1-creating-a-unit-tests-target}

Überspringen Sie diesen Schritt, wenn Ihr App-Projekt in Xcode bereits ein Unit Testing Bundle enthält.

Wählen Sie in Ihrem App-Projekt das Menü **File > New > Target** und fügen Sie ein neues „Unit Testing Bundle“ hinzu. Dieses Bundle kann entweder Objective-C oder Swift verwenden und einen beliebigen Namen haben. Setzen Sie das „Target to be Tested“ auf Ihr App-Hauptziel.

## 2. Schritt: Das Braze SDK zu Ihren Unit-Tests hinzufügen {#step-2-add-the-braze-sdk-to-your-unit-tests}

Stellen Sie mit der gleichen Methode, mit der Sie ursprünglich [das Braze SDK installiert]({{site.baseurl}}/developer_guide/platforms/legacy_sdks/ios/initial_sdk_setup/overview) haben, sicher, dass die gleiche SDK-Installation auch für Ihr Unit-Tests-Ziel verfügbar ist. Zum Beispiel mit CocoaPods:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
  end
end
```

## 3. Schritt: OCMock zu Ihren Unit-Tests hinzufügen {#step-3-add-ocmock-to-your-unit-tests}

Fügen Sie [OCMock](https://ocmock.org/) über CocoaPods, Carthage oder die statische Bibliothek zu Ihrem Test-Ziel hinzu. Zum Beispiel mit CocoaPods:

```
target 'YourAppTarget' do
  pod 'Appboy-iOS-SDK'

  target 'YourAppTargetTests' do
    inherit! :search_paths
    pod 'OCMock'
  end
end
```

## 4. Schritt: Installation der hinzugefügten Bibliotheken abschließen {#step-4-finish-installing-the-added-libraries}

Schließen Sie die Installation des Braze SDK und von OCMock ab. Wenn Sie zum Beispiel CocoaPods verwenden, navigieren Sie in Ihrem Terminal zum Verzeichnis Ihres Xcode-App-Projekts und führen Sie den folgenden Befehl aus:

```
pod install
```

Jetzt sollten Sie in der Lage sein, den von CocoaPods erstellten Xcode-Projekt-Workspace zu öffnen.

## 5. Schritt: Push-Tests hinzufügen {#step-5-adding-push-tests}

Erstellen Sie eine neue Objective-C-Datei in Ihrem Unit-Tests-Ziel.

Wenn das Unit-Tests-Ziel in Swift ist, fragt Xcode möglicherweise: „Would you like to configure an Objective-C bridging header?“ Der Bridging Header ist optional. Sie können also auf **Don't Create** klicken und die Unit-Tests trotzdem erfolgreich ausführen.

Fügen Sie den Inhalt der [`AppboyPushUnitTests.m`](https://github.com/Appboy/appboy-ios-sdk/blob/master/HelloSwift/HelloSwiftTests/AppboyPushUnitTests.m) aus der HelloSwift-Beispiel-App in die neue Datei ein.

## 6. Schritt: Test-Suite ausführen {#step-6-run-test-suite}

Führen Sie die Unit-Tests Ihrer App aus. Dies kann ein einmaliger Überprüfungsschritt sein, oder Sie können ihn dauerhaft in Ihre Test-Suite aufnehmen, um eventuelle Regressionen zu erkennen.