---
nav_title: 중국 Android 기기의 전달 가능성
article_title: 중국 Android 기기의 푸시 전달 가능성
page_order: 10

page_type: reference
description: "이 문서에서는 중국 OEM이 제조한 Android 기기 사용자를 타겟팅할 때 알아야 할 푸시 전달 가능성 관련 주의사항을 다룹니다."
channel: push

---

# 중국 Android 기기의 푸시 전달 가능성 {#push-deliverability-for-chinese-android-devices}

> Xiaomi, OPPO, Vivo, Huawei 등 중국 OEM(Original Equipment Manufacturer)이 제조한 일부 Android 기기는 공격적인 앱 수명 주기 관리를 통해 배터리 수명을 최적화합니다. 이러한 최적화는 백그라운드 앱 처리를 종료하는 의도치 않은 결과를 초래할 수 있으며, 이로 인해 푸시 알림의 전달 가능성이 저하될 수 있습니다.<br><br>이러한 기기에서 앱의 메시징 성능이 예상대로 작동하도록 하려면, 마케팅 팀과 엔지니어링 팀이 협력하여 이 문서에 설명된 단계를 따라야 합니다.

## 개발자를 위한 단계 {#steps-for-developers}
이러한 OEM은 백그라운드 애플리케이션을 공격적으로 종료하고, 백그라운드 작업 실행을 위한 자동 시작을 차단하는 방식으로 최적화를 수행합니다. 개발자는 가능한 한 사용자에게 이러한 제한을 완화하도록 요청할 수 있게 앱을 구성해야 합니다.

이는 앱이 최종사용자의 기기에서 자동으로 시작되도록 설정하여 달성할 수 있으며, 이를 통해 앱이 백그라운드에서 실행되고 Braze로부터 메시지를 수신할 수 있는 권한을 얻게 됩니다. 안타깝게도 이 문제는 Android 자체의 문제가 아닌 OEM별 문제이므로, 각 OEM에 대한 자동 시작 권한 프롬프트를 호출하기 위한 문서화된 API가 없습니다.

이를 해결하려면 [AutoStarter](https://github.com/judemanutd/AutoStarter)와 같은 라이브러리를 애플리케이션에 통합하세요. AutoStarter는 다양한 제조사를 지원하므로, 광범위한 기기에서 시작 권한 매니저를 쉽게 호출할 수 있습니다. AutoStarter를 통합한 후, `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)`를 호출하여 최종사용자의 기기에서 시작 권한 매니저를 표시하세요. 이 동작과 함께 최종사용자에게 앱의 "자동 시작"을 활성화하도록 권장하는 프롬프트를 함께 제공하세요. 마케팅 팀에서 이 메시지를 작성하게 됩니다. 다음 섹션을 참고하세요!

## 마케터를 위한 단계 {#steps-for-marketers}

사용자가 푸시 알림 수신에 옵트인한 후에도 해당 기기의 메시지 전달을 개선하기 위해 추가 조치를 취할 수 있습니다. [푸시 프라이머 메시지]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages) 이후, 중국 OEM 기기를 사용하는 사용자를 타겟팅하는 인앱 메시지를 통해 다음 추가 단계를 안내하는 것을 권장합니다.

- 앱의 "자동 시작" 활성화
- 앱의 배터리 최적화 비활성화

### 중국 OEM 기기 사용자 식별 {#identifying-users-on-chinese-oem-devices}

특정 중국 OEM 기기의 사용자에게 인앱 메시지를 타겟팅하려면 **Device Model** 또는 **Device OS** [세분화 필터]({{site.baseurl}}/user_guide/audience/segments/segmentation_filters)를 사용하세요.

- **Device Model:** 이 필터를 사용하여 모바일 기기 모델별로 사용자를 타겟팅합니다. 예를 들어, Huawei 기기를 식별하려면 모델명과 일치하도록 `huawei`가 포함된 정규식 패턴을 사용합니다. 단계별 설정 안내는 [Huawei 기기를 위한 Device Model 정규식 작성](#build-a-device-model-regex-for-huawei-devices)을 참조하세요.
- **Device OS:** 이 필터를 사용하여 운영 체제별로 사용자를 타겟팅합니다. Huawei와 같은 일부 중국 OEM은 기기 OS 필드에 커스텀 Android 버전을 명시적으로 지정할 수 있습니다. 확인 단계는 [타겟팅 전 Device OS 값 확인](#verify-device-os-values-before-you-target)을 참조하세요.

#### Huawei 기기를 위한 Device Model 정규식 작성 {#build-a-device-model-regex-for-huawei-devices}

1. **Audience** > **Segments**로 이동한 후 Segment를 생성하거나 편집합니다.
2. **Device Model** 필터를 추가합니다.
3. 연산자를 **matches regex**로 설정합니다.
4. Huawei 모델명과 일치하도록 `huawei`를 입력합니다.
5. (선택 사항) Honor 브랜드 기기도 포함하려면 `(huawei|honor)`를 사용합니다.

Braze에서의 정규식 동작 및 패턴 테스트에 대한 자세한 내용은 [정규표현식]({{site.baseurl}}/user_guide/audience/segments/regex)을 참조하세요.

#### 타겟팅 전 Device OS 값 확인 {#verify-device-os-values-before-you-target}

일부 OEM 변형은 기기 메타데이터에 커스텀 OS 이름을 보고할 수 있습니다. 이 값은 기기 모델 및 Android 배포판에 따라 다를 수 있으므로, Segment를 작성하기 전에 사용자가 Braze에 보내는 값을 확인하세요.

1. **Search Users**로 이동한 후, 알려진 타겟 사용자의 프로필을 엽니다.
2. **Overview** 탭에서 **Recent devices**를 확인하고 해당 기기에 표시된 OS 값을 검토합니다.
3. 정확한 OS 문자열을 Segment 필터에 복사합니다:
   - 정확한 일치 또는 정규식 기반 OS 문자열 매칭이 필요한 경우 **Device OS**를 사용합니다.
   - 숫자 버전 범위가 필요한 경우 **Device OS Version Number**를 사용합니다.
4. Segment 작성기에서 **User Lookup**을 사용하여 테스트 사용자가 예상대로 일치하는지 확인합니다.

프로필에서 기기 메타데이터를 찾는 위치에 대한 자세한 내용은 [고객 프로필]({{site.baseurl}}/user_guide/audience/manage_audience/user_profiles)을 참조하세요. Segment 로직 테스트에 대한 자세한 내용은 [Segment 생성]({{site.baseurl}}/user_guide/audience/segments/creating_a_segment#testing-segments)을 참조하세요.