Braze를 사용하여 iOS 푸시 알림을 보내려면 먼저 [Apple 개발자 설명서](https://developer.apple.com/documentation/usernotifications/establishing-a-token-based-connection-to-apns)에 설명된 대로 `.p8` 푸시 알림 파일을 업로드해야 합니다:

1. Apple 개발자 계정에서 [**Certificates, Identifiers & Profiles**](https://developer.apple.com/account/ios/certificate)로 이동합니다.
2. **Keys**에서 **All**을 선택하고 페이지 상단의 추가 버튼(+)을 클릭합니다.
3. **Key Description**에 서명 키의 고유한 이름을 입력합니다.
4. **Key Services**에서 **Apple Push Notification service (APNs)** 체크박스를 선택한 다음 **Continue**를 클릭합니다. **Confirm**을 클릭합니다.
5. 키 ID를 기록해 두세요. **Download**를 클릭하여 키를 생성하고 다운로드합니다. 다운로드한 파일은 한 번만 다운로드할 수 있으므로 안전한 곳에 저장하세요.
6. Braze에서 **설정** > **앱 설정**으로 이동하여 **Apple Push Certificate** 아래에 `.p8` 파일을 업로드합니다. 개발용 또는 프로덕션 푸시 인증서를 업로드할 수 있습니다. 앱이 앱 스토어에 실시간으로 출시된 후 푸시 알림을 테스트하려면 앱의 개발 버전을 위한 별도의 워크스페이스를 설정하는 것이 좋습니다.
7. 메시지가 표시되면 앱의 [번들 ID](https://developer.apple.com/documentation/foundation/nsbundle/1418023-bundleidentifier), [키 ID](https://developer.apple.com/help/account/manage-keys/get-a-key-identifier/) 및 [팀 ID](https://developer.apple.com/help/account/manage-your-team/locate-your-team-id)를 입력합니다. 또한 프로비저닝 프로필에 의해 정의되는 앱의 개발 환경 또는 프로덕션 환경 중 어디로 알림을 보낼지 지정해야 합니다.
8. 완료되면 **저장**을 선택합니다.