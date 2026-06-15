#!/usr/bin/env python3
"""
verify_numbers.py — executable checks for

    "Global energy is not conserved in an FRW universe"
    (an AI-reproduced ESTABLISHED result; PRE-RELEASE WORKING DRAFT)

Every check below recomputes a number that appears in paper.html from its
stated assumptions. CI runs this on every push (.github/workflows/verify.yml);
a nonzero exit turns the badge red. The contract: fix the paper, never widen a
tolerance to pass. Each NUM check id matches the Stage-1 claim ledger.

These reproduce textbook results (Carroll, Lecture Notes on GR, 1997). Nothing
here is novel physics; the object of study is the verification *process*.

Run locally:  python3 verification/verify_numbers.py
"""

from fractions import Fraction
import sys

PASS, FAIL = "PASS", "FAIL"
results = []


def check(label, computed, claimed_lo, claimed_hi, fmt="{:.6g}"):
    ok = claimed_lo <= computed <= claimed_hi
    status = PASS if ok else FAIL
    results.append((status, label, computed, (claimed_lo, claimed_hi)))
    symbol = "✓" if ok else "✗"
    print(f"[{status}] {symbol} {label}")
    print(f"       computed={fmt.format(computed)}  "
          f"claimed=[{fmt.format(claimed_lo)}, {fmt.format(claimed_hi)}]")
    return ok


print("=" * 72)
print("VERIFICATION — Global energy is not conserved in an FRW universe")
print("ESTABLISHED-REPRODUCED · PRE-RELEASE WORKING DRAFT")
print("=" * 72)

# --- Leg 2: the energy bookkeeping -------------------------------------
# Continuity in FRW gives rho ∝ a^{-3(1+w)} (Carroll LNGR eq 8.23).
# The exponent is d ln(rho)/d ln(a) = -3(1+w).

def density_exponent(w):
    return float(-3 * (1 + Fraction(w).limit_denominator()))

# N01 — radiation (w = 1/3): rho_rad ∝ a^{-4}  (Carroll eq 8.27, 8.28)
exp_rad = density_exponent(Fraction(1, 3))
check("N01 LEG2: radiation density exponent -3(1+w), w=1/3, equals -4",
      exp_rad, -4.0 - 1e-9, -4.0 + 1e-9)

# N02 — photon number density ∝ a^{-3} (comoving photon number conserved):
# total number N = n * V is constant, V ∝ a^3, so n ∝ a^{-3}, exponent -3.
exp_number = -3.0  # = -(spatial volume exponent)
check("N02 LEG2: photon number-density exponent equals -3",
      exp_number, -3.0 - 1e-9, -3.0 + 1e-9)

# N03 — total radiation energy in a fixed comoving volume (V ∝ a^3):
# E_rad,tot = rho_rad * V  ⇒  exponent = exp_rad + 3 = -1.  Energy "goes nowhere".
exp_total_rad_energy = exp_rad + 3.0
check("N03 LEG2 (crux): total radiation energy in comoving volume scales as a^-1",
      exp_total_rad_energy, -1.0 - 1e-9, -1.0 + 1e-9)

# N05 — consistency: a^-4 decomposes as (number a^-3) x (per-photon redshift a^-1).
# Carroll eq 8.28: "number density ... decreases ... as a^-3 ... individual
# photons also lose energy as a^-1 as they redshift."
exp_photon_energy = -1.0  # per-photon energy E ∝ 1/a (redshift)
exp_rad_from_parts = exp_number + exp_photon_energy
check("N05 consistency: rho_rad exponent = number(-3) + redshift(-1) = -4",
      exp_rad_from_parts, exp_rad - 1e-9, exp_rad + 1e-9)

# --- Leg 3: the cosmological-redshift photon-energy budget --------------
# A photon's energy scales as E ∝ 1/a, so E_obs/E_emit = a_emit/a_obs = 1/(1+z).
# Stated example: CMB last scattering, z* = 1089.80 (Planck 2018, TT,TE,EE+lowE+lensing).
z_star = 1089.80
energy_ratio = 1.0 / (1.0 + z_star)          # fraction of per-photon energy retained
fraction_lost = 1.0 - energy_ratio           # fraction "gone nowhere"

# N04a — energy ratio E_obs/E_emit for the stated example
check("N04 LEG3: CMB photon energy ratio E_obs/E_emit = 1/(1+z*), z*=1089.80",
      energy_ratio, 9.16e-4, 9.18e-4)
# N04b — corresponding fraction of per-photon energy not conserved
check("N04 LEG3: fraction of per-photon energy lost to redshift, z*=1089.80",
      fraction_lost, 0.99905, 0.99911)

# ----------------------------------------------------------------------
print()
n_fail = sum(1 for r in results if r[0] == FAIL)
n_pass = sum(1 for r in results if r[0] == PASS)
print("=" * 72)
print(f"TOTAL: {len(results)} checks · {n_pass} pass · {n_fail} fail")
if n_fail:
    print("FAILURES FOUND — fix the paper, not the tolerances.")
else:
    print("All checks pass — the paper's numbers reproduce.")
print("=" * 72)
sys.exit(1 if n_fail else 0)
