import copy
import pytest
import os
import cheese
import animals

# ---------------------------------------------------
# Fixture: Fake home directory with patched expanduser
# ---------------------------------------------------
@pytest.fixture
def fake_home(tmp_path, monkeypatch):
    """
    Create a temporary fake home directory for testing.
    Patch os.path.expanduser in both cheese and animals modules
    so that all file operations point to this temporary directory.
    This avoids writing to the real home directory.
    """
    fake_home_dir = tmp_path / "home"
    fake_home_dir.mkdir()

    # Patch expanduser to redirect "~" to fake home
    monkeypatch.setattr(
        cheese.os.path, 'expanduser',
        lambda x: str(x.replace('~', str(fake_home_dir)))
    )
    monkeypatch.setattr(
        animals.os.path, 'expanduser',
        lambda x: str(x.replace('~', str(fake_home_dir)))
    )

    return fake_home_dir

# ---------------------------------------------------
# 1️⃣ Test: Real home directory
# ---------------------------------------------------
def test_def_pref_real_home():
    """
    This test uses the actual home directory.
    ⚠️ WARNING: Writing here will modify ~/.cheese.json and ~/animals.json!
    Only run if you are okay with affecting your real data.
    """
    # Write default cheese preferences to real home
    cheese.write_default_cheese_preferences()
    expected_cheese = cheese._default_prefs
    actual_cheese = cheese.read_cheese_preferences()
    assert actual_cheese == expected_cheese

    # Write default animal preferences to real home
    animals.write_default_animals_preferences()
    expected_animals = animals._default_animals
    actual_animals = animals.read_animals_preferences()
    assert actual_animals == expected_animals

# ---------------------------------------------------
# 2️⃣ Test: Fake home via HOME environment variable
# ---------------------------------------------------
def test_def_pref_home_env(tmp_path, monkeypatch):
    """
    This test patches the HOME environment variable.
    ⚠️ OS-dependent: Works reliably on Linux/macOS, may fail on Windows.
    """
    # Create a fake home directory
    fake_home_dir = tmp_path / "home"
    fake_home_dir.mkdir()

    # Patch HOME so "~" resolves to fake home
    monkeypatch.setenv("HOME", str(fake_home_dir))

    # Write defaults into fake home
    cheese.write_default_cheese_preferences()
    animals.write_default_animals_preferences()

    # Assertions: Read back defaults and check equality
    actual_cheese = cheese.read_cheese_preferences()
    actual_animals = animals.read_animals_preferences()
    assert actual_cheese == cheese._default_prefs
    assert actual_animals == animals._default_animals

# ---------------------------------------------------
# 3️⃣ Test: Fake home via patching os.path.expanduser (recommended)
# ---------------------------------------------------
def test_def_pref_fake_home(fake_home):
    """
    Safest cross-platform approach: patch os.path.expanduser.
    Now "~" will point to our fake_home, so no real files are touched.
    """
    # Write defaults into fake home
    cheese.write_default_cheese_preferences()
    animals.write_default_animals_preferences()

    # Read back defaults and assert equality
    actual_cheese = cheese.read_cheese_preferences()
    expected_cheese = cheese._default_prefs
    assert actual_cheese == expected_cheese

    actual_animals = animals.read_animals_preferences()
    expected_animals = animals._default_animals
    assert actual_animals == expected_animals

# ---------------------------------------------------
# 4️⃣ Test: Modify defaults and verify persistence
# ---------------------------------------------------
def test_def_pref_change_defaults(fake_home, monkeypatch):
    """
    Test that modified defaults are written and read correctly.
    This includes both cheese and animals, and adds new animal families.
    """
    # -----------------------------
    # Step 1: Write initial defaults
    # -----------------------------
    cheese.write_default_cheese_preferences()
    animals.write_default_animals_preferences()

    # Snapshot the initial defaults
    cheese_def_before = copy.deepcopy(cheese._default_prefs)
    animals_def_before = copy.deepcopy(animals._default_animals)

    # -----------------------------
    # Step 2: Modify defaults
    # -----------------------------
    # Change cheese defaults
    monkeypatch.setitem(cheese._default_prefs, 'salads', ['pepper jack'])
    monkeypatch.setitem(cheese._default_prefs, 'spreadable', ['brie'])

    # Add new animal families
    monkeypatch.setitem(animals._default_animals, 'lion_family', ['african lion', 'asiatic lion'])
    monkeypatch.setitem(animals._default_animals, 'wolf_family', ['gray wolf', 'arctic wolf'])

    # Save snapshots of modified defaults
    cheese_def_modified = cheese._default_prefs
    animals_def_modified = animals._default_animals

    # -----------------------------
    # Step 3: Write modified defaults to fake home
    # -----------------------------
    cheese.write_default_cheese_preferences()
    animals.write_default_animals_preferences()

    # -----------------------------
    # Step 4: Read back and assert
    # -----------------------------
    actual_cheese = cheese.read_cheese_preferences()
    actual_animals = animals.read_animals_preferences()

    # Cheese assertions
    assert actual_cheese == cheese_def_modified
    assert actual_cheese != cheese_def_before

    # Animals assertions
    assert actual_animals == animals_def_modified
    assert actual_animals != animals_def_before

    # -----------------------------
    # Step 5: Optional check - JSON files exist
    # -----------------------------
    assert (fake_home / ".cheese.json").exists()
    assert (fake_home / "animals.json").exists()
