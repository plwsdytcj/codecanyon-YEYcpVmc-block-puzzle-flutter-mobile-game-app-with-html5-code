Android release build checklist

1) Create upload keystore (one‑time)

```
keytool -genkey -v -keystore blockpuzzle-upload.jks -keyalg RSA -keysize 2048 -validity 10000 -alias upload
```

Place the generated `blockpuzzle-upload.jks` under `android/app/`.

2) Create `android/key.properties`

Copy from `android/key.properties.example` and fill:

```
storeFile=app/blockpuzzle-upload.jks
storePassword=YOUR_STORE_PASSWORD
keyAlias=upload
keyPassword=YOUR_KEY_PASSWORD
```

Do NOT commit this file or the `.jks`.

3) Build

```
flutter clean
flutter pub get
flutter build appbundle --release
```

The bundle will be at `build/app/outputs/bundle/release/app-release.aab`.

For a test APK:

```
flutter build apk --release
```

4) Play Console

- Create app entry, upload the `.aab` to an Internal testing track first
- Fill Store listing, Content rating, Data safety, Target audience, Ads declaration, and Privacy policy URL
- After pre-launch checks pass, promote to Production

