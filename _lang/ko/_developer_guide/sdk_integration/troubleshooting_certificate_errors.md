---
page_order: 1.35
nav_title: 인증서 신뢰 오류
article_title: SDK 인증서 신뢰 오류 문제 해결
description: "Android, Swift 및 기타 SDK에서 Braze SDK 초기화를 차단할 수 있는 HTTPS 인증서 신뢰 오류를 해결합니다."
---

# SDK 인증서 신뢰 오류 문제 해결 {#troubleshooting-sdk-certificate-trust-errors}

SSL 또는 TLS 인증서 신뢰 오류로 SDK 초기화가 실패하는 경우, 이는 일반적으로 기기, 시뮬레이터, 브라우저 또는 서버가 Braze 엔드포인트의 인증서 체인을 검증할 수 없음을 의미합니다.

예를 들어, Android 또는 기타 JVM 기반 환경에서 다음과 같은 오류가 표시될 수 있습니다.

```
javax.net.ssl.SSLHandshakeException: java.security.cert.CertPathValidatorException: Trust anchor for certification path not found
```

이는 일반적으로 SDK 통합 버그가 아니라 환경의 네트워크 또는 인증서 신뢰 구성 문제입니다.

## 일반적인 원인 {#common-causes}

- 회사 프록시, 방화벽 또는 트래픽 검사 도구가 런타임에서 신뢰하지 않는 인증서로 HTTPS 트래픽을 가로채고 있습니다.
- 기기, 시뮬레이터, 브라우저 또는 서버의 신뢰 저장소에 필수 루트 또는 중간 인증서가 누락되어 있습니다.
- 로컬 보안 설정이 Braze 엔드포인트로의 아웃바운드 HTTPS를 차단하고 있습니다.
- 앱 수준의 인증서 또는 전송 보안 설정이 연결을 차단하고 있습니다.

## 문제 해결 단계 {#troubleshooting-steps}

1. SDK 엔드포인트와 네트워크 접근을 확인합니다.
   - 워크스페이스에 맞는 올바른 [SDK 엔드포인트]({{site.baseurl}}/user_guide/administer/personal/sdk_endpoints)를 사용하고 있는지 확인합니다.
   - 환경이 HTTPS를 통해 해당 엔드포인트에 도달할 수 있는지 확인합니다.
2. 네트워크 간 동작을 비교합니다.
   - 다른 네트워크에서 테스트합니다(예: 회사 Wi-Fi 대신 모바일 데이터).
   - 문제가 하나의 네트워크에서만 발생한다면, 근본 원인은 프록시 또는 방화벽 구성일 가능성이 높습니다.
3. 신뢰 구성을 검증합니다.
   - SDK가 실행되는 런타임에 필수 루트 인증서 및 중간 인증서가 설치되어 있고 신뢰할 수 있는 상태인지 확인합니다.
   - 환경에서 커스텀 인증 기관을 사용하는 경우, 해당 인증서가 올바르게 배포되었는지 확인합니다.
4. 플랫폼 보안 설정을 검토합니다.
   - 앱 또는 환경에 명시적인 전송 또는 인증서 규칙이 있는 경우, 해당 설정이 Braze 엔드포인트에 대한 HTTPS 요청을 허용하는지 확인합니다.
5. 네트워크 또는 보안 팀과 협력합니다.
   - 전체 오류 내용과 타임스탬프를 공유하여 인증서 체인, TLS 검사 설정 및 허용 목록 규칙을 확인할 수 있도록 합니다.

{% alert note %}
Braze SDK 트래픽은 HTTPS를 사용하므로, 인증서 신뢰 실패는 제한적인 네트워크 정책이 적용된 환경에서 모든 Braze SDK(Android, SWIFT, 웹, React Native, Flutter, Unity, Cordova 포함)에 영향을 줄 수 있습니다.
{% endalert %}