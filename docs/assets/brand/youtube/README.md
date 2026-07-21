# TMCO Consulting YouTube assets

These deterministic vector assets extend the repository's authorized TMCO Consulting mark and
Provifact color system. No third-party trademark or generated stock image is included.

| Asset | Size | Use |
| --- | --- | --- |
| `tmco-youtube-avatar.svg` / `.png` | 800×800 | TMCO Consulting channel profile image |
| `tmco-youtube-banner.svg` / `.png` | 2560×1440 | Channel banner; essential content is inside the centered 1235×338 safe region |

The source design uses only repository-native vector shapes, colors, and generic system-font
fallbacks. TMCO Consulting, LLC owns the company identity and has authorized its use in this
project. Provifact™ is a trademark of TMCO Consulting, LLC.

## Design tokens and accessibility

- Palette: deep navy `#07111F`, navy `#0B1F37`, teal `#2DD4BF`, proof blue `#55A7FF`, light text
  `#F3F8FD`, and secondary blue `#8DB9E8` / `#B9CBE0`.
- Typeface: `Inter, Arial, sans-serif`; exports use only SVG text and system fallbacks, with no
  bundled font license.
- Banner alt text: “TMCO Consulting — Modern Workplace, Security, and AI. Provifact: From approved
  change to audit-ready proof.”
- Avatar alt text: “TMCO Consulting T mark on a dark navy field with a teal-to-blue border.”

## Banner safe-area map

```text
2560 × 1440 full image
┌────────────────────────────────────────────────────────────┐
│ television/background crop area                            │
│          ┌──────────────────────────────────────┐          │
│          │ 1235 × 338 centered safe region      │          │
│          │ mark · company · services · product  │          │
│          └──────────────────────────────────────┘          │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

In the SVG, that safe region starts at x=662.5, y=551. All essential mark and text content is
inside it. The 2.1 MB banner PNG is below YouTube's 6 MB banner limit; the avatar PNG is below its
15 MB profile-image limit.

Before upload, visually inspect the PNG files at desktop, mobile, and television crops. YouTube's
current format and size limits are recorded in the [publishing runbook](../../../build-week/youtube-publishing-runbook.md)
and [source ledger](../../../build-week/final-source-ledger.md).
