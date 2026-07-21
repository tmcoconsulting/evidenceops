# TMCO Consulting YouTube Publishing Runbook

Use this runbook for the Build Week demonstration video. It describes a safe setup; it does not
claim that a channel, handle, upload, or custom thumbnail already exists.

## Channel setup

1. Sign in to the Google account controlled by TMCO Consulting.
2. In YouTube, create a business/Brand Account channel if one does not already exist. A Brand
   Account supports the company identity and more than one owner or manager.
3. Channel name: **TMCO Consulting**.
4. Suggested handle: `@tmcoconsulting`, only if YouTube shows it as available. Otherwise choose a
   close company-controlled variant; do not imply availability in public copy.
5. Description:

   > TMCO Consulting, LLC helps organizations modernize endpoint management, cloud identity,
   > security, and AI adoption. Provifact™ turns approved endpoint change into audit-ready proof
   > through read-only observation, deterministic evidence, privacy-safe publication, and bounded
   > AI explanation. https://tmcoconsulting.com

6. Add `https://tmcoconsulting.com` and `https://provifact.tmcoconsulting.com` as channel links.
7. Upload the repository-provided profile and banner assets from
   `docs/assets/brand/youtube/`. Verify their safe-area crop on desktop, mobile, and television.
8. Record channel owner/manager access privately. Do not expose Google account details in Git or
   the video, and do not create another channel if the intended business channel already exists.

## Upload the Build Week video

1. In YouTube Studio choose **Create → Upload videos**.
2. Upload the reviewed MP4. The video must be under three minutes.
3. Recommended title:

   > Provifact™ — From Approved Change to Audit-Ready Proof | OpenAI Build Week

4. Recommended description:

   > Provifact™ by TMCO Consulting connects a Git-approved macOS baseline to GET-only Microsoft
   > Intune collection, deterministic drift, sanitized evidence publication, and bounded GPT-5.6
   > Terra explanation. Deterministic evidence remains authoritative; AI-generated prose is
   > verified, labeled, and subject to human review. Provifact performs no Intune writes and does
   > not decide organizational compliance.
   >
   > Live project: https://provifact.tmcoconsulting.com/
   > Source: https://github.com/tmcoconsulting/provifact
   > Judge path: https://provifact.tmcoconsulting.com/judge-guide/
   >
   > Built for OpenAI Build Week in the Developer Tools category using Codex and GPT-5.6 Terra.

5. Select **Not made for kids** if TJ confirms this business-software demonstration is general
   audience content.
6. Upload `docs/assets/images/provifact-social-card.png` as the custom thumbnail after account
   verification. Do not use a third-party mark or unlicensed music.
7. Select **Public**. Host guidance has said unlisted is acceptable, but the official rules say
   publicly visible; Public is the safest choice.
8. Wait for HD processing. Test playback, audio, title, description, and URL signed out/incognito.
9. Paste the final YouTube URL into Devpost. Do not mark the upload task complete until the video is
   playable without account access.

## Official constraints

- YouTube titles allow up to 100 characters; descriptions up to 5,000.
- Recommended banner size is 2560×1440; minimum is 2048×1152 at 16:9, with a centered 1235×338
  minimum-size safe region and a 6 MB maximum.
- Profile images may be JPG, GIF, BMP, or PNG, must not use animated GIF, and have a 15 MB maximum.
- Custom thumbnails require account verification. A video shorter than three minutes does not need
  the entitlement for uploads longer than 15 minutes.

See the [source ledger](final-source-ledger.md) for the official YouTube Help links.
