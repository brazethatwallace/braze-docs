{% if include.page == "testing" %}[배너 메시지를 작성]({{site.baseurl}}/user_guide/message_building_by_channel/banners/create/#compose-a-banner)하면서{% elsif include.page == "campaigns" %}{% endif %} **미리보기**를 선택하여 배너를 미리 보거나 테스트 메시지를 보낼 수 있습니다.

![배너 작성기의 미리보기 탭.]({% image_buster /assets/img/banners/select_preview.png %}){: style="max-width:50%;"}

하드웨어 차이로 인해 미리보기가 사용자 기기에서의 최종 렌더링과 동일하지 않을 수 있다는 점을 유의하세요.

테스트 메시지를 보내려면 콘텐츠 테스트 그룹 또는 하나 이상의 개별 사용자를 **테스트 수신자**로 추가한 다음 **테스트 전송**을 선택합니다. 테스트 메시지는 기기에서 최대 5분 동안 확인할 수 있습니다. 그런 다음 **미리보기 링크 복사**를 선택하여 임의의 사용자에게 배너가 어떻게 보이는지 확인할 수 있는 공유 가능한 미리보기 링크를 생성하고 복사할 수 있습니다. 이 링크는 7일 동안 유효하며, 이후에는 다시 생성해야 합니다.

![배너 작성기의 미리보기 탭.]({% image_buster /assets/img/banners/preview_banner.png %})

테스트 배너를 검토하면서 다음 사항을 확인하세요:

- 배너 Campaign이 배치에 할당되어 있나요?
- 이미지와 미디어가 타겟 기기 유형 및 화면 크기에서 예상대로 표시되고 작동하나요?
- 링크와 버튼이 사용자를 올바른 위치로 안내하나요?
- Liquid가 예상대로 작동하나요? Liquid가 정보를 반환하지 않는 경우를 대비하여 기본 속성 값을 설정했나요?
- 문구가 명확하고 간결하며 정확한가요?

자세한 내용은 [테스트 메시지 보내기]({{site.baseurl}}/user_guide/messaging/messaging_fundamentals/sending_test_messages/)를 참조하세요.