{% multi_lang_include developer_guide/prerequisites/swift.md %}

## UI 델리게이트 설정(필수) {#setting-up-the-ui-delegate-required}

인앱 메시지의 표시를 사용자 지정하고 다양한 생명주기 이벤트에 반응하려면 [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate)를 설정해야 합니다. 이것은 트리거된 인앱 메시지 페이로드를 수신 및 처리하고, 표시 생명주기 이벤트를 수신하며, 표시 타이밍을 제어하는 데 사용되는 델리게이트 프로토콜입니다. `BrazeInAppMessageUIDelegate`를 사용하려면 다음이 필요합니다:
- 기본 [`BrazeInAppMessageUI`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui) 구현을 `inAppMessagePresenter`로 사용합니다.
- 프로젝트에 `BrazeUI` 라이브러리를 포함합니다.

### 1단계: `BrazeInAppMessageUIDelegate` 프로토콜 구현 {#step-1-implement-the-brazeinappmessageuidelegate-protocol}

먼저 `BrazeInAppMessageUIDelegate` 프로토콜과 원하는 해당 메서드를 구현합니다. 다음 예제에서는 이 프로토콜이 애플리케이션의 `AppDelegate` 클래스에서 구현됩니다.

{% tabs %}
{% tab swift %}
```swift
extension AppDelegate: BrazeInAppMessageUIDelegate {
  // Implement your protocol methods here.
}
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
@interface AppDelegate () <BrazeInAppMessageUIDelegate>

@end

@implementation AppDelegate
  // Implement your protocol methods here.
@end
```
{% endtab %}
{% endtabs %}

### 2단계: `delegate` 객체 할당 {#step-2-assign-the-delegate-object}

이 인앱 메시지 UI를 `inAppMessagePresenter`로 할당하기 전에 `BrazeInAppMessageUI` 인스턴스에 `delegate` 객체를 할당합니다.

{% tabs %}
{% tab swift %}
```swift
let inAppMessageUI = BrazeInAppMessageUI()
inAppMessageUI.delegate = self
AppDelegate.braze?.inAppMessagePresenter = inAppMessageUI
```
{% endtab %}
{% tab OBJECTIVE-C %}
```objc
BrazeInAppMessageUI *inAppMessageUI = [[BrazeInAppMessageUI alloc] init];
inAppMessageUI.delegate = self;
AppDelegate.braze.inAppMessagePresenter = inAppMessageUI;
```

{% alert important %}
일부 델리게이트 메서드는 파라미터가 언어 런타임과 호환되지 않기 때문에 Objective-C에서 사용할 수 없습니다.
{% endalert %}
{% endtab %}
{% endtabs %}

{% alert tip %}
인앱 메시지 UI 델리게이트의 단계별 구현에 대해서는 이 [튜토리얼](https://braze-inc.github.io/braze-swift-sdk/tutorials/braze/c1-inappmessageui)을 참조하세요.
{% endalert %}

## 클릭 시 동작 {#on-click-behavior}

각 `Braze.InAppMessage` 객체에는 클릭 시 동작을 정의하는 [`ClickAction`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazekit/braze/inappmessage/clickaction)이 포함되어 있습니다.

### 클릭 액션 유형 {#click-action-types}

`Braze.InAppMessage`의 `clickAction` 속성정보는 기본값으로 `.none`이 설정되어 있지만, 다음 값 중 하나로 설정할 수 있습니다:

| `ClickAction` | 클릭 시 동작 |
| -------------------------- | -------- |
| `.url(URL, useWebView: Bool)` | 지정된 URL을 외부 브라우저에서 엽니다. `useWebView`가 `true`로 설정된 경우 웹 뷰에서 엽니다. |
| `.none` | 클릭하면 메시지가 닫힙니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="클릭 액션 유형" }

{% alert important %}
버튼이 포함된 인앱 메시지의 경우, 버튼 텍스트를 추가하기 전에 클릭 액션이 추가되면 메시지 `clickAction`이 최종 페이로드에도 포함됩니다.
{% endalert %}

### 클릭 시 동작 사용자 지정 {#customizing-on-click-behavior}

이 동작을 사용자 지정하려면 다음 샘플을 참조하여 `clickAction` 속성정보를 수정할 수 있습니다:

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  if let newUrl = URL(string: "{your-url}") {
    context.message.clickAction = .url(newUrl, useWebView: true)
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

`inAppMessage(_:prepareWith:)` 메서드는 Objective-C에서 사용할 수 없습니다.

{% endtab %}
{% endtabs %}

### 커스텀 동작 처리 {#handling-the-custom-behavior}

다음 [`BrazeInAppMessageUIDelegate`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate) 델리게이트 메서드는 사용자가 인앱 메시지를 클릭할 때 호출됩니다. 이 콜백은 인앱 메시지 버튼 및 HTML 인앱 메시지 버튼(링크)에 대한 사용자 시작 클릭에 대해 트리거되며, 이러한 상호작용에 대해 버튼 ID가 선택적 매개변수로 제공됩니다. 이 콜백은 `brazeBridge.logClick()`을 통해 트리거된 프로그래밍 방식의 클릭에는 호출되지 않습니다.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?,
  message: Braze.InAppMessage,
  view: InAppMessageView
) -> Bool
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view;
```

{% endtab %}
{% endtabs %}

이 메서드는 Braze가 클릭 액션을 계속 실행해야 하는지를 나타내는 부울 값을 반환합니다.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI, shouldProcess clickAction: Braze.InAppMessage.ClickAction,
  buttonId: String?, message: Braze.InAppMessage, view: InAppMessageView
) -> Bool {
    guard let buttonId,
      let idInt = Int(buttonId)
    else { return true }
    var button: BrazeKit.Braze.InAppMessage.Button? = nil

    switch message {
    case .modal(let modal):
      button = modal.buttons[idInt]

    case .modalImage(let modalImage):
      button = modalImage.buttons[idInt]

    case .full(let full):
      button = full.buttons[idInt]

    case .fullImage(let fullImage):
      button = fullImage.buttons[idInt]

    default:
      break
    }

    print(button?.id)
    print(button?.text)
    print(button?.clickAction)

    return true
  }
```

{% endtab %}
{% tab OBJECTIVE-C %}
```objc
- (BOOL)inAppMessage:(BrazeInAppMessageUI *)ui
       shouldProcess:(enum BRZInAppMessageRawClickAction)clickAction
                 url:(NSURL *)uri
            buttonId:(NSString *)buttonId
             message:(BRZInAppMessageRaw *)message
                view:(UIView *)view {
  NSInteger buttonInt = [buttonId integerValue];

  if (message.type == BRZInAppMessageRawTypeFull || message.type == BRZInAppMessageRawTypeModal) {
    BRZInAppMessageRawButton *button = message.buttons[buttonInt];
    NSLog(@"%ld", (long)button.identifier);
    NSLog(@"%@", button.text);
    NSLog(@"%ld", (long)button.clickAction);
  }
  return YES;
}
```

{% endtab %}
{% endtabs %}

## 스와이프로 슬라이드업 메시지 닫기 {#swiping-to-dismiss-slideup-messages}

기본적으로 슬라이드업 인앱 메시지는 스와이프 제스처로 닫을 수 있습니다. 스와이프 방향은 슬라이드업 위치에 따라 다릅니다:

- **왼쪽 또는 오른쪽 스와이프:** 위치에 관계없이 슬라이드업을 닫습니다.
- **하단에서 슬라이드업:** 위에서 아래로 스와이프하면 메시지가 닫힙니다. 아래에서 위로 스와이프하면 닫히지 않습니다.
- **상단에서 슬라이드업:** 아래에서 위로 스와이프하면 메시지가 닫힙니다. 위에서 아래로 스와이프하면 닫히지 않습니다.

이 스와이프 동작은 기본 `BrazeInAppMessageUI` [`SlideupView`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/slideupview)에 내장되어 있으며, 슬라이드업 인앱 메시지에만 적용됩니다. Modal 및 전체 화면 인앱 메시지는 스와이프로 닫기를 지원하지 않습니다. 스와이프 동작을 포함한 슬라이드업 뷰를 추가로 사용자 지정하려면 [`SlideupView.Attributes`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageui/slideupview/attributes-swift.struct)를 수정하거나 서브클래싱을 통해 커스텀 뷰를 제공할 수 있습니다.

{% alert note %}
슬라이드업 메시지 바깥 영역을 탭해도 메시지가 닫히지 않습니다. Modal 또는 전체 화면 인앱 메시지의 경우, 다음 섹션에서 설명하는 `dismissOnBackgroundTap` 속성을 사용하여 바깥 영역 탭으로 닫기를 활성화할 수 있습니다.
{% endalert %}

## Modal 닫기 사용자 지정 {#customizing-modal-dismissals}

외부 탭 닫기를 활성화하려면 사용자 지정하려는 인앱 메시지 유형의 `Attributes` 구조체에서 `dismissOnBackgroundTap` 속성을 수정할 수 있습니다.

예를 들어, Modal 이미지 인앱 메시지에 대해 이 기능을 활성화하려면 다음과 같이 설정할 수 있습니다:

{% tabs %}
{% tab swift %}

```swift
BrazeInAppMessageUI.ModalImageView.Attributes.defaults.dismissOnBackgroundTap = true
```

{% endtab %}
{% tab OBJECTIVE-C %}

`Attributes`를 통한 사용자 지정은 Objective-C에서 사용할 수 없습니다.

{% endtab %}
{% endtabs %}

기본값은 `false`입니다. 이 값은 사용자가 인앱 메시지 외부를 탭했을 때 Modal 인앱 메시지가 닫힐지 여부를 결정합니다.

| `DismissModalOnOutsideTap` | 설명 |
|----------|-------------|
| `true`         | Modal 인앱 메시지가 외부 탭 시 닫힙니다.     |
| `false`        | 기본값, Modal 인앱 메시지가 외부 탭 시 닫히지 않습니다. |
{: .reset-td-br-1 .reset-td-br-2 aria-label="Modal 닫기 사용자 지정" }

인앱 메시지 사용자 지정에 대한 자세한 내용은 이 [문서](https://braze-inc.github.io/braze-swift-sdk/documentation/braze/in-app-message-customization)를 참조하세요.

## 메시지 방향 사용자 지정 {#customizing-message-orientation}

인앱 메시지의 방향을 사용자 지정할 수 있습니다. 모든 메시지에 대해 새로운 기본 방향을 설정하거나, 단일 메시지에 대해 커스텀 방향을 설정할 수 있습니다.

{% tabs local %}
{% tab 모든 메시지 %}
모든 인앱 메시지의 기본 방향을 선택하려면 [`inAppMessage(_:prepareWith:)`](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) 메서드를 사용하여 `PresentationContext`의 `preferredOrientation` 속성을 설정합니다.

예를 들어, 세로 모드를 기본 방향으로 설정하려면:

{% subtabs %}
{% subtab swift %}
```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  context.preferredOrientation = .portrait
}
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  context.preferredOrientation = BRZInAppMessageRawOrientationPortrait;
}
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}

{% tab 단일 메시지 %}
단일 메시지의 방향을 설정하려면 `Braze.InAppMessage`의 `orientation` 속성을 수정합니다:

{% subtabs %}
{% subtab swift %}

```swift
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = .any

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = .portrait

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = .landscape
```

{% endsubtab %}
{% subtab OBJECTIVE-C %}

```objc
// Set inAppMessage orientation to support any configuration
inAppMessage.orientation = BRZInAppMessageRawOrientationAny;

// Set inAppMessage orientation to only display in portrait
inAppMessage.orientation = BRZInAppMessageRawOrientationPortrait;

// Set inAppMessage orientation to only display in landscape
inAppMessage.orientation = BRZInAppMessageRawOrientationLandscape;
```

{% endsubtab %}
{% endsubtabs %}
{% endtab %}
{% endtabs %}

인앱 메시지가 표시된 후 메시지가 계속 표시되는 동안 기기 방향이 변경되면, 메시지의 `orientation` 구성에서 지원하는 경우 메시지가 기기와 함께 회전합니다.

메시지가 표시되려면 기기 방향이 인앱 메시지의 `orientation` 속성에서도 지원되어야 합니다. 또한 `preferredOrientation` 설정은 Xcode에서 타겟 설정의 **Deployment Info** 섹션에 있는 앱의 지원되는 인터페이스 방향에 포함된 경우에만 적용됩니다.

![Xcode에서 지원되는 방향 설정.]({% image_buster /assets/img/supported_interface_orientations_xcode.png %}){: width="2038" height="590"}

{% alert note %}
방향은 메시지 표시에만 적용됩니다. 기기 방향이 변경되면 메시지 뷰는 지원하는 방향 중 하나를 채택합니다. 소형 기기(iPhone, iPod Touch)에서 Modal 또는 전체 화면 인앱 메시지에 가로 방향을 설정하면 콘텐츠가 잘릴 수 있습니다.
{% endalert %}

## 표시 타이밍 사용자 지정 {#customizing-display-timing}

사용자 경험의 특정 시점에서 사용 가능한 인앱 메시지가 표시되는지 여부를 제어할 수 있습니다. 전체 화면 게임 중이거나 로딩 화면에서와 같이 인앱 메시지가 나타나지 않기를 원하는 상황이 있다면, 대기 중인 인앱 메시지를 지연하거나 삭제할 수 있습니다. 인앱 메시지의 타이밍을 제어하려면 `inAppMessage(_:displayChoiceForMessage:)` [델리게이트 메서드](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)를 사용하여 `BrazeInAppMessageUI.DisplayChoice` 속성정보를 설정합니다.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  displayChoiceForMessage message: Braze.InAppMessage
) -> BrazeInAppMessageUI.DisplayChoice
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui displayChoiceForMessage:(BRZInAppMessageRaw *)message
```

{% endtab %}
{% endtabs %}

다음 값 중 하나를 반환하도록 `BrazeInAppMessageUI.DisplayChoice`를 구성합니다.

| 표시 선택                             | 동작                                                                                                                        |
| ----------------------------------- | --------------------------------------------------------------------------------------------------------------------------- |
| `.now`                              | 메시지가 즉시 표시됩니다. 이것이 기본값입니다.                                                                                  |
| `.reenqueue`                        | 메시지가 표시되지 않으며 스택 맨 위로 다시 배치됩니다.                                                                            |
| `.later`                            | 메시지가 표시되지 않으며 스택 맨 위로 다시 배치됩니다. (더 이상 사용되지 않으며, `.reenqueue`를 사용하세요)                              |
| `.discard`                          | 메시지가 삭제되며 표시되지 않습니다.                                                                                             |
{: .reset-td-br-1 .reset-td-br-2 aria-label="표시 타이밍 사용자 지정" }

{% alert tip %}
`InAppMessageUI`의 샘플은 [Swift Braze SDK 리포지토리](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/Swift/Sources/InAppMessageUI) 및 [Objective-C](https://github.com/braze-inc/braze-swift-sdk/tree/main/Examples/ObjC/Sources/InAppMessageUI)를 확인하세요.
{% endalert %}

## 상태 표시줄 숨기기 {#hiding-the-status-bar}

`Full`, `FullImage`, `HTML` 인앱 메시지의 경우 SDK는 기본적으로 상태 표시줄을 숨깁니다. 다른 유형의 인앱 메시지에서는 상태 표시줄이 변경되지 않습니다. 이 동작을 설정하려면 `inAppMessage(_:prepareWith:)` [델리게이트 메서드](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog)를 사용하여 `PresentationContext`의 `statusBarHideBehavior` 속성을 설정합니다. 이 필드는 다음 값 중 하나를 사용합니다.

| 상태 표시줄 숨기기 동작            | 설명                                                                           |
| ----------------------------------- | ------------------------------------------------------------------------------------- |
| `.auto`                             | 메시지 뷰가 상태 표시줄의 숨김 상태를 결정합니다.                                 |
| `.hidden`                           | 항상 상태 표시줄을 숨깁니다.                                                           |
| `.visible`                          | 항상 상태 표시줄을 표시합니다.                                                        |
{: .reset-td-br-1 .reset-td-br-2 aria-label="상태 표시줄 숨기기" }

## 다크 모드 비활성화 {#disabling-dark-mode}

사용자 기기에서 다크 모드가 활성화되어 있을 때 인앱 메시지가 다크 모드 스타일을 적용하지 않도록 하려면, `inAppMessage(_:prepareWith:)` [델리게이트 메서드](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:preparewith:)-11fog) 메서드를 구현하세요. 이 메서드에 전달되는 `PresentationContext`에는 표시할 `InAppMessage` 객체에 대한 참조가 포함되어 있습니다. 각 `InAppMessage`에는 `dark` 및 `light` 모드 테마가 포함된 `themes` 속성정보가 있습니다. `themes.dark` 속성정보를 `nil`로 설정하면 Braze가 자동으로 라이트 테마를 사용하여 인앱 메시지를 표시합니다.

버튼이 있는 인앱 메시지 유형에는 `buttons` 속성정보에 추가적인 `themes` 객체가 있습니다. 버튼이 다크 모드 스타일을 적용하지 않도록 하려면, [`map(_:)`](https://developer.apple.com/documentation/swift/array/map(_:)-87c4d)을 사용하여 `light` 테마만 있고 `dark` 테마가 없는 새 버튼 배열을 생성할 수 있습니다.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(
  _ ui: BrazeInAppMessageUI,
  prepareWith context: inout BrazeInAppMessageUI.PresentationContext
) {
  switch context.message {
    case .slideup:
      guard var slideup = context.message.slideup else { return }
      slideup.themes.dark = nil
      context.message.slideup = slideup

    case .modal:
      guard var modal = context.message.modal else { return }
      modal.themes.dark = nil
      modal.buttons = modal.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modal = modal

    case .modalImage:
      guard var modalImage = context.message.modalImage else { return }
      modalImage.themes.dark = nil
      modalImage.buttons = modalImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.modalImage = modalImage

    case .full:
      guard var full = context.message.full else { return }
      full.themes.dark = nil
      full.buttons = full.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.full = full

    case .fullImage:
      guard var fullImage = context.message.fullImage else { return }
      fullImage.themes.dark = nil
      fullImage.buttons = fullImage.buttons.map {
        var newButton = $0
        newButton.themes = .init(themes: ["light": $0.themes.light])
        return newButton
      }
      context.message.fullImage = fullImage

    default:
      break
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)inAppMessage:(BrazeInAppMessageUI *)ui
         prepareWith:(BrazeInAppMessageUIPresentationContextRaw *)context {
  switch (context.message.type) {
    case BRZInAppMessageRawTypeSlideup: {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;
      break;
    }
    case BRZInAppMessageRawTypeModal:
    case BRZInAppMessageRawTypeFull:
    {
      NSMutableDictionary *updatedThemes = [context.message.themes mutableCopy];
      [updatedThemes removeObjectForKey:@"dark"];
      context.message.themes = updatedThemes;

      NSMutableArray *updatedButtons = [NSMutableArray arrayWithCapacity:context.message.buttons.count];
      for (BRZInAppMessageRawButton *button in context.message.buttons) {
        BRZInAppMessageRawButtonTheme *lightTheme = BRZInAppMessageRawButtonTheme.defaultLight;
        BRZInAppMessageRawButton *newButton = [button mutableCopy];
        newButton.textColor = lightTheme.textColor;
        newButton.backgroundColor = lightTheme.backgroundColor;
        newButton.borderColor = lightTheme.borderColor;
        [updatedButtons addObject:newButton];
      }
      context.message.buttons = updatedButtons;
      break;
    }
    default:
      break;
  }
}
```

{% endtab %}
{% endtabs %}

## 앱 스토어 리뷰 프롬프트 사용자 지정 {#customizing-the-app-store-review-prompt}

인앱 메시지를 Campaign에서 사용하여 사용자에게 앱 스토어 리뷰를 요청할 수 있습니다.

{% alert note %}
이 예제 프롬프트는 Braze의 기본 동작을 재정의하므로, 구현 시 노출 횟수가 자동으로 추적되지 않습니다. [자체 분석을 기록]({{site.baseurl}}/developer_guide/analytics)해야 합니다.
{% endalert %}

### 1단계: 인앱 메시지 델리게이트 설정 {#step-1-set-the-in-app-message-delegate}

먼저 앱에서 [`BrazeInAppMessageUIDelegate`]({{site.baseurl}}/developer_guide/in_app_messages/customization#swift_setting-up-the-ui-delegate-required)를 설정합니다.

### 2단계: 기본 앱 스토어 리뷰 메시지 비활성화 {#step-2-disable-the-default-app-store-review-message}

다음으로 `inAppMessage(_:displayChoiceForMessage:)` [델리게이트 메서드](https://braze-inc.github.io/braze-swift-sdk/documentation/brazeui/brazeinappmessageuidelegate/inappmessage(_:displaychoiceformessage:)-9w1nb)를 구현하여 기본 앱 스토어 리뷰 메시지를 비활성화합니다.

{% tabs %}
{% tab swift %}

```swift
func inAppMessage(_ ui: BrazeInAppMessageUI, displayChoiceForMessage message: Braze.InAppMessage) -> BrazeInAppMessageUI.DisplayChoice {
  if message.extras["AppStore Review"] != nil,
    let messageUrl = message.clickAction.url {
      UIApplication.shared.open(messageUrl, options: [:], completionHandler: nil)
      return .discard
  } else {
    return .now
  }
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (enum BRZInAppMessageUIDisplayChoice)inAppMessage:(BrazeInAppMessageUI *)ui
                            displayChoiceForMessage:(BRZInAppMessageRaw *)message {
  if (message.extras != nil && message.extras[@"AppStore Review"] != nil) {
    [[UIApplication sharedApplication] openURL:message.url options:@{} completionHandler:nil];
    return BRZInAppMessageUIDisplayChoiceDiscard;
  } else {
    return BRZInAppMessageUIDisplayChoiceNow;
  }
}
```

{% endtab %}
{% endtabs %}

### 3단계: 딥링크 생성 {#step-3-create-a-deep-link}

[`scene:openURLContexts:`]({{site.baseurl}}/developer_guide/push_notifications/deep_linking/?sdktab=swift#swift_step-3-implement-a-handler) 핸들러에서 다음 코드를 추가하여 `{YOUR-APP-SCHEME}:app-store-review` 딥링크를 처리합니다. `SKStoreReviewController`를 사용하려면 `StoreKit`을 임포트해야 합니다.

{% tabs %}
{% tab swift %}

```swift
func scene(_ scene: UIScene, openURLContexts URLContexts: Set<UIOpenURLContext>) {
  guard let url = URLContexts.first?.url else { return }
  let urlString = url.absoluteString.removingPercentEncoding
  if (urlString == "{YOUR-APP-SCHEME}:app-store-review") {
    SKStoreReviewController.requestReview()
    return;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% tab OBJECTIVE-C %}

```objc
- (void)scene:(UIScene *)scene openURLContexts:(NSSet<UIOpenURLContext *> *)URLContexts {
  NSURL *url = URLContexts.allObjects.firstObject.URL;
  NSString *urlString = url.absoluteString.stringByRemovingPercentEncoding;
  if ([urlString isEqualToString:@"{YOUR-APP-SCHEME}:app-store-review"]) {
    [SKStoreReviewController requestReview];
    return;
  }
  // Other deep link handling code…
}
```

{% endtab %}
{% endtabs %}

{% raw %}

### 4단계: 커스텀 클릭 동작 설정 {#step-4-set-custom-on-click-behavior}

다음으로, 아래 내용을 포함하는 인앱 메시징 Campaign을 생성합니다.

- 키-값 페어 `"AppStore Review" : "true"`
- 딥링크 `{YOUR-APP-SCHEME}:app-store-review`를 사용하여 클릭 동작을 "앱으로 딥링크"로 설정합니다.

{% endraw %}

{% alert tip %}
Apple은 각 사용자당 연간 최대 3회까지 앱 스토어 리뷰 프롬프트를 제한하므로, Campaign을 사용자당 연간 3회로 [빈도 제한]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/frequency_capping)해야 합니다.<br><br>사용자가 앱 스토어 리뷰 프롬프트를 끌 수 있습니다. 따라서 커스텀 리뷰 프롬프트에서 네이티브 앱 스토어 리뷰 프롬프트가 표시될 것이라고 약속하거나 리뷰를 직접 요청해서는 안 됩니다.
{% endalert %}