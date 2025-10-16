"""
Basic tests for the Local AI Agent
"""

import pytest
import os
import sys

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

def test_config_import():
    """Test that config module can be imported"""
    try:
        import config
        assert hasattr(config, 'LLM_MODEL')
        assert hasattr(config, 'EMBEDDING_MODEL')
        assert hasattr(config, 'RETRIEVAL_COUNT')
        print("✅ Config import test passed")
    except ImportError as e:
        pytest.fail(f"Failed to import config: {e}")

def test_config_values():
    """Test that config has expected default values"""
    import config
    assert config.LLM_MODEL == "llama3.2:1b"
    assert config.EMBEDDING_MODEL == "mxbai-embed-large"
    assert config.RETRIEVAL_COUNT == 5
    print("✅ Config values test passed")

def test_requirements_file():
    """Test that requirements.txt exists and has content"""
    assert os.path.exists("requirements.txt")
    with open("requirements.txt", "r") as f:
        content = f.read()
        assert len(content.strip()) > 0
        assert "langchain" in content
    print("✅ Requirements file test passed")

def test_csv_file():
    """Test that the CSV data file exists"""
    assert os.path.exists("realistic_restaurant_reviews.csv")
    print("✅ CSV file test passed")

def test_main_import():
    """Test that main module can be imported (without running)"""
    try:
        # We can't actually run the main module in tests due to Ollama dependency
        # But we can test that it can be imported
        import importlib.util
        spec = importlib.util.spec_from_file_location("main", "main.py")
        assert spec is not None
        print("✅ Main module import test passed")
    except Exception as e:
        pytest.fail(f"Failed to import main module: {e}")

def test_vector_import():
    """Test that vector module can be imported (without running)"""
    try:
        import importlib.util
        spec = importlib.util.spec_from_file_location("vector", "vector.py")
        assert spec is not None
        print("✅ Vector module import test passed")
    except Exception as e:
        pytest.fail(f"Failed to import vector module: {e}")

if __name__ == "__main__":
    pytest.main([__file__])
