---
nav_title: 중국 Android 기기의 전달 가능성
article_title: 중국 Android 기기의 푸시 전달 가능성
page_order: 10

page_type: reference
description: "이 문서에서는 중국 OEM이 제조한 Android 기기 사용자를 타겟팅할 때 알아야 할 푸시 전달 가능성 관련 주의사항을 다룹니다."
channel: push

---

# 중국 Android 기기의 푸시 전달 가능성 {#push-deliverability-for-chinese-android-devices}

> Xiaomi, OPPO, Vivo 등 중국 OEM(Original Equipment Manufacturer)이 제조한 일부 Android 기기는 공격적인 앱 수명 주기 관리를 통해 배터리 수명을 최적화합니다. 이러한 최적화는 백그라운드 앱 처리를 종료하는 의도치 않은 결과를 초래할 수 있으며, 이로 인해 푸시 알림의 전달 가능성이 저하될 수 있습니다.<br><br>이러한 기기에서 앱의 메시징 성과가 예상대로 작동하도록 하려면, 마케팅 팀과 엔지니어링 팀이 협력하여 이 문서에 설명된 단계를 따라야 합니다.

## 개발자를 위한 단계 {#steps-for-developers}
이러한 OEM은 백그라운드 애플리케이션을 공격적으로 종료하고 백그라운드 작업 실행을 위한 자동 시작을 차단하여 최적화를 수행합니다. 개발자는 가능한 한 사용자가 이러한 제한을 완화하도록 요청하는 앱 설정을 구성해야 합니다.

이를 위해 최종 사용자의 기기에서 앱이 자동으로 시작되도록 설정하면, 앱이 백그라운드에서 실행되고 Braze의 메시지를 수신할 수 있는 권한을 얻게 됩니다. 안타깝게도 이는 Android 자체의 문제가 아닌 OEM별 문제이므로, 각 OEM의 자동 시작 권한 프롬프트를 표시하기 위한 문서화된 API가 없습니다.

이를 해결하려면 [AutoStarter](https://github.com/judemanutd/AutoStarter)와 같은 라이브러리를 애플리케이션에 통합하세요. AutoStarter는 여러 제조사를 지원하므로, 다양한 기기에서 시작 권한 매니저를 쉽게 호출할 수 있습니다. AutoStarter를 통합한 후 `AutoStartPermissionHelper.getInstance().getAutoStartPermission(context)`를 호출하여 최종 사용자의 기기에서 시작 권한 매니저를 표시하세요. 이 동작과 함께 최종 사용자에게 앱의 "자동 시작"을 활성화하도록 안내하는 프롬프트를 함께 표시하세요. 마케팅 팀이 이 메시지를 작성합니다—다음 섹션을 참조하세요!

## 마케터를 위한 단계 {#steps-for-marketers}
사용자가 푸시 알림 수신에 옵트인한 후, 이러한 기기에서 메시지 전달을 개선하기 위해 사용자 측에서 추가로 수행할 수 있는 단계가 있습니다. [푸시 프라이머 메시지]({{site.baseurl}}/user_guide/channels/push/best_practices/push_primer_messages/)에 이어 중국 OEM 기기의 사용자를 타겟으로 하는 인앱 메시지를 통해 다음 추가 단계를 안내하는 것을 권장합니다:

- 앱의 "자동 시작" 활성화
- 앱의 배터리 최적화 비활성화

메시지의 효과를 더욱 높이려면, 열리지 않은 푸시 알림의 정보를 SMS, WhatsApp, LINE 등의 앱 외부 채널과 인앱 메시지 및 Content Cards 등의 인앱 채널을 통해 다시 전달하세요. 사용자가 다음에 앱을 열 때 놓쳤을 수 있는 내용을 확인할 수 있습니다.