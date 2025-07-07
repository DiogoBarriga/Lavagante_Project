# 🔧 LAVAGANTE v1.4 - TROUBLESHOOTING GUIDE

## Common Issues and Solutions

### Installation Issues

#### Issue: Python dependencies fail to install
**Solution:**
```bash
# Upgrade pip first
py -m pip install --upgrade pip

# Install dependencies with specific Python version
py -3.8 -m pip install -r requirements.txt

# For Windows users with compilation issues
py -m pip install --only-binary=all -r requirements.txt
```

#### Issue: Missing Microsoft Visual C++ tools
**Solution:**
1. Install Microsoft Visual C++ Build Tools
2. Or install Visual Studio Community with C++ support
3. Restart command prompt and retry installation

### Runtime Issues

#### Issue: Import errors for core modules
**Solution:**
```python
# Add src directory to Python path
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent / "src"))
```

#### Issue: API connection failures
**Solution:**
1. Check internet connection
2. Verify API keys in environment variables
3. Check if you're using testnet vs mainnet settings
```bash
# Set environment variables
set BINANCE_API_KEY=your_api_key
set BINANCE_SECRET_KEY=your_secret_key
set BINANCE_TESTNET=true
```

#### Issue: Memory errors during analysis
**Solution:**
```python
# Use memory optimization
from optimizations.memory_optimizer import MemoryOptimizer
optimizer = MemoryOptimizer()
optimizer.optimize_dataframe(your_dataframe)
```

### Performance Issues

#### Issue: Slow pattern analysis
**Solution:**
1. Reduce data timeframe for testing
2. Use performance optimizations:
```python
# Enable caching
from optimizations.db_api_optimizer import DatabaseOptimizer
db_opt = DatabaseOptimizer()
db_opt.enable_caching()
```

#### Issue: High memory usage
**Solution:**
1. Monitor memory usage:
```python
from optimizations.memory_optimizer import MemoryOptimizer
memory_opt = MemoryOptimizer()
print(memory_opt.get_memory_usage())
```
2. Use chunked processing for large datasets
3. Clear caches periodically

### Security Issues

#### Issue: Input validation errors
**Solution:**
```python
# Use proper input validation
from security.input_validator_optimized import get_validator
validator = get_validator()
try:
    safe_input = validator.validate_string_input(user_input, "field_name")
except Exception as e:
    print(f"Invalid input: {e}")
```

### Configuration Issues

#### Issue: Configuration not loading
**Solution:**
1. Check config file exists in `config/` directory
2. Verify JSON syntax:
```bash
py -c "import json; json.load(open('config/security_config.json'))"
```

### Testing Issues

#### Issue: Tests failing to run
**Solution:**
```bash
# Run tests with proper Python path
py -m pytest tests/ -v

# Or use the comprehensive test runner
py run_comprehensive_tests.py

# Or run validation tests
py tests/validation/test_core_system_validation.py
```

### Phase 4 Quality Assurance Issues

#### Issue: Static analysis tools not working
**Solution:**
```bash
# Install required tools
py -m pip install bandit pylint flake8

# Run individual tools
py -m bandit -r src/
py -m flake8 src/ --max-line-length=100
py -m pylint src/
```

#### Issue: Test organization problems
**Solution:**
```bash
# Run test analysis
py analyze_tests_fixed.py

# Run comprehensive test runner
py run_comprehensive_tests.py

# Validate Phase 4 completion
py validate_phase4.py
```

### Log Analysis
Check log files in the `logs/` directory for detailed error information:
- `application.log` - General application logs
- `error.log` - Error-specific logs
- `performance.log` - Performance metrics

### Diagnostic Commands

#### System Health Check
```bash
# Check Python environment
py --version
py -m pip list

# Validate core functionality  
py validate_phase4.py

# Run core system validation
py tests/validation/test_core_system_validation.py
```

#### Performance Diagnostics
```bash
# Check memory usage
py -c "from optimizations.memory_optimizer import MemoryOptimizer; print(MemoryOptimizer().get_memory_usage())"

# Profile performance
py profile_performance.py
py analyze_performance.py
```

#### Security Diagnostics
```bash
# Run security analysis
py -m bandit -r src/ -f json -o security_report.json

# Check input validation
py -c "from security.input_validator_optimized import get_validator; print('Security validator working')"
```

### Getting Help
1. Check documentation in `docs/` directory
2. Run validation scripts: `py validate_phase4.py`
3. Check GitHub issues or create a new one
4. Ensure you're using the latest version

### Error Code Reference

#### Common Error Codes
- **VALIDATION_ERROR**: Input validation failed
- **IMPORT_ERROR**: Module import failed
- **MEMORY_ERROR**: Insufficient memory
- **API_ERROR**: External API connection failed
- **CONFIG_ERROR**: Configuration loading failed

#### Resolution Steps
1. **Identify the error code** from logs
2. **Check this guide** for specific solutions
3. **Run diagnostic commands** for more details
4. **Check system requirements** and dependencies
5. **Contact support** if issue persists
