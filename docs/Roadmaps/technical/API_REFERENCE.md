# 📚 LAVAGANTE v1.4 - API REFERENCE

## Core System APIs

### Data Fetching API
```python
from data.fetch import DataFetcher

fetcher = DataFetcher()
# Fetch market data with caching
data = fetcher.fetch_data(symbol="BTCUSDT", interval="1h", limit=100)
```

### Security Validation API
```python
from security.input_validator_optimized import get_validator

validator = get_validator()
# Validate string input
safe_string = validator.validate_string_input(user_input, "symbol")
# Validate numeric input
safe_number = validator.validate_numeric_input(user_input, "price")
# Validate HTTPS URL
safe_url = validator.validate_https_url(user_input, "api_endpoint")
```

### Pattern Recognition API
```python
from integrated_pattern_system import IntegratedPatternSystem

pattern_system = IntegratedPatternSystem()
# Analyze market patterns
result = pattern_system.analyze_patterns(
    data_frame, 
    analysis_type="comprehensive",
    session_id="unique_session"
)
```

### Quantum Portfolio API
```python
from quantum_portfolio_consciousness import QuantumPortfolioConsciousness

qpc = QuantumPortfolioConsciousness()
# Analyze portfolio consciousness
result = qpc.analyze_portfolio_consciousness(portfolio_data)
```

### Risk Management API
```python
from advanced_risk_manager import AdvancedRiskManager, RiskConfig, RiskLimits

risk_manager = AdvancedRiskManager(config, limits)
# Comprehensive risk assessment
risk_result = risk_manager.comprehensive_risk_assessment(
    portfolio_data, market_data, positions
)
```

### Optimization APIs
```python
from optimizations.memory_optimizer import MemoryOptimizer
from optimizations.algorithm_optimizer import AlgorithmOptimizer

# Memory optimization
memory_opt = MemoryOptimizer()
memory_info = memory_opt.get_memory_usage()

# Algorithm optimization
algo_opt = AlgorithmOptimizer()
complexity_info = algo_opt.analyze_complexity(code_string)
```

## Configuration APIs

### Environment Configuration
```python
import os

# Required environment variables
BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_SECRET_KEY = os.getenv('BINANCE_SECRET_KEY')
BINANCE_TESTNET = os.getenv('BINANCE_TESTNET', 'true')
```

### Optimization Configuration
```python
from config.optimization_config import OptimizationConfig

config = OptimizationConfig()
# Access optimization settings
memory_threshold = config.memory_threshold
cache_size = config.cache_size
```

## Return Types and Data Structures

### Analysis Results
```python
{
    'status': 'success' | 'error',
    'data': {
        'patterns': [...],
        'signals': {...},
        'risk_metrics': {...}
    },
    'metadata': {
        'session_id': str,
        'timestamp': datetime,
        'processing_time': float
    }
}
```

### Error Handling
All APIs use consistent error handling with proper exception types and detailed error messages.

## Testing and Validation APIs

### Core System Validation
```python
from tests.validation.test_core_system_validation import run_core_validation

# Run comprehensive system validation
success = run_core_validation()
```

### Quality Assurance
```python
from src.testing.test_qa_system import run_quality_analysis

# Run code quality analysis
results = run_quality_analysis(".")
```

### Performance Optimization
```python
from optimizations.memory_optimizer import MemoryOptimizer
from optimizations.db_api_optimizer import DatabaseOptimizer

# Memory optimization
memory_opt = MemoryOptimizer()
optimized_df = memory_opt.optimize_dataframe(dataframe)

# Database optimization
db_opt = DatabaseOptimizer()
db_opt.create_connection_pool()
```
