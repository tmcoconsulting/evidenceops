# Mission Control

<div class="mission-shell" data-mission-control aria-busy="true">
  <div class="mission-banner" data-mission-banner role="status" aria-live="polite">
    Loading the fingerprint-verified sanitized evidence package…
  </div>

  <header class="mission-header">
    <div>
      <span class="mission-eyebrow">TMCO Consulting endpoint evidence</span>
      <h2 data-mission-title>Mission Control</h2>
      <p data-mission-subtitle>Validating evidence identity and freshness…</p>
    </div>
    <div class="mission-mode" data-mission-mode>VALIDATING</div>
  </header>

  <nav class="mission-nav" aria-label="Primary product navigation">
    <a href="#overview">Overview</a>
    <a href="#findings">Findings</a>
    <a href="../settings-matrix/">Settings</a>
    <a href="#changes">Changes</a>
    <a href="#evidence">Evidence</a>
  </nav>

  <section id="overview" aria-labelledby="overview-title">
    <div class="mission-section-heading">
      <div>
        <span class="mission-eyebrow">Decision view</span>
        <h2 id="overview-title">What requires attention now</h2>
        <p>Technical findings are deterministic. Select an item for its complete public-safe evidence chain.</p>
      </div>
    </div>
    <div class="mission-metrics" data-mission-metrics></div>
    <p class="mission-denominator" data-mission-denominator></p>
    <div class="mission-attention-list" data-attention-list></div>
  </section>

  <section id="changes" aria-labelledby="changes-title">
    <div class="mission-section-heading">
      <div>
        <span class="mission-eyebrow">Current versus prior sanitized snapshot</span>
        <h2 id="changes-title">What changed</h2>
      </div>
      <span class="mission-count" data-change-count></span>
    </div>
    <div class="mission-summary-grid">
      <article class="mission-panel">
        <h3>Resolved findings</h3>
        <div data-resolved-changes></div>
      </article>
      <article class="mission-panel">
        <h3>New drift</h3>
        <div data-new-changes></div>
      </article>
      <article class="mission-panel">
        <h3>Comparison provenance</h3>
        <dl data-change-summary></dl>
      </article>
    </div>
  </section>

  <section id="findings" aria-labelledby="findings-title">
    <div class="mission-section-heading">
      <div>
        <span class="mission-eyebrow">Deterministic comparison</span>
        <h2 id="findings-title">Current findings requiring review</h2>
        <p>Filters use only the validated package. Opening a row exposes the source evidence and fingerprint.</p>
      </div>
      <span class="mission-count" data-finding-count></span>
    </div>
    <div class="mission-filters" aria-label="Finding filters">
      <label>Platform <select data-filter-platform><option value="">All</option></select></label>
      <label>State <select data-filter-drift><option value="">All</option></select></label>
      <label>Severity <select data-filter-severity><option value="">All</option></select></label>
      <label>Setting category <select data-filter-category><option value="">All</option></select></label>
      <button type="button" data-clear-filters>Clear filters</button>
    </div>
    <div class="mission-table-wrap">
      <table class="mission-table">
        <thead>
          <tr><th>Setting</th><th>State</th><th>Severity</th><th>Observed → target</th><th>Assignment</th></tr>
        </thead>
        <tbody data-finding-rows></tbody>
      </table>
    </div>
    <div class="mission-empty" data-finding-empty hidden>No findings match these filters.</div>
  </section>

  <section id="settings" aria-labelledby="settings-title">
    <div class="mission-section-heading">
      <div>
        <span class="mission-eyebrow">Approved desired state</span>
        <h2 id="settings-title">Review every evaluated setting</h2>
        <p>The compact matrix joins exact provider definitions to observed values, targets, assignments, framework references, and read-only operator guidance.</p>
      </div>
      <a class="md-button md-button--primary" href="../settings-matrix/">Open Settings</a>
    </div>
  </section>

  <section id="posture" aria-labelledby="posture-title">
    <h2 id="posture-title">Managed Apple posture</h2>
    <div class="mission-summary-grid">
      <article class="mission-panel">
        <h3>Aggregate device posture</h3>
        <div data-device-summary></div>
      </article>
      <div data-platform-summary></div>
    </div>
  </section>

  <section id="coverage" aria-labelledby="coverage-title">
    <h2 id="coverage-title">Coverage and blind spots</h2>
    <h3>Collected resources not currently evaluated</h3>
    <p>
      Resources are grouped by the explicit reason in the evidence package. Inventory-only records
      do not require a baseline action; mapping and parser gaps do. Assignment expansion records are
      grouped under their public-safe parent resource where the package provides that link.
    </p>
    <div class="mission-resource-list" data-unevaluated-groups></div>

    <h3>Framework cross-references</h3>
    <div class="mission-callout">
      Counts are distinct identifiers referenced by evaluated settings. They are not passed controls,
      framework coverage scores, certifications, or completed assessments.
    </div>
    <div class="mission-table-wrap">
      <table class="mission-table mission-framework-table">
        <thead><tr><th>Framework</th><th>Evaluated settings</th><th>Referenced identifiers</th><th>Aligned</th><th>Drifting</th><th>Meaning</th></tr></thead>
        <tbody data-framework-summary></tbody>
      </table>
    </div>

  </section>

  <section id="evidence" aria-labelledby="evidence-title">
    <h2 id="evidence-title">Evidence, collection health, and privacy</h2>
    <div class="mission-summary-grid">
      <article class="mission-panel">
        <h3>Approved baseline</h3>
        <dl data-baseline-summary></dl>
      </article>
      <article class="mission-panel" id="collection-health">
        <h3>Collection health</h3>
        <div data-endpoint-coverage></div>
        <div data-collection-gaps></div>
      </article>
      <article class="mission-panel">
        <h3>Privacy and publication gate</h3>
        <dl data-privacy-summary></dl>
      </article>
    </div>
  </section>

  <details class="mission-methodology">
    <summary>Methodology and authority boundary</summary>
    <p>
      Git revert changes reviewed desired-state history; it does not revert Intune. EvidenceOps has
      no Intune write capability. Technical configuration may support an assessment objective but
      cannot establish organizational compliance. Human assessors retain final judgment.
    </p>
    <p><a href="../audit-methodology/">Read the deterministic audit methodology</a> · <a href="../data-handling/">Review data handling</a></p>
  </details>

  <dialog class="mission-dialog" data-finding-dialog aria-labelledby="finding-dialog-title">
    <form method="dialog"><button class="mission-dialog-close" aria-label="Close finding detail">Close</button></form>
    <div data-finding-detail></div>
  </dialog>
</div>

<noscript>
  Mission Control requires JavaScript to render the deterministic JSON artifact. The raw public-safe
  package remains available at <code>/assets/data/mission-control.json</code>.
</noscript>
