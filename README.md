# Global Energy Is Not Conserved in an FRW Universe

**An Open Dossier — a verification-instrumented, AI-assisted *reproduction* of an established general-relativity result.**
*Don't trust this paper — run it.*
Irfan Ali-Khan · Independent Researcher

### 📖 Live preview (work in progress)
> **This dossier is an active draft — not yet released.** Sections, claims, and checks may be incomplete or unresolved. Shared early so the ideas can be read and discussed as they develop.

▶ **[Read the self-explaining edition](https://m4gr4th34.github.io/dossier-energy-not-conserved/paper.html)** · [Interactive edition](https://m4gr4th34.github.io/dossier-energy-not-conserved/) · [Audit trail](https://m4gr4th34.github.io/dossier-energy-not-conserved/dossier.html)

> **⚠ PRE-RELEASE WORKING DRAFT — not a released version.**
> This repository is an in-progress draft for human review. **No version number is asserted, no DOI is minted, and no release/timestamp has been run.** The built surface so far is the **self-explaining edition → [`paper.html`](paper.html)**. The other surfaces (interactive console, audit trail, formal PDF) are unbuilt scaffolds.

### ✦ [Publish your own like this →](https://github.com/m4gr4th34/open-dossier-template/blob/main/GETTING-STARTED.md) — free Open Dossier template

[![claims: verified](https://github.com/m4gr4th34/dossier-energy-not-conserved/actions/workflows/verify.yml/badge.svg)](https://github.com/m4gr4th34/dossier-energy-not-conserved/actions/workflows/verify.yml)

## What this is (and is not)

A single, deliberately tight demonstration: an AI agent, working in public with verification instrumented from the first commit, **reproduces an established result** — *global energy is not conserved in a Friedmann–Robertson–Walker (FRW) universe* — shown three independent ways:

1. The covariant law ∇_μT^{μν}=0 does **not** integrate to a conserved global energy without a timelike Killing vector — and an expanding universe has none.
2. Radiation energy density falls as a⁻⁴ while photon number density falls as a⁻³, so total radiation energy falls as a⁻¹ — energy that goes nowhere.
3. The cosmological-redshift photon-energy budget is the concrete face of (2).

**The object of study is the *process*, not the physics.** Every physics claim is labeled **established-reproduced** — nothing here is novel physics, and **no reliability claim is made** about AI-assisted derivation. The method's value proposition — that public, instrumented, AI-assisted derivation surfaces and corrects errors fast — is stated as the experiment's **hypothesis**, evidenced by this repository's own commit history and CI logs, not as a proven conclusion.

## Versioning intent (lineage)

This dossier **versions as a lineage**: **v1 will be the first released milestone** (the AI reproduction of established energy non-conservation), with each later version frozen and citable at its own DOI under a shared concept DOI. *No released version exists yet — this is the pre-release working draft.*

## Companion dossier

**Companion dossier: UAP propulsion** (repo: [`dossier-UAP-propulsion`](https://github.com/m4gr4th34/dossier-UAP-propulsion)) — DOI: **[TO BE LINKED ON RELEASE]**. Distinct research lineages live in separate repos; where they cross-pollinate they cross-cite by DOI, never merged.

## The primary evidence: the build trail

Because the experiment is the process, the **commit history** (granular, never squashed or rebased) and the **CI run logs** ([Actions](https://github.com/m4gr4th34/dossier-energy-not-conserved/actions)) are the primary evidence. The written process narrative in `paper.html` is a faithful summary that points at those commits and runs — it is not the evidence itself.

## Run it

```bash
python3 verification/verify_numbers.py
```

CI runs this on every push (`.github/workflows/verify.yml`). The badge above is the paper's numbers reproducing, continuously.

## Related established work (not claimed here)

Out of scope by design, mentioned only as established context: the cosmological constant Λ, quasilocal energy (Brown–York / Wang–Yau), ADM and Bondi–Sachs mass, unimodular energy-diffusion, and brane-bulk energy exchange.

## License

Paper and prose: CC BY 4.0 · Code: MIT. See [`LICENSE.md`](LICENSE.md).
