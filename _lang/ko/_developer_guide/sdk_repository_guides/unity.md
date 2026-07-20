---
nav_title: Unity SDK
article_title: Unity SDK 리포지토리 가이드
page_order: 9
description: "GitHub에서 미러링된 Braze Unity SDK README 참조입니다."
---

<!-- BEGIN GENERATED README CONTENT -->
# Unity SDK 리포지토리 가이드 {#unity-sdk-repository-guide}

## Braze Unity SDK 소개 {#about-the-braze-unity-sdk}

Braze Unity SDK는 Braze 메시징, 분석 및 사용자 참여 기능을 애플리케이션에 통합하는 데 도움을 줍니다.

시작하려면 다음 리소스를 참조하세요:

- [Braze 사용자 가이드](https://www.braze.com/docs/user_guide/introduction/)
- [Braze 개발자 가이드](https://www.braze.com/docs/developer_guide/sdk_integration/?sdktab=unity)

## 플러그인 설정 {#plugin-setup}

Unity 스크립트에서 Braze를 사용하려면 먼저 플러그인 파일을 Unity 프로젝트로 가져와야 합니다.

**권장:** Android 및 iOS 플러그인은 [SDK 릴리즈 페이지][1]에서 다운로드할 수 있는 Unity 패키지로 번들 제공됩니다.

**수동 플러그인 설정:** 또는 플러그인을 Unity 프로젝트에 직접 복사할 수 있습니다:
  1. 먼저 이 리포지토리를 복제합니다.
  2. 다른 플러그인을 사용하지 않는 경우, 이 리포지토리의 `Plugins` 디렉토리를 Unity 프로젝트의 `Assets` 폴더에 복사하기만 하면 됩니다.
  3. 이미 `/<your-project>/Assets/Plugins` 디렉토리가 있는 경우(다른 플러그인을 이미 사용 중이기 때문일 수 있음), `Plugins/Appboy/AppboyBinding.cs`를 `/<your-project>/Assets/Plugins`에 복사합니다. 그런 다음 이 리포지토리의 `Plugins/iOS` 및 `Plugins/Android` 내용을 각각 `/<your-project>/Assets/Plugins/iOS` 및 `/<your-project>/Assets/Plugins/Android`에 복사합니다.

## 통합 설정 {#integration-setup}

Braze를 Unity 애플리케이션에 통합하려면 [Braze Unity SDK 통합][2] 안내를 완료하세요.

[1]: https://github.com/braze-inc/braze-unity-sdk/releases
[2]: https://www.braze.com/docs/developer_guide/sdk_integration?sdktab=unity

## 연락처 {#contact}

질문이 있으시면 [support@braze.com](mailto:support@braze.com)으로 문의해 주세요.
<!-- END GENERATED README CONTENT -->

리포지토리 세부 정보 및 샘플 프로젝트는 [https://github.com/braze-inc/braze-unity-sdk](https://github.com/braze-inc/braze-unity-sdk)를 참조하세요.