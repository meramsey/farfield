import pytest

from tests.support import load_preset, preset_metadata

BEST_EFFORT = [
    "focus-11-gamma-pink", "focus-11-gamma-theta-pink", "focus-11-older-flac",
]


@pytest.mark.parametrize("name", BEST_EFFORT)
def test_best_effort_tier_and_no_emerge(name):
    session = load_preset(name)
    assert session.fidelity == "best-effort"
    assert session.emerge is None


@pytest.mark.parametrize("name", BEST_EFFORT)
def test_best_effort_says_so_in_title_and_notes(name):
    session = load_preset(name)
    notes = session.notes.lower()
    assert "unverified" in session.title.lower()
    assert "best-effort" in notes and "unverified" in notes


@pytest.mark.parametrize("name", ["focus-11-gamma-pink", "focus-11-older-flac"])
def test_best_effort_disclaims_farfield_measurement(name):
    assert "farfield has not re-measured" in load_preset(name).notes.lower()


def test_theta_variant_discloses_its_arrangement():
    notes = load_preset("focus-11-gamma-theta-pink").notes.lower()
    assert "intermittent" in notes and "design choice" in notes


def test_library_titles_are_unique():
    titles = [e["title"] for e in preset_metadata()]
    assert len(titles) == len(set(titles))
